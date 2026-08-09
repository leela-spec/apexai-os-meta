"""Frozen capability policy: the broker's sole input. Stdlib only.

`Policy` is a parameter to `broker.decide()`, never module state -- there is no
global to mutate, which is what makes VAL-15 (injected content cannot mutate
policy) checkable by construction rather than by convention: every field is a
`tuple` inside a `frozen=True, slots=True` dataclass, so any attempted
assignment raises `FrozenInstanceError` before it could matter.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from hashlib import sha256

from .errors import PolicyError
from .winpath import RootRule, RootSet

_DISPOSITIONS = frozenset({"allow", "approval_required", "forbid"})


@dataclass(frozen=True, slots=True)
class ToolRule:
    tool: str
    allowed: bool
    max_calls: int | None = None


@dataclass(frozen=True, slots=True)
class ActionRule:
    action: str
    disposition: str

    def __post_init__(self) -> None:
        if self.disposition not in _DISPOSITIONS:
            raise PolicyError(
                f"invalid disposition {self.disposition!r} for action {self.action!r}"
            )


@dataclass(frozen=True, slots=True)
class Policy:
    policy_id: str
    policy_version: str
    roots: RootSet
    tools: tuple[ToolRule, ...]
    actions: tuple[ActionRule, ...]
    argv_allowlist: tuple[tuple[str, ...], ...] = ()
    default_disposition: str = "forbid"
    policy_hash: str = ""

    def __post_init__(self) -> None:
        if self.default_disposition not in _DISPOSITIONS:
            raise PolicyError(f"invalid default_disposition {self.default_disposition!r}")

    def tool_rule(self, tool: str) -> ToolRule | None:
        for entry in self.tools:
            if entry.tool == tool:
                return entry
        return None

    def action_rule(self, action: str) -> ActionRule | None:
        for entry in self.actions:
            if entry.action == action:
                return entry
        return None


def canonical_policy_json(policy: Policy) -> str:
    """Deterministic JSON of every field that defines the policy's *meaning* --
    excludes `policy_hash` itself, so this is exactly what the hash is computed over."""
    payload = {
        "policy_id": policy.policy_id,
        "policy_version": policy.policy_version,
        "roots": sorted(
            (
                {"root_id": r.root_id, "real_path": r.cmp_path, "mode": r.mode}
                for r in policy.roots.entries
            ),
            key=lambda r: r["root_id"],
        ),
        "tools": sorted(
            (
                {"tool": t.tool, "allowed": t.allowed, "max_calls": t.max_calls}
                for t in policy.tools
            ),
            key=lambda t: t["tool"],
        ),
        "actions": sorted(
            ({"action": a.action, "disposition": a.disposition} for a in policy.actions),
            key=lambda a: a["action"],
        ),
        "argv_allowlist": sorted(list(prefix) for prefix in policy.argv_allowlist),
        "default_disposition": policy.default_disposition,
    }
    return json.dumps(payload, sort_keys=True, separators=(",", ":"))


def compute_policy_hash(policy: Policy) -> str:
    return "sha256:" + sha256(canonical_policy_json(policy).encode("utf-8")).hexdigest()


def build_policy(
    *,
    policy_id: str,
    policy_version: str,
    root_rules,
    tool_rules,
    action_rules,
    argv_allowlist=(),
    default_disposition: str = "forbid",
) -> Policy:
    """The only supported way to construct a `Policy` -- computes and freezes
    `policy_hash` after construction, so callers never hand-compute it and risk
    a hash that doesn't match its own content."""
    policy = Policy(
        policy_id=policy_id,
        policy_version=policy_version,
        roots=RootSet.build(list(root_rules)),
        tools=tuple(tool_rules),
        actions=tuple(action_rules),
        argv_allowlist=tuple(tuple(prefix) for prefix in argv_allowlist),
        default_disposition=default_disposition,
    )
    object.__setattr__(policy, "policy_hash", compute_policy_hash(policy))
    return policy


__all__ = [
    "RootRule",
    "ToolRule",
    "ActionRule",
    "Policy",
    "canonical_policy_json",
    "compute_policy_hash",
    "build_policy",
]
