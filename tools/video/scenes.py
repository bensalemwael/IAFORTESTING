"""Modèles de scènes animées. Chaque fonction renvoie {"html": ..., "narration": [...]}.

Narration : liste de segments. Une chaîne = voix principale ; {"max": "..."} = réplique de Max (bulle animée) ;
{"pause": secondes, "cue": "nom"} = silence. Dans le texte, {#nom} pose un repère au début du mot suivant.
Repères prédéfinis : "start" (début de scène) et "end". Les éléments d'une scène apparaissent sur leurs repères.
Options communes : trap="texte" (bandeau piège sur le repère {#trap}), sec="2.1.1" (rubrique de l'en-tête).
"""
import html as _html

LETTERS = "ABCDE"


def esc(text):
    """Échappe le texte, puis autorise **gras** et ==surlignage dégradé==."""
    out = _html.escape(text)
    parts = out.split("**")
    out = "".join(f"<b>{p}</b>" if i % 2 else p for i, p in enumerate(parts))
    parts = out.split("==")
    return "".join(f'<span class="hl">{p}</span>' if i % 2 else p for i, p in enumerate(parts))


def attr(text):
    return _html.escape(text, quote=True)


def header(kicker, title, narrow=""):
    return (f'<div class="kicker" data-in="start" data-anim="down">{esc(kicker)}</div>'
            f'<div class="title{narrow}" data-in="start+0.15" data-anim="up">{esc(title)}</div>')


def overlays(trap, max_line):
    out = ""
    if trap:
        out += f'<div class="trap" data-in="trap" data-anim="up">⚠️ {esc(trap)}</div>'
    if max_line:
        out += ('<div class="max" data-in="max" data-anim="pop"><div class="avatar">🧑‍💻</div>'
                f'<div class="bubble"><b>Max, testeur</b>{esc(max_line)}</div></div>')
    return out


def scene(kicker, title, body, narration, trap=None, max_line=None, body_style=""):
    if max_line is None:
        max_line = next((seg["max"] for seg in narration if isinstance(seg, dict) and "max" in seg), None)
    style = f' style="{body_style}"' if body_style else ""
    narrow = " narrow" if max_line else ""
    return {"html": header(kicker, title, narrow) + f'<div class="body"{style}>{body}</div>' + overlays(trap, max_line),
            "narration": narration}


def title_scene(kicker, title, subtitle, chips, narration):
    chip_html = "".join(f'<span class="chip">{esc(c)}</span>' for c in chips)
    body = (f'<div class="hero"><div class="k" data-in="start" data-anim="down">{esc(kicker)}</div>'
            f'<h1 data-in="start+0.2" data-anim="zoom">{esc(title)}</h1>'
            f'<p data-in="sub" data-anim="up">{esc(subtitle)}</p>'
            f'<div class="chips" data-in="chips" data-anim="up">{chip_html}</div></div>')
    return {"html": body, "narration": narration}


def cards(kicker, title, items, narration, cols=None, accent=None, trap=None, max_line=None):
    """items : (icône, titre, texte). La carte i apparaît sur {#c<i>}."""
    cols = cols or min(len(items), 4)
    html = f'<div class="grid" style="grid-template-columns:repeat({cols},1fr)">'
    for i, (icon, head, text) in enumerate(items):
        cls = " accent" if accent == i else ""
        html += (f'<div class="card{cls}" data-in="c{i}" data-ghost="1" data-glow="c{i}">'
                 f'<div class="ic">{icon}</div><h3>{esc(head)}</h3><div>{esc(text)}</div></div>')
    return scene(kicker, title, html + "</div>", narration, trap, max_line)


def rows(kicker, title, items, narration, trap=None, max_line=None, numbered=True):
    """items : (titre, texte). La ligne i apparaît sur {#r<i>}."""
    html = '<div class="rows">'
    for i, (head, text) in enumerate(items):
        badge = f'<div class="n">{i + 1}</div>' if numbered else '<div class="n">✓</div>'
        head_html = f"<h4>{esc(head)}</h4>" if head else ""
        html += (f'<div class="row" data-in="r{i}" data-ghost="1" data-glow="r{i}">{badge}'
                 f'<div>{head_html}{esc(text)}</div></div>')
    return scene(kicker, title, html + "</div>", narration, trap, max_line)


def chat(kicker, title, prompt, answer, narration, verdict=None, note=None, trap=None, max_line=None):
    """Repères : type (frappe du prompt), send, answer (réponse en streaming), verdict, note."""
    html = ('<div class="chat" data-in="start+0.3" data-anim="up"><div class="bar"><i style="background:#ff5f57"></i>'
            '<i style="background:#febc2e"></i><i style="background:#28c840"></i>&nbsp; Assistant IA</div>'
            f'<div class="msg user" data-in="send" data-anim="pop">{esc(prompt)}</div>'
            f'<div class="msg ai" data-in="answer" data-anim="fade"><span data-stream="answer" data-text="{attr(answer)}" data-wps="7"></span></div>'
            f'<div class="input" data-type="type" data-until="send" data-text="{attr(prompt)}" data-cps="34" data-dim="send"></div></div>')
    if verdict:
        text, kind = verdict
        html += f'<div class="stamp {kind}" style="left:690px;top:470px" data-in="verdict" data-anim="stamp">{esc(text)}</div>'
    if note:
        head, text, kind = note
        html += (f'<div class="side"><div class="note {kind}" data-in="note" data-anim="right">'
                 f'<h4>{esc(head)}</h4>{esc(text)}</div></div>')
    return scene(kicker, title, html, narration, trap, max_line, body_style="justify-content:flex-start")


