"""Generate the puzzles for the first sudoku booklet.

- 3x3 puzzles are latin squares (each symbol once per row and column).
- 4x4 puzzles are shidoku (rows, columns and the four 2x2 boxes).
- Every puzzle is carved from a full solution one cell at a time and is only
  accepted while it still has exactly one solution.

Output: booklets/sudoku/puzzles.json (UTF-8, emoji symbols included).
"""

import json
import random
from pathlib import Path

SEED = 20260830
random.seed(SEED)

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "booklets" / "sudoku" / "puzzles.json"


def allowed(grid, size, use_boxes, r, c, v):
    for i in range(size):
        if grid[r][i] == v or grid[i][c] == v:
            return False
    if use_boxes:
        br, bc = (r // 2) * 2, (c // 2) * 2
        for i in range(br, br + 2):
            for j in range(bc, bc + 2):
                if grid[i][j] == v:
                    return False
    return True


def count_solutions(grid, size, use_boxes, limit=2):
    grid = [row[:] for row in grid]
    found = []

    def solve():
        if len(found) >= limit:
            return
        for r in range(size):
            for c in range(size):
                if grid[r][c] == 0:
                    for v in range(1, size + 1):
                        if allowed(grid, size, use_boxes, r, c, v):
                            grid[r][c] = v
                            solve()
                            grid[r][c] = 0
                            if len(found) >= limit:
                                return
                    return
        found.append([row[:] for row in grid])

    solve()
    return found


def full_solution(size, use_boxes):
    grid = [[0] * size for _ in range(size)]

    def fill():
        for r in range(size):
            for c in range(size):
                if grid[r][c] == 0:
                    values = list(range(1, size + 1))
                    random.shuffle(values)
                    for v in values:
                        if allowed(grid, size, use_boxes, r, c, v):
                            grid[r][c] = v
                            if fill():
                                return True
                            grid[r][c] = 0
                    return False
        return True

    assert fill()
    return grid


def carve(solution, size, use_boxes, target_blanks):
    """Remove up to target_blanks cells while the puzzle stays uniquely solvable."""
    grid = [row[:] for row in solution]
    cells = [(r, c) for r in range(size) for c in range(size)]
    random.shuffle(cells)
    blanks = 0
    for r, c in cells:
        if blanks >= target_blanks:
            break
        saved = grid[r][c]
        grid[r][c] = 0
        if len(count_solutions(grid, size, use_boxes)) == 1:
            blanks += 1
        else:
            grid[r][c] = saved
    return grid, blanks


THEMES_3 = [
    ("Pets", ["\U0001F436", "\U0001F431", "\U0001F430"]),            # dog cat rabbit
    ("Farm", ["\U0001F42E", "\U0001F437", "\U0001F414"]),            # cow pig chicken
    ("Fruit", ["\U0001F34E", "\U0001F34C", "\U0001F347"]),           # apple banana grapes
    ("Under the Sea", ["\U0001F41F", "\U0001F419", "\U0001F980"]),   # fish octopus crab
]
THEMES_4 = [
    ("Safari", ["\U0001F981", "\U0001F418", "\U0001F992", "\U0001F435"]),        # lion elephant giraffe monkey
    ("Under the Sea", ["\U0001F41F", "\U0001F419", "\U0001F980", "\U0001F42C"]), # fish octopus crab dolphin
    ("Farm", ["\U0001F42E", "\U0001F437", "\U0001F414", "\U0001F411"]),          # cow pig chicken sheep
    ("Little Bugs", ["\U0001F41D", "\U0001F41E", "\U0001F98B", "\U0001F40C"]),   # bee ladybug butterfly snail
]

# (section, size, kind, theme_index_or_None, target_blanks) — difficulty ramps up.
SPECS = (
    [("A", 3, "picture", i % 4, b) for i, b in enumerate([3, 3, 4, 4, 5, 5, 5, 6])]
    + [("B", 3, "number", None, b) for b in [4, 5, 5, 6]]
    + [("C", 4, "picture", i % 4, b) for i, b in enumerate([6, 6, 7, 7, 8, 8, 9, 10])]
    + [("D", 4, "number", None, b) for b in [10, 11, 12, 12]]
)

puzzles = []
for idx, (section, size, kind, theme_idx, target) in enumerate(SPECS, start=1):
    use_boxes = size == 4
    solution = full_solution(size, use_boxes)
    grid, blanks = carve(solution, size, use_boxes, target)

    if kind == "picture":
        theme_name, symbols = (THEMES_3 if size == 3 else THEMES_4)[theme_idx]
    else:
        theme_name, symbols = "Numbers", [str(n) for n in range(1, size + 1)]

    # verification: stored solution is valid and is the puzzle's only solution
    sols = count_solutions(grid, size, use_boxes)
    assert len(sols) == 1 and sols[0] == solution, f"puzzle {idx} failed verification"

    puzzles.append(
        {
            "id": idx,
            "section": section,
            "size": size,
            "kind": kind,
            "theme": theme_name,
            "symbols": symbols,
            "blanks": blanks,
            "grid": grid,
            "solution": solution,
        }
    )
    print(f"#{idx:02d} sect {section} {size}x{size} {kind:7s} {theme_name:13s} blanks {blanks}/{target}")

OUT.write_text(
    json.dumps({"seed": SEED, "puzzles": puzzles}, ensure_ascii=False, indent=1),
    encoding="utf-8",
)
print(f"\nWrote {len(puzzles)} verified puzzles to {OUT}")
