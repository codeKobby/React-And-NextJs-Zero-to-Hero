from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
rows: list[tuple[int, str, str]] = []
for folder in ROOT.iterdir():
    match = re.fullmatch(r"day_(\d{3})_(.+)", folder.name)
    if not folder.is_dir() or not match:
        continue
    day = int(match.group(1))
    lesson_path = folder / f"{folder.name}.md"
    first_heading = lesson_path.read_text(encoding="utf-8").splitlines()[0]
    title = re.sub(r"^# Day \d{3}: ", "", first_heading)
    rows.append((day, title, f"{folder.name}/{lesson_path.name}"))
rows.sort()
lines = [
    f"# {max((row[0] for row in rows), default=0)}-day course index",
    "",
    "> **Start here:** if you are new to programming or to React, read the [course README](README.md), complete the [setup guide](SETUP.md), and inspect the [examples guide](examples/README.md) before opening Day 001.",
    "",
    "Each lesson uses three-digit numbering so alphabetical file browsing remains chronological. Follow the lessons in order. Every lesson links back to the README, setup guide, examples, and this index.",
    "",
    "| Learning aid | Link |",
    "| --- | --- |",
    "| Course map and learning loop | [README.md](README.md) |",
    "| Install Node.js, VS Code, and extensions | [SETUP.md](SETUP.md) |",
    "| Choose the React or Next.js starter | [examples/README.md](examples/README.md) |",
    "| Teaching contract | [LESSON_STANDARD.md](LESSON_STANDARD.md) |",
    "",
    "| Day | Lesson |",
    "| ---: | --- |",
]
for day, title, path in rows:
    lines.append(f"| {day:03d} | [{title}]({path}) |")
(ROOT / "DAY_INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"Indexed {len(rows)} lessons.")
