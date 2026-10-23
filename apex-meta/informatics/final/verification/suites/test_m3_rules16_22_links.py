#!/usr/bin/env python3
"""
test_m3_rules16_22_links.py — Empirical Verification Oracle for Rules 16-22 Links & Boundaries.

Validates:
1. Existence of all 7 Milestone 3 rule files (Rules 16-22).
2. 100% resolution of relative markdown links in Rules 16-22 to existing files on disk.
3. Portability check: 0 machine-specific absolute links (e.g., file://, C:\\).
4. Zero live mutation guard: AGENTS.md, CLAUDE.md, GEMINI.md free of uncommitted informatics modifications.
5. Research preservation guard: 01-universal-instruction-research/ and 03-research-of-file-10/ preserved.
"""

from __future__ import annotations

import re
import unittest
import urllib.parse
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[5]
KB_DIR = REPO_ROOT / "apex-meta" / "informatics" / "final" / "research" / "06-layered-rule-kb"

M3_RULE_FILES = [
    "rule-16-authoring.md",
    "rule-17-trade-off.md",
    "rule-18-handover.md",
    "rule-19-iterative.md",
    "rule-20-schemas.md",
    "rule-21-sync.md",
    "rule-22-pointers.md",
]

MARKDOWN_LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")


def strip_code(content: str) -> str:
    """Drop fenced blocks and inline code so code examples are not interpreted as live links."""
    without_fences = re.sub(r"```[\s\S]*?```", "", content)
    return re.sub(r"`[^`\n]*`", "", without_fences)


class TestM3RulesLinksAndBoundaries(unittest.TestCase):
    """Empirical verification for Milestone 3 (Rules 16-22)."""

    def test_all_m3_files_exist(self):
        for fname in M3_RULE_FILES:
            with self.subTest(file=fname):
                fpath = KB_DIR / fname
                self.assertTrue(fpath.is_file(), f"M3 rule file missing: {fpath}")
                self.assertGreater(fpath.stat().st_size, 1000, f"M3 rule file unexpectedly small: {fpath}")

    def test_no_machine_specific_absolute_links(self):
        for fname in M3_RULE_FILES:
            with self.subTest(file=fname):
                content = (KB_DIR / fname).read_text(encoding="utf-8")
                stripped = strip_code(content)
                offenders = [
                    link for _, link in MARKDOWN_LINK_RE.findall(stripped)
                    if link.startswith("file://") or ":\\" in link or ":/" in link
                ]
                self.assertEqual(
                    offenders, [],
                    f"{fname} contains machine-specific absolute links: {offenders}",
                )

    def test_all_relative_links_resolve_100_percent(self):
        total_links = 0
        resolved_links = 0
        broken_links = []

        for fname in M3_RULE_FILES:
            content = (KB_DIR / fname).read_text(encoding="utf-8")
            stripped = strip_code(content)
            for anchor, raw_link in MARKDOWN_LINK_RE.findall(stripped):
                if raw_link.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                clean_target = raw_link.split("#")[0]
                if not clean_target:
                    continue
                total_links += 1
                unquoted = urllib.parse.unquote(clean_target)
                if unquoted.startswith("/"):
                    resolved_path = (REPO_ROOT / unquoted.lstrip("/")).resolve()
                else:
                    resolved_path = (KB_DIR / unquoted).resolve()

                if not resolved_path.exists():
                    broken_links.append((fname, anchor, raw_link, str(resolved_path)))
                else:
                    resolved_links += 1

        self.assertEqual(
            broken_links, [],
            f"Broken markdown links found in M3 rules: {broken_links}",
        )
        self.assertGreater(total_links, 50, f"Expected substantial link coverage, found only {total_links}")
        self.assertEqual(total_links, resolved_links)

    def test_zero_live_mutation_carriers(self):
        """Confirm no new modifications or contract injections into live carrier files."""
        carriers = ["AGENTS.md", "CLAUDE.md", "GEMINI.md"]
        for cname in carriers:
            cpath = REPO_ROOT / cname
            self.assertTrue(cpath.is_file(), f"Carrier file missing: {cpath}")
            content = cpath.read_text(encoding="utf-8")
            self.assertNotIn("<apex_contract", content, f"Live carrier {cname} contains injected <apex_contract>")
            self.assertNotIn("06-layered-rule-kb", content, f"Live carrier {cname} contains layered rule kb references")
            self.assertNotIn("16-candidate-3A-ultra", content, f"Live carrier {cname} contains 3A-ultra references")

    def test_research_preservation_zero_modifications(self):
        """Verify research directories 01-universal-instruction-research/ and 03-research-of-file-10/ have no modifications today."""
        res_dirs = [
            REPO_ROOT / "apex-meta" / "informatics" / "final" / "research" / "01-universal-instruction-research",
            REPO_ROOT / "apex-meta" / "informatics" / "final" / "research" / "03-research-of-file-10",
        ]
        today_start = datetime(2026, 10, 22, 0, 0, 0).timestamp()
        for rdir in res_dirs:
            self.assertTrue(rdir.is_dir(), f"Research directory missing: {rdir}")
            modified_today = []
            for item in rdir.rglob("*"):
                if item.is_file():
                    mtime = item.stat().st_mtime
                    if mtime >= today_start:
                        modified_today.append(str(item.relative_to(REPO_ROOT)))
            self.assertEqual(
                modified_today, [],
                f"Research preservation violation: files modified today in {rdir.name}: {modified_today}",
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
