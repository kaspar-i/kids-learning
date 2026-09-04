# Product strategy — families beyond ours, and the selling question

Date: 2026-09-04 · Status: accepted (stages B/C are signal-gated, not scheduled)
Method: software-project-playbook business-analysis brief — the dominant uncertainty here is
**value** ("would other families use/pay for this?"), and analysis cannot answer a value
question; only observed behavior can. So this document names cheap behavioral tests and the
architecture stage each result unlocks — it deliberately does not "architect for scale" first.
Base rate to stay honest about: roughly two-thirds of well-designed product ideas fail their
own metric (Kohavi). Treat every claim below as a hypothesis with a test, ours included.

## 1. How different families use it — TODAY, with zero new code

The capability-link model already multi-tenants: **every family that opens the bare URL and
adds a person gets their own private board** (unguessable code in the link; no accounts).
Our family's board, the neighbors', a homeschool family in Canada — same deployment,
separate boards, zero marginal cost.

| Persona | How they'd use it | What they'd need that we lack |
|---|---|---|
| Our family (core) | Weekly ritual: open link, child marks with parent (CR19) | Nothing — live now |
| Extended family (grandparents) | View the child's board from their own device | Nothing — share the link |
| Estonian families | Same as us | **Estonian UI translation** (the curriculum already is Estonia-aware) |
| Homeschool families (intl.) | Board + the booklet/poster pipeline as their spine | Printable booklet packs; curriculum docs are already public |
| Tutors / after-school clubs | One board per student group | Board naming; many-board management |
| Kindergarten teachers | Class board (~20 names) | Same + would trip the data-protection cliff below (children at scale, institutional) |

## 2. The selling question — three hypotheses, ranked by evidence-fit

**H1 (best risk/reward): sell the CONTENT, not the app.** Printable booklet packs (Animal
Sudoku 1a/1b exists; the framework specifies a whole ladder + poster), sold via
Gumroad/Etsy-style checkout. Why first: real willingness-to-pay signal at a real price
(the Mom-Test "commitment"), **zero personal data held about strangers' children** (no
GDPR cliff), and it funnels buyers to the free board link. The curriculum's research trail
(5 review loops, FI/SG/JP critics) is a genuine differentiator no printable-worksheet shop has.

**H2: hosted family boards, freemium.** Free: one board. Paid (~€3–5/mo): several boards,
board naming, progress history/export. Only worth building after H1 or organic board
creation shows demand — because paid strangers' boards trigger Stage C obligations below.

**H3: institutional (lasteaed/school class boards).** Largest revenue per deal, heaviest
obligations (children's data at institutional scale, procurement, Estonian public-sector
expectations). Only pursue on inbound pull, never speculatively.

**Kill criterion (60 days after sharing the link outside the family):** fewer than 5
external families create a board AND return in week 2, and fewer than 10 booklet-pack
sales at a real price → the selling hypothesis dies; the product remains our family tool +
public repo, which is already a full success. (Compliments and "I'd totally use this" count
as noes; only boards, return visits, and payments count.)

**The behavioral test script** (Mom Test, for 5–10 parent conversations): ask what they
currently do to track their child's learning (past behavior, not opinions); what they last
paid for in this space (workbooks? apps? tutoring?); end by offering the link or a paid
booklet pack and record what they actually DO.

## 3. Architecture by stage (each stage bought by a named signal)

**Stage A — now (LIVE).** Static page + 4 serverless functions + Neon. Board = capability
link. Additive marking (CR19). Multi-family via separate boards. Data held: board codes,
entered names, skill states. Cost: €0.

**Stage B — "shared beyond the household"** (signal: >~20 external boards, or first
Estonian family asks for eesti keel, or any abuse). Still no accounts:
- Estonian/English UI toggle (strings are already centralized in the template)
- Board display-name + simple board-recovery sheet (print/QR of the link)
- Rate limit on board/person creation (one function edit); `/api/stats` counter
  (boards created / boards active in 30 days) — the closed-loop usage audit the playbook
  says almost nobody does
- A plain-language privacy page (what's stored, how to delete)
- H1 needs none of this — booklet sales are a separate checkout page.

**Stage C — commercial app (H2/H3)** (signal: real payments or institutional pull; never
speculative). This is the step that re-tiers the data component (strangers' minors → T2):
- Accounts via a managed auth provider (never hand-rolled) with parent-owned family spaces
- Billing via a merchant-of-record (Paddle-style — handles EU VAT for a solo operator)
- GDPR package: privacy policy, processor agreements (Vercel/Neon), export + delete
  endpoints, retention rule, breach process; children's data entered by parents under
  parental consent, minimal by design (keep the no-email-for-kids rule)
- Only then: board history, multi-board admin, teacher views.

**Non-goals at every stage until a signal says otherwise:** native apps, notifications
(CR19 bans them child-facing anyway), analytics SDKs, social features, AI features.

## 4. Who decides and when it's reviewed

Owner: Kaspar. Review: 90 days after first external sharing — compare boards
created/retained and packs sold against the kill criterion, then explicitly kill, hold, or
fund Stage B/C. (The planned-vs-achieved check is the one practice the evidence most
supports and organizations most skip.)
