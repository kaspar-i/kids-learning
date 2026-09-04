"""Generate puzzles-1a1b.json - all verified content for entry booklets 1a and 1b.

Spec (framework combined-framework.md section 4.4, S-ladder + note 4, and the B-rules):
- Booklet 1a = the sorting/pattern warm-up content plus S1: rows-only strips and
  2x2 double-row grids, cut-out picture tiles, ONE new mechanic (B7):
  "no repeats in a row" (age band 4.5-5.5).
- Booklet 1b = S2: 4x4 picture sudoku with rows AND columns (NO box rule - the
  2x2-box rule arrives only at S3), 6-8 givens (the deliberately eased ramp,
  section 4.4 note 2), tiles -> then draw (B9), ONE new mechanic: columns join rows.

Engine guarantees (kept from scripts/generate_sudoku.py, code copied not imported
so the v0 prototype stays untouched):
- seeded and reproducible (single RNG, fixed seed);
- every production puzzle is carved from a full solution and verified to have
  EXACTLY ONE solution (B15), with the stored solution matching the carve source;
- the two provocation puzzles are verified to have EXACTLY TWO solutions (B19);
- every find-the-mistake / rule-breaker item is verified to contain exactly one
  doubled symbol (B16), with rows-legal-columns-broken construction for 1b's
  column-teaching pages;
- difficulty ramps inside each booklet (strip length 3 -> 4 -> two rows at once;
  givens 8 -> 7 -> 6 with tiles -> draw).

Output: booklets/sudoku/puzzles-1a1b.json (UTF-8, emoji symbols included).
"""

import json
import random
import sys
from itertools import permutations
from pathlib import Path

SEED = 20260904
rng = random.Random(SEED)

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "booklets" / "sudoku" / "puzzles-1a1b.json"

CHECKS = {"unique": 0, "two_sol": 0, "mistake": 0, "recognition": 0}

# --------------------------------------------------------------------------
# Latin-square engine (rows + columns only; NO boxes anywhere in 1a/1b - S3 owns the box rule)
# --------------------------------------------------------------------------

def allowed(grid, size, r, c, v):
    for i in range(size):
        if grid[r][i] == v or grid[i][c] == v:
            return False
    return True


def count_solutions(grid, size, limit=3):
    grid = [row[:] for row in grid]
    found = []

    def solve():
        if len(found) >= limit:
            return
        for r in range(size):
            for c in range(size):
                if grid[r][c] == 0:
                    for v in range(1, size + 1):
                        if allowed(grid, size, r, c, v):
                            grid[r][c] = v
                            solve()
                            grid[r][c] = 0
                            if len(found) >= limit:
                                return
                    return
        found.append([row[:] for row in grid])

    solve()
    return found


def full_solution(size):
    grid = [[0] * size for _ in range(size)]

    def fill():
        for r in range(size):
            for c in range(size):
                if grid[r][c] == 0:
                    values = list(range(1, size + 1))
                    rng.shuffle(values)
                    for v in values:
                        if allowed(grid, size, r, c, v):
                            grid[r][c] = v
                            if fill():
                                return True
                            grid[r][c] = 0
                    return False
        return True

    assert fill()
    return grid


def carve(solution, size, target_blanks):
    grid = [row[:] for row in solution]
    cells = [(r, c) for r in range(size) for c in range(size)]
    rng.shuffle(cells)
    blanks = 0
    for r, c in cells:
        if blanks >= target_blanks:
            break
        saved = grid[r][c]
        grid[r][c] = 0
        if len(count_solutions(grid, size, limit=2)) == 1:
            blanks += 1
        else:
            grid[r][c] = saved
    return grid, blanks


def latin_exact_givens(size, givens, max_tries=500):
    """A rows+columns puzzle with exactly `givens` givens and a unique solution."""
    target = size * size - givens
    for _ in range(max_tries):
        sol = full_solution(size)
        grid, blanks = carve(sol, size, target)
        if blanks == target:
            sols = count_solutions(grid, size, limit=2)
            assert len(sols) == 1 and sols[0] == sol, "uniqueness verification failed"
            CHECKS["unique"] += 1
            return grid, sol
    raise RuntimeError(f"could not carve a unique {size}x{size} with {givens} givens")


