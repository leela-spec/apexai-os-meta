# Commit-Time Action Authorization — Minimal Contract Draft

Date: 2026-08-16
Status: **pre-implementation design draft; not yet a production skill contract**
Decision basis: A1′ + B1 + C1

## Purpose

Define the smallest authorization contract needed to remove redundant Plan -> Session confirmation while preserving meaningful operator control.

The contract deliberately avoids creating:

- a new authorization service;
- a global authorization registry;
- task-level `gate_mode` fields;
- parent/child policy inheritance;
- a new orchestration layer;
- an AI-only semantic permission engine.

The intended model is: **approval evidence lives in the already-confirmed packet; downstream actors carry a reference to that evidence; the durable-write boundary revalidates it immediately before the effect.**

## Core invariant

> A prior operator approval may authorize a later internal durable action only when the exact action is still covered by the same approved basis, action class, target scope, constraints, validity state, and required evidence at commit time.

A before/after preview remains useful evidence. It stops being an additional semantic approval request when it is an exact consequence of a still-valid authorization witness.

## Minimal witness

```yaml
authorization_witness:
  authorization_id: <stable-id>
  authority_ref: <repo-relative path to the operator-confirmed packet or decision>
  basis_digest: "sha256:<digest>"
  allowed_actions: []
  target_scope: []
  constraints: []
  issued_at: <timestamp>
  expires_at: <timestamp-or-null>
  status: active | revoked | expired
```

### Field rules

- `authorization_id`: stable identity for audit/reference; not a permission by itself.
- `authority_ref`: points to the durable packet that contains the operator decision. No separate authorization database is required.
- `basis_digest`: binds the approval to the reviewed semantic/input basis. Any changed basis invalidates reuse.
- `allowed_actions`: explicit action classes. Examples for the first rollout may include `canonicalize_exact_plan`, `objective_status_transition`, and `bounded_code_fix` when that class is already authorized by the relevant execution packet.
- `target_scope`: explicit repo/entity/resource boundaries. Empty or ambiguous scope fails closed. No implicit nearest-parent inheritance.
- `constraints`: invariants/exclusions that must remain true, such as preserving sources or not performing external sends.
- `issued_at`: audit timestamp.
- `expires_at`: optional but explicit. `null` means no time expiry; basis/scope/status checks still apply. Time-sensitive workflows may set an expiry.
- `status`: current authorization state. Anything other than `active` fails closed.

## Optional exact payload binding

Do **not** add payload hashes to every authorization. Add them only where the action must be bound to an exact pending payload or mutation.

```yaml
payload_binding:
  required: true | false
  payload_digest: null | "sha256:<digest>"
```

For the B1 first rollout, external/irreversible actions remain separately operator-gated, so broad external payload pre-authorization is out of scope.

## Commit-time validation order

The durable-effect boundary evaluates in this fixed order:

```yaml
commit_time_authorization_check:
  1_hard_gate:
    fail_if:
      - explicit_manual_override
      - destructive_action
      - external_or_irreversible_action_under_B1
      - source_conflict
      - duplicate_entity_risk
      - operator_judgment_required

  2_witness_state:
    require:
      - authorization_witness_exists
      - status_is_active
      - not_expired_if_expires_at_is_set

  3_basis_binding:
    require:
      - current_basis_digest_equals_authorized_basis_digest

  4_action_binding:
    require:
      - requested_action_in_allowed_actions

  5_scope_binding:
    require:
      - exact_target_within_target_scope
      - ambiguous_scope_fails_closed

  6_payload_binding:
    when_required:
      - current_payload_digest_equals_authorized_payload_digest

  7_constraints_and_evidence:
    require:
      - deterministic_constraints_pass
      - required_objective_evidence_present

  8_optional_semantic_review:
    behavior:
      - may_escalate_to_operator
      - must_not_override_failed_deterministic_checks
      - is_not_primary_authorization_engine

  9_execute_and_record:
    require:
      - apply_idempotently_or_detect_exact_prior_application
      - preserve_mutation_or_action_receipt
```

## B1 protected actions

The first rollout always raises an action-specific operator gate for:

- external sends/publishes;
- payments/trades;
- destructive deletion/migration;
- other irreversible effects outside bounded internal persistence;
- any action explicitly marked manual by the operator.

Persisting a task that *describes* such an action does not authorize performing it.

## C1 Sync boundary

Apex Sync remains outside reusable authorization for its existing protected write:

```yaml
apex_sync_registry_write:
  dry_run_true: normal_sync_behavior
  dry_run_false:
    requires: explicit_operator_request_under_current_sync_contract
    reusable_authorization_witness_does_not_replace_this_gate: true
```

No Sync skill change is required for the core Plan -> Session duplicate-gate fix unless later implementation reveals a transport-only compatibility need.

## Carrier model — reuse existing artifacts

### Plan

Plan already has `operator_gate`. When the operator approves a handoff, that packet may carry the witness as nested approval evidence:

```yaml
operator_gate:
  state: approved_for_handoff
  operator_validation: confirmed
  authorization:
    authorization_id: ...
    basis_digest: ...
    allowed_actions: [...]
    target_scope: [...]
    constraints: [...]
    issued_at: ...
    expires_at: null
    status: active
```

This does **not** add authorization fields to canonical task records.

### Weekly / Status Merge

Weekly already has `operator_validation` and `authority.basis_digest`. Reuse them and add only the reference needed to identify the approved witness:

```yaml
authority:
  state: verified
  basis_digest: "sha256:<digest>"
  verification_ref: <existing review ref>
  authorization_id: <id>
  authorization_ref: <confirmed packet path>
operator_validation: confirmed
```

A changed packet/source already invalidates its prior digest under the current weekly handoff contract.

### Session

Session should consume a reference rather than copy the full policy:

```yaml
mutation_input:
  operator_validation: confirmed
  authorization_id: <id>
  authorization_ref: <confirmed packet path>
  authorization_basis_digest: "sha256:<digest>"
```

Session resolves/rechecks the referenced witness at commit time. If valid, the existing before/after preview becomes audit evidence rather than a second approval request. If invalid or absent, the existing fresh operator confirmation path remains the fallback.

## Compatibility rule

A consequential Session mutation is confirmable by either:

```yaml
confirmation_basis:
  one_of:
    - fresh_operator_confirmation
    - valid_commit_time_authorization_witness
```

Existing historical records remain valid history. Old approvals that lack stable scope/digest evidence are not retroactively reusable.

## Deliberate non-features

Not included in v1:

- task `gate_mode`;
- portfolio/project/epic inheritance rules;
- global authorization lookup service;
- global TTL policy;
- external action pre-authorization;
- generic Sync registry authorization reuse;
- autonomous conflict resolution;
- AI permission decisions that can override deterministic denial.

## Candidate production home — recommendation, not yet operator-selected

**Recommended:** keep the canonical policy under `apex-session/references/authorization-policy.md` because Session owns the confirmed mutation/commit boundary. Plan and Weekly only carry/reference the witness shape.

Alternative: place it in a shared Workflow & Processes reference if later evidence proves multiple independent mutation executors need to own the same validation algorithm.

Do not create a new shared package merely for architectural symmetry.
