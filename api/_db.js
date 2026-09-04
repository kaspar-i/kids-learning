import { neon } from "@neondatabase/serverless";

// Lazy init: a missing DATABASE_URL must surface as a readable JSON error
// from the handlers' catch blocks, not crash the function at module load.
let _sql = null;
function getSql() {
  if (!process.env.DATABASE_URL) {
    throw new Error(
      "DATABASE_URL is not set. In Vercel: Storage -> open the Neon store -> Connect Project -> kids-learning (all environments), then redeploy."
    );
  }
  if (!_sql) _sql = neon(process.env.DATABASE_URL);
  return _sql;
}
export const sql = (...args) => getSql()(...args);

export function readBody(req) {
  if (req.body && typeof req.body === "object") return req.body;
  try { return JSON.parse(req.body || "{}"); } catch { return {}; }
}

export const okCode = (c) => typeof c === "string" && /^[A-Za-z0-9_-]{6,40}$/.test(c);
export const okId = (s, max = 200) => typeof s === "string" && s.length > 0 && s.length <= max;
export const STATES = ["mastered", "learning"];
