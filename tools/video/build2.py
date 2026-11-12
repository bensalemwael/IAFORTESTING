"""Vidéo « réactive » : diapositives dévoilées pas à pas, transitions animées, deux voix, quiz à compte à rebours.

Usage : python build2.py <module_diapositives> <fichier_sortie.mp4>

Chaque diapositive : {section, title, body, steps}. Dans `body`, un élément `data-s="k"` apparaît à l'étape k
et il est surligné pendant cette étape. `{{nom}}` est remplacé par la variable `vars[nom]` de l'étape courante.
Étape : {"say": texte, "voice": "max" (facultatif), "pause": secondes (étape muette), "vars": {...}}.
"""
import asyncio
import html
import re
import importlib
import subprocess
import sys
from pathlib import Path

import edge_tts

from build import CSS as BASE_CSS, FFMPEG, media_duration, render_png, srt_time

HERE = Path(__file__).resolve().parent
VOICES = {"main": ("fr-FR-DeniseNeural", "+4%"), "max": ("fr-FR-HenriNeural", "+2%")}
LEAD_S = 0.5          # silence avant la première phrase d'une diapositive
GAP_S = 0.35          # respiration entre deux étapes
TAIL_S = 0.9          # silence final, doit dépasser la transition entre diapositives
STEP_FADE_S = 0.3     # fondu entre deux étapes d'une même diapositive
SLIDE_FADE_S = 0.6    # transition entre deux diapositives
FPS = 30
TICKS_PER_SECOND = 10_000_000
TRANSITIONS = ["smoothleft", "fade", "slideup", "smoothleft", "wipeleft", "fade"]

CSS = BASE_CSS + """
[data-s] { transition: none; }
.hidden { opacity: 0 !important; transform: translateY(26px); }
.now { box-shadow: 0 0 0 6px rgba(224,138,0,.55), 0 10px 30px rgba(224,138,0,.25) !important; position: relative; }
.speaker { display: inline-block; font-size: 24px; font-weight: 700; color: #fff; background: #7a3fbf; border-radius: 20px; padding: 4px 16px; margin-right: 12px; }
.bubble { background: #f1e9fb; border: 3px solid #b998e3; border-radius: 26px; padding: 22px 30px; font-size: 32px; }
.prompt-card { background: #0f1c3a; color: #e8ecf6; border-radius: 20px; padding: 26px 32px; font-family: Consolas, monospace; font-size: 27px; line-height: 1.5; display: flex; flex-direction: column; gap: 8px; }
.prompt-card .lbl { display: inline-block; min-width: 230px; font-family: "Segoe UI", sans-serif; font-weight: 700; font-size: 22px; padding: 2px 12px; border-radius: 8px; margin-right: 14px; color: #0f1c3a; }
.l1 { background: #9db4ea; } .l2 { background: #8fd1ac; } .l3 { background: #ffd27a; } .l4 { background: #f2a7a2; } .l5 { background: #c7b3ec; } .l6 { background: #a7e0e6; }
.comp { display: grid; grid-template-columns: repeat(3, 1fr); gap: 22px; }
.comp .c { font-size: 28px; padding: 26px; }
.comp .c h3 { font-size: 34px; }
.flow { display: flex; align-items: center; gap: 16px; justify-content: center; }
.flow .st { background: #fff; border-radius: 18px; padding: 22px 26px; box-shadow: 0 6px 24px rgba(19,48,107,.08); font-size: 29px; text-align: center; min-width: 230px; }
.flow .st b { display: block; font-size: 32px; }
.flow .chk { font-size: 26px; color: #17794a; font-weight: 700; text-align: center; }
.flow .ar { font-size: 48px; color: #2456c9; }
.shots { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }
.shots .c { text-align: center; }
.shots .n { font-size: 90px; font-weight: 800; color: #2456c9; line-height: 1; }
.code { font-family: Consolas, monospace; font-size: 25px; background: #f4f6fb; border-radius: 10px; padding: 12px 16px; text-align: left; white-space: pre-wrap; }
.countdown { position: absolute; right: 110px; top: 150px; width: 150px; height: 150px; border-radius: 50%; border: 12px solid #e08a00; color: #e08a00; display: flex; align-items: center; justify-content: center; font-size: 84px; font-weight: 800; background: #fff; }
.countdown:empty { display: none; }
.answer { background: #e2f4ea; border: 3px solid #17794a; border-radius: 18px; padding: 18px 28px; font-size: 32px; }
.answer b { color: #17794a; }
.qa { display: flex; flex-direction: column; gap: 22px; }
.qa .q { font-size: 34px; }
.opts { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }
.opts div { background: #fff; border: 3px solid #d5ddef; border-radius: 16px; padding: 18px 22px; font-size: 30px; text-align: center; }
.opts div.good { border-color: #17794a; background: #e2f4ea; font-weight: 700; }
.metrics { display: grid; grid-template-columns: repeat(4, 1fr); gap: 18px; }
.metrics .c { padding: 22px; font-size: 25px; gap: 8px; }
.metrics .c h3 { font-size: 30px; }
.vs { display: grid; grid-template-columns: 1fr 80px 1fr; gap: 10px; align-items: stretch; }
.vs .mid { display: flex; align-items: center; justify-content: center; font-size: 44px; font-weight: 800; color: #2456c9; }
.tbl3 td:first-child { font-weight: 700; color: #13306b; width: 260px; }
"""


