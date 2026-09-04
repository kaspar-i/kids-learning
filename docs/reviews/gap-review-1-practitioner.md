# Gap Review 1 — Practitioner (early-primary / school-readiness)

**Reviewer stance:** 25 years in Estonian/Nordic kindergarten and grades 1–3; reviewing for what is *missing*, what will not survive contact with a real 5-year-old or a real family week, and incoherence. Explicitly NOT re-auditing internal arithmetic — five prior loops did that, and my own spot-checks (tier counts 18/18/17/26/11/10, trunk membership and ancestor-closure, keystone census of 24, the two-file v1.5 status stories) all came back clean.

**Documents read in full:** `curriculum/learning-path.md` (v1.5, incl. the JSON block), `docs/methodology/combined-framework.md` (v1.5). Skimmed for grounding: the four research reports, `README.md`, `STATE.md`, `scripts/generate_sudoku.py`, loop reviews 1–5.

**Classification used throughout, as instructed:** *missing from the GRAPH* / *covered in framework prose but absent from the graph* / *deliberately out of scope per an explicit ruling*. Where something looks missing but is actually covered elsewhere, I say where.

---

## Overall verdict

This is the most internally disciplined home-learning design I have ever reviewed — the mastery machinery, the anti-pressure rulings, the honest chokepoint admissions and the ops pricing are genuinely excellent — and it is also, unmistakably, a tree built by people who think a childhood is made of literacy, numeracy and computational thinking. The academic core is over-engineered to a jeweler's finish while an entire stratum of what Estonian kindergarten and grades 1–3 actually consist of — music, movement after age six, practical life, traffic safety, health, the human body, Estonian cultural belonging, reading for *pleasure* — is either absent or waved at in prose, even though the framework twice claims national-curriculum coverage it does not have. Two incoherences rise to blocking: the only shipped child-facing artifact (the Animal Sudoku booklet) violates the converged sudoku doctrine that learning-path §7 claims it follows "exactly," and the English strand's load-bearing daily read-aloud is simultaneously required by three trunk nodes and ruled out of existence by the framework's own "non-session days carry no system work" rule. Everything blocking or important is fixable with roughly ten small nodes, two framework rulings, and one honest sentence replacing each overclaim; nothing requires re-architecting.

**Finding counts:** 2 blocking, 10 important, 11 nice-to-have. Also noted: 6 suspected gaps that turned out to be covered or deliberately ruled — credited in §1.6.

---

## 1. Missing skills and domains

### 1.1 BLOCKING (none in this area — see §4 for the two blockers)

### 1.2 Important

**I-1. Practical life / self-care — missing from the graph; partially in framework prose; the research layer itself dropped it.**
- What: dressing (zips, laces at ~6), tidying own materials, table setting, eating independence, simple food-preparation involvement — Montessori's practical-life pillar and a literal *koolivalmidus* criterion (R3: "Koolivalmidus: ... independence in dressing/eating," "self-dressing"; Finland's "taking care of oneself" competence).
- Evidence of the drop: framework §6's own SEL root row lists "separation/**self-care**" as a tier-0 root — but the actual node `sel-emotions-turns` contains no self-care sub-check. The prose promised it; the graph lost it. Worse, research report R1 contains *no mention at all* of Montessori practical life (searches for "practical life," "pouring," "grace and courtesy," "dressing" return nothing) — the omission is upstream and propagated. Partial graph coverage exists only as scattered exercise lines: "Own the backpack checklist" (`ef-multistep-projects`), "takes responsibility for own tasks and belongings" (`sel-conflict-resolution`, 7–8).
- Where it should live: tier 0, SEL or MOT-SPA, Archetype-B observation cluster, never gating anything.
- Fix: add `sel-selfcare` (tier 0, `cluster: true`, `check: "B"`): (a) dresses fully independently incl. fastenings, laces by ~6; (b) tidies own activity materials without prompting (this is also control-of-error culture — the booklet system depends on it); (c) sets/clears the table or equivalent daily contribution. Prereqs `[]`. Restore "self-care" to the §6 SEL root row truthfully, and note the R1 research gap in the framework's provenance.

