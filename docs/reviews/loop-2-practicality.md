# Loop 2 Review — Practicality & Completeness

**Reviewer focus:** reachability, prerequisite sanity, JSON/prose consistency, parent/teacher usability, difficulty-ramp realism, gaps/dead-ends/orphans.
**Documents reviewed in full:** `docs/methodology/combined-framework.md` (v1.1), `curriculum/learning-path.md` (v1.1). Research reports consulted for grounding (R4 C3.4 redundancy rule, R4 C2/C3.2 caps).
**Method:** the JSON block was extracted and validated mechanically (Python script: parse, unique ids, reference resolution, acyclicity via toposort, tier ordering, fan-in caps, per-tier counts, edge counts, cross-domain edge census, ancestor closures per career, sink analysis, intra-tier chain lengths, ageBand/tier consistency, boss-gate consumers). Findings below distinguish what was verified from what was inferred.

---

## 0. Verification of v1.0→v1.1 fixes and structural claims (all mechanically confirmed)

The following v1.1 claims were re-derived from the data, not trusted:

- JSON parses; all ids unique; all `prereqs`, `careers`, `quest`, `capstone_prereqs` references resolve.
- Graph is acyclic (topological sort completes 93/93); no prerequisite points to a later tier.
- Tier counts 17/18/15/24/10/9 = 93, matching §1 and §7. Twelve tier-0 roots; every zero-prereq node is tier 0; every non-tier-0 node has ≥1 prereq.
- Edge count 123 exactly; cross-domain edges 31 exactly (the doc's "31 of 123 ≈ 25%" is accurate). The "4 bridges after exclusions" figure is reproducible under one defensible reading (lit-letter-knowledge→mot-letter-formation, mot-letter-formation→log-sudoku-symbols, dig-beebot-arrows→log-decompose-debug, log-decompose-debug→dig-scratch), though the doc never enumerates them — see issue 2 note.
- Fan-in ≤2 everywhere except `t5-research-project` at 3, as claimed.
- Longest intra-tier chain is 3 (claim: ≤3, budget 6); longest tiers-0–3 chain is 9 ending at `num-problems-data` (claim: 9). Verified.
- Both boss milestones gate only numeracy consumers (`num-addsub-20` → addsub-100, mult-groups, money-time; `num-times-tables` → problems-data). The "never cross-domain" ruling is honored in the data.
- CR14 re-banding is applied consistently in both files' tier/band tables; the sudoku ladder in the graph matches §4.4 (boxes at S3/tier 1 on 4×4; 6×6 at S4/tier 2; 9×9 intro at S5/tier 3); English oral leg has its tier-1 continuation and `lit-en-reading` carries the twin Simple-View prereqs; fluency nodes are staged (addsub-10/20, tables-1/times-tables); all 8 quest nodes exist with resolving `quest_for`/`quest` links; every career closure bottoms out in tier-0 roots.

Loop-1's claimed fixes hold. The problems below are new findings, mostly at the layer the validator cannot see: prose-vs-graph semantic mismatches and operational feasibility.

---

## 1. CRITICAL — Booklet #1 is locked on day one by its own prerequisite semantics

`log-sudoku-4x4` — "Booklet #1's home node" — requires `log-sorting-patterns` AND `ef-attention-persist` to be **Consolidated** (framework §5.1: only Consolidated satisfies prerequisites; Consolidated = check passed again ≥2 weeks after Mastered). Worse, `ef-attention-persist` is an Archetype-B observation tally: ≥3 unprompted instances logged across ≥2 weeks — twice, presumably, to consolidate.

Consequence, taken literally: a family that buys the flagship sudoku booklet cannot legitimately open it for roughly 4–6 weeks. And the circularity is doctrinal: GP16 says EF is "trained through games-with-rules (sudoku included)" — the attention node that gates sudoku is supposed to be trained *by* sudoku-class games.

The starting-frontier rule (framework §5.1) surfaces four *roots* on day 1, and `log-sudoku-4x4` is not a root, so this is not a corner case — it is the designed day-one experience colliding with the designed first product.

**Fix (pick one, document it):** (a) make booklet 1 self-contained — its opening pages *are* the sorting/pattern content and the S1 rows-only strips, and completing them counts as the prerequisite checks (the booklet already spans S1–S2, so this is nearly free); (b) demote these two intra-tier-0 edges to soft edges; or (c) rule explicitly that tier-0 intra-tier edges gate *credit*, not *access*.

---

## 2. CRITICAL — The Band-2+ daily session is double-booked; no weekly domain allocation exists

Framework §3 (dose row) + B18 + §5.6, taken together for Band 2 (6–7, session 15–20 min, 6×/week):

- Every session opens with a ~2-min retrieval strip (B18).
- Alternating days carry ~15 min English phonics **or** ~10 min number-fact retrieval (§3 dose row) — so all 6 weekly sessions are training-ground days.
- B18 simultaneously defines a booklet as "one 2-page spread **per session**."
- Unlock trials (<10 min) ride inside the session some weeks (§5.6).

Arithmetic: phonics days have 17 of 15–20 minutes committed before any booklet spread, sudoku page, science experiment, spatial work, or SEL/COM activity happens; number days leave 3–8 min. Across the week that is ~0–25 leftover minutes for the **eight other domains**, which hold 14 of tier 1's 18 nodes. §5.6 prices *parent* load carefully but never allocates *content*: there is no worked weekly template anywhere showing how 10 domains share 6 short sessions. Either the dose row, B18's spread-per-session, or the session lengths must give; currently the three specs cannot be simultaneously true, and the thing that silently dies is exactly the guided-play majority of the curriculum (inverting CR3's "structured practice is a scheduled dose, never the whole diet").

**Fix:** publish a binding weekly template per band (e.g., Band 2: 2 phonics sessions, 2 number sessions, 2 free-choice/booklet sessions; fluency maintenance between doses rides the retrieval strips), and amend B18 to "one spread per *booklet* session."

---

## 3. MAJOR — The "common trunk inherited by all eight careers" claim is false in the graph

Learning-path §1: "The shared trunk — EF, the SEL core, oral communication, literacy, and the numeracy chain through the boss gates — feeds all eight careers… lives in the trunk's *reachability*." §4 preamble: "All eight also inherit the common trunk: `ef-attention-persist → ef-plan-check`, the literacy root, and the numeracy chain through `num-addsub-20`."

Computed hard ancestor closures (quest ∪ capstone_prereqs) say otherwise:

- **Lawyer** (21-node closure): contains **zero numeracy nodes**, **zero EF nodes**, zero science, zero logic/digital, zero English-track literacy. Neither boss gate is in any lawyer path.
- **Doctor** (43 nodes): **no EF node** in the closure.
- **Software engineer** (41 nodes): **no EF node** (both EF out-edges — to `cre-iterate-v2` and `quest-scientist` — miss its closure; the sudoku line that would carry `ef-attention-persist` is enrichment-only).
- **Finance** (26 nodes): **zero literacy and zero communication nodes** — a highlighted Finance path never requires learning to read.

Since §1 makes path-highlighting *computed from reachability, never from tags*, the tool built to those rules will contradict the document's own promise: "what do I need to open Lawyer?" answers with no arithmetic at all, and GP16's "EF trunk feeds every branch" is implemented as out-degree 3 from `ef-plan-check` into two branches. Note the irony: the bridge-cap definition *excludes* "edges fanning out of the EF trunk — EF feeds every branch by design" — an exclusion clause for edges that mostly do not exist.

**Fix:** define a named `trunk` node set (e.g., `ef-plan-check`, `num-addsub-20`, `lit-comprehension` or `lit-reading-fluency`, `com-explain-decision`, `sel-cooperation`) that is implicitly unioned into every career's `capstone_prereqs` (documented in §1 and enforced by the validator), **or** soften §1/§4 to say the trunk is a poster-layer/curricular guarantee, not a graph property. The first option is truer to GP12/GP16.

---

## 4. MAJOR — The redundancy argument is logically backwards under AND semantics

Learning-path §3 (tier 5): "each of those single vestibules has two tier-4 inbound routes, so one hated subject still cannot wall off the wonder." With AND fan-in — and v1.1 uses **only** AND; OR-groups are "permitted by the schema but unused" — two inbound edges mean **both** are mandatory. Two routes *into* a node under AND is anti-redundancy: more ways to be blocked, not an alternative path. R4 C3.4's original rule ("at least two routes into every tier-gateway node, so one hated activity type never blocks the tree") only achieves its stated purpose if the routes are OR-alternatives; the research doc conflates the two and v1.1 inherited the conflation while explicitly dropping the OR mechanism.

Concrete chokepoints as shipped: a child who hates formal debate loses **lawyer and manager** (t4-debate is a hard leg of both t5-argument-law and t5-org-leadership); a child who resists extended writing (t4-academic-writing) loses **lawyer, scientist, and doctor**; t4-english-fluent gates doctor, scientist, and software-engineer simultaneously. The activity-agnostic node specs (paper-only Bee-Bot, any-puzzle Puzzle Maker) genuinely mitigate at tiers 0–2 but do nothing at tiers 4–5 where the claim is made.

**Fix:** either introduce real OR-groups at the tier-4/5 layer where alternatives are honest (e.g., t5-argument-law: t4-debate AND (t4-academic-writing OR a moot-court-portfolio alternative)), or delete the redundancy sentence and state plainly that career wonders have chokepoints — which is defensible (careers are aspirational lore, CR12) but must not be sold as redundancy.

---

## 5. MAJOR — No cold-start / placement protocol exists

Both documents assume a blank-slate child starting at ~5 with all tier-0 nodes unmastered (starting-frontier rule, day-1 poster). There is no procedure for: a 6–8-year-old entering the system; a 5-year-old who already counts to 20 and holds a tripod grip; or (per GP1's own mastery-not-age doctrine) any child whose real frontier is mid-tier-1 on day one. Under the state machine as written, every already-possessed skill still costs a check, a ≥2-week wait, and a re-check *per node, in dependency order* — weeks of ceremony before the child touches their actual frontier, which is precisely the demotivation pattern §5.5 bans. Grep confirms: no placement, onboarding, or grandfathering text in either file.

**Fix:** add a placement ruling to framework §5.1: on system entry, the parent runs a batched placement sweep (top-down from the estimated frontier, using the same per-node checks); nodes passed at placement are marked Consolidated directly (the two-session spacing requirement is waived **for placement only**), decay timers start at placement date.

---

## 6. MAJOR — `num-numbers-100` can never be Consolidated as specified (deadlock)

The node's description: "its mastery check lives downstream in `num-addsub-100`'s place-value work." But `num-addsub-100` lists `num-numbers-100` as a hard prerequisite, and only **Consolidated** nodes satisfy prerequisites. A literal implementation deadlocks: the node cannot be checked until a node that cannot unlock until this node is checked. A human parent will improvise; the tooling §7 promises (and the frontier computation) will not.

**Fix:** give `num-numbers-100` its own modest check (reads, writes, orders numbers to 100 — pass/fail-able in 10 minutes) and defer only the *linear-placement accuracy* criterion downstream, which is what the Siegler & Booth note actually requires.

---

## 7. MAJOR — The sudoku line is a dead end; framework §4.4 promises feeds the graph doesn't deliver

Framework §4.4 (tree placement): picture sudoku "feed[s] LOG debugging/conditionals, NUM systematic checking, and … the COM reasoning bridge." In the graph, the entire four-node sudoku chain has **zero outgoing hard edges** — `log-sudoku-master` is the only non-quest sink in tiers 0–3 (mechanically confirmed). `log-decompose-debug` descends from `dig-beebot-arrows`, not sudoku; `com-because-reasons` descends from `com-retell-story` (sudoku appears only in its flavor text). All promised feeds live as soft edges in a poster spec that does not yet exist. The learning-path is internally honest about this (R4 A4.3 anti-lock rationale), but the two canonical documents now disagree about the structural role of the first product: the framework claims the sudoku cluster is a load-bearing "tier 0 entry node… feeding" three branches; the graph makes it structurally optional for every career and every era.

**Fix:** either (a) rewrite framework §4.4's tree-placement paragraph to say "soft-feeds (poster layer)"; or (b) add one honest hard edge — `log-sudoku-boxes` is a genuinely strong preparation for `log-decompose-debug`'s find-the-bug work and could stand as an OR-alternative to `dig-beebot-arrows` if OR-groups are activated (see issue 4). Do not leave the contradiction: a future author will "fix" the graph against §4.4 and hard-lock the creativity/logic branches behind sudoku, the exact R4 anti-pattern.

---

## 8. MAJOR — The English oral-comprehension leg idles through tier 2 (age 7–8)

The strand runs `lit-en-oral-vocab` (t0) → `lit-en-oral-2` (t1) → *nothing at tier 2* → consumed by `lit-en-reading` (t3). So the leg that GP10 says "starts hard at 5" and that loop 1 specifically wired in "so the oral leg of the Simple View never idles" has no node, no exercises, and no scheduled work for the entire grade-1 year — while the decay rule (8–12 weeks) would mark a tier-1 oral node Needs-polish long before its tier-3 consumer arrives. Families will keep reading aloud anyway, but this is the one strand the docs insist the school will not supply, in the exact year English decoding (phonics-2) ramps and could crowd it out. Related: `t4-english-fluent` ("writes and presents comfortably in English") has no English *writing* ancestor anywhere — its writing leg is Estonian `lit-composition`; acceptable for a coarse tier-4 bundle, but worth a note in its description.

**Fix:** add `lit-en-oral-3` at tier 2 (listens to longer English read-alouds/audio, retells, growing vocabulary — cheap to author, mostly parent read-aloud protocol), prereq `lit-en-oral-2`, and repoint `lit-en-reading`'s comprehension-leg prereq at it.

---

## 9. MINOR — `dig-typing`'s prerequisite fails the doc's own load-bearing test

`dig-typing` ← `dig-scratchjr`. The test ("could the child plausibly do B well without A?") fails: typing has no dependence on block programming. The edge exists to satisfy invariant 2 inside the branch. The honest prerequisite is `mot-letter-formation` (letter knowledge + output mapping) or `lit-writing-sentences` (something to type). Swapping it costs nothing structurally (fan-in stays ≤2) and would slightly raise the cross-domain count by one — fine.

## 10. MINOR — Quest exercises demand skills outside their prerequisite closures

- `quest-manager` ("shopping list inside a set budget") needs euro arithmetic; `num-money-time` is not in its closure (prereqs: ef-multistep-projects, sel-conflict-resolution).
- `quest-doctor`'s chart-writing assumes handwriting/recording fluency; no literacy or motor node is in its closure.
The fan-in-2 cap forced these choices, which is fine — but the quest cards should carry an "assumes you can also…" line (soft-prereq list) so an 8-year-old's computed "first door" answer doesn't overpromise. Cheap fix in the booklet pipeline spec.

## 11. MINOR — Needs-polish prerequisite semantics are undefined

Framework §5.1: only Consolidated satisfies prerequisites; a decayed node moves to Needs-polish. Unstated: does Needs-polish still satisfy? A literal tool re-locks the entire downstream subtree after a summer holiday — half the colored poster goes dark, the precise demotivation §5.5 bans. Intent is clearly "dims but keeps satisfying" (content merely re-enters warm-ups). Write one sentence saying so.

## 12. MINOR — Consolidation is undefined for observation tallies, quests, and multi-week sub-checks

(a) Archetype-B: what does "check passed again ≥2 weeks later" mean for a ≥3-instances-over-≥2-weeks tally — three more instances? (b) Quest nodes: is a week-scale restaurant night to be *re-run* two weeks later to consolidate? (Harmless since quests are sinks, but the state machine claims to apply to all nodes.) (c) Several sub-checks are themselves multi-week (num-money-time's savings-jar chart, ef-goal-setting's month chart) inside nodes governed by the 1–3-week granularity rule, without an extended-fluency flag. Rule once: quests and month-scale dispositional nodes are "Mastered = done, Consolidated = Mastered" (single-shot), tallies consolidate by one further logged instance after 2 weeks.

## 13. MINOR — Tier-3 numeracy quietly reintroduces the one-year run-ahead CR14 corrected

Numbers to 10,000, brackets (`num-multidigit`), fractions (`num-fractions`), perimeter + two-step problems (`num-problems-data`), full korrutustabel — i.e., nearly the entire Estonian grade-3 checkpoint list — all sit in tier 3, ageBand 8–9 = grade 2, with nothing of it in tier 4. The walkthrough discloses "at or ahead of Estonian grade 2… typically met across the tier-3/4 boundary," but the data disagrees with "across the boundary": the whole list is banded 8–9. This is exactly the silent drift CR14 existed to purge, returned as default calibration. Bands are calibration not gates (GP1), so severity is minor — but annotate `num-multidigit` and `num-problems-data` as "grade-3 checkpoint content; completing during tier 4 is normal" (the same disclaimer `num-addsub-20` carries), so the poster doesn't imply an 8-year-old is behind.

## 14. MINOR — Gross motor is in the domain spec but absent from the graph

Framework §6 MOT-SPA scope and chain begin "gross before fine; proximal→distal"; the graph's motor entry point is tripod grip. At 5, gross-motor items (balance, ball skills, bilateral coordination) are koolivalmidus-relevant and cheap to include as one tier-0 cluster/observation node (or explicitly rule them out of scope as "life, not system" — either is fine, but currently the framework promises what the tree omits).

## 15. MINOR — The next deliverable needs 17 mastery checks that don't exist yet

§5.2 says every node ships with a written parent-runnable criterion; 91 of 93 defer to a booklet pipeline that hasn't started. Fine as an authoring order, but the tier-0 poster (named "first tree deliverable" in §7) is unusable without the 17 tier-0 checks — the poster's whole mechanic is coloring nodes on passed checks. Sequence the tier-0 check authoring *with* the poster, not with the (later) booklet pipeline.

## 16. MINOR — `lit-ee-decoding` (tier 1, koolieelik year) cites a material source that doesn't exist yet

§7 sources Estonian-track exercises from "the child's Estonian school materials… from age 7." The node is banded 6–7 — the year *before* school. In practice lasteaed's koolieelik prep partially covers it, but the sourcing note should say "lasteaed koolieelik materials and parent-run veerimine games" for tier 1, reserving "school materials" for tiers 2–3.

---

## Summary

The graph is mechanically sound and the loop-1 fixes genuinely hold — the remaining defects are in the semantic layer the validator can't see. The two critical items are both about the **first month of real use**: booklet 1 is unopenable under the system's own unlock rules (issue 1), and the daily session cannot hold what three different rules put inside it (issue 2). The three most consequential doc-vs-data contradictions are the trunk-reachability claim (issue 3), the AND-semantics redundancy claim (issue 4), and the sudoku feeds (issue 7) — each will mislead the first tool or author that trusts the prose. Issues 5, 6, 8 are single-paragraph fixes that close real deadlocks/gaps. Everything else is polish.