def prompt_build(kicker, title, lines, narration, badge=None, trap=None, max_line=None, width=1250):
    """lines : (étiquette, texte). La ligne i apparaît sur {#l<i>}, avec texte tapé ; badge sur {#badge}."""
    html = f'<div class="editor" style="width:{width}px" data-in="start+0.3" data-anim="up">'
    for i, (label, text) in enumerate(lines):
        html += (f'<div class="line" data-glow="l{i}"><span class="label c{i % 8}" data-in="l{i}" data-anim="pop">{esc(label)}</span>'
                 f'<span data-type="l{i}+0.3" data-text="{attr(text)}" data-cps="45"></span></div>')
    html += "</div>"
    if badge:
        big, small = badge
        html += f'<div class="badge" data-in="badge" data-anim="pop"><b>{esc(big)}</b><span>{esc(small)}</span></div>'
    return scene(kicker, title, html, narration, trap, max_line)


def flow(kicker, title, steps, narration, check=None, trap=None, max_line=None, loop=False):
    """steps : (icône, titre, texte). L'étape i apparaît sur {#s<i>} ; check sur {#check}."""
    html = '<div class="flow">'
    for i, (icon, head, text) in enumerate(steps):
        if i:
            html += f'<div class="arrow" data-in="s{i}-0.2" data-ghost="1">➜</div>'
        html += (f'<div class="step" data-in="s{i}" data-ghost="1" data-glow="s{i}"><div class="ic">{icon}</div>'
                 f'<h4>{esc(head)}</h4>{esc(text)}</div>')
    if loop:
        html += '<div class="arrow" data-in="loop" data-anim="pop">↺</div>'
    html += "</div>"
    if check:
        html += f'<div class="check" data-in="check" data-anim="up">{esc(check)}</div>'
    return scene(kicker, title, html, narration, trap, max_line)


def versus(kicker, title, left, right, narration, trap=None, max_line=None):
    """left/right : (titre, [puces]). Repères : left, right."""
    def panel(side, data):
        head, items = data
        lis = "".join(f"<li>{esc(x)}</li>" for x in items)
        anim = "left" if side == "left" else "right"
        return f'<div class="panel" data-in="{side}" data-ghost="1" data-glow="{side}"><h3>{esc(head)}</h3><ul>{lis}</ul></div>'
    html = f'<div class="versus">{panel("left", left)}<div class="vs" data-in="right" data-anim="pop">VS</div>{panel("right", right)}</div>'
    return scene(kicker, title, html, narration, trap, max_line)


def table(kicker, title, head, body_rows, narration, trap=None, max_line=None):
    """La ligne i apparaît sur {#r<i>}."""
    html = '<table class="t"><tr>' + "".join(f"<th>{esc(h)}</th>" for h in head) + "</tr>"
    for i, cells in enumerate(body_rows):
        html += f'<tr data-in="r{i}" data-ghost="1">' + "".join(f"<td>{esc(c)}</td>" for c in cells) + "</tr>"
    return scene(kicker, title, html + "</table>", narration, trap, max_line)


def bignum(kicker, title, value, unit, caption, narration, decimals=0, trap=None, max_line=None):
    """Compteur animé sur {#n}, légende sur {#cap}."""
    html = (f'<div class="big"><span class="num" data-in="n" data-anim="pop"><span data-count="n" data-to="{value}" data-dec="{decimals}">0</span></span>'
            f'<span class="unit" data-in="n+0.4" data-anim="fade"> {esc(unit)}</span>'
            f'<p data-in="cap" data-anim="up">{esc(caption)}</p></div>')
    return scene(kicker, title, html, narration, trap, max_line)


def quiz(kicker, question, options, good, explain, ask, reveal, seconds=4):
    """Question lue, compte à rebours muet, puis bonne(s) réponse(s) et explication.
    `good` : indice ou liste d'indices. Mettre {#rev} au début de `reveal`."""
    good = [good] if isinstance(good, int) else list(good)
    cols = 2 if len(options) == 4 else 1
    opts = "".join(
        f'<div class="opt" data-in="start+{0.9 + 0.35 * i:.2f}" data-anim="left" {"data-good" if i in good else "data-dim"}="rev">'
        f'<span class="letter">{LETTERS[i]}</span><span>{esc(o)}</span></div>'
        for i, o in enumerate(options))
    html = (f'<div class="question" data-in="start+0.3" data-anim="up">{esc(question)}</div>'
            f'<div class="options" style="grid-template-columns:repeat({cols},1fr)">{opts}</div>'
            f'<div class="explain" data-in="rev+0.4" data-anim="up">✅ {esc(explain)}</div>'
            f'<div class="timer" data-countdown="cd" data-len="{seconds}"><svg viewBox="0 0 200 200"><circle class="bg" cx="100" cy="100" r="90"/>'
            '<circle class="fg" cx="100" cy="100" r="90"/></svg><b>3</b></div>')
    return scene(kicker, "Quiz éclair", html, [*ask, {"pause": seconds, "cue": "cd"}, *reveal])


def code(kicker, title, text, narration, note=None, trap=None, max_line=None):
    """Bloc de code tapé sur {#code} ; note facultative à droite sur {#note}."""
    html = f'<div class="code" style="width:1150px" data-in="start+0.3" data-anim="up"><span data-type="code" data-text="{attr(text)}" data-cps="60"></span></div>'
    if note:
        head, body, kind = note
        html += f'<div class="side"><div class="note {kind}" data-in="note" data-anim="right"><h4>{esc(head)}</h4>{esc(body)}</div></div>'
    return scene(kicker, title, html, narration, trap, max_line, body_style="justify-content:flex-start")
