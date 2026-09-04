# Gap Review 2 — Systems-Level Coverage & Design Blind Spots

**Reviewer role:** external curriculum designer / educational psychologist; whole-system coverage review.
**Scope:** `curriculum/learning-path.md` v1.5 + `docs/methodology/combined-framework.md` v1.5, audited against the project's own evidence base (`docs/research/01–04`). Deliberately NOT re-verified: internal arithmetic, censuses, edge counts (loops 1–5 own that; spot-checks below confirm they still hold in v1.5).
**Date:** 2026-09-04

---

## Overall verdict

This is an unusually disciplined piece of curriculum engineering — the ruling discipline (GP/CR/B/A citations, named carve-outs, priced parent load) is better than most ministry submissions I review — but its five review loops have optimized *internal consistency* while leaving *coverage* and *deployment* claims under-audited: the tree quietly narrows "education 5–9" to the six domains report 03 happened to build matrices for, then claims national-curriculum coverage it does not have (music, art, PE/swimming, health, and the human body are absent — the last of which the doctor career's own §2 prose claims to seed); several careers name adult competencies (probability, persuasion, media consumption judgment, CAD) whose childhood roots exist nowhere in the graph; and the system's two largest real-world dependencies — an untrained parent delivering synthetic phonics 1:1, and a four-year cadence that survives travel, atypical development, and the documented age-8–10 motivation dip — are argued past rather than designed for. Nothing here breaks the graph; most fixes are one ruling, one cluster node, or one honest sentence. But two findings are blocking as claims currently stand, and the pattern behind them — "the framework inherits report 03's scope silently and then overstates what the tree covers" — deserves a named ruling so it stops recurring.

---

## 1. Domain coverage gaps vs. the standards the project itself researched

The tree's 10 domains cover exactly the six matrices of report 03 (§3.1–3.6) plus R4's LOG/COM/CRE/SPA split. Report 03's *country profiles* (§2), however, document subjects the matrices never tabulated — and the framework makes two coverage claims against them: §6 "The Estonian kindergarten curriculum's seven areas + üldoskused map cleanly onto these domains, so the tree doubles as national-curriculum coverage evidence" and §5.4 "the tree's tier-0/1 coverage should demonstrably meet [koolivalmidus]." Neither claim survives the audit. No framework ruling anywhere scopes these subjects out (verified by search: *muusika/kunst/liikumine/kehaline/swim/inimeseõpetus* appear in neither governing document except SEL's template citation).

### D1 — Music: genuine hole (no node, no prose, no scope ruling) — IMPORTANT
- **Evidence:** Estonian lasteaed curriculum names *muusika* as one of its seven areas and I kooliaste carries it as a subject grades 1–3 (R3 §2.1); England's EYFS "expressive arts & design" is one of the seven assessed areas (R3 §2.3); Singapore NEL's "aesthetics & creative expression" likewise (R3 §2.5). Zero nodes, zero prose, zero ruling. The gap is also pedagogical, not just curricular: the project's own R1 evidence uses music as a *channel* (rhythmic counting, times tables through movement and clapping, circle songs — R1 §3.1–3.2), and none of that made it into even the exercise lines of the numeracy training grounds.
- **Verdict class:** missing from the graph AND from prose; not scoped out.
- **Fix:** Either (a) a framework scope ruling (see D-fix below) naming music school/lasteaed-delivered and out of tree scope, plus correction of the §6 "maps cleanly" sentence; or (b) one school/life-evidenced observation node per era on the `lit-reading-fluency` pattern (e.g. tier-0 `cre-music-play`: keeps a beat, sings back a phrase — Archetype B tally, never a hard gate). Minimum: fix the two overreaching claims.

### D2 — PE / gross motor after tier 0, and swimming: genuine hole — IMPORTANT
- **Evidence:** `mot-gross-body` (tier 0) is the *only* gross-motor node in the system; the branch's own §6 scope line promises "gross motor, fine motor, and spatial." R3 §3.5 expects bike riding and consolidating ball skills at 6, running/jumping/throwing technique at 7, complex playground skills at 8, sport-specific skills at 9 — and R3 §2.1 names Estonia's **compulsory beginner swimming course within I kooliaste (target ~200 m)** under *kehaline kasvatus*, a statutory subject the tree never mentions.
- **Verdict class:** missing from graph; prose covers only the tier-0 koolivalmidus half; not scoped out.
- **Fix:** Scope ruling (school delivers PE and swimming; tree tracks nothing above tier 0) + correct the §6 MOT-SPA scope line to say "gross motor *at school-readiness level only*". Optionally one tier-2 school-evidenced observation cluster ("moves like a schoolkid": bike, swim progress, ball game) so the poster's MOT column doesn't silently become a desk-skills column after age 6 — which it currently does.

