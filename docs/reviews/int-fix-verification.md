# International-Review Fix Verification (v1.6 → v1.7)

**Date:** 2026-09-04
**Scope:** Verify that `docs/methodology/combined-framework.md` v1.7 and `curriculum/learning-path.md` v1.7 implement every BLOCKING and IMPORTANT finding (and the claimed nice-to-haves) from the three international reviews (`int-review-finland.md`, `int-review-singapore.md`, `int-review-japan.md`); mechanically re-verify the v1.7 graph across all three data sources; sweep the shipped app (`curriculum/skill-tree-template.html` / built `skill-tree.html`) for CR19 consistency. Fix-verification only — no new scope.
**Method:** Full read of both v1.7 documents and all three reviews; targeted extraction of every v1.7-touched node card; scripted validation of the learning-path JSON (md block, `learning-path.json`, and the html-embedded `DATA`, compared byte-equivalent after normalization); line-level read of the app template.

**Verdict: ISSUES FOUND — but none in the documents.** All 42 review findings (3 blocking — one shared issue — 27 important, 12 nice-to-have) are genuinely implemented in the v1.7 texts; every mechanical check passes; the three graph copies are identical. The issues are in the collateral sweep: the shipped app satisfies CR19's blocking clause (red removed, additive palette) but **conflicts with CR19 clauses 3 and 4** (career-tab progress bar/counts; full-DAG default view), and its tier subtitles contradict CR14's grade anchoring. Details and severities in Part 4.

---

## Part 1 — Finding-by-finding checklist

Disposition legend: **✔ implemented** (present in the v1.7 text at the cited location, verified verbatim-level) · **✔* implemented as ruling** (the fix demanded a ruling/commitment and the ruling is written; the downstream artifact remains future work by design) · **⚠** implemented in text but contradicted by the shipped app (see Part 4).

### Finland (1 blocking · 9 important · 6 nice)

