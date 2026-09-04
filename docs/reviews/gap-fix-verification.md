# Gap-Fix Verification Report — v1.6 + Entry Booklet Pair

**Role:** verification reviewer (last gate) over the two gap-review implementations: curriculum v1.6 (`curriculum/learning-path.md`, `docs/methodology/combined-framework.md`) and the rebuilt entry booklet pair (`booklets/sudoku/animal-sudoku-1a1b.html`).
**Method:** every BLOCKING and IMPORTANT finding from `gap-review-1-practitioner.md` and `gap-review-2-systems.md` extracted into a checklist and verified against the actual v1.6 text and graph data (not the changelogs); the booklet verified page-by-page against framework §4.4 and the B-rules; the full graph re-verified mechanically by script (52 checks: censuses, acyclicity, references, fan-in, trunk closure, bridge re-derivation, career closures, three-way data sync, booklet puzzle uniqueness).
**Date:** 2026-09-04.

**Verdict: CLEAN.** 26 of 27 deduplicated blocking/important checklist items fully implemented; 1 partial (P1 interim tick ladders — ruled, but authored inline only for `t4-english-fluent`); 0 missing; no collateral damage found. All four editor deviations are coherent as implemented and their stated justifications verified true. Three residual cosmetic observations, none blocking.

---

## 1. Checklist — Review 1 (practitioner)

