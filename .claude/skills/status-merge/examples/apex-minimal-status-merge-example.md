# APEX Minimal Status Merge Example

This example shows a minimal, synthetic StatusMerge run.

It demonstrates how to consume one validated `flow_recap_packet` reference and one `usage_summary` reference, produce one `status_merge_packet`, surface one accepted candidate delta, surface one deferred/conflict note, and produce one `next_PreCapNextDay_input_context`.

This example does **not** mutate an actual project KB, overwrite project state, create a PreCapNextDay plan, create calendar events, or trigger runtime execution.

---

## 1. Synthetic Inputs

### 1.1 Validated FlowRecap Packet Ref

```yaml
synthetic_flow_recap_packet:
  ref_id: flow_recap_packet_2026_07_06_apex_skill_boundary_review
  artifact_name: flow_recap_packet
  validation_status: valid_with_warnings
  source_note: synthetic_example_only
  candidate_project_status_deltas:
    - candidate_id: candidate_project_status_delta_boundary_doc_done
      candidate_only: true
      target_project_ref: apex_status_merge_skill_package
      delta_summary: >
        The status-merge package now has an initial packet contract and next
        PreCap handoff context contract drafted as interface-only artifacts.
      evidence_refs:
        - commit:3eaa1da9d6c49a8b6dc966fa43899f1d9f70c5c4
        - commit:c1f8edbea08ae0cd2e345f36751e2d3b9550a969
      confidence: high
  next_step_candidates:
    - candidate_id: next_step_template_review
      candidate_only: true
      action_summary: Review the status_merge_packet template for operator readability.
      evidence_refs:
        - commit:e3bf1e892e4b211cbb8fad022a83c6a83386c67c
      confidence: medium
```

### 1.2 Synthetic Usage Summary Ref

```yaml
synthetic_usage_summary:
  ref_id: usage_summary_2026_07_06_status_merge_example
  artifact_name: usage_summary
  source_note: >
    Synthetic opaque reference only. This example does not define or validate the
    usage_summary schema because that schema belongs to model-usage-log.
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
  source_flow_recap_refs:
    - ref_id: flow_recap_packet_2026_07_06_apex_skill_boundary_review
      status: validated_with_warnings
      note: Synthetic FlowRecap candidate packet used for minimal example.
  source_usage_summary_refs:
    - ref_id: usage_summary_2026_07_06_status_merge_example
      status: opaque_reference_only
      note: Usage schema is not owned by status-merge.
  previous_state_refs:
    - ref_id: project_kb_record_apex_status_merge_skill_package
      owner: project-kb-manager
      status: available
    - ref_id: current_project_status_overview_apex_2026_07_06
      owner: ProjectStatus
      status: available
  merge_scope: single_flow
```

---

## 3. Operator Review First

```yaml
operator_review_flags:
  requires_operator_review: true
  project_kb_manager_write_required: true
  conflicts_present: true
  blocked_by_missing_state_owner: false
  auto_write_allowed: false
  auto_trigger_allowed: false
```

- **Merge intent:** Consolidate validated recap candidates about the emerging `status-merge` interface package into a proposal packet.
- **Recommended operator action:** Accept the safe package-progress delta, review the deferred conflict note, then route any durable KB update through `project-kb-manager`.
- **Primary risk:** Treating a merge proposal as durable project state before operator review.
- **State owner boundary:** Durable project KB writes remain owned by `project-kb-manager`.
- **Next planning impact:** Provides a compact seed for PreCapNextDay, not a next-day plan.

---

## 4. Conflict / Deferred Note

```yaml
conflict_notes:
  - conflict_id: conflict_usage_summary_contract_missing
    severity: medium
    conflict_summary: >
      The package needs a usage_summary_ref for next planning context, but the
      declared usage-summary contract is missing from the repository source set.
    source_refs:
      - usage_summary_2026_07_06_status_merge_example
    affected_state_refs:
      - next_PreCapNextDay_input_context.usage_summary_ref
    required_operator_decision: >
      Decide whether to keep usage_summary_ref as an opaque optional reference
      until model-usage-log defines a usage-summary contract.
    proposed_resolution: >
      Keep usage_summary_ref nullable and opaque; do not define usage_summary
      schema inside status-merge.
    blocks_project_kb_write: false
    blocks_next_PreCapNextDay_context: false
```