**I-2. Safety and health literacy — missing from graph AND framework; only e-safety exists.**
- What: pedestrian traffic rules (a *named koolivalmidus outcome*: "traffic safety rules as a pedestrian" — this child walks to school alone at 7, in Estonian winter darkness where a helkur/reflector is legally required), water safety, stranger script, home-alone basics; hygiene, sleep, food, daily rhythm. R3 records that *inimeseõpetus* (grades 1–3) covers "daily rhythm and time use, health, safety, money basics" — the tree took the money and left the rest. The DIG branch's e-safety thread is real but is the *only* safety content in 100 nodes.
- Where: tier 0–1, SEL or SCI, Archetype-B cluster; sleep/food/hygiene as a Life-costume (B13) content set, not drills.
- Fix: add `sel-safe-well` (tier 0–1, cluster, check B): (a) crosses streets by the rules on real walks, tallied; (b) reflector/helmet habit in season; (c) knows the stranger/lost script and own address; (d) water rules said and followed at the pool. Health-rhythm content (why sleep, washing hands, teeth) enters as sci/booklet Life pages — no check needed beyond the cluster. Never a prerequisite of anything.

**I-3. Physical education after age six — the gross-motor strand dead-ends at tier 0; school swimming is invisible.**
- What: `mot-gross-body` (5–6) is a documented leaf (loop reviews confirm) — and then the entire gross-motor half of MOT-SPA vanishes for the remaining 12 years of the tree. Meanwhile R3 records that Estonian I kooliaste *kehaline kasvatus* includes a **compulsory beginner swimming course (target ~200 m)**, plus skating/skiing exposure norms and bike-riding at ~6. A tree that plans `t5-life-sciences` in detail but cannot see the statutory swimming course its own child will sit is academically lopsided in exactly the way GP16 warns against for EF/SEL.
- Where: tier 1–2 MOT-SPA continuation; observation-only; never gates desk work (same ruling `mot-gross-body` already carries).
- Fix: add `mot-gross-2` (tier 1–2, cluster, check B): (a) water confidence → readiness for the school swim course; (b) rides a bike; (c) seasonal skills exposure (skates or skis, per family). Soft-link from `mot-gross-body`. One sentence in framework §6 MOT-SPA acknowledging the swimming course as an external anchor alongside koolivalmidus.

**I-4. Music — missing from graph, framework, and scope rulings entirely.**
- What: singing in tune, steady beat, rhythm games, songs known by heart. *Muusika* is one of the Estonian kindergarten's seven statutory areas and a grades 1–3 subject; this is also the country of the laulupidu. The word "songs" appears in the system exactly once as a vehicle for English vocabulary (`lit-en-oral-vocab`). Beat-keeping and rhythm work are also cheap phonological-awareness allies (syllable clapping already lives in `lit-phonemic-awareness` — the bridge is right there).
- Deliberate scope-out? I checked: **no ruling excludes music.** There is no CR, no GP, no "lives elsewhere" note. It was simply never thought of. That distinguishes it from, say, wild nodes or third languages.
- Where: tier 0, a tenth-domain question the framework must answer honestly — either a small MOT-SPA/CRE-homed observation node or an explicit scope ruling.
- Fix (minimal): `cre-music-play` or `mot-rhythm-song` (tier 0, check B): keeps a steady beat, sings 4–5 songs from memory (Estonian repertoire welcome — see I-5), plays call-and-response rhythm games. Fix (honest alternative): a framework ruling stating music is deliberately left to lasteaed/huviring, with the §6 mapping claim corrected (see I-8). Either is acceptable; silence is not.

**I-5. Estonian cultural belonging — wild-node cover only; koolivalmidus names it.**
- What: "Estonia and its symbols" is a listed koolivalmidus outcome (R3); folk calendar (mardipäev, kadripäev, jõulud, vastlapäev), Estonian songs and rhymes, "knows some rhymes/poems by heart" (another listed koolivalmidus outcome). Current coverage: R1's wild-node *example list* mentions "Estonian folk songs" — i.e., culture survives only if the child spontaneously claims it. For an Estonian family deliberately running an **English-language home system** with English as the trunk's crown jewel, the identity counterweight deserves better than a blank node.
- Where: tier 0–1; fold into the seasonal scheduling layer the framework already has (§3 "autumn = measuring/harvest, winter = story/reading" — extend to the folk calendar), plus one small node.
- Fix: `sel-my-estonia` or a SCI Life-costume set (tier 1, check B or single-shot): knows flag/anthem context and own address; marks 3–4 folk-calendar feasts through the year; knows 2–3 Estonian songs/poems by heart (which also restores the memorization koolivalmidus item — see N-4). Alternatively an explicit ruling that culture is the poster's seasonal layer + wild nodes — but then §5.4's koolivalmidus claim must be trimmed (I-8).

