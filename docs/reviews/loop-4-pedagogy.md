# Review Loop 4 — Pedagogical Soundness (convergence pass)

**Reviewer focus:** verify the loop-3 fixes hold; report only issues that would mislead a user, contradict the research evidence, break the data contract, or make textual claims provably false.
**Documents reviewed in full:** `docs/methodology/combined-framework.md` (v1.3), `curriculum/learning-path.md` (v1.3). Research reports re-consulted on every citation the loop-3 edits touched (R1 §2.1/BR4/§8.1; R2 §10/§13/Siegler & Booth; R3 §5–§7/Suggate; R4 A6.7/C1).
**Method:** the JSON block was extracted and re-validated mechanically (parse, unique ids, reference resolution, acyclicity, tier monotonicity, edge and cross-domain census, bridge derivation with the framework §6 exclusion lists, fan-in, trunk ancestor-closure, per-career highlight sets, scoped boss rule, keystone census, `check`-field validity, intra-tier chain lengths, leaf/orphan scan, ageBand/tier consistency) — and additionally diffed against `curriculum/learning-path.json` and the `DATA` constant embedded in `curriculum/skill-tree.html`.
**Date:** 2026-08-30.

---

## 0. Verification — everything from loop 3 HOLDS

All machine-verified against the actual v1.3 JSON and prose:

