# Status Merge Packet Template

Use this template to produce an operator-facing `status_merge_packet` after reviewing validated FlowRecap candidates, usage-summary references, previous state references, and conflict signals.

This template is intentionally card/list based. Do not convert it into a wide table. Do not use it to mutate durable project state directly.

---

## 1. Merge Packet Header

```yaml
status_merge_packet:
  merge_packet_id: status_merge_packet_<YYYY_MM_DD>_<short_slug>
  artifact_name: status_merge_packet
  created_or_updated_at: <YYYY-MM-DD>
  merge_scope: <single_flow | execution_day | multi_day_backlog | conflict_review_only>
  validation_status: <valid | valid_with_warnings | operator_review_recommended | blocked_by_conflict | blocked_by_missing_state_owner>
```

### Source Refs

```yaml
source_flow_recap_refs:
  - ref_id: <flow_recap_packet_ref>
    status: <validated | validated_with_warnings | partial | missing>
    note: <compact note>

source_usage_summary_refs:
  - ref_id: <usage_summary_ref_or_null>
    status: <available | missing | not_applicable | opaque_reference_only>
    note: <compact note>

previous_state_refs:
  - ref_id: <project_status_or_kb_ref>
    owner: <project-kb-manager | ProjectStatus | apex_orchestration_state_packet | other>
    status: <available | stale | missing | conflict>
```

---

## 2. Operator Review First

> **Do not write durable project state from this packet directly.**
>
> Treat every state-changing item below as a proposal unless there is explicit operator confirmation and the durable write is performed through the appropriate owner, especially `project-kb-manager` for project KB records.

```yaml
operator_review_flags:
  requires_operator_review: <true | false>
  project_kb_manager_write_required: <true | false>
  conflicts_present: <true | false>
  blocked_by_missing_state_owner: <true | false>
  auto_write_allowed: false
  auto_trigger_allowed: false
```

### Review Summary Card

- **Merge intent:** <what this merge is trying to consolidate>
- **Recommended operator action:** <accept proposal | review conflicts | defer | block>
- **Primary risk:** <main risk if accepted too early>
- **State owner boundary:** Durable project KB writes must go through `project-kb-manager`.
- **Next planning impact:** <how this affects next_PreCapNextDay_input_context>

---

## 3. Prominent Conflict Notes

Use this section before accepted deltas. If any high-severity conflict exists, set `validation_status: blocked_by_conflict` unless the conflict is explicitly non-blocking.

```yaml
conflict_notes:
  - conflict_id: conflict_<short_slug>
    severity: <high | medium | low | unknown>
    conflict_summary: <what conflicts>
    source_refs:
      - <ref_id>
    affected_state_refs:
      - <state_ref_id>
    required_operator_decision: <decision needed>
    proposed_resolution: <candidate resolution or null>
    blocks_project_kb_write: <true | false>
    blocks_next_PreCapNextDay_context: <true | false>
```

### Conflict Cards

#### Conflict: `<conflict_id>`

- **Severity:** <high | medium | low | unknown>
- **What conflicts:** <plain-language summary>
- **Evidence:** <source refs>
- **Affected state:** <state refs>
- **Operator decision needed:** <decision>
- **Proposed resolution:** <proposal or none>
- **Blocks:** <project KB write / next PreCap context / neither>

---

## 4. Accepted Delta Candidates

Accepted means accepted for merge proposal, not durable write. These entries may become durable only after operator review and owner-safe write handling.

```yaml
accepted_delta_candidates:
  - candidate_id: accepted_delta_<short_slug>
    source_ref: <flow_recap_packet_ref_or_other_evidence_ref>
    delta_type: <project_status | milestone | next_action | blocker | consumed_recap | usage_context | other>
    target_owner: <project-kb-manager | ProjectStatus | model-usage-log | status-merge | other>
    target_ref: <existing_or_new_state_ref>
    proposed_change_summary: <compact summary>
    acceptance_basis: <why this candidate is accepted into the merge proposal>
    evidence_refs:
      - <ref_id>
    confidence: <high | medium | low | unknown>
    durable_write_status: proposal_only
```

### Accepted Candidate Cards

#### Accepted Candidate: `<candidate_id>`

- **Target owner:** <owner>
- **Target ref:** <ref>
- **Change proposed:** <summary>
- **Why accepted into packet:** <basis>
- **Evidence:** <refs>
- **Confidence:** <high | medium | low | unknown>
- **Durable write status:** `proposal_only`

---

## 5. Rejected Delta Candidates

Rejected means not included in the merge proposal. Preserve the rationale so future recap review does not re-open the same candidate without new evidence.

```yaml
rejected_delta_candidates:
  - candidate_id: rejected_delta_<short_slug>
    source_ref: <flow_recap_packet_ref_or_other_evidence_ref>
    rejection_reason: <duplicate | insufficient_evidence | out_of_scope | contradicted_by_state | wrong_owner | other>
    evidence_refs:
      - <ref_id>
    revisit_condition: <what would make it worth reconsidering, or null>
```

### Rejected Candidate Cards

#### Rejected Candidate: `<candidate_id>`

- **Reason:** <reason>
- **Evidence:** <refs>
- **Revisit condition:** <condition or none>

---

## 6. Deferred Delta Candidates

Deferred means potentially useful but not safe or ready to merge now.

```yaml
deferred_delta_candidates:
  - candidate_id: deferred_delta_<short_slug>
    source_ref: <flow_recap_packet_ref_or_other_evidence_ref>
    deferral_reason: <needs_operator_decision | needs_state_owner | needs_evidence | blocked_by_conflict | timing | other>
    needed_before_acceptance:
      - <condition>
    evidence_refs:
      - <ref_id>
    suggested_next_review: <next_status_merge | next_weekly_review | after_operator_decision | other>
```