| Finding | Severity | Implemented? Where | Verdict |
|---|---|---|---|
| **D-1** Booklet contradicts doctrine; §7 overclaims conformity | BLOCKING | Both halves of the fix delivered: (a) booklet **regenerated to spec** as the 1a/1b pair (`animal-sudoku-1a1b.html`, verified in §3 below); (b) old booklet ruled a **superseded v0 prototype** — framework §4.4 note 5 (names each violation: 3×3 grids, digits at 5, several mechanics per booklet, no split/tile sheet, B3 age span), learning-path §7 reworded ("Honesty note (v1.6), replacing the earlier 'exactly as specified' overclaim"), README folder tree labels v0 files | ✅ IMPLEMENTED |
| **D-2** Daily read-aloud simultaneously mandatory and forbidden | BLOCKING | **CR18** (family read-aloud rail): ~10 min daily, exempted *by name* from §3's no-daily-prescriptions rule; named in §3 daily budget + weekly template; **priced in §5.6** (~70 min/week parent row, "previously off the books"); all three `lit-en-oral-*` cards ride it explicitly ("checks run inside sessions, the rail carries only reading and talk"); no-streak/missed-night-is-nothing clause (CR4) | ✅ IMPLEMENTED |
| **I-1** Practical life / self-care | IMPORTANT | `sel-selfcare` tier-0 root, cluster, check B, 3 sub-checks (dressing incl. fastenings, tidying, table job); zero consumers (verified mechanically); §6 SEL root row restored truthfully ("real since v1.6"); R1 research gap flagged (node provenance + CR17) | ✅ IMPLEMENTED |
| **I-2** Safety and health literacy | IMPORTANT | `sel-safe-well` tier-0 root, cluster, check B, 4 sub-checks (real-walk crossings, helkur habit, stranger/lost script + address, water rules); health rhythms routed to B13 Life pages + `sci-body-health`; zero consumers | ✅ IMPLEMENTED |
| **I-3** Gross motor dead-ends at tier 0; swimming invisible | IMPORTANT | `mot-gross-2` tier 1, cluster, check B (water confidence toward the statutory swim course, bike, seasonal skills); §6 MOT-SPA row acknowledges the compulsory ~200 m swimming course as external anchor; §3 Band-2 motor row updated. Deviation: hard edge from `mot-gross-body` instead of soft link — see §4 | ✅ IMPLEMENTED |
| **I-4** Music absent from graph, prose, rulings | IMPORTANT | *Both* acceptable fixes delivered: `cre-music-play` tier-0 root (beat, 4–5 songs, 2–3 Estonian rhymes/poems by heart) **and** the scope ruling (CR17: lasteaed delivers muusika proper) | ✅ IMPLEMENTED |
| **I-5** Estonian cultural belonging | IMPORTANT | Delivered via the review's own alternative: seasonal layer extended to the folk calendar (§3, named feasts, songs join `cre-music-play`); songs/poems by heart in `cre-music-play`; own address in `sel-safe-well`; Estonia-and-symbols named lasteaed-delivered (CR17, §5.4) — with both overclaims trimmed as the review required. Deviation (no `sel-my-estonia` node) — see §4 | ✅ IMPLEMENTED |
| **I-6** Reading for pleasure | IMPORTANT | `lit-reads-for-fun` tier 3, check B (unprompted ≥3× / 2 weeks, child-kept title log); zero consumers (verified); excluded from keystones by extended GP13 rule (no reward/ceremony — GP9 respected); Estonian bedtime read-aloud named protected ritual (CR18 "soil" clause) | ✅ IMPLEMENTED |
| **I-7** Media consumption literacy | IMPORTANT | `dig-media-sense` tier 3 (ad-or-content ×3 real pieces, who-made-this/what-the-app-gets, co-authored watch-time agreement); prereq `dig-block-projects` (creator experience feeds viewer judgment — the review suggested `dig-scratchjr` *or* `dig-block-projects`); soft-highlighted on youtuber path; §2 youtuber profile updated ("the viewer is trained before the creator") | ✅ IMPLEMENTED |
| **I-8** Coverage overclaims §5.4 / §6 | IMPORTANT | §5.4 koolivalmidus claim reworded (covers language/math/motor/social/self-care/safety/time-orientation; "names lasteaed as the delivering source for the rest"; "the tree *plus a normal lasteaed year* double as evidence; the tree alone does not claim to"); §6 "map cleanly" → per-area honest mapping ("the tree plus school together — not the tree alone"); CR17 rules the division so the pattern stops recurring | ✅ IMPLEMENTED |
| **I-9** Parent SSP phonology unaddressed | IMPORTANT | **B22** (per-GPC audio models + per-set parent pronunciation micro-guides, binding per phonics booklet); §5.4 quarterly check listens for parent-transmitted GPC errors, not just coverage; SSP Parent Delivery Mini-Guide a named deliverable shipped before `lit-en-phonics-1` unlocks | ✅ IMPLEMENTED |
| **I-10** Doctor body vocabulary claimed, absent | IMPORTANT | "the human body & health" restored to §6 SCI content cycles; `sci-measure-record` bursts extended (+ body-data exercise); `sci-body-health` carries the vocabulary rung; §2 doctor profile now cites the node ("real since v1.6") | ✅ IMPLEMENTED |
| Damage: I1 four-checkpoint claim (only 3 cards) | (named in scope) | `num-times-tables` card gained the no-deadline checkpoint sentence "added in v1.6 so the four checkpoint nodes really do all say so on their own cards"; verified all four cards (`num-multidigit`, `num-fractions`, `num-problems-data`, `num-times-tables`) carry it | ✅ IMPLEMENTED |
| Damage: D-4 phantom "Assessment rule (A)" class | (named in scope) | §0 traceability convention now cites "§5 mastery/assessment ruling (cited as §5.x)" and documents the phantom class + colliding namespace as dropped | ✅ IMPLEMENTED |

## 2. Checklist — Review 2 (systems)

