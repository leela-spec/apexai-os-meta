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
    conflict_type: <state_owner_unclear | competing_status_values | stale_vs_newer_evidence | duplicate_recap_candidate | project_identity_ambiguous | usage_summary_incomplete | next_action_conflict>
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
- **Type:** <conflict_type>
- **What conflicts:** <plain-language summary>
- **Evidence:** <source refs>
- **Affected state:** <state refs>
- **Operator decision needed:** <decision>
- **Proposed resolution:** <proposal or none>
- **Blocks:** <project KB write / next PreCap context / neither>

---

## 4. Accepted Delta Candidates

Accepted means accepted into this merge proposal only. It does not mean durable KB mutation unless the operator confirms and the write routes through `project-kb-manager`.

```yaml
accepted_delta_candidates:
  - candidate_id: delta_<short_slug>
    source_ref: <flow_recap_packet_ref_or_other_source>
    delta_summary: <compact summary>
    proposed_destination: <project_kb_manager_update_proposal | ProjectStatus_view_update_proposal | next_PreCapNextDay_context_seed | consumed_recap_register_view>
    acceptance_basis: <evidence summary or operator note>
    operator_confirmation_status: <confirmed | not_confirmed | not_required_for_low_risk_view_only>
    project_kb_manager_write_boundary: proposal_only_until_confirmed
```

### Accepted Delta Cards

#### Accepted Candidate: `<candidate_id>`

- **Source:** <source ref>
- **Delta:** <what changed>
- **Why accepted into proposal:** <basis>
- **Proposed destination:** <destination>
- **Write status:** Proposal only unless confirmed through `project-kb-manager`.
- **Next planning effect:** <effect on next_PreCapNextDay_input_context>

---

## 5. Rejected Delta Candidates

Use this section for candidates that should not move forward because they are duplicate, unsupported, contradicted, out of scope, or owned by another package.

```yaml
rejected_delta_candidates:
  - candidate_id: delta_<short_slug>
    source_ref: <source ref>
    delta_summary: <compact summary>
    disposition: rejected
    reason: <why rejected>
    evidence_refs:
      - <ref_id>
```

### Rejected Delta Cards

#### Rejected Candidate: `<candidate_id>`

- **Source:** <source ref>
- **Delta:** <what was proposed>
- **Reason rejected:** <reason>
- **Evidence:** <refs>
- **State impact:** No durable write. No next PreCap seed unless separately accepted elsewhere.

---

## 6. Deferred Delta Candidates

Use this section for candidates that may become valid later but currently need more evidence, owner review, conflict resolution, or operator decision.

```yaml
deferred_delta_candidates:
  - candidate_id: delta_<short_slug>
    source_ref: <source ref>
    delta_summary: <compact summary>
    disposition: <deferred | duplicate | superseded | insufficient_evidence>
    reason: <why deferred>
    unblock_condition: <what would make this usable>
    revisit_context: <next session / next PreCap / operator review / never>
```

### Deferred Delta Cards

#### Deferred Candidate: `<candidate_id>`

- **Source:** <source ref>
- **Delta:** <what was proposed>
- **Reason deferred:** <reason>
- **Unblock condition:** <needed evidence or decision>
- **Revisit context:** <where it should be reconsidered>

---

## 7. Combined Rejected or Deferred Register

The contract-level `status_merge_packet` field is `rejected_or_deferred_delta_candidates`. This compact register may combine the detailed rejected and deferred cards above.

```yaml
rejected_or_deferred_delta_candidates:
  - candidate_id: <delta_id>
    source_ref: <source ref>
    delta_summary: <compact summary>
    disposition: <rejected | deferred | duplicate | superseded | insufficient_evidence>
    reason: <compact reason>
```

---

## 8. Proposed Project KB Update

This section is a proposal for `project-kb-manager`, not a direct write. Leave blocked or conflicting changes visible.

```yaml
proposed_project_kb_update:
  proposal_id: project_kb_update_proposal_<short_slug>
  durable_write_owner: project-kb-manager
  target_project_refs:
    - <project_ref>
  proposed_changes_summary:
    - <compact change proposal>
  blocked_changes:
    - blocked_change_id: <blocked_change_id>
      reason: <conflict | missing owner | missing evidence | operator decision required>
      source_refs:
        - <ref_id>
  operator_gate_status: <ready_for_operator_review | confirmed_for_project_kb_manager | blocked_by_conflict | blocked_by_missing_state_owner>
```

### Project KB Update Review Card

- **Durable write owner:** `project-kb-manager`
- **Proposed records affected:** <project refs>
- **Changes ready for review:** <short list>
- **Changes blocked:** <short list>
- **Operator gate:** <status>
- **Explicit warning:** Do not directly edit project KB durable records from this packet.

---

## 9. Updated All-Project Status Packet View

This is a merge view/proposal for operator review. It does not redefine `current_project_status_overview` and does not replace `ProjectStatus`.