# --------------------------------------------------------------------------
# S1 strip engine (rows-only rule)
# --------------------------------------------------------------------------

def strip_count(cells, n):
    """Number of row-permutations of 1..n consistent with the givens."""
    cnt = 0
    for perm in permutations(range(1, n + 1)):
        if all(g == 0 or g == p for g, p in zip(cells, perm)):
            cnt += 1
    return cnt


def make_strip(n, blank_at):
    """Rows-only strip, one blank -> unique by B15 (verified, not assumed)."""
    sol = list(range(1, n + 1))
    rng.shuffle(sol)
    cells = [0 if i == blank_at else v for i, v in enumerate(sol)]
    assert strip_count(cells, n) == 1, "strip not unique"
    CHECKS["unique"] += 1
    return {"cells": cells, "solution": sol}


def make_breaker(n):
    """Finished strip with exactly one doubled symbol (one twin pair)."""
    sol = list(range(1, n + 1))
    rng.shuffle(sol)
    cells = sol[:]
    i = rng.randrange(n)
    j = rng.choice([k for k in range(n) if k != i])
    cells[i] = cells[j]
    dup = cells[i]
    assert cells.count(dup) == 2, "breaker must contain exactly one twin pair"
    assert sorted(set(cells)) != sorted(range(1, n + 1))
    CHECKS["mistake"] += 1
    return {"cells": cells, "dup": dup, "dup_positions": sorted([i, j]), "fixed": sol}


def make_2x2():
    """S1's 2x2: TWO rows at once, rows-only rule (columns may repeat - that is
    exactly the point 1b will later change). One blank per row -> unique."""
    rows, sols = [], []
    for _ in range(2):
        sol = [1, 2]
        rng.shuffle(sol)
        b = rng.randrange(2)
        rows.append([0 if i == b else v for i, v in enumerate(sol)])
        sols.append(sol)
    total = strip_count(rows[0], 2) * strip_count(rows[1], 2)
    assert total == 1, "2x2 rows-only grid not unique"
    CHECKS["unique"] += 1
    return {"rows": rows, "solution": sols}


# --------------------------------------------------------------------------
# Symbol sets (B14: familiar animals/food; tiles standardised on ONE cast so the
# tile sheets stay cuttable - the recurring cast is also the B5 narrative wrapper)
# --------------------------------------------------------------------------

SAFARI = ["\U0001F981", "\U0001F418", "\U0001F992", "\U0001F435"]   # lion elephant giraffe monkey
SKY = ["☀️", "\U0001F319", "⭐", "☁️"]      # sun moon star cloud (easy to DRAW - B9 draw stage)
FOOD3 = ["\U0001F34E", "\U0001F964", "\U0001F36A"]                  # apple cup cookie (Life page: set the table)
PETS3 = ["\U0001F436", "\U0001F431", "\U0001F430"]                  # decoration-only sets for recognition pages
SEA4 = ["\U0001F41F", "\U0001F419", "\U0001F980", "\U0001F42C"]
FARM4 = ["\U0001F42E", "\U0001F437", "\U0001F414", "\U0001F411"]
BUGS4 = ["\U0001F41D", "\U0001F41E", "\U0001F98B", "\U0001F40C"]

# --------------------------------------------------------------------------
# Booklet 1a - S1 (mechanic: "no repeats in a row") + sorting/pattern warm-up
# --------------------------------------------------------------------------

b1a = {}

# Warm-up spread content (the sorting-and-attention content section 4.4 folds into 1a)
b1a["sorting"] = [
    {"cells": [PETS3[0], PETS3[1], FOOD3[0], PETS3[2]], "odd": 2},
    {"cells": [FOOD3[0], SEA4[0], FOOD3[2], FOOD3[1]], "odd": 1},
    {"cells": [BUGS4[0], BUGS4[2], FARM4[1], BUGS4[3]], "odd": 2},
]
b1a["patterns"] = [  # continue the pattern by placing a tile (safari tiles exist)
    {"symbols": SAFARI, "cells": [1, 4, 1, 4, 1, 0], "answer": 4},          # AB
    {"symbols": SAFARI, "cells": [2, 3, 3, 2, 3, 0], "answer": 3},          # ABB
    {"symbols": SAFARI, "cells": [1, 2, 3, 1, 2, 0], "answer": 3},          # ABC
]