**I-6. Reading for pleasure — the system trains decoding meticulously and appetite not at all.**
- What: every Estonian-literacy touchpoint in the graph is instrumental (veerimine ladders, dictation, comprehension checks on school texts). No node, check, or ruling anywhere concerns *choosing* to read, being read to in Estonian, library habit, or book ownership — the single strongest motivational lever this age band has, and the thing that actually separates fluent 9-year-old readers from reluctant ones. Framework §3 waves read-alouds into "ordinary childhood," which is precisely how they die in a working family's week (and see B-2: for English the same gesture creates a contradiction).
- Where: LIT, tier 2–3, dispositional.
- Fix: `lit-reads-for-fun` (tier 2–3, check B): child *unprompted* picks up and reads self-chosen material ≥3 times across 2 weeks; evidence line is a title log the child keeps. Plus one framework sentence making the (Estonian) bedtime read-aloud a named, protected family ritual rather than an unmentioned assumption. Careful: this node must never gate anything and must never get a reward attached (GP9 would be violated by paying for pleasure-reading — the check is observational only).

**I-7. Media consumption literacy — prose thread with no node, now overdue given the YouTuber career.**
- What: the DIG domain scope line promises "e-safety **and media judgment** threaded from first screen contact," but the graph delivers judgment nowhere: e-safety appears only as exercise lines (screen-rules card, account hygiene). Nothing anywhere teaches: this video wants your watch-time; that is an ad; that influencer is paid; why the algorithm feeds you more of the same. The v1.5 addition of a YouTuber career makes the tree actively glamorize the platform for an 8-year-old while never once training the 8-year-old *viewer*. The production side is genuinely well-gated (family-only publishing, parent-held gate — good); the consumption side is naked.
- Where: DIG, tier 2–3.
- Fix: `dig-media-sense` (tier 2–3, prereq `dig-scratchjr` or `dig-block-projects`): tells content from advertising in three real examples; explains in own words what a video/app gets when you keep watching; family watch-time agreement co-authored. Cheap, parent-runnable, and it makes the youtuber wonder honest.

**I-8. The two coverage overclaims — framework §5.4 and §6 assert what I-1..I-5 disprove.**
- What: §5.4: "the tree's tier-0/1 coverage should **demonstrably meet** [koolivalmidus]" — not while self-dressing, traffic rules, Estonia-and-symbols, healthy behaviour, poems-by-heart and gymnastics/skiing/skating exposure have no nodes (all are on R3's own koolivalmidus list). §6: "The Estonian kindergarten curriculum's seven areas + üldoskused **map cleanly** onto these domains, so the tree doubles as national-curriculum coverage evidence" — *muusika*, *kunst* (beyond Beauty pages/form drawing) and *liikumine* (beyond one tier-0 leaf) do not map at all, and *mina ja keskkond* maps only partially (nature yes; traffic/health/culture no).
- Why important and not cosmetic: these sentences are the *system's own stated anchors* — a family relying on the tree as "school-readiness evidence" (the framework's phrase) would walk into a koolivalmidus assessment with real holes.
- Fix: either add the I-1..I-5 nodes (after which both claims become true), or rewrite both claims to name the exclusions and where the family covers them (lasteaed does music/movement daily; the system covers the desk-shaped remainder). Honesty is the framework's house style everywhere else — extend it here.

