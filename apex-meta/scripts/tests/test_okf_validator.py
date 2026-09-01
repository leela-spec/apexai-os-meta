#!/usr/bin/env python3
"""
test_okf_validator.py — Automated unit & fixture test suite for okf_validator.py.

Covers:
- RED tests (must fail): malformed YAML, missing type, missing index, broken index link, duplicate durable ID, pseudo-OKF drift.
- GREEN tests (must pass): valid OKF bundles, custom local types (Research, Plan, Standard), omitted optional metadata, long code lines.
"""

from __future__ import annotations

import importlib.util
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "okf_validator.py"
SPEC = importlib.util.spec_from_file_location("okf_validator_under_test", SCRIPT)
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
sys.modules["okf_validator_under_test"] = validator
SPEC.loader.exec_module(validator)

validate_bundle = validator.validate_bundle


class TestOKFValidator(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)

    # ---------------------------------------------------------
    # GREEN TESTS (Must Pass Cleanly)
    # ---------------------------------------------------------

    def test_green_valid_bundle(self):
        """A properly formatted OKF v0.2 bundle passes with zero errors."""
        bundle_dir = os.path.join(self.test_dir, "valid_bundle")
        os.makedirs(bundle_dir, exist_ok=True)

        with open(os.path.join(bundle_dir, "index.md"), "w", encoding="utf-8") as f:
            f.write('---\nokf_version: "0.2"\ntitle: Valid Bundle\n---\n\n# Index\n\n- [Concept A](concept_a.md)\n')

        with open(os.path.join(bundle_dir, "concept_a.md"), "w", encoding="utf-8") as f:
            f.write('---\ntype: Reference\ntitle: Concept A\ndescription: A valid reference concept.\n---\n\n# Concept A\n\nShort description.\n')

        with open(os.path.join(bundle_dir, "log.md"), "w", encoding="utf-8") as f:
            f.write("# Change Log\n\n## 2026-09-01\n\nInitial version.\n")

        report = validate_bundle(bundle_dir)
        self.assertTrue(report.passed)
        self.assertEqual(report.okf_errors, 0)
        self.assertEqual(report.apex_profile_errors, 0)

    def test_green_custom_local_types(self):
        """Local profile types like 'Research', 'Plan', 'Standard' are valid and accepted."""
        bundle_dir = os.path.join(self.test_dir, "custom_types_bundle")
        os.makedirs(bundle_dir, exist_ok=True)

        with open(os.path.join(bundle_dir, "index.md"), "w", encoding="utf-8") as f:
            f.write('---\nokf_version: "0.2"\n---\n# Index\n- [Plan](my_plan.md)\n- [Research](my_research.md)\n')

        with open(os.path.join(bundle_dir, "my_plan.md"), "w", encoding="utf-8") as f:
            f.write('---\ntype: Plan\ntitle: My Plan\n---\n# Plan\n')

        with open(os.path.join(bundle_dir, "my_research.md"), "w", encoding="utf-8") as f:
            f.write('---\ntype: Research\ntitle: My Research\n---\n# Research\n')

        report = validate_bundle(bundle_dir)
        self.assertTrue(report.passed)
        self.assertEqual(report.okf_errors, 0)

    def test_green_code_block_exemptions(self):
        """Code blocks with long lines and multiple statements do not trigger errors."""
        bundle_dir = os.path.join(self.test_dir, "code_exempt_bundle")
        os.makedirs(bundle_dir, exist_ok=True)

        with open(os.path.join(bundle_dir, "index.md"), "w", encoding="utf-8") as f:
            f.write('---\nokf_version: "0.2"\n---\n# Index\n- [Concept](code_concept.md)\n')

        with open(os.path.join(bundle_dir, "code_concept.md"), "w", encoding="utf-8") as f:
            f.write(
                '---\ntype: Reference\ntitle: Code Concept\n---\n\n'
                '# Code Concept\n\n'
                '```python\n'
                '# Very long procedural code block with more than 50 words on a single line for testing purposes\n'
                'def example_long_function_call_with_many_parameters_and_complex_expressions(arg1, arg2, arg3, arg4):\n'
                '    return [x.do_something() for x in arg1 if x.is_valid() and not x.is_expired()]\n'
                '```\n'
            )

        report = validate_bundle(bundle_dir)
        self.assertTrue(report.passed)
        self.assertEqual(report.okf_errors, 0)
        self.assertEqual(report.advisory_warnings, 0)

    # ---------------------------------------------------------
    # RED TESTS (Must Fail Deterministically)
    # ---------------------------------------------------------

    def test_red_missing_root_index(self):
        """Bundle missing root index.md fails OKF conformance."""
        bundle_dir = os.path.join(self.test_dir, "missing_index_bundle")
        os.makedirs(bundle_dir, exist_ok=True)

        with open(os.path.join(bundle_dir, "concept.md"), "w", encoding="utf-8") as f:
            f.write('---\ntype: Reference\n---\n# Concept\n')

        report = validate_bundle(bundle_dir)
        self.assertFalse(report.passed)
        self.assertGreaterEqual(report.okf_errors, 1)
        self.assertTrue(any(f.rule == "OKF-ROOT-INDEX-EXISTS" for f in report.findings))

    def test_red_missing_type_in_concept(self):
        """Concept file missing 'type' in frontmatter triggers OKF error."""
        bundle_dir = os.path.join(self.test_dir, "missing_type_bundle")
        os.makedirs(bundle_dir, exist_ok=True)

        with open(os.path.join(bundle_dir, "index.md"), "w", encoding="utf-8") as f:
            f.write('---\nokf_version: "0.2"\n---\n# Index\n- [No Type](no_type.md)\n')

        with open(os.path.join(bundle_dir, "no_type.md"), "w", encoding="utf-8") as f:
            f.write('---\ntitle: No Type Concept\n---\n# Content\n')

        report = validate_bundle(bundle_dir)
        self.assertFalse(report.passed)
        self.assertTrue(any(f.rule == "OKF-TYPE-REQUIRED" for f in report.findings))

    def test_red_malformed_yaml_frontmatter(self):
        """Unparseable YAML frontmatter triggers OKF error."""
        bundle_dir = os.path.join(self.test_dir, "bad_yaml_bundle")
        os.makedirs(bundle_dir, exist_ok=True)

        with open(os.path.join(bundle_dir, "index.md"), "w", encoding="utf-8") as f:
            f.write('---\nokf_version: "0.2"\n---\n# Index\n- [Bad](bad.md)\n')

        with open(os.path.join(bundle_dir, "bad.md"), "w", encoding="utf-8") as f:
            f.write('---\nthis is not valid key value yaml\n---\n# Content\n')

        report = validate_bundle(bundle_dir)
        self.assertFalse(report.passed)
        self.assertTrue(any(f.rule == "OKF-FRONTMATTER-PARSE" for f in report.findings))

    def test_red_broken_index_link(self):
        """Link in governed index pointing to nonexistent file triggers APEX_PROFILE error."""
        bundle_dir = os.path.join(self.test_dir, "broken_link_bundle")
        os.makedirs(bundle_dir, exist_ok=True)

        with open(os.path.join(bundle_dir, "index.md"), "w", encoding="utf-8") as f:
            f.write('---\nokf_version: "0.2"\n---\n# Index\n- [Missing](does_not_exist.md)\n')

        report = validate_bundle(bundle_dir)
        self.assertFalse(report.passed)
        self.assertTrue(any(f.rule == "APEX-LINK-INTEGRITY" for f in report.findings))

    def test_red_duplicate_durable_id(self):
        """Duplicate durable 'id' in same governed bundle triggers APEX_PROFILE error."""
        bundle_dir = os.path.join(self.test_dir, "dup_id_bundle")
        os.makedirs(bundle_dir, exist_ok=True)

        with open(os.path.join(bundle_dir, "index.md"), "w", encoding="utf-8") as f:
            f.write('---\nokf_version: "0.2"\n---\n# Index\n- [A](a.md)\n- [B](b.md)\n')

        with open(os.path.join(bundle_dir, "a.md"), "w", encoding="utf-8") as f:
            f.write('---\ntype: Reference\nid: APEX-REF-001\n---\n# A\n')

        with open(os.path.join(bundle_dir, "b.md"), "w", encoding="utf-8") as f:
            f.write('---\ntype: Reference\nid: APEX-REF-001\n---\n# B\n')

        report = validate_bundle(bundle_dir)
        self.assertFalse(report.passed)
        self.assertTrue(any(f.rule == "APEX-UNIQUE-DURABLE-ID" for f in report.findings))

    def test_red_pseudo_okf_drift(self):
        """File named .okf.md without YAML frontmatter triggers APEX_PROFILE error."""
        bundle_dir = os.path.join(self.test_dir, "pseudo_okf_bundle")
        os.makedirs(bundle_dir, exist_ok=True)

        with open(os.path.join(bundle_dir, "index.md"), "w", encoding="utf-8") as f:
            f.write('---\nokf_version: "0.2"\n---\n# Index\n- [Pseudo](pseudo.okf.md)\n')

        with open(os.path.join(bundle_dir, "pseudo.okf.md"), "w", encoding="utf-8") as f:
            f.write('# Pseudo OKF File\n\nNo frontmatter here.\n')

        report = validate_bundle(bundle_dir)
        self.assertFalse(report.passed)
        self.assertTrue(any(f.rule == "APEX-PSEUDO-OKF-DRIFT" for f in report.findings))


if __name__ == "__main__":
    unittest.main()
