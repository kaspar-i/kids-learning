"""Build the static booklet HTML from puzzles.json + booklet-template.html.

The template's <script data-removed-by-build> block is the old client-side
renderer kept for reference; this build strips it and injects fully static
markup, so the booklet needs no JavaScript (prints and screenshots reliably).
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / "booklets" / "sudoku"

SECTIONS = {
    "A": ("Warm-up · 3×3 Pictures", "var(--secA)", "Every picture appears once in each row → and each column ↓."),
    "B": ("3×3 Numbers", "var(--secB)", "Same rule, now with numbers 1–3. Write the missing ones."),
    "C": ("Big kid · 4×4 Pictures", "var(--secC)", "New rule: each 2×2 box (thick lines) also gets every picture once!"),
    "D": ("Champion · 4×4 Numbers", "var(--secD)", "The hardest ones. Numbers 1–4 in every row, column and box."),
}


def stars(p):
    if p["size"] == 3:
        s = 1 if p["blanks"] <= 3 else 2 if p["blanks"] <= 4 else 3
    else:
        s = 1 if p["blanks"] <= 6 else 2 if p["blanks"] <= 8 else 3
    return "★" * s + "☆" * (3 - s)


def grid_html(p, solved=False, mini=False):
    size = p["size"]
    cls = ("grid gs3" if size == 3 else "grid gs4") if mini else ("grid g3" if size == 3 else "grid g4")
    src = p["solution"] if solved else p["grid"]
    cells = []
    for r in range(size):
        for c in range(size):
            v = src[r][c]
            box = ((" boxL" if c == 2 else "") + (" boxT" if r == 2 else "")) if size == 4 else ""
            if v == 0:
                cells.append(f'<span class="blank{box}"></span>')
            else:
                cells.append(f'<span class="{box.strip()}">{p["symbols"][v - 1]}</span>')
    return f'<div class="{cls}" role="img" aria-label="{size} by {size} puzzle">{"".join(cells)}</div>'


def puzzle_html(p):
    name, color, _ = SECTIONS[p["section"]]
    if p["kind"] == "picture":
        legend = f'<footer class="legend">Use each of these: <span class="syms">{" ".join(p["symbols"])}</span></footer>'
        title = f'Puzzle {p["id"]} · {p["theme"]}'
    else:
        legend = f'<footer class="legend">Write the numbers <span class="syms">{" · ".join(p["symbols"])}</span></footer>'
        title = f'Puzzle {p["id"]}'
    return f'''<article class="puzzle" style="--sc:{color}">
    <header><span class="chip">{p["section"]}</span><h3>{title}</h3><span class="stars" aria-label="difficulty">{stars(p)}</span></header>
    {grid_html(p)}
    {legend}
  </article>'''


EXAMPLE = {
    "size": 3, "kind": "picture", "symbols": ["\U0001F436", "\U0001F431", "\U0001F430"],
    "grid": [[1, 2, 3], [3, 1, 2], [2, 3, 0]],
    "solution": [[1, 2, 3], [3, 1, 2], [2, 3, 1]],
}

data = json.loads((D / "puzzles.json").read_text(encoding="utf-8"))
puzzles = data["puzzles"]
sheets = []

sheets.append('''<section class="sheet cover">
  <div class="kicker">Little Learners · Puzzle Booklet 1</div>
  <h1>Animal <span class="sun">Sudoku</span></h1>
  <div class="cover-grid" aria-hidden="true">
    <span>\U0001F436</span><span>\U0001F431</span><span>\U0001F431</span><span>\U0001F436</span>
  </div>
  <p class="sub">24 picture and number puzzles for ages 5–8 · from first tries to champion level</p>
  <div class="belongs">This book belongs to __________________</div>
</section>''')

sheets.append(f'''<section class="sheet rules">
  <h2>How to play</h2>
  <ol>
    <li>Look at one <b>row</b> (→). Every picture must appear <b>exactly once</b>.</li>
    <li>Now check the <b>column</b> (↓) — exactly once there too.</li>
    <li>Find a dashed box and ask: <i>which picture is missing here?</i></li>
    <li>Draw the missing picture (or write its number). Do this for every empty box!</li>
    <li>In the 4×4 puzzles there is one more rule: each <b>2×2 box</b> with thick lines also gets every picture once.</li>
  </ol>
  <div class="example">
    {grid_html(EXAMPLE)}
    <p style="max-width:32ch;font-size:16px;line-height:1.6">In this row the \U0001F436 and the \U0001F431 are already there…<br>so the empty box must be the <b>\U0001F430</b>!</p>
  </div>
  <div class="tipbox"><b>For grown-ups:</b> one or two puzzles per sitting is plenty. If an answer is wrong, don't correct it — ask "can you check this row together with me?" and let your child find it. The booklet gets harder section by section (look at the stars); it's fine to stay in a section until it feels easy.</div>
  <span class="pgnum">2</span>
</section>''')

page_no = 3
for key in "ABCD":
    name, color, blurb = SECTIONS[key]
    group = [p for p in puzzles if p["section"] == key]
    for i in range(0, len(group), 2):
        strip = (
            f'<div class="section-strip" style="--sc:{color}"><h2>{name}</h2><p>{blurb}</p></div>'
            if i == 0 else ""
        )
        pair = "".join(puzzle_html(p) for p in group[i:i + 2])
        sheets.append(f'''<section class="sheet">
      {strip}
      <div class="puzzles2">{pair}</div>
      <span class="pgnum">{page_no}</span>
    </section>''')
        page_no += 1

for i in range(0, len(puzzles), 12):
    chunk = puzzles[i:i + 12]
    sols = "".join(
        f'<div class="sol"><span class="lbl">Puzzle {p["id"]}</span>{grid_html(p, solved=True, mini=True)}</div>'
        for p in chunk
    )
    sheets.append(f'''<section class="sheet">
    <div class="section-strip" style="--sc:var(--sun)"><h2>Answers</h2><p>No peeking until you've tried! Puzzles {i + 1}–{min(i + 12, len(puzzles))}</p></div>
    <div class="sols">{sols}</div>
    <span class="pgnum">{page_no}</span>
  </section>''')
    page_no += 1

sheets = [s.replace('<section class="sheet', f'<section id="sheet-{i + 1}" class="sheet', 1) for i, s in enumerate(sheets)]

tpl = (D / "booklet-template.html").read_text(encoding="utf-8")
tpl = re.sub(r"<script data-removed-by-build>.*?</script>\s*", "", tpl, flags=re.S)
out = tpl.replace("__BOOK_HTML__", "\n".join(sheets))
assert "__PUZZLES_JSON__" not in out and "__BOOK_HTML__" not in out
(D / "animal-sudoku-booklet.html").write_text(out, encoding="utf-8")
print(f"built {len(sheets)} sheets -> {D / 'animal-sudoku-booklet.html'} ({len(out)} chars)")
