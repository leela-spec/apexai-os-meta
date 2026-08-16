"""Regression tests for epic-local Apex Sync task identity.

Run from the repository root with:
    python -m unittest discover -s scripts/tests -t . -v
"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts import apex_sync


class ApexSyncEpicLocalIdentityTests(unittest.TestCase):
    def setUp(self) -> None:
        self._temp = tempfile.TemporaryDirectory()
        self.root = Path(self._temp.name)

    def tearDown(self) -> None:
        self._temp.cleanup()

    def write_task(
        self,
        epic: str,
        filename: str,
        *,
        task_id: int,
        status: str = "open",
        depends_on: tuple[int, ...] = (),
        blocked_by: tuple[str, ...] = (),
    ) -> None:
        task_path = self.root / "apex-meta" / "epics" / epic / filename
        task_path.parent.mkdir(parents=True, exist_ok=True)
        lines = [
            "---",
            f"id: {task_id}",
            f'title: "{epic} task {task_id}"',
            f"status: {status}",
            "priority: medium",
            f"depends_on: [{', '.join(str(item) for item in depends_on)}]",
            f"blocked_by: [{', '.join(blocked_by)}]",
            "---",
            "",
            f"# {epic} task {task_id}",
            "",
        ]
        task_path.write_text("\n".join(lines), encoding="utf-8")

    def test_same_integer_id_in_different_epics_is_valid_and_unambiguous(self) -> None:
        self.write_task("alpha", "001.md", task_id=1)
        self.write_task("beta", "001.md", task_id=1)

        report = apex_sync.command_next(self.root, True, "2026-08-16T00:00:00Z")

        flags = report["dependency_validation_report"]["review_flags"]
        self.assertNotIn("duplicate_task_id", {item["flag"] for item in flags})
        candidates = report["next_action_report"]["candidates"]
        self.assertEqual([item["task_key"] for item in candidates], ["alpha:001", "beta:001"])

    def test_duplicate_integer_id_inside_one_epic_is_flagged(self) -> None:
        self.write_task("alpha", "001.md", task_id=1)
        self.write_task("alpha", "002.md", task_id=1)

        load = apex_sync.read_task_files(self.root)

        duplicates = [item for item in load.review_flags if item["flag"] == "duplicate_task_id"]
        self.assertEqual(len(duplicates), 2)
        self.assertEqual({item["task_key"] for item in duplicates}, {"alpha:001"})

    def test_dependency_resolution_uses_the_current_epic(self) -> None:
        self.write_task("alpha", "001.md", task_id=1, status="done")
        self.write_task("alpha", "002.md", task_id=2, depends_on=(1,))
        self.write_task("beta", "001.md", task_id=1, status="open")

        report = apex_sync.command_next(self.root, True, "2026-08-16T00:00:00Z")

        candidates = report["next_action_report"]["candidates"]
        by_key = {item["task_key"]: item for item in candidates}
        self.assertIn("alpha:002", by_key)
        self.assertEqual(by_key["alpha:002"]["depends_on_keys"], ["alpha:001"])
        self.assertIn("beta:001", by_key)

    def test_dependency_missing_in_current_epic_is_not_satisfied_elsewhere(self) -> None:
        self.write_task("alpha", "002.md", task_id=2, depends_on=(1,))
        self.write_task("beta", "001.md", task_id=1, status="done")

        load = apex_sync.read_task_files(self.root)

        missing = [item for item in load.review_flags if item["flag"] == "missing_dependency_target"]
        self.assertEqual(len(missing), 1)
        self.assertEqual(missing[0]["task_key"], "alpha:002")
        self.assertEqual(missing[0]["missing_dependency_keys"], ["alpha:001"])

    def test_numeric_blocker_resolution_uses_the_current_epic(self) -> None:
        self.write_task("alpha", "001.md", task_id=1, status="done")
        self.write_task("alpha", "002.md", task_id=2, blocked_by=("1",))
        self.write_task("beta", "001.md", task_id=1, status="open")

        report = apex_sync.command_next(self.root, True, "2026-08-16T00:00:00Z")

        by_key = {item["task_key"]: item for item in report["next_action_report"]["candidates"]}
        self.assertIn("alpha:002", by_key)
        self.assertEqual(by_key["alpha:002"]["blocked_by_task_keys"], ["alpha:001"])

    def test_cycle_detection_reports_epic_qualified_keys(self) -> None:
        self.write_task("alpha", "001.md", task_id=1, depends_on=(2,))
        self.write_task("alpha", "002.md", task_id=2, depends_on=(1,))
        self.write_task("beta", "001.md", task_id=1)

        load = apex_sync.read_task_files(self.root)

        cycles = [item for item in load.review_flags if item["flag"] == "circular_dependency_risk"]
        self.assertEqual(len(cycles), 1)
        self.assertEqual(cycles[0]["depends_on_cycle"], ["alpha:001", "alpha:002", "alpha:001"])

    def test_unlock_depth_is_computed_per_epic(self) -> None:
        self.write_task("alpha", "001.md", task_id=1)
        self.write_task("alpha", "002.md", task_id=2, depends_on=(1,))
        self.write_task("beta", "001.md", task_id=1)

        load = apex_sync.read_task_files(self.root)

        self.assertEqual(
            apex_sync.compute_unlock_depths(load.tasks),
            {"alpha:001": 1, "alpha:002": 0, "beta:001": 0},
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
