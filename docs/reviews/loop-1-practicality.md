# Loop 1 Review — Practicality & Completeness

**Reviewer focus:** reachability, prerequisite sanity, JSON/prose consistency, parent/teacher usability, difficulty-ramp realism.
**Files reviewed:** `docs/methodology/combined-framework.md` (v1.0), `curriculum/learning-path.md` (v1.0), all four reports in `docs/research/` (skimmed for grounding).
**Method:** full read of both documents plus a programmatic validation pass over the embedded JSON graph (parse, uniqueness, reference resolution, topological sort, fan-in, dead-end enumeration, per-tier and cross-tier longest-path computation, per-career feeder and tag counts).

---

## 0. What actually checks out

To be fair before being critical — these claims were verified true by script:

- JSON parses; 78 nodes; all ids unique; all `prereqs` and `careers` references resolve.
- Graph is acyclic; every prereq points same-tier-or-earlier; every non-tier-0 node has ≥1 prereq; fan-in ≤ 2 everywhere.
- Tier counts match the prose exactly (16/15/16/13/9/9).
- Longest intra-tier chain is 2 (claim: ≤2 ✓). Longest chain within tiers 0–3 is 7 nodes and it is the numeracy spine (claim ✓).
- Six of the eight career spines in §4 trace along real edges end-to-end (doctor, software, manager, lawyer, scientist, engineer, finance — see below for the exception).
- The Estonian grade-3 checkpoint content (0–10,000, korrutustabel, fractions 1/2–1/5, perimeter, 2-step problems) is genuinely covered by tier-3 numeracy nodes. Koolivalmidus items are covered by tiers 0–1.
- Most exercise pairs are concrete enough for a parent to run tomorrow ("part-whole ladybirds 5 = 3 + □", "pay 1.40 € two ways, make change from 2 €"). This is a real strength.

Now the problems.

---

## 1. CRITICAL — Career path-highlighting is uncomputable from the canonical data

The tree's marquee feature (CR12: "what do I need to open Doctor?" path-highlighting) **cannot be computed from the JSON**, which §6 declares "the canonical data":

- Careers are records with `id/title/emoji/description` only. **No field links a career to its capstone prerequisites.** The t5→career association exists only as reverse inference through node `careers` metadata — which the document itself says is "highlight metadata, never gating."
- The metadata is far too noisy to drive highlighting. Measured tag counts across tiers 0–3 (of 60 nodes): **scientist 48, doctor 36, engineer 36, manager 30, lawyer 29, finance 27, software-engineer 27, entrepreneur 25.** Highlighting "scientist" would light 80% of the child's map — that is not a path, it is the whole tree, and it destroys the promised "opening options" reading.
- The actual spines live only in §4 prose, unreachable by tooling.

Also, §6's validation preamble claims "every career reachable from tier-0 roots" was *validated* — but with careers absent from the graph, that property is not even well-defined over the data. It happens to hold under the charitable reading (every t5 node chains to tier 0, every career is listed on ≥1 t5 node), but the claim as stated is unfalsifiable.

**Fix:** add to each career object either `capstone_prereqs: [t5-ids...]` (making careers real sink nodes, exempt from the fan-in cap) or a `spine: [node-ids...]` field mirroring §4. Then reachability and highlighting become checkable properties of the file. Re-run validation and state exactly what was checked.

## 2. CRITICAL — The entrepreneur spine is fictional and the creativity branch is broken

§4 gives the entrepreneur spine as `cre-idea-fluency → cre-make-own-puzzle → cre-iterate-v2 → t4-design-build`-or-`t4-money-management → t5-venture`. Checked against the JSON:

- **`cre-iterate-v2 → t4-money-management` does not exist.** `t4-money-management.prereqs = [num-money-time, ef-goal-setting]`.
- **`t4-design-build → t5-venture` does not exist.** `t5-venture.prereqs = [t4-money-management, t4-leading-teams]`.
- Therefore the creativity chain — the entrepreneur's *heaviest* domain per §2 — dead-ends at `cre-iterate-v2 → t4-design-build → t5-applied-engineering`, i.e. **into the engineer career**, and `t5-venture` (domain: creativity!) requires **zero creativity nodes**. A child can open "Run a Real Venture" having never made a puzzle, generated an idea list, or iterated a version 2.
- Structurally: creativity has nodes at tiers 0, 1, 2 and then nothing until tier 5. Ages 8–13 — exactly when the entrepreneur profile says idea fluency and iteration should compound — have no creativity nodes at all.