| # | Sev | Demanded | Disposition | Where in v1.7 |
|---|---|---|---|---|
| FIN-1 | BLOCKING | Kill child-visible red / "not learned" state | ✔ | CR19 clause 1 — red state **removed entirely**, additive unmarked/learning/mastered palette *for parents and children alike* (the owner's decision, stronger than FIN-1's five-state proposal and documented as such); app code confirms: `STATES = ["learning","mastered"]`, legend "not started yet" neutral, no `.s-notlearned` CSS exists |
| FIN-2 | IMPORTANT | Extend CR13/CR12 display law to screens by name | ⚠ | CR19 clause 3 verbatim (era-scoped default, frontier-first, sealed scrolls beyond current+1, wonders never progress bars, DAG never shown to child). Charter text complete; **shipped app violates it** — Part 4, issue 2 |
| FIN-3 | IMPORTANT | App charter: no aggregates/%, notifications, timers, cross-child screens | ⚠ | CR19 clause 4 verbatim (no "X of N," no era %, no % toward career, no notifications, no visible timers, no cross-child grid). Charter text complete; **career-tab bar violates it** — Part 4, issue 1 |
| FIN-4 | IMPORTANT | App mirrors paper poster; child owns the record | ✔ | CR19 clause 2 (poster primary, marking with/by the child, celebration physical, pause protection binds app) + clause 7 (engine before dashboard) |
| FIN-5 | NICE | No live decay ticking | ✔ | CR19 clause 5 (quarterly-sweep button not daemon, pauses honored, softened-dim default code path); app has no decay code at all — trivially conformant |
| FIN-6 | IMPORTANT | Band-1 check register: observed-in-play or game-format; neutral-face from Band 2 | ✔ | §5.2 "Band-1 check register" — (a) observation-in-play logged like B-instances OR game format with the 1b trial as named template, (b) neutral-face protocol scoped "from Band 2" (also stamped on the administration-protocol bullet), (c) Band-1 strips ruled game-format; learning-path §7 re-states it for the 21 tier-0 check specs |
| FIN-7 | NICE | Era-graded wonder rendering | ✔ | §6 poster-spec rendering rule (a): Spark poster's horizon unnamed (skyline/mountains), names+door-cards from Builder/Explorer, path-highlighting answer-only |
| FIN-8 | IMPORTANT | Whole-child day ledger, combined desk cap, standing yield | ✔ | §5.6 — school-side column added to the load table per band (incl. homework estimates), combined daily desk cap ≤30–40 min at Bands 3–4 with system-sheds-first, crunch-week yield promoted to standing budget |
| FIN-9 | IMPORTANT | Reword CR14 numeracy run-ahead; make Band-2 number dose pull-conditional | ✔ | CR14 — "evidence-permitted and family-chosen — the earlier 'evidence-endorsed' overstated it," with the R3 slow-clock counter-evidence named; Band-2 number-led slots pull-conditional (also wired into the §3 Band-2 template row) |
| FIN-10 | NICE | Name the daily outdoor hour as soil | ✔ | §3 seasonal-texture paragraph: outdoor hour "never scheduled, never logged, never a check… sessions fit around the outdoor day, not the reverse" |
| FIN-11 | IMPORTANT | Seasonal phenomenon week | ✔ | §3 seasonal-layer vehicle (a): 2–4×/year, one child-chosen question across ≥3 domains, B19-documented, wild-node compatible, folk-calendar hosts |
| FIN-12 | IMPORTANT | Wire wild nodes into the frontier; Reggio proposal clause | ✔ | §5.1 — a claimed wild node always holds one surfaced frontier slot until retired (floor, not ceiling); starting-frontier rule gains "or anything the child proposes" |
| FIN-13 | IMPORTANT | Sustainability lens + costume carriers | ✔ | §6 cross-cutting lens; B13 waste-sort/repair Life page; `cre-iterate-v2` "version 2 uses less"; `t4-design-build` uses-less cycle; `quest-entrepreneur` costs incl. materials AND leftovers; `t4-venture-lab` materials-honest P&L; `sci-body-health` seed give-back/feeder |
| FIN-14 | NICE | Name multiliteracy lens | ✔ | §6 lens with carriers listed and interpret/produce pairing rule |
| FIN-15 | NICE | Name the rejected Nordic English path | ✔ | GP10 "The rejected lighter path, named" — costs ~zero desk minutes, comparable endpoint ~3–4 years later, family chose the by-9 endpoint |
| FIN-16 | NICE | Drop numeric latency bars; retrieval-listen | ✔ | §5.5 covert-timing ban ("a hidden stopwatch is still a stopwatch"); §5.2 check-format example rewritten; both boss `mastery_check` fields now carry the retrieval-listen, "gentle and unclocked, no racing" |

### Singapore (1 blocking · 8 important · 3 nice)