| Finding | Severity | Implemented? Where | Verdict |
|---|---|---|---|
| **D4/C1** Human body & health missing; doctor seed undelivered | BLOCKING | `sci-body-health` tier 2, cluster, check mixed, 4 sub-checks (body parts/senses-as-organs, healthy habits, 3-step first aid, weeks-long care-for-a-living-thing log — also closing R1's N-2); prereq `sci-observe-senses`; **feeds `quest-doctor`** (swapped for `sci-measure-record` under the fan-in-2 cap, assumes-measuring line on the quest card — exactly the review's suggested mechanism); §6 SCI row + §3 Band-3 science row updated | ✅ IMPLEMENTED |
| **P3** Untrained-parent premise under the by-9 claim | BLOCKING | All three demanded pieces: (a) SSP Parent Delivery Mini-Guide (~10 pages, named first-class deliverable); (b) §5.4 dose-adequacy argument reconditioned ("1:1 counts as the argued advantage **only with the parent-delivery ruling followed**... never on parental goodwill alone"), Nickow/Oreopoulos/Quan weakest-arm caveat named in text; (c) quarterly delivery-quality check ("delivery first, dose second, professional eyes third") | ✅ IMPLEMENTED |
| **D1** Music | IMPORTANT | = R1 I-4: `cre-music-play` + CR17 + §6 corrected | ✅ IMPLEMENTED |
| **D2** PE / swimming | IMPORTANT | = R1 I-3: CR17 scope ruling (school delivers PE + swimming) + `mot-gross-2` observation cluster + §6 MOT-SPA scope honest | ✅ IMPLEMENTED |
| **D3** Mina ja keskkond / health / safety / civics | IMPORTANT | `sel-safe-well` + `sci-body-health` health slice + `num-measure-data` sub-check (d) days-of-week + CR17 civics division + §5.4 narrowed | ✅ IMPLEMENTED |
| **C1** (important half) service leg riding `t5-life-sciences` flavor text | IMPORTANT | Card carries the KNOWN COARSE-LAYER GAP admission ("the `t5-financial-analysis` admission pattern"): zero SEL ancestry named, service milestone promised at decomposition | ✅ IMPLEMENTED |
| **C2** Probability root | IMPORTANT | `num-chance` tier 3 (certain/possible/impossible, spinner comparison by counts, two-dice tally); §2 finance profile updated. Deviation: feeds `t5-advanced-math`, not `t4-algebra-data` — see §4 | ✅ IMPLEMENTED |
| **C3** Media consumption + analytics gap | IMPORTANT | `dig-media-sense` (= R1 I-7) **and** the `t5-creator-business` card admission ("'audience analytics read honestly' presupposes chart-and-data literacy that this chain's hard ancestry does not carry") | ✅ IMPLEMENTED |
| **C4** `t4-english-fluent` steepest un-staged middle | IMPORTANT | Card rewritten: DECOMPOSES FIRST on the §5.2 trigger, names the productive-spoken-English rung ("the missing register added as a real node"), staged graded-reading + English composition, carries the spelling-transfer concession forward ("conceded here so decomposition remembers it"), interim ticks authored inline (graded-reader level, first voluntary retell, first paragraph) | ✅ IMPLEMENTED |
| **C5** Engineer CAD gap unadmitted | IMPORTANT | `t5-applied-engineering` card admission (CAD-lite/data-tools rung at decomposition); learning-path §3 tier-5 paragraph extended to name all five admission-carrying cards consistently ("since v1.6 the admission is applied consistently, not only where loop 3 happened to look") | ✅ IMPLEMENTED |
| **C6** Entrepreneur persuasion/negotiation | IMPORTANT | `t5-venture` card admission (pitch vs. enrichment-only `com-present`, COM leg at decomposition); negotiation's first costume added to `sel-conflict-resolution` (trade-and-swap games) exactly as suggested | ✅ IMPLEMENTED |
| **P1** Tier-4 motivational vacuum | IMPORTANT | Trigger **ruled** (§5.2: frontier enters tier 4 → that branch decomposed within one quarter, owner + trigger named; `t4-english-fluent` first); interim ticks **ruled** for every bundle. Ticks *authored inline* only on `t4-english-fluent`; the rest delegated to the poster pipeline — see §4, deviation 3 | ⚠️ PARTIAL (minor) |
| **P2** Atypical development | IMPORTANT | §5.4 refer-out ruling: four named triggers incl. the bilingual masking asymmetry watched explicitly; refer to eripedagoog/logopeed/Rajaleidja; decay-dimming softened for documented difficulties (the review's exact ADHD-profile concern) | ✅ IMPLEMENTED |
| **P4** Re-entry protocol | IMPORTANT | §5.6 ruled: declared-pause timer suspension + no dimming during a pause; ≥2-week gap → strips-plus-booklet-only week, training grounds re-enter one rung down (different representation), retest queue resets from return date | ✅ IMPLEMENTED |
| **P5** Lag lever cannibalizes breadth budget | IMPORTANT | §5.4 lever sequence: swap capped at one quarter consecutively; squeeze priced (surviving booklet session leans on B13 rotation, warm-up-riding strands unharmed, strips carry the rest); after a capped quarter the lever becomes the P2 triggers, "never more dose" | ✅ IMPLEMENTED |
| **P6** Observation-tally validity | IMPORTANT | §5.2 guard-rails: one-line *described* observation per instance; keystone-level B nodes need a second adult's countersign or outside-context instance; second-hand evidence from named non-family adults explicitly legitimate (also closes R1 N-8) | ✅ IMPLEMENTED |
| **P7** Check administration + language of check | IMPORTANT | §5.2 administration protocol (neutral face, no mid-check hints, first-error-is-information, stop after 2 misses, return ≥3 days with different-representation corrective, no same-day retries) + language ruling (any non-LIT-EN check in either language, read-aloud on request, at every age) | ✅ IMPLEMENTED |
| Damage: I2 STATE.md stale/self-contradictory | nice-to-have (checked) | STATE.md rows now all v1.6, viewer row single and consistent ("PUBLISHED at v1.6") | ✅ IMPLEMENTED |
| Damage: I3 §6 EF "exactly two" gloss | (named in scope) | Gloss added in place ("stated gloss, v1.6... checkable only with this gloss, so the gloss now travels with the claim"); mechanically confirmed: exactly 2 class-(a) edges into branch nodes, exactly 2 EF quest fan-in edges excluded under (c) | ✅ IMPLEMENTED |
| Damage: I4 v1.5 changelog clause | cosmetic (checked) | Framework changelog now reads "no ruling changed — GP12's text was extended to cover the ninth career (the corrected form of v1.5's changelog clause, per gap review 2 I4)" | ✅ IMPLEMENTED |

*(Nice-to-haves were out of scope for this gate but were spot-confirmed delivered where the editor claimed them: N-1 `num-chance`, N-2 care-log in `sci-body-health`, N-3 days-of-week in `num-measure-data`(d), N-4 poems in `cre-music-play`(c), N-5 board-game costume note on `log-sudoku-master`, N-6 observational-drawing costume on `cre-idea-fluency`, N-7 §5.6 multi-child paragraph, N-8 in P6's fix, N-11 calming sub-check in `sel-emotions-turns`, D6 unit breadth on `num-problems-data`, C7 `t4-money-management` softened, P8 tenth-slot first-class ruling in §6, P9 autonomy-inside-dose-sessions ruling in §3.)*

---

## 3. Booklet conformance — `animal-sudoku-1a1b.html` vs framework §4.4 / B-rules

**Verdict: CONFORMS.** Verified page-by-page (28 sheets read in full) and mechanically.

- **One mechanic per half (B7, §4.4 note 4):** 1a teaches exactly one rule — no repeats in a row (S1, rows-only strips and row-independent two-row grids; page 1a·10 explicitly says "up-and-down does not matter yet"). 1b teaches exactly one new rule — columns join in (S2). ✅
- **No digits, no box rule:** mechanically verified — zero digit symbols in any grid; the box rule appears nowhere as content (the sole mention is the closing teaser naming the *next* node "Boxes Join In", which is correct signposting, not teaching). Symbol sets are pictures throughout. ✅
- **Motor ramp (B9/B3):** tiles from page 1 (18 mm tiles in 20 mm cells, tile sheet shipped in *both* halves); drawing offered only late in 1b (1b·8 "tiles or draw", 1b·9 draw-only with deliberately easy sky glyphs). Ages on covers: 1a "~4½–5½", 1b "~5–6" — matching the S1/S2 rows, one grid module per booklet. ✅
- **Recognition before production (B10/CR15 battery):** 1a — worked example (1a·5) → two recognition pages (1a·6 spot-the-twins; 1a·7 legal-or-not + which-tile-goes-here) → production buffet (1a·8–11). 1b — worked example (1b·4) → two recognition pages (1b·5 column-twins + tower check; 1b·6 which-tile with say-why) → production (1b·7–9). 2–3 recognition pages per new mechanic: met (2 each). ✅
- **Explore-first (GP7/B10):** both halves open the mechanic with a free-play grid before the single worked example ("play first", "strategies your child finds alone stick better"). ✅
- **Find-the-mistake (B16):** 1a·12 and 1b·11, each before nothing (production complete), with B17 scripted if-stuck + process-praise footers. ✅
- **Two-solutions provocation (B19):** 1a·13 trickster strip (hand-verified: exactly 2 solutions) and 1b·12 trickster grid (solver-verified: exactly 2). Both marked special. ✅
- **Make-your-own (B10):** 1a·13 (fill-then-erase strips) and 1b·12 (fill the whole grid, remove tiles, "you are the puzzle boss"). ✅
- **Unlock trial in 1b:** 1b·13 — two fresh grids, run ≥3 days apart, solved alone and self-checked, no scores/timer/red pen — matches §5.2 Archetype A (two sittings ≥3 days) and the §5.2 administration protocol's tone. Capability statement + poster/evidence ceremony per B20/GP13. 1a correctly ends with a pencil-tick (partial node), 1b with the node colour-in. ✅
- **Pair-level page budget (B18 as amended loop 4):** 28 pages total, 20 working pages = 10 working spreads *for the pair as a whole* — inside the 20–28-page / 8–10-spread budget. ✅
- **Retrieval (B18 Band-1 elapsed-time keying):** "Do you remember?" bands sample earlier pages by elapsed time ("from last week's pages (booklet 1a)") — the Band-1 exception applied correctly. ✅
- **Puzzle validity (B15):** solver-verified — all 14 posed 4×4s (production, choice, explore, trials) have unique solutions; both tricksters exactly 2; all answer-page grids are valid Latin squares consistent with their givens; 1a strips hand-verified unique. Givens on 1b 4×4s: 6–8 everywhere (S2 spec incl. note 2's deliberate easing). ✅
- Also present: B1/B2 (icon chips + read-aloud lines addressed to the parent), B5 (narrative on covers only), B11 (≥3 same-level puzzles, "pick any order"), B13 (Life: set-the-table page; Beauty: mirror-pattern page; formal puzzles), B14, B17, B19 (date/self-portrait/can-do boxes, my-thinking margins), B20 (capability statements, no per-page rewards).

---

## 4. Editor deviations — coherence check

1. **`num-chance` → `t5-advanced-math` (not `t4-algebra-data`).** Stated justification: `t4-algebra-data` fan-in already at the cap of 2 with both legs load-bearing; tier-skipping edge follows the `num-money-time` (tier 2) → `t4-money-management` (tier 4) precedent. **Verified true:** `t4-algebra-data` prereqs = [`num-fractions`, `num-problems-data`] (both plainly load-bearing for "abstraction over fluent arithmetic"); the cited precedent edge exists; `t5-advanced-math` fan-in is now 2 and its description names the probability lab as the seed's consumer. The alternative would have forced dropping a load-bearing edge or breaching invariant 3. Coherent; finance closure verified to contain `num-chance` ("in the hard closure since v1.6" claim true). ✅
2. **`mot-gross-body` → `mot-gross-2` as a hard edge** (review sketched a soft link). Stated justification: invariant 2 requires every non-tier-0 node to carry ≥1 prereq, and this is the honest candidate. **Verified true:** invariant 2 is real and enforced; the edge passes the load-bearing test (balance/coordination genuinely underlie bike and stroke); `mot-gross-2` has zero consumers (mechanically verified), so the hard edge can never gate desk work — the review's actual concern. ✅
3. **Tick-ladder ruling instead of authored per-bundle ladders** (P1 asked for "three lines each, now"). §5.2 rules ticks for *every* tier-4 bundle ("the extended-fluency tick mechanism extended upward — authored in the poster pipeline"); only `t4-english-fluent` carries its ladder inline. **Coherent with the system's own division of labor** (per-node check specs live in the pipelines, not the learning path — §5.2/§7 convention; tier-0 checks ship with the poster), and the years-away frontier plus the ruled trigger mean no child is exposed meanwhile. But the poster pipeline is itself unbuilt, so nine bundles' ticks are a promise riding a ruling. **⚠️ PARTIAL — acceptable, flagged as the one open thread** (severity: minor; owner exists: poster spec authoring). |
4. **`sel-my-estonia` decomposed rather than authored.** Review I-5 explicitly allowed "a ruling that culture is the seasonal layer + wild nodes — but then §5.4's claim must be trimmed." Implementation delivers *more* than the alternative: rhymes/poems + songs in `cre-music-play` (koolivalmidus memorization item restored), address in `sel-safe-well`, folk calendar as a named §3 scheduling layer under CR17, symbols/civics named lasteaed-delivered, and both overclaims trimmed. Nothing of I-5's substance is lost; no orphan claims remain (§5.4 no longer lists Estonia-and-symbols as tree-covered). ✅

---

## 5. Mechanical results (script: 52 checks)

| Check | Result |
|---|---|
| md JSON block == `learning-path.json` == `skill-tree.html` DATA (deep equality) | ✅ all three v1.6-identical |
| Node count 108; per-tier 21/19/18/29/11/10 | ✅ |
| 136 hard edges; 34 raw cross-domain (~25%) | ✅ |
| 17 roots, all tier 0; every non-tier-0 node ≥1 prereq | ✅ |
| 24 keystones; none of the 8 v1.6 additions keystoned (GP13 exclusions) | ✅ |
| All references resolve (prereqs, careers, quest, capstone_prereqs, trunk); ids unique | ✅ |
| Acyclic; prereqs same-tier-or-earlier | ✅ |
| Fan-in ≤2 everywhere except `t5-research-project` (=3) | ✅ |
| 9 quests, all tier 3, all `check: single-shot` | ✅ |
| Trunk = 26 ids, unchanged from v1.5, ancestor-closed | ✅ |
| Every tier-5 node consumed (capstone_prereqs ∪ edges) | ✅ |
| Every career's closure ∪ trunk contains the full English strand (oral 1–3, phonics 1–2, reading); reaches tier-0 roots; TR6 ≥3 roots/≥3 domains | ✅ |
| Scoped boss rule (no tier-0–3 non-numeracy branch node has a boss ancestor) | ✅ |
| Bridge list re-derived from the §6 definition + exclusion lists: exactly the 2 named (`lit-letter-knowledge → mot-letter-formation`, `mot-letter-formation → log-sudoku-symbols`) | ✅ |
| §6 EF gloss: exactly 2 class-(a) edges into branch nodes; the 2 quest fan-ins excluded under (c) | ✅ |
| v1.6 wiring: `quest-doctor` = {`sci-body-health`, `sel-conflict-resolution`}; `sci-body-health` ← `sci-observe-senses`; `num-chance` ← `num-measure-data`, → `t5-advanced-math`; `mot-gross-2` ← `mot-gross-body`; `dig-media-sense` ← `dig-block-projects`; `lit-reads-for-fun` ← `lit-reading-fluency` | ✅ |
| All six no-gate nodes (`sel-selfcare`, `sel-safe-well`, `cre-music-play`, `mot-gross-2`, `lit-reads-for-fun`, `dig-media-sense`) have zero consumers | ✅ |
| Booklet: 14 posed 4×4s unique-solution; 2 tricksters exactly 2; answers = valid Latin squares; no digits in any grid | ✅ |

---

## 6. Items not delivered / residual observations

**Blocking: none. Major: none.**

1. **⚠️ MINOR — P1 partial:** interim sub-level tick ladders authored inline only for `t4-english-fluent`; the other nine tier-4 bundles get theirs "in the poster pipeline" per the §5.2 ruling. Defensible under the system's own authoring conventions and shielded by the ruled decomposition trigger, but the poster spec is unbuilt, so this is a promise with an owner rather than shipped text. Carry to the poster-spec work item.
2. **COSMETIC — README staleness (pre-existing, R1 D-3a/b nice-to-haves, partially fixed):** line 3 still reads "last year of kindergarten and the first 3 school years" (pre-CR14 anchoring; tier table says middle lasteaed year); the folder-tree annotation still says "the 3 review/improvement loops" while §"How it was built" correctly says 5 loops + 2 gap reviews. The folder tree itself was fixed (json/viewer/scripts now listed; v0 files labeled).
3. **COSMETIC — booklet niggles:** (a) 1b's decorative cover grid is under-constrained (3 completions) — it carries no solve instruction, so B15 does not apply, but a unique-solution cover would be tidier; (b) one "Do you remember?" band item (1a·10) shows the ✋ place-a-tile icon on an 11 mm mini cell while tiles are 18 mm — the child will point or say instead; the 🗣 icon (used for the equivalent 1b·4 item) would be the consistent choice.

*Filed 2026-09-04 — gap-fix verification pass (last gate). Verification script: session scratchpad `verify_v16.py` (52 checks, reproducible against the three data files and the booklet HTML).*
