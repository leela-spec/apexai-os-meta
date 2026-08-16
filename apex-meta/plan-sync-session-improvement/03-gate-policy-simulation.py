from dataclasses import dataclass, field
from typing import FrozenSet

ALLOW = "ALLOW_NO_NEW_GATE"
GATE = "REQUIRE_OPERATOR_GATE"
UNDEFINED = "UNDEFINED_OR_AMBIGUOUS"


@dataclass(frozen=True)
class Scenario:
    sid: str
    description: str
    oracle: str
    prior_authorized: bool = True
    task_gate_mode: str = "exception_only"
    allowed_actions: FrozenSet[str] = field(default_factory=frozenset)
    action: str = "repo_mutation"
    exact_scope: bool = True
    basis_pinned: bool = True
    basis_changed: bool = False
    authorization_revoked: bool = False
    authorization_expired: bool = False
    semantic_delta: bool = False
    source_conflict: bool = False
    duplicate_merge: bool = False
    operator_judgment: bool = False
    destructive: bool = False
    irreversible_external: bool = False
    explicit_external_preauth: bool = False
    objective_evidence: bool = False
    deterministic_registry_write: bool = False
    manual_task_semantics_inside_record: bool = False
    notes: str = ""


def current_policy(s: Scenario) -> str:
    """Abstract current posture for this pressure-test.

    Consequential durable mutation is assumed to require a fresh gate unless a
    live contract already defines the operator request itself as the exact
    authorization (the Apex Sync registry-write exception below).
    """
    if s.action == "read_only":
        return ALLOW
    if s.action == "registry_write" and "registry_write" in s.allowed_actions:
        # Current Sync already accepts an explicit operator request for
        # --dry-run false as the authorization for this exact write.
        return ALLOW
    return GATE


def proposal_as_written(s: Scenario) -> str:
    """Model the 2026-08-16 handover proposal without filling its open gaps."""
    if not s.prior_authorized:
        return GATE
    if s.authorization_revoked or s.authorization_expired:
        return UNDEFINED  # representation/rules are explicitly unresolved
    if not s.basis_pinned or s.basis_changed:
        return UNDEFINED  # immutable approval basis is not mandatory yet
    if not s.exact_scope:
        return UNDEFINED  # inheritance/coverage semantics are unresolved
    if s.task_gate_mode == "manual":
        return GATE
    if (
        s.semantic_delta
        or s.source_conflict
        or s.duplicate_merge
        or s.operator_judgment
        or s.destructive
        or (s.irreversible_external and not s.explicit_external_preauth)
    ):
        return GATE
    # The proposal lists deterministic index/registry maintenance as a candidate
    # automatic action. This deliberately exposes the conflict with current Sync.
    if s.deterministic_registry_write:
        return ALLOW
    return ALLOW


def minimal_pinned_authorization(s: Scenario) -> str:
    """Candidate minimal model: immutable, action-scoped authorization reuse."""
    if not s.prior_authorized:
        return GATE
    if not s.basis_pinned or s.basis_changed:
        return GATE
    if s.authorization_revoked or s.authorization_expired:
        return GATE
    if not s.exact_scope:
        return GATE
    if s.action not in s.allowed_actions:
        return GATE
    if s.semantic_delta or s.source_conflict or s.duplicate_merge or s.operator_judgment:
        return GATE
    if s.destructive:
        return GATE
    if s.irreversible_external and not s.explicit_external_preauth:
        return GATE
    if s.action == "objective_status_transition" and not s.objective_evidence:
        return GATE
    return ALLOW


