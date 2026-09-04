# Loop 2 — Pedagogy Review

**Reviewer focus:** internal consistency, unresolved methodology conflicts, developmental appropriateness, alignment with the research reports — and verification that loop-1's claimed fixes actually hold.
**Documents reviewed in full:** `docs/methodology/combined-framework.md` (v1.1), `curriculum/learning-path.md` (v1.1), `docs/reviews/loop-1-pedagogy.md`. Research reports R1–R4 consulted for every contested citation. All structural claims about the JSON graph re-verified programmatically (node/edge counts, acyclicity, tier ordering, fan-in, roots, chain lengths, cross-domain/bridge counts, and — new this loop — full ancestor closures per career and EF fan-out).

**Verdict:** v1.1 is a genuine improvement — 14 of loop-1's 16 actionable findings are correctly fixed and verified (see §6). But two of the repairs papered over deeper problems rather than solving them, and the repairs themselves introduced new false claims. The two most serious: **booklet #1's home node is unreachable for weeks after day 1** under the system's own mastery semantics, and **the "shared trunk feeds all eight careers via reachability" claim — the v1.1 replacement for the withdrawn 80%-tag claim — is false in the strongest possible way: the intersection of all eight careers' hard ancestor closures is the empty set.** Seven of eight careers are missing at least one of their own declared "heaviest domains" from their hard closure. Both flagship deliverables (sudoku booklet 1, career-highlighting poster) would ship broken as specified.

---

## 1. Critical findings

### C1. Booklet #1's home node is locked on day 1 — for weeks — and the lock is pedagogically circular

`log-sudoku-4x4` (learning-path §6) carries hard prereqs `log-sorting-patterns` **and** `ef-attention-persist`. Under framework §5.1, a node becomes Available only when all hard prereqs are **Consolidated**, and Consolidated means the check passed **again ≥2 weeks after** first mastery. `ef-attention-persist` is additionally an Archetype-B observation-tally cluster: each of its two sub-checks needs **≥3 unprompted instances logged across ≥2 weeks** (framework §5.2).

Chain the definitions and the earliest a rule-following family can open the picture-sudoku node is roughly **4–6 weeks after starting** — for the product line whose S1 level (framework §4.4) is aimed at ages **4.5–5.5** and which framework §4.4 explicitly calls the "**tier 0 entry node**." Booklet #1, the first deliverable of the entire project, hangs off a node that no child can touch in month one.

The lock is also circular against the framework's own theory:

- GP16: EF is "trained through games-with-rules **(sudoku included)**, never through abstract brain-training." The workout is locked behind the outcome of the workout.
- `ef-attention-persist`'s own exercise is "Sand-timer challenge: stay with **a chosen puzzle page** for 10 minutes" — while the system's flagship puzzle pages are locked behind it.
- Demanding 10 minutes of sustained persistence as a *precondition* for a 2×2 rows-only tile strip inverts the developmental direction: S1 strips are 1–3-minute tasks that *build* persistence. Nothing in R1 §8.1 or R4 C5 gates the sudoku line on an EF credential.

**Fix (small, surgical):** make `log-sudoku-4x4` a tier-0 root (13th root), with `log-sorting-patterns` and `ef-attention-persist` demoted to soft helps-with edges on the poster layer. Its S1–S2 internal ladder already provides the on-ramp; B15 self-checking makes early failure harmless. If a hard gate is wanted for the *full 4×4 can-do*, split S1 (rows-only strips) as the root micro-node and gate only S2. Alternatively, at minimum, add a framework rule that **tier-0 intra-tier edges are satisfied by Mastered, not Consolidated** — otherwise every tier-0 chain (`num-bonds-5`, `lit-letter-knowledge`, `dig-robot-game` are also day-1-locked) carries a hidden multi-week consolidation tax that §5.6's ops budget never prices.

### C2. The v1.1 replacement for the career-metadata fix is false: the shared trunk does not reach the careers, and 7 of 8 careers are missing their own declared "heaviest domains" from their hard closures

Loop-1 M4 was "fixed" by making `careers` tags advisory and ruling that highlighting is **computed by reachability** from `quest`/`capstone_prereqs`, with this claim (learning-path §1):

> "The shared trunk — EF, the SEL core, oral communication, literacy, and the numeracy chain through the boss gates — feeds all eight careers: R4 B2's ~80%-shared-foundations finding lives in the trunk's *reachability*, not in tag counts."

