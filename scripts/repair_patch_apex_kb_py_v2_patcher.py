#!/usr/bin/env python3
"""Deterministically repair the v2 apex_kb.py patcher regex anchors."""

from __future__ import annotations

from pathlib import Path


TARGET = Path("scripts/patch_apex_kb_py_v2_source_storage_and_epistemic_lint.py")


def main() -> int:
    text = TARGET.read_text(encoding="utf-8")
    replacements = {
        r'rf"^def {re.escape(name)}\\(.*?^def "': r'rf"^def {re.escape(name)}\(.*?^def "',
        r'rf"^def {re.escape(name)}\\(.*"': r'rf"^def {re.escape(name)}\(.*"',
    }
    for old, new in replacements.items():
        if old not in text:
            raise SystemExit(f"missing expected patcher pattern: {old}")
        text = text.replace(old, new, 1)
    TARGET.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
