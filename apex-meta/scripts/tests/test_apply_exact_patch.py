#!/usr/bin/env python3
"""
test_apply_exact_patch.py — Unit tests for the deterministic exact-match patch runner.
"""

from __future__ import annotations

import importlib.util
import os
import shutil
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "apply_exact_patch.py"
SPEC = importlib.util.spec_from_file_location("apply_exact_patch_under_test", SCRIPT)
assert SPEC and SPEC.loader
patch_runner = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(patch_runner)

apply_patch_blocks = patch_runner.apply_patch_blocks
parse_patch_file = patch_runner.parse_patch_file


class TestApplyExactPatch(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_parse_valid_patch(self):
        patch_file = os.path.join(self.test_dir, "test.patch")
        with open(patch_file, "w", encoding="utf-8") as f:
            f.write(
                "<file>\n"
                "foo/bar.md\n"
                "</file>\n"
                "<old>\n"
                "hello world\n"
                "</old>\n"
                "<new>\n"
                "hello universe\n"
                "</new>\n"
            )

        blocks = parse_patch_file(patch_file)
        self.assertEqual(len(blocks), 1)
        self.assertEqual(blocks[0][0], "foo/bar.md")
        self.assertEqual(blocks[0][1], "hello world")
        self.assertEqual(blocks[0][2], "hello universe")

    def test_apply_patch_success(self):
        target_file = os.path.join(self.test_dir, "sample.md")
        with open(target_file, "w", encoding="utf-8") as f:
            f.write("# Title\n\nSome introductory text.\n\nOld Section Content\n\nFooter\n")

        patch_file = os.path.join(self.test_dir, "sample.patch")
        with open(patch_file, "w", encoding="utf-8") as f:
            f.write(
                "<file>\n"
                "sample.md\n"
                "</file>\n"
                "<old>\n"
                "Old Section Content\n"
                "</old>\n"
                "<new>\n"
                "New Modern Section Content\n"
                "</new>\n"
            )

        results = apply_patch_blocks(patch_file, repo_root=self.test_dir)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["status"], "APPLIED")

        with open(target_file, "r", encoding="utf-8") as f:
            updated_content = f.read()

        self.assertIn("New Modern Section Content", updated_content)
        self.assertNotIn("Old Section Content", updated_content)
        self.assertIn("# Title", updated_content)

    def test_apply_patch_not_found(self):
        target_file = os.path.join(self.test_dir, "sample.md")
        with open(target_file, "w", encoding="utf-8") as f:
            f.write("# Title\n\nText\n")

        patch_file = os.path.join(self.test_dir, "sample.patch")
        with open(patch_file, "w", encoding="utf-8") as f:
            f.write(
                "<file>\n"
                "sample.md\n"
                "</file>\n"
                "<old>\n"
                "Nonexistent Text\n"
                "</old>\n"
                "<new>\n"
                "Replacement\n"
                "</new>\n"
            )

        with self.assertRaises(ValueError) as ctx:
            apply_patch_blocks(patch_file, repo_root=self.test_dir)
        self.assertIn("not found in live file", str(ctx.exception))

    def test_apply_patch_ambiguous_multiple_matches(self):
        target_file = os.path.join(self.test_dir, "sample.md")
        with open(target_file, "w", encoding="utf-8") as f:
            f.write("duplicate line\nsome other text\nduplicate line\n")

        patch_file = os.path.join(self.test_dir, "sample.patch")
        with open(patch_file, "w", encoding="utf-8") as f:
            f.write(
                "<file>\n"
                "sample.md\n"
                "</file>\n"
                "<old>\n"
                "duplicate line\n"
                "</old>\n"
                "<new>\n"
                "unique line\n"
                "</new>\n"
            )

        with self.assertRaises(ValueError) as ctx:
            apply_patch_blocks(patch_file, repo_root=self.test_dir)
        self.assertIn("AMBIGUOUS", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