### D3 — *Mina ja keskkond* / health / safety / civics: hole plus an overreaching anchor claim — IMPORTANT
- **Evidence:** The koolivalmidus profile the framework claims to "demonstrably meet" (§5.4) includes *mina ja keskkond* outcomes: home/family/professions, Estonia and its symbols, **traffic safety as a pedestrian**, care for nature, **basics of healthy behaviour**, plus days of the week (R3 §2.1). Grades 1–3 continue this as *inimeseõpetus* (emotions ✓ covered, but also **health, safety, daily rhythm/time use** — not covered) — a subject the framework itself holds up as "the explicit subject template" for SEL (§6). The tree covers the social-emotional and nature-observation slices only; professions are charmingly half-covered by the careers-as-wonders layer, but health, safety, Estonia/community content is absent.
- **Verdict class:** partly prose-only (SEL slice), partly missing; not scoped out; §5.4's claim is false as written.
- **Fix:** Narrow §5.4 to the criteria the tree actually covers (language, math, motor, social) and name lasteaed as the source for the rest; or add a small tier-0/1 "my world" cluster (Archetype B, life-evidenced: traffic rules, healthy habits, days of the week). The health slice should merge with D4's fix.

### D4 — The human body & health: consensus milestone missing, and the doctor career's own seed corpus is undelivered — **BLOCKING**
- **Evidence:** R3 §3.3's **consensus** row at age 6 is "body parts & senses"; Estonian *loodusõpetus* grades 1–3 explicitly includes "human senses and body" (R3 §2.1); *inimeseõpetus* includes health; koolivalmidus includes healthy behaviour. R4 B3's doctor row names "body-parts & living/non-living vocab" as an age 5–9 booklet-able precursor. Learning-path §2 (doctor) claims the seed corpus includes "living/non-living **and body vocabulary**" — but no node anywhere teaches body vocabulary: `sci-observe-senses` does leaves/living-nonliving/weather; `sci-measure-record`'s content bursts are "plants, materials, habitats"; the first human-body content in the entire system is `t5-life-sciences` at 14–18. The teddy-clinic quest *exercises* body knowledge its prerequisite chain never *builds*.
- **Verdict class:** missing from graph; claimed in prose (§2) — a claim-vs-graph contradiction of exactly the class earlier loops treated as critical.
- **Fix:** Cheapest honest fix: extend `sci-measure-record`'s content-burst list to "plants, materials, habitats, **the human body and senses**" and add a named sub-check (it is already a content-burst node); or add a tier-2 `sci-body-health` cluster (body parts/senses vocabulary; healthy-habits talk; simple first-aid steps — the last doubling as D3's safety slice), prereq `sci-observe-senses`, feeding `quest-doctor` (swap for its `sci-measure-record` prereq or leave as advisory). Also satisfies inimeseõpetus/koolivalmidus health coverage.

### D5 — Visual art techniques: prose-partial, and the aesthetic strand dead-ends — NICE-TO-HAVE
- **Evidence:** *Kunst* is a named Estonian area (K and grades 1–3, R3 §2.1); EYFS expressive arts. The tree has fragments — Beauty pages (B13), form drawing (MOT warm-ups), draw-what-you-see (SCI) — but no drawing/making progression, and CRE's chain (idea-fluency → puzzle-maker → iterate → invent) runs the *inventive* strand only: the Beauty/aesthetic strand has no node above tier 0–1 and no consumer anywhere. See also P8.
- **Fix:** Scope ruling (school delivers kunst) + fold an explicit observational-drawing rung into existing nodes' exercise lines; or accept and document as wild-node territory (CR6) — but then say so.

