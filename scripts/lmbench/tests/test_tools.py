"""Tool implementation mechanics, against a real filesystem via fsguard."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

from scripts.lmbench import fsguard, tools, winpath


class TestClaimTools(unittest.TestCase):
    def test_claim_tools_identified(self):
        for name in (
            "classify_failure",
            "apply_declared_recovery",
            "record_evidence",
            "emit_escalation",
            "request_approval",
            "finish",
        ):
            self.assertTrue(tools.is_claim_tool(name))
        self.assertFalse(tools.is_claim_tool("write_file"))

    def test_do_claim_always_succeeds_and_echoes_args(self):
        result = tools.do_claim("finish", {"status": "completed", "summary": "done"})
        self.assertTrue(result.ok)
        self.assertEqual(result.output, {"status": "completed", "summary": "done"})


class TestFileTools(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.roots = winpath.RootSet.build(
            [winpath.RootRule("WORK", str(self.root), "rw")]
        )
        self.guard = fsguard.FsGuard(self.roots)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _resolved(self, rel):
        candidate = winpath.normalize_path(rel, base=str(self.root))
        self.assertIsNone(candidate.reject_code)
        return candidate.real

    def test_list_dir(self):
        (self.root / "a.txt").write_text("x", encoding="utf-8")
        (self.root / "b.txt").write_text("y", encoding="utf-8")
        result = tools.do_list_dir(self.guard, [self._resolved(".")], {})
        self.assertTrue(result.ok)
        self.assertEqual(sorted(result.output["entries"]), ["a.txt", "b.txt"])

    def test_read_file_numbers_lines(self):
        (self.root / "f.txt").write_text("one\ntwo\nthree", encoding="utf-8")
        result = tools.do_read_file(self.guard, [self._resolved("f.txt")], {})
        self.assertTrue(result.ok)
        self.assertEqual(result.output["text"], "1: one\n2: two\n3: three")
        self.assertEqual(result.output["total_lines"], 3)

    def test_read_file_line_range(self):
        (self.root / "f.txt").write_text("one\ntwo\nthree\nfour", encoding="utf-8")
        result = tools.do_read_file(
            self.guard, [self._resolved("f.txt")], {"start_line": 2, "end_line": 3}
        )
        self.assertEqual(result.output["text"], "2: two\n3: three")

    def test_write_file(self):
        result = tools.do_write_file(
            self.guard, [self._resolved("new.txt")], {"content": "hello"}
        )
        self.assertTrue(result.ok)
        self.assertEqual((self.root / "new.txt").read_text(encoding="utf-8"), "hello")

    def test_apply_patch_replaces_the_requested_occurrence_only(self):
        (self.root / "f.py").write_text("x = 1\nx = 1\n", encoding="utf-8")
        result = tools.do_apply_patch(
            self.guard,
            [self._resolved("f.py")],
            {"path": "f.py", "old_text": "x = 1", "new_text": "x = 2", "occurrence": 2},
        )
        self.assertTrue(result.ok)
        self.assertEqual(result.output["occurrences_found"], 2)
        self.assertEqual((self.root / "f.py").read_text(encoding="utf-8"), "x = 1\nx = 2\n")

    def test_apply_patch_reports_when_old_text_absent(self):
        (self.root / "f.py").write_text("unrelated content", encoding="utf-8")
        result = tools.do_apply_patch(
            self.guard,
            [self._resolved("f.py")],
            {"path": "f.py", "old_text": "not_present", "new_text": "x"},
        )
        self.assertFalse(result.ok)
        self.assertEqual(result.error, "old_text_not_found")

    def test_run_command_captures_exit_code_and_output(self):
        result = tools.do_run_command(
            self.guard,
            [sys.executable, "-c", "print('hi'); exit(0)"],
            cwd=str(self.root),
        )
        self.assertTrue(result.ok)
        self.assertEqual(result.output["exit_code"], 0)
        self.assertIn("hi", result.output["stdout"])

    def test_run_command_nonzero_exit_still_reports_ok_true_with_the_code(self):
        # A nonzero exit is data for the semantic grader, not a tool failure.
        result = tools.do_run_command(
            self.guard,
            [sys.executable, "-c", "exit(1)"],
            cwd=str(self.root),
        )
        self.assertTrue(result.ok)
        self.assertEqual(result.output["exit_code"], 1)


if __name__ == "__main__":
    unittest.main()
