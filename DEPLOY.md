# Deploying the Skill Tree to the internet (Vercel + Neon)

The app is one static page ([public/index.html](public/index.html)) plus four tiny serverless
functions in [api/](api/) that store people and progress in a Postgres database. Vercel hosts
both; Neon provides the database. Both free tiers are more than enough.

**~5 minutes, one time:**

1. **Import the repo into Vercel** — at https://vercel.com/new, choose the
   `kids-learning` GitHub repository → Deploy (no settings to change; `vercel.json`
   already points at `public/`).
2. **Add the database** — in the Vercel project: **Storage → Create Database → Neon**
   (choose an EU region, e.g. Frankfurt). This automatically sets the `DATABASE_URL`
   environment variable. Redeploy when prompted.
3. **Create the tables** — open `https://<your-app>.vercel.app/api/setup` once in the
   browser. It replies `{"ok":true,"message":"Schema ready."}` and is safe to call again.
4. **Open the app** — `https://<your-app>.vercel.app`. Add the first person; the app
   creates a board and puts its code in the URL (`?board=…`). **Share that exact link** —
   the board code in the URL is the key to your family's board. Anyone with the link can
   view and edit that board; anyone without it cannot find it.

Every push to the GitHub repo redeploys automatically.

## Data & privacy

- The database stores only: board codes, the names people enter, and per-skill states
  (mastered / learning / not learned). No accounts, no e-mails, no tracking.
- Use **first names or nicknames** — especially for children.
- Deleting a person (✕ on their chip) removes their progress permanently.
- A lost board link cannot be recovered from inside the app — bookmark it. (It can be
  looked up in the Neon console's `boards` table if ever needed.)

## Without deployment

The same page works anywhere (open the file, GitHub Pages, the Claude artifact) — it then
saves progress **in that browser only** and shows "💾 saving on this device only" in the
header. The shared board needs the Vercel deployment.

## Local development

```bash
python scripts/extract_learning_path.py   # refresh graph JSON from learning-path.md
python scripts/build_skill_tree.py        # rebuild curriculum/skill-tree.html + public/index.html
```
