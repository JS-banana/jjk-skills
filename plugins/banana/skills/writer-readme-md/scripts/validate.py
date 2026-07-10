#!/usr/bin/env python3
"""Validate the writer-readme-md skill package or a generated README."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_REFERENCES = [
    "references/method.md",
    "references/patterns.md",
    "references/review-rubric.md",
    "references/badges.md",
    "references/examples.md",
]

FORBIDDEN_SKILL_FILES = [
    "references/README-anatomy.md",
    "references/badge-catalog.md",
    "references/project-patterns.md",
    "references/scoring-rubric.md",
    "references/writing-principles.md",
    "assets/templates/brand-focused.md",
    "assets/templates/complete-manual.md",
    "assets/templates/minimal-facade.md",
    "assets/templates/operation-manual.md",
    "assets/templates/standard-framework.md",
    "assets/templates/cli.md",
    "assets/templates/library.md",
    "assets/templates/web-app.md",
    "assets/templates/service.md",
    "assets/templates/personal-tool.md",
    "assets/templates/monorepo.md",
]

PLACEHOLDER_PATTERNS = [
    r"\{\{[^}]+\}\}",
    r"\{owner\}",
    r"\{repo\}",
    r"\bOWNER\b",
    r"\bREPO\b",
    r"\buser/repo\b",
    r"\bTODO\b",
    r"\bFIXME\b",
    r"Project Name",
]

REQUIRED_OPENAI_INTERFACE = [
    "display_name",
    "short_description",
    "default_prompt",
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_frontmatter(content: str) -> dict[str, str] | None:
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return None
    data: dict[str, str] = {}
    key = None
    buffer: list[str] = []
    for line in match.group(1).splitlines():
        if re.match(r"^[a-zA-Z0-9_-]+:\s*", line):
            if key:
                data[key] = "\n".join(buffer).strip()
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            if value in {">", "|"}:
                buffer = []
            else:
                buffer = [value.strip('"')]
        elif key:
            buffer.append(line.strip())
    if key:
        data[key] = " ".join(part for part in buffer if part).strip()
    return data


def unquote_yaml_value(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def parse_simple_yaml_sections(content: str) -> dict[str, dict[str, str]]:
    sections: dict[str, dict[str, str]] = {}
    current: str | None = None
    for raw_line in content.splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        section = re.match(r"^([A-Za-z0-9_-]+):\s*$", raw_line)
        if section:
            current = section.group(1)
            sections.setdefault(current, {})
            continue
        item = re.match(r"^\s+([A-Za-z0-9_-]+):\s*(.+?)\s*$", raw_line)
        if current and item:
            sections[current][item.group(1)] = unquote_yaml_value(item.group(2))
    return sections


def validate_openai_yaml(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    openai_yaml = skill_dir / "agents/openai.yaml"
    if not openai_yaml.exists():
        return ["missing agents/openai.yaml"]

    sections = parse_simple_yaml_sections(read(openai_yaml))
    if "openai" in sections:
        errors.append("agents/openai.yaml must use top-level interface:, not openai:")
    interface = sections.get("interface")
    if interface is None:
        errors.append("agents/openai.yaml missing top-level interface:")
        return errors

    for key in REQUIRED_OPENAI_INTERFACE:
        if not interface.get(key):
            errors.append(f"agents/openai.yaml missing interface.{key}")

    short_description = interface.get("short_description", "")
    if short_description and not (25 <= len(short_description) <= 64):
        errors.append("agents/openai.yaml interface.short_description must be 25-64 characters")

    default_prompt = interface.get("default_prompt", "")
    if default_prompt and "$writer-readme-md" not in default_prompt:
        errors.append("agents/openai.yaml interface.default_prompt must mention $writer-readme-md")

    return errors


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return ["missing SKILL.md"]

    content = read(skill_md)
    frontmatter = extract_frontmatter(content)
    if not frontmatter:
        errors.append("SKILL.md frontmatter is missing or invalid")
    else:
        name = frontmatter.get("name", "")
        description = frontmatter.get("description", "")
        if name != "writer-readme-md":
            errors.append("SKILL.md name must be writer-readme-md")
        if "Use when" not in description:
            errors.append("description must include trigger wording")
        if len(description) > 1024:
            errors.append("description exceeds 1024 characters")
        if "<" in description or ">" in description:
            errors.append("description must not contain angle brackets")

    lines = content.splitlines()
    if len(lines) > 110:
        errors.append(f"SKILL.md is too long ({len(lines)} lines; target <= 110)")

    required_mentions = REQUIRED_REFERENCES + ["scripts/validate.py"]
    for rel in required_mentions:
        if rel not in content:
            errors.append(f"SKILL.md does not mention {rel}")

    for rel in REQUIRED_REFERENCES:
        if not (skill_dir / rel).exists():
            errors.append(f"missing required file: {rel}")

    for rel in FORBIDDEN_SKILL_FILES:
        if (skill_dir / rel).exists():
            errors.append(f"obsolete file still present: {rel}")

    errors.extend(validate_openai_yaml(skill_dir))

    return errors


def markdown_headings(content: str) -> list[tuple[int, str]]:
    headings: list[tuple[int, str]] = []
    in_block = False
    for line in content.splitlines():
        if re.match(r"^```", line):
            in_block = not in_block
            continue
        if in_block:
            continue
        match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if match:
            headings.append((len(match.group(1)), match.group(2)))
    html_h1 = re.findall(r"<h1[^>]*>(.*?)</h1>", content, flags=re.IGNORECASE | re.DOTALL)
    headings.extend((1, re.sub(r"<.*?>", "", h).strip()) for h in html_h1)
    return headings


def code_block_languages(content: str) -> tuple[int, int]:
    total = 0
    with_lang = 0
    in_block = False
    for line in content.splitlines():
        match = re.match(r"^```([^\s`]*)\s*$", line)
        if not match:
            continue
        if in_block:
            in_block = False
            continue
        total += 1
        if match.group(1):
            with_lang += 1
        in_block = True
    return total, with_lang


def relative_refs(content: str) -> list[str]:
    refs: list[str] = []
    patterns = [
        r"!\[[^\]]*\]\(([^)]+)\)",
        r"\[[^\]]+\]\(([^)]+)\)",
        r"src=[\"']([^\"']+)[\"']",
    ]
    for pattern in patterns:
        refs.extend(re.findall(pattern, content))
    result = []
    for ref in refs:
        clean = ref.split()[0].strip("<>")
        if re.match(r"^(https?:|mailto:|#)", clean):
            continue
        if clean.startswith("data:"):
            continue
        result.append(clean.split("#", 1)[0])
    return [ref for ref in result if ref]


def validate_readme(readme: Path) -> list[str]:
    errors: list[str] = []
    content = read(readme)
    headings = markdown_headings(content)
    h1_count = sum(1 for level, _ in headings if level == 1)
    if h1_count != 1:
        errors.append(f"expected exactly one H1, found {h1_count}")

    total_blocks, with_lang = code_block_languages(content)
    if total_blocks and with_lang < total_blocks:
        errors.append("some fenced code blocks lack language identifiers")

    for pattern in PLACEHOLDER_PATTERNS:
        if re.search(pattern, content):
            errors.append(f"placeholder or sample token remains: {pattern}")

    broken: list[str] = []
    for ref in relative_refs(content):
        if not (readme.parent / ref).exists():
            broken.append(ref)
    if broken:
        errors.append("broken relative references: " + ", ".join(sorted(set(broken))))

    if re.search(r"img\.shields\.io/.+(\{|\}|OWNER|REPO|user/repo)", content):
        errors.append("badge contains unresolved owner/repo placeholder")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill", type=Path, help="Skill directory to validate")
    parser.add_argument("--readme", type=Path, help="README file to validate")
    args = parser.parse_args()

    if not args.skill and not args.readme:
        args.skill = Path(__file__).resolve().parents[1]

    errors: list[str] = []
    if args.skill:
        errors.extend(f"skill: {e}" for e in validate_skill(args.skill.resolve()))
    if args.readme:
        errors.extend(f"readme: {e}" for e in validate_readme(args.readme.resolve()))

    if errors:
        for error in errors:
            print(f"FAIL {error}")
        return 1

    target = []
    if args.skill:
        target.append("skill")
    if args.readme:
        target.append("readme")
    print("PASS " + " and ".join(target))
    return 0


if __name__ == "__main__":
    sys.exit(main())