def slide_html(slide, index, total, chapter, step, vars_):
    body = slide["body"]
    for name, value in vars_.items():
        body = body.replace("{{" + name + "}}", value)
    body = re.sub(r"\{\{\w+\}\}", "", body)
    max_step = len(slide["steps"])
    hidden = ", ".join(f'[data-s="{k}"]' for k in range(step + 1, max_step + 1))
    rules = (f"{hidden} {{ opacity: 0 !important; transform: translateY(26px); }}" if hidden else "")
    rules += f' [data-s="{step}"] {{ box-shadow: 0 0 0 6px rgba(224,138,0,.55), 0 10px 30px rgba(224,138,0,.25) !important; }}' if step > 0 else ""
    section = f'<span class="sec">{html.escape(slide["section"])}</span>' if slide["section"] else ""
    title = "" if not slide["title"] else f'<h2>{html.escape(slide["title"])}</h2>'
    count = vars_.get("count", "")
    progress = (index + (step + 1) / max_step) / total * 100
    return f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>{CSS}{rules}</style></head>
<body><div class="frame">
<div class="top"><span class="tag">{html.escape(chapter)}</span>{section}</div>
{title}<div class="content">{body}</div>
<div class="countdown">{html.escape(count)}</div>
<div class="foot">{index + 1} / {total}</div><div class="bar" style="width:{progress:.2f}%"></div>
</div></body></html>"""


async def synthesize(text, voice_key, mp3_path):
    voice, rate = VOICES[voice_key]
    cues = []
    communicate = edge_tts.Communicate(text, voice, rate=rate, boundary="SentenceBoundary")
    with open(mp3_path, "wb") as audio:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio.write(chunk["data"])
            elif chunk["type"] in ("SentenceBoundary", "WordBoundary"):
                start = chunk["offset"] / TICKS_PER_SECOND
                cues.append((start, start + chunk["duration"] / TICKS_PER_SECOND, chunk["text"]))
    return cues


def run(args):
    subprocess.run([FFMPEG, "-y", "-loglevel", "error", *args], check=True)


def build_slide(slide, index, total, chapter, work):
    """Rend les étapes, la voix et le clip vidéo muet d'une diapositive. Renvoie (vidéo, audio, durée, cues)."""
    steps = slide["steps"]
    images, starts, audios, cues = [], [], [], []
    clock = LEAD_S
    for k, step in enumerate(steps):
        stem = work / f"s{index:02}_{k:02}"
        page = stem.with_suffix(".html")
        page.write_text(slide_html(slide, index, total, chapter, k, step.get("vars", {})), encoding="utf-8")
        png = stem.with_suffix(".png")
        render_png(page, png)
        images.append(png)
        starts.append(clock)
        if "say" in step:
            mp3 = stem.with_suffix(".mp3")
            spoken = asyncio.run(synthesize(step["say"], step.get("voice", "main"), mp3))
            length = media_duration(mp3)
            audios.append((mp3, clock))
            prefix = "Max : " if step.get("voice") == "max" else ""
            cues.extend((clock + a, clock + b, prefix + t) for a, b, t in spoken)
            clock += length + GAP_S
        else:
            clock += step["pause"]
    duration = clock - GAP_S + TAIL_S if "say" in steps[-1] else clock + TAIL_S

    video = work / f"slide{index:02}.mp4"
    inputs, lengths = [], []
    for k, png in enumerate(images):
        end = starts[k + 1] if k + 1 < len(images) else duration
        begin = 0 if k == 0 else starts[k] - STEP_FADE_S
        lengths.append(end - begin)
        inputs += ["-loop", "1", "-framerate", str(FPS), "-t", f"{end - begin:.3f}", "-i", str(png)]
    chains = [f"[{k}:v]fps={FPS},format=yuv420p,settb=AVTB[i{k}]" for k in range(len(images))]
    last = "i0"
    for k in range(1, len(images)):
        chains.append(f"[{last}][i{k}]xfade=transition=fade:duration={STEP_FADE_S}:offset={starts[k] - STEP_FADE_S:.3f}[x{k}]")
        last = f"x{k}"
    run([*inputs, "-filter_complex", ";".join(chains), "-map", f"[{last}]", "-t", f"{duration:.3f}",
         "-c:v", "libx264", "-preset", "fast", "-crf", "16", "-r", str(FPS), str(video)])

    audio = work / f"slide{index:02}.wav"
    audio_inputs = ["-f", "lavfi", "-t", f"{duration:.3f}", "-i", "anullsrc=r=48000:cl=stereo"]
    parts = ["[0:a]anull[a0]"]
    for n, (mp3, at) in enumerate(audios, 1):
        audio_inputs += ["-i", str(mp3)]
        delay = int(round(at * 1000))
        parts.append(f"[{n}:a]aformat=sample_rates=48000:channel_layouts=stereo,adelay={delay}|{delay}[a{n}]")
    mix = "".join(f"[a{n}]" for n in range(len(audios) + 1))
    parts.append(f"{mix}amix=inputs={len(audios) + 1}:normalize=0:duration=first,apad,atrim=0:{duration:.3f}[out]")
    run([*audio_inputs, "-filter_complex", ";".join(parts), "-map", "[out]", "-c:a", "pcm_s16le", str(audio)])
    return video, audio, duration, cues