### D6 — Measurement-unit breadth vs the grade-3 list — NICE-TO-HAVE
- **Evidence:** The grade-3 checkpoint list the tree carries as target content includes units "cm/m/km, g/kg, s/min/h, €" (R3 §2.1). The graph delivers length-cm (`num-measure-data`), time (`num-money-time`), € — but mass, volume and km appear in no node's can-do or exercises (thermometer lives in SCI).
- **Fix:** One line: extend `num-measure-data`'s sub-check (a) or `num-problems-data`'s exercises to include g/kg and km estimation. No new node needed.

---

## 2. Career-back competency gaps

Method: each career's adult profile (learning-path §2, R4 B3) checked against the hard closure ∪ trunk, then the tier-4/5 bundles checked for un-staged middles.

### C1 — Doctor: no biology-of-the-body root (see D4 — BLOCKING); care-exposure smuggled into a bundle — IMPORTANT
- Beyond D4: the §2 profile calls the empathy/SEL pairing "decisive," §4 honestly labels the SEL chain enrichment (quest door + trunk), but `t5-life-sciences` then carries "sustained people-facing service... the SEL leg of medicine" **in its exercise list** with zero SEL ancestry (`t4-science-method` is its only prereq). That is a competency riding a bundle's flavor text — the exact pattern §3 refuses for `t5-financial-analysis`'s spreadsheet gap, where the card at least admits it.
- **Fix:** When tiers 4–5 decompose, give the doctor vestibule a real SEL/service leg (e.g. `t4-leading-teams`-class people-facing milestone or a named service node); until then, add the same "known coarse-layer gap" admission sentence `t5-financial-analysis` carries.

### C2 — Probability & reasoning under uncertainty: no childhood root for finance/scientist/manager — IMPORTANT
- **Evidence:** Learning-path §2 finance names "probability intuition" in the profile; R4 B3's finance row lists "**probability intuition (dice/spinner games)**" as an age 5–9, explicitly *booklet-able* precursor; the manager profile is "decides with incomplete information." First appearance in the graph: `t5-advanced-math` ("Probability lab") at **14–18**. Verified by search: no node below tier 5 mentions chance, dice-as-probability, or likelihood. (Not a national-curriculum gap — none of the five systems demands probability by 9 — so this is purely a career-back hole against the project's own R4.)
- **Fix:** Cheap and native: a tier-3 `num-chance` micro-node (or a fourth sub-check on `num-problems-data`): plays and reasons about spinner/dice games — "which is more likely, can it be certain?" — feeding `t4-algebra-data`. The games-with-rules asset (GP16) already supplies the format.

### C3 — Media literacy as *consumption*: prose-thread only, for a system with a content-creator career — IMPORTANT
- **Evidence:** R3 §3.6 consensus rows: age 8 "searching with judgment ('is this source for kids?')", age 9 "**understands the internet has authors & intentions (early media literacy)**" — a majority-consensus milestone in-band. In the tree, e-safety is a rider clause on DIG exercise lines (`dig-scratchjr`, `dig-scratch`, `t4-media-production`) and never a named check anywhere; *critical consumption* (who made this, what do they want, is it true) appears nowhere at all. For the YouTuber career this is not decoration — audience judgment as a consumer precedes creator judgment, and `t5-creator-business` claims "audience analytics read honestly" with no data-literacy ancestry beyond the trunk's arithmetic (`num-problems-data`'s charts are *not* in the trunk).
- **Fix:** Promote the e-safety thread to one named sub-check at `dig-scratch` or a tier-3 DIG micro-node ("Who made this?": identifies author and purpose of three media pieces; kind/unkind message sort) — the R3 sequence already gives the ladder. Note the analytics gap on the `t5-creator-business` card the way `t5-financial-analysis` does.

### C4 — `t4-english-fluent`: the steepest un-staged middle in the system, carrying the flagship strand — IMPORTANT
- **Evidence:** The node bridges from `lit-en-reading` ("short English texts... decodable-plus readers"; chapter books explicitly deferred) to "reads novels and non-fiction, writes and presents comfortably" in a single bundle. Between them lie 3–4 years of graded-reader progression, English composition stages, and — nowhere else in the tree — **productive spoken English**: every oral node to tier 3 is receptive ("answers in either language" is the ruled register), yet this node's exercise is "deliver a school presentation in English." The trunk's whole by-9 argument (§5.4) hands over to this bundle. Six of nine careers depend on it via hard edges or trunk display.
- **Fix:** Decompose this bundle *first* when tiers 4–5 decompose (before `t4-programming` or anything else): staged reading levels, an English-speaking rung (retell/present in English, low-stakes), and English composition — each with sub-level ticks (see P1).

