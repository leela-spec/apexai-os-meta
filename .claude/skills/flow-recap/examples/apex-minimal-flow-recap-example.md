# APEX Minimal FlowRecap Example

> Synthetic example for manual validation of the `flow-recap` package.
>
> This example uses one APEX-only flow. It consumes a synthetic normalized raw flow dump, produces one candidate project status delta, produces one model usage delta candidate, and includes operator review flags. It does not produce an updated all-project status packet and does not write project KB state.

---

## 0. Example Scope

```yaml
example_scope:
  project: APEX
  example_type: minimal_single_flow
  source_material: synthetic
  active_flow_count: 1
  flow_id: F3
  flow_label: APEX flow-recap minimal interface package
  out_of_scope:
    - updated_all_project_status_packet
    - project_kb_write
    - accepted_project_status_update
    - next_PreCapNextDay_input_context
    - runtime_execution
    - scheduler
    - calendar_write
```

---

## 1. Synthetic Source Flow Packet Ref

```yaml
source_flow_packet_ref:
  packet_id: flow_packet_2026_07_06_F3
  artifact_name: flow_packet
  execution_day: 2026-07-06
  flow_id: F3
  project: APEX
  packet_path_or_label: synthetic://precap-next-day/flow_packet_2026_07_06_F3
  source_status: synthetic_example
  planned_output: flow-recap minimal interface package first contract
```

---

## 2. Synthetic Normalized Raw Flow Dump

```yaml
normalized_raw_flow_dump_ref:
  dump_id: raw_flow_dump_2026_07_06_F3_flow_recap_contract
  artifact_name: normalized_raw_flow_dump
  execution_day: 2026-07-06
  flow_id: F3
  packet_path_or_label: synthetic://raw-flow-dump/raw_flow_dump_2026_07_06_F3_flow_recap_contract
  source_status: synthetic_example
```

**Synthetic normalized raw dump summary:**

```yaml
synthetic_normalized_raw_flow_dump:
  completion_state: completed
  evidence_sources:
    - ref_type: artifact_path
      ref_label: .claude/skills/flow-recap/references/flow-recap-packet-contract.md
      evidence_role: supports_delta
    - ref_type: operator_note
      ref_label: "Create one minimal FlowRecap interface package file at a time."
      evidence_role: supports_delta
  operator_summary:
    normalized_summary: >
      The first FlowRecap reference contract was created for APEX. It defines
      flow_recap_packet ownership, candidate status delta boundaries, model
      usage candidate boundaries, and no-runtime rules.
    uncertainty_notes:
      - skipped_flow_marker_ref is supported as an optional reference input through raw-flow-dump-normalize.
  produced_outputs:
    - output_label: flow-recap-packet-contract.md
      change_type: created
      evidence_ref: .claude/skills/flow-recap/references/flow-recap-packet-contract.md
  decisions_made:
    - decision_summary: Keep FlowRecap project status changes candidate-only.
      status: made
      evidence_ref: .claude/skills/flow-recap/references/flow-recap-packet-contract.md
  blockers_or_failures:
    - blocker_summary: No skipped-flow marker blocker remains; skipped_flow_marker_ref stays optional for skipped or blocked flows.
      status: resolved
  open_questions:
    - Should future examples include a skipped_flow_marker_ref case in addition to completed-flow cases?
  model_usage_notes:
    - surface: ChatGPT
      model_or_mode: unspecified
      usage_note: Operator requested GitHub repo write through connector.
  normalization_confidence:
    confidence_level: high
    confidence_reasons:
      - created artifact path is explicit
      - operator scope was explicit
      - mutation boundaries were explicit
```

---

## 3. Flow Recap Packet Output

```yaml
flow_recap_packet:
  recap_id: flow_recap_2026_07_06_F3_minimal_interface
  artifact_name: flow_recap_packet
  execution_day: 2026-07-06
  flow_id: F3
  source_flow_packet_ref: flow_packet_2026_07_06_F3
  normalized_raw_flow_dump_ref: raw_flow_dump_2026_07_06_F3_flow_recap_contract
  recap_status: ready_for_operator_review
  validation_status: valid_with_warnings
```

## 4. What Happened

**Flow result:** completed

**Compact recap:**  
A minimal FlowRecap packet contract was created for the APEX orchestration system. The file defines how FlowRecap converts one flow packet plus a normalized raw flow dump into a compact recap, a candidate project status delta, a model usage delta candidate, a next-step proposal, unresolved questions, and operator review flags. The contract explicitly avoids status merge, project KB mutation, final usage logging, calendar writes, scheduling, and runtime behavior.

**Work completed:**

- Created `flow-recap-packet-contract.md` under the new `flow-recap` package.
- Recorded source inspection and one missing source gap.
- Defined candidate-only and no-runtime validation rules.

**Not completed / out of scope:**

- Did not create an accepted project status update.
- Did not write project KB state.
- Did not produce `updated_all_project_status_packet`.
- Did not create a next-day plan or calendar event.

---

## 5. Evidence Summary

```yaml
evidence_summary:
  evidence_status: partial
  confidence: high
```

**Evidence used:**