- **Counts:** 97 nodes (18/18/17/25/10/9 per tier — §1 table, §7 and invariant 4 all agree; tiers 0–3 = 78); **124 edges**; **31 raw cross-domain edges (exactly "31 of 124")**; 14 roots, all tier 0; fan-in ≤ 2 except `t5-research-project` = 3; acyclic; no later-tier edges; every non-tier-0 node has ≥ 1 prereq.
- **Bridges:** applying the §6 exclusion lists mechanically leaves exactly `lit-letter-knowledge → mot-letter-formation` and `mot-letter-formation → log-sudoku-symbols` — the named 2-bridge list reproduces; the two loop-3 edges (`spa-build-diagram → spa-scale-drawings`, `dig-scratchjr → dig-block-projects`) and both re-parented edges are intra-branch as claimed. The "exactly two EF out-edges in tiers 0–3" claim is also exact.
- **M1 fixed and verified:** `common_trunk` is now 26 ids, ancestor-closed (zero violations), and **all eight careers' computed highlights (closure ∪ trunk) now contain the full English strand** (`lit-en-phonics-1/2`, `lit-en-oral-3`, `lit-en-reading`) — the five-careers-need-no-English display lie is gone. The `t4-english-fluent` in/out decision is now stated explicitly with a rationale.
- **M2 fixed:** the strip-borne consolidation retest is a ruled mechanism (3–4 items over two consecutive strips, ~2/strip, all-correct, re-queue on error), the weekly item arithmetic is done and correct (5–6 × 4 = 20–24), sampling priority is ruled, retests capped at 2 nodes/week on different days. (One wording nit remains — minor 4 below.)
- **M3 fixed:** B18 is now 8–10 working spreads; 2 booklet sessions/week × 8–10 spreads = 4–5 weeks ≈ one month — the equivalence is now arithmetically true; the ~1-week rung exists (a′); Band 1 keys gaps to elapsed time; GP8's day/week/month/quarter ladder and B18's rungs now agree.
- **M4 fixed:** node cadences subordinated to the §3 template; `num-tables-1`/`num-times-tables` minutes now ride the fluency-maintenance sessions + strips, `dig-typing` rides the booklet/project sessions; "daily" prescriptions abolished outside strips. Band-4 arithmetic closes (20 + 20–40 + 40 ≤ 100). (The cap that came with this fix has a scoping bug — finding 1 below.)
- **M5 fixed:** Band-2 phonics dose is ~10–12 min, explicitly placed on CR3's ramp, with the whole-diet clause addressed ("dose + strip must leave the session a playful remainder").
- **M6 fixed:** §4.4's every-level checklist now names the 2–3-recognition-page introduction battery; CR15's provenance claim is corrected (verified against R1 — line 60's "pages 2–6 are recognition tasks… roughly 3:1" is in R1's page grammar; R1 §8.1's checklist indeed omits it).
- **M7 fixed:** entry point split into booklets 1a/1b, each one new mechanic; B7 holds with no carve-out, consistently stated in §4.4 note 4, the tier-0 walkthrough, the node card, and §7 first-consumers.
- **M8 fixed:** §5.4 argues dose adequacy (1:1 dosing, older-starter efficiency via Suggate — verified present in R3 §7's annotated list, and R3 §7 *is* the bibliography — prepared oral base) and installs the quarterly GPC-trajectory lag trigger with the third-session lever.
- **Loop-3 minors m1–m10 all fixed and verified:** GP10 decoding-onset curation order (matches R2 line 192 verbatim in spirit); invariant 4 cites R4 C1's real ~120–160 (verified at R4 line 137); CR14/§5.4 cite R3 §6 = Implications (verified); scope line says "middle lasteaed year"; `lit-letter-knowledge` "writes OR builds"; quests "week-to-month-scale"; English encoding sub-ticks in phonics-1/2; keystones defined in GP13 and tagged (exactly 22, matching the stated composition: 2 bosses + 8 quests + 12 branch-leg caps); `ef-attention-persist` ramped (2-step entry / 3-step mastery) and `check: "mixed"`; Band-2 English row rewords sight words as tricky-words-within-SSP.
- **Loop-3 practicality issues all fixed:** `spa-scale-drawings` (tier 3 MOT-SPA exists; engineer spine and §3 Band-4 motor row updated; `t4-design-build` re-parented); `dig-block-projects` (tier-2 DIG rung; walkthrough sentence now true; decay argument on the card); cluster consolidation ruled + `check` field machine-readable (all values valid; all 8 quests single-shot); `lit-comprehension`/`lit-composition` language-of-check ruled on cards and §7; `t5-financial-analysis` gap named on the card and in §3; `dig-beebot-arrows` entry ramp; `sci-observe-senses` third exercise added; `num-numbers-100` "builds with digit cards."
- **Data contract:** the md JSON block, `curriculum/learning-path.json`, and the `DATA` constant inside `curriculum/skill-tree.html` are **byte-identical in content** (verified by parse-and-compare). All v1.2 node ids retained; the two new nodes are additions, no renames — viewer-safe.

The graph and the derived display products are now clean. What remains is small, operational-prose only, and none of it touches the JSON.

---

## 1. Findings

### F1 (MAJOR, wording-scope, one-sentence fix) — the ≤2-concurrent-training-grounds cap contradicts the Band-2/3 templates it sits next to

The loop-3 subordination rule (§3) states, and §5.6 repeats as the feasibility argument: "**at most two training-ground nodes may sit in Practicing concurrently** … so the per-node lines can never sum past the session row."

Three paragraphs above, the binding Band-2 template schedules **three** training-ground strands running concurrently every week — 2 phonics-led sessions (`lit-en-phonics-1`), 2 number-led sessions (a staged `num-*` fluency node), and the letter-formation dose, which the template itself calls "**the third training-ground strand at this band**." All three are tier-1 nodes banded 6–7; for most of the koolieelik year all three sit in Practicing simultaneously. Band 3 is the same shape (phonics-2 + a numeracy stage + `mot-handwriting-auto`, with `lit-reading-fluency` nominally Practicing too, school-evidenced). CR1 *mandates* all three explicit strands. Followed literally, the cap forces a family or a tooling audit to bench one evidence-mandated strand at exactly the band where all three switch on; followed charitably, the cap means "don't *add* training grounds beyond what the band's template already prices" — which is clearly the intent (the surrounding paragraph is about node cadences never adding time on top of the template), but is not what the sentence says. The budget genuinely closes at Band 2 (the template partitions the week; letter formation rides warm-up pages), so the *conclusion* in §5.6 is true — the stated *reason* is false against the system's own canonical schedule.

**Fix (both occurrences, §3 and §5.6):** scope the cap — e.g. "at most two training-ground nodes **whose dose occupies a template session slot**; a strand whose minutes ride warm-up pages (letter formation at Band 2) or that is school-evidenced (`lit-reading-fluency`) does not count against the cap" — or equivalently "no training-ground nodes in Practicing beyond the band template's named strands."

### F2 (minor) — §3 Band-3 direct-instruction cell runs times tables a band early against the graph

Band 3 (7–8, grade 1) direct-instruction row: "Phonics→spelling; **times tables via spaced retrieval**." But table *retrieval* is `num-tables-1`, tier 3, banded 8–9; the same table's Band-3 math-frontier row says only "×/÷ as equal groups/arrays"; and the tier-2 walkthrough rules "concept before drill … table retrieval waits for tier 3" (R3 §5 multiplication-timing row). This reads like a pre-CR14 remnant (in v1.0 Band 3 was labeled grade 2, where tables belong). Softened by CR9's 7–9 glow window and mastery-pull, but the cell is the "what do I drill this year" row and it points a parent at drills the tree schedules a band later. **Fix:** reword the cell, e.g. "number-fact retrieval within 20/100; first tables late in the band as mastery allows."

### F3 (minor) — §4's "reachable from tier-2 prerequisites" is false for one quest

Learning-path §4: "each career's first highlighted door is its tier-3 quest node (`quest-*`), **reachable from tier-2 prerequisites**." `quest-scientist`'s prereqs are `sci-fair-test` (**tier 3**) and `ef-plan-check` (tier 1) — the deliberate loop-2 rewiring. True for the other seven. **Fix:** one clause — "…tier-2 prerequisites (`quest-scientist` alone additionally requires tier-3 `sci-fair-test`, by design)."

### F4 (minor) — "no third pass exists" undercounts its own sittings

§5.1's new provenance sentence: "This is R4 A6.7's two-pass model with the second pass distributed into strips — mastery check (pass one), strip-borne retest (pass two); **no third pass exists**." But §5.2's Archetype A defines the mastery check itself as "passed twice ≥3 days apart" (the boss checks say so inline), so the road to Consolidated is three check sittings — two mastery sittings plus the distributed retest — where R4 line 153's model is two. The *mechanism* is fully specified and fine; only the equivalence claim is loose, in a document that prides itself on honest counting. **Fix:** "mastery check (one check *event*, run in two sittings per §5.2) plus the strip-borne retest; no further check event exists."

### F5 (minor) — `sci-observe-senses` check-archetype default is inconsistent with the `num-money-time` precedent

`sci-observe-senses` is a cluster whose sub-check (c) — "talks about weather and seasons **across a week**," exercised via the week-long weather strip — is not a <10-minute Archetype-A table check; the structurally identical weeks-long-chart sub-check in `num-money-time` earned that node `check: "mixed"`. `sci-observe-senses` carries no `check` field and so defaults to "A", which tells tooling to schedule a strip-borne ≥2-week re-pass of the whole bank. Harmless in practice, but the `check` field exists precisely so tooling never re-derives archetypes from prose. **Fix:** stamp `check: "mixed"` naming (c) single-shot-at-completion (or reword (c) as a <10-min Friday-talk performance check and leave the default).

### F6 (minor, carry-over of loop-3 m11 — the one loop-3 item not addressed) — unexplained check-interval deviation on the second boss

`num-times-tables` `mastery_check`: "passed twice **at least a week apart**" vs. Archetype A's default "≥3 days" (which `num-addsub-20` follows). Almost certainly deliberate (a bigger automaticity claim earns a longer verification gap) — but the traceability convention flags every deviation, and this one is silent. **Fix:** append "(deliberately longer than Archetype A's ≥3 days: a full-korrutustabel automaticity claim earns a wider verification gap)" — or align to ≥3 days.

### F7 (minor) — "thin" entry booklets vs. B18's binding size

§4 preamble makes every B-rule binding for every booklet; B18 pins "a booklet is 20–28 pages … 8–10 two-page working spreads." §4.4 note 4 ships the entry point as "a pair of **thin** booklets — 1a and 1b." Both cannot hold: if 1a/1b each met B18's size they would not be thin. Spacing labels are unaffected (Band 1 keys gaps to elapsed time), but the booklet-1 author must guess which rule wins — the exact silent-deviation pattern loop 3's M7 removed one level up. **Fix:** one sentence in B18 or §4.4 note 4 — e.g. "the entry pair splits one standard booklet's page budget between 1a and 1b (B18's size applies to the pair, its cadence to whatever the child works)."

### F8 (minor) — the keystone definition is not quite mechanically checkable, and §7 asks tooling to check it

§7 validation includes "the keystone set matching GP13's definition." A mechanical reading of GP13 (c) — "era-capping chain-end of a branch's tier-3 line, one per leg where a branch has several" — yields two untagged tier-3 chain-ends: `dig-typing` (covered — GP13 excludes micro-nodes and the card says "Micro-node") and **`num-fractions`** (not covered: it is neither micro nor mid-chain — it is a genuine tier-3 chain-end feeding only `t4-algebra-data`, arguably numeracy's second leg). The tag-is-normative clause makes this legal, but the stated exclusion categories don't explain this particular exclusion, so a validator cannot reproduce the 22 without a special case. **Fix:** either tag `num-fractions` as a keystone (defensible: it caps the fractions leg) or add its category to GP13's exclusion note (e.g. "checkpoint-content nodes that continue directly into a same-strand tier-4 bundle are mid-arc, not era-capping").

---

## 2. Verdict

**Converged.** Every loop-3 fix — all eight majors, all nine practicality issues, ten of eleven minors — is verifiably in place, and every structural, arithmetic and display claim I could recompute (node/edge/bridge/trunk/keystone/highlight censuses, the B18 cadence arithmetic, the strip-item arithmetic, the band budgets, the citation corrections against R1–R4) now holds, including the three-way consistency of the md block, `learning-path.json`, and the viewer's embedded data. Nothing remaining touches the JSON, the graph invariants, or any pedagogical ruling. The one finding above minor (F1) is a scoping error in a single sentence stated twice — the cap added by loop-3's own fix contradicts the band templates beside it — and its charitable intent is recoverable from context; it should be patched in a touch-up along with the seven one-line minors, none of which warrants another full loop.
