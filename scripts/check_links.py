from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []
for path in ROOT.rglob("*.md"):
    if any(part in {'.git', 'node_modules', '.next', 'dist', 'authored_lessons'} for part in path.parts):
        continue
    text = path.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^]]+\]\(([^)#]+)(?:#[^)]+)?\)", text):
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        target_path = (path.parent / target).resolve()
        if not target_path.exists():
            errors.append(f"{path.relative_to(ROOT)} -> {target}")
if errors:
    print("Broken Markdown links:")
    print("\n".join(errors))
    raise SystemExit(1)
print("Markdown link check passed.")
