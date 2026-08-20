from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {
    "## Table of contents",
    "## Keywords and terms",
    "## Topics",
    "## Worked example",
    "## Execution trace",
    "## Prediction experiment",
    "## Broken example and repair",
    "## Guided practice before independent work",
    "## Project application",
    "## Independent exercises",
    "## References",
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def lessons() -> list[Path]:
    return sorted(
        (p for p in ROOT.iterdir() if p.is_dir() and re.fullmatch(r"day_\d{3}_.+", p.name)),
        key=lambda p: int(p.name.split("_", 2)[1]),
    )


def check() -> list[str]:
    errors: list[str] = []
    paths = lessons()
    if len(paths) != 61:
        errors.append(f"expected 60 lessons, found {len(paths)}")
    if [int(p.name.split("_", 2)[1]) for p in paths] != list(range(1, 62)):
        errors.append("lesson numbering is not exactly day_001 through day_060")
    for path in paths:
        lesson = path / f"{path.name}.md"
        if not lesson.exists():
            errors.append(f"missing lesson file: {lesson.relative_to(ROOT)}")
            continue
        text = lesson.read_text(encoding="utf-8")
        for heading in REQUIRED:
            if heading not in text:
                errors.append(f"{lesson.relative_to(ROOT)} missing {heading}")
        if len(text.split()) < 900:
            errors.append(f"{lesson.relative_to(ROOT)} is too short for the lesson contract")
        if len(re.findall(r"^\d+\. ", text, flags=re.MULTILINE)) < 12:
            errors.append(f"{lesson.relative_to(ROOT)} needs 12 numbered exercises")
        toc_start = text.find("## Table of contents")
        toc_end = text.find("\n## ", toc_start + 4)
        toc = text[toc_start : toc_end if toc_end != -1 else len(text)]
        headings = {slug(match.group(1)) for match in re.finditer(r"^##?#? (.+)$", text, flags=re.MULTILINE)}
        for anchor in re.findall(r"\]\(#([^)]+)\)", toc):
            if anchor not in headings:
                errors.append(f"{lesson.relative_to(ROOT)} has broken TOC anchor #{anchor}")
        for required in ("practice/exercises.md", "practice/hints.md", "practice/solutions.md"):
            if not (path / required).exists():
                errors.append(f"{path.relative_to(ROOT)}/{required} is missing")
    index = ROOT / "DAY_INDEX.md"
    if not index.exists():
        errors.append("missing DAY_INDEX.md")
    else:
        days = [int(n) for n in re.findall(r"^\| (\d{3}) \|", index.read_text(encoding="utf-8"), flags=re.MULTILINE)]
        if days != list(range(1, 62)):
            errors.append("DAY_INDEX.md is not numerically complete")
    return errors


errors = check()
if errors:
    print("Course check failed:")
    print("\n".join(f"- {error}" for error in errors))
    raise SystemExit(1)
print("Course check passed: 61 sortable lessons, structured sections, TOCs, and practice files are present.")
