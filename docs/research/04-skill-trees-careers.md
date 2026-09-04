# Research Report 04 — Skill-Tree Design & Career-Back Competency Mapping (Ages 5–9)

**Purpose:** Inform the design of a Civilization-style skill tree spanning the last kindergarten year through grade 3 (~ages 5–9), terminating in 8 visible "career capstone" nodes, plus the mastery mechanics behind printable exercise booklets (first: picture sudoku).

**Audience context:** English-language system, Estonian family. Estonia's national kindergarten curriculum (*koolieelse lasteasutuse riiklik õppekava*) and basic-school curriculum (*põhikooli riiklik õppekava*) are competency-based and align unusually well with the frameworks below — Estonia is a top PISA performer and runs the ProgeTiiger programme putting computational thinking into early grades, so a skill tree with an explicit logic/digital branch will feel native, not exotic.

---

## Part A — How Mastery Paths and Tech Trees Are Actually Designed

### A1. Mastery learning: the pedagogical spine

The core idea predates all software. **Benjamin Bloom, "Learning for Mastery" (1968)**: hold *achievement* constant and let *time* vary, instead of the classroom default (time constant, achievement varies). Students don't advance until they demonstrate mastery (typically ~80–90% on a formative check); those who fail get corrective instruction and retest. **Bloom's "2 Sigma Problem" (1984)** found 1:1 tutoring + mastery methods moved the average student ~2 standard deviations above conventional classrooms — this paper is the explicit founding citation of Khan Academy, ALEKS, and most adaptive-learning products. **Thomas Guskey** and **James Block** carried the implementation research: mastery learning works when (a) units are small, (b) the mastery check is genuinely diagnostic, and (c) correctives are *different* from the original instruction, not just "read it again."

Supporting cognitive science that must be baked into mechanics, not just content:

| Principle | Key researcher/work | Skill-tree implication |
|---|---|---|
| Zone of Proximal Development | Lev Vygotsky | Next unlockable nodes should be *just* beyond current mastery — the tree's "frontier" IS the ZPD, made visible |
| Scaffolding | Wood, Bruner & Ross (1976) | Each node's exercises start heavily supported, fade support within the node |
| Spaced repetition / forgetting curve | Ebbinghaus; Cepeda et al. (2006) | Mastery must decay-and-refresh; a node "mastered" once at age 6 is not mastered at 8 |
| Retrieval practice | Roediger & Karpicke (2006) | Booklet exercises = retrieval events, not re-reading; mixed-review pages in every booklet |
| Desirable difficulties | Robert Bjork | Interleave node types within a booklet; a booklet that's 100% one skill overstates mastery |
| Cognitive load | John Sweller | Young children: one new element per exercise; picture sudoku works because rules are near-zero verbal load |
| Deliberate practice | K. Anders Ericsson | Nodes need tight feedback loops — self-checkable answers, parent check pages |
| Flow channel | Mihaly Csikszentmihalyi | Difficulty ramps inside each node: ~80% success rate is the sweet spot for children |

### A2. Khan Academy's knowledge map: what it did and why it changed

Khan Academy is the most instructive real-world case because it built a literal skill tree, then partially retreated from it.

- **2011–2014, the Knowledge Map:** a zoomable constellation of ~400 (later 1,000+) math skills from single-digit addition through calculus, with explicit prerequisite edges. Stars filled as you progressed. Mastery states per skill evolved into four levels: **Attempted → Practiced → Level Two → Mastered**, with the key mechanic that you could not reach "Mastered" in one sitting — **Mastery Challenges** resurfaced the skill *days later*, mixed with other skills (spaced retrieval built into the state machine). Sal Khan describes the rationale in *The One World Schoolhouse* (2012): the map exposed that "gaps" (an unmastered prerequisite three tiers back) were the root cause of later failure.
- **Why they retired the free-roam map (2014→"Missions", 2018→"Course Mastery"):** users got lost. A 1,000-node visible graph produced choice paralysis and grinding of easy far-flung nodes. Khan kept the *underlying* prerequisite graph for its recommendation engine but replaced the visible artifact with course-scoped mastery percentages. **Lesson: the prerequisite graph and the map you show are two different products.** Keep the graph rigorous internally; show children a curated, small, era-scoped view.
- Their internal ordering also leaned on the **Common Core Coherence Map** (Student Achievement Partners, lead writer Jason Zimba) — a public prerequisite graph over math standards worth mining directly for our numeracy branch.

