#!/usr/bin/env python3
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

RA_VERSION = "0.6.6"
ROOT = Path(__file__).resolve().parent.parent


def walk_files(skip_team_skills: bool = False):
    for current, directories, filenames in os.walk(ROOT):
        relative = Path(current).relative_to(ROOT)
        directories[:] = [
            name for name in directories
            if name not in {".git", "node_modules"}
            and not (skip_team_skills and relative == Path("Ego") and name == "TeamSkill")
            and not (skip_team_skills and relative == Path(".agents") and name == "skills")
        ]
        for filename in filenames:
            yield relative / filename


def main() -> int:
    failures = []
    agents = ROOT / "AGENTS.md"
    if not agents.is_file():
        failures.append("AGENTS.md is missing in the repository root")
    elif agents.stat().st_size > 32768:
        failures.append("AGENTS.md is larger than 32 KiB")

    github = ROOT / ".github"
    if (github / "copilot-instructions.md").exists():
        failures.append(".github/copilot-instructions.md must not exist")
    if (github / "instructions").is_dir():
        failures.append(".github/instructions/ must not exist")

    for relative in walk_files():
        if relative.name == "AGENTS.md" and relative != Path("AGENTS.md"):
            failures.append(f"nested AGENTS.md found: {relative.as_posix()}")

    skills = ROOT / ".agents" / "skills"
    if skills.is_dir():
        for skill_dir in sorted(path for path in skills.iterdir() if path.is_dir()):
            skill_file = skill_dir / "SKILL.md"
            if not skill_file.is_file():
                failures.append(f"{skill_file.relative_to(ROOT).as_posix()} is missing")
                continue
            content = skill_file.read_text(encoding="utf-8")
            expected_name = skill_dir.name
            if not re.search(rf"^name: *{re.escape(expected_name)} *$", content, re.MULTILINE):
                failures.append(f"{skill_file.relative_to(ROOT).as_posix()}: name must be {expected_name}")
            description = re.search(r"^description: *(.*)$", content, re.MULTILINE)
            if not description or not description.group(1):
                failures.append(f"{skill_file.relative_to(ROOT).as_posix()}: description is missing")
            elif len(description.group(1)) > 1024:
                failures.append(f"{skill_file.relative_to(ROOT).as_posix()}: description is longer than 1024 characters")

    if not (ROOT / "Ego" / "RAP.md").is_file():
        failures.append("Ego/RAP.md is missing")

    for relative in walk_files(skip_team_skills=True):
        if relative.name == "SKILL.md":
            failures.append(f"SKILL.md outside .agents/skills and Ego/TeamSkill: {relative.as_posix()}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print(f"RA仓规 {RA_VERSION}: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
