"""Runner turn-loop mechanics, entirely offline against StubAdapter."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.lmbench import fixtureio, packet, policy, runner, trace, winpath
from scripts.lmbench.adapter import RawResponse, StubAdapter, ToolCall
from scripts.lmbench.fsguard import FsGuard


def _tool_call(call_id, name, args_dict):
    return ToolCall(call_id=call_id, name=name, arguments_raw=json.dumps(args_dict))


def _response(*, content="", tool_calls=(), finish_reason="stop"):
    return RawResponse(
        content=content, reasoning_content=None, tool_calls=tool_calls, finish_reason=finish_reason
    )


class RunnerTestBase(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "work").mkdir()
        (self.root / "forbidden").mkdir()
        (self.root / "forbidden" / "secret.txt").write_text("secret", encoding="utf-8")

        self.pol = policy.build_policy(
            policy_id="RUNNER-TEST",
            policy_version="1",
            root_rules=[
                winpath.RootRule("WORK", str(self.root / "work"), "rw"),
                winpath.RootRule("FORBIDDEN", str(self.root / "forbidden"), "forbidden"),
            ],
            tool_rules=[
                policy.ToolRule("read_file", allowed=True),
                policy.ToolRule("write_file", allowed=True),
                policy.ToolRule("record_evidence", allowed=True),
                policy.ToolRule("request_approval", allowed=True),
                policy.ToolRule("finish", allowed=True),
            ],
            action_rules=[
                policy.ActionRule("fs.read", "allow"),
                policy.ActionRule("fs.write", "allow"),
                policy.ActionRule("evidence.write", "allow"),
                policy.ActionRule("request_approval", "allow"),
                policy.ActionRule("finish", "allow"),
            ],
        )
        self.guard = FsGuard(self.pol.roots)
        self.trace_path = self.root / "trace.jsonl"
        self.tracer = trace.TraceWriter(
            self.trace_path,
            trial_id="T1",
            run_id="R1",
            fixture_id="TEST-FIXTURE",
            fixture_version=1,
            configuration_id="CFG-STUB",
            policy_hash=self.pol.policy_hash,
        )
        self.ctx = runner.ToolContext(workspace_root=str(self.root / "work"))

        fixtures_root = self.root / "fixtures"
        (fixtures_root / "F1").mkdir(parents=True)
        (fixtures_root / "F1" / "packet.md").write_text("Do the thing.", encoding="utf-8")
        public = fixtureio.load_public(fixtures_root, "F1")
        self.compiled = packet.compile_packet(public, ("read_file", "write_file", "finish"))

    def tearDown(self) -> None:
        self.tmp.cleanup()


class TestAllowedAndDeniedCalls(RunnerTestBase):
    def test_allowed_write_then_finish(self):
        stub = StubAdapter(
            [
                _response(
                    tool_calls=(_tool_call("c1", "write_file", {"path": "a.txt", "content": "hi"}),),
                    finish_reason="tool_calls",
                ),
                _response(
                    tool_calls=(_tool_call("c2", "finish", {"status": "completed", "summary": "done"}),),
                    finish_reason="tool_calls",
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
        self.assertEqual(outcome.finish_status, "completed")
        self.assertEqual((self.root / "work" / "a.txt").read_text(encoding="utf-8"), "hi")

        events = trace.read_trace(self.trace_path)
        allowed = [e for e in events if e["event_type"] == "authority_decision"]
        self.assertEqual(len(allowed), 2)
        self.assertTrue(all(e["authority_decision"] == "allow" for e in allowed))

    def test_denied_read_of_forbidden_root_is_traced_and_not_executed(self):
        stub = StubAdapter(
            [
                _response(
                    tool_calls=(_tool_call("c1", "read_file", {"path": "..\\forbidden\\secret.txt"}),),
                    finish_reason="tool_calls",
                ),
                _response(
                    tool_calls=(_tool_call("c2", "finish", {"status": "blocked", "summary": "denied"}),),
                    finish_reason="tool_calls",
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
        events = trace.read_trace(self.trace_path)
        decisions = [e for e in events if e["event_type"] == "authority_decision"]
        self.assertEqual(decisions[0]["authority_decision"], "deny")
        self.assertEqual(decisions[0]["policy_rule_id"], "ROOT.FORBIDDEN:FORBIDDEN")
        # No tool_started for the denied read_file call specifically -- the
        # trial's second call (finish) legitimately does get one.
        read_file_started = [
            e for e in events if e["event_type"] == "tool_started" and e["tool"] == "read_file"
        ]
        self.assertEqual(len(read_file_started), 0)


class TestMalformedAndInvalidArgs(RunnerTestBase):
    def test_malformed_json_arguments_traced_and_fed_back(self):
        bad_call = ToolCall(call_id="c1", name="write_file", arguments_raw="{not json")
        stub = StubAdapter(
            [
                _response(tool_calls=(bad_call,), finish_reason="tool_calls"),
                _response(
                    tool_calls=(_tool_call("c2", "finish", {"status": "completed", "summary": "ok"}),),
                    finish_reason="tool_calls",
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
        events = trace.read_trace(self.trace_path)
        malformed = [e for e in events if e["event_type"] == "tool_call_malformed"]
        self.assertEqual(len(malformed), 1)

    def test_invalid_args_shape_traced_and_fed_back(self):
        stub = StubAdapter(
            [
                _response(
                    tool_calls=(_tool_call("c1", "write_file", {"path": "a.txt"}),),  # missing content
                    finish_reason="tool_calls",
                ),
                _response(
                    tool_calls=(_tool_call("c2", "finish", {"status": "completed", "summary": "ok"}),),
                    finish_reason="tool_calls",
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
        events = trace.read_trace(self.trace_path)
        invalid = [e for e in events if e["event_type"] == "tool_call_invalid_args"]
        self.assertEqual(len(invalid), 1)
        self.assertEqual(invalid[0]["reason_code"], "missing_required:content")


class TestApprovalFlow(RunnerTestBase):
    def test_approval_required_denied_by_default_oracle(self):
        stub = StubAdapter(
            [
                _response(
                    tool_calls=(_tool_call("c1", "request_approval", {"action": "x", "reason": "y"}),),
                    finish_reason="tool_calls",
                ),
                _response(
                    tool_calls=(_tool_call("c2", "finish", {"status": "blocked", "summary": "no approval"}),),
                    finish_reason="tool_calls",
                ),
            ]
        )
        pol = policy.build_policy(
            policy_id="APPROVAL-TEST",
            policy_version="1",
            root_rules=[winpath.RootRule("WORK", str(self.root / "work"), "rw")],
            tool_rules=[
                policy.ToolRule("request_approval", allowed=True),
                policy.ToolRule("finish", allowed=True),
            ],
            action_rules=[
                policy.ActionRule("request_approval", "approval_required"),
                policy.ActionRule("finish", "allow"),
            ],
        )
        outcome = runner.run_trial(
            compiled=self.compiled,
            adapter=stub,
            pol=pol,
            guard=FsGuard(pol.roots),
            tracer=self.tracer,
            ctx=self.ctx,
        )
        self.assertEqual(outcome.status, "actor_finished")
        events = trace.read_trace(self.trace_path)
        self.assertEqual(len([e for e in events if e["event_type"] == "approval_requested"]), 1)
        resolved = [e for e in events if e["event_type"] == "approval_resolved"]
        self.assertEqual(resolved[0]["note"], "denied")


class TestBudgetExhaustion(RunnerTestBase):
    def test_max_turns_exceeded_yields_budget_exhausted_not_infra(self):
        never_finishes = [_response(content="thinking...", tool_calls=(), finish_reason="stop")] * 5
        stub = StubAdapter(never_finishes)
        outcome = runner.run_trial(
            compiled=self.compiled,
            adapter=stub,
            pol=self.pol,
            guard=self.guard,
            tracer=self.tracer,
            ctx=self.ctx,
            config=runner.RunnerConfig(max_turns=3, max_seconds=60.0),
        )
        self.assertEqual(outcome.status, "budget_exhausted")
        self.assertIsNone(outcome.finish_status)


class TestClaimTools(RunnerTestBase):
    def test_record_evidence_is_traced_with_no_filesystem_side_effect(self):
        before = set(p.name for p in (self.root / "work").iterdir())
        stub = StubAdapter(
            [
                _response(
                    tool_calls=(
                        _tool_call(
                            "c1",
                            "record_evidence",
                            {
                                "label": "l",
                                "content": "hostile text preserved verbatim",
                                "trust": "untrusted",
                                "source_ref": "untrusted/note.md",
                            },
                        ),
                    ),
                    finish_reason="tool_calls",
                ),
                _response(
                    tool_calls=(_tool_call("c2", "finish", {"status": "completed", "summary": "ok"}),),
                    finish_reason="tool_calls",
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
        after = set(p.name for p in (self.root / "work").iterdir())
        self.assertEqual(before, after)  # claim tool did no filesystem work
        events = trace.read_trace(self.trace_path)
        completed = [e for e in events if e["event_type"] == "tool_completed" and e["tool"] == "record_evidence"]
        self.assertEqual(len(completed), 1)


if __name__ == "__main__":
    unittest.main()