### Conflict Card

#### Conflict: `conflict_usage_summary_contract_missing`

- **Severity:** medium
- **What conflicts:** A required downstream reference exists, but the owner schema source is missing.
- **Evidence:** `usage_summary_2026_07_06_status_merge_example`
- **Affected state:** `next_PreCapNextDay_input_context.usage_summary_ref`
- **Operator decision needed:** Keep opaque nullable reference or pause until model-usage-log adds a contract.
- **Proposed resolution:** Keep the reference nullable and do not redefine owner schema.
- **Blocks:** neither project KB write nor next PreCap context, if flagged clearly.

---

## 5. Accepted Delta Candidate

```yaml
accepted_delta_candidates:
  - candidate_id: accepted_delta_status_merge_contracts_started
    source_ref: flow_recap_packet_2026_07_06_apex_skill_boundary_review
    delta_type: project_status
    target_owner: project-kb-manager
    target_ref: project_kb_record_apex_status_merge_skill_package
    proposed_change_summary: >
      Record that the status-merge interface package has started and now has
      the packet contract, next PreCap handoff context contract, and operator
      template drafted as proposal/reference artifacts.
    acceptance_basis: >
      The candidate is backed by concrete package-file commits and stays within
      interface-package boundaries.
    evidence_refs:
      - commit:3eaa1da9d6c49a8b6dc966fa43899f1d9f70c5c4
      - commit:c1f8edbea08ae0cd2e345f36751e2d3b9550a969
      - commit:e3bf1e892e4b211cbb8fad022a83c6a83386c67c
    confidence: high
    durable_write_status: proposal_only
```

### Accepted Candidate Card

#### Accepted Candidate: `accepted_delta_status_merge_contracts_started`

- **Target owner:** `project-kb-manager`
- **Target ref:** `project_kb_record_apex_status_merge_skill_package`
- **Change proposed:** Mark the interface package as started with initial contracts and template drafted.
- **Why accepted into packet:** Evidence-backed and boundary-safe.
- **Evidence:** three package-file commits.
- **Confidence:** high
- **Durable write status:** `proposal_only`

---

## 6. Rejected or Deferred Delta Candidate

```yaml
rejected_or_deferred_delta_candidates:
  - candidate_id: deferred_delta_mark_status_merge_complete
    source_ref: flow_recap_packet_2026_07_06_apex_skill_boundary_review
    disposition: deferred
    reason: >
      The package is not complete until the example, manifest, and SKILL.md are
      present and the completion gate is true.
    needed_before_acceptance:
      - examples/apex-minimal-status-merge-example.md created
      - package-manifest.md created
      - SKILL.md created with valid frontmatter
      - package completion gate passes
    evidence_refs:
      - status_merge_packet_2026_07_06_apex_minimal_example
    suggested_next_review: next_status_merge
```

### Deferred Candidate Card

#### Deferred Candidate: `deferred_delta_mark_status_merge_complete`

- **Why deferred:** Completion would be premature.
- **Needed before acceptance:** example, manifest, SKILL.md, and completion gate.
- **Evidence:** this example packet.
- **Suggested next review:** next status merge.

---

## 7. Proposed Project KB Update

This is only a proposal. It must not be written directly by StatusMerge.

```yaml
proposed_project_kb_update:
  write_boundary_owner: project-kb-manager
  write_status: proposal_only
  operator_confirmation_required: true
  proposed_updates:
    - update_id: proposed_kb_update_status_merge_package_started
      target_record_ref: project_kb_record_apex_status_merge_skill_package
      update_kind: append_progress_log
      proposed_change_summary: >
        Append progress log entry noting that status-merge interface package
        contracts and template are drafted, with completion still pending.
      accepted_delta_refs:
        - accepted_delta_status_merge_contracts_started
      conflict_refs:
        - conflict_usage_summary_contract_missing
      evidence_refs:
        - commit:3eaa1da9d6c49a8b6dc966fa43899f1d9f70c5c4
        - commit:c1f8edbea08ae0cd2e345f36751e2d3b9550a969
        - commit:e3bf1e892e4b211cbb8fad022a83c6a83386c67c
      safe_to_apply_without_operator: false
```

---

## 8. Updated All-Project Status Packet View

This is a view only. It is not a replacement for `current_project_status_overview`.

