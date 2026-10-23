#!/usr/bin/env python3
"""
Canonical-ownership invariants for the live Apex Informatics suite.

These tests enforce the structural guarantees established by the canonical-ownership
compression pass. They exist because three real defects survived a green validator run
and 185 passing tests:

  D1  `FA-04` was assigned to two unrelated rules in one file.
  D9  An inline `patch_intent.v1` schema copy drifted from the authoritative JSON,
      silently dropping every `maxLength` bound the real schema enforces.
  RBL-05 Absolute `file:///c:/GitDev/...` links resolved only on one machine.

Each test below closes one of those classes mechanically rather than by convention.
Research record: apex-meta/informatics/Agent_Setup/NextIteration/DeepReasoning/
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[5]
INFORMATICS_DIR = REPO_ROOT / "apex-meta" / "informatics" / "final"

# The seven governed files of the live suite.
GOVERNED_FILES = [
    "index.md",
    "general-informatics-router.md",
    "writing-profile.md",
    "file-architecture.md",
    "execution-modes.md",
    "anti-drift-rules.md",
    "governance-schemas.md",
]

# A rule DEFINITION, as opposed to a reference. Two authoring styles are in use:
#   - **WP-01 [P0 | I98/E98/R05] Title**: body
#   ### FA-01: Title
RULE_DEFINITION_PATTERNS = [
    re.compile(r"^\s*-\s+\*\*((?:WP|FA|EM|AD|GS)-\d{2})\s+\[", re.MULTILINE),
    re.compile(r"^#{2,4}\s+((?:WP|FA|EM|AD|GS)-\d{2}):", re.MULTILINE),
]

# A `Canonical: `XX-NN`` cross-reference emitted by the compression pass.
CANONICAL_POINTER_PATTERN = re.compile(r"[Cc]anonical[^:\n]*:\s*`((?:WP|FA|EM|AD|GS)-\d{2})`")

MARKDOWN_LINK_PATTERN = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")


def get_path(name: str) -> Path:
    if (INFORMATICS_DIR / name).exists():
        return INFORMATICS_DIR / name
    if (INFORMATICS_DIR / "specs" / name).exists():
        return INFORMATICS_DIR / "specs" / name
    return INFORMATICS_DIR / name


def read(name: str) -> str:
    return get_path(name).read_text(encoding="utf-8")


def strip_code(content: str) -> str:
    """Drop fenced blocks and inline code so illustrative examples are not read as real links."""
    without_fences = re.sub(r"```[\s\S]*?```", "", content)
    return re.sub(r"`[^`\n]*`", "", without_fences)


def rule_definitions(content: str) -> list[str]:
    found: list[str] = []
    for pattern in RULE_DEFINITION_PATTERNS:
        found.extend(pattern.findall(content))
    return found


class TestDurableRuleIdUniqueness(unittest.TestCase):
    """D1 guard: a durable rule ID must identify exactly one rule."""

    def test_no_duplicate_rule_id_within_a_file(self):
        for name in GOVERNED_FILES:
            with self.subTest(file=name):
                ids = rule_definitions(read(name))
                duplicates = sorted({rid for rid in ids if ids.count(rid) > 1})
                self.assertEqual(
                    duplicates, [],
                    f"{name} defines these durable rule IDs more than once: {duplicates}. "
                    f"Durable IDs are the suite's stable cross-reference mechanism (WP-15); "
                    f"retire an ID and leave a gap rather than reusing it.",
                )

    def test_no_duplicate_rule_id_across_the_suite(self):
        owners: dict[str, list[str]] = {}
        for name in GOVERNED_FILES:
            for rid in rule_definitions(read(name)):
                owners.setdefault(rid, []).append(name)
        collisions = {rid: files for rid, files in owners.items() if len(set(files)) > 1}
        self.assertEqual(
            collisions, {},
            f"Durable rule IDs defined in more than one file: {collisions}",
        )

    def test_rule_id_prefix_matches_its_home_file(self):
        """A WP- rule belongs in writing-profile.md, an FA- rule in file-architecture.md, etc."""
        expected_home = {
            "WP": "writing-profile.md",
            "FA": "file-architecture.md",
            "EM": "execution-modes.md",
            "AD": "anti-drift-rules.md",
            "GS": "governance-schemas.md",
        }
        for name in GOVERNED_FILES:
            for rid in rule_definitions(read(name)):
                prefix = rid.split("-")[0]
                self.assertEqual(
                    expected_home[prefix], name,
                    f"{name} defines {rid}, but {prefix}- rules are owned by {expected_home[prefix]}",
                )


class TestCanonicalPointerIntegrity(unittest.TestCase):
    """Every `Canonical: `XX-NN`` cross-reference must resolve to a real rule."""

    @classmethod
    def setUpClass(cls):
        cls.defined = set()
        for name in GOVERNED_FILES:
            cls.defined.update(rule_definitions(read(name)))

    def test_suite_defines_rules(self):
        self.assertGreater(
            len(self.defined), 90,
            "Rule-definition extraction found almost nothing; the authoring style likely changed "
            "and RULE_DEFINITION_PATTERNS needs updating before these guards mean anything.",
        )

    def test_every_canonical_pointer_resolves(self):
        for name in GOVERNED_FILES:
            content = read(name)
            for target in CANONICAL_POINTER_PATTERN.findall(content):
                with self.subTest(file=name, target=target):
                    self.assertIn(
                        target, self.defined,
                        f"{name} points at canonical rule {target}, which no governed file defines.",
                    )

    def test_canonical_pointer_never_targets_its_own_file(self):
        """A pointer that resolves inside its own file is a no-op, not a cross-reference."""
        for name in GOVERNED_FILES:
            content = read(name)
            local = set(rule_definitions(content))
            for target in CANONICAL_POINTER_PATTERN.findall(content):
                with self.subTest(file=name, target=target):
                    self.assertNotIn(
                        target, local,
                        f"{name} marks {target} as canonical elsewhere, but defines it locally.",
                    )


class TestLinkPortability(unittest.TestCase):
    """RBL-05 guard: links must resolve in every clone, runner, and OS."""

    def test_no_machine_specific_absolute_links(self):
        for name in GOVERNED_FILES:
            with self.subTest(file=name):
                content = read(name)
                offenders = [
                    link for link in MARKDOWN_LINK_PATTERN.findall(strip_code(content))
                    if link.startswith("file://")
                ]
                self.assertEqual(
                    offenders, [],
                    f"{name} uses absolute file:// links that resolve only on one machine: {offenders}",
                )

    def test_relative_links_resolve(self):
        for name in GOVERNED_FILES:
            content = read(name)
            for link in MARKDOWN_LINK_PATTERN.findall(strip_code(content)):
                if link.startswith(("http://", "https://", "#", "mailto:")):
                    continue
                target = link.split("#")[0]
                if not target:
                    continue
                with self.subTest(file=name, link=link):
                    base_dir = get_path(name).parent
                    resolved = (base_dir / target.replace("%20", " ")).resolve()
                    self.assertTrue(
                        resolved.exists(),
                        f"{name} links to '{link}', which does not resolve to an existing path (looked at {resolved}).",
                    )


class TestNoReEmbeddedUpstreamSchema(unittest.TestCase):
    """D9 guard: the suite must cite the authoritative patch schema, never re-embed it."""

    SCHEMA_PATH = (
        REPO_ROOT / ".claude" / "skills" / "deterministic-markdown-patcher2"
        / "references" / "patch-intent-schema.json"
    )

    def test_authoritative_schema_exists(self):
        self.assertTrue(
            self.SCHEMA_PATH.exists(),
            f"Authoritative patch intent schema missing at {self.SCHEMA_PATH}; "
            f"governance-schemas.md cites it as the single source.",
        )

    def test_governance_schemas_does_not_re_embed_the_json_schema(self):
        content = read("governance-schemas.md")
        self.assertNotRegex(
            content, r'```json\s*\{[\s\S]*?"\$schema"[\s\S]*?```',
            "governance-schemas.md re-embeds a full JSON Schema definition. A copy drifted from "
            "the authoritative file once already (D9), dropping its maxLength bounds. State the "
            "operative contract and link the source instead (WP-23).",
        )

    def test_governance_schemas_states_the_operative_contract(self):
        content = read("governance-schemas.md")
        for invariant in (
            "require_unique_match", "fail_on_ambiguity",
            "allow_full_file_rewrite", "max_files_touched",
        ):
            with self.subTest(invariant=invariant):
                self.assertIn(
                    invariant, content,
                    f"governance-schemas.md must state the safety invariant '{invariant}' "
                    f"even though it no longer embeds the schema.",
                )


if __name__ == "__main__":
    unittest.main(verbosity=2)
