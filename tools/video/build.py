"""Génère un épisode vidéo animé à partir d'un module de scènes (dossier episodes/).

Usage : python build.py <module_episode> [dossier_sortie]
Étapes : voix (edge-tts, mise en cache) -> repères au mot près -> page HTML de l'épisode ->
capture image par image en parallèle -> piste audio -> MP4 avec sous-titres incrustés et pistes SRT/VTT.
"""
import asyncio
import hashlib
import html
import importlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import edge_tts
import imageio_ffmpeg

HERE = Path(__file__).resolve().parent
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
NODE = os.environ.get("NODE_EXE") or shutil.which("node") or "node"
VOICES = {"main": ("fr-FR-VivienneMultilingualNeural", "-3%"), "max": ("fr-FR-RemyMultilingualNeural", "+0%")}
FPS = 30
WORKERS = 1
SCENE_LEAD_S = 1.0      # la voix démarre après la transition d'entrée
SEGMENT_GAP_S = 0.35
SCENE_TAIL_S = 0.9
CAPTION_MAX_WORDS = 15
CAPTION_MAX_CHARS = 84
TICKS = 10_000_000
MARKER = re.compile(r"\{#([\w.]+)\}")
CUE_ATTRS = re.compile(r'data-(?:in|out|type|until|stream|glow|count|countdown|good|bad|dim)="([^"]+)"')


def run(args, **kwargs):
    return subprocess.run(args, check=True, **kwargs)


def duration_of(path):
    probe = subprocess.run([FFMPEG, "-i", str(path)], capture_output=True, text=True, encoding="utf-8", errors="replace")
    h, m, s = re.search(r"Duration: (\d+):(\d+):(\d+\.\d+)", probe.stderr).groups()
    return int(h) * 3600 + int(m) * 60 + float(s)


def split_markers(text):
    plain, marks = "", {}
    for part in re.split(r"(\{#[\w.]+\})", text):
        match = MARKER.fullmatch(part)
        if match:
            marks[match.group(1)] = len(plain)
        else:
            plain += part
    return plain.replace("’", "'"), marks


async def tts(text, voice_key, mp3):
    voice, rate = VOICES[voice_key]
    words = []
    communicate = edge_tts.Communicate(text, voice, rate=rate, boundary="WordBoundary")
    with open(mp3, "wb") as out:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                out.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                words.append([chunk["offset"] / TICKS, (chunk["offset"] + chunk["duration"]) / TICKS, chunk["text"]])
    return words


def speak(text, voice_key, cache):
    """Synthèse mise en cache : relancer un épisode ne refait que les phrases modifiées."""
    key = hashlib.sha1(f"{VOICES[voice_key]}|{text}".encode("utf-8")).hexdigest()[:16]
    mp3, meta = cache / f"{key}.mp3", cache / f"{key}.json"
    if not (mp3.exists() and meta.exists()):
        for attempt in range(5):
            try:
                words = asyncio.run(tts(text, voice_key, mp3))
                break
            except Exception:  # service vocal momentanément indisponible : nouvel essai après une pause
                if attempt == 4:
                    raise
                time.sleep(5 * (attempt + 1))
        meta.write_text(json.dumps({"words": words, "duration": duration_of(mp3)}), encoding="utf-8")
    data = json.loads(meta.read_text(encoding="utf-8"))
    return mp3, data["words"], data["duration"]


def align(plain, words):
    """Position de chaque mot prononcé dans le texte écrit."""
    out, cursor = [], 0
    for start, end, word in words:
        found = plain.find(word, cursor)
        if found < 0:
            continue
        out.append((found, start, end, word))
        cursor = found + len(word)
    return out