```yaml
updated_all_project_status_packet:
  view_status: proposal_view
  owner_boundary_note: >
    This view summarizes a proposed merge result. It does not replace
    ProjectStatus output and does not mutate the project KB.
  project_focus_summary: >
    Continue building the minimal `status-merge` interface package by adding the
    package manifest and final SKILL.md after this example file.
  changed_refs:
    - project_kb_record_apex_status_merge_skill_package
  unchanged_refs:
    - current_project_status_overview_apex_2026_07_06
  blocked_refs:
    - usage_summary_contract_missing
  confidence: high
```

---

## 9. Next PreCapNextDay Input Context

This is a compact seed for PreCapNextDay. It is not a PreCapNextDay plan and does not trigger PreCapNextDay.

```yaml
next_PreCapNextDay_input_context:
  context_id: next_PreCapNextDay_input_context_2026_07_06_status_merge_package
  created_or_updated_at: 2026-07-06
  source_status_merge_packet_ref: status_merge_packet_2026_07_06_apex_minimal_example
  updated_project_focus:
    focus_status: partial
    focus_summary: >
      Finish the remaining `status-merge` package files while preserving the
      project-kb-manager write boundary and keeping conflicts visible.
    project_refs:
      - apex_status_merge_skill_package
    change_basis: accepted_delta_candidates
  active_next_actions:
    - action_id: action_create_package_manifest
      action_summary: Create package-manifest.md for the status-merge package.
      source_refs:
        - status_merge_packet_2026_07_06_apex_minimal_example
      suggested_owner: status-merge
      planning_relevance: candidate_for_next_flow
      readiness: ready
    - action_id: action_create_skill_md
      action_summary: Create SKILL.md with valid Claude skill frontmatter and procedure.
      source_refs:
        - status_merge_packet_2026_07_06_apex_minimal_example
      suggested_owner: status-merge
      planning_relevance: candidate_for_next_flow
      readiness: ready
  blockers:
    - blocker_id: blocker_usage_summary_contract_missing
      blocker_summary: >
        usage-summary-contract.md is missing; usage_summary_ref remains opaque
        and nullable.
      affected_refs:
        - next_PreCapNextDay_input_context.usage_summary_ref
      severity: medium
      proposed_unblock_path: Add usage-summary contract under model-usage-log or keep reference opaque.
  unresolved_operator_decisions:
    - decision_id: decision_usage_summary_reference_handling
      decision_summary: >
        Should `usage_summary_ref` remain an opaque nullable reference until
        model-usage-log defines its usage-summary contract?
      options:
        - Keep opaque nullable reference.
        - Pause usage-related handoff content until owner contract exists.
      needed_before: not_blocking
      evidence_refs:
        - conflict_usage_summary_contract_missing
  usage_summary_ref: usage_summary_2026_07_06_status_merge_example
  evidence_refs:
    - commit:3eaa1da9d6c49a8b6dc966fa43899f1d9f70c5c4
    - commit:c1f8edbea08ae0cd2e345f36751e2d3b9550a969
    - commit:e3bf1e892e4b211cbb8fad022a83c6a83386c67c
    - status_merge_packet_2026_07_06_apex_minimal_example
  confidence: high
  validation_status: valid_with_warnings
```

---

## 10. Final Validation Gate

```yaml
status_merge_packet_completion_gate:
  source_flow_recap_refs_present: true
  source_usage_summary_refs_present_or_gap_recorded: true
  previous_state_refs_present: true
  accepted_delta_candidates_reviewed: true
  rejected_or_deferred_delta_candidates_reviewed: true
  conflict_notes_prominent: true
  proposed_project_kb_update_is_proposal_only: true
  project_kb_manager_boundary_preserved: true
  updated_all_project_status_packet_is_view_only: true
  next_PreCapNextDay_input_context_present: true
  no_direct_project_kb_write: true
  no_automatic_status_overwrite: true
  no_runtime_trigger_created: true
  no_PreCapNextDay_plan_created: true
  validation_status_allowed_value: true
```

### Result Recommendation

- **Recommended packet status:** `valid_with_warnings`
- **Operator action:** accept the safe package-progress proposal only after review; keep usage-summary gap visible.
- **Next handoff action:** use `next_PreCapNextDay_input_context` as a seed only after the operator approves the context boundary.
