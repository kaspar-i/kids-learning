import crypto from "node:crypto";
import { sql, readBody, okCode, okId } from "./_db.js";

export default async function handler(req, res) {
  try {
    if (req.method === "POST") {
      const { code, name } = readBody(req);
      if (!okCode(code) || !okId(name, 30)) return res.status(400).json({ error: "bad input" });
      const board = await sql`select code from boards where code = ${code}`;
      if (!board.length) return res.status(404).json({ error: "no such board" });
      const id = "p" + crypto.randomBytes(6).toString("base64url");
      await sql`insert into people (id, board_code, name) values (${id}, ${code}, ${name.trim().slice(0, 30)})`;
      return res.status(200).json({ id });
    }
    if (req.method === "DELETE") {
      const { code, id } = req.query;
      if (!okCode(code) || !okId(id, 40)) return res.status(400).json({ error: "bad input" });
      await sql`delete from people where id = ${id} and board_code = ${code}`;
      return res.status(200).json({ ok: true });
    }
    res.status(405).json({ error: "method not allowed" });
  } catch (e) {
    res.status(500).json({ error: String(e.message || e) });
  }
}