**I-9. Parent-delivered English SSP assumes parent phonics competence; no audio ruling exists.**
- What: the entire English decoding strand (the system's flagship run-ahead) is delivered 1:1 by an Estonian parent, and a UK-style SSP lives or dies on *pure GPC pronunciation* (/m/ not "muh"; English short vowels that Estonian does not have). A parent who models /æ/ as Estonian *ä* for two years bakes in errors no school will later fix — school English starts at grade 3 and won't do phonics. The framework prices the parent's *minutes* meticulously (§5.6) and says nothing about the parent's *phonology*. B2 ("English sentences addressed to the parent to read aloud") quietly assumes competent parent English throughout. The dose-adequacy argument (§5.4) leans on 1:1 quality — "every minute lands at the child's exact frontier" — which is exactly the assumption at risk.
- Where: framework GP10/CR2 territory; booklet pipeline.
- Fix: one ruling: the SSP strand runs on a named program-with-audio or QR-linked per-GPC audio models in the booklets (printable-plus-audio is a solved problem); each phonics booklet carries a parent pronunciation micro-guide per new GPC set (a natural B21 extension); the quarterly §5.4 trajectory check listens for parent-transmitted GPC errors, not just coverage.

**I-10. Doctor path: "body vocabulary" is claimed in §2 and exists nowhere.**
- Classification: incoherence between learning-path §2 and the graph, plus a genuine content gap. §2's doctor profile names "living/non-living **and body vocabulary**" in the age-5–9 seed corpus. The graph delivers living/non-living (`sci-observe-senses`) and nothing else: no body-parts, senses-as-organs, bones/heart/lungs content anywhere in tiers 0–3, and framework §6's SCI content cycles ("plants/animals/materials/Earth/seasons") *omit the human body* even though R3's Estonian loodusõpetus list explicitly includes "human senses and body." A doctor-pulled child gets a teddy clinic quest with zero body knowledge under it.
- Fix: add "the human body" to the §6 SCI content-cycle list and to `sci-measure-record`'s content bursts (its description already names "plants, materials, habitats" — add body/senses), with a body-map Life page in the booklet line. No new node needed — this is a content-burst repair plus making §2's sentence true.

### 1.3 Nice-to-have

**N-1. Probability seed absent though the finance profile claims "probability intuition."** First chance content is `t5-advanced-math` (age 14+). Dice/spinner intuition games are nearly free at 7–9 and belong as a B13 Life costume inside `num-problems-data` or the sudoku-adjacent game culture. Make §2's finance sentence true the cheap way.

**N-2. Care for a living thing.** Estonian kindergarten's "care for nature," the classic empathy-and-responsibility seed (and doctor-flavored). Currently the closest thing is pressing dead leaves (`sci-measure-record`). A weeks-long plant/pet care log (single-shot chart, same mechanics as the savings jar) fits SCI tier 1–2 perfectly.

**N-3. Calendar and days of the week.** Koolivalmidus lists "days of the week and seasons"; seasons live in `sci-observe-senses`, clock in `num-measure-data` — days-of-week/months/yesterday-tomorrow orientation has no home. Fold a fourth sub-check into `num-measure-data` or the weather strip.

**N-4. Learning by heart.** "Knows some rhymes/poems by heart" is a koolivalmidus item and a live Estonian school practice (peast õppimine); the system trains retrieval science everywhere and verbatim memory nowhere. Cover via I-5's songs/poems, or one exercise line in `com-retell-story`.

**N-5. Strategy board games / chess.** Board-game night exists as an exercise line (`sel-emotions-turns`). GP14 ("same skill in many costumes") begs for checkers/chess/Ticket-to-Ride as an official LOG costume family at tiers 2–3 — planning, look-ahead and losing-gracefully in one box. A costume note, not a node.

**N-6. Representational art-making.** *Kunst* is a school subject; the system's visual arts are form drawing (pre-writing), Beauty pages (pattern), and craft (MOT). Drawing-as-depiction (draw a person, draw from observation beyond the SCI leaf) is thin. Acceptable as-is if the §6 mapping claim stops citing kunst as mapped (I-8); one CRE costume line would close it fully.

**N-7. Multi-child families.** The project is named "kids-learning"; the docs design for exactly one child. Several exercises conscript siblings ("timed by a sibling," "check a sibling can find the bed") while §5.5 bans sibling comparison — good — but nothing rules on: shared sessions, one poster per child, hand-me-down booklets (self-checking pages are consumables), or the second child entering via placement sweep. One §5.6 paragraph would do.

**N-8. Archetype-B evidence sources for peer-facing skills.** `sel-conflict-resolution` ("resolves *peer* conflicts") and parts of `sel-team-roles` require ≥3 unprompted instances — of behavior the parent mostly does not witness (it happens at lasteaed/school/huviring). The check spec should legitimize second-hand evidence (teacher's report, coach's word) explicitly, or parents will either stall the node or fake the tally.

**N-9. README is stale on three counts** (see §4, D-3).

**N-10. Doc hygiene pair** (see §4, D-4/D-5): the framework's phantom "Assessment rule (A)" citation class, and STATE.md's self-contradictory viewer row.

**N-11. Calming strategies.** Framework §6's SEL consensus chain begins "co-regulation → self-regulation → emotion vocabulary…" but the graph starts at vocabulary: no node teaches an actual calming toolkit (breathing, counting down, break-taking). Coping-with-failure lives in `sel-cooperation` ("not-yet bookmark") — good but thin. One sub-check in `sel-emotions-turns` ("uses a chosen calming move when upset, tallied") closes the prose-graph gap.

### 1.4 Checked and NOT gaps (credit where due)

- **Free play protection** — genuinely handled structurally: session caps are the *whole* system time (§3 binding), "everything outside the session is ordinary childhood," no streaks/loss-aversion (CR4), system yields to school in crunch weeks (§5.6). This is better protection than most commercial products ever write down.
- **Second/third language timing** — explicitly ruled (GP10, CR2, B21 contrast pages, decoding-onset curation order). Russian/German B-language legitimately post-dates the 5–9 scope.
- **Scissors/gluing/crafts fine-motor breadth** — adequately present (`mot-pencil-grip` scissors, form drawing everywhere, tööõpetus craft thread through `mot-handwriting-auto` and `t4-design-build`).
- **Waiting/boredom tolerance** — partially covered and honestly placed (`ef-attention-persist`, koolivalmidus "waits, persists 15–20 min" at Band 2, delayed-gratification charts).
- **Friendship skills** — the SEL chain covers the mechanics (turns → cooperation → conflict → roles); see N-8 for the evidence-source caveat. A dedicated "making and keeping a friend" node would be over-engineering; life covers it.
- **Tier-4/5 coarseness, lawyer/entrepreneur chokepoints, DIG absence from seven career closures** — all already named, owned, and scheduled for decomposition in the docs themselves. No action needed; this is what honest design debt looks like.

---

## 2. Age-band and family-week reality check

**Mostly survives contact — said plainly.** The band calibrations are right (10-min persistence at 5, box rule alone at S3, digits not before numeral formation, tables concept-before-drill, the tier-0 Mastered-not-Consolidated exception, the placement sweep, assumes-lines on quest cards instead of hidden edges). The v1.1–v1.4 loop fixes visibly did their job. Three real-world problems remain:

**R-1 (= B-2, blocking, detailed in §4).** The daily English read-aloud contradiction — the one place where the week as specified does not actually contain the work as specified.

**R-2 (= I-9, important).** Parent SSP delivery quality — the band-reality version: at Band 2 the template asks a working parent for 2 phonics-led sessions plus 2 number-led plus 2 booklet sessions *plus* the unpriced daily read-aloud plus school-prep life. The minutes fit on paper because the read-aloud is off the books.

**R-3 (nice-to-have).** Six sessions/week at Band 1–2 is the *design* number; a two-job family in a normal Estonian winter (illness waves, travel) will run 4. The framework's own fallback ("drop practice pages, never the strips") is the right minimum-viable-week rule — but it is buried in §5.6's prose. Promote it to a named rule so a tired parent can find it, and state explicitly that a 4-session week is a normal week, not a failure week.

Nothing in tiers 0–3 is developmentally misplaced in the classic sense; the two deliberate range-end placements (`num-numbers-100`, S2's 6–8 givens) are flagged in place, which is exactly how it should be done.

---

## 3. Career-path sense check (all nine)

- **Doctor** — Story mostly holds: SCI method spine, precision via MOT (verified in the hard closure via `t4-academic-writing → lit-composition → mot-handwriting-auto`), empathy honestly labeled enrichment + quest-carried (`quest-doctor` requires `sel-conflict-resolution`; `t5-life-sciences` bakes in volunteering). **But:** the claimed body-vocabulary seed does not exist (I-10), and no care-for-living-things experience exists (N-2). A doctor path whose only patient before 14 is a teddy and whose biology contains no body is a story with a hole in the middle.
- **Software engineer** — Coherent end to end; the sudoku/unplugged double on-ramp, the loop-3 `dig-block-projects` decay fix, and typing riding transcription are all defensible. No gaps found.
- **Manager** — Coherent: SEL chain → leading teams, COM chain → debate → org-leadership, money via `t4-money-management → t5-financial-analysis`. The plan-do-debrief culture is genuinely seeded at 6 (`ef-plan-check`). No gaps found.
- **Lawyer** — The argumentation story is the tree's best: because-reasons at 6, steel-listening at 7, family court at 8, debate → mock trial. Fairness reasoning is present (quest + conflict resolution). Single-vestibule chokepoint already owned in §1/§3 of the learning path. No gaps found.
- **Scientist** — Coherent; the loop-2 `quest-scientist → sci-fair-test` rewiring was the right call. No gaps found.
- **Engineer** — Coherent since `spa-scale-drawings` landed; the spatial spine now actually spans the 8–9 window the doctrine calls most trainable. No gaps found.
- **Entrepreneur** — Coherent; creativity chain runs unbroken, unit economics arrives via money nodes, flop-metabolizing is a real check (`cre-iterate-v2`). Single-vestibule chokepoint owned. No gaps found.
- **Finance** — Spine solid (the full numeracy chain is the path, correctly). **But** the §2 profile's "probability intuition" differentiator has no seed before age 14 (N-1) — either seed it or stop claiming it.
- **YouTuber** — The production/venture story is coherent and the parent-gated publishing stance is the most responsible treatment of this career I have seen anywhere. **But** the viewer-side media literacy the DIG scope line promises does not exist as content (I-7), and a "content creator" path in a tree with zero music/performance craft (I-4) will feel thin the day the child wants to make anything with sound in it.

**Cross-career note:** the trunk-union display mechanism (closure ∪ `common_trunk`) is the right answer to the "Lawyer needs no math" lie, and the docs' refusal to fake edge-level breadth is admirable. The career layer's real weaknesses are the three claimed-but-unseeded competencies above (body, probability, media judgment) — all cheap fixes.

---

## 4. Interruption damage and incoherence

**D-1. BLOCKING — The shipped flagship booklet contradicts the doctrine, and learning-path §7 claims the opposite.**
- learning-path §7: "First consumers: the picture-sudoku booklet line hangs off `log-sudoku-4x4 → …` **exactly as specified in framework §4.4** (entry booklets 1a/1b covering S1–S2 per the B7 split…)."
- Reality on disk (README + `scripts/generate_sudoku.py`): one booklet, "Animal Sudoku (ages 5–8)," sections **A 3×3 pictures → B 3×3 numbers → C 4×4 pictures + box rule → D 4×4 numbers**.
- Violations of the converged spec: 3×3 Latin squares appear nowhere in the S-ladder (S1 is 2×2 + rows-only strips with tiles); **digits at the age-5 entry** violate B9/B3's motor ramp (place tiles → draw → write; digits arrive at S4, ages 7–8); pictures→numbers→box-rule→numbers is **three new mechanics in one booklet** against B7's one; there is no 1a/1b split, no tile sheet, no stated recognition battery; "ages 5–8" spans three grid modules against B3.
- To be fair: the booklet predates the converged framework (STATE.md sequence). But no document *says* so — instead §7 asserts conformity. A family holding the doctrine in one hand and booklet 1 in the other sees the system contradict itself on day 1, on its flagship.
- Fix: either regenerate booklet 1 as the 1a/1b pair per §4.4 (the generator script is 90% there — it already enforces unique solutions), or stamp the existing booklet, in README and §7, as a **legacy prototype superseded by the 1a/1b spec**. One of the two, before the next print run.

**D-2. BLOCKING — The daily read-aloud is simultaneously mandatory and forbidden.**
- Framework §3 (binding): "**'Daily' prescriptions do not exist outside the ~2-minute strips (non-session days carry no system work, by rule).**" and "Everything outside the session is ordinary childhood: free play, read-alouds, life."
- The graph: `lit-en-oral-vocab` — "**Daily** English read-aloud with point-to-the-picture checks" (exercise line); `lit-en-oral-2` — "daily read-alouds… Two story questions… **after each English read-aloud**"; `lit-en-oral-3` — "**Chapter-a-night** English read-aloud."
- These are trunk nodes with mastery checks, on the strand the framework calls the one school won't supply; §5.4's dose-adequacy argument for the by-9 endpoint explicitly leans on "(c) the oral-comprehension leg runs from 5." So: either the read-aloud is system work — then it violates the subordination rule and is missing from every §5.6 parent-minutes row — or it is "ordinary childhood" — then the trunk's oral leg has **no scheduled delivery vehicle at all** and the endpoint argument rests on unpriced, unprotected goodwill. The likeliest real-world outcome is the worst one: it silently stops happening in busy months and nobody notices until the `lit-en-oral-3` check fails.
- Fix (one ruling): name the **daily 10-minute family read-aloud** (Estonian and English alternating or stacked, family's choice) as the single sanctioned daily item *outside* the session system — priced in §5.6 (~70 min/week parent time, honestly), named in the §3 template as the read-aloud rail the oral-leg nodes ride, and exempted *by name* from the no-daily-prescriptions rule. This also gives the Estonian read-aloud (I-6) its home.

**D-3. Nice-to-have — README stale on three counts** (classic interruption residue): (a) scope line still says "**last** year of kindergarten and the first 3 school years" — the pre-CR14 anchoring; the learning path's own tier table says tier 0 = lasteaed *middle* year and tiers 2–3 = school years 1–2 with the grade-3 checkpoint at the 3/4 boundary; (b) "critique logs from the **3** review/improvement loops" — five loops are on disk; (c) the folder tree omits `curriculum/learning-path.json`, `curriculum/skill-tree.html`, `scripts/extract_learning_path.py`, `scripts/build_skill_tree.py`, all of which exist and two of which STATE.md names as pipeline steps.

**D-4. Nice-to-have — Phantom citation class.** Framework §0 traceability: downstream work "must cite either a Guiding Principle (GP), a Conflict ruling (CR), a Booklet rule (B), **or an Assessment rule (A)** from this document" — the document contains no A-numbered rules (§5 is prose-structured; the A1–A6 citations that do appear are R4's *report parts*, a colliding namespace). Either number §5's rulings (A1 = state machine, A2 = archetypes, …) or drop the clause.

**D-5. Nice-to-have — STATE.md contradicts itself** about the skill-tree viewer: one row says "PUBLISHED — … (**needs republish after v1.5**)", the next says v1.5 "viewer **rebuilt & republished**." One of the two is stale; a resuming session cannot tell which.

**D-6. Verified clean (so future reviewers need not re-check):** no truncated sentences or mid-thought breaks found in either main document; all internal § cross-references resolve; both v1.5 status paragraphs tell the same revision story; censuses consistent (100 nodes / 130 edges / 24 keystones / 9 quests, matching my hand counts per tier); `common_trunk`'s 26 ids all exist and the set is ancestor-closed on spot-check; the absence of loop 5 from the status lines is benign (loop 5 changed nothing; STATE.md documents it). The minor JSON ordering oddity (`dig-beebot-arrows`, a tier-0 node, sits among tier-1 entries) is cosmetic. The weather-record duplication between `sci-observe-senses` (c) and `sci-cause-effect` is a defensible spiral, not damage.

---

## Top-5 priority recommendations

1. **Resolve the booklet-vs-doctrine contradiction (D-1).** Regenerate booklet 1 as the 1a/1b entry pair per framework §4.4 — or explicitly mark the shipped Animal Sudoku as a superseded prototype in README and learning-path §7. The flagship artifact and the doctrine must stop disagreeing.
2. **Rule the daily read-aloud into existence (D-2 + I-6).** One framework ruling: a named, priced, daily 10-minute family read-aloud rail (Estonian and English) that the `lit-en-oral-*` nodes officially ride; amend §3, §5.6 and the three node cards. Add the `lit-reads-for-fun` dispositional node so Estonian reading appetite is seen, not just Estonian decoding.
3. **Add the life stratum (I-1, I-2, I-3).** Three small Archetype-B clusters, none gating anything: `sel-selfcare` (tier 0), `sel-safe-well` (tier 0–1, traffic/reflector/water/stranger + health rhythms), `mot-gross-2` (tier 1–2, water confidence for the statutory school swim course, bike, seasonal skills). This is ~3 nodes and makes the koolivalmidus claim true.
4. **Answer the music question and fix the two overclaims (I-4, I-8).** Either one tier-0 rhythm-and-song node (which also carries I-5's Estonian repertoire and N-4's poems-by-heart) or an explicit scope ruling — and in both cases rewrite §5.4's "demonstrably meet" and §6's "map cleanly" to say exactly what is and is not covered.
5. **Make the career claims true where they are currently prose-only (I-7, I-9, I-10, N-1).** Add `dig-media-sense` (viewer-side judgment the YouTuber wonder owes), the SSP audio/pronunciation ruling (the English endpoint's real delivery risk), the human body in the SCI content cycles (the doctor's claimed seed), and a probability Life-costume at tier 3 (the finance profile's claimed intuition).

*Filed 2026-09-04. — Gap review 1, practitioner pass.*