### A3. Knowledge Space Theory and learning trajectories: the rigorous versions

- **Knowledge Space Theory — Jean-Paul Doignon & Jean-Claude Falmagne** (*Knowledge Spaces*, 1999): the mathematical foundation of **ALEKS**. A domain is a set of problems; a *knowledge state* is a feasible subset of mastered problems; prerequisite relations constrain which states exist. Two killer concepts to steal:
  - **Inner fringe** — skills just mastered (fragile, schedule review).
  - **Outer fringe** — skills the learner is ready to learn *right now*. ALEKS only ever offers the outer fringe. Our tree's "unlockable next" set is exactly this.
- **Learning trajectories in early mathematics — Douglas Clements & Julie Sarama** (*Learning and Teaching Early Math: The Learning Trajectories Approach*; the Building Blocks curriculum; learningtrajectories.org / LT2). This is **the single most directly usable source for our ages 5–7 numeracy branch**: empirically validated developmental progressions (e.g., counting: reciter → corresponder → counter (small numbers) → producer → counter-on → skip counter), each with matched activities. Their central finding: children's math develops along natural progressions with identifiable levels, and instruction pitched one level up outperforms grade-level instruction. **Jere Confrey's Math-Mapper** did similar work for middle grades.
- **Dynamic Learning Maps (University of Kansas):** a ~5,000-node research learning map across ELA/math — proof that fine-grained maps exist, and a warning about maintenance cost at that granularity.
- **Bill McCallum's Common Core Progressions documents** — narrative prerequisite logic for K–3 math domains (counting & cardinality → operations & algebraic thinking → base ten), free, and battle-tested.

### A4. Civilization-style tech trees: game-design principles that transfer

The Civ tech tree (Sid Meier & Bruce Shelley, 1991; descended from the tech-card system in Avalon Hill's *Civilization* board game, 1980) is the canonical "visible prerequisite DAG as motivation engine." Design principles distilled from Civ I–VI, and from designer commentary (Soren Johnson, lead designer Civ IV, has written extensively on tech-tree design; Sid Meier's axiom: *"a game is a series of interesting decisions"*):

