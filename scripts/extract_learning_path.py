"""Extract the machine-readable JSON block from curriculum/learning-path.md,
validate the graph, and write curriculum/learning-path.json."""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MD = ROOT / "curriculum" / "learning-path.md"
OUT = ROOT / "curriculum" / "learning-path.json"

text = MD.read_text(encoding="utf-8")
blocks = re.findall(r"```json\s*\n(.*?)\n```", text, flags=re.S)
if not blocks:
    sys.exit("no ```json block found in learning-path.md")
data = json.loads(blocks[-1])

nodes = {n["id"]: n for n in data["nodes"]}
careers = {c["id"]: c for c in data["careers"]}
errors = []

for n in data["nodes"]:
    for p in n.get("prereqs", []):
        if p not in nodes:
            errors.append(f"node {n['id']}: unknown prereq {p}")
    for c in n.get("careers", []):
        if c not in careers:
            errors.append(f"node {n['id']}: unknown career {c}")
    if n["tier"] != 0 and not n.get("prereqs"):
        errors.append(f"node {n['id']}: tier {n['tier']} but no prereqs")

# cycle check via DFS
state = {}
def visit(nid, stack):
    if state.get(nid) == 1:
        errors.append(f"cycle: {' -> '.join(stack + [nid])}")
        return
    if state.get(nid) == 2:
        return
    state[nid] = 1
    for p in nodes[nid].get("prereqs", []):
        if p in nodes:
            visit(p, stack + [nid])
    state[nid] = 2

for nid in nodes:
    visit(nid, [])

# reachability: every career must be fed by at least one node chain from tier 0
fed = {c: False for c in careers}
def reaches_tier0(nid, seen):
    n = nodes[nid]
    if n["tier"] == 0:
        return True
    return any(reaches_tier0(p, seen) for p in n.get("prereqs", []) if p in nodes and p not in seen and not seen.add(p))

for n in data["nodes"]:
    for c in n.get("careers", []):
        if c in fed:
            fed[c] = True
for c, ok in fed.items():
    if not ok:
        errors.append(f"career {c}: no node feeds it")

tiers = sorted({n["tier"] for n in data["nodes"]})
print(f"nodes: {len(nodes)}, careers: {len(careers)}, tiers: {tiers}")
print(f"domains: {sorted({n['domain'] for n in data['nodes']})}")
if errors:
    print("VALIDATION ERRORS:")
    for e in errors:
        print(" -", e)
    sys.exit(1)

OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"OK -> {OUT}")
