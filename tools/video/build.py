"""Génère une vidéo MP4 narrée à partir d'une liste de diapositives.

Usage : python build.py <module_diapositives> <fichier_sortie.mp4>
Étapes : HTML -> capture Edge -> voix edge-tts -> segments ffmpeg -> concaténation + sous-titres.
"""
import asyncio
import importlib
import html
import re
import subprocess
import sys
from pathlib import Path

import edge_tts
import imageio_ffmpeg

HERE = Path(__file__).resolve().parent
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
VOICE = "fr-FR-DeniseNeural"
RATE = "-6%"
LEAD_S = 0.6
TAIL_S = 1.1
FADE_S = 0.4
TICKS_PER_SECOND = 10_000_000

CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
html, body { width: 1920px; height: 1080px; overflow: hidden; }
body { font-family: "Segoe UI", system-ui, sans-serif; color: #1c2430; background: #f4f6fb; }
.frame { position: relative; width: 1920px; height: 1080px; padding: 70px 110px 90px; display: flex; flex-direction: column; }
.top { display: flex; justify-content: space-between; align-items: center; margin-bottom: 26px; }
.tag { font-size: 26px; color: #5d6877; font-weight: 600; letter-spacing: .5px; }
.sec { font-size: 26px; background: #2456c9; color: #fff; padding: 6px 20px; border-radius: 30px; font-weight: 700; }
h2 { font-size: 64px; line-height: 1.12; margin-bottom: 36px; color: #13306b; }
.content { flex: 1; display: flex; flex-direction: column; justify-content: center; gap: 30px; font-size: 34px; line-height: 1.4; }
.bar { position: absolute; left: 0; bottom: 0; height: 12px; background: #2456c9; }
.foot { position: absolute; right: 110px; bottom: 30px; font-size: 22px; color: #8a94a3; }
b { color: #13306b; }
.hero { text-align: center; display: flex; flex-direction: column; align-items: center; gap: 26px; }
.hero h1 { font-size: 104px; line-height: 1.05; color: #13306b; }
.kicker { font-size: 34px; color: #2456c9; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; }
.lead { font-size: 42px; color: #33405a; }
.chips { display: flex; gap: 20px; margin-top: 20px; }
.chips span { background: #fff; border: 2px solid #d5ddef; padding: 12px 26px; border-radius: 40px; font-size: 30px; }
.grid { width: 100%; border-collapse: separate; border-spacing: 0; background: #fff; border-radius: 18px; overflow: hidden; box-shadow: 0 6px 24px rgba(19,48,107,.08); font-size: 32px; }
.grid th { background: #13306b; color: #fff; text-align: left; padding: 18px 26px; }
.grid td { padding: 16px 26px; border-top: 1px solid #e6eaf3; vertical-align: top; }
.grid.cmp td:first-child { font-weight: 700; color: #13306b; width: 230px; }
.k1, .k2 { padding: 2px 14px; border-radius: 10px; color: #fff !important; }
.k1 { background: #17794a; } .k2 { background: #2456c9; }
.note { font-size: 30px; color: #5d6877; text-align: center; }
.small { font-size: 24px; color: #8a94a3; } .center { text-align: center; }
.cards4, .cards3 { display: grid; gap: 28px; }
.cards4 { grid-template-columns: repeat(4, 1fr); } .cards3 { grid-template-columns: repeat(3, 1fr); }
.c { background: #fff; border-radius: 22px; padding: 34px 30px; box-shadow: 0 6px 24px rgba(19,48,107,.08); border-top: 8px solid #9db4ea; font-size: 30px; display: flex; flex-direction: column; gap: 14px; }
.c.hl { border-top-color: #e08a00; background: #fff8ec; }
.c h3 { font-size: 38px; color: #13306b; }
.ic { font-size: 64px; } .ic.big { font-size: 110px; }
.ex { font-size: 26px; color: #5d6877; font-style: italic; border-left: 4px solid #d5ddef; padding-left: 14px; }
.split { display: grid; grid-template-columns: 1fr 1fr; gap: 36px; }
.box { background: #fff; border-radius: 22px; padding: 36px 40px; box-shadow: 0 6px 24px rgba(19,48,107,.08); display: flex; flex-direction: column; gap: 16px; }
.box h3 { font-size: 40px; color: #13306b; }
.box.ok { border-left: 10px solid #17794a; } .box.warn { border-left: 10px solid #e08a00; }
ul { padding-left: 40px; display: flex; flex-direction: column; gap: 12px; }
ul.big { font-size: 34px; }
.trap { background: #fff4dc; border: 2px solid #f0c060; border-radius: 18px; padding: 22px 32px; font-size: 32px; }
.tokens { display: flex; justify-content: center; flex-wrap: wrap; gap: 10px; }
.tokens span { white-space: pre; background: #fff; border: 3px solid #2456c9; border-radius: 12px; padding: 14px 18px; font-size: 46px; font-family: Consolas, monospace; color: #13306b; }
.tokens span:nth-child(odd) { background: #e6edfb; }
.map { position: relative; background: #fff; border-radius: 22px; box-shadow: 0 6px 24px rgba(19,48,107,.08); min-height: 520px;
  background-image: linear-gradient(#eef1f7 1px, transparent 1px), linear-gradient(90deg, #eef1f7 1px, transparent 1px); background-size: 60px 60px; }
.dot { position: absolute; background: #2456c9; color: #fff; padding: 8px 18px; border-radius: 30px; font-size: 30px; font-weight: 600; }
.dot.b { background: #17794a; } .dot.c { background: #b3261e; }
.ring { position: absolute; border: 4px dashed #2456c9; border-radius: 50%; }
.predict { display: flex; flex-direction: column; gap: 24px; }
.prompt { background: #13306b; color: #fff; border-radius: 18px; padding: 26px 34px; font-size: 38px; }
.bars { display: flex; flex-direction: column; gap: 16px; }
.bars div { display: grid; grid-template-columns: 220px 1fr 120px; align-items: center; gap: 20px; font-size: 34px; }
.bars i { display: block; height: 40px; background: #2456c9; border-radius: 8px; min-width: 6px; }
.bars em { font-style: normal; color: #5d6877; }
.window { background: #fff; border-radius: 18px; padding: 26px; box-shadow: 0 6px 24px rgba(19,48,107,.08); }
.tape { display: flex; gap: 14px; align-items: center; font-size: 30px; }
.tape .out { flex: 1; color: #aab3c2; border: 3px dashed #d5ddef; padding: 18px; border-radius: 12px; }
.tape .in { flex: 2; background: #e6edfb; border: 4px solid #2456c9; padding: 18px; border-radius: 12px; color: #13306b; font-weight: 700; text-align: center; }
.tape .next { color: #17794a; font-weight: 700; }
.steps { display: grid; grid-template-columns: 1fr 70px 1fr 70px 1fr; align-items: stretch; gap: 10px; }
.s { background: #fff; border-radius: 22px; padding: 30px; box-shadow: 0 6px 24px rgba(19,48,107,.08); font-size: 29px; display: flex; flex-direction: column; gap: 14px; }
.s h3 { font-size: 36px; color: #13306b; }
.arrow { display: flex; align-items: center; justify-content: center; font-size: 60px; color: #2456c9; }
.usecase { background: #e2f4ea; border: 2px solid #8fd1ac; border-radius: 18px; padding: 22px 32px; font-size: 32px; text-align: center; }
.caps { display: grid; grid-template-columns: 1fr 1fr; gap: 18px 30px; }
.caps div { display: flex; gap: 20px; align-items: center; background: #fff; border-radius: 16px; padding: 18px 24px; box-shadow: 0 4px 16px rgba(19,48,107,.07); font-size: 29px; }
.caps div:last-child { grid-column: 1 / span 2; }
.caps .n { flex: none; width: 60px; height: 60px; border-radius: 50%; background: #2456c9; color: #fff; display: flex; align-items: center; justify-content: center; font-size: 32px; }
.story { background: #13306b; color: #fff; border-radius: 18px; padding: 26px 34px; font-size: 38px; text-align: center; }
.story b { color: #ffd27a; }
.traps { list-style: none; padding: 0; gap: 16px; }
.traps li { background: #fff; border-left: 10px solid #e08a00; border-radius: 12px; padding: 16px 26px; font-size: 31px; box-shadow: 0 4px 16px rgba(19,48,107,.06); }
.quiz { display: flex; flex-direction: column; gap: 26px; }
.q { background: #fff; border-radius: 20px; padding: 28px 36px; box-shadow: 0 6px 24px rgba(19,48,107,.08); font-size: 33px; }
.q ol { margin: 14px 0 0 60px; display: flex; flex-direction: column; gap: 6px; }
.q.ok { border-left: 10px solid #17794a; }
.hero.compact { gap: 18px; }
.caps .n { font-style: normal; font-weight: 700; }
"""


def slide_html(slide, index, total, chapter):
    section = f'<span class="sec">{html.escape(slide["section"])}</span>' if slide["section"] else ""
    title = "" if index == 0 else f'<h2>{html.escape(slide["title"])}</h2>'
    progress = (index + 1) / total * 100
    return f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>{CSS}</style></head>
<body><div class="frame">
<div class="top"><span class="tag">{html.escape(chapter)}</span>{section}</div>
{title}<div class="content">{slide["body"]}</div>
<div class="foot">{index + 1} / {total}</div><div class="bar" style="width:{progress:.2f}%"></div>
</div></body></html>"""


def render_png(html_path, png_path):
    profile = HERE / "edge-shot-profile"
    subprocess.run([EDGE, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    f"--user-data-dir={profile}", "--window-size=1920,1080", "--virtual-time-budget=3000",
                    f"--screenshot={png_path}", html_path.as_uri()],
                   check=True, capture_output=True, timeout=90)
    if not png_path.exists():
        raise RuntimeError(f"Capture absente : {png_path}")


async def synthesize(text, mp3_path):
    """Écrit l'audio et renvoie les phrases avec leurs instants (secondes)."""
    sentences = []
    communicate = edge_tts.Communicate(text, VOICE, rate=RATE, boundary="SentenceBoundary")
    with open(mp3_path, "wb") as audio:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio.write(chunk["data"])
            elif chunk["type"] in ("SentenceBoundary", "WordBoundary"):
                start = chunk["offset"] / TICKS_PER_SECOND
                sentences.append((start, start + chunk["duration"] / TICKS_PER_SECOND, chunk["text"]))
    return sentences


def media_duration(path):
    probe = subprocess.run([FFMPEG, "-i", str(path)], capture_output=True, text=True, encoding="utf-8", errors="replace")
    match = re.search(r"Duration: (\d+):(\d+):(\d+\.\d+)", probe.stderr)
    if not match:
        raise RuntimeError(f"Durée illisible : {path}")
    hours, minutes, seconds = match.groups()
    return int(hours) * 3600 + int(minutes) * 60 + float(seconds)


def encode_segment(png, mp3, out, duration):
    lead_ms = int(LEAD_S * 1000)
    video_filter = (f"[0:v]scale=1920:1080,format=yuv420p,fade=t=in:st=0:d={FADE_S},"
                    f"fade=t=out:st={duration - FADE_S:.3f}:d={FADE_S}[v]")
    audio_filter = f"[1:a]adelay={lead_ms}|{lead_ms},apad[a]"
    subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-loop", "1", "-framerate", "30", "-i", str(png), "-i", str(mp3),
                    "-filter_complex", f"{video_filter};{audio_filter}", "-map", "[v]", "-map", "[a]",
                    "-t", f"{duration:.3f}", "-c:v", "libx264", "-preset", "medium", "-tune", "stillimage", "-crf", "20",
                    "-r", "30", "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-ac", "2", str(out)], check=True)


def srt_time(seconds):
    millis = int(round(seconds * 1000))
    hours, millis = divmod(millis, 3_600_000)
    minutes, millis = divmod(millis, 60_000)
    secs, millis = divmod(millis, 1000)
    return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"


def build(module_name, output):
    module = importlib.import_module(module_name)
    slides, chapter = module.SLIDES, module.CHAPTER
    work = HERE / f"work-{module_name}"
    work.mkdir(exist_ok=True)
    segments, cues, clock = [], [], 0.0
    for index, slide in enumerate(slides):
        stem = work / f"s{index:02}"
        html_path, png, mp3, seg = (stem.with_suffix(ext) for ext in (".html", ".png", ".mp3", ".mp4"))
        html_path.write_text(slide_html(slide, index, len(slides), chapter), encoding="utf-8")
        render_png(html_path, png)
        sentences = asyncio.run(synthesize(slide["narration"], mp3))
        duration = media_duration(mp3) + LEAD_S + TAIL_S
        encode_segment(png, mp3, seg, duration)
        cues.extend((clock + LEAD_S + start, clock + LEAD_S + end, text) for start, end, text in sentences)
        clock += media_duration(seg)
        segments.append(seg)
        print(f"diapositive {index + 1}/{len(slides)} : {duration:.1f} s", flush=True)

    concat_list = work / "concat.txt"
    concat_list.write_text("".join(f"file '{seg.as_posix()}'\n" for seg in segments), encoding="utf-8")
    srt = Path(output).with_suffix(".srt")
    srt.write_text("\n".join(f"{i}\n{srt_time(a)} --> {srt_time(b)}\n{t}\n" for i, (a, b, t) in enumerate(cues, 1)),
                   encoding="utf-8")
    joined = work / "joined.mp4"
    subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(concat_list),
                    "-c", "copy", str(joined)], check=True)
    subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-i", str(joined), "-i", str(srt), "-map", "0", "-map", "1",
                    "-c", "copy", "-c:s", "mov_text", "-metadata:s:s:0", "language=fre",
                    "-metadata", f"title={chapter}", "-movflags", "+faststart", str(output)], check=True)
    print(f"OK {output} : {media_duration(output) / 60:.1f} min, {len(cues)} sous-titres")


if __name__ == "__main__":
    sys.path.insert(0, str(HERE))
    build(sys.argv[1], sys.argv[2])
