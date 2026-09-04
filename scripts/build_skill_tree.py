"""Inject curriculum/learning-path.json into the skill-tree template.

Outputs the same app twice:
- curriculum/skill-tree.html  (artifact preview / local use)
- public/index.html           (served by Vercel next to the /api functions)
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
tpl = (ROOT / "curriculum" / "skill-tree-template.html").read_text(encoding="utf-8")
data = (ROOT / "curriculum" / "learning-path.json").read_text(encoding="utf-8")
assert "__DATA__" in tpl
out = tpl.replace("__DATA__", data)
(ROOT / "curriculum" / "skill-tree.html").write_text(out, encoding="utf-8")
(ROOT / "public").mkdir(exist_ok=True)
(ROOT / "public" / "index.html").write_text(out, encoding="utf-8")
print(f"built curriculum/skill-tree.html and public/index.html ({len(out)} chars)")
