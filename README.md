# Kids Learning

A learning system for children: a fully detailed program for the **last kindergarten year through school year 3 (ages ~5–9)** — academics plus the life stratum (practical life, safety, music, movement, body & health) — extending as a Civilization-style skill tree through coarser middle/high-school milestones to nine career end-goals, with printable exercise booklets. See the framework's scope rulings (docs/methodology/combined-framework.md) for what the home system owns vs what school delivers.

## Folder structure

```
kids-learning/
├── README.md                  ← you are here
├── docs/
│   ├── research/              ← 4 researcher reports (methodologies, cognitive science,
│   │                            national curricula incl. Estonian, skill trees & careers)
│   ├── methodology/           ← combined-framework.md — the unified pedagogical framework
│   │                            (conflicts between methodologies explicitly resolved)
│   └── reviews/               ← critique logs: 5 review loops + 2 gap reviews + fix verification
├── STATE.md                   ← live project status + resume instructions (read first)
├── curriculum/
│   ├── learning-path.md       ← the master skill tree: tiers, nodes, prerequisites,
│   │                             9 career end-goals; contains a machine-readable JSON block
│   ├── learning-path.json     ← extracted canonical graph (regenerated, do not hand-edit)
│   ├── skill-tree-template.html
│   └── skill-tree.html        ← interactive viewer (published as artifact)
├── booklets/
│   └── sudoku/
│       ├── animal-sudoku-1a1b.html    ← Booklet 1a+1b: the spec-conforming entry pair
│       │                                 (ages 5–6; print once, staple into two thin booklets)
│       ├── puzzles-1a1b.json          ← its generated puzzles, each verified unique-solution
│       ├── booklet-1a1b-template.html
│       ├── animal-sudoku-booklet.html ← v0 PROTOTYPE (predates the framework's booklet
│       │                                 ladder; superseded by 1a/1b — kept for reference)
│       ├── puzzles.json               ← v0 prototype data
│       └── booklet-template.html      ← v0 prototype template
└── scripts/
    ├── generate_booklet1_pair.py ← generator for the 1a/1b entry pair (change SEED for fresh puzzles)
    ├── build_booklet1_pair.py    ← renders puzzles-1a1b.json + template → animal-sudoku-1a1b.html
    ├── generate_sudoku.py     ← v0 prototype generator
    ├── build_booklet.py       ← v0 prototype build
    ├── extract_learning_path.py ← extracts + validates the JSON graph from learning-path.md
    └── build_skill_tree.py    ← injects learning-path.json into the viewer template
```

## How the content was produced

1. **Research** — 4 parallel researcher agents: child-centered methods (Montessori, Waldorf, Reggio Emilia…), cognitive science of learning, national curricula for ages 5–9 (Estonian, Finnish, UK, US, Singapore), and skill-tree/career-competency design.
2. **Synthesis** — a curriculum architect merged the research into one conflict-free framework; a learning-path designer built the career skill tree from it.
3. **Review** — 5 improvement loops (3 planned + 2 convergence passes), each with 2 independent critical reviewers (pedagogical soundness; practicality & completeness) followed by an editor applying the fixes; converged at v1.4 with 0 critical / 0 major. Afterwards: 2 independent gap reviews by education-professional critics (docs/reviews/gap-review-*.md).

## Booklet pipeline

To regenerate or make a new sudoku booklet:

```bash
python scripts/generate_sudoku.py   # new puzzles.json (edit SEED / SPECS for variety)
python scripts/build_booklet.py     # rebuild animal-sudoku-booklet.html
```

Every puzzle is carved from a full solution and accepted only while it still has **exactly one solution**. Difficulty ramps by section: A (3×3 pictures) → B (3×3 numbers) → C (4×4 pictures, box rule) → D (4×4 numbers).

## Next booklet ideas

- Mazes & pre-writing line tracing (fine motor, Tier 0)
- Number bonds to 10 with pictures (Tier 0–1)
- Pattern sequences (logic, Tier 0–1)
- First word building / phonics (Tier 1)
- Clock & calendar (Tier 2)