### C5 — Engineer: CAD/digital promised with zero DIG ancestry, and *unadmitted* — IMPORTANT
- **Evidence:** `t5-applied-engineering` names "CAD, robotics" and its exercises "CAD-design and fabricate a working part," with prereqs `t4-design-build` + `t5-advanced-math` — no DIG node in the closure. Learning-path §3 admits exactly this structural class of gap ("seven of nine careers reach 18 with zero DIG nodes in their closure") but names **only** `t5-financial-analysis` and puts the admission only on that card. Same defect, inconsistent honesty.
- **Fix:** Extend the §3 sentence and add the admission line to the `t5-applied-engineering` card; route a digital-tools node into the design-build chain at decomposition (it can be the same spreadsheet/data-tools node finance is promised, or a CAD-lite rung off `t4-design-build`).

### C6 — Entrepreneur: persuasion is enrichment-only while the capstone demands a pitch — IMPORTANT
- **Evidence:** §2 names "persuading" in the profile; `t5-venture`'s exercises: "a final pitch." But §4 rules `com-present` *enrichment* for entrepreneur ("soft-highlighted, not in the hard closure"), and the trunk's COM chain stops at `com-because-reasons` — so the hard path to a student company contains no structured-speaking node at all. Negotiation (offer/counter-offer/compromise), named nowhere, is the other classic entrepreneurial competency with no root; `sel-conflict-resolution` is the nearest cousin and is also outside this closure.
- **Fix:** At tier-4/5 decomposition give `t4-venture-lab` or `t5-venture` a COM leg (fan-in space exists at `t5-venture` only via swap; otherwise the card-admission pattern applies). A negotiation flavor ("trade-and-swap games") fits naturally as an exercise line on `sel-conflict-resolution` or `quest-entrepreneur` today.

### C7 — `t4-money-management` claims "interest" with no percent in its ancestry — NICE-TO-HAVE
- Prereqs are `num-money-time` + `ef-goal-setting`; percent/ratio live in `t4-algebra-data`, which is not an ancestor. `t5-financial-analysis` recovers it via `t5-advanced-math`, but this card's own claim ("understands saving, **interest**") outruns its chain. Fix: soften the card ("simple interest, felt through the savings chart") or add the prereq at decomposition.

### C8 — Lawyer: cleanest wiring of the nine; only note that "civics and legal reasoning" (`t5-argument-law`) has no earlier rules-of-community root (ties D3) — NICE-TO-HAVE.

**Checked and found sound:** software engineer (complete chain, English and math legs both present); scientist (stats via `num-problems-data → t4-algebra-data`; writing leg present); manager (closure genuinely contains the COM chain via `t5-org-leadership ← t4-debate` — verified); youtuber's production and venture legs (both real, honest edge chains); `quest-scientist`'s tier-3 prereq (deliberate, documented); the fan-in-3 carve-out at `t5-research-project`.

---

## 3. Psychological & systemic blind spots

### P1 — Tier-4 is a motivational vacuum exactly where the project's own evidence predicts fragility — IMPORTANT
- **Evidence:** GP13's anti-stall doctrine demands poster motion "at least monthly," delivered in tiers 0–3 via sub-level ticks and staged nodes. Tier-4 bundles are **multi-year** nodes (`t4-algebra-data` spans negative numbers through statistics; `t4-english-fluent` spans ~3 years of reading growth) with *no tick mechanism* — the extended-fluency ruling (§5.2) is scoped to training grounds. R2 §9.4: ability self-assessment turns accurate and motivation turns fragile at ~8–10 — i.e., precisely at the tier-3/4 boundary. The decomposition promise ("when the family actually approaches them") has no owner, no trigger, and no date; a fast child arrives at 9.5 with the booklet pipeline (Bands 1–4) behind them and sealed-scroll bundles ahead.
- **Fix:** Rule a decomposition *trigger* (e.g., "when the child's frontier first enters tier 4 in any branch, that branch's bundles are decomposed within one quarter") and give every tier-4 bundle interim sub-level ticks now (three lines each). Decompose `t4-english-fluent` first (C4).

