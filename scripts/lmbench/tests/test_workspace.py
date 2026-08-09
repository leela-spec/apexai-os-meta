"""VAL-18: cleanup verifies no surviving child process, identity-checked by
(pid, creation_time) rather than bare pid -- and cleanup failure is itself
reported, never silently swallowed."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

from scripts.lmbench import workspace


class TestVAL18ProcessTermination(unittest.TestCase):
    def test_spawned_child_is_confirmed_alive_then_confirmed_gone(self):
        popen = workspace.spawn_tracked(
            [sys.executable, "-c", "import time; time.sleep(60)"],
            cwd=str(Path.cwd()),
        )
        try:
            self.assertTrue(workspace.is_alive(popen.pid))
            ok = workspace.terminate_verified(popen)
            self.assertTrue(ok)
            self.assertFalse(workspace.is_alive(popen.pid))
        finally:
            if popen.poll() is None:
                popen.kill()
                popen.wait(timeout=5)

    def test_terminate_on_already_exited_process_is_a_clean_success(self):
        popen = workspace.spawn_tracked([sys.executable, "-c", "pass"], cwd=str(Path.cwd()))
        popen.wait(timeout=10)
        ok = workspace.terminate_verified(popen)
        self.assertTrue(ok)

    def test_is_alive_false_for_a_pid_that_was_never_a_real_process(self):
        # A PID astronomically unlikely to be in use. is_alive must return
        # False, not raise.
        self.assertFalse(workspace.is_alive(999_999))


class TestWorkspaceLifecycle(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.base = Path(self.tmp.name)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_allocate_creates_a_fresh_directory(self):
        trial_dir = workspace.allocate(self.base, "T1")
        self.assertTrue(trial_dir.is_dir())

    def test_allocate_refuses_to_reuse_an_existing_trial_id(self):
        workspace.allocate(self.base, "T1")
        with self.assertRaises(FileExistsError):
            workspace.allocate(self.base, "T1")

    def test_destroy_removes_the_directory_and_reports_success(self):
        trial_dir = workspace.allocate(self.base, "T1")
        (trial_dir / "f.txt").write_text("x", encoding="utf-8")
        ok = workspace.destroy(trial_dir)
        self.assertTrue(ok)
        self.assertFalse(trial_dir.exists())

    def test_destroy_on_already_missing_directory_reports_success(self):
        missing = self.base / "never-existed"
        self.assertTrue(workspace.destroy(missing))


if __name__ == "__main__":
    unittest.main()