| # | Sev | Demanded | Disposition | Where in v1.7 |
|---|---|---|---|---|
| A-1 | BLOCKING | Display-law spec before app ships | ⚠ | CR19 (whole charter). Same caveat as FIN-2/FIN-3 — Part 4 |
| A-2 | IMPORTANT | States derive from check events, not hand-set colors | ✔* | CR19 clause 6 — the hand-set v1 is named an **accepted, stated simplification** (acceptable because the app is a mirror, clause 2; the §5.2 checks + §5.3 log stay source of truth), with the derived-states requirement binding any future computing version. Honest-deviation route, consistent with the house style; learning-path §7 names the app a tooling consumer |
| A-3 | NICE | Build the engine before the dashboard | ✔ | CR19 clause 7 (retest queues, dim-check sweeps, placement sweeps, strip generation) |
| S-1 | IMPORTANT | Stage the model method; plant one-step + comparison problem types | ✔ | Four-node ramp verified on the cards: `num-addsub-20` rung 1 (one-step join/separate/part-whole as a **named sub-check**, first pictorial part-whole bar beside the ten-frame), `num-addsub-100` rung 2 (comparison model, "how many more/fewer" **named as a sub-check**, R2 r22 closed), `num-mult-groups` rung 3 (equal-groups bar beside the array), `num-problems-data` reworded so only two-step composition is new; §6 NUM row now claims CPA **and** the model method. Trunk sub-question: §1 gains the explicit "the schedule carries them" scoping sentence |
| S-2 | IMPORTANT | Non-routine puzzler pages, heuristics named-after-met | ✔ | B24(a) — one puzzler page per numeracy booklet from tier 2, method not given, ≥2 legitimate attacks, S5 idiom, B17 footer |
| S-3 | NICE | Remainder / doubles-near-doubles / reasonableness | ✔ | All three verified on cards: `num-times-tables` remainder-sharing exercise; `num-addsub-20` doubles/near-doubles/compensation ladder (strategy ladder named in full); `num-addsub-100` "will 47+25 land nearer 70 or 100?" |
| S-4 | IMPORTANT | Within-set variation as a design rule | ✔ | B23 — author states what varies/stays constant, one dimension at a time, contrast sets as adjacent items |
| S-5 | IMPORTANT | Numeracy applied reference before sudoku extends past S3 | ✔* | §4.4 note 6 — the numeracy booklet family's §4.4-grade reference ruled the **next methodology deliverable, authored before the sudoku line extends past S3** (level table, checklist, model-method ramp, B24 puzzlers, B23 exercised). The ordering constraint the finding demanded is now binding; the document itself is correctly future work |
| S-6 | IMPORTANT | GP17 ceiling response | ✔ | GP17 — sustained >~95% surfaces the stretch variant before the next rung, more volume never the response; §5.1 "deep or forward?" made an explicit weekly curation choice |
| S-7 | NICE | Ahead-of-trajectory paragraph | ✔ | §5.4 — lead is normal, depth before acceleration, the parent–teacher school-interface conversation named and scheduled (start of each school year) |
| S-8 | IMPORTANT | English floor on the CR18 rail + quarterly line | ✔ | CR18 — English ≥ half the nights or stacked ~5+5, share ruled / pattern free, missed night still nothing; §5.4 quarterly dim-check gains the rail-floor question |
| S-9 | IMPORTANT | Invited-production seed at 6–8 | ✔ | CR18 (English songs in repertoire, volunteered English received warmly), §3 Band-2 template (standing invited-echo line on phonics sessions), B2 register extension (never corrected mid-flow) |

### Japan (1 blocking · 10 important · 3 nice)

