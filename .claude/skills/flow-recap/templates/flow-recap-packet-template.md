# FlowRecap Result Card Template

> Use after one planned flow is completed, partial, blocked, skipped, or abandoned and the available execution evidence has been normalized when needed.
>
> This is the operator-facing projection of a `flow_recap_packet`. It does not replace the contracts in `references/flow-recap-packet-contract.md` and `references/project-status-delta-contract.md`.

---

# Result — `<flow title>`

**Outcome:** `<completed | partially completed | blocked | skipped | abandoned | unknown>`  
**What changed:** `<one sentence describing the evidence-supported result>`  
**Next:** `<one concrete next-step proposal; not a next-day plan>`  
**Review:** `<none | approve candidate status delta | review evidence gap | review usage learning | clarify decision>`

> **State boundary:** Everything below is recap evidence or a candidate proposal. Nothing here is accepted project state, a durable KB update, or a final usage log.

## What happened

`<2–5 evidence-based sentences. State what was completed, what remained incomplete, and why the result matters.>`

**Completed**

- `<completed item>`
- `<completed item>`

**Not completed / out of scope**

- `<unfinished, deferred, or intentionally excluded item>`

## Outputs and decisions

**Outputs created or changed**

- **`<artifact or output>`** — `<created | updated | reviewed | proposed | no_output | unknown>`  
  Evidence: `<source ref>`

**Decisions**

- **`<decision summary>`** — `<made | proposed | deferred | needs_operator_validation>`  
  Evidence: `<source ref>`

## Blockers and open questions

- **Blocker or warning:** `<summary or none>`
- **Open question:** `<question or none>`

## Candidate status change — review required

**Candidate:** `<one compact proposed project-status change, or “no state change proposed”>`  
**Target:** `<project / task / workstream / artifact / decision / blocker>`  
**Confidence:** `<high | medium | low | unknown>`  
**Recommended route:** `<status-merge | project-kb-manager update | ProjectStatus review | no action | operator decision needed>`

**Evidence**

- `<evidence ref supporting the candidate>`

**Operator action**

- [ ] Approve for downstream status review
- [ ] Edit the candidate
- [ ] Reject the candidate
- [ ] Defer pending more evidence

## Usage learning — advisory

**Planned vs actual:** `<match | mismatch | unknown — short explanation>`  
**Observed route:** `<surface/model if evidenced; otherwise unknown>`  
**Learning signal:** `<reuse_route | avoid_route | use_only_for_high_value_tasks | insufficient_data | operator_review_needed>`  
**Confidence:** `<high | medium | low | unknown>`

**Operator action:** `<send to model-usage-log | edit | discard | no action>`

## Evidence and confidence

**Evidence status:** `<sufficient | partial | conflicting | missing_minimum_evidence>`  
**Overall confidence:** `<high | medium | low | unknown>`

**Evidence used**

- `<source ref — what it supports>`

**Gaps or conflicts**

- `<gap, stale source, conflict, or none>`

## Downstream handoff

- **Status candidate →** `<status-merge ref or no_action>`
- **Usage candidate →** `<model-usage-log ref or no_action>`
- **Next planning signal →** `<one sentence for later PreCap use; not a next-day plan>`
- **Supporting detail →** `<flow packet, evidence handoff, prompt, and artifact refs>`

---

## Compact machine handoff

```yaml
flow_recap_handoff:
  recap_id: <flow_recap_YYYY_MM_DD_flow_id_slug>
  artifact_name: flow_recap_packet
  execution_day: <YYYY-MM-DD>
  flow_id: <F1|F2|F3|F4|operator_defined>
  flow_result: <completed|partially_completed|skipped|blocked|abandoned|unknown>
  recap_status: <ready_for_operator_review|operator_validated|low_confidence|blocked_by_missing_evidence>
  validation_status: <valid|valid_with_warnings|operator_review_recommended|low_confidence|blocked_by_missing_minimum_evidence>
  source_flow_packet_ref: <path-or-id>
  normalized_raw_flow_dump_ref: <path-or-id>
  evidence_status: <sufficient|partial|conflicting|missing_minimum_evidence>
  confidence: <high|medium|low|unknown>
  candidate_project_status_delta:
    delta_id: <candidate_project_status_delta_YYYY_MM_DD_flow_id_slug>
    delta_type: <task_progress|new_task_candidate|blocker_added|blocker_removed|decision_added|artifact_created|artifact_updated|priority_signal_changed|no_state_change>
    state: candidate
    requires_operator_validation: true
    suggested_acceptance_route: <status_merge|project_kb_manager_update_mode|ProjectStatus_review|no_action|operator_decision_needed|unknown>
  model_usage_delta_candidate:
    candidate_id: <model_usage_delta_candidate_YYYY_MM_DD_flow_id_slug>
    state: advisory_candidate
    finalization_owner: model-usage-log
    route_signal: <reuse_route|avoid_route|use_only_for_high_value_tasks|insufficient_data|operator_review_needed>
    confidence: <high|medium|low|unknown>
  next_step_proposal:
    proposed_owner: <operator|PreCapNextDay|project-kb-manager|status-merge|model-usage-log|unknown>
    requires_operator_validation: true
  operator_review_flags:
    - <review flag>
```

## Completion check

```yaml
completion_gate:
  result_card_first: true
  what_changed_next_and_review_visible: true
  source_flow_packet_ref_present: true
  normalized_raw_flow_dump_ref_present: true
  evidence_summary_present: true
  candidate_project_status_delta_present_or_no_state_change: true
  candidate_project_status_delta_marked_candidate_only: true
  model_usage_delta_candidate_present_and_not_final: true
  next_step_proposal_present_and_not_a_next_day_plan: true
  operator_review_flags_present: true
  downstream_handoff_visible: true
  no_project_kb_write_or_status_merge_claimed: true
  no_runtime_scheduler_or_calendar_write_created: true
```
