# Loop 4 Review — Practicality & Completeness (Convergence Pass)

**Reviewer focus:** verification that the loop-3 fixes hold; career reachability from tier 0; acyclic and sensible prerequisites; JSON-vs-prose consistency; usable exercise guidance; difficulty-ramp realism and cadence arithmetic.
**Documents reviewed in full:** `docs/methodology/combined-framework.md` (v1.3), `curriculum/learning-path.md` (v1.3). Research reports spot-checked for every citation the loop-3 fixes touched (R4 C1 node budget, R3 §6 numeracy clock, R1 §2.1/BR4 recognition battery, R2 §10 EE-before-EN, R4 A6.7 consolidation, Suggate in R3). Viewer pipeline (`extract_learning_path.py`, `learning-path.json`, `skill-tree.html`) checked for currency.
**Method:** the JSON block was extracted and validated mechanically (parse, unique ids, reference resolution, toposort acyclicity, tier monotonicity, edge census, fan-in census, per-tier node counts, cross-domain edge census with the framework §6 exclusion lists applied edge-by-edge, trunk ancestor-closure, per-career capstone closures and highlight sets (closure ∪ trunk), English-strand membership per highlight, DIG membership per closure, scoped boss-ancestry scan, keystone census against GP13, `check`-field value validity, tier-3 chain-end census, leaf census, ageBand/tier consistency, intra-tier longest chains). Everything in §0 is machine-verified.

**Verdict up front: CONVERGED.** Every loop-3 major and minor that the v1.3 changelogs claim fixed is actually fixed, and every structural number in both documents is exactly true against the data. What remains is six genuine minors — five are one-sentence label/wording fixes at seams the validator cannot reach, one is a missing template-slot name on a single node card. None blocks the tier-0 poster, booklets 1a/1b, or the strip/retest tooling.

---

## 0. Verification — loop-3 fixes and v1.3 claims that HOLD (all machine-verified)

**Graph and data contract:**
- Parses as JSON; **97 nodes** (18/18/17/25/10/9 per tier — §1 table and §7 match exactly); 8 careers; all `prereqs`/`quest`/`capstone_prereqs`/`common_trunk` references resolve; ids unique; acyclic; every edge same-tier-or-earlier; **exactly 124 edges** as claimed.
- **14 roots, all tier 0**; every non-tier-0 node has ≥1 prereq; ageBand/tier consistent on all 97 nodes.
- Fan-in ≤2 everywhere except `t5-research-project` at 3 — invariant 3 exact.
- **Raw cross-domain edges: exactly 31 of 124 (25.0%)** — the "~25% (31 of 124)" claim is exact. Applying the framework §6 exclusion lists edge-by-edge (EF out-edges ×2 — and exactly two exist, as §6 claims; 7 named corequisites — all present; quest fan-in ×7; tier-4/5 fan-in ×13) leaves **exactly the two named bridges**: `lit-letter-knowledge → mot-letter-formation`, `mot-letter-formation → log-sudoku-symbols`. Invariant 9 reproducible.
- Loop 3's two added edges (`spa-build-diagram → spa-scale-drawings`, `dig-scratchjr → dig-block-projects`) and both re-parents verified intra-branch — the bridge re-derivation note in §1 is correct.
- Scoped boss rule: zero tier-0–3 non-numeracy branch nodes carry either boss in hard ancestry.
- Only documented leaves in tiers 0–3: `mot-gross-body`, `log-sudoku-master`, the 8 quests. No accidental orphans; both new nodes have consumers.
- Longest intra-tier chain 3; the 9-node cross-tier numeracy spine of invariant 5 verified node-by-node.

**Loop-3 issue 1 / M1 (trunk omitted English) — FIXED and holding.** `common_trunk` is 26 ids, ancestor-closed (verified edge-by-edge), and now contains `lit-en-phonics-1/2`, `lit-en-oral-3`, `lit-en-reading`. **All eight careers' computed highlights (closure ∪ trunk) contain the full English strand** — machine-verified per career. The "22" count is gone from both documents; both now describe the three actual legs; the `t4-english-fluent` in/out decision is made explicitly (§1) with a stated reason. Invariant 8 (≥3 tier-0 roots in ≥3 domains per highlight) holds with margin (minimum found: 9 roots, 5 domains).

**Loop-3 issue 2 (spatial dark at tier 3) — FIXED.** `spa-scale-drawings` exists (tier 3, prereq `spa-build-diagram`, consumer `t4-design-build`), the §3 Band-4 motor row and §6 MOT-SPA chain both name the new rung, the engineer spine in §4 runs through it, and all counts were updated correctly (25/97/124 all verified).

**Loop-3 issue 3 (DIG empty at tier 2 / decay gap) — FIXED.** `dig-block-projects` exists (tier 2), `dig-scratch` re-parented onto it, framework §3 Builder row and §6 DIG chain updated. Every tier 0–3 era now covers its branch columns for both previously-dark branches.

