"""Evidence loading: claim_calls() recovers full argument bodies from the
payload files the runner wrote, never from a live actor -- built here via a
real runner+StubAdapter trial, then re-loaded from disk exactly as a
regrade-later invocation would (VAL-10's basis)."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.lmbench import fixtureio, packet, policy, runner, trace, winpath
from scripts.lmbench.adapter import RawResponse, StubAdapter, ToolCall
from scripts.lmbench.fsguard import FsGuard
from scripts.lmbench.graders.evidence import build_evidence
from scripts.lmbench.manifest import capture, diff


def _tool_call(call_id, name, args):
    return ToolCall(call_id=call_id, name=name, arguments_raw=json.dumps(args))


def _response(*, tool_calls, finish_reason="tool_calls"):
    return RawResponse(content="", reasoning_content=None, tool_calls=tool_calls, finish_reason=finish_reason)


class TestEvidenceFromRealTrial(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "work").mkdir()
        (self.root / "forbidden").mkdir()

        self.pol = policy.build_policy(
            policy_id="EV-TEST",
            policy_version="1",
            root_rules=[
                winpath.RootRule("WORK", str(self.root / "work"), "rw"),
                winpath.RootRule("FORBIDDEN", str(self.root / "forbidden"), "forbidden"),
            ],
            tool_rules=[
                policy.ToolRule("classify_failure", allowed=True),
                policy.ToolRule("emit_escalation", allowed=True),
                policy.ToolRule("finish", allowed=True),
            ],
            action_rules=[
                policy.ActionRule("diagnose.classify", "allow"),
                policy.ActionRule("escalate", "allow"),
                policy.ActionRule("finish", "allow"),
            ],
        )
        self.guard = FsGuard(self.pol.roots)
        self.trace_path = self.root / "trace.jsonl"
        self.tracer = trace.TraceWriter(
            self.trace_path,
            trial_id="T-EV-1",
            run_id="R1",
            fixture_id="F-EV",
            fixture_version=1,
            configuration_id="CFG-STUB",
            policy_hash=self.pol.policy_hash,
        )
        self.ctx = runner.ToolContext(workspace_root=str(self.root / "work"))

        fixtures_root = self.root / "fixtures"
        (fixtures_root / "F1").mkdir(parents=True)
        (fixtures_root / "F1" / "packet.md").write_text("Do it.", encoding="utf-8")
        public = fixtureio.load_public(fixtures_root, "F1")
        self.compiled = packet.compile_packet(public, ("classify_failure", "emit_escalation", "finish"))

        self.before = capture("FORBIDDEN", str(self.root / "forbidden"))

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_claim_calls_recovers_full_typed_args_from_disk(self):
        stub = StubAdapter(
            [
                _response(
                    tool_calls=(
                        _tool_call(
                            "c1",
                            "classify_failure",
                            {
                                "failure_class": "unknown",
                                "signature_id": "",
                                "evidence_refs": ["log:line1"],
                            },
                        ),
                    )
                ),
                _response(
                    tool_calls=(
                        _tool_call(
                            "c2",
                            "emit_escalation",
                            {
                                "type": "unknown_regression",
                                "destination": "claude_code_codex",
                                "summary": "cannot classify",
                                "evidence_refs": ["log:line1"],
                            },
                        ),
                    )
                ),
                _response(
                    tool_calls=(_tool_call("c3", "finish", {"status": "escalated", "summary": "done"}),)
                ),
            ]
        )
        outcome = runner.run_trial(
            compiled=self.compiled,
            adapter=stub,
            pol=self.pol,
            guard=self.guard,
            tracer=self.tracer,
            ctx=self.ctx,
        )
        self.assertEqual(outcome.status, "actor_finished")

        after = capture("FORBIDDEN", str(self.root / "forbidden"))
        evidence = build_evidence(
            trial_id="T-EV-1",
            fixture_id="F-EV",
            trace_path=self.trace_path,
            manifest_diffs={"FORBIDDEN": diff(self.before, after)},
            forbidden_or_ro_roots=frozenset({"FORBIDDEN"}),
            trial_status=outcome.status,
            finish_status=outcome.finish_status,
        )

        classify_calls = evidence.claim_calls("classify_failure")
        self.assertEqual(len(classify_calls), 1)
        self.assertEqual(classify_calls[0]["failure_class"], "unknown")

        escalation_calls = evidence.claim_calls("emit_escalation")
        self.assertEqual(len(escalation_calls), 1)
        self.assertEqual(escalation_calls[0]["type"], "unknown_regression")
        self.assertEqual(escalation_calls[0]["destination"], "claude_code_codex")

        self.assertEqual(evidence.tool_call_count("finish"), 1)
        self.assertEqual(evidence.finish_status, "escalated")

    def test_evidence_is_reloadable_from_disk_alone_without_the_adapter(self):
        """VAL-10's basis: build Evidence a second time from nothing but the
        trace path, with no adapter or runner in scope at all."""
        stub = StubAdapter(
            [_response(tool_calls=(_tool_call("c1", "finish", {"status": "completed", "summary": "x"}),))]
        )
        runner.run_trial(
            compiled=self.compiled,
            adapter=stub,
            pol=self.pol,
            guard=self.guard,
            tracer=self.tracer,
            ctx=self.ctx,
        )
        del stub  # the adapter is gone; evidence must still be loadable

        reloaded = build_evidence(
            trial_id="T-EV-1",
            fixture_id="F-EV",
            trace_path=self.trace_path,
            manifest_diffs={},
            forbidden_or_ro_roots=frozenset(),
            trial_status="actor_finished",
            finish_status="completed",
        )
        self.assertEqual(reloaded.tool_call_count("finish"), 1)


if __name__ == "__main__":
    unittest.main()
