# ADR 001 — Hosting and storage for the progress-tracking app

Date: 2026-09-04 · Status: accepted

## Context

The skill-tree viewer becomes a multi-user app: named people mark skills
mastered / learning / not-learned, progress must be shared across devices and people, and
the owner asked for it to be on GitHub and available from the internet. Project tier
(software-project-playbook): **T1** — one accountable human, failure cost is a family's
checkmarks, maintenance horizon is years, and the data includes **children's first names**,
which sets the data-minimalism constraints below even at family scale.

## Decision

- **Repo**: public GitHub repository (owner's explicit request), app + curriculum + docs together.
- **Hosting**: Vercel serving the static page from `public/` and four serverless functions
  from `api/`. **Database**: Neon Postgres via the Vercel integration.
- **Access model**: capability URL — an unguessable board code in the link, no accounts.
- **Data minimalism** (the minors-data floor): store only board code, entered names
  (nicknames encouraged), per-skill states. No e-mail, no auth provider, no analytics.
- **Degradation**: the page probes `api/ping`; without an API it falls back to
  localStorage (per-device), so the artifact preview and any static host still work.

## Alternatives rejected

- **Claude artifact `db` capability**: zero infra, but declaring `db` makes the artifact
  organization-internal — people outside the owner's Claude organization could not use it.
  Fails the "available from internet" requirement. Kept as design preview only.
- **GitHub Pages alone**: no backend → no shared board. Fails the requirement.
- **Supabase (DB+API in one)**: viable, but anon-key + RLS policy design is more security
  surface than four parameterized-SQL functions; owner already knows Vercel+Neon (kummihai).
- **Auth/accounts**: complexity with no buyer at family scale; the board code is the
  capability. Revisit only on an observed signal (abuse, or strangers' boards at scale —
  which would also trigger a GDPR/consent review, see playbook Q6).
