# FILE: .claude/skills/PrecapNextDay/examples/apex-only-template-example/flows/F4-flow-packet.md

# Flow Packet — F4 — APEX validation/handover

```yaml
flow_packet_status:
  packet_id: flow_packet_2026_06_18_F4
  artifact_name: flow_packet
  execution_day: "2026-06-18"
  flow_id: F4
  project: Apex
  APEX_operator_label: APEX_validation_handover
  generation_mode: bootstrap_mode
  review_status: operator_review_recommended
  flow_status: planned
  validation_status: operator_review_recommended
```

## Flow Identity

| Field | Value | Notes |
|---|---|---|
| Flow ID | F4 | Contract flow slot retained. |
| Project | Apex | APEX-only example. |
| Contract-safe flow role | operator_defined | Presentation override; schema authority unchanged. |
| Operator label | APEX_validation_handover | Presentation-only. |

## Context Summary

```yaml
flow_context_summary:
  primary_goal: Validate the template layer and prepare a review handoff.
  source_context_used:
    - validation-checklist
    - operator-output-format-design
    - generated template/example files
  missing_context:
    - operator review outcome
  assumptions:
    - Final approval happens after critique.
  confidence: medium
```

## Sprint Plan

| Sprint | Focus | Expected output | Prompt pack ref | Review flag |
|---|---|---|---|---|
| S1 | Audit templates against contracts. | Template audit notes. | `../prompts/F4-flow-prompt-pack.md#S1` | contract drift |
| S2 | Audit examples for APEX-only scope. | Boundary audit notes. | `../prompts/F4-flow-prompt-pack.md#S2` | non-APEX leakage |
| S3 | Prepare handoff and next update queue. | Handoff summary. | `../prompts/F4-flow-prompt-pack.md#S3` | pending critique |

## Linked Outputs

| Output | Ref | Status |
|---|---|---|
| prompt pack | `../prompts/F4-flow-prompt-pack.md` | review_ready_degraded |
| final audit | `../handoff/template-layer-final-audit-summary.md` | draft |
| FlowRecap handoff | `../handoff/FlowRecap-handoff.md#F4` | prepared_not_run |

## Operator Review Flags

| Flag ID | Severity | Flag | Action |
|---|---|---|---|
| F4-ORF-001 | medium | Validation is self-audit only until operator critique. | Review files and supply corrections. |

```yaml
flow_packet_completion_gate:
  flow_identity_present: true
  APEX_operator_label_is_presentation_only: true
  sprint_plan_present_or_omission_reason_present: true
  prompt_pack_ref_present_or_degraded_flag_present: true
  usage_tracking_refs_present_or_degraded_flag_present: true
  raw_flow_dump_template_ref_present: true
  FlowRecap_handoff_prepared_without_running_FlowRecap: true
  no_project_work_executed: true
```
