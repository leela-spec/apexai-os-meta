# APEX Minimal Status Merge Example

This example shows a minimal, synthetic StatusMerge run for APEX only.

It demonstrates how to consume one validated `flow_recap_packet` reference and one opaque `usage_summary` reference, produce one `status_merge_packet`, surface one accepted candidate delta, surface one deferred/conflict note, and produce one `next_PreCapNextDay_input_context`.

This example does **not** mutate an actual project KB, overwrite project state, create a PreCapNextDay plan, create calendar events, start an agent, schedule anything, or trigger runtime execution.

---

## 1. Synthetic Inputs

### 1.1 Validated FlowRecap Packet Ref

```yaml
synthetic_flow_recap_packet:
  ref_id: flow_recap_packet_2026_07_06_apex_status_merge_minimal
  artifact_name: flow_recap_packet
  validation_status: valid
  source_note: synthetic_example_only
  candidate_project_status_deltas:
    - candidate_id: candidate_delta_status_merge_contract_done
      candidate_only: true
      target_project_ref: apex_status_merge_skill_package
      delta_summary: >
        StatusMerge now has interface contracts for the status_merge_packet and
        next_PreCapNextDay_input_context, and an operator-facing packet template.
      evidence_refs:
        - commit:9dc21016090e46b3f797a617956c8caf7825a3c7
        - commit:772d4d56243ebc95c2f10aba3e722c6e19b0e0e3
        - commit:bb795f81bb30049668104839144fb550ee5cbcc0
      confidence: high
  next_step_candidates:
    - candidate_id: next_step_add_example_manifest_and_skill
      candidate_only: true
      action_summary: >
        Complete the minimal example, package manifest, and SKILL.md while
        preserving the project-kb-manager durable write boundary.
      evidence_refs:
        - ref: status_merge_packet_contract
        - ref: next_precap_handoff_context_contract
        - ref: status_merge_packet_template
      confidence: high
```

### 1.2 Synthetic Usage Summary Ref

```yaml
synthetic_usage_summary:
  ref_id: usage_summary_2026_07_06_status_merge_minimal
  artifact_name: usage_summary
  source_note: >
    Synthetic opaque reference only. This example does not define or validate the
    usage_summary schema because that schema belongs outside status-merge.
  status: opaque_reference_only
```

### 1.3 Previous State Refs

```yaml
previous_state_refs:
  - ref_id: project_kb_record_apex_status_merge_skill_package
    owner: project-kb-manager
    status: available
  - ref_id: current_project_status_overview_apex_2026_07_06
    owner: ProjectStatus
    status: available
```

---

## 2. Produced Status Merge Packet

```yaml
status_merge_packet:
  merge_packet_id: status_merge_packet_2026_07_06_apex_minimal_example
  artifact_name: status_merge_packet
  created_or_updated_at: 2026-07-06
  merge_scope: single_flow
  validation_status: operator_review_recommended

  source_flow_recap_refs:
    - ref_id: flow_recap_packet_2026_07_06_apex_status_merge_minimal
      status: validated
      note: Synthetic FlowRecap packet with one accepted project-status candidate.

  source_usage_summary_refs:
    - ref_id: usage_summary_2026_07_06_status_merge_minimal
      status: opaque_reference_only
      note: Usage context is referenced only and not schema-expanded here.

  previous_state_refs:
    - ref_id: project_kb_record_apex_status_merge_skill_package
      owner: project-kb-manager
      status: available
    - ref_id: current_project_status_overview_apex_2026_07_06
      owner: ProjectStatus
      status: available
```

---

## 3. Operator Review Flags

```yaml
operator_review_flags:
  requires_operator_review: true
  project_kb_manager_write_required: true
  conflicts_present: true
  blocked_by_missing_state_owner: false
  auto_write_allowed: false
  auto_trigger_allowed: false
```

### Review Summary Card

- **Merge intent:** Consolidate one synthetic validated FlowRecap candidate into a StatusMerge proposal for the APEX status-merge skill package.
- **Recommended operator action:** Review and accept the project-kb-manager update proposal if the package progress should be recorded durably.
- **Primary risk:** Treating the proposal as a durable status update before project-kb-manager confirmation.
- **State owner boundary:** Durable project KB writes must go through `project-kb-manager`.
- **Next planning impact:** The next PreCapNextDay input context can include continuing the package build with manifest and SKILL.md.

---

## 4. Prominent Conflict / Deferred Note

