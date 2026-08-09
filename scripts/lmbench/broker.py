"""The deterministic capability broker. Pure function, no I/O, no filesystem
access, no subprocess -- importing anything that could touch the machine here
would make "the broker cannot do I/O" unprovable by reading its import block.

`decide()` is closed-world default-deny: every branch below yields a distinct,
traceable `policy_rule_id`, there is no bare `else: allow`, and the walk always
ends at `DEFAULT.CLOSED` if nothing more specific matched. A rejected/malformed
path is *denied and traced*, never raised -- the attempt is the finding, so it
must produce an `authority_decision` event like any other request, not vanish
into an exception handler.

Approval re-entry (`approval_ref` set) re-evaluates every step from scratch.
Only the one action's disposition changes. Roots, tools, and argv are
re-checked unconditionally, so an approval can never widen root scope -- the
classic "approved once, now it's a general capability" failure is structurally
unreachable rather than a rule someone has to remember to enforce.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from hashlib import sha256
from typing import Mapping

from .policy import Policy
from .winpath import PathCandidate

VERDICT_ALLOW = "allow"
VERDICT_DENY = "deny"
VERDICT_APPROVAL = "approval_required"

VERDICTS = frozenset({VERDICT_ALLOW, VERDICT_DENY, VERDICT_APPROVAL})

_WRITE_ACTIONS = frozenset({"fs.write", "fs.delete"})


@dataclass(frozen=True, slots=True)
class BrokerRequest:
    trial_id: str
    turn_index: int
    call_id: str
    tool: str
    action: str
    typed_args: Mapping[str, object]
    target_paths: tuple[PathCandidate, ...] = ()
    argv: tuple[str, ...] | None = None
    approval_ref: str | None = None
    call_count_so_far: int = 0


@dataclass(frozen=True, slots=True)
class Decision:
    verdict: str
    policy_rule_id: str
    reason_code: str
    args_digest: str
    evaluated_rules: tuple[str, ...]
    resolved_paths: tuple[str, ...] = ()


def _args_digest(request: BrokerRequest) -> str:
    payload = json.dumps(dict(request.typed_args), sort_keys=True, default=str)
    return "sha256:" + sha256(payload.encode("utf-8")).hexdigest()


def _argv_allowed(argv: tuple[str, ...], allowlist: tuple[tuple[str, ...], ...]) -> bool:
    if not argv or not os.path.isabs(argv[0]):
        return False
    for prefix in allowlist:
        if prefix and len(prefix) <= len(argv) and tuple(argv[: len(prefix)]) == prefix:
            return True
    return False


def _outcome(
    request: BrokerRequest,
    evaluated: list[str],
    verdict: str,
    rule_id: str,
    reason_code: str,
    resolved_paths: tuple[str, ...] = (),
) -> Decision:
    return Decision(
        verdict=verdict,
        policy_rule_id=rule_id,
        reason_code=reason_code,
        args_digest=_args_digest(request),
        evaluated_rules=tuple(evaluated),
        resolved_paths=resolved_paths,
    )


def decide(policy: Policy, request: BrokerRequest) -> Decision:
    evaluated: list[str] = []

    # 1-2: tool existence and grant.
    evaluated.append("TOOL.LOOKUP")
    tool_rule = policy.tool_rule(request.tool)
    if tool_rule is None:
        return _outcome(request, evaluated, VERDICT_DENY, "TOOL.UNKNOWN", "unknown_tool")
    if not tool_rule.allowed:
        return _outcome(request, evaluated, VERDICT_DENY, "TOOL.NOT_ALLOWED", "tool_not_allowed")
    evaluated.append("TOOL.ALLOWED")

    # 3: per-tool call budget.
    if tool_rule.max_calls is not None:
        evaluated.append("TOOL.BUDGET")
        if request.call_count_so_far >= tool_rule.max_calls:
            return _outcome(request, evaluated, VERDICT_DENY, "TOOL.BUDGET", "tool_budget_exceeded")

    # 4-5: every target path, in order. An unrepresentable path is denied and
    # traced here -- never raised -- because the attempt is itself the finding.
    resolved: list[str] = []
    for candidate in request.target_paths:
        evaluated.append("PATH.CHECK")
        if candidate.reject_code is not None:
            return _outcome(
                request, evaluated, VERDICT_DENY, "PATH.UNREPRESENTABLE", candidate.reject_code
            )
        rule = policy.roots.classify(candidate.cmp)
        if rule is None:
            return _outcome(
                request, evaluated, VERDICT_DENY, "ROOT.OUTSIDE_ALL", "path_outside_all_roots"
            )
        if rule.mode == "forbidden":
            return _outcome(
                request,
                evaluated,
                VERDICT_DENY,
                f"ROOT.FORBIDDEN:{rule.root_id}",
                "forbidden_root",
            )
        if rule.mode == "ro" and request.action in _WRITE_ACTIONS:
            return _outcome(
                request,
                evaluated,
                VERDICT_DENY,
                f"ROOT.READ_ONLY:{rule.root_id}",
                "write_to_readonly_root",
            )
        resolved.append(candidate.real)

    # 6: action disposition. Closed-world: an action with no rule falls to the
    # policy default under an explicit DEFAULT.CLOSED rule id, not a bare else.
    action_rule = policy.action_rule(request.action)
    if action_rule is not None:
        disposition = action_rule.disposition
        rule_id = f"ACTION.{request.action}"
        default_reason = "action_forbidden"
    else:
        disposition = policy.default_disposition
        rule_id = "DEFAULT.CLOSED"
        default_reason = "default_closed"
    evaluated.append(rule_id)

    if disposition == "forbid":
        return _outcome(request, evaluated, VERDICT_DENY, rule_id, default_reason)
    if disposition == "approval_required" and request.approval_ref is None:
        return _outcome(request, evaluated, VERDICT_APPROVAL, rule_id, "approval_required")
    # disposition == "allow", or approval_required with approval_ref supplied --
    # every check above already ran unconditionally in this same call.

    # 7: process-spawn argv allowlist.
    if request.action == "proc.exec":
        evaluated.append("PROC.ARGV")
        if request.argv is None or not _argv_allowed(request.argv, policy.argv_allowlist):
            return _outcome(request, evaluated, VERDICT_DENY, "PROC.ARGV", "argv_not_allowlisted")

    evaluated.append("DEFAULT.ALLOW")
    return _outcome(
        request,
        evaluated,
        VERDICT_ALLOW,
        rule_id,
        "allowed",
        resolved_paths=tuple(resolved),
    )


__all__ = [
    "VERDICT_ALLOW",
    "VERDICT_DENY",
    "VERDICT_APPROVAL",
    "VERDICTS",
    "BrokerRequest",
    "Decision",
    "decide",
]
