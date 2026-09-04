import { sql, readBody, okCode, okId, STATES } from "./_db.js";

export default async function handler(req, res) {
  try {
    if (req.method !== "POST") return res.status(405).json({ error: "method not allowed" });
    const { code, personId, nodeId, state } = readBody(req);
    if (!okCode(code) || !okId(personId, 40) || !okId(nodeId, 200)) {
      return res.status(400).json({ error: "bad input" });
    }
    if (state !== null && !STATES.includes(state)) return res.status(400).json({ error: "bad state" });

    // the person must belong to the board named by the capability code
    const person = await sql`select id from people where id = ${personId} and board_code = ${code}`;
    if (!person.length) return res.status(404).json({ error: "no such person on this board" });

    if (state === null) {
      await sql`delete from progress where person_id = ${personId} and node_id = ${nodeId}`;
    } else {
      await sql`insert into progress (person_id, node_id, state) values (${personId}, ${nodeId}, ${state})
        on conflict (person_id, node_id) do update set state = ${state}, updated_at = now()`;
    }
    res.status(200).json({ ok: true });
  } catch (e) {
    res.status(500).json({ error: String(e.message || e) });
  }
}