# Explore + ONE worked example (GP7/B10: exploration precedes the worked example)
b1a["explore"] = {"symbols": SAFARI[:3], "cells": [0, 0, 0]}
_w = make_strip(3, 1)
b1a["worked"] = {"symbols": SAFARI[:3], **_w}

# Recognition battery (2 pages, before any production - CR15/B10)
b1a["rec_break"] = []
for n, syms in [(3, PETS3), (3, FOOD3), (4, SEA4), (4, FARM4)]:
    item = make_breaker(n)
    item["symbols"] = syms
    b1a["rec_break"].append(item)
    CHECKS["recognition"] += 1

b1a["rec_legal"] = []
for legal, (n, syms) in zip([True, False, True], [(3, SAFARI[:3]), (3, BUGS4[:3]), (4, SEA4)]):
    if legal:
        sol = list(range(1, n + 1))
        rng.shuffle(sol)
        item = {"cells": sol, "legal": True, "symbols": syms}
    else:
        br = make_breaker(n)
        item = {"cells": br["cells"], "legal": False, "symbols": syms, "dup": br["dup"]}
    b1a["rec_legal"].append(item)
    CHECKS["recognition"] += 1

b1a["rec_which"] = []
for n, syms in [(3, SAFARI[:3]), (3, PETS3), (4, SAFARI)]:
    s = make_strip(n, rng.randrange(n))
    p = s["cells"].index(0)
    answer = s["solution"][p]
    distractor = rng.choice([v for v in s["cells"] if v != 0])
    choices = [answer, distractor]
    rng.shuffle(choices)
    b1a["rec_which"].append({"symbols": syms, "cells": s["cells"], "solution": s["solution"],
                             "choices": choices, "answer": answer})
    CHECKS["recognition"] += 1

# Production buffets (B11: >=3 same level before any step up; one difficulty per page, B7)
b1a["prod3"] = [{"symbols": SAFARI[:3], **make_strip(3, pos)} for pos in [0, 2, 1, rng.randrange(3)]]
b1a["prod4"] = [{"symbols": SAFARI, **make_strip(4, pos)} for pos in [1, 3, 0, 2]]
b1a["prod22"] = [{"symbols": [SAFARI[0], SAFARI[3]], **make_2x2()} for _ in range(4)]

# Life page (B13 / S1 row: "set the table" - same rows-only logic in a real-world costume)
b1a["life"] = {"symbols": FOOD3, "rows": [make_strip(3, pos) for pos in [2, 0, 1]]}

# Find-the-mistake page (B16): three finished strips, exactly one hides a twin pair
_fm_good1 = list(range(1, 5)); rng.shuffle(_fm_good1)
_fm_good2 = list(range(1, 5)); rng.shuffle(_fm_good2)
_fm_bad = make_breaker(4)
_fm_strips = [{"cells": _fm_good1, "bad": False}, {"cells": _fm_bad["cells"], "bad": True},
              {"cells": _fm_good2, "bad": False}]
rng.shuffle(_fm_strips)
b1a["mistake"] = {"symbols": SAFARI, "strips": _fm_strips,
                  "bad_index": next(i for i, s in enumerate(_fm_strips) if s["bad"]),
                  "dup": _fm_bad["dup"], "fixed": _fm_bad["fixed"]}

# Provocation page (B19): a strip with TWO answers - find both
_ps = list(range(1, 4)); rng.shuffle(_ps)
_pb = rng.sample(range(3), 2)
_prov_cells = [0 if i in _pb else v for i, v in enumerate(_ps)]
assert strip_count(_prov_cells, 3) == 2, "provocation strip must have exactly two solutions"
CHECKS["two_sol"] += 1
_prov_sols = [list(perm) for perm in permutations(range(1, 4))
              if all(g == 0 or g == p for g, p in zip(_prov_cells, perm))]
b1a["provocation"] = {"symbols": SAFARI[:3], "cells": _prov_cells, "solutions": _prov_sols}

