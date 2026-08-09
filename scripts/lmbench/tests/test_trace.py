"""Trace writer/reader: closed enum, fixed field order, fsync-visible,
corrupt-line-reports-its-number."""

from __future__ import annotations

import json
import os
import tempfile
import unittest
from pathlib import Path

from scripts.lmbench import trace


class TestTraceWriter(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name) / "trace.jsonl"
        self.writer = trace.TraceWriter(
            self.path,
            trial_id="T1",
            run_id="R1",
            fixture_id="CODE-01a",
            fixture_version=1,
            configuration_id="CFG-1",
            policy_hash="sha256:abc",
        )

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_unknown_event_type_raises(self):
        with self.assertRaises(trace.TraceError):
            self.writer.emit("not_a_real_event_type")

    def test_emit_writes_fixed_field_order(self):
        self.writer.emit("trial_allocated")
        line = self.path.read_text(encoding="utf-8").strip()
        record = json.loads(line)
        self.assertEqual(tuple(record.keys()), trace._FIELDS)

    def test_emit_returns_stable_event_id_and_increments_seq(self):
        id1 = self.writer.emit("trial_allocated")
        id2 = self.writer.emit("fixture_materialized")
        self.assertNotEqual(id1, id2)
        events = trace.read_trace(self.path)
        self.assertEqual(events[0]["seq"], 1)
        self.assertEqual(events[1]["seq"], 2)

    def test_fsync_makes_data_visible_to_a_second_handle_before_close(self):
        self.writer.emit("trial_allocated")
        # Open a fresh handle without going through our own writer/reader --
        # if fsync weren't happening this could (on some platforms) still be
        # buffered in the writer's own handle.
        with self.path.open("r", encoding="utf-8") as fresh:
            content = fresh.read()
        self.assertIn("trial_allocated", content)

    def test_append_only_never_rewrites_prior_lines(self):
        self.writer.emit("trial_allocated")
        first_write_bytes = self.path.stat().st_size
        self.writer.emit("fixture_materialized")
        second_write_bytes = self.path.stat().st_size
        self.assertGreater(second_write_bytes, first_write_bytes)
        events = trace.read_trace(self.path)
        self.assertEqual(len(events), 2)

    def test_corrupt_line_reports_its_line_number(self):
        self.writer.emit("trial_allocated")
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write("{not valid json\n")
        with self.assertRaises(trace.TraceError) as ctx:
            trace.read_trace(self.path)
        self.assertIn(":2:", str(ctx.exception))

    def test_missing_file_reads_as_empty_list(self):
        missing = Path(self.tmp.name) / "does-not-exist.jsonl"
        self.assertEqual(trace.read_trace(missing), [])

    def test_no_response_bodies_field_exists(self):
        # The trace schema has no field capable of holding a full model
        # response body -- only payload_ref (a pointer) and *_digest (a hash).
        self.assertNotIn("model_response_body", trace._FIELDS)
        self.assertNotIn("content", trace._FIELDS)


class TestReplayAuthority(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name) / "trace.jsonl"
        self.writer = trace.TraceWriter(
            self.path,
            trial_id="T1",
            run_id="R1",
            fixture_id="CODE-01a",
            fixture_version=1,
            configuration_id="CFG-1",
            policy_hash="sha256:abc",
        )

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_replay_authority_returns_only_authority_events_in_order(self):
        self.writer.emit("trial_allocated")
        self.writer.emit("authority_decision", authority_decision="allow", policy_rule_id="A.1")
        self.writer.emit("tool_started")
        self.writer.emit("authority_decision", authority_decision="deny", policy_rule_id="A.2")
        events = trace.read_trace(self.path)
        replay = trace.replay_authority(events)
        self.assertEqual(len(replay), 2)
        self.assertEqual([e["policy_rule_id"] for e in replay], ["A.1", "A.2"])

    def test_event_counts(self):
        self.writer.emit("trial_allocated")
        self.writer.emit("trial_allocated")
        self.writer.emit("tool_started")
        counts = trace.event_counts(trace.read_trace(self.path))
        self.assertEqual(counts["trial_allocated"], 2)
        self.assertEqual(counts["tool_started"], 1)


if __name__ == "__main__":
    unittest.main()
