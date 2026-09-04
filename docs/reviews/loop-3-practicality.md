# Loop 3 Review — Practicality & Completeness

**Reviewer focus:** reachability, prerequisite sanity, JSON/prose consistency, parent usability, difficulty-ramp realism, gaps/dead-ends/orphans; verification that loop-1/loop-2 fixes actually hold.
**Documents reviewed in full:** `docs/methodology/combined-framework.md` (v1.2), `curriculum/learning-path.md` (v1.2). Research reports spot-checked for cited rules (R4 C2 granularity, C3.2 fan-in).
**Method:** the JSON block was extracted and validated mechanically (Python: parse, reference resolution, toposort acyclicity, tier monotonicity, fan-in census, per-tier node counts, edge count, cross-domain edge census, trunk ancestor-closure, per-career ancestor closures and highlight sets (closure ∪ trunk), consumer/orphan analysis, boss-ancestry scan scoped per the framework §3 rule, domain-coverage-per-tier matrix). Everything in §0 below is machine-verified, not eyeballed.

---

## 0. Verification — the v1.2 claims and prior-loop fixes that HOLD

All mechanically confirmed against the actual JSON:

- **Parses as JSON**; 95 nodes, 8 careers, 22 trunk ids; all `prereqs`/`quest`/`capstone_prereqs`/`common_trunk` references resolve; ids unique.
- **Acyclic**; every edge points same-tier-or-earlier; **exactly 122 edges**; **exactly 31 raw cross-domain edges** (the §1 "31 of 122" claim is exact, not approximate); tier counts 18/18/16/24/10/9 match §7 exactly.
- **Fan-in ≤ 2 everywhere except `t5-research-project` at 3** — as claimed.
- Every non-tier-0 node has ≥1 prereq; every zero-prereq node is tier 0 (14 roots, matching the walkthrough's "fourteen roots, eighteen nodes").
- **`common_trunk` is ancestor-closed** (verified edge-by-edge).
- **Scoped boss rule holds**: no tier-0–3 non-numeracy branch node has either boss milestone in its hard ancestry (quests excluded per the carve-out, and every quest that does inherit a boss — entrepreneur, finance via `num-money-time`/`num-addsub-100` — is legitimately carved out).
- **Counted-bridge list verified by hand against the framework §6 exclusion lists**: of the 31 cross-domain edges, 29 fall under a *named* exclusion (LOG↔DIG spine ×3, MOT transcription ×3, NUM→SCI measurement ×1, EF out-edges ×2, quest fan-in ×7, tier-4/5 fan-in ×13), leaving exactly `lit-letter-knowledge → mot-letter-formation` and `mot-letter-formation → log-sudoku-symbols` — the two named bridges. The count is reproducible as promised.
- **Longest intra-tier chain is 3** (tier 0: sorting→robot→arrows; tier 1: bonds-10→±10→±20; tier 3: tables-1→tables→problems); the 9-node cross-tier numeracy spine claim is correct.
- **Every career's closure terminates in tier-0 roots**; every tier-5 vestibule is consumed by at least one `capstone_prereqs`; the "at least two tier-5 vestibules in ancestry except lawyer and entrepreneur" claim checks out (finance and engineer reach 2 via `t5-advanced-math` in ancestry).
- **Only three deliberate leaves in tiers 0–3**: `mot-gross-body` (documented as observation-only), `log-sudoku-master` (S-ladder self-containment is documented doctrine, §4.4), and the 8 quest nodes (doors, not feeders). No accidental orphans.
- Loop-2 fixes verified in place and consistent: booklet #1 day-1 start (sudoku root + demoted soft edges), the binding weekly template, `num-numbers-100`'s own check (deadlock resolved), `lit-en-oral-3` + twin-prereq `lit-en-reading`, `dig-typing` re-parented onto transcription, quest soft-prereq "assumes you can also…" lines, placement sweep ruling, `mot-gross-body`, tier-0 checks authored with the poster, Estonian sourcing note, Needs-polish semantics, grade anchoring (CR14) now consistent across every table and node card I checked.

This is a genuinely well-audited graph. The remaining defects below are mostly at the seams the validator doesn't reach: what the *highlight computation* shows the child, what the *branch columns* look like per era, and arithmetic in the booklet cadence prose.

---

## 1. MAJOR — The `common_trunk` omits the entire English literacy strand; five of eight careers' highlighted paths show no English beyond age-6 listening

**Machine-verified:** computing highlight = ancestor closure of (`quest` ∪ `capstone_prereqs`) ∪ `common_trunk` per §1, the highlighted sets for **manager, lawyer, engineer, entrepreneur, and finance contain zero of** {`lit-en-phonics-1`, `lit-en-phonics-2`, `lit-en-oral-3`, `lit-en-reading`, `t4-english-fluent`}. Only doctor, software-engineer and scientist inherit English literacy, via `t4-english-fluent` under `t5-research-project`/`t5-software-craft`.

Why this is wrong by the documents' own logic:

- The trunk exists precisely because "closures alone would tell a child that Lawyer needs no math and Doctor needs no self-regulation" (§1). By the same argument, the current trunk tells a child that **Lawyer needs no English** — in a system whose entire printed output is English, whose flagship home responsibility is the 2–3-year English SSP program (GP10, CR2, CR14's first scheduled run-ahead), and whose weekly template gives *every* child 2 phonics-led sessions at Bands 2–3 regardless of career.
- Both §1 (learning-path) and the framework §6 career-capstone note describe the trunk as containing "literacy roots with **both fluency legs**." The actual 22-id list contains the Estonian leg (`lit-ee-decoding → lit-reading-fluency`) and the English **oral** leg only through tier 1 (`lit-en-oral-vocab`, `lit-en-oral-2`). There is no English fluency leg. The description and the data disagree; poster coloring computed from the data will render the disagreement visibly on five wonders.
- Even the oral leg is truncated: `lit-en-oral-3` (tier 2) is excluded, so the trunk's English story *stops at age ~7* on the poster.

**Fix:** add `lit-en-phonics-1`, `lit-en-phonics-2`, `lit-en-oral-3`, `lit-en-reading` to `common_trunk` (the set remains ancestor-closed automatically — phonics-1's ancestors `lit-phonemic-awareness`/`lit-letter-knowledge` are already in the trunk; en-reading's twin prereqs are the two other additions). Trunk becomes 26 ids. Update the "22 node ids" count in learning-path §1, §6 preamble, and framework §6/GP12 note, and correct "both fluency legs" to name the three legs actually included. Decide explicitly whether `t4-english-fluent` also belongs (defensible either way at the coarse layer; if excluded, say why on the tier-4 walkthrough).

---

## 2. MAJOR — The motor-spatial branch has no tier-3 node: the spatial trunk goes dark from age ~8 to ~10

**Machine-verified:** the domain-coverage matrix shows tier 3 covers 9 of 10 domains — `motor-spatial` is absent (its only tier-3 presence is `quest-engineer`, which the poster renders *above* the branch columns and which is a one-week single-shot event, not skill progression).

The spatial chain runs `spa-pattern-blocks` (5–6) → `spa-shapes-symmetry` (6–7) → `spa-build-diagram` (7–8) → **nothing** → `t4-design-build` (10–13). This directly contradicts:

- Framework §6 MOT-SPA: spatial is "a *trunk*, not an engineer-leaf … most curricula under-serve it; ours should not" (Wai: spatial predicts STEM independently and is *highly trainable at 5–9* — i.e., precisely the band where our branch stops).
- Framework §3 Band 4 motor row promises "Handwriting speed for extended writing; ruler; typing introduced; 1 cm cells" — typing landed in DIG, ruler work in NUM/SCI, and handwriting-speed has no tier-3 node (the tier-2 `mot-handwriting-auto` training ground stops emitting tree events once consolidated).
- The engineer spine (§4) at the 8–9 band consists of `quest-engineer` plus a creativity node; the career whose defining aptitude is spatial has no spatial work at all during the last fully-detailed year of the system.

**Fix:** add one tier-3 MOT-SPA node — e.g. `spa-scale-drawings` (reads and produces simple scale drawings and 3-D nets; draws top/front/side views of a built model; plots points on a labeled grid/first coordinates), prereq `spa-build-diagram`, careers [engineer, doctor, scientist]. Re-parent `t4-design-build` from `spa-build-diagram` onto it (fan-in stays 2). Then update the counts this touches: tier 3 → 25 nodes, total 96, edge count 123, §5 invariant 4, §7 tier counts — and re-derive the bridge list (the new edge is intra-domain; the count stays 2, but §1 says any edit must re-derive, so do it on the record).

---

## 3. MINOR — The digital branch is empty at tier 2, and the decay-refresh mechanism cannot reach screen skills

The DIG chain jumps from `dig-scratchjr` (tier 1, 6–7) to `dig-scratch` (tier 3, 8–9). The tier-2 walkthrough says "ScratchJr projects deepen" — but there is no node to record that deepening, so the branch column is empty for the whole Builder era (machine-verified: tier 2 covers 9 of 10 domains, `digital` absent).

The practical consequence: `dig-scratchjr` consolidates at ~7 and its decay timer (8–12 weeks, §5.1) expires long before its consumers unlock at ~8.5. The prescribed refresh channel — "its content re-enters booklet warm-ups until refreshed" (§5.1 Needs-polish) — is a **paper** retrieval strip; block coding cannot ride it. As written, the flagship first-screen skill spends a year dimmed with no mechanism to refresh it.

**Fix (either):** (a) add a small tier-2 DIG node (block-projects II: plans a multi-sprite project on paper first, uses loops+events deliberately, fixes own bugs — prereq `dig-scratchjr`, consumer `dig-scratch`), which also fills the empty column; or (b) if the branch gap is accepted, amend §5.6's dim-check note with a screen-skill refresh channel (e.g., one co-used block-coding session per month counts as use, logged on the node's evidence line). (a) is better; it makes the walkthrough sentence true.

---

## 4. MINOR — The B18 booklet cadence arithmetic still doesn't close against the binding weekly template (loop-2 fix incomplete)

B18 (framework §4.3) pins: 10–13 working spreads per booklet, "one working spread per booklet session — the **2–3** booklet/free-choice sessions of the §3 weekly template — so a booklet spans **≈3–5 weeks ≈ one month**," and hangs the retrieval-gap labels on it (booklet N−1 "≈1 month" back, N−3/N−4 "≈1 season" back).

But the binding §3 template schedules **exactly 2** booklet sessions in every band that schedules them at all (Band 2: 2; Band 3: 2; Band 4: 2; Band 1: no fixed slot). No band has 3. At 2 spreads/week, 10–13 spreads = **5–6.5 weeks**, not 3–5. The gap labels drift accordingly: N−1 ≈ 6 weeks (not "≈1 month"), N−3/N−4 ≈ 4.5–6.5 months (not "≈1 season" — a season is 3). The whole point of the v1.2 revision was "expanding gaps under honest labels"; the labels are once again dishonest by ~50–100%.

**Fix (pick one, state it):** (a) trim booklets to 8–10 working spreads (4–5 weeks at 2/week — the "≈ one month" equivalence becomes true); (b) keep 10–13 and relabel: booklet ≈ 5–6 weeks, N−1 ≈ 6 weeks, N−2/N−3 ≈ one season; or (c) schedule 3 booklet sessions at some bands and say which. Whichever wins, delete "2–3" or make some template row actually say 3.

---

## 5. MINOR — Consolidation class is not machine-readable, and mixed clusters fall under no ruling

The §5.1 consolidation-by-type ruling (a loop-2 addition) covers Archetype A (re-pass ≥2 weeks), Archetype B (one further logged instance), and quests/month-scale dispositional nodes (single-shot). Two gaps remain:

1. **No field in the JSON carries the class.** Quests are identifiable via `quest_for`, but "month-scale dispositional" nodes are not: tooling cannot discover that `ef-goal-setting` (month goal chart) is single-shot while `sel-conflict-resolution` is a B-tally, except by reading English prose in `description`. The framework says the ruling exists "for tooling"; tooling has nothing to read.
2. **Clusters with mixed sub-check types are unruled.** `ef-attention-persist` explicitly mixes A and B sub-checks; `num-money-time` mixes two A sub-checks with a weeks-long savings-jar chart (which is exactly the "savings jars" example §5.1 assigns to the single-shot class — but that class ruling attaches to *nodes*, and this node is a cluster, not flagged). Which rule consolidates the node?

**Fix:** add an explicit optional field (e.g. `check: "A" | "B" | "single-shot"`, defaulting to A) to the node schema and stamp the exceptions; add one sentence to §5.1: "a cluster consolidates per its slowest sub-check's class" (or: each sub-check consolidates under its own archetype and the node consolidates when all have).

---

## 6. MINOR — `lit-comprehension` and `lit-composition` sit in language limbo the sourcing note doesn't cover

The §7 Estonian-sourcing note covers exactly three nodes (`lit-ee-decoding`, `lit-reading-fluency`, `lit-writing-sentences`). But `lit-comprehension` and `lit-composition` (tier 3) are on the same Estonian leg — their prereqs are Estonian fluency/writing — while their printed exercises ("non-fiction page on hedgehogs," "story-mountain plan, draft, checklist edit") would be produced by the English-language booklet line. A child at this node is *not* required to read English at that level (`lit-en-reading` is a sibling, not an ancestor), so an English-printed comprehension page is undeliverable to some children who legitimately qualify for the node; an Estonian-printed one is outside the stated production scope.

**Fix:** extend the §7 sourcing note to these two nodes (evidence via Estonian school texts + parent-run question protocol, same support-don't-duplicate stance), or state on the node cards that the booklet-line versions of these exercises assume `lit-en-reading` and are the *second* representation, not the check.

---

## 7. MINOR — No digital literacy anywhere in six careers' highlighted paths; `t5-financial-analysis` promises spreadsheets with no digital ancestry

Machine-verified: the highlighted sets for manager, lawyer, scientist, engineer, entrepreneur, finance and doctor contain **zero DIG-domain nodes** (only software-engineer's does), and `common_trunk` contains none either. Yet `t5-financial-analysis` — capstone for finance *and* manager — says "models scenarios in **spreadsheets**," with no typing, no tools, no digital node in its entire hard ancestry. That's the same missing-load-bearing-edge pattern the doc polices elsewhere (`dig-typing → t4-programming` was added for exactly this reason). Career weighting justifies DIG being *light* for a lawyer; it does not justify a finance path whose own capstone text names a digital tool its chain never provides.

**Fix (cheap):** add `dig-typing` to `t4-money-management`'s or `t5-financial-analysis`'s prereqs is over-heavy at this coarse layer; instead, note it in the §3 tier-5 honesty paragraph as a known decomposition target ("when tier 4–5 decompose, a digital-tools/spreadsheet node enters the money-management chain"), or add basic digital literacy to the trunk conversation alongside issue 1. Pick one; currently the text just contradicts the graph.

---

## 8. MINOR — `dig-beebot-arrows` pitches its mastery bar at the top of the 5–6 band

"Writes and debugs arrow-card programs of **six or more steps** … predicts where a program lands before running it," banded 5–6, in a band whose WM budget is 2–3 chunks (GP5). Cards externalize state (B4), which is why this is minor rather than major, but prediction-before-running a 6-step program is a 6-to-7-year-old behavior in ProgeTiiger-style practice (typical kindergarten Bee-Bot work is 2–4 steps). As the *entry* experience of a root-adjacent node it will undershoot GP17's 70–90% success target for a just-turned-5 starter.

**Fix:** write the ramp into the description the way `num-numbers-100` writes its deliberate deviation: entry at 2–3-step programs, mastery bar at 6+ with prediction — or move the 6+/predict bar into a sub-level tick and set mastery at 4+ steps with prediction on short programs.

---

## 9. MINOR — Two authoring nits in node cards

1. `sci-observe-senses` is a 3-sub-check cluster but ships exercises for only sub-checks (a) and (b); the weather/seasons sub-check (c) has no exercise. Since the node is Mastered only when **all** sub-checks pass (§5.2), the parent has a check with no corresponding activity. Add a third exercise (e.g., the week-long weather-picture strip it already describes).
2. `num-numbers-100`'s inline check says "reads, **writes** and orders number cards to 100," but its only ancestor is `num-counting-cardinality` — numeral *formation* lives in `mot-letter-formation`, a same-tier non-ancestor. A child can legitimately face this check unable to form two-digit numerals. Change "writes" to "builds with digit cards" (the exercises are already card-based) or drop the word.

---

## Summary

The graph itself is in genuinely good shape: every structural claim in §5/§7 survived mechanical verification, previous loops' fixes are real, and the audit trail (named bridge lists, flagged deviations, scoped rulings) is unusually honest. What loop 3 finds is that the *derived products* now lag the graph: the highlight/coloring computation — the thing the child actually sees — omits the system's single most important home-taught strand for five careers (issue 1); two branch columns go dark for a full era each, one of them the branch the framework brags about protecting (issues 2–3); and the booklet cadence prose still doesn't survive multiplication by its own weekly template (issue 4). Issues 1, 2 and 4 should be fixed before the tier-0 poster and booklet #1 ship, because all three are baked into those two deliverables' specs; the rest can ride the next revision.
