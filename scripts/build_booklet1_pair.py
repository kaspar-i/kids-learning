"""Build the static entry-pair booklet HTML (1a + 1b in one printable file).

Reads booklets/sudoku/puzzles-1a1b.json + booklets/sudoku/booklet-1a1b-template.html,
writes booklets/sudoku/animal-sudoku-1a1b.html - fully static markup, no JavaScript
needed at view time (same convention as the v0 build).

Layout follows framework section 4.4 note 4 (the entry pair splits ONE standard
booklet's B18 budget): 28 A4 pages total, 19 working pages (~9-10 two-page spreads
for the pair as a whole). Booklet 1a = pages 1-14, booklet 1b = pages 15-28; a
parent prints once and staples two thin booklets.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / "booklets" / "sudoku"

data = json.loads((D / "puzzles-1a1b.json").read_text(encoding="utf-8"))
A, B = data["b1a"], data["b1b"]
SAFARI = data["sets"]["safari"]
SKY = data["sets"]["sky"]
FOOD = data["sets"]["food"]

LION, ELEPHANT, GIRAFFE, MONKEY = SAFARI

# ---------------------------------------------------------------- renderers

def cells_html(values, symbols, focus=None):
    out = []
    for i, v in enumerate(values):
        cls = []
        if v == 0:
            cls.append("blank")
            if focus is not None and i == focus:
                cls.append("focus")
        inner = "" if v == 0 else symbols[v - 1]
        cl = f' class="{" ".join(cls)}"' if cls else ""
        out.append(f"<span{cl}>{inner}</span>")
    return "".join(out)


def strip_html(values, symbols, size="", focus=None, aria="puzzle strip"):
    n = len(values)
    cls = f"grid {size}".strip()
    return (f'<div class="{cls}" role="img" aria-label="{aria}" '
            f'style="grid-template-columns:repeat({n},var(--cs,var(--cellB)))">'
            f"{cells_html(values, symbols, focus)}</div>")


def grid2d_html(grid, symbols, size="", focus_cell=None, aria="puzzle grid"):
    n = len(grid[0])
    cls = f"grid {size}".strip()
    rows = []
    for r, row in enumerate(grid):
        f = focus_cell[1] if (focus_cell is not None and focus_cell[0] == r) else None
        rows.append(cells_html(row, symbols, f))
    return (f'<div class="{cls}" role="img" aria-label="{aria}" '
            f'style="grid-template-columns:repeat({n},var(--cs,var(--cellB)))">'
            f"{''.join(rows)}</div>")


def vcol_html(values, symbols, size="", aria="column strip"):
    cls = f"grid vcol {size}".strip()
    return (f'<div class="{cls}" role="img" aria-label="{aria}">'
            f"{cells_html(values, symbols)}</div>")


def emoji_row_html(emojis, size=""):
    cls = f"grid {size}".strip()
    spans = "".join(f"<span>{e}</span>" for e in emojis)
    return (f'<div class="{cls}" role="img" aria-label="picture row" '
            f'style="grid-template-columns:repeat({len(emojis)},var(--cs,var(--cellB)))">{spans}</div>')


def checkopts():
    return '<div class="checkopts"><span class="opt">✓</span><span class="opt">✗</span></div>'


def choices_html(choices, symbols):
    tiles = "".join(f'<span class="ctile">{symbols[v - 1]}</span>' for v in choices)
    return f'<div class="choicetiles"><span class="qm">?</span>{tiles}</div>'


def rowitem(label, inner, extra=""):
    return f'<div class="rowitem"><span class="lbl">{label}</span>{inner}{extra}</div>'


def griditem(label, inner):
    return f'<div class="griditem"><span class="glbl">{label}</span>{inner}</div>'


def section(title, blurb, color):
    return (f'<div class="section-strip" style="--sc:{color}">'
            f"<h2>{title}</h2><p>{blurb}</p></div>")


def iconchip(icons, say, color):
    return (f'<div class="iconchip" style="--sc:{color}">{icons}'
            f'<span class="say">{say}</span></div>')


def band(label, items_html):
    inner = "".join(f'<div class="banditem">{h}</div>' for h in items_html)
    return (f'<div class="band-box"><span class="bandlbl">🔁 {label}</span>{inner}</div>')


def band_item_html(item):
    t = item["type"]
    syms = item["symbols"]
    if t == "breaker" or t == "legalcol":
        return strip_html(item["cells"], syms, "band") + '<span class="bic">⭕ 👯</span>'
    if t == "pattern":
        return strip_html(item["cells"], syms, "band") + '<span class="bic">✋ ?</span>'
    if t == "missing":
        return strip_html(item["cells"], syms, "band") + '<span class="bic">🗣 ?</span>'
    raise ValueError(t)


def parenthint(color, stuck, praise):
    return (f'<div class="parenthint" style="--sc:{color}"><b>For grown-ups — if stuck, say:</b> '
            f'&ldquo;{stuck}&rdquo; <b>Praise the move that worked:</b> &ldquo;{praise}&rdquo;</div>')


MYTHINK = '<div class="mythink">💭 My thinking (a grown-up writes what I say): ______________________________________________</div>'


def mini_sol(label, inner):
    return f'<div class="sol"><span class="lbl">{label}</span>{inner}</div>'


sheets = []

def sheet(book, page, body, cls=""):
    c = f"sheet {cls}".strip()
    sheets.append(f'<section class="{c}">\n{body}\n<span class="pgnum">{book} · {page}</span>\n</section>')


# ================================================================ BOOKLET 1a

# --- cover 1a (page number omitted on covers, like v0) ---
sheets.append(f'''<section class="sheet cover" style="--bc:var(--secA)">
  <div class="kicker">Little Learners · Entry Pair · Booklet 1a</div>
  <h1>Animal <span class="accent">Sudoku</span> 1a</h1>
  <div style="font-size:46px;letter-spacing:8px" aria-hidden="true">{LION}{ELEPHANT}{GIRAFFE}{MONKEY}</div>
  {strip_html([1, 0, 3], SAFARI[:3], aria="cover strip")}
  <p class="story">Lion, Elephant, Giraffe and Monkey love standing in line —<br>
  but <b>never two of the same friend in one row!</b></p>
  <p class="sub">Rows only · cut-out tiles · one rule · ages ~4½–5½</p>
  <div class="belongs">This book belongs to __________________</div>
</section>''')

# --- how-to 1a ---
wk = A["worked"]
wk_blank = wk["cells"].index(0)
wk_missing = SAFARI[:3][wk["solution"][wk_blank] - 1]
wk_present = [SAFARI[:3][v - 1] for v in wk["cells"] if v != 0]
sheet("1a", 2, f'''<div class="rules" style="--bc:var(--secA);display:flex;flex-direction:column;gap:5mm;flex:1">
  <h2>How this booklet works</h2>
  <p class="lead"><b>Read aloud:</b> &ldquo;Every friend stands in the row <b>exactly once</b>.
  Twins are not allowed!&rdquo; That is the only rule in this whole booklet.</p>
  <div class="iconlegend">
    <div class="row"><span class="ic">👀 →</span> Look along the row, one box at a time.</div>
    <div class="row"><span class="ic">{ELEPHANT}{ELEPHANT}🚫</span> Two of the same friend in a row? Not allowed!</div>
    <div class="row"><span class="ic">✋</span> Put a cut-out tile in each dashed box (tile sheet on the next page).</div>
    <div class="row"><span class="ic">⭕</span> Circle pictures when a page asks you to find something.</div>
    <div class="row"><span class="ic">✓ ✗</span> Colour the happy check if a row is right, the cross if it is wrong.</div>
  </div>
  <div class="example">
    {strip_html(wk["cells"], SAFARI[:3], aria="worked example strip")}
    <p style="max-width:34ch;font-size:15.5px;line-height:1.6">{" and ".join(wk_present)} are already in the row&hellip;<br>
    so the empty box must be <b>{wk_missing}</b>! The row checks itself:<br>if you ever see twins, something needs another try.</p>
  </div>
  <div class="docsurface">
    <div class="portrait">draw<br>yourself!</div>
    <div class="docfields">
      <div>📅 Today is: ______________</div>
      <div class="cando"><span class="box"></span> I can sort toys into groups</div>
      <div class="cando"><span class="box"></span> I can copy a clapping pattern</div>
      <div class="cando"><span class="box"></span> I can play a game and take turns</div>
    </div>
  </div>
  <div class="tipbox"><b>For grown-ups:</b> cut out the tiles overleaf first. There is no schedule — your child picks this
  booklet up whenever they like, and a page or two per sitting is plenty. All puzzles on a page are the <b>same</b> level:
  let your child choose the order. Never correct a wrong tile — ask &ldquo;can you check this row with me?&rdquo; and let
  them find the twins themselves. If a page feels too hard, go back one page for a <i>different</i> puzzle rather than
  repeating the same one. Mistakes are just &ldquo;not yet&rdquo;.</div>
</div>''')

# --- tile sheet 1a ---
tiles_1a = "".join(f"<span>{s}</span>" for s in (SAFARI * 4)) + "".join(f"<span>{s}</span>" for s in (FOOD * 3))
sheet("1a", 3, f'''{section("Tile sheet ✂️", "Cut along the dashed lines — these tiles play every puzzle in this booklet.", "var(--secA)")}
  <p class="tiles-note"><b>For grown-ups:</b> cut out all the tiles and keep them in an envelope clipped to the
  booklet. Placing tiles (instead of writing) is on purpose at this age — answers can be changed without any
  rubbing out, so trying again always feels safe.</p>
  <div class="tilegrid">{tiles_1a}</div>''')

# --- W1: sorting + patterns warm-up ---
sort_rows = "".join(
    rowitem("abc"[i], emoji_row_html(item["cells"]), '<span style="font-size:22px">✏️❌</span>')
    for i, item in enumerate(A["sorting"]))
pat_rows = "".join(
    rowitem("abc"[i], strip_html(item["cells"], item["symbols"]), '<span style="font-size:22px">✋</span>')
    for i, item in enumerate(A["patterns"]))
sheet("1a", 4, f'''{section("Warm-up: sort &amp; patterns", "Read aloud: one of these does not belong — cross it out! Then: what comes next?", "var(--secA)")}
  {iconchip("👀 ✏️❌", "cross out the one that does not belong", "var(--secA)")}
  <div class="rowstack">{sort_rows}</div>
  <div style="height:6mm"></div>
  {iconchip("👀 ✋", "place the tile that comes next", "var(--secA)")}
  <div class="rowstack">{pat_rows}</div>''')

# --- W2: explore + the rule (ONE worked example, B10) ---
sheet("1a", 5, f'''{section("Meet the rule", "First play freely — then see the rule at work.", "var(--secA)")}
  {iconchip("✋ 🙂", "play: line up the friends any way you like", "var(--secA)")}
  <div class="rowstack">
  {rowitem("", strip_html(A["explore"]["cells"], A["explore"]["symbols"], aria="free play strip"),
           '<span style="font-size:15px;color:var(--ink-soft);max-width:52mm">Then look: did two of the same friend sneak in? 👀</span>')}
  </div>
  <div style="height:5mm"></div>
  {iconchip(f"{ELEPHANT}{ELEPHANT} 🚫", "the rule: never two of the same friend in one row", "var(--secA)")}
  <div class="example">
    {strip_html(wk["cells"], SAFARI[:3], aria="worked example")}
    <p style="max-width:36ch;font-size:15.5px;line-height:1.7">👀 Who is already here? {" , ".join(wk_present)}.<br>
    🤔 Who is missing? <b>{wk_missing}</b>!<br>✋ Place the {wk_missing} tile. Row full, no twins — done!</p>
  </div>
  <div class="parenthint" style="--sc:var(--secA)"><b>For grown-ups:</b> show this example once, slowly, thinking aloud —
  then hand over. From here on, your child discovers their own way of checking; that is the point.</div>''')

# --- W3: recognition 1 — spot the twins ---
rb_rows = "".join(
    rowitem("abcd"[i], strip_html(item["cells"], item["symbols"], aria="finished strip"))
    for i, item in enumerate(A["rec_break"]))
sheet("1a", 6, f'''{section("Spot the twins!", "Read aloud: every one of these rows is finished — but each hides twins. Circle both twins.", "var(--secB)")}
  {iconchip("👀 👯 ⭕", "find the two matching pictures and circle them", "var(--secB)")}
  <div class="rowstack">{rb_rows}</div>''')

# --- W4: recognition 2 — legal-or-not + which tile ---
legal_rows = "".join(
    rowitem("abc"[i], strip_html(item["cells"], item["symbols"], aria="finished strip"), checkopts())
    for i, item in enumerate(A["rec_legal"]))
which_rows = "".join(
    rowitem("abc"[i],
            strip_html(item["cells"], item["symbols"], focus=item["cells"].index(0), aria="strip with one empty box"),
            choices_html(item["choices"], item["symbols"]))
    for i, item in enumerate(A["rec_which"]))
sheet("1a", 7, f'''{section("Right or wrong?", "Read aloud: is this row allowed? Colour the ✓ or the ✗.", "var(--secB)")}
  {iconchip("👀 ✓✗", "colour the check if the row is right", "var(--secB)")}
  <div class="rowstack">{legal_rows}</div>
  <div style="height:6mm"></div>
  {section("Which tile goes here?", "Read aloud: point to the tile that belongs in the yellow box.", "var(--secB)")}
  {iconchip("🤔 👉", "point to the right tile — why not the other one?", "var(--secB)")}
  <div class="rowstack">{which_rows}</div>''')

# --- W5: production, 3-strips ---
p3 = "".join(rowitem("abcd"[i], strip_html(s["cells"], s["symbols"]), '<span style="font-size:22px">✋</span>')
             for i, s in enumerate(A["prod3"]))
sheet("1a", 8, f'''{section("Three friends", "Your puzzles now! Pick any order — all four are the same level.", "var(--secA)")}
  {iconchip("👀 → ✋", "fill every dashed box — no twins in a row", "var(--secA)")}
  <div class="rowstack">{p3}</div>
  <footer class="legend">Use each of these: <span class="syms">{" ".join(SAFARI[:3])}</span></footer>''')

# --- W6: production, 4-strips ---
p4 = "".join(rowitem("abcd"[i], strip_html(s["cells"], s["symbols"]), '<span style="font-size:22px">✋</span>')
             for i, s in enumerate(A["prod4"]))
sheet("1a", 9, f'''{section("Now four friends!", "Monkey joins the line. Same rule, longer row.", "var(--secA)")}
  {iconchip("👀 → ✋", "fill every dashed box — no twins in a row", "var(--secA)")}
  <div class="rowstack">{p4}</div>
  <footer class="legend">Use each of these: <span class="syms">{" ".join(SAFARI)}</span></footer>''')

# --- W7: production, 2x2 two rows at once + remember band ---
p22 = "".join(griditem("abcd"[i], grid2d_html(g["rows"], g["symbols"], aria="two-row grid"))
              for i, g in enumerate(A["prod22"]))
sheet("1a", 10, f'''{section("Two rows at once", "Read aloud: each ROW follows the rule on its own. (Up-and-down does not matter yet — that is booklet 1b's secret!)", "var(--secA)")}
  {band("Do you remember? From your earlier pages", [band_item_html(i) for i in A["remember"]])}
  {iconchip("👀 → ✋", "check each row by itself", "var(--secA)")}
  <div class="gridrow">{p22}</div>
  <footer class="legend">Use each of these in every row: <span class="syms">{SAFARI[0]} {SAFARI[3]}</span></footer>''')

# --- W8: Life page — set the table ---
life_rows = "".join(
    rowitem("abc"[i], strip_html(s["cells"], FOOD, aria="picnic table row"), '<span style="font-size:22px">✋</span>')
    for i, s in enumerate(A["life"]["rows"]))
sheet("1a", 11, f'''{section("Set the table! 🧺", "Read aloud: three picnic tables. Every table needs one apple, one cup and one cookie — no table gets two of the same.", "var(--secA)")}
  {iconchip("🧺 ✋", "give every table one of each — same rule, real life!", "var(--secA)")}
  <div class="rowstack">{life_rows}</div>
  <footer class="legend">Every table gets: <span class="syms">{" ".join(FOOD)}</span></footer>
  <div class="parenthint" style="--sc:var(--secA)"><b>For grown-ups:</b> this is the same row rule wearing real-life
  clothes. At your next real meal, let your child set the table the sudoku way — one of each, no twins.</div>''')

# --- W9: find the mistake ---
fm = A["mistake"]
fm_rows = "".join(
    rowitem("abc"[i], strip_html(s["cells"], fm["symbols"], aria="finished strip"), checkopts())
    for i, s in enumerate(fm["strips"]))
sheet("1a", 12, f'''{section("The fix-it page 🔧", "Read aloud: someone finished these three rows — but ONE row has twins. Find it, circle the twins, and fix it with your tiles.", "var(--secB)")}
  {iconchip("👀 👯 ⭕ ✋", "find the wrong row, circle the twins, fix it", "var(--secB)")}
  <div class="rowstack">{fm_rows}</div>
  {MYTHINK}
  {parenthint("var(--secB)",
              "Let&rsquo;s check one row at a time — do you see the same friend twice anywhere?",
              "You checked every row before deciding — that is exactly how puzzle-checkers work!")}''')

# --- W10: provocation (two answers) + make your own ---
pv = A["provocation"]
sheet("1a", 13, f'''{section("Star page ⭐", "A tricky strip and your very own puzzle to make.", "var(--sun)")}
  <div class="special">
    <span class="sptitle">⭐ The trickster strip — it has TWO answers!</span>
    {rowitem("", strip_html(pv["cells"], pv["symbols"], aria="two-answer strip"),
             '<span style="font-size:15px;color:var(--ink-soft);max-width:56mm">Find one answer&hellip; now take the tiles off and find a DIFFERENT one! Which do you like better? 😄</span>')}
  </div>
  <div style="height:5mm"></div>
  <div class="create-box">
    <span class="cptitle">🎨 Make your own strip!</span>
    <div class="gridrow">
      {strip_html([0, 0, 0], SAFARI[:3], aria="empty strip")}
      {strip_html([0, 0, 0, 0], SAFARI, aria="empty strip")}
    </div>
    <p style="margin:0;font-size:14.5px;line-height:1.6">✋ Fill a whole strip with tiles (no twins!) &hellip;
    then take ONE tile away and give the puzzle to a grown-up. Did they solve it? ⭕ Check their row!</p>
  </div>
  {MYTHINK}''')

# --- answers 1a ---
sols_1a = []
for i, s in enumerate(A["prod3"]):
    sols_1a.append(mini_sol(f"Three friends {'abcd'[i]}", strip_html(s["solution"], s["symbols"], "mini")))
for i, s in enumerate(A["prod4"]):
    sols_1a.append(mini_sol(f"Four friends {'abcd'[i]}", strip_html(s["solution"], s["symbols"], "mini")))
for i, g in enumerate(A["prod22"]):
    sols_1a.append(mini_sol(f"Two rows {'abcd'[i]}", grid2d_html(g["solution"], g["symbols"], "mini")))
for i, s in enumerate(A["life"]["rows"]):
    sols_1a.append(mini_sol(f"Table {'abc'[i]}", strip_html(s["solution"], FOOD, "mini")))
sols_1a.append(mini_sol("Fix-it: row fixed", strip_html(fm["fixed"], fm["symbols"], "mini")))
for i, s in enumerate(pv["solutions"]):
    sols_1a.append(mini_sol(f"Trickster answer {i + 1}", strip_html(s, pv["symbols"], "mini")))
legal_key = ", ".join(f"{'abc'[i]} {'✓' if it['legal'] else '✗'}" for i, it in enumerate(A["rec_legal"]))
which_key = ", ".join(f"{'abc'[i]} = {it['symbols'][it['answer'] - 1]}" for i, it in enumerate(A["rec_which"]))
fixit_key = f"row {'abc'[fm['bad_index']]} had the twins ({fm['symbols'][fm['dup'] - 1]})"
sheet("1a", 14, f'''{section("Answers", "No peeking until you have tried! Remember: the rows check themselves — twins mean try again.", "var(--sun)")}
  <div class="sols">{"".join(sols_1a)}</div>
  <div style="height:4mm"></div>
  <p class="keyline"><b>Right or wrong?</b> {legal_key} &nbsp;·&nbsp; <b>Which tile?</b> {which_key} &nbsp;·&nbsp; <b>Fix-it page:</b> {fixit_key}</p>
  <div style="height:3mm"></div>
  <div class="cap">You can keep the row rule with three AND four friends! 🎉</div>
  <div style="height:3mm"></div>
  <div class="stampbox"><b>Wall poster:</b> put a pencil tick on your <b>Picture Sudoku 4×4</b> node — booklet 1b
  finishes it! <b>Next:</b> start booklet 1b in about a week. Its first page peeks back at these pages —
  that little look-back is how the puzzles stick.</div>''')

# ================================================================ BOOKLET 1b

# --- cover 1b ---
sheets.append(f'''<section class="sheet cover" style="--bc:var(--secC)">
  <div class="kicker">Little Learners · Entry Pair · Booklet 1b</div>
  <h1>Animal <span class="accent">Sudoku</span> 1b</h1>
  <div style="font-size:46px;letter-spacing:8px" aria-hidden="true">{LION}{ELEPHANT}{GIRAFFE}{MONKEY}</div>
  {grid2d_html([[1, 2, 3, 4], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], SAFARI, aria="cover grid")}
  <p class="story">The friends have a new game: a big square!<br>
  Now the rule works <b>across →</b> AND <b>down ↓</b>.</p>
  <p class="sub">4×4 · rows and columns · tiles, then drawing · ages ~5–6 · start after booklet 1a</p>
  <div class="belongs">This book belongs to __________________</div>
</section>''')

# --- how-to 1b ---
bwk = B["worked"]
bwk_syms = bwk["symbols"]
bwk_row = bwk["row"]
bwk_missing1 = bwk_syms[bwk["answer"] - 1]
bwk_missing2 = bwk_syms[bwk["wrong"] - 1]
sheet("1b", 2, f'''<div class="rules" style="--bc:var(--secC);display:flex;flex-direction:column;gap:5mm;flex:1">
  <h2>One new thing: columns join in!</h2>
  <p class="lead"><b>Read aloud:</b> &ldquo;You already know the row rule. Here is the whole new thing in this booklet:
  now the <b>columns</b> (going down ↓) follow the rule too. Every friend exactly once in each row →
  <b>and</b> in each column ↓.&rdquo;</p>
  <div class="iconlegend">
    <div class="row"><span class="ic">👀 →</span> Check along the row — every friend exactly once.</div>
    <div class="row"><span class="ic">👀 ↓</span> NEW: check down the column too — exactly once there as well!</div>
    <div class="row"><span class="ic">✋</span> Place tiles first. Later pages ask you to draw ✏️ instead.</div>
    <div class="row"><span class="ic">{ELEPHANT}{ELEPHANT}🚫</span> Twins in a row OR in a column? Not allowed — that is how you check yourself.</div>
  </div>
  <div class="example">
    {grid2d_html(B["example_solved"]["grid"], SAFARI, "mini", aria="solved example grid")}
    <p style="max-width:40ch;font-size:15.5px;line-height:1.65">A finished 4×4 — look with your child: every row has all
    four friends, and every column too. No twins anywhere!</p>
  </div>
  <div class="docsurface">
    <div class="portrait">draw<br>yourself!</div>
    <div class="docfields">
      <div>📅 Today is: ______________</div>
      <div class="cando"><span class="box"></span> I finished booklet 1a</div>
      <div class="cando"><span class="box"></span> I can spot twins in a row all by myself</div>
      <div class="cando"><span class="box"></span> I can fill a row with no twins</div>
    </div>
  </div>
  <div class="tipbox"><b>For grown-ups:</b> start this booklet about a week after 1a — the &ldquo;Do you
  remember?&rdquo; boxes deliberately look back at last week's pages. Cut the tile sheet overleaf. Everything from 1a
  still applies: child picks the order on a page, one or two pages per sitting, never correct — ask &ldquo;can you
  check this column with me?&rdquo;. The last puzzle pages switch from tiles to drawing; wobbly drawings are perfect.</div>
</div>''')

# --- tile sheet 1b ---
tiles_1b = "".join(f"<span>{s}</span>" for s in (SAFARI * 6))
sheet("1b", 3, f'''{section("Tile sheet ✂️", "Cut along the dashed lines — enough tiles to fill a whole 4×4 grid.", "var(--secC)")}
  <p class="tiles-note"><b>For grown-ups:</b> 24 tiles — a full 4×4 needs sixteen, and spares always help.
  Keep them with the envelope from booklet 1a.</p>
  <div class="tilegrid">{tiles_1b}</div>''')

# --- W1: remember band + explore + worked example ---
expl = B["explore"]
sheet("1b", 4, f'''{section("Meet the big square", "Left: play first — fill it with tiles any way, then check → and ↓ for twins. Right: watch the new rule work.", "var(--secC)")}
  {band("Do you remember? From last week&rsquo;s pages (booklet 1a)", [band_item_html(i) for i in B["remember_1a"]])}
  <div class="gridrow">
    {griditem("Play first! ✋", grid2d_html(expl["grid"], expl["symbols"], aria="explore grid"))}
    {griditem("Watch the new rule 👀", grid2d_html(bwk["grid"], bwk_syms, focus_cell=[bwk_row, bwk["focus"]], aria="worked example grid"))}
  </div>
  <p style="font-size:15.5px;line-height:1.7;max-width:100ch">👀 → The yellow row is missing <b>{bwk_missing1}</b> and
  <b>{bwk_missing2}</b> — the row alone cannot decide which goes where!<br>
  👀 ↓ Look DOWN the yellow box&rsquo;s column&hellip; <b>{bwk_missing2}</b> is already there. So the yellow box must be
  <b>{bwk_missing1}</b> — and the last box takes {bwk_missing2}. The column decided!</p>
  <div class="parenthint" style="--sc:var(--secC)"><b>For grown-ups:</b> walk through this one example aloud, slowly —
  then stop teaching. Strategies your child finds alone stick better than ones we hand over.</div>''')

# --- W2: recognition — twins in the columns + legal-or-not towers ---
rbs = []
for i, item in enumerate(B["rec_break"]):
    rbs.append(griditem(f"{'ab'[i]} ⭕👯↓", grid2d_html(item["grid"], item["symbols"], aria="finished grid with column twins")))
col_items = "".join(
    f'<div class="griditem">{vcol_html(it["cells"], it["symbols"], aria="column strip")}<span class="glbl">{"abcdef"[i]}</span>{checkopts()}</div>'
    for i, it in enumerate(B["rec_cols"]))
sheet("1b", 5, f'''{section("Twins in the columns!", "Read aloud: every ROW in these two grids is perfect — but down the columns, twins hide! Circle each pair. Then: is each tower allowed? Colour ✓ or ✗.", "var(--secB)")}
  {iconchip("👀 ↓ 👯 ⭕", "rows are fine — the columns hide the twins (two pairs each)", "var(--secB)")}
  <div class="gridrow">{rbs[0]}{rbs[1]}</div>
  <div style="height:3mm"></div>
  {iconchip("👀 ↓ ✓✗", "tower check — every friend exactly once", "var(--secB)")}
  <div class="gridrow" style="gap:5mm">{col_items}</div>''')

# --- W3: recognition — which tile (the column decides) ---
which_items = "".join(
    griditem("ab"[i],
             grid2d_html(it["grid"], it["symbols"], focus_cell=[it["row"], it["focus"]], aria="grid with choice") +
             choices_html(it["choices"], it["symbols"]))
    for i, it in enumerate(B["rec_which"]))
sheet("1b", 6, f'''{section("Which tile goes here?", "Read aloud: two tiles want the yellow box — but only one is allowed. The row cannot decide alone: let the column help you!", "var(--secB)")}
  {iconchip("🤔 👉 ↓", "point to the right tile — and say why the other cannot come", "var(--secB)")}
  <div class="gridrow">{which_items}</div>
  <p style="font-size:14.5px;color:var(--ink-soft);margin:3mm 0 0">🗣 Say it like a puzzle-checker: &ldquo;It cannot be ____, because its column already has one!&rdquo;</p>
  <div class="parenthint" style="--sc:var(--secB)"><b>For grown-ups:</b> this page is the whole new skill of booklet 1b in
  one move — the row leaves two choices, the column removes one. If your child picks right but cannot say why, play it
  out with tiles: put the wrong tile in and check its column together.</div>''')

# --- W4: production, 8 givens ---
p8 = "".join(griditem("abc"[i], grid2d_html(g["grid"], g["symbols"], aria="4 by 4 puzzle"))
             for i, g in enumerate(B["prod8"]))
sheet("1b", 7, f'''{section("Your first big squares", "Pick any one to start — all three are the same level.", "var(--secC)")}
  {iconchip("👀 →↓ ✋", "every friend once per row AND once per column", "var(--secC)")}
  <div class="gridrow">{p8}</div>
  <footer class="legend">Use each of these: <span class="syms">{" ".join(SAFARI)}</span></footer>''')

# --- W5: production, 7 givens ---
p7 = "".join(griditem("abc"[i], grid2d_html(g["grid"], g["symbols"], aria="4 by 4 puzzle"))
             for i, g in enumerate(B["prod7"]))
sheet("1b", 8, f'''{section("More empty boxes", "Same rule — a little more thinking. Tiles, or draw ✏️ if you like!", "var(--secC)")}
  {iconchip("👀 →↓ ✋✏️", "place tiles — or draw the friends yourself", "var(--secC)")}
  <div class="gridrow">{p7}</div>
  <footer class="legend">Use each of these: <span class="syms">{" ".join(SAFARI)}</span></footer>''')

# --- W6: production, 6 givens, draw, band, no symbol bank (fading support, B10) ---
p6 = "".join(griditem("abc"[i], grid2d_html(g["grid"], g["symbols"], aria="4 by 4 puzzle"))
             for i, g in enumerate(B["prod6"]))
sheet("1b", 9, f'''{section("Sky puzzles — draw them! ✏️", "New pictures, easy to draw: sun, moon, star, cloud. No tiles this time — and no helper row. You know the rule by heart now!", "var(--secC)")}
  {iconchip("👀 →↓ ✏️", "draw each missing picture yourself", "var(--secC)")}
  <div class="gridrow">{p6}</div>
  {parenthint("var(--secC)",
              "Pick one empty box. Which pictures are already in its row? And in its column? Who is left?",
              "You used the column to decide — the row could not tell you, and you found the trick!")}''')

# --- W7: Beauty page ---
sheet("1b", 10, f'''{section("Pattern painting 🎨", "Read aloud: no rule to obey here — make a tile pattern that is the SAME on both sides of the line, like butterfly wings.", "var(--secD)")}
  {band("Do you remember? From your earlier pages", [band_item_html(i) for i in B["remember_mid"]])}
  {iconchip("🦋 ✋🎨", "make it mirror — then colour it in", "var(--secD)")}
  <div class="gridrow" style="align-items:center">
    {grid2d_html([[0, 0, 0, 0]] * 4, SAFARI, aria="empty pattern grid")}
    <p style="max-width:52mm;font-size:15px;line-height:1.7">The middle is the fold line.<br>Left side = right side!<br><br>Try one with tiles first, then draw and colour your favourite.</p>
  </div>
  {MYTHINK}''')

# --- W8: find the mistake 4x4 ---
bm = B["mistake"]
sheet("1b", 11, f'''{section("The fix-it page 🔧", "Read aloud: this grid is finished — but ONE box is wrong. One friend appears twice in a row AND twice in a column. Circle both pairs of twins, then say which box to fix.", "var(--secB)")}
  {iconchip("👀 →↓ 👯 ⭕", "find the twins across AND down — they point to the wrong box", "var(--secB)")}
  <div class="gridrow" style="align-items:center">
    {grid2d_html(bm["grid"], bm["symbols"], aria="finished grid with one mistake")}
    <p style="max-width:56mm;font-size:15px;line-height:1.7">🗣 Say it like a puzzle-checker:<br>&ldquo;This box must be ____,<br>because its row has twins<br><b>and</b> its column has twins!&rdquo;</p>
  </div>
  {MYTHINK}
  {parenthint("var(--secB)",
              "Which friend do you see twice in one row? Now look — is it twice in a column too? Where do they cross?",
              "You followed the row AND the column to the very box where they cross — that is real detective work!")}''')

# --- W9: provocation + make your own ---
bpv = B["provocation"]
sheet("1b", 12, f'''{section("Star page ⭐", "A grid with two answers, and a puzzle factory of your own.", "var(--sun)")}
  <div class="special">
    <span class="sptitle">⭐ The trickster grid — it has TWO answers!</span>
    <div class="gridrow" style="align-items:center">
      {grid2d_html(bpv["grid"], bpv["symbols"], aria="two-answer grid")}
      <p style="max-width:52mm;font-size:15px;line-height:1.7">Solve it with tiles&hellip; then shuffle them off and find the OTHER answer! Which one do you like better, and why? 😄</p>
    </div>
  </div>
  <div style="height:5mm"></div>
  <div class="create-box">
    <span class="cptitle">🎨 Make your own 4×4!</span>
    <div class="gridrow" style="align-items:center">
      {grid2d_html([[0, 0, 0, 0]] * 4, SAFARI, aria="empty grid")}
      <p style="max-width:56mm;font-size:14.5px;line-height:1.7">The puzzle-maker&rsquo;s secret: ✋ fill the WHOLE grid
      first (rows and columns, no twins!)&hellip; then take a few tiles away and give it to a grown-up.
      👀 Check their answer — you are the puzzle boss now!</p>
    </div>
  </div>''')

# --- unlock trial + stamp + capability ---
t1, t2 = B["trial"]
sheet("1b", 13, f'''{section("The unlock trial 🗝️", "For grown-ups — read this box first.", "var(--secC)")}
  <div class="trialbox"><b>How to run it (5 minutes, no test feeling):</b> when the last pages felt easy, offer ONE of
  these two fresh grids as &ldquo;today&rsquo;s puzzle&rdquo;. Your child solves it <b>alone</b> (tiles or pencil) and
  <b>checks it themselves</b> — every row →, every column ↓, no twins. On a different day, <b>at least 3 days later</b>,
  offer the second grid the same way. Both solved and self-checked without help = the node is mastered. No scores, no
  timer, no red pen — if a grid goes wrong, smile, shelve it, and try again another week: it only means &ldquo;not
  yet&rdquo;.</div>
  <div style="height:4mm"></div>
  <div class="gridrow">
    {griditem("Trial 1 — one day", grid2d_html(t1["grid"], t1["symbols"], aria="trial grid 1"))}
    {griditem("Trial 2 — another day (3+ days later)", grid2d_html(t2["grid"], t2["symbols"], aria="trial grid 2"))}
  </div>
  <div style="height:4mm"></div>
  <div class="cap">You can solve real rows-and-columns sudoku! 🎉</div>
  <div style="height:3mm"></div>
  <div class="stampbox"><b>Wall poster time:</b> colour in your <b>Picture Sudoku 4×4</b> node and let a grown-up sign
  it. 🗣 Tell them: <i>what can you do now that you couldn&rsquo;t before? What surprised you?</i> (They write it next
  to the node.) The next scroll on the sudoku path — <b>Boxes Join In</b> — is waiting further up the tree.</div>''')

# --- answers 1b ---
sols_1b = []
for lbl, group in [("First squares", B["prod8"]), ("More boxes", B["prod7"]), ("Sky", B["prod6"])]:
    for i, g in enumerate(group):
        sols_1b.append(mini_sol(f"{lbl} {'abc'[i]}", grid2d_html(g["solution"], g["symbols"], "mini")))
sols_1b.append(mini_sol("Fix-it grid", grid2d_html(bm["solution"], bm["symbols"], "mini")))
for i, s in enumerate(bpv["solutions"]):
    sols_1b.append(mini_sol(f"Trickster {i + 1}", grid2d_html(s, bpv["symbols"], "mini")))
sols_1b.append(mini_sol("Trial 1", grid2d_html(t1["solution"], t1["symbols"], "mini")))
sols_1b.append(mini_sol("Trial 2", grid2d_html(t2["solution"], t2["symbols"], "mini")))
colcheck_key = ", ".join(f"{'abcdef'[i]} {'✓' if it['legal'] else '✗'}" for i, it in enumerate(B["rec_cols"]))
bwhich_key = ", ".join(f"{'ab'[i]} = {it['symbols'][it['answer'] - 1]}" for i, it in enumerate(B["rec_which"]))
fixit_key_b = (f"the wrong box was row {bm['wrong_cell'][0] + 1}, column {bm['wrong_cell'][1] + 1} — "
               f"{bm['symbols'][bm['wrong_value'] - 1]} should be {bm['symbols'][bm['correct_value'] - 1]}")
sheet("1b", 14, f'''{section("Answers", "No peeking until you have tried! Twins across or down always mean: try that box again.", "var(--sun)")}
  <div class="sols">{"".join(sols_1b)}</div>
  <div style="height:4mm"></div>
  <p class="keyline"><b>Column check:</b> {colcheck_key} &nbsp;·&nbsp; <b>Which tile?</b> {bwhich_key}</p>
  <p class="keyline"><b>Fix-it grid:</b> {fixit_key_b}.</p>
  <p class="keyline"><b>Twins in the columns:</b> grid a and grid b each hide two pairs — every pair sits in one column, and the two pairs share the same two swapped boxes.</p>''')

# ---------------------------------------------------------------- write out

sheets = [s.replace('<section class="sheet', f'<section id="sheet-{i + 1}" class="sheet', 1)
          for i, s in enumerate(sheets)]

tpl = (D / "booklet-1a1b-template.html").read_text(encoding="utf-8")
out = tpl.replace("__BOOK_HTML__", "\n".join(sheets))
assert "__BOOK_HTML__" not in out, "placeholder not replaced"
(D / "animal-sudoku-1a1b.html").write_text(out, encoding="utf-8")

working = 10 + 9
total = len(sheets)
print(f"built {total} sheets -> {D / 'animal-sudoku-1a1b.html'} ({len(out)} chars)")
print(f"page budget check (B18, pair as a whole): {total} pages total (spec 20-28); "
      f"{working} working pages (spec ~16-20, 8-10 two-page spreads); "
      f"booklet 1a = 14 pages (10 working), booklet 1b = 14 pages (9 working)")