Computed against the graph (ancestor closure of `quest` ∪ `capstone_prereqs` per career):

- **The intersection of all eight closures is empty.** Not ~80% shared; not one single shared node. Not even `ef-attention-persist`.
- **Lawyer** (closure = 21 nodes): contains **zero numeracy, zero EF, zero logic, zero science**. Its §2 profile declares "heaviest on literacy, communication, **logic and EF**."
- **Doctor**: zero EF nodes — §2 declares EF a heaviest domain ("holds multi-step protocols in working memory under stress").
- **Software engineer**: zero EF, zero SEL — §2 declares EF heaviest; §2 calls debugging "the *emotional* skill."
- **Scientist**: zero logic nodes — logic is its first-listed heaviest domain.
- **Finance** (closure = 26 nodes): numeracy + EF **only** — zero literacy ("fluent reading of tables and statements"), zero logic, both declared heaviest.
- **Engineer**: zero literacy; **Entrepreneur**: zero communication ("persuading" is in its profile).
- Only **manager**'s closure covers all four of its declared heaviest domains.

Clause by clause, the §1 sentence fails: EF reaches 5 careers (not 8), oral communication reaches 2, literacy 5, the numeracy chain 7 (lawyer's closure has no numeracy at all).

This is not just a prose bug. Path-highlighting is now *specified* to be computed this way, so the poster mechanic will tell an 8-year-old, accurately per the graph and falsely per R4 B2: **lawyer needs no math, doctor needs no self-regulation, finance needs no reading.** That contradicts R4 B2's core finding ("every one of the 8 careers requires: fluent literacy, fluent numeracy, working memory & inhibitory control, sustained attention, oral communication, cooperation, persistence"), contradicts TR7 ("mid-tree nodes deliberately fan out to multiple careers so the map reads as opening options"), and contradicts GP12. The underlying cause is honest: fan-in ≤ 2 + hard-edges-only necessarily produces narrow closures. But then closures cannot *be* the whole highlighting story.

**Fix:** define the **common trunk as an explicit named node list** (the R4 B2 seven shared foundations mapped to ~15–20 node ids: EF chain, SEL core, `com-*` through `com-explain-decision`, both literacy roots + fluency, numeracy chain through the boss gates), and specify highlighting as **closure ∪ trunk** for every career — the trunk rendered as "every wonder needs this" base coloring, the closure as the career-specific overlay. The §4 spines already hand-label "enrichment" soft highlights; this formalizes the same mechanism. Then rewrite the §1 sentence to claim what is true: the ~80% sharing lives in the *schedule* (every child gets the whole trunk regardless of career interest), not in edge reachability. Also verify TR6's "every career traces back to ≥3 layer-0 trunk items" as a validation rule — lawyer currently bottoms out in 4 roots, which passes, but nothing checks it.

---

## 2. Major findings

### M1. CR14's "English phonics remains the only strand scheduled ahead of the Estonian curriculum" is false — tier 3 schedules the entire Estonian grade-3 outcome list a year early, and R3 itself recommends owning this

CR14 correctly shifted the grade labels (verified: framework §3 and the tier table now agree with R3 §1). But the *content* did not move: tier 3 (`ageBand: "8-9"` = Estonian grade 2 under the corrected mapping) contains `num-multidigit` (to 10,000), `num-times-tables` (full korrutustabel), `num-fractions` (1/2–1/5), `num-problems-data` (2-step problems, perimeter) — i.e., **the complete ~9–10 checkpoint list, scheduled at 8–9**. The walkthrough's hedge "typically met across the tier-3/4 boundary" contradicts the nodes' own age bands.

The placement itself is internationally defensible (England Y3–4, Singapore P2–3, US G3 all put this content at 8–9; R2 §13's 8–9 row matches). And R3's own final recommendation (§7) says explicitly: "let the English-literacy **and numeracy** branches run ahead on the UK/Singapore schedules, since the school system will not supply English phonics or CPA math early." So the run-ahead is evidence-endorsed — but CR14 claims it doesn't exist. One document, two positions; the anti-acceleration guardrails (GP11/GP18) are being *claimed* while the schedule quietly does the opposite, which is exactly the failure mode CR14 was written to end.

**Fix:** amend CR14 to name **two** scheduled run-aheads — English literacy (UK-style SSP begun 6–7) and numeracy (international consensus clock, citing R3 §7) — with the Estonian grade-3 list remaining the external *legal* checkpoint at ~9–10 and mastery-gating as the pressure valve. Or re-band the four tier-3 numeracy nodes to "8-10". Pick one; don't keep the "only strand" sentence.

### M2. The binding "a boss is never a cross-domain gate" rule is violated 7 times in the graph

Framework §3 (marked **binding**): "no literacy, science, logic, SEL or other non-numeracy node is ever locked behind a boss." Computed: 7 non-numeracy nodes sit downstream of a boss milestone in the hard graph — `quest-entrepreneur` (creativity, tier 3, via `num-money-time` ← `num-addsub-20`), `t4-science-method`, `t4-venture-lab`, `t5-life-sciences`, `t5-research-project`, `t5-venture`, `t5-applied-engineering`.

Most of these edges are pedagogically *right* (you cannot make change from €2 without within-20 arithmetic; you cannot chart experimental data without number work). The rule text is what's wrong: it was written for tier-0–3 branch nodes and never scoped, while the bridge-cap definition in §6 *did* get the capstone/tier-4/5 carve-out. As written, tooling that enforces the binding rule will reject a correct graph.

**Fix:** scope the rule: "no **tier-0–3 branch node** (career quests excluded) is ever locked behind a boss" — quest-entrepreneur then needs either the carve-out extended to quests (defensible: quests sit above the domains, per §6) or an explicit note. One sentence in framework §3 and one in learning-path §1.

### M3. "The tier-1 EF node feeds every branch (GP16)" is false in the graph

GP16 and the tier-1 walkthrough both state `ef-plan-check` "feeds every branch." Computed: `ef-plan-check` has exactly three outgoing edges — `ef-multistep-projects` (own branch), `cre-iterate-v2`, `quest-scientist`. The whole EF domain's fan-out reaches logic, creativity, SEL, one science quest, and two tier-4 numeracy/SEL bundles. **Literacy, digital, motor-spatial, communication, and the science branch proper receive no EF edge anywhere.** The bridge-cap exclusion (a) in §6 justifies itself by "EF feeds every branch by design (GP16)" — excluding a class of edges that mostly don't exist.

This is prose-vs-graph dishonesty of the kind loop 3's tooling will trip over, and it matters pedagogically: if EF genuinely gated every branch, fan-in ≤ 2 would be arithmetically impossible — which is presumably *why* the edges aren't there. The framework should say what is actually true.

**Fix:** rewrite GP16's operationalization and the tier-1 walkthrough: EF is trunk **via session design** (every booklet trains persistence/WM/inhibition as a by-product — which §6's own EF row already states: "trained as by-product of engaging, gradually harder rule-games — never drilled directly") and via the *observation-tally checks*, not via prerequisite edges. Keep the 2–3 real EF edges; delete the "feeds every branch" wording; re-justify bridge-exclusion (a) accordingly.

### M4. The boss-gate mastery checks don't measure fluency — a finger-counter passes the "fluent" milestone

`num-addsub-20`'s inline check: "10 mixed +/− facts within 20 incl. crossing ten, 9/10, passed twice at least 3 days apart." No time criterion, no retrieval criterion. A child solving every item by counting on from one passes — but that child is precisely *not* fluent, and fluency is the entire point of the milestone (GP6: automaticity frees WM; R2 §11: "fluent retrieval of bonds to 10/20 by ~7–8 is the automaticity that unlocks multi-digit work"). Same defect in `num-times-tables`'s check (untimed 9/10 passes a skip-counter, not a retriever).

The framework's own model criterion (§5.2, straight from R2 §8) is "adds within 10 in **≤3 s per fact**, 9/10 correct, two sessions ≥3 days apart," and §5.5 explicitly permits "timed-but-gentle" at fluency stages. The two most consequential checks in the system are the only inline ones — and both drop the clause that makes them measure the right construct.

**Fix:** add "≤3 s per fact (gentle: parent observes retrieval-not-counting; no visible stopwatch pressure)" to both `mastery_check` strings.

### M5. CR3's dose figures contradict CR16's ruling — the framework now disagrees with itself about daily time

CR3 (unrevised since v1.0): "structured practice is a *scheduled dose* (**10–15 min/day at 5–6 rising to 25–30 by 8–9**), never the whole diet." CR16 (new in v1.1) rules that the **total session** is 15–20 min at 7–8 and 20 min at 8–9 (30 = autonomy-only ceiling), and §3's binding budget makes the DI dose sit *inside* the session. So CR3's structured-practice-alone figure at 8–9 (25–30) **exceeds the entire scheduled session** (20), and its 5–6 figure (10–15) equals the whole session — self-refuting its own "never the whole diet" clause. CR3's parenthetical is a fossil from before CR16 existed.

**Fix:** update CR3's parenthetical to match CR16 and §3 (e.g., "~10 min inside the session at 5–6, rising to ~15 min inside the 20-min session by 8–9"). Also fix the Band-1 residual: the §3 DI row says "~10 min/day" while the binding budget paragraph says the structured portion happens "on training-ground days" — daily vs. some-days, still ambiguous after loop-1 F3.

### M6. ScratchJr is a single app-specific hard funnel for the whole upper digital chain and the software career — and `dig-typing`'s prerequisite fails the load-bearing test

Learning-path §1 boasts that would-be funnels were made activity-agnostic (`dig-beebot-arrows` satisfiable paper-only; `cre-make-own-puzzle` any puzzle). But `dig-scratchjr` — a specific, tablet-first commercial app — is the sole hard route into `dig-scratch`, `dig-typing`, and thence `t4-programming` → `t5-software-craft`. A family without a tablet, or a child who bounces off that one app, is hard-walled out of the software wonder: exactly the R4 C3.4 failure the section claims to have engineered away. Worse, `dig-typing` ← `dig-scratchjr` flunks the file's own load-bearing test ("could the child plausibly do B well without A?" — typing needs letter knowledge, not ScratchJr); the edge visibly exists only to satisfy invariant 2 (every non-tier-0 node needs a prereq).

**Fix:** reword `dig-scratchjr` activity-agnostically ("any introductory block-based environment — ScratchJr, Scratch junior-mode, Code.org pre-reader course"), matching the beebot treatment. Re-parent `dig-typing` onto `dig-beebot-arrows` (keeps it in-branch, honest enough: typing serves the programming chain) or `mot-letter-formation`.

---

## 3. Minor findings

1. **`quest-scientist` demands the skill it doesn't require.** The quest is a full one-variable fair-test cycle ("change ONE thing, record daily") with prereqs `sci-measure-record` + `ef-plan-check` — while `sci-fair-test`, the tier-3 node that *teaches* one-variable control, is not in its ancestry. A child can unlock a quest whose core demand R3 places at 8–9 straight from tier-2 skills. Swap `sci-measure-record` for `sci-fair-test` (fan-in stays 2; measure-record remains in ancestry).
2. **The bridge count doesn't reproduce.** Claimed: "4 of 123 ≈ 3%." Under §6's stated exclusions I compute **3** (`lit-letter-knowledge→mot-letter-formation`, `mot-letter-formation→log-sudoku-symbols`, `dig-beebot-arrows→log-decompose-debug`) — and the third depends on whether "the shared LOG→DIG on-ramp" exclusion covers a **DIG→LOG** edge. Within the cap either way, but a *binding* cap needs a mechanically checkable definition: list the counted bridge edges explicitly in §1 and fix the exclusion's direction.
3. **Advisory `careers` tags are still incoherent — now 67 tag/ancestry mismatches (up from 33).** Harmless for gating (tags demoted, correctly), but they drive **poster coloring**, so the poster will show doctor-colored nodes whose entire feeder chains carry no doctor color — the same visual incoherence loop-1 M4 described. Either derive coloring from computed closures too, or prune the tags to the ~3 genuinely heaviest feeds per node and accept the look.
4. **Archetype-B misfit on `ef-attention-persist` sub-check (b).** "Follows a 3-step spoken instruction from memory" cannot be evidenced by "≥3 *unprompted* instances" — an instruction is a prompt by definition, and it's a WM capacity check, sit-down-testable in two minutes. Tag sub-check (b) Archetype A; keep (a) as the tally.
5. **`num-numbers-100` GP18 tension still unacknowledged** (loop-1 §4.4, asked-for sentence never added): reading/writing/ordering to 100 at 6–7 sits on the US-K range end of the R3 spread while GP18 preaches depth-over-range and the koolivalmidus target is 12. The v1.1 demotion note covers Siegler & Booth but not this. One sentence.
6. **"UK clock" mislabels the phonics schedule.** UK Reception children start statutory SSP at **4–5** and decode CVC words by 5 (R3 §5). Starting at 6–7 is a UK-style *program* on a deliberately delayed start — two years behind the actual UK clock. CR2/GP10/§5.4's "on the UK/Singapore timeline" should say "UK-style SSP sequence, begun at 6–7 by our own ruling (CR2), reaching the same endpoint by ~9."
7. **B18's booklet arithmetic is loose.** 24–32 pages at one 2-page spread/day = 12–16 sessions ≈ **2–2.5 weeks** at 6 sessions/week, not "≈3–4 weeks" — unless cover/story/reward pages don't consume sessions, which B18 should then say, since the N−1 ≈ 1-month spacing label leans on the booklet-month equivalence.
8. **Three training grounds at Band 2, two slots.** The §3 DI alternation prices phonics and number-fact days only; `mot-letter-formation` (tagged `training-ground`, 6–7, explicit instruction per GP2) has no scheduled minutes. Form-drawing warm-ups cover the motor warm-up, not letter-formation instruction. Say where its dose lives (inside the booklet's warm-up pages? a third alternation day?) or untag it.

---

## 4. Loop-1 fixes verified as actually holding (re-checked, not assumed)

CR14 grade labels (framework §3 + tier table consistent with R3 §1); age-8 career quests restored as 8 real tier-3 `quest-*` nodes with tier-2-reachable prereqs (M2 ✓); `cre-make-own-puzzle` puzzle-agnostic, creativity chain unbroken to `t5-venture` (M3 ✓, entrepreneur spine now a real path — every §4 spine edge-verified this loop); `num-numbers-100` demoted, `num-teens` extracted, boss prereqs now `num-addsub-10` + `num-teens` (M6 ✓); English oral chain wired (`lit-en-oral-vocab → lit-en-oral-2 → lit-en-reading`, twin-leg Simple View ✓, M7); cluster-node ruling + 5 marked clusters (M5 ✓ as bounded amendment); extended-fluency staging (within-10/within-20, tables-1/full ✓); ScratchJr re-banded to 6–7 matching R3 (F1 ✓); CR16 written (F2 ✓); CR15 scoping written and internally coherent (F4 ✓); B18 cadence pinned per-spread (F5 ✓); frontier unified at 3–5 + day-1 rule (F6, §5.2 ✓); S-table/band-row/node ladder all consistent, box rule at S3 on 4×4, 6–8 givens flagged as deliberate deviation (F7 ✓); chapter-book exercise fixed (`lit-en-reading` now decodable-plus, chapter books deferred to t4 ✓); per-sitting persistence stamp removed (B20 note ✓); B21 contrast pages exist and are referenced from both phonics nodes ✓; §5.6 ops budget exists and prunes retests/decay-sweeps by rule ✓; Estonian-content sourcing note added (§7 ✓); "50–80 brief" withdrawn ✓.

Structural invariants re-verified: 93 nodes (17/18/15/24/10/9), 123 edges, all references resolve, acyclic, no later-tier prereqs, 12 tier-0 roots, no non-tier-0 roots, fan-in ≤2 except `t5-research-project` (3), longest intra-tier chain 3, longest tier-0–3 chain 9, raw cross-domain 31/123 ≈ 25% as stated.

---

## 5. Priority order for the fix loop

1. **C1** — unlock booklet #1 (root-ify `log-sudoku-4x4` or add the tier-0 Mastered-satisfies rule). Blocks the first deliverable.
2. **C2** — define the explicit common-trunk node list and closure∪trunk highlighting; rewrite the §1 reachability sentence. Blocks the poster.
3. **M4** — add the fluency clause to both boss checks (two strings).
4. **M1, M2, M3, M5** — four scoping/honesty edits to the framework text (CR14 second run-ahead; boss-rule scope; GP16 wording; CR3 numbers). No graph surgery.
5. **M6** + minors 1, 4 — small graph/node-text edits (`dig-scratchjr` wording, `dig-typing` re-parent, `quest-scientist` prereq swap, archetype tag).
6. Minors 2, 3, 5–8 — one editing pass.