# Remember band for late-1a pages (B18 Band-1: elapsed-time labels, days scale)
_rb = make_breaker(3)
_rb["symbols"] = PETS3
b1a["remember"] = [
    {"type": "breaker", **_rb},
    {"type": "pattern", "symbols": SAFARI, "cells": [4, 1, 4, 1, 0], "answer": 4},
]

# --------------------------------------------------------------------------
# Booklet 1b - S2 (mechanic: "columns join rows"), 4x4, 6-8 givens, tiles -> draw
# --------------------------------------------------------------------------

b1b = {}

b1b["example_solved"] = {"symbols": SAFARI, "grid": full_solution(4)}

def two_blank_row_item(symbols):
    """Full 4x4 minus two cells of one row: the row alone cannot decide, the
    column can - the teaching shape for 'columns join rows'. Verified unique."""
    sol = full_solution(4)
    r = rng.randrange(4)
    c1, c2 = sorted(rng.sample(range(4), 2))
    grid = [row[:] for row in sol]
    grid[r][c1] = 0
    grid[r][c2] = 0
    sols = count_solutions(grid, 4, limit=2)
    assert len(sols) == 1 and sols[0] == sol
    CHECKS["unique"] += 1
    u1, u2 = sol[r][c1], sol[r][c2]
    # verify the pedagogy: the wrong choice for (r,c1) really is blocked by column c1
    assert any(sol[i][c1] == u2 for i in range(4) if i != r)
    return {"symbols": symbols, "grid": grid, "solution": sol,
            "row": r, "cols": [c1, c2], "focus": c1,
            "answer": u1, "wrong": u2}

b1b["worked"] = two_blank_row_item(SAFARI)

# Recognition battery page 1: rows all legal, COLUMNS broken (swap two cells in one row)
b1b["rec_break"] = []
for syms in [SAFARI, SEA4]:
    sol = full_solution(4)
    r = rng.randrange(4)
    c1, c2 = sorted(rng.sample(range(4), 2))
    grid = [row[:] for row in sol]
    grid[r][c1], grid[r][c2] = grid[r][c2], grid[r][c1]
    for row in grid:                       # every row is still a permutation
        assert sorted(row) == [1, 2, 3, 4]
    bad_cols = []
    for c in range(4):
        col = [grid[i][c] for i in range(4)]
        dups = {v for v in col if col.count(v) == 2}
        if dups:
            v = dups.pop()
            bad_cols.append({"col": c, "dup": v,
                             "rows": [i for i in range(4) if grid[i][c] == v]})
    assert len(bad_cols) == 2, "swap must break exactly two columns"
    CHECKS["mistake"] += 1
    CHECKS["recognition"] += 1
    b1b["rec_break"].append({"symbols": syms, "grid": grid, "solution": sol,
                             "bad_cols": bad_cols})

# Recognition battery page 2: legal-or-not COLUMN strips + which-tile-goes-here
b1b["rec_cols"] = []
flags = [True, False, True, False, False, True]
for legal in flags:
    if legal:
        col = list(range(1, 5)); rng.shuffle(col)
        b1b["rec_cols"].append({"cells": col, "legal": True, "symbols": FARM4})
    else:
        br = make_breaker(4)
        b1b["rec_cols"].append({"cells": br["cells"], "legal": False,
                                "symbols": FARM4, "dup": br["dup"]})
    CHECKS["recognition"] += 1

b1b["rec_which"] = []
for syms in [SAFARI, BUGS4]:
    item = two_blank_row_item(syms)
    choices = [item["answer"], item["wrong"]]
    rng.shuffle(choices)
    item["choices"] = choices
    b1b["rec_which"].append(item)
    CHECKS["recognition"] += 1

# Production buffets: 8 -> 7 -> 6 givens (S2's eased 6-8 range, note 2), 3 per level (B11)
def prod_grid(symbols, givens, mode):
    grid, sol = latin_exact_givens(4, givens)
    return {"symbols": symbols, "grid": grid, "solution": sol,
            "givens": givens, "mode": mode}

b1b["explore"] = prod_grid(SAFARI, 8, "place")
b1b["prod8"] = [prod_grid(SAFARI, 8, "place") for _ in range(3)]
b1b["prod7"] = [prod_grid(SAFARI, 7, "place-or-draw") for _ in range(3)]
b1b["prod6"] = [prod_grid(SKY, 6, "draw") for _ in range(3)]   # draw stage: drawable symbols