```yaml
updated_all_project_status_packet:
  view_id: updated_all_project_status_packet_<YYYY_MM_DD>_<short_slug>
  source_status_merge_packet_ref: <merge_packet_id>
  accepted_delta_register_view:
    - <candidate_id>
  consumed_recap_candidate_list:
    - recap_ref: <flow_recap_packet_ref>
      disposition: <accepted | partially_accepted | rejected | deferred | conflict_review_needed>
  project_status_summary:
    - project_ref: <project_ref>
      status_view: <compact current status after proposed merge>
      source_refs:
        - <ref_id>
  unresolved_conflicts:
    - <conflict_id>
```

### Status View Cards

#### Project: `<project_ref>`

- **Status view:** <compact status after proposed merge>
- **Accepted deltas included:** <candidate ids>
- **Conflicts still open:** <conflict ids or none>
- **Durable write status:** Proposal/view only unless accepted through owner boundary.

---

## 10. Consumed Recap Candidate List

This is a view of recap consumption for merge review. If durable consumed-recap registry updates are needed, route them through `project-kb-manager`.

```yaml
consumed_recap_candidate_list:
  - recap_ref: <flow_recap_packet_ref>
    disposition: <accepted | partially_accepted | rejected | deferred | conflict_review_needed>
    accepted_candidate_ids:
      - <candidate_id>
    rejected_or_deferred_candidate_ids:
      - <candidate_id>
    conflict_ids:
      - <conflict_id>
    registry_update_status: <proposal_only | confirmed_for_project_kb_manager | not_required>
```

---

## 11. Next PreCapNextDay Input Context

This is a compact seed for the next PreCapNextDay run, not the next-day plan itself.

```yaml
next_PreCapNextDay_input_context:
  context_id: next_precap_context_<YYYY_MM_DD>_<short_slug>
  created_or_updated_at: <YYYY-MM-DD>
  source_status_merge_packet_ref: <merge_packet_id>
  updated_project_focus:
    - focus_id: focus_<short_slug>
      project_ref: <project_ref>
      focus_summary: <compact focus>
      source_refs:
        - <ref_id>
      status: <proposed_new_focus | continued_focus | reduced_focus | paused_focus | conflict_review_needed>
  active_next_actions:
    - action_id: action_<short_slug>
      project_ref: <project_ref>
      action_summary: <compact next action candidate>
      action_status: <ready_for_precap_consideration | blocked_by_operator_decision | blocked_by_missing_evidence | deferred | conflict_review_needed>
      source_refs:
        - <ref_id>
  blockers:
    - blocker_id: blocker_<short_slug>
      blocker_summary: <compact blocker>
      affected_project_refs:
        - <project_ref>
      source_refs:
        - <ref_id>
      resolution_needed: <operator_decision | project_kb_manager_update | missing_evidence | conflict_resolution | no_action_required>
  unresolved_operator_decisions:
    - decision_id: decision_<short_slug>
      decision_summary: <operator decision needed>
      options:
        - <option>
      source_refs:
        - <ref_id>
      impact_if_unresolved: <blocks_next_precap | limits_next_precap_confidence | blocks_project_kb_write | informational_only>
  usage_summary_ref: <usage_summary_ref_or_null>
  evidence_refs:
    - <ref_id>
  confidence:
    level: <high | medium | low | blocked>
    rationale: <compact rationale>
    limiting_factors:
      - <factor>
  validation_status: <valid | valid_with_warnings | operator_review_recommended | blocked_by_conflict | blocked_by_missing_state_owner>
```

### Next PreCap Context Card

- **Primary focus for next PreCapNextDay:** <focus summary>
- **Ready actions:** <short list>
- **Blocked actions:** <short list>
- **Operator decisions carried forward:** <short list>
- **Usage context:** <usage summary ref or missing>
- **Confidence:** <level and rationale>

---

## 12. Evidence and Traceability

```yaml
evidence_refs:
  - ref_id: <source_ref>
    source_type: <flow_recap_packet | usage_summary | previous_state | operator_note | project_kb_record | ProjectStatus_view | apex_orchestration_state_packet>
    relevance: <why this evidence matters>
    confidence: <high | medium | low | unknown>
```

### Evidence Notes

- **FlowRecap evidence:** <refs and compact summary>
- **Usage evidence:** <refs and compact summary, or missing>
- **Previous state evidence:** <refs and compact summary>
- **Operator notes:** <refs and compact summary, if any>

---

## 13. Validation Checklist

```yaml
validation_checklist:
  required_fields_present: <true | false>
  source_flow_recap_refs_present: <true | false>
  previous_state_refs_present: <true | false>
  conflicts_reviewed_before_accepted_deltas: <true | false>
  accepted_rejected_deferred_conflicting_deltas_separated: <true | false>
  project_kb_manager_boundary_explicit: <true | false>
  all_state_changes_marked_as_proposal_unless_confirmed: <true | false>
  no_direct_project_record_mutation: true
  no_status_overwrite: true
  no_runtime_created: true
  no_scheduler_created: true
  no_agent_created: true
  no_calendar_write_created: true
  next_PreCapNextDay_input_context_included: <true | false>
  validation_status: <valid | valid_with_warnings | operator_review_recommended | blocked_by_conflict | blocked_by_missing_state_owner>
```

### Completion Statement

```text
This status_merge_packet is an operator-facing merge proposal. Durable project KB updates are not performed here and must route through project-kb-manager after operator confirmation. Conflicts and deferred deltas remain visible for review before the next PreCapNextDay run.
```
