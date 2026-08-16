from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone, timedelta
from typing import FrozenSet, Optional

ALLOW = "ALLOW"
GATE = "GATE"


@dataclass(frozen=True)
class AuthorizationWitness:
    authorization_id: str
    authority_ref: str
    basis_digest: str
    allowed_actions: FrozenSet[str]
    target_scope: FrozenSet[str]
    constraints: FrozenSet[str] = field(default_factory=frozenset)
    issued_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    expires_at: Optional[datetime] = None
    status: str = "active"


@dataclass(frozen=True)
class ActionRequest:
    action: str
    target: str
    basis_digest: str
    now: datetime
    payload_digest: Optional[str] = None
    required_payload_digest: Optional[str] = None
    required_constraints_satisfied: bool = True
    objective_evidence_present: bool = True
    source_conflict: bool = False
    duplicate_entity_risk: bool = False
    operator_judgment_required: bool = False
    destructive: bool = False
    irreversible_external: bool = False
    explicit_manual_override: bool = False
    semantic_review_escalates: bool = False


@dataclass(frozen=True)
class Result:
    outcome: str
    reason: str


def in_scope(target: str, scopes: FrozenSet[str]) -> bool:
    if not scopes:
        return False
    return any(target == s or target.startswith(s.rstrip("/") + "/") for s in scopes)


def validate_commit_time(witness: Optional[AuthorizationWitness], req: ActionRequest) -> Result:
    if req.explicit_manual_override:
        return Result(GATE, "explicit_manual_override")
    if req.destructive:
        return Result(GATE, "destructive_action")
    if req.irreversible_external:
        return Result(GATE, "b1_external_or_irreversible_gate")
    if req.source_conflict:
        return Result(GATE, "source_conflict")
    if req.duplicate_entity_risk:
        return Result(GATE, "duplicate_entity_risk")
    if req.operator_judgment_required:
        return Result(GATE, "operator_judgment_required")

    if witness is None:
        return Result(GATE, "missing_authorization_witness")
    if witness.status != "active":
        return Result(GATE, f"authorization_{witness.status}")
    if witness.expires_at is not None and req.now >= witness.expires_at:
        return Result(GATE, "authorization_expired")
    if req.basis_digest != witness.basis_digest:
        return Result(GATE, "basis_digest_changed")
    if req.action not in witness.allowed_actions:
        return Result(GATE, "action_not_authorized")
    if not in_scope(req.target, witness.target_scope):
        return Result(GATE, "target_out_of_scope")
    if req.required_payload_digest is not None and req.payload_digest != req.required_payload_digest:
        return Result(GATE, "payload_digest_mismatch")
    if not req.required_constraints_satisfied:
        return Result(GATE, "constraint_failed")
    if req.action == "objective_status_transition" and not req.objective_evidence_present:
        return Result(GATE, "objective_evidence_missing")
    if req.semantic_review_escalates:
        return Result(GATE, "semantic_review_escalation")

    return Result(ALLOW, "covered_by_active_commit_time_authorization")


def validate_sync_registry_write(*, explicit_operator_non_dry_run_request: bool) -> Result:
    if explicit_operator_non_dry_run_request:
        return Result(ALLOW, "c1_explicit_sync_registry_write_request")
    return Result(GATE, "c1_registry_write_requires_explicit_operator_request")