### P2 — Atypical development: no screening, no referral, and a dose-shaped-only lag lever — IMPORTANT
- **Evidence:** The framework's individual-differences machinery is pace-only (mastery-not-age, placement sweep, correctives one rung down). Nothing addresses dyslexia, ADHD, or DLD: §5.4's monitoring loop has exactly one lever when the child falls behind — *add a third phonics session* — which is the wrong-shaped response to a specific learning difficulty, and the bilingual setting actively masks early signals (Estonian's transparent orthography lets a dyslexic child decode passably while English exposes them — R2 §10.2's asymmetry cuts both ways). The evidence reports themselves never covered atypical development; the framework inherited that silence without flagging it.
- **Fix:** One paragraph in §5.4: named referral triggers (e.g., phonemic-awareness sub-skills not consolidating by ~6.5 despite dose; persistent b/d-class reversals plus family history; tally-based attention criteria unreachable across two quarters) → professional assessment, and a ruling that decay-dimming is softened for a child with a documented difficulty (the dimming poster is a demoralization engine for exactly the ADHD profile).

### P3 — The parent-as-tutor premise: the dose-adequacy argument borrows trained-tutor effect sizes for an untrained parent — **BLOCKING** (as the claim stands)
- **Evidence:** §5.4's by-9 endpoint argument leans on "1:1 dosing — every minute lands at the child's exact frontier... tutoring effects dwarf whole-class effects minute-for-minute." The tutoring literature the project itself cites (Nickow, Oreopoulos & Quan 2020, in R2 §8: ~0.35 SD "for real tutoring programs") is dominated by *trained* tutors and paraprofessionals with protocols; parent-delivered tutoring is that meta-analysis's weakest arm. Synthetic phonics delivery is a genuine skill (pure phonemes, no added schwa, blending technique, decodable-text routines) and **no deliverable in the system teaches it** — B17 scripts hint-lines for booklet pages, not SSP delivery. The framework prices parent *time* (§5.6) meticulously and parent *skill* not at all. This is the single most load-bearing unexamined assumption in the system, because trunk composition, CR14's run-ahead, and the B18 cadence all sit on the by-9 claim.
- **Fix:** (a) Add a parent-delivery mini-guide to the deliverables list (10 pages: phoneme purity, blending routine, what a session looks like, common errors — the SSP schemes the project cites all publish such guides); (b) recondition the §5.4 argument: "1:1 dosing *with the delivery guide followed*"; (c) add delivery-quality to the quarterly monitor (one line: parent self-checks against the guide when lag appears, *before* adding dose).

### P4 — No interruption/re-entry protocol, for a family whose documented reality is interruption — IMPORTANT
- **Evidence:** The spacing labels (B18), decay timers, weekly template, and consolidation-retest queue all assume continuous weeks; the only yield rule is "system yields to school homework in a crunch week" (§5.6). A 2–4-week travel gap at Band 2 breaks the phonics cadence, expires strip obligations, and queues a demoralizing backlog — and the project's own STATE.md lists "user travels; interruptions expected" as a standing constraint. CR4 even bans streak mechanics *because* "a family trip must never feel like losing" — the value is stated, the mechanism is missing.
- **Fix:** One ruled protocol in §5.6: after any gap ≥2 weeks — first week back is strips-plus-booklet only (no dose, no checks), every Practicing training-ground re-enters one rung down, retest queue resets rather than accumulates, and the poster never dims *during* a declared family pause (suspend decay timers on declared breaks).

### P5 — The lag lever cannibalizes the eight-domain breadth budget, un-priced — IMPORTANT
- **Evidence:** §5.4's third phonics session is "swapped in for a booklet/free-choice slot." §3 is explicit that the two booklet/free-choice sessions **are** the delivery vehicle for the eight non-training-ground domains ("they *are* the booklet/free-choice sessions"). A child more than one phase behind therefore runs SCI, LOG, SEL-projects, DIG, MOT-SPA, CRE, COM through **one** weekly session for as long as the lag lasts — the framework prices everything else and never prices this.
- **Fix:** Cap the swap (e.g., at most one quarter consecutively, then the lever becomes "review delivery quality / consider P2 referral" rather than more dose), and say which domains' cadence-riding strands survive the squeeze.