**Fix:** add a tier-3 creativity node (e.g. `cre-invent-product`: "invents and makes something for a real audience, v1→v2, and presents it" — prereqs `cre-iterate-v2`, `com-explain-decision`-ish) and a tier-4 one (or route `t5-venture.prereqs` through a creativity-bearing t4). Rewrite the §4 entrepreneur spine to match real edges.

## 3. MAJOR — `lit-en-oral-vocab` is an orphan; the English oral-language strand vanishes for 3 years

Script-confirmed: **nothing in the graph depends on `lit-en-oral-vocab` ("English Ears")**. It is the only non-terminal dead end in tiers 0–2.

This is not just a lint error — it contradicts the project's own doctrine three times over:

- GP10 makes English *language comprehension* from age 5 a load-bearing strand ("starts hard at 5").
- R2's design implications explicitly demand "a **separate node track** for 'English vocabulary & listening' starting at 5" (02-cognitive-science.md, §10 design implications) — a *track*, not one floating node.
- The Simple View / Scarborough logic the framework cites: reading = decoding × language comprehension. Yet `lit-en-reading` (t3, "reads short English texts independently") requires only `lit-en-phonics-2`. In the model as written, a child can "read English for real" with no modeled English vocabulary at all — decoding without comprehension.

Between tier 0 and tier 3 there are **no English listening/vocabulary nodes** (tier 1 and 2 have none), so a 4-year strand the prose says "runs hard" has nothing to master, nothing to decay, nothing for booklet warm-ups to sample.

**Fix:** add `lit-en-oral-2` (t1/t2: follows short spoken English stories, ~500-word receptive bank, answers who/what questions orally) and wire `lit-en-oral-vocab` → `lit-en-oral-2` → `lit-en-reading` (making `lit-en-reading.prereqs = [lit-en-phonics-2, lit-en-oral-2]` — fits the fan-in cap).

## 4. MAJOR — `t4-english-fluent` is a dead end above which everything implicitly needs it

"English as a Working Language" — which §2 and the node itself call "the system's working language secured" — **feeds nothing**. No tier-5 node requires it: not `t5-software-craft` (READMEs, docs, Stack Overflow), not `t5-research-project` (literature is in English), not `t5-financial-analysis` (annual reports). Every t5 vestibule silently assumes English fluency and none declares it.

