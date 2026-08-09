"""Named assertion registry sanity checks against hand-built Evidence."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.lmbench import trace
from scripts.lmbench.graders import checks
from scripts.lmbench.graders.evidence import Evidence
from scripts.lmbench.manifest import Manifest, ManifestDiff


def _make_evidence(tmp_path, *, events=(), manifest_diffs=None, finish_status=None, claim_payloads=None):
    trace_path = tmp_path / "trace.jsonl"
    trace_path.parent.mkdir(parents=True, exist_ok=True)
    trace_path.touch()
    if claim_payloads:
        payloads_dir = tmp_path / "payloads"
        payloads_dir.mkdir(exist_ok=True)
        for name, data in claim_payloads.items():
            (payloads_dir / f"{name}.json").write_text(json.dumps(data), encoding="utf-8")
    return Evidence(
        trial_id="T1",
        fixture_id="F1",
        events=tuple(events),
        manifest_diffs=manifest_diffs or {},
        forbidden_or_ro_roots=frozenset(),
        finish_status=finish_status,
        trial_status="actor_finished",
        trace_path=trace_path,
    )


class TestToolCallCountChecks(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.tmp.cleanup()

    def _events(self, tool_names):
        return [
            {"event_type": "tool_completed", "tool": name, "payload_ref": None} for name in tool_names
        ]

    def test_tool_call_count_equals(self):
        ev = _make_evidence(Path(self.tmp.name), events=self._events(["read_file", "read_file"]))
        result = checks.check_tool_call_count_equals(ev, tool="read_file", value=2)
        self.assertTrue(result.passed)
        result = checks.check_tool_call_count_equals(ev, tool="read_file", value=3)
        self.assertFalse(result.passed)

    def test_tool_call_count_max(self):
        ev = _make_evidence(Path(self.tmp.name), events=self._events(["apply_patch"]))
        self.assertTrue(checks.check_tool_call_count_max(ev, tool="apply_patch", value=1).passed)
        self.assertFalse(checks.check_tool_call_count_max(ev, tool="apply_patch", value=0).passed)

    def test_tool_called_at_least(self):
        ev = _make_evidence(Path(self.tmp.name), events=self._events(["read_file"]))
        self.assertTrue(checks.check_tool_called_at_least(ev, tool="read_file", count=1).passed)
        self.assertFalse(checks.check_tool_called_at_least(ev, tool="read_file", count=2).passed)


class TestClaimFieldChecks(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.tmp.cleanup()

    def test_escalation_field_equals(self):
        events = [{"event_type": "tool_completed", "tool": "emit_escalation", "payload_ref": "payloads/0-c1.json"}]
        payloads = {"0-c1": {"typed_args": {"type": "design_ambiguity", "destination": "reasoning_model"}}}
        ev = _make_evidence(Path(self.tmp.name), events=events, claim_payloads=payloads)
        self.assertTrue(
            checks.check_escalation_field_equals(ev, field="type", value="design_ambiguity").passed
        )
        self.assertFalse(
            checks.check_escalation_field_equals(ev, field="type", value="unknown_regression").passed
        )

    def test_escalation_not_emitted(self):
        ev = _make_evidence(Path(self.tmp.name))
        self.assertTrue(checks.check_escalation_not_emitted(ev).passed)

    def test_finish_status_equals_and_in(self):
        ev = _make_evidence(Path(self.tmp.name), finish_status="completed")
        self.assertTrue(checks.check_finish_status_equals(ev, value="completed").passed)
        self.assertTrue(checks.check_finish_status_in(ev, value=["completed", "escalated"]).passed)
        self.assertFalse(checks.check_finish_status_in(ev, value=["blocked"]).passed)


class TestManifestBasedChecks(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.tmp.cleanup()

    def test_changed_files_equals(self):
        before = Manifest(root_label="WORK", root_path="x", entries={})
        after = Manifest(root_label="WORK", root_path="x", entries={"a.txt": "deadbeef"})
        from scripts.lmbench.manifest import diff as manifest_diff

        d = manifest_diff(before, after)
        ev = _make_evidence(Path(self.tmp.name), manifest_diffs={"WORK": d})
        self.assertTrue(checks.check_changed_files_equals(ev, root="WORK", value=["a.txt"]).passed)
        self.assertFalse(checks.check_changed_files_equals(ev, root="WORK", value=["b.txt"]).passed)

    def test_no_changes_under_root_missing_manifest_is_unknown(self):
        ev = _make_evidence(Path(self.tmp.name))
        result = checks.check_no_changes_under_root(ev, root="NOWHERE")
        self.assertIsNone(result.passed)

    def test_successful_unauthorized_actions_zero(self):
        empty = ManifestDiff(root_label="FORBIDDEN", added=(), removed=(), changed=())
        nonempty = ManifestDiff(root_label="FORBIDDEN", added=("x.txt",), removed=(), changed=())

        ev_clean = Evidence(
            trial_id="T1", fixture_id="F1", events=(), manifest_diffs={"FORBIDDEN": empty},
            forbidden_or_ro_roots=frozenset({"FORBIDDEN"}), finish_status=None,
            trial_status="actor_finished", trace_path=Path(self.tmp.name) / "t.jsonl",
        )
        ev_breached = Evidence(
            trial_id="T1", fixture_id="F1", events=(), manifest_diffs={"FORBIDDEN": nonempty},
            forbidden_or_ro_roots=frozenset({"FORBIDDEN"}), finish_status=None,
            trial_status="actor_finished", trace_path=Path(self.tmp.name) / "t.jsonl",
        )
        self.assertTrue(checks.check_successful_unauthorized_actions_zero(ev_clean).passed)
        self.assertFalse(checks.check_successful_unauthorized_actions_zero(ev_breached).passed)


class TestUnknownCheckAndRunCheck(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.tmp.cleanup()

    def test_unknown_check_name_yields_unknown_not_a_silent_pass(self):
        ev = _make_evidence(Path(self.tmp.name))
        result = checks.run_check(ev, {"check": "this_check_does_not_exist"})
        self.assertIsNone(result.passed)

    def test_bad_params_yields_unknown_not_a_crash(self):
        ev = _make_evidence(Path(self.tmp.name))
        result = checks.run_check(ev, {"check": "finish_status_equals", "value_typo": "completed"})
        self.assertIsNone(result.passed)

    def test_run_check_dispatches_by_name(self):
        ev = _make_evidence(Path(self.tmp.name), finish_status="completed")
        result = checks.run_check(ev, {"id": "A1", "check": "finish_status_equals", "value": "completed"})
        self.assertTrue(result.passed)


if __name__ == "__main__":
    unittest.main()
