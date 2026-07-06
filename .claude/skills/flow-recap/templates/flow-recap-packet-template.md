# Flow Recap Packet Template

> Use this template after one planned flow has been executed, skipped, partially completed, or blocked, and after a normalized raw flow dump exists.
>
> This template is operator-facing. It is not a schema authority. Full contracts live in `references/flow-recap-packet-contract.md` and `references/project-status-delta-contract.md`.

---

## 1. Recap Header

```yaml
recap_header:
  recap_id: <flow_recap_YYYY_MM_DD_flow_id_slug>
  artifact_name: flow_recap_packet
  execution_day: <YYYY-MM-DD>
  flow_id: <F1|F2|F3|F4|operator_defined>
  recap_status: <ready_for_operator_review|operator_validated|low_confidence|blocked_by_missing_evidence>
  validation_status: <valid|valid_with_warnings|operator_review_recommended|low_confidence|blocked_by_missing_minimum_evidence>
```

**Source flow packet:** `<path-or-id>`  
**Normalized raw flow dump:** `<path-or-id>`  
**Optional prompt pack:** `<path-or-id-or-NA>`

---

## 2. What Happened

**Flow result:** `<completed|partially_completed|skipped|blocked|abandoned|unknown>`

**Compact recap:**  
`<2-5 sentences summarizing what happened, using only supplied evidence.>`

**Work completed:**

- `<completed item 1>`
- `<completed item 2>`
- `<completed item 3>`

**Not completed / out of scope:**

- `<unfinished or intentionally omitted item>`
- `<scope boundary or deferred item>`

---

## 3. Evidence Summary

```yaml
evidence_summary:
  evidence_status: <sufficient|partial|conflicting|missing_minimum_evidence>
  confidence: <high|medium|low|unknown>
```

**Evidence used:**

- `<evidence ref 1 — what it supports>`
- `<evidence ref 2 — what it supports>`
- `<evidence ref 3 — what it supports>`

**Evidence gaps or conflicts:**

- `<gap/conflict 1 or NA>`
- `<gap/conflict 2 or NA>`

---

## 4. Outputs Created or Changed

- **`<artifact or output label>`** — `<created|updated|reviewed|proposed|no_output|unknown>`  
  Evidence: `<evidence ref>`  
  Note: `<short note>`

- **`<artifact or output label>`** — `<created|updated|reviewed|proposed|no_output|unknown>`  
  Evidence: `<evidence ref>`  
  Note: `<short note>`

---

## 5. Decisions Made

- **Decision:** `<decision summary or NA>`  
  Status: `<made|proposed|deferred|needs_operator_validation>`  
  Evidence: `<evidence ref>`

- **Decision:** `<decision summary or NA>`  
  Status: `<made|proposed|deferred|needs_operator_validation>`  
  Evidence: `<evidence ref>`

---

## 6. Blockers, Failures, and Open Questions

**Blockers / failures:**

- `<blocker or failure summary>`
- `<blocker or failure summary>`

**Unresolved questions:**

- `<question that needs operator or later-system validation>`
- `<question that should be carried forward>`

---

## 7. Candidate Project Status Delta

> **Candidate-only warning:** The following section is not accepted project state. It must not overwrite `ProjectStatus`, mutate the project KB, create an updated all-project status packet, or become next PreCapNextDay context until accepted by the operator-gated status merge or project KB update path.

```yaml
candidate_project_status_delta:
  delta_id: <candidate_project_status_delta_YYYY_MM_DD_flow_id_slug>
  target_project: <project-or-unknown>
  target_scope: <task|workstream|artifact|decision|blocker|NA>
  delta_type: <task_progress|new_task_candidate|blocker_added|blocker_removed|decision_added|artifact_created|artifact_updated|priority_signal_changed|no_state_change>
  confidence: <high|medium|low|unknown>
  requires_operator_validation: true
  suggested_acceptance_route: <status_merge|project_kb_manager_update_mode|ProjectStatus_review|no_action|operator_decision_needed|unknown>
```

**Proposed change:**  
`<one compact sentence describing what should change if accepted.>`

**Evidence:**

- `<evidence ref supporting this candidate delta>`
- `<evidence ref supporting this candidate delta>`

**Validation reason:**  
`<why this needs validation, or why confidence is low/high.>`

---

## 8. Model Usage Delta Candidate

> **Candidate-only warning:** This is not the final usage log. It is a candidate capture for `model-usage-log` or the usage owner to validate later.

```yaml
model_usage_delta_candidate:
  candidate_id: <model_usage_delta_candidate_YYYY_MM_DD_flow_id_slug>
  finalization_owner: model-usage-log
  confidence: <high|medium|low|unknown>
```

**Observed usage notes:**

- `<surface/model/prompt/usage note if known>`
- `<quota/cost/scarcity note if explicitly evidenced>`

**Unknown or not captured:**

- `<missing usage detail>`
- `<missing usage detail>`

---

## 9. Next-Step Proposal

> This is a next-step proposal, not a next-day plan.

```yaml
next_step_proposal:
  proposed_owner: <operator|PreCapNextDay|project-kb-manager|status-merge|model-usage-log|unknown>
  requires_operator_validation: true
```

**Recommended next step:**  
`<one concrete next action proposed from this recap.>`

**Why:**  
`<short evidence-based rationale.>`

**Do not do yet:**

- `<thing that should not be treated as accepted or scheduled>`
- `<thing that requires a later gate>`

---

## 10. Operator Review Flags

- `<flag 1: candidate status delta requires validation>`
- `<flag 2: usage candidate requires validation>`
- `<flag 3: evidence/confidence issue>`

---

## 11. Recap Completion Gate

```yaml
completion_gate:
  source_flow_packet_ref_present: true
  normalized_raw_flow_dump_ref_present: true
  evidence_summary_present: true
  work_completed_summary_present: true
  outputs_created_or_changed_listed: true
  candidate_project_status_delta_marked_candidate_only: true
  model_usage_delta_candidate_marked_not_final: true
  next_step_proposal_is_not_next_day_plan: true
  operator_review_flags_present: true
  no_project_kb_write_or_status_merge_claimed: true
  no_runtime_scheduler_or_calendar_write_created: true
```