**Loop-3 issue 4 / M3 (booklet cadence arithmetic) — FIXED, and the arithmetic now closes.** B18 trims to 8–10 working spreads (16–20 working pages of a 20–28-page booklet — internally consistent); at the template's exactly-2 booklet sessions/week that is 4–5 weeks ≈ one month, so N−1 ≈ 1 month and N−3/N−4 ≈ 3–4 months ≈ a season are now honest labels. The "2–3 sessions" phrase is gone. GP8's ~1-week rung got its own strip rung (a′). Band 1 gets the elapsed-time keying its slot-free template requires.

**Loop-3 issue 5 / M2 (consolidation retest unspecified; class not machine-readable) — FIXED.** §5.1 now defines the strip-borne retest concretely (3–4 items from the check bank across two consecutive strips, all-correct, error path specified, ≤2 nodes queued/week), does the weekly item arithmetic (20–24 items — correct: 5–6 sessions × 4), and rules strip priority. The `check` field (`A`/`B`/`single-shot`/`mixed`) is in the schema and stamped — all values valid, all 8 quests `single-shot`, cluster-consolidation ruled per sub-check. (One wording residue — finding 3 below.)

**Loop-3 issues 6–9 and pedagogy M5–M8, m1–m10 — all FIXED as claimed.** Band-2 phonics dose ~10–12 min on CR3's ramp (both texts agree now); §4.4 every-level checklist carries the 2–3-page recognition battery and CR15's provenance correction matches what R1 actually says (battery in §2.1/BR4, absent from §8.1's table — verified in R1); booklet 1 split 1a/1b per B7 with no carve-out needed, consistently in §4.4 note 4, the tier-0 walkthrough, the node card, and §7; §5.4 argues dose adequacy (Suggate verified present in R3) and adds the quarterly GPC-lag trigger with a named lever; node cadences subordinated to the §3 template with the ≤2-training-grounds cap, and tables/typing re-slotted on their cards; `lit-comprehension`/`lit-composition` carry the language-of-the-check ruling and the §7 sourcing note covers them; the DIG-gap in seven careers is named honestly in §3 and on `t5-financial-analysis` (the "seven of eight" claim is machine-exact); `dig-beebot-arrows` and `ef-attention-persist` have ramped entries; `sci-observe-senses` has its third exercise; `num-numbers-100` says "builds with digit cards"; GP10 rules the EE-before-EN curation order (matching R2 line 192, verified); invariant 4 cites R4's real ~120–160 (verified at R4 line 137); CR14 cites R3 §6, which is really the Implications section (verified); the scope line says middle lasteaed year; `lit-letter-knowledge` allows built names; quests are "week-to-month-scale"; encoding sub-ticks exist in both phonics nodes; keystones are defined in GP13 and tagged — **exactly 22, matching the stated count**, with the boss/quest/chain-end structure GP13 describes.

**Viewer pipeline current:** `learning-path.json` (97 nodes, 26 trunk ids) and `skill-tree.html` both contain the v1.3 nodes; no stale counts embedded; existing node ids unchanged (v1.3 only added ids), so poster/viewer references stay stable.

---

## 1. Remaining findings (all MINOR — none blocks convergence)

### 1. §4 doctor spine names the "SEL chain" without the enrichment label its own rule requires
`learning-path.md` §4 preamble: "where a chain is *not* inside the capstone's hard ancestor closure it is labeled **enrichment**." Machine-verified: **doctor's capstone closure contains zero SEL nodes** (t5-life-sciences/t5-research-project ancestry never touches SEL). Yet the doctor line's parenthetical says "SEL chain for empathy" with no label — the only unlabeled out-of-closure chain in §4 (all other careers' parentheticals were verified in-closure or labeled). SEL does reach doctor's *highlight* via `quest-doctor` (← `sel-conflict-resolution`) and the trunk's SEL core, so the poster is fine; only the prose breaks its own rule. **Fix:** label it — e.g. "SEL chain for empathy — via the quest door and the trunk, not the capstone closure."

### 2. `num-fractions` is an untagged tier-3 chain-end that GP13's exclusion clause doesn't cover
GP13 keystone rule (c): era-capping tier-3 chain-end per branch leg, with "micro-nodes and mid-chain nodes deliberately excluded." Machine census of tier-3 chain-ends (consumers only in tier ≥4) leaves exactly two untagged: `dig-typing` (named a micro-node on its card — covered by the exclusion) and **`num-fractions`** (a full node, not mid-chain — its only consumer is `t4-algebra-data`), which is covered by neither the tag nor the exclusion wording. §7 claims validation includes "the keystone set matching GP13's definition"; on this one node the definition and the tag set disagree. **Fix (either):** tag `num-fractions` keystone (numeracy then caps two legs, like literacy caps three), or add three words to GP13's exclusion ("…and side strands that rejoin the main line at tier 4"). Cosmetically small, but the §7 validation claim should be literally true.

### 3. §5.1's "no third pass exists" collides with §5.2's "passed twice ≥3 days apart"
§5.1 now glosses the mechanism as "R4 A6.7's two-pass model … mastery check (pass one), strip-borne retest (pass two); **no third pass exists**." But Archetype A's mastery check is itself "passed twice ≥3 days apart" (§5.2, and both boss cards), so end-to-end there are three passing events; R4's actual A6.7 model (verified: "mastery check passed twice, ≥2 weeks apart") had two. The *mechanism* is fully specified and internally workable — this is purely the provenance sentence — but a future author could read "two-pass model" as license to collapse the mastery check to one sitting. **Fix:** reword to "no separate retest *session* exists — two verification *stages*: the §5.2 mastery check (itself two sittings), then the strip-borne retest," and drop or qualify the "is R4's two-pass model" equivalence.

### 4. Boss 2's retest interval deviates from the Archetype-A default without the house-style flag
`num-times-tables` inline check: "passed twice at least **a week** apart"; Archetype A's default (§5.2) and boss 1's inline check: "≥3 days." Almost certainly deliberate (a bigger fluency claim earns a longer verification gap), but the doctrine flags every other deliberate deviation in place (S2 givens, `num-numbers-100` range, B18 trim) and this one is silent — leftover loop-3 pedagogy m11, not claimed fixed in the v1.3 changelog and not fixed. **Fix:** one clause on the card ("a week, not the Archetype-A 3 days — the larger fluency claim earns the longer gap") or align to the default.

### 5. `mot-handwriting-auto`'s cadence line names no template slot, against the binding §3 subordination rule
§3 (binding): "every exercise-cadence line in the learning path must name the template slot that carries it." The loop-3 audit note names tables and typing; sweep of all remaining cadence-bearing exercise lines shows read-alouds, weather strips and goal-chart ticks are life-side (exempt under §3's "everything outside the session is ordinary childhood"), leaving exactly one desk-work violation: `mot-handwriting-auto`'s "**Weekly** copy passage" (Band 3, a training-ground node) names no slot. **Fix:** name it — e.g. "rides the booklet sessions' form-drawing/warm-up lane (§3 template), like letter formation at Band 2."

### 6. `spa-scale-drawings` quietly assumes scale arithmetic its ancestry never provides
The new node's check includes "draws it to a stated scale," but its ancestry is pure MOT-SPA — no numeracy at all — and the scoped boss rule rightly forbids hard-wiring `num-times-tables` into a tier-3 spatial branch node. Same pattern the docs fixed twice before (`num-numbers-100` "writes," quest assumes-lines): a parent can run the check on a child whose ×/÷ frontier can't yet do 1 cm : 50 cm conversion. **Fix:** one sentence on the card in the quest idiom — "scales stay friendly (1 cell = one floor tile / one big step); numeric scale conversion assumes the child's `num-tables-1` frontier, or the parent co-pilots the arithmetic" — a soft assumes-line, never an edge.

---

## 2. What was checked and found clean (so loop 5 need not re-check)

- All eight careers reachable from tier-0 roots; every tier-5 vestibule consumed by a `capstone_prereqs`; every career highlight carries the full English strand and ≥9 tier-0 roots across ≥5 domains.
- Weekly arithmetic: template session counts × session lengths match §5.6's child-minutes rows for all four bands; Band-4 standing prescriptions (tables 3 min in fluency slots, typing 10 min in booklet-session openers, strips ~2 min/session) now fit inside 5 × 20 with the working spread — the loop-3 M4 overflow is genuinely gone.
- Strip arithmetic: 4-item strips × 5–6 sessions = 20–24 items; retest weeks consume ≤8 of them for ≤2 queued nodes; priority ordering stated. Consistent with B18's rung rotation.
- B18 internal page math (20–28 pages, 16–20 working, 8–10 spreads, 4–5 weeks) consistent everywhere it is cited.
- CR3 ↔ §3 Band-2 dose; CR16 dose/ceiling split; boss semantics ↔ §1/§3; bridge lists identical in both documents; S-table ages ↔ band rows ↔ node ageBands; sourcing notes ↔ node cards; `check`/`keystone`/`cluster` field contracts ↔ framework rulings.
- Research grounding of every loop-3-touched citation verified against the actual report files.
- Viewer pipeline regenerated at v1.3; node ids stable.

## 3. Convergence judgment

**Converged.** The graph and both documents' arithmetic are now exactly true under mechanical verification, all prior majors are closed and holding, and the six residual findings are one-line label/wording patches with no structural consequences. Recommend applying findings 1–5 as a single editorial pass (no id changes, no count changes — nothing the viewer or the §7 checklist needs re-run for except the keystone decision in finding 2), and finding 6 as one added sentence when the spa card next opens. Ship the tier-0 poster and booklets 1a/1b on this version.
