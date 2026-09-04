# Loop 1 — Pedagogy Review

**Reviewer focus:** internal consistency, unresolved methodology conflicts, developmental appropriateness, alignment with the four research reports.
**Documents reviewed in full:** `docs/methodology/combined-framework.md` (v1.0), `curriculum/learning-path.md` (v1.0). Research reports R1–R4 read in full for grounding. Structural claims about the JSON graph were verified programmatically (fan-in, tier counts, chain lengths, acyclicity, career reachability, ancestor closure of career metadata, cross-domain edge share).

**Verdict:** The framework is a genuinely strong synthesis, but the learning path quietly breaks four of its load-bearing commitments — the Estonian grade anchoring is off by one year everywhere, the age-8 career capstone quests the whole motivational design depends on have vanished, the creativity branch is hard-locked behind sudoku in direct violation of a named R4 anti-pattern, and the career-highlighting metadata is incoherent (33 ancestor-closure violations). Several prose claims about the graph are demonstrably false against the graph itself. None of this is fatal; all of it is fixable before the poster or booklet 2 ships.

---

## 1. Major findings

### M1. The Estonian grade anchoring is off by one year, system-wide — and it contradicts CR2's "single deliberate run-ahead" claim

Per R3 §1 (the framework's own cited source): Estonian children enter grade 1 at age 7 (must turn 7 by 1 Oct), so grade 1 spans ~7–8, grade 2 ~8–9, grade 3 ~9–10. End-of-grade-3 outcomes (numbers to 10,000, full korrutustabel, fractions) are reached by Estonian children at ~10.

Both documents label the bands a year early:

- Framework §3 table: Band 3 "~7–8 = Grade 2", Band 4 "~8–9 = Grade 3". R3's own mapping says ages 7–8 = grade 1, 8–9 = grade 2.
- Learning path §1 tier table: Tier 1 "6–7 = Koolieelik → grade 1 (school year 1)" — a 6–7-year-old is a koolieelik, not a first-grader. Tier 2 "7–8 = Grade 2", Tier 3 "8–9 = Grade 3".
- Learning path §3 Tier 3: "the Estonian grade-3 checkpoint, met or exceeded" at ages 8–9 — i.e., grade-3 outcomes demanded roughly during the year most Estonian children are in **grade 2**.

Consequences:

1. **CR2 is violated.** CR2 states English phonics is "the single place we deliberately run ahead of the Estonian schedule." The tier bands run *everything* — numeracy, science, composition — a year ahead of the Estonian grades they claim to mirror. Either this is intentional acceleration (then it needs its own CR ruling, because GP11 and R3 §5 argue early acceleration is negative-EV) or the labels are wrong.
2. **The tier-1 boss gate lands pre-school.** `num-addsub-20` ("fluent +/− within 20") closes tier 1 at ~7 — before Estonian school begins, when the official koolivalmidus arithmetic expectation is +/− **within 5**. The consensus "~7" milestone in R3 §3.2 means "during grade 1" in the late-start systems.
3. `lit-ee-decoding` (tier 1, 6–7) says "school-led at 7 — this node supports the school's work," but school-led decoding happens in grade 1 = ages 7–8 = tier 2's band. The node sits one band before the institution it claims to lean on.

**Fix:** Either (a) shift the grade labels one year later (Tier 1 = koolieelik, Tier 2 = grade 1, Tier 3 = grade 2, and the grade-3 checkpoint becomes a tier-3-to-4 boundary object at ~9–10), keeping content targets as aspirational-not-labelled-as-school-parity; or (b) keep the ambitious bands but add a CR14 that explicitly owns the ~1-year run-ahead for numeracy/literacy and reconciles it with GP11/GP18 (mastery-gating gives partial cover, but the era labels and "met or exceeded" language set parent expectations, which is exactly what GP11 warns about).

### M2. The age-8 career capstone quests are gone; "Horizons" was silently repurposed from age 8+ to age 14–18

The framework is unambiguous:

- GP12: capstones "unlockable from ~tier 3 (age 8+)".
- CR12: "capstone quests unlockable from tier 3 (~age 8)".
- Framework §3 band table, Band 4 (8–9): "Explorer (tier 3; **Horizons capstones begin**)".
- Framework §6: capstones are child-sized multi-week quests — "patient chart for a sick teddy; family restaurant night; paper bridge holding 10 coins; month-long pocket-money ledger" (from R4 B3/C1, where Horizons is a tier of 8–12 quest nodes visible from day 1 and unlockable from tier 3).

The learning path renames Horizons to ages ~14–18 (tier 5 "career vestibules"), inserts a Voyager tier, and **contains zero capstone quest nodes at ages 8–9**. Its Tier 3 walkthrough still says "Career capstone quests become unlockable from here (CR12)" — but there is nothing in the graph to unlock: careers hang exclusively off tier-5 feeders. The kid-sized quests were scattered as ordinary exercises (paper bridge → `cre-iterate-v2`; pocket-money ledger → `t4-money-management`, now at 10–13; restaurant night and teddy chart are gone entirely).

This inverts the motivational architecture. An 8-year-old asking "what do I need to open Doctor?" now gets a highlighted path through gymnasium biology at 16 — the exact "distant, unreachable" failure the wonder mechanic was designed to avoid. R4 A4.6's pull only works when the payoff is a few nodes away.

**Fix:** Restore a capstone-quest layer per the framework: 8–9 quest nodes (one per career + design-your-own), age 8–9, each a multi-week quest with the R4 B3 flavor quests as content, unlockable from tier 3, marked as "wonder, level 1." The tier-4/5 vestibules can stay as the *later* continuation, but the wonder a child opens at 8 must be the teddy chart, not `t5-life-sciences`.

### M3. The creativity branch is hard-locked behind sudoku — a named R4 anti-pattern

`cre-make-own-puzzle` (tier 1, the only CRE node above tier 0) hard-requires `log-sudoku-4x4`. Everything creative above it chains on: `cre-iterate-v2` → `t4-design-build` → `t5-applied-engineering`. Verified: **the engineer career's ancestor set includes `log-sudoku-4x4`** as a hard prerequisite.

R4 explicitly forbids this twice: A4.3 "a child who races ahead in logic must never be hard-locked out of the creativity branch," and C4 anti-patterns "locking CRE/SEL branches behind academic grind." Framework §6 CRE row says creativity is "never locked behind academic grind (R4 anti-pattern)." The learning path does precisely what all three prohibit. A child who dislikes sudoku is locked out of Version 2 culture, design-build, and (per the hard edges) the engineer wonder.

**Fix:** Make `cre-make-own-puzzle`'s puzzle-agnostic ("makes own puzzle/game for someone else" — any mechanic: mazes, pattern challenges, riddles) with `cre-idea-fluency` as the only hard prereq and sudoku as a soft/helps-with edge; or add an OR-group (any completed tier-0 LOG or SPA node qualifies). R4 C3.2 allows OR-groups; the learning path dropped them without a ruling.

### M4. Career metadata is not ancestor-closed: path-highlighting is incoherent (33 violations), and the "~80% shared" claim is contradicted by the data

CR12/GP12 make `careers` the mechanism for "what do I need to open Doctor?" highlighting. Verified programmatically: **33 edges where a node lists a career its own hard prerequisite does not list.** Examples:

- `num-addsub-20` feeds all 8 careers, but its prereqs `num-bonds-10` (4 careers) and `num-numbers-100` (3) don't list doctor/manager/lawyer/entrepreneur. Highlighting "Manager" would light the boss gate but not the bonds that lead to it.
- `num-times-tables` (all 8) ← `num-mult-groups` (4). A doctor path shows times tables floating with no visible ancestry.
- `lit-reading-fluency` (all 8) ← `lit-ee-decoding` (4).

Also, learning path §1 claims "~80% of tiers 0–3 feeds all eight careers — that is the point." In the data, **10 of 60 tier 0–3 nodes (17%)** list all eight. Either the metadata under-represents the R4 B2 convergence finding, or the claim is false. Both can't stand.

**Fix:** Compute highlighting as graph reachability (ancestors of any node listing career X), not from per-node lists — then the stored lists only need to be right at the leaves; or enforce ancestor closure as a validation rule alongside acyclicity. Re-audit the lists against R4 B2 (does a manager really not need `num-mult-groups`?) and either fix the lists or soften the 80% sentence.

### M5. The "one can-do per node" granularity claim is false for at least a fifth of tiers 0–3

Learning path §1: "Tier 0–3 nodes obey the granularity rule (R4 C2): one assessable can-do statement… parent-checkable in under 10 minutes." R4 C2 rejects "knows addition" as too big. But many nodes bundle 2–4 distinct assessables:

- `num-measure-data`: measure in cm **+** tell full/half hours **+** record pictographs (three unrelated checks).
- `num-money-time`: coins/change **+** clock to five minutes **+** savings chart.
- `spa-shapes-symmetry`: 2-D composition **+** 3-D solids **+** symmetry **+** tangrams.
- `sci-observe-senses`: multi-sense observation **+** living/non-living sorting **+** weather/seasons talk.
- `ef-attention-persist`: 10-minute persistence **+** 3-step instruction from memory (inhibition/persistence vs working memory — different EFs per Diamond, R2 §3).

A parent cannot run a 5–10-item check in <10 minutes on a four-part node, and mastery state becomes ambiguous (child tells time but can't measure — Practicing or Mastered?). This looks like the 78-node budget was reached by bundling, which also explains why tiers 0–3 hold 60 nodes against R4 C1's recommended 110–150. (The "50–80 brief" invoked in §5 invariant 4 traces to no document in the repo — the traceability convention breaks exactly where the deviation needs justifying.)

**Fix:** Split the worst bundles (the five above at minimum; audit all 60) into single-check nodes, or formally amend the granularity rule with a ruling that permits "cluster nodes" with named sub-checks that must all pass. Cite where the 50–80 brief comes from or delete the reference.

### M6. `num-numbers-100` as a hard prereq of the boss gate contradicts the consensus chain and over-pitches Siegler & Booth

`num-addsub-20` requires `num-numbers-100` ("places numbers on an **empty 0–100 line with linear spacing**; reads/writes/orders to 100"). Three problems:

1. **Wrong order vs. the consensus chain.** R3 §4 (quoted "verbatim" per the framework's appendix): bonds → +/− stories → **fluency within 10/20** → place value. The graph inverts it, putting the 0–100 material before within-20 fluency.
2. **Fails the load-bearing test the file itself claims every edge passed** ("could the child plausibly do B well without A?"). A child can be fluent within 20 without linear placement on an empty 0–100 line; teen-numbers-as-ten-and-ones is the only load-bearing part, and it's a minor element of the node.
3. **Developmentally over-pitched as a 6–7 mastery criterion.** Siegler & Booth (R2 §11): the log→linear shift for 0–100 completes "by grade 2" (~7–8). R2's design implication is number-line *estimation practice* from 6, not a linear-placement mastery gate at 6–7. As written, a normally developing 6-year-old mid-shift is blocked from the era's boss milestone by a representation still maturing.

**Fix:** Demote the edge to soft. If teen-number structure is load-bearing for crossing ten, carve out a small "teens as ten-and-ones" node as the hard prereq and let 0–100 linear placement live at tier 2 as its own node.

### M7. The English oral-language strand is a dead end in the graph — the Simple View of Reading is structurally violated

Verified: **no node lists `lit-en-oral-vocab` as a prerequisite.** `lit-en-reading` (8–9) depends only on `lit-en-phonics-2`. So the graph asserts a child reaches "Reading English for Real" through decoding alone.

This contradicts the framework's and reports' most-repeated literacy claim: GP10 ("English language comprehension starts hard at 5" as one of two tracks), R2 §10.1 (Reading comprehension = Decoding × Language comprehension — "both necessary, neither sufficient"), R3 §4 ("oral-vocabulary nodes feed comprehension directly — two-strand Reading Rope shape"). The node's own description admits it ("vocabulary and listening comprehension keep compounding alongside") — prose the graph ignores. For an EAL child this is not a technicality: decoding English without English vocabulary produces word-calling, not reading.

**Fix:** Add an English-oral chain (e.g., `lit-en-oral-vocab` → tier-1/2 "English Ears II" listening-comprehension node → hard edge into `lit-en-reading`). Fan-in stays ≤2 if phonics-2 and oral are its two prereqs.

---

## 2. Framework-internal inconsistencies

### F1. ScratchJr timing: the framework contradicts itself, and the learning path follows the wrong half

CR5 and §6 DIG both quote the R3 chain: "Bee-Bot (5–6) → ScratchJr (**6–7**) → Scratch (8–9)." The §3 band table puts Bee-Bot at 6–7 and ScratchJr at **7–8**. The learning path codifies the band table (`dig-beebot-arrows` tier 1, `dig-scratchjr` tier 2). One document, two schedules, no ruling. Combined with M1's off-by-one this shifts the digital chain up to two years later than the R3/Estonian ProgeTiiger practice it cites as its model (Bee-Bots are in Estonian *kindergartens*). Pick one schedule and state it once.

### F2. Session-length conflict between R1 and R2 silently resolved — against the framework's own promise

R2 §13 gives sessions of 15–20 min at 7–8 and 20 min at 8–9; R1 §10 gives 20–25 and 25–30. Framework §3 adopts R1's larger numbers while citing both. §2's contract is "where reports disagree, Section 2 records the conflict and the ruling." This disagreement got no CR. Minor in effect, but it breaks the framework's core promise of never silently overriding a source, in the one place a parent will actually feel it (daily time).

### F3. The daily time architecture is ambiguous at 5–6

Band 1: session "10–15 min", direct-instruction dose "~10 min/day." If the dose lives inside the session, DI is 66–100% of daily contact time — flatly contradicting CR3 ("structured practice is a scheduled dose, never the whole diet") and GP11's play-first register. If it's on top, total daily load is ~20–25 min and should be stated. Nowhere resolved. Specify: dose is separate from (or within) the booklet session, and give the total.

### F4. B10's 3:1 recognition-to-production ratio is contradicted by the flagship booklet spec

B10 mandates "recognition tasks before production ~3:1." §4.4 gives each sudoku level **one** recognition page (find-the-mistake) against ≥3 production puzzles — a 1:3 ratio, the exact inverse. (The bug originates in R1, which states the ratio in BR4 and then ignores it in §8.1 — but the framework's job was to catch that.) Either the ratio is wrong (plausible for a self-checking puzzle format, where solving carries its own feedback) and should be scoped to *new-concept introduction pages only*, or the sudoku spec needs more recognition pages. Rule on it; booklet authors will hit this on page 1.

### F5. Retrieval cadence: per-session (GP8) vs per-booklet (B18), and a booklet-cadence assumption that doesn't add up

GP8 and R2 r8: *every session* opens with ~2 min retrieval. B18 implements a warm-up *per booklet*. A booklet satisfying B10+B11+B13+B16+B19 (exploration, worked example, ≥3 puzzles per level across several levels, Life/Beauty/Knowledge rotation, find-the-mistake, make-your-own, provocation, documentation pages) is realistically 20–30+ pages = 2–4 weeks of 1–3-page sessions. Yet B18's spacing math ("N−1 ≈ 1 week, N−4 ≈ 1 month") assumes one booklet per week. Either booklets are much thinner than the rules imply, or the spacing schedule is mislabeled (N−1 ≈ 1 month, N−4 ≈ a season — materially different). Pin down booklet size and cadence; respecify warm-ups per session-block (e.g., every 2-page spread opens with a 4-item retrieval strip).

### F6. Frontier size: GP9 says "2–4 unlocked options," §5.1 says "3–5"

Inherited from R4 (A5 vs C3.6) and duplicated rather than reconciled. Trivial to fix; pick one.

### F7. "Standard 4×4 sudoku" at tier 0 vs box rule at S3

`log-sudoku-4x4` and R4 C5 say "solves a **standard** 4×4" at tier 0, but the framework's own ladder introduces the 2×2 box rule only at S3 (tier 1, 6–7); S1–S2 are rows/columns only. "Standard" implies boxes. A booklet author reading the node will build the wrong booklet 1. Reword the tier-0 can-do to "rows-and-columns 4×4" and let the box rule stay the S3 event. (Related: §4.4 S2 says "6–8 givens" where cited source R1 §8.1 says "4–6" — probably a deliberate easing, but the traceability convention requires deviations to be flagged, and this one isn't.)

---

## 3. Learning-path prose vs. its own graph (verified)

- **"Tier 0 — Spark (5–6): the ten roots."** Tier 0 has 16 nodes, 12 of them zero-prereq roots. Neither number is ten.
- **Entrepreneur spine is not a path in the graph.** §4 gives `cre-iterate-v2 → t4-design-build`-or-`t4-money-management → t5-venture`. Verified: `t4-design-build` is **not** an ancestor of `t5-venture`, and no CRE node is (`cre-idea-fluency` not in t5-venture's ancestor set). The creativity chain — the entrepreneur's declared heaviest domain — dead-ends at design-build for this career; the real path runs through money/leading-teams only. Also "-or-" contradicts §1's "hard prerequisites only (AND)". Either add the CRE→venture edge (e.g., `t5-venture` OR-group) or rewrite the spine honestly.
- **"Single-feeder software, lawyer and engineer vestibules."** By the careers metadata, software-engineer has two tier-5 feeders (`t5-advanced-math`, `t5-software-craft`) and engineer has two (`t5-advanced-math`, `t5-applied-engineering`). Only lawyer is single-feeder. The sentence is wrong for two of its three examples.
- **Cross-branch edge cap breached.** Framework §6: bridges "capped at ~10–15% of edges." Verified: 21 of 93 edges (23%) are cross-domain. Either recount what counts as a "bridge" (and define it), or thin the edges, or raise the cap with a note.
- **Era-gate semantics are undefined.** The boss milestones "gate the eras," but nothing outside the numeracy branch requires `num-addsub-20` or `num-times-tables`; a child can be deep in tier-3 literacy without the tier-1 boss. If eras are per-domain poster groupings, say so; if the boss gate seals the next poster, that's an age-independent cross-domain lock that needs a ruling against GP1's domain-specificity (R2 §1.2: development is domain-specific).

---

## 4. Developmental appropriateness spot-checks

Most tier-0/1 targets are well-calibrated (counting to 20 with cardinality, subitise 1–5, bonds of 5, 10-min persistence, retelling, rows-only sudoku — all match R2/R3 consensus). Exceptions:

- **`lit-en-reading` exercise vs. its own can-do.** The node promises "reads *short* English texts and instructions" (matching Band 4's "short independent English instructions OK", framework §3), then assigns "**chapter-a-night** English reader." For an Estonian 8–9-year-old ~2 years into home phonics, a nightly English chapter book is far beyond both the can-do and the band assumption. Downgrade to decodable-plus readers / short non-fiction; chapter books belong in t4-english-fluent.
- **`ef-attention-persist` exercise: "stamp the I-kept-going box."** This is a per-instance reward for time-on-task — the exact mechanic §5.5 and B20 ban ("no points for time-on-task"). Persistence is the competence here, which blurs it, but a stamp-per-sitting is an activity token, not a competence marker. Replace with the capability statement at node completion ("you can stay with a puzzle for 10 minutes now").
- **Linear empty-0–100-line at 6–7** — see M6.
- **`num-numbers-100` also front-loads reading/writing/ordering to 100 at 6–7** while GP18 preaches depth-over-range and praises the Estonian koolieelik target (12) and UK depth-to-10 revision. Tension unacknowledged; at minimum note that this node is deliberately on the US-K range end of the spread.
- **Cross-language phonics interference is designed for in R2 but absent downstream.** R2 §10.2 flags Estonian 1:1 vs English one-to-many mappings as a predictable interference point ("expect interference points… teach English GPCs as 'English's tricky code'"). `lit-en-phonics-1` keeps the tricky-code framing but nothing anywhere (B-rules, nodes, exercises) handles contrast pages or sequencing between the two decoding systems running simultaneously at 6–7 (e.g., Estonian *i* vs English *i*). One B-rule or a phonics-node design note would close this.

---

## 5. Hand-wavy / underspecified areas

1. **Parent-load budget is never computed.** Daily sessions + per-session retrieval + consolidation retests (every node, ≥2 weeks later) + decay tracking on 8–12-week timers across ~60 active nodes + evidence log + ceremonies — run by a parent, alongside real school from age 7. Nobody has added this up. A single worked example ("week in the life at age 6: X minutes parent, Y minutes child") would either validate the design or force healthy pruning. This is the likeliest real-world failure mode of the whole system.
2. **Day-1 frontier problem.** Twelve tier-0 roots are simultaneously Available, but the frontier discipline says show 3–5. Which 3–5? Who chooses the starting subset, and on what basis? Unaddressed in both documents (poster spec presumably — but the *rule* for choosing belongs in the framework).
3. **The training-grounds flag exists nowhere in the data.** CR1 requires the two explicit-instruction strands be "flagged visually"; TR4 requires register skins. The JSON schema has no field for either, yet the JSON is declared "the canonical data" that downstream tooling parses. Add `strand: explicit|guided` and `register` fields (or explicitly assign the flags to the poster spec *by node id list*, so it's checkable).
4. **Estonian-language content in an English-language system.** `lit-ee-decoding`, `lit-reading-fluency`, `lit-writing-sentences` prescribe Estonian-text exercises ("read a short Estonian sentence…") inside a system whose scope statement says "English-language materials." Who authors the Estonian booklet content, or are these nodes checked via school evidence only? One sentence would resolve it; right now the booklet pipeline can't act on these nodes.
5. **Dropped consensus edges without rulings.** Framework §6 chains include "sorting/patterning → counting principles" and "oral language → phonological awareness"; neither edge exists in the graph (`num-counting-cardinality` and `lit-phonemic-awareness` are roots). Presumably casualties of the fan-in cap — fine, but the appendix claims the R3 chains were adopted "verbatim as the safe dependency edges." Note the omissions or add soft edges.
6. **Equipment as a hard gate.** The entire DIG chain funnels through `dig-beebot-arrows` (needs a Bee-Bot or floor-grid setup). R4 C3.4/A6.6 required ≥2 paths into gateways precisely so "one hated activity type never blocks the tree" — the learning path dropped the redundant-paths rule for tiers 0–3 without a ruling. Paper-only arrow programs are already in the exercise text; make the node explicitly satisfiable without hardware.

---

## 6. Claims verified as holding (so later loops need not re-check)

Fan-in ≤ 2 everywhere; tier counts 16/15/16/13/9/9 = 78; graph is acyclic; every non-tier-0 node has ≥1 prereq; all careers reachable from tier-0 roots; longest intra-tier chain 2; longest tier-0–3 spine 7 (the numeracy chain); composition correctly gated on transcription (Berninger); fractions built from sharing after mult-groups; concept-before-drill order for tables; `sci-fair-test` at ~9 and SEL ladder match the R3 consensus rows; B15/B16/B19 are faithfully instantiated in the sudoku nodes; anti-comparison/no-red-ink language is consistent throughout.

---

## 7. Priority order for the fix loop

1. M2 (restore age-8 capstone quests) and M1 (grade anchoring) — they change the tier table, so do them before any poster work.
2. M3 + §5.6 (unlock CRE and DIG chains; reintroduce OR-groups/soft edges).
3. M4 (ancestor-closure rule or reachability-based highlighting) + M7 (English oral chain) + M6 (demote the 0–100 edge) — pure graph edits.
4. M5 (split bundled nodes) — do together with 3 to keep counts honest.
5. F1–F7 and §3 prose corrections — one editing pass over both documents.
6. §5.1 parent-load worked example — one page, high value.