def captions_for(plain, placed, offset, prefix):
    """Découpe en sous-titres courts, coupés après une ponctuation forte ou à la longueur maximale."""
    chunks, current = [], []
    for i, (pos, start, end, word) in enumerate(placed):
        current.append((pos, start, end, word))
        after = plain[pos + len(word): pos + len(word) + 2]
        text_len = sum(len(w[3]) + 1 for w in current)
        sentence_end = re.match(r"\s*[.?!…]", after) and len(current) >= 4
        if sentence_end or len(current) >= CAPTION_MAX_WORDS or text_len >= CAPTION_MAX_CHARS or i == len(placed) - 1:
            chunks.append(current)
            current = []
    out = []
    for chunk in chunks:
        first, last = chunk[0][0], chunk[-1][0] + len(chunk[-1][3])
        while last < len(plain) and plain[last] in ".,;:!?…»)":
            last += 1
        out.append({"start": offset + chunk[0][1], "end": offset + chunk[-1][2] + 0.25, "text": prefix + plain[first:last].strip()})
    return out


def build_timeline(scenes, cache):
    timeline, audio, captions, clock = [], [], [], 0.0
    for index, sc in enumerate(scenes):
        start = clock
        cues = {"start": start + (0.05 if index == 0 else 0.35)}
        t = start + (0.6 if index == 0 else SCENE_LEAD_S)
        for seg in sc["narration"]:
            if isinstance(seg, dict) and "pause" in seg:
                if seg.get("cue"):
                    cues[seg["cue"]] = t
                t += seg["pause"]
                continue
            voice = "max" if isinstance(seg, dict) else "main"
            text = seg["max"] if voice == "max" else seg
            if voice == "max":
                cues.setdefault("max", t)
            plain, marks = split_markers(text)
            mp3, words, length = speak(plain, voice, cache)
            placed = align(plain, words)
            if not placed:
                raise RuntimeError(f"Aucun mot aligné dans la scène {index} : {plain[:60]}")
            for name, at in marks.items():
                hit = next((p for p in placed if p[0] >= at), placed[-1])
                cues[name] = t + hit[1]
            captions += captions_for(plain, placed, t, "Max : " if voice == "max" else "")
            audio.append((mp3, t))
            t += length + SEGMENT_GAP_S
        end = t - SEGMENT_GAP_S + SCENE_TAIL_S
        cues["end"] = end
        timeline.append({"start": start, "end": end, "cues": cues})
        clock = end
    for i in range(len(captions) - 1):
        captions[i]["end"] = min(captions[i]["end"], captions[i + 1]["start"])
    return timeline, audio, captions, clock + 0.8


def check_cues(scenes, timeline):
    for index, (sc, tl) in enumerate(zip(scenes, timeline)):
        for spec in CUE_ATTRS.findall(sc["html"]):
            for part in spec.split(","):
                name = re.match(r"[\w.]+", part.strip()).group(0)
                if name not in tl["cues"]:
                    raise RuntimeError(f"Scène {index} : repère « {name} » absent de la narration (ajoutez {{#{name}}})")


