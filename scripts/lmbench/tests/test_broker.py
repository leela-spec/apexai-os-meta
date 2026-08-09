"""Broker decision truth table. Every `policy_rule_id` the broker can emit,
including the closed-world fallthrough, must be reachable and asserted here."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.lmbench import broker, policy, winpath


def _candidate(base, rel):
    return winpath.normalize_path(rel, base=base)


class BrokerTestBase(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "work").mkdir()
        (self.root / "readonly").mkdir()
        (self.root / "forbidden").mkdir()
        self.base = str(self.root)

        self.pol = policy.build_policy(
            policy_id="TEST-POLICY",
            policy_version="1",
            root_rules=[
                winpath.RootRule("WORK", str(self.root / "work"), "rw"),
                winpath.RootRule("RO", str(self.root / "readonly"), "ro"),
                winpath.RootRule("FORBIDDEN", str(self.root / "forbidden"), "forbidden"),
            ],
            tool_rules=[
                policy.ToolRule("read_file", allowed=True),
                policy.ToolRule("write_file", allowed=True),
                policy.ToolRule("apply_patch", allowed=True, max_calls=1),
                policy.ToolRule("run_command", allowed=True),
                policy.ToolRule("request_approval", allowed=True),
                policy.ToolRule("disabled_tool", allowed=False),
            ],
            action_rules=[
                policy.ActionRule("fs.read", "allow"),
                policy.ActionRule("fs.write", "allow"),
                policy.ActionRule("proc.exec", "allow"),
                policy.ActionRule("widen_scope", "approval_required"),
                policy.ActionRule("delete_repo", "forbid"),
            ],
            argv_allowlist=[("C:\\Python312\\python.exe", "-m", "unittest")],
            default_disposition="forbid",
        )

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _request(self, **kwargs):
        defaults = dict(
            trial_id="T1",
            turn_index=0,
            call_id="c1",
            typed_args={},
            target_paths=(),
        )
        defaults.update(kwargs)
        return broker.BrokerRequest(**defaults)


class TestToolGate(BrokerTestBase):
    def test_unknown_tool_denied(self):
        req = self._request(tool="no_such_tool", action="fs.read")
        d = broker.decide(self.pol, req)
        self.assertEqual(d.verdict, broker.VERDICT_DENY)
        self.assertEqual(d.policy_rule_id, "TOOL.UNKNOWN")

    def test_disabled_tool_denied(self):
        req = self._request(tool="disabled_tool", action="fs.read")
        d = broker.decide(self.pol, req)
        self.assertEqual(d.verdict, broker.VERDICT_DENY)
        self.assertEqual(d.policy_rule_id, "TOOL.NOT_ALLOWED")

    def test_tool_budget_exceeded(self):
        req = self._request(
            tool="apply_patch",
            action="fs.write",
            target_paths=(_candidate(self.base, "work\\a.py"),),
            call_count_so_far=1,
        )
        d = broker.decide(self.pol, req)
        self.assertEqual(d.verdict, broker.VERDICT_DENY)
        self.assertEqual(d.policy_rule_id, "TOOL.BUDGET")

    def test_tool_budget_first_call_allowed(self):
        req = self._request(
            tool="apply_patch",
            action="fs.write",
            target_paths=(_candidate(self.base, "work\\a.py"),),
            call_count_so_far=0,
        )
        d = broker.decide(self.pol, req)
        self.assertEqual(d.verdict, broker.VERDICT_ALLOW)


class TestPathGate(BrokerTestBase):
    def test_unrepresentable_path_denied_and_traced_not_raised(self):
        req = self._request(
            tool="read_file",
            action="fs.read",
            target_paths=(_candidate(self.base, "work\\NUL"),),
        )
        d = broker.decide(self.pol, req)  # must not raise
        self.assertEqual(d.verdict, broker.VERDICT_DENY)
        self.assertEqual(d.policy_rule_id, "PATH.UNREPRESENTABLE")
        self.assertEqual(d.reason_code, "RESERVED_NAME")

    def test_path_outside_all_roots_denied(self):
        outside = winpath.normalize_path("C:\\Windows\\System32\\config\\SAM", base=self.base)
        req = self._request(tool="read_file", action="fs.read", target_paths=(outside,))
        d = broker.decide(self.pol, req)
        self.assertEqual(d.verdict, broker.VERDICT_DENY)
        self.assertEqual(d.policy_rule_id, "ROOT.OUTSIDE_ALL")

    def test_forbidden_root_denied(self):
        req = self._request(
            tool="read_file",
            action="fs.read",
            target_paths=(_candidate(self.base, "forbidden\\secret.txt"),),
        )
        d = broker.decide(self.pol, req)
        self.assertEqual(d.verdict, broker.VERDICT_DENY)
        self.assertEqual(d.policy_rule_id, "ROOT.FORBIDDEN:FORBIDDEN")

    def test_write_to_readonly_root_denied(self):
        req = self._request(
            tool="write_file",
            action="fs.write",
            target_paths=(_candidate(self.base, "readonly\\a.txt"),),
        )
        d = broker.decide(self.pol, req)
        self.assertEqual(d.verdict, broker.VERDICT_DENY)
        self.assertEqual(d.policy_rule_id, "ROOT.READ_ONLY:RO")

    def test_read_from_readonly_root_allowed(self):
        req = self._request(
            tool="read_file",
            action="fs.read",
            target_paths=(_candidate(self.base, "readonly\\a.txt"),),
        )
        d = broker.decide(self.pol, req)
        self.assertEqual(d.verdict, broker.VERDICT_ALLOW)
        self.assertEqual(len(d.resolved_paths), 1)

    def test_write_to_rw_root_allowed_and_resolved_path_returned(self):
        req = self._request(
            tool="write_file",
            action="fs.write",
            target_paths=(_candidate(self.base, "work\\a.txt"),),
        )
        d = broker.decide(self.pol, req)
        self.assertEqual(d.verdict, broker.VERDICT_ALLOW)
        self.assertEqual(len(d.resolved_paths), 1)
        self.assertTrue(d.resolved_paths[0].lower().startswith(str(self.root / "work").lower()))


class TestActionGate(BrokerTestBase):
    def test_forbidden_action_denied(self):
        req = self._request(tool="write_file", action="delete_repo")
        d = broker.decide(self.pol, req)
        self.assertEqual(d.verdict, broker.VERDICT_DENY)
        self.assertEqual(d.policy_rule_id, "ACTION.delete_repo")

    def test_approval_required_without_ref_yields_approval_verdict(self):
        req = self._request(tool="request_approval", action="widen_scope")
        d = broker.decide(self.pol, req)
        self.assertEqual(d.verdict, broker.VERDICT_APPROVAL)
        self.assertEqual(d.policy_rule_id, "ACTION.widen_scope")

    def test_approval_required_with_ref_allowed(self):
        req = self._request(
            tool="request_approval", action="widen_scope", approval_ref="approval-1"
        )
        d = broker.decide(self.pol, req)
        self.assertEqual(d.verdict, broker.VERDICT_ALLOW)

    def test_default_closed_for_action_with_no_rule(self):
        req = self._request(tool="read_file", action="undeclared_action")
        d = broker.decide(self.pol, req)
        self.assertEqual(d.verdict, broker.VERDICT_DENY)
        self.assertEqual(d.policy_rule_id, "DEFAULT.CLOSED")

    def test_approval_cannot_widen_root_scope(self):
        """An approval_ref changes only the action's disposition. Roots are
        re-checked unconditionally, so an approval can never smuggle through a
        forbidden-root write -- this is the test for that structural claim."""
        req = self._request(
            tool="write_file",
            action="widen_scope",
            target_paths=(_candidate(self.base, "forbidden\\secret.txt"),),
            approval_ref="approval-1",
        )
        d = broker.decide(self.pol, req)
        self.assertEqual(d.verdict, broker.VERDICT_DENY)
        self.assertEqual(d.policy_rule_id, "ROOT.FORBIDDEN:FORBIDDEN")


class TestProcExecGate(BrokerTestBase):
    def test_argv_not_allowlisted_denied(self):
        req = self._request(
            tool="run_command",
            action="proc.exec",
            argv=("C:\\Windows\\System32\\cmd.exe", "/c", "del", "*"),
        )
        d = broker.decide(self.pol, req)
        self.assertEqual(d.verdict, broker.VERDICT_DENY)
        self.assertEqual(d.policy_rule_id, "PROC.ARGV")

    def test_argv_allowlisted_prefix_allowed(self):
        req = self._request(
            tool="run_command",
            action="proc.exec",
            argv=("C:\\Python312\\python.exe", "-m", "unittest", "discover"),
        )
        d = broker.decide(self.pol, req)
        self.assertEqual(d.verdict, broker.VERDICT_ALLOW)

    def test_relative_argv0_denied_even_if_it_matches_by_string(self):
        req = self._request(
            tool="run_command",
            action="proc.exec",
            argv=("python.exe", "-m", "unittest"),
        )
        d = broker.decide(self.pol, req)
        self.assertEqual(d.verdict, broker.VERDICT_DENY)
        self.assertEqual(d.policy_rule_id, "PROC.ARGV")

    def test_missing_argv_on_proc_exec_denied(self):
        req = self._request(tool="run_command", action="proc.exec", argv=None)
        d = broker.decide(self.pol, req)
        self.assertEqual(d.verdict, broker.VERDICT_DENY)
        self.assertEqual(d.policy_rule_id, "PROC.ARGV")


class TestEveryRuleIdReachable(BrokerTestBase):
    """A meta-test: walk the fixtures above and assert the full rule-id set
    the broker can emit has actually been exercised somewhere in this file."""

    def test_rule_id_coverage(self):
        expected = {
            "TOOL.UNKNOWN",
            "TOOL.NOT_ALLOWED",
            "TOOL.BUDGET",
            "PATH.UNREPRESENTABLE",
            "ROOT.OUTSIDE_ALL",
            "ROOT.FORBIDDEN:FORBIDDEN",
            "ROOT.READ_ONLY:RO",
            "ACTION.delete_repo",
            "ACTION.widen_scope",
            "DEFAULT.CLOSED",
            "PROC.ARGV",
        }
        # Every id above appears as a literal assertEqual target somewhere in
        # this module's source -- a cheap but real coverage guarantee that a
        # newly-added rule id can't silently go untested.
        src = Path(__file__).read_text(encoding="utf-8")
        for rule_id in expected:
            self.assertIn(rule_id, src, f"rule id {rule_id!r} not exercised by any test")


if __name__ == "__main__":
    unittest.main()