| # | Sev | Demanded | Disposition | Where in v1.7 |
|---|---|---|---|---|
| APP-1 | BLOCKING | Re-specify the app before build | ⚠ | CR19. Same caveat — Part 4 |
| APP-2 | IMPORTANT | No hand-marking bypass of the check machinery | ✔* | CR19 clause 6 (see A-2) + clause 2's "an app entry is a transcription of the wall, not an adult's verdict" |
| APP-3 | IMPORTANT | App carries ceremonies/pauses or is ruled subordinate | ✔ | CR19 clause 2 — poster primary, app mirrors and never replaces, declared-pause protection binds the app, celebration stays physical (the "explicitly subordinate" arm of J's fix, chosen and written) |
| J-1 | IMPORTANT | Contribution ladder beyond tier 0 | ✔ | `sel-contribution` (tier 1, cluster, check B, prereq `sel-selfcare`, zero consumers): rota-owned weekly job, shared-space reset, weekly food element maturing to ~8, regular service to a person; §6 SEL row contribution ladder + "the family is this system's community of contribution"; §3 band rows carry the progression |
| J-2 | IMPORTANT | Rota-reliability check semantics | ✔ | §5.2 — tally unit = completed rota cycle (job done all week, ≤1 reminder), applied to `sel-selfcare`(c) and the ladder; the pleasant-task/duty tension named |
| J-3 | IMPORTANT | Weekly family meeting | ✔ | CR20 — ~10 min, child chairs from ~7, rota assignment organ, second-and-last named exemption, priced in §5.6, wired into the §3 template |
| J-4 | IMPORTANT | Multi-day Big Problem + corrective-rule scoping | ✔ | B24(b) — one marked multi-day problem per booklet from Band 2, no-hints footer script, *takai mondai* keystone attachment; GP17 scope clause exempts the Big Problem from drop-a-rung |
| J-5 | IMPORTANT | Compare-two-ways page class | ✔ | B25 — two worked solutions side by side, parent defends the losing method one round, distinguished from B19's two-solutions page |
| J-6 | IMPORTANT | Quest-revival tradition; written v2s actually run | ✔ | §5.1 quest-revival ruling (poster/seasonal layer, debrief sheet read aloud first, tree state untouched); §3 seasonal vehicle (b); `quest-entrepreneur` card: "version 2 RUNS… opens by reading this decision aloud, so the hansei is a promise the system keeps" |
| J-7 | IMPORTANT | Care-of-work ritual (fair copy) | ✔ | §5.3 fair-copy ruling (keystone work sample as deliberate best version; grandparent letter the canonical first instance; adults never rank); `mot-handwriting-auto` monthly child-chosen "most beautiful page"; B17 posture/unhurried-strokes footer line. (`lit-composition`'s card carries the posted grandparent letter; the ritual itself correctly lives in §5.3, which governs keystone evidence) |
| J-8 | IMPORTANT | Seasonal layer ships vehicles | ✔ | B13(a) season-keyed Life page per printed booklet; `sci-cause-effect` four-season weather-strip recurrence; `sci-body-health` care log keyed to spring planting; §3 restates all three |
| J-9 | NICE | Parent models being wrong | ✔ | B17 weekly own-mistake narration with CR20's parent turn as its scheduled home |
| J-10 | NICE | Identity-talk script; abandoned-wonder rendering | ✔ | B17 identity-talk script (praise the pull, never affirm the label); §6 rendering rules (b) folded-map-corner exit, (c) script rides B17 |
| J-11 | NICE | Child gives back on the rail; non-household audience | ✔ | CR18 return leg (from ~8, one rail night flips direction); `lit-reading-fluency` card carries it; `com-present` gains the non-household-audience showing |

**Checklist result: 42/42 findings addressed in the documents.** 39 fully implemented, 3 implemented-as-ruling by design (A-2/APP-2 via CR19 clause 6's stated v1 simplification; S-5 via the §4.4 note 6 ordering commitment) — each of these is the honest-deviation route the reviews themselves permitted. The ⚠ marks are not document failures; they flag the app-side conflicts in Part 4.

---

## Part 2 — Mechanical re-verification (scripted)

Script: scratchpad `verify_v17.py`, run against the md JSON block, `curriculum/learning-path.json`, and `curriculum/skill-tree.html`'s embedded `DATA`.

| Check | Expected | Result |
|---|---|---|
| md JSON block ≡ learning-path.json | identical | **PASS** (normalized deep-equal) |
| learning-path.json ≡ skill-tree.html DATA | identical | **PASS** |
| Node total | 109 | **PASS** |
| Tier counts | 21/20/18/29/11/10 | **PASS** |
| Unique ids | all | **PASS** |
| Hard edges | 137 | **PASS** |
| Raw cross-domain edges | 34 | **PASS** |
| Roots (zero-prereq) | 17, all tier 0 | **PASS** |
| Keystones | 24 | **PASS** |
| `common_trunk` | 26 ids, all resolve, ancestor-closed | **PASS** |
| All references resolve (prereqs, career tags, quest, capstone_prereqs, trunk) | no dangling | **PASS** |
| Acyclic; prereqs same-tier-or-earlier; every non-tier-0 node has ≥1 prereq | — | **PASS** |
| Fan-in ≤2 | sole exception `t5-research-project` = 3 | **PASS** (only violation is the sanctioned one) |
| Quest nodes | 9, all `check: "single-shot"`, matching career `quest` ids | **PASS** |
| `sel-contribution` | tier 1, prereqs `["sel-selfcare"]`, cluster, check B, **zero consumers** | **PASS** — zero consumers confirmed and confirmed *intended*: the card itself rules "NO consumers and never gates desk work — the standing life-stratum ruling" |
| Counted bridges (framework §6 definition + exclusion lists) | exactly `lit-letter-knowledge → mot-letter-formation`, `mot-letter-formation → log-sudoku-symbols` | **PASS** |
| Scoped boss rule (no tier-0–3 non-numeracy branch node with a boss in ancestry) | none | **PASS** |
| `check`-field values valid (A/B/single-shot/mixed/absent) | all valid | **PASS** |
| Longest cross-tier spine, tiers 0–3 (invariant 5) | 9 | **PASS** |
| TR6: every career's closure ∪ trunk reaches ≥3 tier-0 roots in ≥3 domains | all 9 careers | **PASS** |

**All mechanical checks pass. The three data sources are v1.7-identical.**

---

## Part 3 — CR19 vs. the shipped app: consistency verdict

Checked `curriculum/skill-tree-template.html` (884 lines, read in full) and the built `skill-tree.html` (behavior identical; same `STATES`, same career summary, same DATA).

**What conforms (and it includes the blocking item):**

- **Clause 1 (additive palette) — CONFORMS.** Exactly two markable states (`learning`, `mastered`); unmarked renders neutral card-color with legend text "not started yet"; no red skill state exists in CSS, state list, or storage writes. The lone red-tinted color (`--todo`) survives only as the remove-person ✕ hover — an admin-action color, not a skill mark; the code comments the intent on both counts ("deliberately NO negative/red state a child could see"). The blocking finding of all three reviews is genuinely fixed in the shipped code, not just the charter.
- **Clause 4, partially — CONFORMS on:** no whole-tree "X/109," no per-era percent, no notifications, no visible session timers, no cross-child grid (progress renders for one selected person at a time; the career-panel counts are static path sizes, not progress).
- **Clause 5 — trivially CONFORMS** (no decay logic exists).
- **Clause 6 — CONFORMS:** states are hand-set taps, exactly the accepted v1 simplification the clause states.

**What conflicts (flagged honestly, per the sweep's question):**

1. **The career-tab progress bar and counts CONFLICT with CR19 clause 4 — and with clause 3's "never as progress bars."** `renderCareerSummary()` shows, for the selected child and career: "*{name}: N mastered · N learning · N ahead*" plus a two-segment bar whose widths are `(m / core.length * 100)%` and `(l / core.length * 100)%`. That is a fraction toward a career rendered visually, plus per-career mastered counts against a stated path total ("{core.length} path skills") — the "X of N mastered" and "% toward a career" forms clause 4 bans verbatim, on a surface clause 1 rules "assumed child-visible regardless of view flags." Mitigations are real (additive green/amber on neutral, soft "ahead" language, appears only after actively selecting a person and a career) and the deficit-display harm the blocking finding targeted is absent — but the charter bans the *mechanism*, grants this no exemption, and demonstrates with clause 6 that it knows how to state an accepted deviation when one is intended. **Severity: MAJOR.** Repair is one of: (a) remove the bar and counts, or replace with the charter-sanctioned form (capability statements / frontier view); (b) gate them behind an explicit parent view *and* amend CR19, which currently forecloses view-flag defenses; or (c) amend CR19 with a stated clause-6-style v1 deviation. As shipped, charter and app disagree and neither says so.

2. **The Overview default view CONFLICTS with CR19 clause 3.** The app's default tab renders the full internal DAG — all six tiers, all 109 nodes, all 137 edges, side by side with the nine career cards — with no era scoping, no sealed scrolls, no frontier. Clause 3 rules the exact opposite for "any digital family surface" (era-scoped default, tiers beyond current+1 as sealed scrolls, "the internal DAG never shown to the child… applies to screens too"), naming the app's natural affordances as the Khan free-roam anti-pattern. Under clause 1's shoulder-surfing standard the parent-tool defense is unavailable as written. **Severity: MAJOR** (same repair menu as issue 1; a child-mode/parent-mode split *plus* a CR19 amendment acknowledging it would be the cheapest honest resolution, since JPN APP-1's own fix language — "child mode = poster metaphor, parent mode = full tree, alone" — offers the pattern CR19 chose not to adopt).

**Net verdict on the sweep's question:** the charter matches the shipped app on the palette (the blocking issue — fully consistent) and on hand-set states; it does **not** match on the career-tab progress bar/counts or the full-map default view. The claim "no aggregates pushed at children beyond the career-tab progress bar" is accurate as a description of the app — and that one remaining aggregate is precisely the one CR19 clause 4 prohibits.

---

## Part 4 — Everything missing or damaged, with severity

| # | Severity | Item | Detail / fix |
|---|---|---|---|
| 1 | **MAJOR** | Career-tab progress bar + mastered counts vs. CR19 clauses 3–4 | Part 3, conflict 1. `skill-tree-template.html` `renderCareerSummary()` (template ~lines 763–784; built file ~3272–3293) |
| 2 | **MAJOR** | Full-DAG default Overview vs. CR19 clause 3 | Part 3, conflict 2. Structural; predates the charter, but the charter binds "any digital family surface, current or future" without a stated deviation |
| 3 | **MODERATE** | App tier subtitles contradict CR14's grade anchoring | `TIER_META` labels tier 1 "school year 1," tier 2 "school year 2," tier 3 "school year 3" — the pre-CR14 one-year-ahead labeling both documents corrected in loop 1 (tier 1 = koolieelik/final kindergarten year; tiers 2–3 = school years 1–2). Age bands are right; the school-year phrasing is wrong on the family's actual surface. One-line fix in `TIER_META` (template line ~299–306) + rebuild |
| 4 | **MINOR** | `learning-path.md` Status line still opens "**Status:** v1.6, designed 2026-08-30…" | Title says v1.7 and the changelog covers v1.7, but the leading version token wasn't bumped (framework's parallel line correctly says v1.7). Cosmetic; one token |
| 5 | **TRIVIAL** | Dead `s-notlearned` residue in `applyStates()` | `classList.remove(..., "s-notlearned")` survives in template (line 597) and built file (3106) with no CSS and no setter — harmless scrub of the removed red state. Note: a stale `"not-learned"` value carried over in an old board's storage would render a literal "undefined" state mark (`STATE_MARK[st]` unguarded); worth a one-line guard whenever the file is next touched |

Nothing in either governing document is missing or damaged: every landmark named in the v1.7 changelogs exists at its claimed location, every census is exact, no v1.6 machinery was broken by the edit (bridge list, boss scoping, trunk closure, tier-0 exception, keystone set, check-field taxonomy, sourcing notes all intact), and the graph's one addition (`sel-contribution` + its single intra-branch edge) lands exactly as declared.

---

## Bottom line

The v1.7 edit is a faithful, complete implementation of the three international reviews at document level — 42/42 findings, with the three deliberate honest-deviation rulings (CR19 clause 6, §4.4 note 6) correctly stated rather than papered over — and the graph is mechanically sound and identical across all three data sources. The open work is entirely on the app side: the CR19 charter as written is stricter than the shipped app on aggregates (career progress bar) and view scoping (full-map default), and the app's tier subtitles still carry the pre-CR14 grade labels. Either the app moves to the charter or CR19 gains stated v1 deviations for those two clauses; today the two artifacts disagree silently, which is the one pattern this project's own doctrine consistently refuses.
