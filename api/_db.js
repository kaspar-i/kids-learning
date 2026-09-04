import { neon } from "@neondatabase/serverless";

export const sql = neon(process.env.DATABASE_URL);

export function readBody(req) {
  if (req.body && typeof req.body === "object") return req.body;
  try { return JSON.parse(req.body || "{}"); } catch { return {}; }
}

export const okCode = (c) => typeof c === "string" && /^[A-Za-z0-9_-]{6,40}$/.test(c);
export const okId = (s, max = 200) => typeof s === "string" && s.length > 0 && s.length <= max;
export const STATES = ["mastered", "learning"];
