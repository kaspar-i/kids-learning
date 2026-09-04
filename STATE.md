# Project state & resume instructions

_Last updated: 2026-09-04 ~14:45 (session c277cb92)_

## Where things stand

| Deliverable | Status |
|---|---|
| Animal Sudoku booklet | ✅ DONE — artifact https://claude.ai/code/artifact/58f19aaf-abcf-4101-ab1b-7bb856405791 |
| Research reports (4) | ✅ DONE — docs/research/ |
| Combined framework | ✅ v1.6 — docs/methodology/combined-framework.md (gap fixes: CR17/CR18/B22, SSP delivery, re-entry protocol, overclaim rewordings) |
| Learning path (108-node graph, 9 careers, 17 roots) | ✅ v1.6 — life stratum (sel-selfcare, sel-safe-well, cre-music-play, mot-gross-2), sci-body-health→quest-doctor, lit-reads-for-fun, num-chance, dig-media-sense |
| Skill-tree viewer | ✅ PUBLISHED at v1.6 — artifact https://claude.ai/code/artifact/112da60a-91f8-4da4-896e-334682a74fa8 |
| Gap reviews by 2 hard critics (user request 2026-09-04) | ✅ DONE and user approved "Everything" — all blocking/important findings applied (see gap-review-*.md) |
| Booklet 1a/1b entry pair (spec-conforming) | ✅ BUILT & PUBLISHED to the Animal Sudoku artifact URL — booklets/sudoku/animal-sudoku-1a1b.html; old booklet marked v0 prototype |
| Gap-fix verification | ✅ CLEAN — 26/27 blocking+important items implemented, 1 deliberate partial (tier-4 tick ladders delegated to the future poster pipeline), 0 missing, no collateral damage; booklet pair solver-verified conformant. Report: docs/reviews/gap-fix-verification.md |
| YouTuber career addition (user request 2026-09-04) | ✅ DONE — v1.5: career "youtuber" 🎬 + quest-youtuber + t4-media-production + t5-creator-business; graph 100 nodes / 130 edges, all invariants re-verified; viewer rebuilt & republished |

## Fine-tuning outcome (loops 4–5)

Workflow `wf_c83aaa07-6c7` COMPLETE — do not resume. Note: its `converged:true` return was coincidental — the loop-5 reviewer AGENTS died on a session usage limit before returning, BUT both had already written full verdicts to docs/reviews/loop-5-*.md: **"Converged, cleanly"**, all loop-4 fixes verified mechanically, nothing blocking. So v1.4 convergence is genuine (verified from the on-disk review files, 2026-09-04).

## After the youtuber addition completes

1. `python scripts/extract_learning_path.py` — must pass (validates graph).
2. Run one verification reviewer over the diff if the editor's summary reports anything uncertain.
3. `python scripts/build_skill_tree.py` — rebuild viewer.
4. Republish `curriculum/skill-tree.html` to artifact 112da60a-91f8-4da4-896e-334682a74fa8 (same file path from session c277cb92, or pass url from another session).
5. Update README.md (8 → 9 careers) and this file; update memory kids-learning-project.md.

## Review-loop history

| Loop | Issues (critical/major) | Result |
|---|---|---|
| 1 | 33 (2c/14m) | fixed → v1.1 |
| 2 | 32 (4c/12m) | fixed → v1.2, graph 78→95 nodes |
| 3 | 27 (0c/10m) | fixed → v1.3, graph 97 nodes |
| 4 | 14 (0c/1m) | fixed → v1.4; both reviewers voted converged |
| 5 | 0 (verification pass) | **CONVERGED** — v1.4 fit for use |

## Standing user preferences for this project

- Quality over speed; more review rounds welcome (loops 4-6 are exactly this).
- User travels; interruptions expected — keep state on disk, keep steps resumable.
- Booklets: printable A4, picture-based for youngest tier; regenerate via scripts/ (change SEED).
- Next booklet candidates listed in README.md.
