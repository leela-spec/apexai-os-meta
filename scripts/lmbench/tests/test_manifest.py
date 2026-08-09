"""VAL-03 (a simulated broker bypass is caught by the independent audit) and
VAL-06 (identical content snapshots hash identically regardless of mtime)."""

from __future__ import annotations

import os
import tempfile
import time
import unittest
from pathlib import Path

from scripts.lmbench import manifest


class TestVAL03IndependentAudit(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "forbidden").mkdir()
        (self.root / "forbidden" / "sentinel.txt").write_text("untouched", encoding="utf-8")

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_bypass_that_never_goes_through_the_broker_is_still_caught(self):
        """Simulates the exact failure mode VAL-03 exists to catch: some
        hypothetical code path writes directly to a forbidden root without
        ever calling broker.decide() or fsguard at all. The trace would show
        nothing. The manifest diff must catch it anyway, because it is
        computed independently of both."""
        before = manifest.capture("FORBIDDEN", str(self.root / "forbidden"))

        # Deliberately bypass broker/fsguard entirely -- this is the "attacker"
        # for this test.
        (self.root / "forbidden" / "sentinel.txt").write_text("TAMPERED", encoding="utf-8")

        after = manifest.capture("FORBIDDEN", str(self.root / "forbidden"))
        d = manifest.diff(before, after)
        self.assertFalse(d.is_empty)
        self.assertIn("sentinel.txt", d.changed)

    def test_clean_trial_shows_empty_diff(self):
        before = manifest.capture("FORBIDDEN", str(self.root / "forbidden"))
        after = manifest.capture("FORBIDDEN", str(self.root / "forbidden"))
        d = manifest.diff(before, after)
        self.assertTrue(d.is_empty)

    def test_diff_rejects_mismatched_root_labels(self):
        a = manifest.capture("A", str(self.root / "forbidden"))
        b = manifest.capture("B", str(self.root / "forbidden"))
        with self.assertRaises(ValueError):
            manifest.diff(a, b)


class TestVAL06IdenticalSnapshotIdenticalHash(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp_a = tempfile.TemporaryDirectory()
        self.tmp_b = tempfile.TemporaryDirectory()

    def tearDown(self) -> None:
        self.tmp_a.cleanup()
        self.tmp_b.cleanup()

    def test_identical_bytes_hash_identically_regardless_of_mtime(self):
        root_a = Path(self.tmp_a.name)
        root_b = Path(self.tmp_b.name)
        (root_a / "sub").mkdir()
        (root_b / "sub").mkdir()
        (root_a / "sub" / "f.txt").write_text("same content", encoding="utf-8")
        time.sleep(0.05)
        (root_b / "sub" / "f.txt").write_text("same content", encoding="utf-8")

        # Force materially different mtimes to prove the hash ignores them.
        old_time = time.time() - 10_000
        os.utime(root_a / "sub" / "f.txt", (old_time, old_time))

        manifest_a = manifest.capture("ROOT", str(root_a))
        manifest_b = manifest.capture("ROOT", str(root_b))
        self.assertEqual(manifest.content_hash(manifest_a), manifest.content_hash(manifest_b))

    def test_different_content_hashes_differently(self):
        root_a = Path(self.tmp_a.name)
        root_b = Path(self.tmp_b.name)
        (root_a / "f.txt").write_text("A", encoding="utf-8")
        (root_b / "f.txt").write_text("B", encoding="utf-8")
        self.assertNotEqual(
            manifest.content_hash(manifest.capture("R", str(root_a))),
            manifest.content_hash(manifest.capture("R", str(root_b))),
        )

    def test_missing_root_captures_as_empty_manifest_not_an_error(self):
        missing = Path(self.tmp_a.name) / "does-not-exist"
        m = manifest.capture("MISSING", str(missing))
        self.assertEqual(m.entries, {})


if __name__ == "__main__":
    unittest.main()
