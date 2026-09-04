# Review Loop 3 — Pedagogical Soundness

**Reviewer focus:** internal consistency, unresolved methodology conflicts, developmental appropriateness per band, alignment with `docs/research/`.
**Documents reviewed in full:** `docs/methodology/combined-framework.md` (v1.2), `curriculum/learning-path.md` (v1.2). Research reports R1–R4 consulted for grounding on every disputed claim below.
**Date:** 2026-08-30.

---

## 0. What was re-verified and HOLDS (loop-1/2 fixes confirmed)

Before criticizing, I recomputed the structural claims rather than trusting them:

- **Node counts:** tier 0 = 18 (14 roots), tier 1 = 18, tier 2 = 16, tier 3 = 24 (16 + 8 quests), tier 4 = 10, tier 5 = 9 → **95 total**. Matches §1 table and invariant 4.
- **Edge count:** summed `prereqs` = **122 hard edges**. Matches.
- **Raw cross-domain edges:** counted by walking every edge against the domain map = **31 of 122 (25.4%)**. Matches the "~25% (31 of 122)" claim exactly.
- **Counted bridges:** after applying the framework §6 exclusion lists (2 EF tier-0–3 out-edges; 7 named developmental corequisites; all quest and tier-4/5 fan-in), the remainder is exactly `lit-letter-knowledge → mot-letter-formation` and `mot-letter-formation → log-sudoku-symbols`. **The named 2-bridge list is reproducible.**
- **Fan-in:** ≤2 everywhere except `t5-research-project` at 3. Matches invariant 3.
- **Boss-ancestry scoping:** no tier-0–3 non-numeracy branch node has `num-addsub-20` or `num-times-tables` in its hard ancestry (only numeracy nodes, quests, and tier-4/5 bundles do). The scoped rule holds.
- **`common_trunk` is ancestor-closed** (every hard ancestor of each of the 22 ids is itself in the list). Structurally valid — but see M1 for what the list *omits*.
- **Longest within-tier chain 3, longest tier-0–3 spine 9** (the numeracy chain) — both confirmed.
- Loop-2 fixes all physically present: `log-sudoku-4x4` is a genuine root; `mot-gross-body`, `lit-en-oral-3`, `num-teens` exist; `dig-typing` re-parented onto `mot-letter-formation`; `quest-scientist` routed through `sci-fair-test`; boss checks carry gentle inline criteria; tier-5 chokepoints (lawyer, entrepreneur) stated honestly.

This is genuinely good structural hygiene. The problems below are therefore mostly *not* graph problems — they live in the operational layer (time arithmetic, check mechanics, display truth) and in the flagship booklet spec, which is exactly where the next deliverables will inherit them.

---

## 1. MAJOR findings

### M1 — `common_trunk` omits the entire English-literacy strand; 5 of 8 career highlights show zero English decoding

The trunk exists (learning-path §1) because "closures alone would tell a child that Lawyer needs no math and Doctor needs no self-regulation." It then commits the identical sin with English:

- The 22-id trunk carries the **Estonian** decoding leg through tier 2 (`lit-ee-decoding`, `lit-reading-fluency`) and the **English oral** leg only through tier 1 (`lit-en-oral-vocab`, `lit-en-oral-2`). It contains **no** `lit-en-phonics-1`, `lit-en-phonics-2`, `lit-en-oral-3`, or `lit-en-reading`.
- I walked every career's computed highlight (closure of `quest` ∪ `capstone_prereqs`, ∪ trunk). English decoding enters only via `lit-en-reading → t4-english-fluent → {t5-software-craft, t5-research-project}`. So **doctor, software engineer, and scientist** get English phonics highlighted; **manager, lawyer, entrepreneur, engineer, and finance do not** — their posters will say, in effect, "Lawyer needs no English reading."
- This contradicts: **GP10** (English decoding is *the* strand "the school will not supply" — mandatory for every child in this family), **GP12** ("every child walks the whole trunk"), **CR14** (English literacy is a *scheduled* run-ahead — scheduled for whom, if the trunk doesn't carry it?), and the document's own gloss of the trunk as "literacy roots with **both fluency legs**" — the 22-id list contains no English fluency leg at all, so the descriptive phrase is false against its own data.

**Fix (small and safe):** add 4 ids — `lit-en-phonics-1`, `lit-en-phonics-2`, `lit-en-oral-3`, `lit-en-reading` — to `common_trunk` (ancestor-closure is preserved: all their ancestors are already in the trunk or in the added set). Update "22" to "26" in learning-path §1/§6 and framework §6 note; re-run invariant 8.

### M2 — Consolidation retests cannot ride the vehicle they are assigned to

- §5.1: Consolidated = "check passed again ≥2 weeks later; **the retest rides the B18 warm-up strips**, never a separate session." §5.6 repeats: "consolidation retests ride the B18 retrieval strips automatically."
- §5.2 Archetype A defines the check as "**5–10 items**, parent-runnable in **<10 minutes**."
- B18 defines the strip as "**4 items, ~2 min**" — which must *simultaneously* sample three gap scales (same booklet / N−1 / N−3-4), carry "maintenance of whichever strands are *not* that day's emphasis" (§3 template — this is the stated mechanism that lets doses alternate without decay), and host Needs-polish refresh content (§5.1, §5.6).

A 5–10-item check cannot fit inside a 4-item strip that already has three standing jobs. Nowhere is it defined what a strip-borne retest actually *is*. Note also that the framework quietly hardened R4's model: R4 A6.7 defined Consolidated as "check passed **twice**, ≥2 weeks apart," while §5.2 + §5.1 now require *three* passes (twice ≥3 days apart for Mastered, again ≥2 weeks later) — and routed the third through a carrier too small to hold it. Since **Consolidated is what satisfies every prerequisite above tier 0**, this is the load-bearing joint of the whole mastery machine, and it is unspecified.

**Fix — write one of these into §5.1:** (a) consolidation retest = 3–4 items sampled from the node's check bank, spread over two consecutive strips in the retest week, all-correct to pass; or (b) on a retest week the strip extends to 6 items, the extra 2 from the retest node; or (c) revert to R4's two-pass model (pass #2 at ≥2 weeks IS consolidation, run as a full mini-check in a free-choice tail). Then do the weekly item arithmetic once: 6 strips × 4 items = 24 items/week against ~5 concurrently-active strands, and state the sampling priority when demand exceeds supply.

### M3 — The booklet-cadence arithmetic does not close, and the spacing labels rest on it

B18 (self-described as "cadence pinned"): one working spread per booklet session, "the **2–3** booklet/free-choice sessions of the §3 weekly template," so a 10–13-spread booklet "spans ≈3–5 weeks ≈ one month," and this equivalence "is what the N−1 and N−3/N−4 gap labels rest on."

But the §3 template grants **exactly 2** booklet sessions in every band (Band 2: "2 booklet/free-choice"; Band 3: "2"; Band 4: "2"). There is no band with 3. At 2 spreads/week, 10–13 spreads = **5–6.5 weeks ≈ 1.5 months**: "N−1 ≈ 1 month" is actually ~6 weeks and "N−3/4 ≈ 1 season" is ~4.5–6 months. The expanding-gap ladder the strips implement is mislabeled by ~50% under the system's own binding template. Worse at Band 1: booklet spreads have "no fixed slot" at all, so for the **flagship Band-1 sudoku booklet** the N−1 gap has no defined value.

**Fix:** either cut working spreads to 8–10, or relabel the gaps honestly (N−1 ≈ 6 weeks; sample N−2/N−3 for the season rung), and state a Band-1 cadence assumption (or key Band-1 strips to elapsed weeks, not booklet index). Also reconcile GP8's named ladder (1 day / **1 week** / 1 month / 1 quarter) with B18's actual sources (days / month / season) — the ~1-week rung is currently unrepresented except incidentally via "earlier pages of the same booklet."

### M4 — Node-level exercise dosing overflows the priced weekly budget

§3/§5.6 make the session **the total daily system time** ("everything outside the session is ordinary childhood"); Band 4 = 5 × 20 = **100 child-min/week**. But the nodes prescribe:

- `num-times-tables`: "Three gentle minutes **daily**" (~21 min/wk, including non-session days that by rule contain no system work);
- `dig-typing`: "Ten calm minutes, **three times a week**" (30 min/wk);
- template fixed costs: 2 booklet/project sessions (40) + 1 written-expression (20) + strips (~10);
- 1–2 fluency-maintenance sessions (20–40) must somehow host tables *and* typing *and* handwriting/phonics maintenance.

Summed: ~120–140 min of standing prescriptions inside a 100-min budget — before science, quests, or SEL touch anything. §5.6 prices *parent* load carefully but never sums *child-side per-node prescriptions* against the template; the overflow lands precisely at the boss-gate band.

**Fix:** add a rule that every exercise cadence must name its template slot ("tables = the retrieval strip + fluency-maintenance sessions," not "daily"; "typing lives inside the booklet/project sessions"), and cap concurrent training-ground nodes in Practicing at ≤2. Re-audit all tier-2/3 exercise lines against the band budgets once.

### M5 — Band-2 phonics dose contradicts CR3's ramp and the "never the whole diet" clause

CR3 (binding): "up to ~10 min of the 10–15-min session at 5–6 … **rising to ~15 min of the 20-min session by 8–9**." §3 Band 2 (age 6–7): "~15 min English phonics" inside a "15–20 min" session. The 8–9 ceiling dose is already prescribed at 6–7, and on phonics days dose (15) + strip (2) = 17 of a 15–20-min session — structured practice **is** the whole diet on those days, in the koolieelik year, whose register row still promises "guided play + first formal strands." Two binding texts disagree; a booklet/session author can follow either.

**Fix:** set the Band-2 phonics dose to ~10–12 min (1:1 SSP needs less than the UK's 20-min classroom dose; nothing in R2 requires 15 at 6), or amend CR3's ramp and add an explicit sentence that training-ground *days* at Band 2+ are exempt from the whole-diet clause. Pick one; don't leave both.

### M6 — CR15's recognition battery never made it into §4.4, which authors are told to copy

R1's page grammar is explicit (R1 §2.1 three-period lesson + BR4): after the one worked example, "pages 2–6 are recognition tasks ('point to/color the row that breaks the rule') … Recognition pages should outnumber production roughly 3:1 for any new concept." B10 step 3 carries this; CR15 correctly scopes it to introduction pages. But **§4.4's binding every-level checklist** ("unique solutions … ≥3 puzzles per difficulty … one find-the-mistake page … one make-your-own … one provocation") instantiates exactly **one** recognition page per mechanic — and CR15 then declares "the §4.4 sudoku spec is compliant as written," which is true only if the introduction-page battery is assumed silently. §4.4 calls itself "the concrete instantiation all future booklet families copy": an author working from it ships the inverse ratio that CR15 exists to prevent, in booklet #1. (Side note: CR15's claim that "the bug originates inside R1" misreads R1 — R1's page grammar at §2.1/BR4 always contained the battery; only its §8.1 checklist omitted it. The framework inherited the checklist, not the grammar.)

**Fix:** add one line to §4.4's every-level list: "2–3 recognition pages immediately after each level's worked example — point-to/color the rule-breaker, legal-or-not strips, which-tile-goes-here choices — before the production buffet (B10/CR15)."

### M7 — Booklet #1 as re-scoped violates B7 ("one new mechanic per booklet") without a carve-out

`log-sudoku-4x4`'s loop-2 fix ("its opening pages ARE the sorting/patterns content and the S1 rows-only strips, then 4×4 picture grids") packs at least three new mechanics into one booklet for a day-1 five-year-old: sorting/patterning, the rows rule (S1), and the columns rule (S2) — §4.4's own table treats S1 and S2 as separate levels with separate "new difficulty" entries and even separate age bands (4.5–5.5 vs 5–6). B7 is binding ("one new mechanic per booklet") and the flagship product now silently breaks it. The day-1 motivation for the root fix was sound; the collateral damage to B7 was never ruled on.

**Fix:** either split booklet 1 (1a = sorting/patterns + S1 strips; 1b = S2 4×4 — both can still hang off the single `log-sudoku-4x4` node), or write an explicit, argued B7 carve-out for the entry booklet (in the spirit of the tier-0 exception: the entry band tolerates a gentler rule because everything is new on day 1). Silent violation in the first shipped product is the one place not to have it.

### M8 — "Same endpoint by ~9" for English phonics is asserted, never argued, and unmonitored

The claim appears three times (CR2, CR14, §5.4) as settled fact. The dose behind it: 2 × ~15 min/week explicit phonics at Band 2, 2 phonics→spelling sessions at Band 3 — roughly **one-third** of the UK benchmark it cites (daily ~20-min SSP lessons plus school-wide reinforcement), delivered to an **L2** child. Real mitigators exist — 1:1 dosing beats classroom delivery; older starters acquire decoding faster (Suggate is already in R3's own bibliography) — but the framework never invokes them, and no mechanism notices if the trajectory is failing. For the single most consequential home-led strand in the system, "we'll get there by 9" is currently a hope, not a design.

**Fix:** (a) one paragraph in §5.4 arguing dose adequacy from the 1:1 and older-starter evidence; (b) a monitoring trigger: at each quarterly dim-check, compare GPC-set coverage against the by-9 trajectory; if >1 phase behind, add a third phonics-led session (the template has a free-choice tail to donate). Cheap, and it converts the claim from assertion to controlled system.

---

## 2. MINOR findings

**m1 — The EE-before-EN decoding order is unruled.** R2 (§10 design implication, line 192) says explicit English reading is "sensible from ~6–7, **after Estonian decoding is underway**." In the graph, `lit-ee-decoding` and `lit-en-phonics-1` both hang off `lit-letter-knowledge` with no ordering; a family could run English phonics first. The framework rules on sixteen conflicts but is silent on the one uniquely bilingual sequencing question it faces. Fix: a sentence in GP10/CR2 — either "surface `lit-ee-decoding` ahead of `lit-en-phonics-1` in frontier curation (soft order, never an edge)" or an explicit ruling that parallel onset is fine and why (B21 contrast pages + disjoint GPC sets).

**m2 — Phantom citation in invariant 4.** Learning-path invariant 4 cites "R4 C1's **110–150** sketch." R4 says "~**120–160** nodes" (line 137); "110–150" appears nowhere in R4. Ironically this sits in the same invariant that withdrew v1.0's phantom "50–80 brief." CR13 cites the correct range. Fix the number.

**m3 — Wrong section number for the numeracy run-ahead source.** CR14 and learning-path §3 cite "R3 §7" for the recommendation to run number work on UK/Singapore schedules. That recommendation is R3 **§6** (Implications, line 257); R3 §7 is the annotated bibliography. In a doctrine whose selling point is traceability, the load-bearing ruling cites the wrong section.

**m4 — Pre-CR14 remnant in the learning-path scope line.** "from age-5 foundations (**last lasteaed year**)" — under CR14, ages 5–6 are the *middle* lasteaed year (the tier table two paragraphs later says so); koolieelik (6–7) is the last. The scope line still carries the v1.0 anchoring the whole CR14 exercise corrected.

**m5 — `lit-letter-knowledge` demands writing at a band whose binding rule is "place/circle, don't write."** The tier-0 criterion includes "writes own name in printed capitals" and the exercise is "trace-then-write name plate," while §3 Band 1 motor row says "place/circle, don't write" and letter *formation* is a tier-1 node. Name-writing at 5–6 is developmentally normal and koolivalmidus-aligned — but then the Band-1 rule needs the standard name-writing carve-out, or the criterion should read "writes **or builds** own name (letter tiles fine)."

**m6 — "Week-scale" quests that are month-scale.** §3/§6 call the quests "each a week-scale … first door," but `quest-finance` is "a month-long pocket-money ledger" and `ef-goal-setting` tracks a month; the §5.1 single-shot ruling itself says "month-scale dispositional nodes." Change the wording to "week-to-month-scale" so the granularity story is consistent.

**m7 — No English encoding anywhere before ~10–13.** A "UK-style SSP sequence" includes writing/spelling from the start (encoding consolidates GPC knowledge); here English spelling first appears inside `t4-english-fluent`. Estonian dictation exists (`lit-writing-sentences`), English none. Fix: add encoding sub-ticks to `lit-en-phonics-1/2` (word-building with letter cards is already there; add write-the-CVC-word once `mot-letter-formation` is in hand, and 3-word gentle English dictation at tier 2).

**m8 — "Keystone node" is used but never defined.** GP13 and §5.3 attach evidence (work sample, dictated sentence) to "keystone nodes"; no definition exists and no node is tagged. The poster and booklet pipelines cannot implement it. Fix: define (e.g., boss milestones + era-final nodes + quests) and tag in the JSON.

**m9 — `ef-attention-persist` sub-check (b) sits at the top of the Band-1 WM budget.** "Follows a 3-step spoken instruction from memory" as a pass/fail check at 5–6, where §3 gives 2–3 chunks and the SEL/EF row says "2–3-step instructions." Fine for a 6-year-old, heavy for a fresh 5-year-old. Fix: accept 2-step at band entry with 3-step for mastery, or note it is expected to consolidate late in the band.

**m10 — "Sight words emerging" precedes phonics in the Band-2 English row.** As phrased, a parent can read it as memorize-whole-words-before-phonics — the opposite of the SSP doctrine the same cell announces. Reword: "first tricky/high-frequency words taught within the SSP sequence."

**m11 — Unexplained check-interval deviation on the second boss.** `num-times-tables` requires passes "at least a week apart" where Archetype A's default is "≥3 days." Probably deliberate (bigger fluency claim, longer verification gap) — say so, or align it.

---

## 3. Verdict

The v1.2 graph is structurally sound — every count, cap, closure, and scoping claim I recomputed held, which is rare and creditable. The remaining defects cluster in two places: **(1) the operational layer**, where the binding texts contradict each other or their own arithmetic (trunk vs. GP10/GP12 display truth for English; consolidation checks that don't fit their assigned carrier; booklet≈month labels resting on a third weekly session the template never grants; node dosing that overflows the priced budget; a Band-2 phonics dose above CR3's own ramp), and **(2) the flagship booklet spec**, where CR15's recognition battery was never written into §4.4 and the loop-2 root fix quietly broke B7. All eight major findings have small, mechanical fixes; none requires re-litigating any ruling. Fix M1 before printing any career poster, and M2/M3 before building the strip/retest tooling, because everything downstream inherits them.