### P6 — Observation-tally validity: the parent is a motivated rater with no guard-rails — IMPORTANT
- **Evidence:** Archetype B ("≥3 unprompted instances across ≥2 weeks") certifies SEL/EF trunk nodes that sit on every career highlight. The rater is a parent who wants the poster to advance, "unprompted" is nowhere operationalized per node, and there is no second-observer, no written-instance requirement, no exemplar bank. R4 A5's own model (scouting) uses a *non-parent* counselor precisely to separate affection from verification; the framework cites the model and drops the separation. Five loops audited the tallies' arithmetic; none audited their validity.
- **Fix:** Cheap rigor: each Archetype-B instance must be a one-line *described* observation in the evidence log (what happened, when — description resists inflation better than a tick); keystone-level B nodes get a second adult's countersign or an outside-context instance (kindergarten teacher comment, playground with non-family). Two sentences in §5.2.

### P7 — Check administration and language-of-check validity — IMPORTANT
- **Evidence:** Archetype-A checks ask the parent to make live psychometric strategy classifications ("listens for retrieval or a fast derived fact, not finger-counting") with no administration protocol: nothing rules hint-drift during checks, same-day retry, or reacting to the first error. And from Band 4 the materials assume "short independent English instructions" — so every non-language check from ~8 silently conflates the target skill with English proficiency; a math check failed for vocabulary reasons is a validity failure the documents never name (B2 solves this at 5–7 via icons, then the protection lapses).
- **Fix:** (a) A half-page check-administration script in §5.2 (neutral face, no mid-check teaching, stop-and-return rule after 2 misses); (b) one ruling: *any check outside LIT-EN may be administered in either language, instructions read aloud on request, at every age* — cost: one sentence.

### P8 — The wonder set is a professional-class monoculture and the aesthetic strand has no ladder — NICE-TO-HAVE (but watch it)
- **Evidence:** All nine careers are academic/commercial (doctor…youtuber); no artist, musician, athlete, chef, teacher, or tradesperson — while the tree simultaneously has no music (D1), no art progression (D5), and no PE above tier 0 (D2), so a child pulled toward any aesthetic or athletic identity finds neither a wonder nor a branch. The ruled valves (design-your-own tenth slot, wild nodes at ~10–15%, CR6/CR12) are real but live entirely in the unbuilt poster spec. Career-interest churn is the project's own cited premise (CR12); the current set teaches "worthy futures cluster here."
- **Fix:** When the poster spec is authored, make the tenth slot *first-class* (same card stock, same quest scaffold template) and pre-author one worked example of a wild-node chain (e.g., a music or football chain) so the valve demonstrably works. No graph change needed.

