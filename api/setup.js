// One-time (idempotent) schema bootstrap: open /api/setup once after connecting Neon.
import { sql } from "./_db.js";

export default async function handler(req, res) {
  try {
    await sql`create table if not exists boards (
      code text primary key,
      created_at timestamptz not null default now()
    )`;
    await sql`create table if not exists people (
      id text primary key,
      board_code text not null references boards(code) on delete cascade,
      name text not null,
      created_at timestamptz not null default now()
    )`;
    await sql`create table if not exists progress (
      person_id text not null references people(id) on delete cascade,
      node_id text not null,
      state text not null check (state in ('mastered','learning')),
      updated_at timestamptz not null default now(),
      primary key (person_id, node_id)
    )`;
    await sql`create index if not exists idx_people_board on people(board_code)`;
    res.status(200).json({ ok: true, message: "Schema ready." });
  } catch (e) {
    res.status(500).json({ ok: false, error: String(e.message || e) });
  }
}
