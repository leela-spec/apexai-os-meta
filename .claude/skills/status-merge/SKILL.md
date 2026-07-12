---
name: status-merge
description: Use this skill to review FlowRecap candidate deltas against confirmed Apex Session and Sync references, record the operator merge decision, and prepare a proposal-only Apex Session mutation request.
---

# Status Merge

## Contract

`status-merge` owns the operator-reviewable proposal between weekly evidence and Apex Session. It does not mutate project state, write Project KB records, create plans, or run Apex Plan or Sync.

```yaml
inputs:
  required: [source_flow_recap_refs, previous_session_or_sync_refs]
  optional: [source_usage_summary_refs, operator_merge_notes, evidence_refs]
outputs:
  - status_merge_packet
  - proposed_apex_session_mutation
  - next_PreCapNextDay_input_context
durable_owner: apex-session
```

## Procedure

1. Load recap evidence, confirmed Session context, and relevant Sync reports by reference.
2. Classify each candidate as accepted-for-mutation, rejected, deferred, or conflicting; preserve evidence and confidence.
3. Present conflicts and the exact operator choice before any accepted candidate.
4. Produce a proposal-only `proposed_apex_session_mutation` for approved candidates; it names status/entity changes, evidence refs, and the required Session receipt.
5. Produce a compact next-planning seed without creating the next-day plan.
6. Return the packet for G5. Only a confirmed G5 decision may be supplied to Apex Session.

## Boundaries

```yaml
boundaries:
  direct_project_or_task_mutation: false
  project_kb_mutation: false
  apex_plan_or_sync_execution: false
  next_day_plan_creation: false
  calendar_or_runtime_creation: false
  durable_write_status: proposal_only
```

## Failure behavior

```yaml
failure_modes:
  missing_confirmed_engine_context: mark_low_confidence_and_request_named_source
  candidate_treated_as_truth: restore_candidate_only_status
  conflict_unresolved: return_blocked_by_conflict
  operator_not_confirmed: preserve_proposal_without_session_handoff
```

## Completion gate

```yaml
completion_gate:
  evidence_refs_present: true
  candidate_and_confirmed_state_separated: true
  operator_decision_visible: true
  apex_session_mutation_request_proposal_only: true
  next_context_compact: true
```