### P9 — Autonomy narrows with age, against the SDT gradient — NICE-TO-HAVE
- Band 1: 6/6 sessions child-chosen; Band 4: 2/5 (three are prescribed doses) — bounded choice shrinks exactly as R2 §9.4 says motivation becomes fragile. Mitigation is cheap: rule that *within* dose sessions the child picks order/format among equivalent materials (B11's buffet logic, extended upward), and say so in §3.

### Transfer assumptions — checked, substantially sound (no severity)
GP14 (≥2–3 costumes), the sudoku cluster's soft-feed-only role, and the §4 enrichment labels are honest about non-transfer — this is better than most published curricula. Two residues, noted not graded: (a) the EF trunk's presence on every career highlight is a domain-generality *display* claim the project's own R2 §3.3 (near-transfer only) would not certify — acceptable as poster lore, but the poster spec should not let it become a prose claim; (b) `t4-english-fluent`'s cross-language writing-transfer premise is fine for structure and false for spelling, which the node itself concedes — the risk is only that decomposition (C4) forgets the concession.

---

## 4. Interruption damage (truncations, contradictions, dangling references)

The v1.5 cross-document state is in better shape than a many-session build usually leaves: JSON block, node counts (100/130/24 keystones/9 quests/26 trunk), trunk ancestor-closure, bridge list, quest-prereq tiering, and the §7 census all re-verify. Found anyway:

### I1 — "The four checkpoint nodes say so on their own cards" — only three do — NICE-TO-HAVE
- Learning-path §3 (tier-3 walkthrough) claims four node cards carry the CR14 no-deadline checkpoint note. Cards carrying it: `num-multidigit`, `num-fractions`, `num-problems-data` — three. The natural fourth (`num-times-tables`, whose korrutustabel *is* grade-3 checkpoint content) says "boss milestone" but carries no checkpoint/no-deadline sentence. Either add the sentence to that card or change "four" to "three."

### I2 — STATE.md self-contradicts and is stale against v1.5 — NICE-TO-HAVE
- The viewer row says "needs republish after v1.5" while the youtuber row says "viewer rebuilt & republished"; the learning-path row still reads "97-node graph ✅ v1.4" and the framework row "✅ v1.4" although both files are v1.5/100 nodes. Not a curriculum defect, but this is the file the project's own memory says to read first when resuming — it currently misleads the resumer.

### I3 — Framework §6 note (a): "the v1.5 graph carries exactly two [EF cross-branch out-edges] in tiers 0–3" — true only under an unstated gloss — NICE-TO-HAVE
- `ef-plan-check → quest-scientist` and `ef-multistep-projects → quest-manager` are also cross-branch EF out-edges inside tiers 0–3; they are excluded as quest fan-in under carve-out (c), but the sentence as written counts edges, not class-(a) members, and is false without the gloss. Add "(quest fan-in excluded under (c))" to the sentence.

### I4 — Framework changelog: "no ruling or principle changed" in v1.5, but GP12's text was materially extended — COSMETIC
- GP12 gained the "R4 B2 mapped the original eight; the ninth... draws on the same shared trunk" clause. The *ruling* indeed stands; the sentence would be safer as "no ruling changed; GP12's text extended to cover the ninth career."

### I5 — Verified clean (reported so the next reviewer need not re-check)
- `learning-path.json` is content-synced with the md block (100 nodes, 130 edges, 24 keystones, 9 careers, 26-id trunk — machine-checked this review). README already says "9 career end-goals." Keystone census recomputes (2 bosses + 9 quests + 13 leg-caps). The doctor-spine enrichment labeling, `quest-scientist` singleton clause, and the trunk's ancestor closure all hold.

---

## Top-5 priority recommendations

1. **Add the human body & health strand (D4/C1/D3).** Extend `sci-measure-record`'s content bursts (or add a tier-2 `sci-body-health` cluster: body parts & senses vocabulary, healthy habits, simple safety) feeding `quest-doctor`. It closes a five-system consensus milestone, an Estonian statutory subject slice, the koolivalmidus health criterion, and the doctor career's own undelivered §2 claim — one node.
2. **Write the missing scope ruling and retract the two overreaching coverage claims (D1/D2/D3/D5).** A new CR (or §6 structural note): music, art, PE/swimming, and *mina ja keskkond* civics are school/lasteaed-delivered and out of tree scope (optionally trackable as school-evidenced observation nodes on the `lit-reading-fluency` pattern); then correct §6's "maps cleanly / coverage evidence" sentence and §5.4's koolivalmidus claim to match what the tree actually covers.
3. **Repair the parent-capability premise under the English-by-9 claim (P3, with P2 and P5 riding along).** Add a parent SSP-delivery mini-guide to the deliverables; recondition §5.4's dose-adequacy argument on it; give the quarterly monitor a delivery-quality check, a capped dose lever, and named refer-out triggers for suspected dyslexia/ADHD.
4. **Plant the two missing career-back roots the project's own research calls booklet-able (C2/C3).** A tier-3 chance/probability micro-node (dice/spinner reasoning → `t4-algebra-data`) and a named media-consumption-judgment check on the DIG e-safety thread ("who made this and why") — each one node or one sub-check, each closing a gap for three-plus careers.
5. **Rule the two continuity mechanisms the four-year horizon depends on (P1/P4/C4).** (a) An interruption/re-entry protocol (≥2-week gap → strips-only week, one rung down, suspended decay on declared pauses); (b) a tier-4 decomposition trigger with interim sub-level ticks on every bundle — `t4-english-fluent` decomposed first, including a productive-spoken-English rung — so the poster keeps moving through ages 10–13, where the project's own evidence says motivation is most fragile.

**Tally: 2 blocking · 14 important · 10 nice-to-have (+1 cosmetic).**
