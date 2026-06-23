#!/usr/bin/env python3
"""Expand collapsed YAML folded scalars in the apex-kb skill package.

The repair is deterministic and package-local. It only rewrites lines shaped as:

  key: >    sentence part    sentence part

into parseable folded scalar form:

  key: >
    sentence part
    sentence part
"""

from __future__ import annotations

import datetime as dt
import re
import shutil
from pathlib import Path


ROOT = Path(".claude/skills/apex-kb")
BACKUP_ROOT = Path(".repair-backups/apex-kb-folded-scalar-repair")
PATTERN = re.compile(r"^(?P<indent>\s*)(?P<key>[A-Za-z_][A-Za-z0-9_]*): >\s{4,}(?P<body>\S.*)$")


def expand_line(line: str) -> list[str]:
    match = PATTERN.match(line)
    if not match:
        return [line]
    indent = match.group("indent")
    key = match.group("key")
    body = match.group("body").rstrip()
    parts = [part.strip() for part in re.split(r"\s{4,}", body) if part.strip()]
    return [f"{indent}{key}: >"] + [f"{indent}  {part}" for part in parts]


def repair_text(text: str) -> str:
    out: list[str] = []
    changed = False
    for line in text.splitlines():
        replacement = expand_line(line)
        if replacement != [line]:
            changed = True
        out.extend(replacement)
    if not changed:
        return text.rstrip() + "\n"
    return "\n".join(out).rstrip() + "\n"


def main() -> int:
    if not ROOT.exists():
        raise SystemExit(f"Missing package root: {ROOT}")
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    backup_root = BACKUP_ROOT / stamp
    changed: list[Path] = []
    for path in sorted(ROOT.rglob("*.md")):
        old = path.read_text(encoding="utf-8")
        new = repair_text(old)
        if old != new:
            dest = backup_root / path
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, dest)
            path.write_text(new, encoding="utf-8", newline="\n")
            changed.append(path)
    print(f"changed_files: {len(changed)}")
    for path in changed:
        print(path.as_posix())
    if changed:
        print(f"backup_path: {backup_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