def build(module_name, output):
    sys.path.insert(0, str(HERE))
    module = importlib.import_module(module_name)
    slides, chapter = module.SLIDES, module.CHAPTER
    work = HERE / f"work-{module_name}"
    work.mkdir(exist_ok=True)
    clips, all_cues, offset = [], [], 0.0
    for index, slide in enumerate(slides):
        video, audio, duration, cues = build_slide(slide, index, len(slides), chapter, work)
        clips.append((video, audio, duration))
        all_cues.extend((offset + a, offset + b, t) for a, b, t in cues)
        offset += duration - SLIDE_FADE_S
        print(f"diapositive {index + 1}/{len(slides)} : {duration:.1f} s, {len(slide['steps'])} étapes", flush=True)

    inputs, chains = [], []
    for video, audio, _ in clips:
        inputs += ["-i", str(video), "-i", str(audio)]
    for i in range(len(clips)):
        chains.append(f"[{2 * i}:v]fps={FPS},format=yuv420p,settb=AVTB[v{i}]")
    last, cursor = "v0", 0.0
    for i in range(1, len(clips)):
        cursor += clips[i - 1][2] - SLIDE_FADE_S
        transition = TRANSITIONS[i % len(TRANSITIONS)]
        chains.append(f"[{last}][v{i}]xfade=transition={transition}:duration={SLIDE_FADE_S}:offset={cursor:.3f}[w{i}]")
        last = f"w{i}"
    for i, (_, _, duration) in enumerate(clips):
        keep = duration if i == len(clips) - 1 else duration - SLIDE_FADE_S
        chains.append(f"[{2 * i + 1}:a]atrim=0:{keep:.3f},asetpts=PTS-STARTPTS[a{i}]")
    chains.append("".join(f"[a{i}]" for i in range(len(clips))) + f"concat=n={len(clips)}:v=0:a=1[aout]")
    joined = work / "joined.mp4"
    run([*inputs, "-filter_complex", ";".join(chains), "-map", f"[{last}]", "-map", "[aout]",
         "-c:v", "libx264", "-preset", "medium", "-crf", "21", "-pix_fmt", "yuv420p", "-profile:v", "high", "-c:a", "aac", "-b:a", "160k", "-ar", "48000", str(joined)])

    srt = Path(output).with_suffix(".srt")
    srt.write_text("\n".join(f"{i}\n{srt_time(a)} --> {srt_time(b)}\n{t}\n" for i, (a, b, t) in enumerate(all_cues, 1)),
                   encoding="utf-8")
    run(["-i", str(joined), "-i", str(srt), "-map", "0", "-map", "1", "-c", "copy", "-c:s", "mov_text",
         "-metadata:s:s:0", "language=fre", "-metadata", f"title={chapter}", "-movflags", "+faststart", str(output)])
    run(["-i", str(srt), str(Path(output).with_suffix(".vtt"))])
    print(f"OK {output} : {media_duration(output) / 60:.1f} min, {len(all_cues)} sous-titres")


if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2])