**Fix:** make `t4-english-fluent` a prereq of at least `t5-software-craft` and `t5-research-project` (both currently have a free prereq slot... `t5-research-project` doesn't — it has 2. Either raise the cap to 3 for t5, which R4 C3.2 permits, or accept the trade and document it). At minimum, add a stated rationale for why it's a leaf.

## 5. MAJOR — Node granularity: the "1–3 weeks" rule is violated by an order of magnitude on the most important nodes

§1 restates R4 C2: every tier 0–3 node is "masterable in 1–3 weeks of 10–20-minute sessions." That is false for at least:

| Node | Realistic duration |
|---|---|
| `lit-en-phonics-1` (full SATPIN GPC set + CVC blending + decodable strips) | 2–3 school terms. R2 itself cites Seymour: English decoding takes 2.5+ years total; the tree compresses all of it into two nodes |
| `num-addsub-20` (fluency crossing ten, retrieval level) | most of a school year (it *is* the year-long era gate) |
| `num-times-tables` (full korrutustabel ×/÷ retrieval) | a school year (Estonian curriculum spreads it over grades 2–3) |
| `lit-reading-fluency`, `mot-handwriting-auto` | each a year-scale automatization |

Consequences are practical, not cosmetic: a child sits in "Practicing" on `lit-en-phonics-1` for 6+ months with zero visible tree progress — precisely the motivation failure GP13 and the frontier design exist to prevent; and booklet warm-ups (B18) can't sample "last week's node" when nodes turn over quarterly. Either the granularity claim must be dropped (bad — it's evidence-based), or these nodes must be split: phonics-1 into 2–3 GPC-set nodes, addsub-20 into "within 10" / "within 20 crossing ten", times-tables into the standard 2-5-10 / 3-4-8 / 6-7-9 stages. Note the node budget (78 of ~120–160) has room for exactly this.

## 6. MAJOR — The sudoku line's ages contradict the framework's own booklet spec (and the framework contradicts itself)

The first shipping deliverable hangs on these nodes, so this needs settling now:

- Framework §4.4 (mirroring R1 §8.1 exactly): S3 = **4×4** with 2×2 boxes at **6–7**; S4 = **6×6** at **7–8**; S5 = 6×6 hard + 9×9 intro at **8–9**; S6 = 9×9 + variants at **9+**.
- Framework §3 band table says instead: 6×6 at **6–7**, first 9×9 at **7–8**, 9×9 digits + variants at **8–9**. **§3 and §4.4 disagree by a full year at every step.**
- The tree follows §3: `log-sudoku-6x6` (t1, 6–7), `log-sudoku-symbols` (t2, 7–8, "first 9×9"), `log-sudoku-master` (t3, 8–9, variants). So learning-path node content runs one S-level ahead of the booklet spec the same file cites as "exactly as specified in framework §4.4" (§7 of learning-path — that sentence is currently untrue at the content level).

Two smaller sudoku slips in the same nodes: (a) `log-sudoku-6x6` says "box rule introduced alone" — per S3 the box rule is introduced on **4×4 with 2×2 boxes**, and a 6×6's boxes are 2×3; the node erases the 4×4-with-boxes stage entirely. (b) Its exercise cites "Booklet levels S3-S4", spanning two booklet levels and two years of the §4.4 table inside one "1–3 week" node — same granularity disease as issue 5.

**Fix:** pick one timetable (the conservative §4.4/R1 one is the evidence-cited one), correct §3's band row or §4.4, then re-band the three sudoku nodes and their descriptions to match. Mastery gates age anyway (GP1), so the fix is cheap — but the *documents* must agree, because booklet 2's spec will be copied from one of them.

## 7. MAJOR — Era/boss-gate semantics are undefined where data meets doctrine

Framework §3 and learning-path §1 say the two boss milestones "close" / "gate" the eras. But in the graph, `num-addsub-20` gates only its numeracy descendants; nothing stops a child reaching every tier-3 SEL/COM/science node while the boss milestone is unmastered. So what does "closing Foundations" *mean* operationally? Three incompatible readings are all consistent with the text: (a) ceremonial only (poster celebration, no gating); (b) the tier-N+1 *poster* is withheld until the boss is Consolidated (a hidden global AND-gate that contradicts "mastery gates progression per-skill"); (c) only the numeracy branch waits. Downstream tooling (poster generator, frontier logic) cannot be built until one is chosen. Recommend (a) explicitly, in both files, since (b) would let arithmetic block a child's science frontier — exactly what GP1 forbids.

## 8. MAJOR — Dispositional nodes cannot be checked by the assessment machinery as specified

Framework §5.2 defines the universal check format: 5–10 items, parent-runnable in <10 minutes, passed twice ≥3 days apart. That format fits fact-fluency, but is meaningless for a third of the tree: `sel-conflict-resolution` ("resolves peer conflicts without an adult"), `ef-attention-persist` ("sustains a task 10 minutes"), `sel-cooperation`, `ef-goal-setting` ("tracks a goal for a month" — the node's own exercise takes 4× longer than the claimed mastery window), `sel-team-roles`. These are observed-over-weeks dispositions. Nothing in either document defines an observation-based check protocol (e.g. "parent logs 3 unprompted instances across 2 weeks"). Since "only Consolidated satisfies prerequisites," fuzzy SEL/EF checks will silently become either rubber stamps or bottlenecks — and `ef-plan-check` feeds *every* branch.

**Fix:** add a second check archetype to §5.2 (naturalistic observation tally with a concrete threshold) and tag each node with which archetype applies.

## 9. Prose/data mismatches (each small, collectively corrosive to trust in the doc)

1. **"the ten roots"** (learning-path §3, tier 0 heading): tier 0 has 16 nodes of which **12** are zero-prereq roots. Neither number is ten.
2. **"Nine bundles, one per major strand"** (§3, tier 4): tier 4 has numeracy ×2, literacy ×2, and **zero** nodes for logic, EF, and creativity. Not one-per-strand on either side.
3. **"every career is reachable through at least two tier-5 feeders except the single-feeder software, lawyer and engineer vestibules"** (§3, tier 5): by `careers` metadata, software-engineer has **2** t5 feeders (`t5-software-craft`, `t5-advanced-math`) and engineer has 2; only lawyer is single-feeder. The sentence conflates "vestibule dedicated to X" with "feeder listing X" — and neither concept exists in the data (see issue 1).
4. **"Nine tracked domains"** (framework §6): the table lists **ten** (LIT, NUM, LOG, SCI, SEL, EF, COM, DIG, MOT-SPA, CRE). The arithmetic in the intro (R4's nine + SCI, with SPA merged into MOT-SPA) also yields ten. Learning-path §1 correctly lists ten without noticing the conflict.
5. Learning-path §7 claims the sudoku line hangs off the nodes "exactly as specified in framework §4.4" — untrue at the age/content level (issue 6).
6. Frontier rule says the child sees "3–5 Available nodes," but 12 tier-0 nodes are Available on day one. Presumably the poster spec curates; neither document says so or says how the 12 are throttled to 5.

## 10. Minor gaps and nits

- **`log-sudoku-master` is a tier-3 dead end.** Defensible (hobby capstone), but given the software-engineer §2 blurb calls the sudoku line "the tree's signature on-ramp," consider a soft edge into `t4-programming` at poster level, or say why not.
- **No typing/keyboarding node** anywhere, though framework §3 band 4 promises "typing introduced" at 8–9 and `t4-programming` presupposes it.
- **Doctor's SEL story stops at tier 3.** §2 calls the empathy/inhibition pairing "decisive" for doctor, but no t4/t5 node on the doctor path touches SEL (`t4-leading-teams` is manager/entrepreneur-tagged only). Coarse tiers excuse some of this; a doctor tag on `t4-leading-teams` or an SEL flavor in `t5-life-sciences` (bedside-manner shadowing exercise exists there already) would close it.
- **E-safety** is one exercise bullet inside `dig-scratchjr` ("family screen-rules card") despite DIG's spec saying "threaded from first screen contact." Thin. Fine for v1 if the booklet pipeline owns it — say so.
- **Estonian/English GPC interference:** `lit-en-phonics-1` requires `lit-letter-knowledge` (letters with *Estonian* sound values). R2 explicitly warns about interference (Estonian 1:1 vs English many-to-one). The dependency is right, but the node description should carry the interference warning the research demands; currently only "tricky code" framing survives.
- **Two nodes embed their unlock trials inside `exercises`** (`num-addsub-20`, `num-times-tables`) while all other nodes defer checks to the booklet pipeline. Schema inconsistency — either all nodes get a `mastery_check` field (per R4 C6's YAML sketch, which the framework §5.3 endorses) or none embed it.
- `log-sudoku-symbols` (writing digits) has a free prereq slot and no dependency on numeral formation (`mot-letter-formation`, which explicitly covers numerals). Cheap, sensible edge.
- Exercise vagueness spots (rare, but they stand out against otherwise concrete guidance): "Spaced fluency ladder: 3 gentle minutes, chart your own curve" (what is a ladder? what is charted?); "Booklet levels S3-S4" (a pointer, not an exercise); `t5-*` exercises are fine as vision but are not exercises in the C2 sense — flag them as illustrative.

## 11. Priority fix list for loop 2

1. Model careers in the JSON (capstone prereqs or spine field); re-run and honestly restate the validation claims. (Issue 1)
2. Repair the creativity/entrepreneur chain: t3 creativity node + t5-venture prereq rewire + §4 spine correction. (Issue 2)
3. Wire `lit-en-oral-vocab` into a track ending at `lit-en-reading`; add the missing t1/t2 oral-English node. (Issue 3)
4. Give `t4-english-fluent` downstream consumers or a stated exemption. (Issue 4)
5. Split the four-plus year-scale nodes or amend the granularity claim. (Issue 5)
6. Reconcile framework §3 vs §4.4 sudoku ages; re-band the three sudoku nodes. (Issue 6)
7. Define boss-gate semantics (recommend: ceremonial). (Issue 7)
8. Add an observation-based mastery-check archetype for SEL/EF/dispositional nodes. (Issue 8)
9. Sweep the six prose/data mismatches in §9. (mechanical)