def write_page(meta, scenes, timeline, captions, total, path):
    data = {"scenes": timeline, "captions": captions}
    scene_html = "".join(f'<section class="scene" id="scene-{i}">{sc["html"]}</section>' for i, sc in enumerate(scenes))
    css = (HERE / "theme.css").as_uri()
    js = (HERE / "runtime.js").as_uri()
    path.write_text(f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><link rel="stylesheet" href="{css}"></head>
<body>{scene_html}<div id="caption"></div><div id="progress"></div><div id="brand">{html.escape(meta["brand"])}</div>
<script>window.EPISODE = {json.dumps(data, ensure_ascii=False)}; window.DURATION = {total:.3f};</script>
<script src="{js}"></script></body></html>""", encoding="utf-8")


def capture(page, work, total):
    frames = int(total * FPS)
    bounds = [round(frames * k / WORKERS) for k in range(WORKERS + 1)]
    parts = [work / f"part{k}.mp4" for k in range(WORKERS)]

    def job(k):
        return run([NODE, str(HERE / "capture.js"), str(page), str(parts[k]), str(FPS), FFMPEG, str(bounds[k]), str(bounds[k + 1])],
                   capture_output=True, text=True, encoding="utf-8", errors="replace").stdout.strip()

    with ThreadPoolExecutor(WORKERS) as pool:
        for line in pool.map(job, range(WORKERS)):
            print("  ", line, flush=True)
    listing = work / "parts.txt"
    listing.write_text("".join(f"file '{p.as_posix()}'\n" for p in parts), encoding="utf-8")
    video = work / "video.mp4"
    run([FFMPEG, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(listing), "-c", "copy", str(video)])
    return video


def mix_audio(audio, total, work):
    inputs = ["-f", "lavfi", "-t", f"{total:.3f}", "-i", "anullsrc=r=48000:cl=stereo"]
    chains = ["[0:a]anull[a0]"]
    for n, (mp3, at) in enumerate(audio, 1):
        inputs += ["-i", str(mp3)]
        delay = int(round(at * 1000))
        chains.append(f"[{n}:a]aformat=sample_rates=48000:channel_layouts=stereo,adelay={delay}|{delay}[a{n}]")
    labels = "".join(f"[a{n}]" for n in range(len(audio) + 1))
    chains.append(f"{labels}amix=inputs={len(audio) + 1}:normalize=0:duration=first,loudnorm=I=-16:TP=-1.5:LRA=11,"
                  f"aresample=48000,atrim=0:{total:.3f}[out]")
    script = work / "mix.txt"
    script.write_text(";\n".join(chains), encoding="utf-8")
    wav = work / "voice.wav"
    run([FFMPEG, "-y", "-loglevel", "error", *inputs, "-/filter_complex", str(script), "-map", "[out]", "-c:a", "pcm_s16le", str(wav)])
    return wav


def srt_time(seconds):
    ms = int(round(seconds * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"


def build(module_name, out_dir):
    sys.path.insert(0, str(HERE / "episodes"))
    sys.path.insert(0, str(HERE))
    module = importlib.import_module(module_name)
    meta, scenes = module.META, module.SCENES
    work = HERE / "work" / module_name
    cache = HERE / "work" / "voice-cache"
    work.mkdir(parents=True, exist_ok=True)
    cache.mkdir(parents=True, exist_ok=True)

    timeline, audio, captions, total = build_timeline(scenes, cache)
    check_cues(scenes, timeline)
    print(f"{module_name} : {len(scenes)} scènes, {total / 60:.1f} min", flush=True)
    page = work / "episode.html"
    write_page(meta, scenes, timeline, captions, total, page)
    if "--page-only" in sys.argv:
        return
    page_hash = hashlib.sha1(page.read_bytes() + (HERE / "theme.css").read_bytes() + (HERE / "runtime.js").read_bytes()).hexdigest()
    stamp = work / "video.hash"
    video = work / "video.mp4"
    if video.exists() and stamp.exists() and stamp.read_text() == page_hash:
        print("  capture inchangée : réutilisation", flush=True)
    else:
        video = capture(page, work, total)
        stamp.write_text(page_hash)
    wav = mix_audio(audio, total, work)

    out_dir.mkdir(parents=True, exist_ok=True)
    stem = out_dir / meta["file"]
    srt = stem.with_suffix(".srt")
    srt.write_text("\n".join(f"{i}\n{srt_time(c['start'])} --> {srt_time(c['end'])}\n{c['text']}\n"
                             for i, c in enumerate(captions, 1)), encoding="utf-8")
    run([FFMPEG, "-y", "-loglevel", "error", "-i", str(video), "-i", str(wav), "-map", "0:v", "-map", "1:a", "-c:v", "copy",
         "-c:a", "aac", "-b:a", "192k", "-shortest", "-metadata", f"title={meta['title']}", "-movflags", "+faststart",
         str(stem.with_suffix(".mp4"))])
    run([FFMPEG, "-y", "-loglevel", "error", "-i", str(srt), str(stem.with_suffix(".vtt"))])
    print(f"OK {stem.with_suffix('.mp4')} : {duration_of(stem.with_suffix('.mp4')) / 60:.1f} min", flush=True)


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    build(args[0], Path(args[1]) if len(args) > 1 else HERE / "out")
