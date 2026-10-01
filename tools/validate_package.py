#!/usr/bin/env python3
"""Read-only package smoke checks. This does not validate animation quality."""

from __future__ import annotations

import ast
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "rig-motion-skill"
TEXT_SUFFIXES = {".md", ".py", ".json", ".yaml", ".yml"}


def main() -> int:
    problems: list[str] = []
    contents: dict[Path, str] = {}
    files = sorted(
        path for path in ROOT.rglob("*")
        if path.is_file() and ".git" not in path.relative_to(ROOT).parts
        and "__pycache__" not in path.relative_to(ROOT).parts
    )
    for path in files:
        if path.suffix not in TEXT_SUFFIXES:
            continue
        label = path.relative_to(ROOT).as_posix()
        try:
            source = path.read_text(encoding="utf-8")
            contents[path] = source
            if re.search(r"[\u0400-\u04ff]", source):
                problems.append(f"{label}: unexpected Cyrillic in English package")
            if path.suffix == ".py":
                ast.parse(source, filename=label)
            elif path.suffix == ".json":
                json.loads(source)
        except (UnicodeError, ValueError, SyntaxError) as exc:
            problems.append(f"{label}: {exc}")

    entry = contents.get(SKILL / "SKILL.md", "")
    frontmatter = re.match(r"\A---\n(.*?)\n---(?:\n|$)", entry, re.S)
    if not frontmatter:
        problems.append("SKILL.md: missing frontmatter")
    else:
        metadata = frontmatter.group(1)
        if not re.search(r"^name: rig-motion-skill$", metadata, re.M):
            problems.append("SKILL.md: name must match the installable folder")
        if not re.search(r"^description: .+", metadata, re.M):
            problems.append("SKILL.md: missing description")

    interface = contents.get(SKILL / "agents" / "openai.yaml", "")
    description = re.search(r'^\s+short_description: (".*")$', interface, re.M)
    if description:
        try:
            short = json.loads(description.group(1))
            if not 25 <= len(short) <= 64:
                problems.append("openai.yaml: short_description must be 25–64 characters")
        except ValueError as exc:
            problems.append(f"openai.yaml: invalid quoted description: {exc}")
    else:
        problems.append("openai.yaml: missing quoted short_description")

    references = set(SKILL.glob("references/*.md"))
    linked_references: set[Path] = set()
    local_links = 0
    for path, source in contents.items():
        if path.suffix != ".md":
            continue
        for match in re.finditer(r"!?\[[^\]\n]*\]\(([^)\n]+)\)", source):
            target = match.group(1).strip()
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            if target.startswith("#") or urlsplit(target).scheme:
                continue
            relative = unquote(target.split("#", 1)[0])
            destination = (path.parent / relative).resolve()
            local_links += 1
            if not destination.is_relative_to(ROOT) or not destination.exists():
                problems.append(f"{path.relative_to(ROOT)}: broken/outside local link {target}")
            if destination in references:
                linked_references.add(destination)
    for path in sorted(references - linked_references):
        problems.append(f"{path.relative_to(ROOT)}: reference has no incoming Markdown link")

    catalog = contents.get(SKILL / "references" / "sources.md", "")
    source_ids = re.findall(r"^\| ([A-Z]\d{2}) \|", catalog, re.M)
    if not source_ids or len(source_ids) != len(set(source_ids)):
        problems.append("sources.md: missing or duplicate source IDs")
    for image in SKILL.glob("assets/*.png"):
        if not image.read_bytes().startswith(b"\x89PNG\r\n\x1a\n"):
            problems.append(f"{image.relative_to(ROOT)}: invalid PNG signature")

    print(json.dumps({
        "skill_files": sum(path.is_relative_to(SKILL) for path in files),
        "reference_guides": len(references),
        "source_records": len(source_ids),
        "local_links_checked": local_links,
        "problems": problems,
        "scope": "Static packaging checks only; no application or artistic validation.",
    }, indent=2))
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