# Find-the-mistake (B16): one overwritten cell -> one animal doubled in its row AND column
_sol = full_solution(4)
_r, _c = rng.randrange(4), rng.randrange(4)
_grid = [row[:] for row in _sol]
_wrong_v = rng.choice([v for v in range(1, 5) if v != _sol[_r][_c]])
_grid[_r][_c] = _wrong_v
_row_dups = [c for c in range(4) if _grid[_r][c] == _wrong_v]
_col_dups = [r for r in range(4) if _grid[r][_c] == _wrong_v]
assert len(_row_dups) == 2 and len(_col_dups) == 2
CHECKS["mistake"] += 1
b1b["mistake"] = {"symbols": SAFARI, "grid": _grid, "solution": _sol,
                  "wrong_cell": [_r, _c], "wrong_value": _wrong_v,
                  "correct_value": _sol[_r][_c]}

# Provocation (B19): a 4x4 with exactly TWO solutions
def make_two_solution_grid(symbols, max_tries=300):
    for _ in range(max_tries):
        grid, sol = latin_exact_givens(4, 6)
        givens_cells = [(r, c) for r in range(4) for c in range(4) if grid[r][c] != 0]
        rng.shuffle(givens_cells)
        for r, c in givens_cells:
            saved = grid[r][c]
            grid[r][c] = 0
            sols = count_solutions(grid, 4, limit=3)
            if len(sols) == 2:
                CHECKS["two_sol"] += 1
                return {"symbols": symbols, "grid": [row[:] for row in grid],
                        "solutions": sols}
            grid[r][c] = saved
    raise RuntimeError("no two-solution grid found")

b1b["provocation"] = make_two_solution_grid(SAFARI)

# Unlock-trial grids (learning-path section 7: the node's check ships with its booklet;
# framework 5.2 Archetype A - two sittings >=3 days apart, fresh items)
b1b["trial"] = [prod_grid(SAFARI, 6, "free"), prod_grid(SAFARI, 6, "free")]

# Remember bands (B18 Band-1 elapsed-time keying)
_rb1 = make_strip(3, 1)
_rb2 = make_breaker(4)
_rb2["symbols"] = SEA4
b1b["remember_1a"] = [    # "from last week's pages (booklet 1a)"
    {"type": "missing", "symbols": PETS3, **_rb1},
    {"type": "breaker", **_rb2},
]
_rb3 = make_breaker(4)    # a column strip judged legal-or-not
_rb3["symbols"] = FARM4
_rb4 = make_strip(4, 2)
b1b["remember_mid"] = [   # "from your earlier pages"
    {"type": "legalcol", "cells": _rb3["cells"], "legal": False, "symbols": FARM4, "dup": _rb3["dup"]},
    {"type": "missing", "symbols": SAFARI, **_rb4},
]

# --------------------------------------------------------------------------
# Write + summary
# --------------------------------------------------------------------------

data = {
    "seed": SEED,
    "spec": "framework section 4.4 S1-S2 entry pair (note 4); B7 one mechanic per booklet; "
            "B15 unique solutions verified; B16 mistakes verified; B19 provocations = exactly 2 solutions",
    "sets": {"safari": SAFARI, "sky": SKY, "food": FOOD3},
    "b1a": b1a,
    "b1b": b1b,
}

OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")

prod_1a = len(b1a["prod3"]) + len(b1a["prod4"]) + len(b1a["prod22"]) + len(b1a["life"]["rows"])
prod_1b = len(b1b["prod8"]) + len(b1b["prod7"]) + len(b1b["prod6"]) + len(b1b["trial"]) + 1  # +explore
print("booklet 1a: %d verified-unique production items (4x 3-strip, 4x 4-strip, "
      "4x 2x2 double-row, 3x set-the-table row)" % prod_1a)
print("booklet 1b: %d verified-unique 4x4 grids (1 explore@8 + 3@8 + 3@7 + 3@6 givens + 2 trial@6)" % prod_1b)
print("verification counters: %s" % CHECKS)
print("all uniqueness / two-solution / mistake assertions passed")
print("wrote %s" % OUT)