```yaml
conflict_notes:
  - conflict_id: conflict_usage_summary_contract_missing
    severity: medium
    conflict_type: usage_summary_incomplete
    conflict_summary: >
      The status-merge package can reference usage summaries, but the dedicated
      usage-summary contract was not available during source inspection.
    source_refs:
      - usage_summary_2026_07_06_status_merge_minimal
      - source_gap:.claude/skills/model-usage-log/references/usage-summary-contract.md
    affected_state_refs:
      - status_merge_packet_2026_07_06_apex_minimal_example
    required_operator_decision: >
      Decide whether an opaque usage_summary_ref is sufficient for this package
      stage or whether model-usage-log must first publish its usage-summary
      contract.
    proposed_resolution: >
      Keep usage_summary_ref as opaque reference-only and do not define the
      usage_summary schema inside status-merge.
    blocks_project_kb_write: false
    blocks_next_PreCapNextDay_context: false
```

### Conflict Card

#### Conflict: `conflict_usage_summary_contract_missing`

- **Severity:** Medium
- **Type:** `usage_summary_incomplete`
- **What conflicts:** Usage summaries are referenced, but their source contract is missing.
- **Evidence:** Synthetic usage ref plus recorded source gap.
- **Affected state:** StatusMerge output can remain valid with warning/operator review.
- **Operator decision needed:** Accept opaque reference-only handling or block until the usage contract exists.
- **Proposed resolution:** Keep usage context reference-only in this package.
- **Blocks:** Neither project KB write nor next PreCap context in this example.

---

## 5. Accepted Delta Candidate

```yaml
accepted_delta_candidates:
  - candidate_id: candidate_delta_status_merge_contract_done
    source_ref: flow_recap_packet_2026_07_06_apex_status_merge_minimal
    delta_summary: >
      StatusMerge package now has interface contracts and a packet template
      establishing operator-gated merge proposals and next PreCap context seed.
    proposed_destination: project_kb_manager_update_proposal
    acceptance_basis: >
      The candidate is supported by synthetic refs to the package files created
      in the current APEX status-merge package build flow.
    operator_confirmation_status: not_confirmed
    project_kb_manager_write_boundary: proposal_only_until_confirmed
```

### Accepted Candidate Card

#### Accepted Candidate: `candidate_delta_status_merge_contract_done`

- **Source:** `flow_recap_packet_2026_07_06_apex_status_merge_minimal`
- **Delta:** Interface contracts and template are ready for operator review.
- **Why accepted into proposal:** The files exist as package artifacts and preserve the no-runtime/no-auto-write boundary.
- **Proposed destination:** `project_kb_manager_update_proposal`
- **Write status:** Proposal only unless confirmed through `project-kb-manager`.
- **Next planning effect:** Continue with example, package manifest, and SKILL.md finalization.

---

## 6. Rejected or Deferred Delta Candidates

```yaml
rejected_or_deferred_delta_candidates:
  - candidate_id: candidate_delta_usage_summary_schema_embed
    source_ref: usage_summary_2026_07_06_status_merge_minimal
    delta_summary: >
      Embed or recreate usage_summary schema fields inside status-merge.
    disposition: deferred
    reason: >
      The usage summary schema is outside status-merge ownership and its source
      contract is missing. StatusMerge must keep usage references opaque.
```

### Deferred Candidate Card

#### Deferred Candidate: `candidate_delta_usage_summary_schema_embed`

- **Source:** `usage_summary_2026_07_06_status_merge_minimal`
- **Delta:** Define usage summary schema inside status-merge.
- **Reason deferred:** Wrong ownership and missing source authority.
- **Unblock condition:** model-usage-log publishes the usage-summary contract, after which StatusMerge may reference it but still not own it.
- **Revisit context:** Package audit or model-usage-log integration review.

---

## 7. Proposed Project KB Update

This is a proposal only. It is not a write.

```yaml
proposed_project_kb_update:
  proposal_id: project_kb_update_proposal_status_merge_minimal
  durable_write_owner: project-kb-manager
  target_project_refs:
    - apex_status_merge_skill_package
  proposed_changes_summary:
    - >
      Record that status-merge now has packet contract, next PreCap handoff
      context contract, and operator-facing packet template drafted.
    - >
      Record that usage_summary remains reference-only because its source
      contract is missing.
  blocked_changes:
    - blocked_change_id: blocked_usage_summary_schema_embedding
      reason: missing evidence and wrong state owner
      source_refs:
        - source_gap:.claude/skills/model-usage-log/references/usage-summary-contract.md
  operator_gate_status: ready_for_operator_review
```

### Project KB Update Review Card