- `.claude/skills/flow-recap/references/flow-recap-packet-contract.md` — supports artifact creation and boundary definitions.
- `.claude/Claude.md` — supports that FlowRecap is a missing skill intended to output `flow_recap_packet` behind operator gate G4.
- `apex-meta/kb/claude-code-orchestration-design/wiki/concepts/flow-recap-packet.md` — supports the concept that FlowRecap compresses flow evidence into recap summary and candidate state delta.

**Evidence gaps or conflicts:**

- `.claude/skills/raw-flow-dump-normalize/references/skipped-flow-marker-contract.md` is available as the optional skipped_flow_marker_ref authority.
- This example is synthetic and should not be treated as proof of actual operator project work.

---

## 6. Outputs Created or Changed

- **`.claude/skills/flow-recap/references/flow-recap-packet-contract.md`** — created  
  Evidence: GitHub commit for the created file  
  Note: First file in the FlowRecap minimal interface package.

---

## 7. Decisions Made

- **Decision:** FlowRecap owns `flow_recap_packet` and `candidate_project_status_delta`, but candidate deltas remain unaccepted until a later operator-gated merge or project KB acceptance path.  
  Status: made  
  Evidence: `flow-recap-packet-contract.md`

- **Decision:** Model usage output from FlowRecap is only `model_usage_delta_candidate`, not a final usage log.  
  Status: made  
  Evidence: `flow-recap-packet-contract.md`

---

## 8. Blockers, Failures, and Open Questions

**Blockers / failures:**

- No skipped-flow marker blocker remains. `skipped_flow_marker_ref` remains optional because completed flows do not require it.

**Unresolved questions:**

- Should a later synthetic example demonstrate a skipped flow with `skipped_flow_marker_ref` populated?
- Should `model-usage-log` define the final usage delta schema before FlowRecap examples are expanded?

---

## 9. Candidate Project Status Delta

> **Candidate-only warning:** This is not accepted project state. It must not overwrite `ProjectStatus`, mutate the project KB, create an updated all-project status packet, or become next PreCapNextDay context until accepted by the operator-gated status merge or project KB update path.

```yaml
candidate_project_status_delta:
  delta_id: candidate_project_status_delta_2026_07_06_F3_flow_recap_contract
  target_project: APEX
  target_scope: flow-recap skill package
  delta_type: artifact_created
  confidence: high
  requires_operator_validation: true
  suggested_acceptance_route: status_merge
```

**Proposed change:**  
Record that the FlowRecap minimal interface package now has its first reference contract created and ready for operator review.

**Evidence:**

- `.claude/skills/flow-recap/references/flow-recap-packet-contract.md`
- GitHub commit creating the file

**Validation reason:**  
The artifact exists, but whether this becomes durable APEX project status must be accepted later by the operator-gated status merge or project KB path.

---

## 10. Model Usage Delta Candidate

> **Candidate-only warning:** This is not the final usage log. It is a candidate capture for `model-usage-log` or the usage owner to validate later.

```yaml
model_usage_delta_candidate:
  candidate_id: model_usage_delta_candidate_2026_07_06_F3_flow_recap_contract
  finalization_owner: model-usage-log
  confidence: low
```

**Observed usage notes:**

- ChatGPT used GitHub connector actions to inspect source files and create a repository file.
- Exact model, token count, and provider quota impact were not captured.

**Unknown or not captured:**

- Exact model usage amount
- Final usage category
- Quota/budget impact

---

## 11. Next-Step Proposal

> This is a next-step proposal, not a next-day plan.

```yaml
next_step_proposal:
  proposed_owner: operator
  requires_operator_validation: true
```

**Recommended next step:**  
Review and accept creation of `project-status-delta-contract.md` as the next FlowRecap package file, keeping it candidate-only and non-mutating.

**Why:**  
The packet contract references `candidate_project_status_delta`, so a dedicated minimal delta contract is the next interface needed before templates and examples can be validated end-to-end.

**Do not do yet:**

- Do not treat the candidate delta as accepted project status.
- Do not create `updated_all_project_status_packet`.
- Do not write project KB records from this example.

---

## 12. Operator Review Flags

- Candidate project status delta requires operator validation before any durable state update.
- Model usage delta candidate requires validation by the future `model-usage-log` owner.
- Example uses synthetic evidence and must not be treated as actual project execution history.
- `skipped_flow_marker_ref` support exists but remains optional for this completed-flow synthetic example.

---

## 13. Negative Output Check

```yaml
negative_output_check:
  updated_all_project_status_packet_created: false
  project_kb_write_created: false
  accepted_project_status_update_created: false
  next_PreCapNextDay_input_context_created: false
  calendar_event_created: false
  runtime_or_scheduler_created: false
```

---

## 14. Completion Gate

```yaml
completion_gate:
  apex_only_example: true
  one_flow_only: true
  synthetic_normalized_raw_flow_dump_consumed: true
  one_candidate_project_status_delta_produced: true
  one_model_usage_delta_candidate_produced: true
  operator_review_flag_present: true
  updated_all_project_status_packet_not_produced: true
  project_kb_write_not_created: true
  candidate_delta_not_treated_as_accepted_state: true
  model_usage_candidate_not_treated_as_final_usage_log: true
```