1. **Eras/tiers gate global progression.** The tree is chunked into Ancient → Classical → Medieval… You can't see or worry about Flight while in the Bronze Age. *Transfers directly: age-band tiers hide complexity and keep the visible frontier small.*
2. **AND-prerequisites with sparse fan-in.** Most Civ techs require 1–2 prior techs, rarely 3. Wide fan-in makes the graph illegible.
3. **Multiple viable paths, no dead ends.** Every branch eventually reconnects; specializing in one branch delays but never permanently locks others. *For kids: a child who races ahead in logic must never be hard-locked out of the creativity branch.*
4. **Eureka/Inspiration boosts (Civ VI):** performing a real in-world action (e.g., meet another civilization) cuts a related tech's research cost ~40–50%. *This is the best single mechanic to steal: real-world quests ("measure three things in the kitchen with a ruler") discount the practice requirement of a node — bridges paper exercises to life.*
5. **Costs scale by tier**, so early nodes give fast wins (crucial for a 5-year-old's first week) and later nodes teach persistence.
6. **Distant visible payoffs pull behavior.** Players beeline toward a wonder several techs away. *Career capstone nodes should be visible-but-greyed from day one.*
7. **Negative examples:** *Path of Exile*'s 1,300-node passive tree — famously illegible, requires third-party planners; *Duolingo* deleted its skill tree entirely in 2022 for a single linear path because users made pathological choices — but paid for it in lost learner agency. **Sweet spot: a real DAG, but small enough to print on one poster per tier.**

### A5. Badge and mastery-recognition systems

- **Scouting merit badges (1910s–):** the oldest working model. Properties worth copying: each badge has *published, concrete requirements* ("do/show/explain X"), an external verifier (counselor ≈ parent), and badges ladder into ranks (≈ tiers). Badges certify *demonstrated performance*, never attendance.
- **Mozilla Open Badges (2011; now the 1EdTech Open Badges 3.0 standard):** a badge = image + machine-readable metadata (issuer, criteria, evidence). Even for a family system, keeping a per-badge *evidence log* ("mastered 2026-09-14, booklet 3, retest 2026-09-28") is the load-bearing idea.
- **Khan Academy badges** (Meteorite → Moon → Earth → Sun → Black Hole rarity ladder) and **energy points**: their retrospective lesson is that points-for-activity got farmed; badges tied to *mastery states* held value.
- **Duolingo crowns/legendary levels:** mastery levels per skill (≈ Khan's practiced/mastered ladder) work; **streak mechanics are loss-aversion engines and are inappropriate for ages 5–9** — missing a day because of a family trip should never feel like losing.
- **Motivation research guardrails:** Deci & Ryan's **Self-Determination Theory** — sustainable motivation needs *autonomy, competence, relatedness*; extrinsic rewards for already-enjoyed activities can backfire (**Lepper, Greene & Nisbett 1973** — the classic preschool drawing/reward study). Meta-analyses (Hamari et al. 2014) find gamification works best when rewards are *informational* (signal competence) rather than *controlling*. **Rule: badge the mastery, never bribe the activity. Let the child choose among 2–4 frontier nodes (autonomy). Ceremony over prizes (relatedness: parent signs the node on the poster).**

### A6. Prerequisite-graph design principles (synthesis)

1. **It must be a DAG** (no cycles), but *shown* era-by-era, not whole.
2. **Prerequisite = genuinely load-bearing.** Test: "could a child plausibly do B well without A?" If yes, the edge is decoration — cut it. Decorative edges are the #1 failure mode (they create fake bottlenecks and inflate chains).
3. **Distinguish hard prerequisites (AND), soft prerequisites ("helpful", rendered as dashed lines, not enforced), and corequisites** (letter formation ↔ pencil grip develop together).
4. **Fan-in ≤ 3, fan-out unbounded.** Foundational nodes (counting to 10, phonemic awareness) legitimately unlock many things — that's what makes them feel important.
5. **Chain-length budget:** longest path within a tier ≤ ~6 nodes, so a child sees a tier as conquerable.
6. **Redundant paths on purpose:** at least two routes into every tier-gateway node, so one hated activity type never blocks the tree.
7. **Mastery is a state machine, not a checkbox:** e.g., *Introduced → Practiced → Mastered (passed check) → Consolidated (passed a spaced re-check ≥2 weeks later) → needs-polish (decay timer expired)*. Only *Consolidated* counts as a satisfied prerequisite for far-downstream nodes.
8. **Every node carries an explicit, parent-runnable mastery criterion** (see Part C).

---

## Part B — Career-Back Competency Mapping (Ages 5–9 → 8 Target Careers)

### B1. The frameworks

| Framework | Owner / key figures | Structure | What we take |
|---|---|---|---|
| **OECD Learning Compass 2030** | OECD (Andreas Schleicher's directorate) | Core foundations (literacy, numeracy, digital & data literacy, health) → knowledge/skills/attitudes/values → **transformative competencies**: creating new value, reconciling tensions & dilemmas, taking responsibility; **student agency**; Anticipation–Action–Reflection cycle | Our tier-0/1 branches ≈ "core foundations"; student agency justifies child-chooses-frontier mechanic; AAR cycle = quest structure (plan → do → reflect page in booklets) |
| **CASEL 5** | CASEL (Roger Weissberg et al.) | Self-awareness, self-management, social awareness, relationship skills, responsible decision-making | The complete spec for our SEL branch; **Durlak et al. 2011** meta-analysis (213 programs): SEL programs → +11 percentile points academic achievement — SEL is a *prerequisite feeder* to academics, not a side branch |
| **P21 / Framework for 21st Century Learning** | Partnership for 21st Century Learning | The "4 Cs": critical thinking, communication, collaboration, creativity + information/media/tech literacy | Naming and balance check for non-academic branches |
| **Computational thinking** | Jeannette Wing (2006, CACM); **Marina Umaschi Bers** (*Coding as a Playground*, ScratchJr, KIBO) | Decomposition, pattern recognition, abstraction, algorithms, debugging | The logic/digital branch spec; Bers shows ages 4–7 can do real sequencing/debugging with ScratchJr & Bee-Bot |
| **Executive function** | **Adele Diamond** (2013 Annual Review); Center on the Developing Child, Harvard | Three core EFs: inhibitory control, working memory, cognitive flexibility → planning, self-monitoring | EF is the *trunk* of the tree — see B2 |
| **DigComp 2.2 / ISTE Standards for Students** | EU JRC / ISTE | Digital competence areas | Sanity check for the digital branch at child-appropriate level |

**Predictive evidence for which early skills matter:**
- **Duncan et al. 2007** ("School Readiness and Later Achievement", *Developmental Psychology*, 6 longitudinal datasets): **early math skills at school entry are the strongest predictor of later achievement** — stronger than early reading, which is second; attention skills third. Early math is not just for STEM careers; it predicts *everything*.
- **Moffitt, Caspi et al. 2011** (Dunedin cohort, PNAS): childhood **self-control** predicts adult health, wealth, and (inversely) criminality, controlling for IQ and class. (The famous marshmallow test's predictive power shrank under controls in **Watts, Duncan & Quan 2018** — so treat self-control as trainable context-dependent skill, not fixed trait.)
- **Heckman** (Perry Preschool analyses): early non-cognitive skill investment has the highest ROI of any educational spending; effects run through character skills more than IQ.
- **Wai, Lubinski & Benbow 2009**: adolescent **spatial ability** predicts STEM careers over and above math/verbal — and spatial skill is highly trainable at 5–9 (blocks, LEGO, maps, tangrams, mental rotation games). Most curricula under-serve it; ours should not.
- **Dweck** (growth mindset) and **Duckworth** (grit): real but modest effects in replications (Sisk et al. 2018); implement as *praise-the-process norms and productive-failure framing* baked into materials, not as standalone nodes.

### B2. The convergence finding (this shapes the whole tree)

When you map all 8 careers back to age 5–9 foundations, **~80% of the foundations are shared**. Every one of the 8 careers requires, at age 5–9 grain: fluent literacy, fluent numeracy, working memory & inhibitory control, sustained attention, oral communication, cooperation, and error-tolerance/persistence. **Therefore: build ONE common trunk, and differentiate careers through (a) weighting of upper-tier branches and (b) themed "quests" that flavor practice, not through separate sub-trees.** A skill tree that forks toward "doctor" at age 6 would be both developmentally wrong and motivationally brittle (children's career interests churn).

### B3. Career-back mapping table

Skill domains: **NUM** numeracy · **LIT** literacy · **LOG** logic & computational thinking · **EF** executive function · **SEL** social-emotional · **COM** communication · **DIG** digital literacy · **CRE** creativity · **SPA** spatial/fine-motor (recommend adding this 9th domain — see Wai above).

| Career | Heaviest domains | Concrete age 5–9 precursor skills (booklet-able) | Signature "flavor quest" examples |
|---|---|---|---|
| **Doctor** | LIT, NUM, EF, SEL | Reading stamina; body-parts & living/non-living vocab; measurement (temperature, weight); working memory (multi-step instructions); fine motor precision; empathy & perspective-taking (CASEL social awareness); calm under "yuck/scary" (inhibitory control) | Keep a "patient chart" for a sick teddy: temperature graph over 5 days; follow a 4-step first-aid card from memory |
| **Software engineer / IT** | LOG, NUM, EF, DIG | Sequencing (order 5 pictures); pattern completion; decomposition (break a task into steps); conditionals ("if red card, clap"); debugging (find the wrong step); Bee-Bot/ScratchJr programs; **picture sudoku → constraint satisfaction**; binary-style sorting games | Write a "program" (arrow cards) to walk a parent through the room; find the bug in a 6-step sandwich recipe |
| **Fortune-500 manager** | SEL, COM, EF, NUM | Turn-taking & role allocation in group play; planning a multi-step project (drawing a plan *before* building); explaining a decision in 3 sentences; reading emotions from faces; simple resource budgeting ("you have 10 tokens"); delegation in family chores | Run a "family restaurant night": menu, prices, assign roles, debrief what to improve (AAR cycle) |
| **Lawyer** | LIT, COM, LOG, EF | Reading comprehension (who/what/why questions); retelling with sequence intact; giving reasons ("I think X *because*…"); spotting rule violations in games; fairness reasoning; listening-then-summarizing another's position | Family "court" over a toy dispute: each side states a claim + 2 reasons; judge (parent) rules |
| **Scientist** | LOG, NUM, LIT, CRE | Observation & recording (draw what you see, 3 details); sorting/classification by ≥2 attributes; measurement with standard units; prediction → test → compare ("What will float?"); simple bar charts; question-asking fluency | Grow two plants, one in the dark — daily picture log, conclusion sentence |
| **Engineer** | SPA, NUM, LOG, CRE | Mental rotation & tangrams; build-from-diagram (LEGO instructions ≈ reading technical drawings); stable-structure intuition (bridges from paper); measuring & comparing lengths; iterate-after-failure ("version 2") | Build a bridge holding 10 coins from 5 sheets of paper; document v1 vs v2 |
| **Entrepreneur** | CRE, SEL, COM, NUM | Idea fluency (10 uses for a box); noticing problems ("what's annoying at home?"); simple money: coins, prices, change, profit = sell − cost; persuading (make a poster that convinces); coping with a flopped idea (self-management) | Lemonade/craft stand with real cost & profit accounting; pitch a toy invention in 1 minute |
| **Finance professional** | NUM, EF, LOG, LIT | Strong number sense & place value; skip counting → multiplication; comparing quantities & simple ratios ("2 for the price of 3?"); saving/delayed gratification (savings jar with a chart); probability intuition (dice/spinner games); reading tables | Track pocket money for a month in a ledger; "is the big pack actually cheaper?" supermarket quest |

### B4. Estonian curriculum cross-check

The Estonian kindergarten curriculum's seven learning areas (mina ja keskkond, keel ja kõne, matemaatika, kunst, muusika, liikumine + üldoskused/general skills including play, cognition and self-management) map cleanly onto the 9 domains above; grades 1–3 (I kooliaste) competencies likewise. Practically: our tree can double as evidence the child is ahead of / on track with the national curriculum, which matters for Estonian school readiness evaluation (koolivalmidus) at the kindergarten→school transition.

---

## Part C — Concrete Guidance for Our Skill Tree

### C1. Tier structure (recommendation)

Five eras, mapped to age/grade bands, Civ-style names optional but recommended for the poster:

| Tier | Era name | Age / Estonian stage | Scope | Approx. node count |
|---|---|---|---|---|
| 0 | **Spark** | ~5, last lasteaed year | School-readiness foundations: counting to 20, phonemic awareness, pencil control, 10-min sustained attention, feelings vocabulary, first sequencing | 20–30 |
| 1 | **Foundations** | ~6–7, grade 1 | Decoding→reading, add/sub within 20, patterns & sorting, ScratchJr-level sequencing, turn-taking, telling a story in order | 30–40 |
| 2 | **Builder** | ~7–8, grade 2 | Reading to learn, add/sub within 100 + intro multiplication, debugging & conditionals, planning-before-doing, money, measurement, first typed/digital creation | 30–40 |
| 3 | **Explorer** | ~8–9, grade 3 | Multiplication/division fluency, paragraph writing, multi-step problem solving, data & charts, real Scratch, running a small project end-to-end | 30–40 |
| 4 | **Horizons** | visible from day 1, unlockable from tier 3 | 8 **career capstone quests** (one per career, multi-week, e.g. the restaurant night, the bridge, the ledger) + open "design your own" | 8–12 |

Total: **~120–160 nodes.** (Khan-scale ~1,000 is unmaintainable for a family; Duolingo-scale linearity kills agency; one poster per tier must be printable and legible.)

**Branches (columns on the poster):** NUM, LIT, LOG, EF, SEL, COM, DIG, CRE, SPA. EF and SEL nodes are *real nodes with real checks* (e.g., "followed a 3-step instruction from memory, 4/5 days"), not vibes — Diamond's and Durlak's evidence earns them equal billing.

### C2. Node granularity rule

**A node = one assessable "can-do" statement, masterable in 1–3 weeks of 10–20-minute sessions, checkable by a parent with a 5–10 item check in under 10 minutes.**

- Too big (reject): "knows addition." Too small (reject): "adds 3+4."
- Right-sized examples: "adds two numbers within 20 crossing ten"; "solves a 4×4 picture sudoku unaided"; "retells a story with beginning-middle-end"; "writes a Bee-Bot/arrow program of 6+ steps to reach a target."
- Every node ships with: can-do statement, 2–3 practice activity types (at least one printable, one physical/no-paper), mastery check spec, and its Eureka quest (see C4).

### C3. Prerequisite rules (enforceable spec)

1. **DAG only; edges must pass the load-bearing test** ("could the child do B without A?" — if plausibly yes, use a dashed *soft* edge or none).
2. **Hard prerequisites per node: max 3** (typical 1–2). Distinguish AND (all required) — the default — from the rare OR-group ("any counting-to-20 node").
3. **Prerequisite satisfaction requires *Consolidated* status**, i.e., mastery check passed twice, ≥2 weeks apart (spaced verification à la Khan Mastery Challenges). States: *Locked → Available (outer fringe) → Practicing → Mastered → Consolidated → Needs-polish* (decay timer: 8–12 weeks without use for fluency skills).
4. **Chain length ≤ 6 inside a tier; every tier gateway reachable by ≥ 2 paths.**
5. **Cross-branch edges are allowed but flagged as "bridge" nodes** (e.g., LIT "reads simple instructions" → LOG "follows a written recipe/algorithm"); keep them to ~10–15% of edges so branches stay legible.
6. **Frontier size shown to the child: 3–5 available nodes at a time** (ALEKS outer-fringe discipline; child picks — SDT autonomy). The full tier poster is visible; future tiers appear as sealed scrolls/greyed continents.
7. **Career capstones are visible from day 1** as distant wonders, each with its path highlighted on demand ("what do I need to open Doctor?").

### C4. Mechanics to steal, per source

- **From Civ VI:** *Eurekas* — every node has one real-world quest that discounts required practice (e.g., node "counts money to 1 €": Eureka = pay for bread at the shop yourself). Bridges booklets to life; parents love it.
- **From Khan:** mastery is multi-level and time-separated; mixed-review "mastery challenge" pages at the back of every booklet re-test 5–8 older nodes.
- **From ALEKS/KST:** only offer the outer fringe; track the inner fringe for review scheduling.
- **From Scouting/Open Badges:** published criteria + evidence log + a signing ceremony on the poster (sticker/stamp/parent signature) — informational reward, relatedness built in.
- **Anti-patterns (do not build):** streaks/loss-aversion; points for time-on-task; badges for attendance; a single forced linear path; locking CRE/SEL branches behind academic grind; decorative prerequisites.

### C5. Where picture sudoku plugs in (booklet #1)

Picture sudoku is a **LOG-branch node cluster** with near-zero literacy load — ideal first booklet for age 5:
- Tier 0: "completes 4×4 picture sudoku with 1 picture type missing per row" (feeds: visual scanning, one-constraint reasoning).
- Tier 0→1: "solves standard 4×4 picture sudoku unaided" (feeds: multi-constraint elimination — direct precursor to LOG debugging/conditionals and NUM systematic checking; exercises Diamond's working memory + inhibitory control: you must *not* place the tempting-but-illegal picture).
- Tier 1: "solves 6×6 picture sudoku" and "explains *why* a cell must be X" (COM bridge: reasoning aloud — the lawyer/scientist "because" muscle).
- Difficulty ramp inside the booklet: 80% solvable-comfortably, per the flow channel; final 2 pages stretch.

### C6. Suggested node data model

```yaml
id: log-sudoku-4x4
branch: LOG
tier: 0
can_do: "Solves a standard 4x4 picture sudoku without help"
prereqs_hard: [log-sorting-1attr, ef-attention-10min]
prereqs_soft: [spa-visual-scan]
mastery_check: "3 fresh 4x4 puzzles, ≤1 hint total, within 15 min"
consolidation: "repeat with 2 puzzles ≥14 days later"
decay_weeks: 12
eureka: "Spots and explains a mistake in a parent's deliberately-wrong puzzle (practice requirement halved)"
activities: [booklet-01, physical-card-sudoku]
feeds_careers: [software_engineer, scientist, finance]   # metadata for career-path highlighting, not gating
```

### C7. Key sources index

Bloom 1968, 1984 · Guskey, *Implementing Mastery Learning* · Doignon & Falmagne, *Knowledge Spaces* (1999) · Clements & Sarama, *Learning and Teaching Early Math* + learningtrajectories.org · Common Core Coherence Map (Student Achievement Partners) & McCallum's Progressions · Khan, *The One World Schoolhouse* (2012) · Wing, "Computational Thinking" (CACM 2006) · Bers, *Coding as a Playground* (2018) · Diamond, "Executive Functions" (Annu. Rev. Psychol. 2013) · CASEL framework; Durlak et al. 2011 · OECD Learning Compass 2030 concept notes · Duncan et al. 2007 · Moffitt et al. 2011 (Dunedin) · Watts, Duncan & Quan 2018 · Heckman (Perry Preschool) · Wai, Lubinski & Benbow 2009 · Deci & Ryan (SDT); Lepper, Greene & Nisbett 1973 · Bjork (desirable difficulties); Roediger & Karpicke 2006 · Ericsson (deliberate practice) · Sid Meier / Bruce Shelley (Civilization); Soren Johnson on tech-tree design · Mozilla/1EdTech Open Badges · Estonian riiklikud õppekavad (lasteaed + I kooliaste), ProgeTiiger.