def main() -> None:
    now = datetime(2026, 8, 16, 17, 50, tzinfo=timezone.utc)
    witness = AuthorizationWitness(
        authorization_id="auth:plan:w34:abc123",
        authority_ref="apex-meta/handoff/plan-packet-w34.md",
        basis_digest="sha256:abc123",
        allowed_actions=frozenset({"canonicalize_exact_plan", "objective_status_transition", "bounded_code_fix"}),
        target_scope=frozenset({"apex-meta/epics/w34", "src/approved-surface"}),
        constraints=frozenset({"preserve_sources", "no_external_send", "no_destructive_write"}),
        issued_at=now - timedelta(hours=1),
        expires_at=now + timedelta(hours=6),
    )

    scenarios = [
        ("exact_plan_serialization", ALLOW, ActionRequest("canonicalize_exact_plan", "apex-meta/epics/w34/001.md", witness.basis_digest, now)),
        ("second_exact_serialization_same_scope", ALLOW, ActionRequest("canonicalize_exact_plan", "apex-meta/epics/w34/002.md", witness.basis_digest, now)),
        ("objective_done_with_evidence", ALLOW, ActionRequest("objective_status_transition", "apex-meta/epics/w34/001.md", witness.basis_digest, now, objective_evidence_present=True)),
        ("objective_done_missing_evidence", GATE, ActionRequest("objective_status_transition", "apex-meta/epics/w34/001.md", witness.basis_digest, now, objective_evidence_present=False)),
        ("changed_basis", GATE, ActionRequest("canonicalize_exact_plan", "apex-meta/epics/w34/001.md", "sha256:changed", now)),
        ("scope_escape", GATE, ActionRequest("bounded_code_fix", "src/unapproved/file.py", witness.basis_digest, now)),
        ("action_escape", GATE, ActionRequest("entity_merge", "apex-meta/epics/w34/001.md", witness.basis_digest, now)),
        ("source_conflict", GATE, ActionRequest("canonicalize_exact_plan", "apex-meta/epics/w34/001.md", witness.basis_digest, now, source_conflict=True)),
        ("duplicate_merge", GATE, ActionRequest("canonicalize_exact_plan", "apex-meta/epics/w34/001.md", witness.basis_digest, now, duplicate_entity_risk=True)),
        ("operator_judgment", GATE, ActionRequest("objective_status_transition", "apex-meta/epics/w34/001.md", witness.basis_digest, now, operator_judgment_required=True)),
        ("external_send_even_if_parent_approved", GATE, ActionRequest("external_send", "external:invoice:123", witness.basis_digest, now, irreversible_external=True)),
        ("destructive_action", GATE, ActionRequest("bounded_code_fix", "src/approved-surface/file.py", witness.basis_digest, now, destructive=True)),
        ("manual_override", GATE, ActionRequest("bounded_code_fix", "src/approved-surface/file.py", witness.basis_digest, now, explicit_manual_override=True)),
        ("semantic_reviewer_escalates", GATE, ActionRequest("bounded_code_fix", "src/approved-surface/file.py", witness.basis_digest, now, semantic_review_escalates=True)),
    ]

    expired = AuthorizationWitness(**{**witness.__dict__, "authorization_id": "auth:expired", "expires_at": now - timedelta(seconds=1)})
    revoked = AuthorizationWitness(**{**witness.__dict__, "authorization_id": "auth:revoked", "status": "revoked"})
    lifecycle = [
        ("expired_authorization", expired, ActionRequest("bounded_code_fix", "src/approved-surface/file.py", witness.basis_digest, now), GATE),
        ("revoked_authorization", revoked, ActionRequest("bounded_code_fix", "src/approved-surface/file.py", witness.basis_digest, now), GATE),
        ("no_witness", None, ActionRequest("bounded_code_fix", "src/approved-surface/file.py", witness.basis_digest, now), GATE),
    ]

    print("CARRIER_SHAPES")
    print("plan_has_new_task_field=false")
    print("plan_operator_gate_authorization_fields=8")
    print("weekly_reuses_existing_basis_digest=true")
    print("weekly_added_scalar_refs=2")
    print("session_added_scalar_refs=3")
    print("sync_reusable_authorization_changes=0")
    print()

    print("SCENARIOS")
    correct = unsafe = overblocked = 0
    for name, expected, req in scenarios:
        res = validate_commit_time(witness, req)
        correct += int(res.outcome == expected)
        unsafe += int(res.outcome == ALLOW and expected == GATE)
        overblocked += int(res.outcome == GATE and expected == ALLOW)
        print(f"{name}: expected={expected} actual={res.outcome} reason={res.reason}")

    for name, wit, req, expected in lifecycle:
        res = validate_commit_time(wit, req)
        correct += int(res.outcome == expected)
        unsafe += int(res.outcome == ALLOW and expected == GATE)
        overblocked += int(res.outcome == GATE and expected == ALLOW)
        print(f"{name}: expected={expected} actual={res.outcome} reason={res.reason}")

    total = len(scenarios) + len(lifecycle)
    print("\nSYNC_C1")
    for explicit in (False, True):
        res = validate_sync_registry_write(explicit_operator_non_dry_run_request=explicit)
        print(f"explicit_operator_non_dry_run_request={str(explicit).lower()}: {res.outcome} {res.reason}")

    print("\nLONG_RUN")
    gates = 0
    for i in range(1, 51):
        req = ActionRequest("bounded_code_fix", f"src/approved-surface/file-{i}.py", witness.basis_digest, now)
        if validate_commit_time(witness, req).outcome == GATE:
            gates += 1
    print(f"covered_internal_actions=50 repeated_operator_gates={gates}")

    print("\nMETRICS")
    print(f"policy_correctness={correct}/{total}")
    print(f"unsafe_allows={unsafe}")
    print(f"overblocks={overblocked}")
    print("new_global_registry_required=false")
    print("new_task_gate_field_required=false")
    print("new_daemon_or_service_required=false")
    print("production_code_claim=false")


if __name__ == "__main__":
    main()