### Deferred Candidate Cards

#### Deferred Candidate: `<candidate_id>`

- **Why deferred:** <reason>
- **Needed before acceptance:** <conditions>
- **Evidence:** <refs>
- **Suggested next review:** <review point>

---

## 7. Proposed Project KB Update

This section is a proposal for `project-kb-manager`, not a direct write. Do not include fields outside the durable schema owner’s allowed shape.

```yaml
proposed_project_kb_update:
  write_boundary_owner: project-kb-manager
  write_status: proposal_only
  operator_confirmation_required: true
  proposed_updates:
    - update_id: proposed_kb_update_<short_slug>
      target_record_ref: <record_ref_or_new_candidate_ref>
      update_kind: <create | update | append_progress_log | mark_consumed_recap | other>
      proposed_change_summary: <summary>
      accepted_delta_refs:
        - <accepted_delta_id>
      conflict_refs:
        - <conflict_id_or_null>
      evidence_refs:
        - <ref_id>
      safe_to_apply_without_operator: false
```

### Project KB Write Boundary Card

- **Boundary owner:** `project-kb-manager`
- **Packet status:** proposal only
- **Operator confirmation required:** yes
- **Direct write allowed here:** no
- **Unsafe if:** conflicts unresolved, owner missing, evidence missing, schema mismatch, or operator has not approved.

---

## 8. Updated All-Project Status Packet View

This is a merge-result view for review. It must not redefine or replace `current_project_status_overview` unless the owning skill/process explicitly accepts it.

```yaml
updated_all_project_status_packet:
  view_status: <proposal_view | operator_confirmed_view | blocked>
  owner_boundary_note: >
    This is a StatusMerge review view, not a durable ProjectStatus schema
    replacement and not a project KB write.
  project_focus_summary: <compact summary>
  changed_refs:
    - <state_ref_or_candidate_ref>
  unchanged_refs:
    - <state_ref>
  blocked_refs:
    - <state_ref_or_candidate_ref>
  confidence: <high | medium | low | unknown>
```

---

## 9. Next PreCapNextDay Input Context

This section is the compact downstream seed for PreCapNextDay. It is not a daily plan and must not auto-trigger PreCapNextDay.

```yaml
next_PreCapNextDay_input_context:
  context_id: next_PreCapNextDay_input_context_<YYYY_MM_DD>_<short_slug>
  created_or_updated_at: <YYYY-MM-DD>
  source_status_merge_packet_ref: <merge_packet_id>
  updated_project_focus:
    focus_status: <updated_from_accepted_deltas | unchanged | partial | blocked_by_conflict | unknown>
    focus_summary: <compact planning seed summary>
    project_refs:
      - <project_ref>
    change_basis: <accepted_delta_candidates | operator_review | previous_state_only | conflict_review_only | insufficient_evidence>
  active_next_actions:
    - action_id: action_<short_slug>
      action_summary: <candidate next action>
      source_refs:
        - <ref_id>
      suggested_owner: <operator | PreCapNextDay | project-kb-manager | ProjectStatus | status-merge | unknown>
      planning_relevance: <candidate_for_next_flow | supporting_context | followup_after_operator_decision | blocked>
      readiness: <ready | needs_operator_decision | needs_evidence | blocked | deferred>
  blockers:
    - blocker_id: blocker_<short_slug>
      blocker_summary: <blocker summary>
      affected_refs:
        - <ref_id>
      severity: <high | medium | low | unknown>
      proposed_unblock_path: <operator action or evidence needed>
  unresolved_operator_decisions:
    - decision_id: decision_<short_slug>
      decision_summary: <decision needed>
      options:
        - <option>
      needed_before: <next_PreCapNextDay | project_kb_manager_write | ProjectStatus_refresh | future_weekly_plan | not_blocking>
      evidence_refs:
        - <ref_id>
  usage_summary_ref: <usage_summary_ref_or_null>
  evidence_refs:
    - <ref_id>
  confidence: <high | medium | low | unknown>
  validation_status: <valid | valid_with_warnings | operator_review_recommended | blocked_by_conflict | blocked_by_missing_state_owner>
```

---

## 10. Final Validation Gate

```yaml
status_merge_packet_completion_gate:
  source_flow_recap_refs_present: <true | false>
  source_usage_summary_refs_present_or_gap_recorded: <true | false>
  previous_state_refs_present: <true | false>
  accepted_delta_candidates_reviewed: <true | false>
  rejected_delta_candidates_reviewed: <true | false>
  deferred_delta_candidates_reviewed: <true | false>
  conflict_notes_prominent: <true | false>
  proposed_project_kb_update_is_proposal_only: <true | false>
  project_kb_manager_boundary_preserved: <true | false>
  updated_all_project_status_packet_is_view_only: <true | false>
  next_PreCapNextDay_input_context_present: <true | false>
  no_direct_project_kb_write: <true | false>
  no_automatic_status_overwrite: <true | false>
  no_runtime_trigger_created: <true | false>
  validation_status_allowed_value: <true | false>
```

### Result Recommendation

- **Recommended packet status:** <valid | valid_with_warnings | operator_review_recommended | blocked_by_conflict | blocked_by_missing_state_owner>
- **Operator action:** <accept proposal | review conflicts | defer | block | request owner-safe project-kb-manager write>
- **Next handoff action:** <use context as PreCapNextDay seed | hold until conflict resolved | hold until state owner clarified>