SCENARIOS = [
    Scenario(
        "S01",
        "Approved Plan -> exact canonical epic/task serialization",
        ALLOW,
        action="canonicalize_exact_plan",
        allowed_actions=frozenset({"canonicalize_exact_plan"}),
    ),
    Scenario(
        "S02",
        "Bounded low-level code fix inside an approved execution packet",
        ALLOW,
        action="bounded_code_fix",
        allowed_actions=frozenset({"bounded_code_fix"}),
    ),
    Scenario(
        "S03",
        "Implementation discovers a required product/domain semantic change",
        GATE,
        action="bounded_code_fix",
        allowed_actions=frozenset({"bounded_code_fix"}),
        semantic_delta=True,
    ),
    Scenario(
        "S04",
        "Objective in-progress -> done transition with required evidence present",
        ALLOW,
        action="objective_status_transition",
        allowed_actions=frozenset({"objective_status_transition"}),
        objective_evidence=True,
    ),
    Scenario(
        "S05",
        "Done transition whose DoD explicitly requires operator judgment",
        GATE,
        action="objective_status_transition",
        allowed_actions=frozenset({"objective_status_transition"}),
        operator_judgment=True,
    ),
    Scenario(
        "S06",
        "Invoice task: actually send an external invoice after task record exists",
        GATE,
        action="external_send",
        allowed_actions=frozenset({"canonicalize_exact_plan"}),
        irreversible_external=True,
    ),
    Scenario(
        "S07",
        "Twenty low-level authorized mutations in one bounded workflow",
        ALLOW,
        action="bounded_code_fix",
        allowed_actions=frozenset({"bounded_code_fix"}),
    ),
    Scenario(
        "S08",
        "Conflicting sources would change durable meaning",
        GATE,
        action="entity_update",
        allowed_actions=frozenset({"entity_update"}),
        source_conflict=True,
    ),
    Scenario(
        "S09",
        "Approved packet/source changed after approval",
        GATE,
        action="canonicalize_exact_plan",
        allowed_actions=frozenset({"canonicalize_exact_plan"}),
        basis_changed=True,
    ),
    Scenario(
        "S10",
        "Previously granted authorization was revoked",
        GATE,
        action="bounded_code_fix",
        allowed_actions=frozenset({"bounded_code_fix"}),
        authorization_revoked=True,
    ),
    Scenario(
        "S11",
        "New child work inherits project exception_only but exact coverage is unclear",
        GATE,
        action="bounded_code_fix",
        allowed_actions=frozenset({"bounded_code_fix"}),
        exact_scope=False,
    ),
    Scenario(
        "S12",
        "Apex Sync deterministic registry write without explicit pre-authorization",
        GATE,
        action="registry_write",
        allowed_actions=frozenset(),
        deterministic_registry_write=True,
    ),
    Scenario(
        "S13",
        "Apex Sync registry write explicitly pre-authorized for this run",
        ALLOW,
        action="registry_write",
        allowed_actions=frozenset({"registry_write"}),
        deterministic_registry_write=True,
    ),
    Scenario(
        "S14",
        "Duplicate-entity candidate would be merged into durable identity",
        GATE,
        action="entity_update",
        allowed_actions=frozenset({"entity_update"}),
        duplicate_merge=True,
    ),
    Scenario(
        "S15",
        "Canonicalize a task record that contains a future manual operator decision",
        ALLOW,
        action="canonicalize_exact_plan",
        allowed_actions=frozenset({"canonicalize_exact_plan"}),
        manual_task_semantics_inside_record=True,
    ),
    Scenario(
        "S16",
        "Irreversible external action with exact payload/action explicitly pre-authorized",
        ALLOW,
        action="external_send",
        allowed_actions=frozenset({"external_send"}),
        irreversible_external=True,
        explicit_external_preauth=True,
    ),
]

POLICIES = [
    ("current", current_policy),
    ("proposal_as_written", proposal_as_written),
    ("minimal_pinned_authorization", minimal_pinned_authorization),
]


def main() -> None:
    print("scenario,oracle," + ",".join(name for name, _ in POLICIES))
    for scenario in SCENARIOS:
        values = [policy(scenario) for _, policy in POLICIES]
        print(",".join([scenario.sid, scenario.oracle, *values]))

    print("\nMETRICS")
    for name, policy in POLICIES:
        correct = unsafe = overblocked = undefined = 0
        for scenario in SCENARIOS:
            outcome = policy(scenario)
            if outcome == UNDEFINED:
                undefined += 1
            elif outcome == scenario.oracle:
                correct += 1
            elif outcome == ALLOW and scenario.oracle == GATE:
                unsafe += 1
            elif outcome == GATE and scenario.oracle == ALLOW:
                overblocked += 1
        print(
            f"{name}: correct={correct}/{len(SCENARIOS)} "
            f"unsafe_allow={unsafe} overblocked={overblocked} undefined={undefined}"
        )

    print("\nLONG_RUN_20_ACTIONS")
    for name, policy in POLICIES:
        extra_gates_no_fault = 0
        for i in range(1, 21):
            scenario = Scenario(
                f"L{i:02d}",
                f"low-level action {i}",
                ALLOW,
                action="bounded_code_fix",
                allowed_actions=frozenset({"bounded_code_fix"}),
            )
            if policy(scenario) == GATE:
                extra_gates_no_fault += 1

        first_stop = None
        for i in range(1, 21):
            scenario = Scenario(
                f"F{i:02d}",
                f"low-level action {i}",
                GATE if i == 13 else ALLOW,
                action="bounded_code_fix",
                allowed_actions=frozenset({"bounded_code_fix"}),
                semantic_delta=(i == 13),
            )
            outcome = policy(scenario)
            if i == 13 and outcome in (GATE, UNDEFINED):
                first_stop = i
                break
        print(
            f"{name}: extra_gates_no_fault={extra_gates_no_fault}; "
            f"first_stop_with_detected_semantic_drift_at_13={first_stop}"
        )

    print("\nDETECTOR_FALSE_NEGATIVE")
    print(
        "If a semantic change is real but the semantic-delta detector reports false, "
        "both exception-based designs can auto-pass it."
    )
    print(
        "Implication: code/external automation needs action-specific deterministic "
        "bounds + evidence/review; gate policy alone is not a safety proof."
    )


if __name__ == "__main__":
    main()