- **Durable write owner:** `project-kb-manager`
- **Proposed records affected:** `apex_status_merge_skill_package`
- **Changes ready for review:** Package status can reflect the created interface files.
- **Changes blocked:** Embedding usage_summary schema.
- **Operator gate:** `ready_for_operator_review`
- **Explicit warning:** Do not directly edit project KB durable records from this example.

---

## 8. Updated All-Project Status Packet View

This is a view/proposal only.

```yaml
updated_all_project_status_packet:
  view_id: updated_all_project_status_packet_2026_07_06_apex_minimal
  source_status_merge_packet_ref: status_merge_packet_2026_07_06_apex_minimal_example
  accepted_delta_register_view:
    - candidate_delta_status_merge_contract_done
  consumed_recap_candidate_list:
    - recap_ref: flow_recap_packet_2026_07_06_apex_status_merge_minimal
      disposition: partially_accepted
  project_status_summary:
    - project_ref: apex_status_merge_skill_package
      status_view: >
        Interface package build is in progress. Contracts and template are ready;
        example, manifest, and SKILL.md are next.
      source_refs:
        - commit:9dc21016090e46b3f797a617956c8caf7825a3c7
        - commit:772d4d56243ebc95c2f10aba3e722c6e19b0e0e3
        - commit:bb795f81bb30049668104839144fb550ee5cbcc0
  unresolved_conflicts:
    - conflict_usage_summary_contract_missing
```

---

## 9. Next PreCapNextDay Input Context

This is a compact seed for PreCapNextDay. It is not a PreCapNextDay plan.

```yaml
next_PreCapNextDay_input_context:
  context_id: next_precap_context_2026_07_06_status_merge_minimal
  created_or_updated_at: 2026-07-06
  source_status_merge_packet_ref: status_merge_packet_2026_07_06_apex_minimal_example
  updated_project_focus:
    - focus_id: focus_status_merge_package_completion
      project_ref: apex_status_merge_skill_package
      focus_summary: Complete the status-merge interface package without crossing runtime or durable-write boundaries.
      source_refs:
        - status_merge_packet_2026_07_06_apex_minimal_example
      status: continued_focus
  active_next_actions:
    - action_id: action_create_manifest_and_skill_md
      project_ref: apex_status_merge_skill_package
      action_summary: Create package manifest and SKILL.md after this example is accepted.
      action_status: ready_for_precap_consideration
      source_refs:
        - candidate_delta_status_merge_contract_done
  blockers:
    - blocker_id: blocker_usage_summary_contract_missing
      blocker_summary: Dedicated usage-summary contract is missing, so usage remains opaque reference-only.
      affected_project_refs:
        - apex_status_merge_skill_package
      source_refs:
        - conflict_usage_summary_contract_missing
      resolution_needed: missing_evidence
  unresolved_operator_decisions:
    - decision_id: decision_accept_opaque_usage_summary_ref
      decision_summary: Accept opaque usage_summary_ref handling for this interface-only package stage.
      options:
        - accept_reference_only_usage_summary
        - block_until_usage_summary_contract_exists
      source_refs:
        - conflict_usage_summary_contract_missing
      impact_if_unresolved: limits_next_precap_confidence
  usage_summary_ref: usage_summary_2026_07_06_status_merge_minimal
  evidence_refs:
    - flow_recap_packet_2026_07_06_apex_status_merge_minimal
    - usage_summary_2026_07_06_status_merge_minimal
    - project_kb_record_apex_status_merge_skill_package
  confidence:
    level: medium
    rationale: >
      The package boundary is clear and the accepted delta is supported, but one
      upstream usage-summary contract is missing.
    limiting_factors:
      - missing_usage_summary_contract
  validation_status: operator_review_recommended
```

### Next PreCap Context Card

- **Primary focus for next PreCapNextDay:** Complete package manifest and SKILL.md while preserving boundaries.
- **Ready actions:** Create remaining package files in sequence.
- **Blocked actions:** Do not embed usage_summary schema inside status-merge.
- **Operator decisions carried forward:** Whether opaque usage_summary_ref is sufficient for this stage.
- **Usage context:** `usage_summary_2026_07_06_status_merge_minimal`
- **Confidence:** Medium, because one source contract is missing.

---

## 10. Non-Mutation Statement

```yaml
non_mutation_statement:
  project_kb_mutated: false
  project_state_overwritten: false
  PreCapNextDay_plan_created: false
  calendar_event_created: false
  runtime_triggered: false
  scheduler_created: false
  agent_created: false
  durable_write_required_owner: project-kb-manager
```

```text
This example produces a status_merge_packet proposal and next_PreCapNextDay_input_context seed only. It does not mutate project KB, overwrite files, or create a PreCapNextDay plan.
```
