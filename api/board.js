import crypto from "node:crypto";
import { sql, okCode } from "./_db.js";

export default async function handler(req, res) {
  try {
    if (req.method === "POST") {
      const code = crypto.randomBytes(9).toString("base64url");
      await sql`insert into boards (code) values (${code})`;
      return res.status(200).json({ code });
    }
    if (req.method === "GET") {
      const code = req.query.code;
      if (!okCode(code)) return res.status(400).json({ error: "bad code" });
      const people = await sql`select id, name from people where board_code = ${code} order by created_at`;
      const rows = await sql`select p.id as person_id, pr.node_id, pr.state
        from people p join progress pr on pr.person_id = p.id
        where p.board_code = ${code}`;
      const progress = {};
      for (const r of rows) {
        (progress[r.person_id] = progress[r.person_id] || {})[r.node_id] = r.state;
      }
      return res.status(200).json({ people, progress });
    }
    res.status(405).json({ error: "method not allowed" });
  } catch (e) {
    res.status(500).json({ error: String(e.message || e) });
  }
}
