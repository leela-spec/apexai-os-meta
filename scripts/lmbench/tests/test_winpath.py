"""Hostile-path battery for `winpath.normalize_path` and `RootSet.classify`.

Every vector here is a documented way to defeat a naive `str.startswith` root
check on Windows. Each must produce a *reject_code*, never an exception and
never a silently-accepted path.
"""

from __future__ import annotations

import os
import tempfile
import unittest
from pathlib import Path

from scripts.lmbench import winpath


class TestNormalizePathRejections(unittest.TestCase):
    """~25 hostile vectors. Every one must yield reject_code, not raise."""

    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.base = self.tmp.name

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _reject(self, raw, expected_code):
        candidate = winpath.normalize_path(raw, base=self.base)
        self.assertEqual(
            candidate.reject_code, expected_code, f"{raw!r} -> {candidate.reject_code!r}"
        )
        self.assertIsNone(candidate.real)
        self.assertIsNone(candidate.cmp)

    def test_not_a_string(self):
        self._reject(12345, "NOT_STRING")
        self._reject(None, "NOT_STRING")
        self._reject([], "NOT_STRING")

    def test_empty(self):
        self._reject("", "EMPTY")

    def test_nul_byte(self):
        self._reject("work\x00ok.txt", "NUL_BYTE")

    def test_alternate_data_stream(self):
        self._reject("work\\ok.txt:evil", "ADS")
        self._reject("ok.txt:$DATA", "ADS")
        self._reject("a:b:c", "ADS")

    def test_unc_and_device_prefix(self):
        self._reject("\\\\?\\C:\\Windows", "UNC_OR_DEVICE_PREFIX")
        self._reject("\\\\.\\PhysicalDrive0", "UNC_OR_DEVICE_PREFIX")
        self._reject("\\\\server\\share\\file", "UNC_OR_DEVICE_PREFIX")
        self._reject("//server/share/file", "UNC_OR_DEVICE_PREFIX")

    def test_reserved_device_names(self):
        for name in ("NUL", "nul", "CON", "PRN", "AUX", "COM1", "com3", "LPT1", "lpt9"):
            self._reject(f"work\\{name}", "RESERVED_NAME")
            self._reject(f"work\\{name}.txt", "RESERVED_NAME")

    def test_trailing_dot_or_space(self):
        self._reject("work\\ok.txt ", "TRAILING_DOT_OR_SPACE")
        self._reject("work\\ok.txt.", "TRAILING_DOT_OR_SPACE")
        self._reject("work\\evil \\ok.txt", "TRAILING_DOT_OR_SPACE")

    def test_wildcards(self):
        self._reject("work\\*.txt", "WILDCARD")
        self._reject("work\\ok?.txt", "WILDCARD")

    def test_short_names(self):
        self._reject("work\\PROGRA~1", "SHORT_NAME")
        self._reject("work\\PROGRA~1\\file.txt", "SHORT_NAME")

    def test_dot_and_dotdot_components_are_not_themselves_rejected(self):
        # ".." is not rejected at normalize time -- it collapses via normpath,
        # and whether it escapes a root is the broker's job (ROOT.OUTSIDE_ALL),
        # not the normalizer's. Rejecting it here would hide the attempt.
        candidate = winpath.normalize_path("..\\..\\etc\\passwd", base=self.base)
        self.assertIsNone(candidate.reject_code)
        self.assertIsNotNone(candidate.real)


class TestNormalizePathAcceptance(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.base = self.tmp.name

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_ordinary_relative_path_resolves_under_base(self):
        candidate = winpath.normalize_path("work\\ok.txt", base=self.base)
        self.assertIsNone(candidate.reject_code)
        self.assertTrue(candidate.real.lower().startswith(self.base.lower()))
        self.assertEqual(candidate.cmp, os.path.normcase(candidate.real))

    def test_forward_slashes_normalize_the_same_as_backslashes(self):
        a = winpath.normalize_path("work/ok.txt", base=self.base)
        b = winpath.normalize_path("work\\ok.txt", base=self.base)
        self.assertEqual(a.cmp, b.cmp)

    def test_case_insensitive_comparison_form(self):
        a = winpath.normalize_path("Work\\OK.txt", base=self.base)
        b = winpath.normalize_path("work\\ok.txt", base=self.base)
        self.assertEqual(a.cmp, b.cmp)
        # but the real (trace) form preserves case
        self.assertIn("Work", a.real)


class TestRootSetClassify(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "work").mkdir()
        (self.root / "work" / "secrets").mkdir()
        (self.root / "answers").mkdir()

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _classify(self, roots, rel):
        root_set = winpath.RootSet.build(roots)
        candidate = winpath.normalize_path(rel, base=str(self.root))
        self.assertIsNone(candidate.reject_code)
        return root_set.classify(candidate.cmp)

    def test_longest_prefix_wins_for_nested_forbidden_inside_rw(self):
        roots = [
            winpath.RootRule("WORK", str(self.root / "work"), "rw"),
            winpath.RootRule("SECRETS", str(self.root / "work" / "secrets"), "forbidden"),
        ]
        outer = self._classify(roots, "work\\ok.txt")
        inner = self._classify(roots, "work\\secrets\\key.txt")
        self.assertEqual(outer.root_id, "WORK")
        self.assertEqual(inner.root_id, "SECRETS")

    def test_path_outside_every_root_classifies_to_none(self):
        roots = [winpath.RootRule("WORK", str(self.root / "work"), "rw")]
        result = self._classify(roots, "answers\\key.md")
        self.assertIsNone(result)

    def test_str_startswith_bypass_is_not_a_bypass_here(self):
        # "workshop" should not be classified under a root named "work" just
        # because the string happens to start with it.
        (self.root / "workshop").mkdir()
        roots = [winpath.RootRule("WORK", str(self.root / "work"), "rw")]
        result = self._classify(roots, "workshop\\ok.txt")
        self.assertIsNone(result)

    def test_root_mode_validation(self):
        with self.assertRaises(ValueError):
            winpath.RootRule("BAD", str(self.root), "read-write")


if __name__ == "__main__":
    unittest.main()
