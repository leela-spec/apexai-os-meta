# FILE: .claude/skills/PrecapNextDay/examples/apex-only-template-example/flows/F3-flow-packet.md

# Flow Packet — F3 — APEX output templates/examples

```yaml
flow_packet_status:
  packet_id: flow_packet_2026_06_18_F3
  artifact_name: flow_packet
  execution_day: "2026-06-18"
  flow_id: F3
  project: Apex
  APEX_operator_label: APEX_output_templates_examples
  generation_mode: bootstrap_mode
  review_status: operator_review_recommended
  flow_status: planned
  validation_status: operator_review_recommended
```

## Flow Identity

| Field | Value | Notes |
|---|---|---|
| Flow ID | F3 | Contract flow slot retained. |
| Project | Apex | APEX-only example. |
| Contract-safe flow role | orchestration_system_buildout | Existing allowed contract role fits APEX buildout. |
| Operator label | APEX_output_templates_examples | Presentation-only. |

## Context Summary

```yaml
flow_context_summary:
  primary_goal: Create the blank template set and APEX-only example artifacts.
  source_context_used:
    - operator-output-format-design
    - target template file list
    - PreCap contracts
  missing_context:
    - operator critique of first draft
  assumptions:
    - Template depth is macro/meso for review.
  confidence: medium
```

## Sprint Plan

| Sprint | Focus | Expected output | Prompt pack ref | Review flag |
|---|---|---|---|---|
| S1 | Create main next-day-plan template. | Dashboard template. | `../prompts/F3-flow-prompt-pack.md#S1` | readability |
| S2 | Create flow packet and prompt pack templates. | Per-flow templates. | `../prompts/F3-flow-prompt-pack.md#S2` | prompt placeholder depth |
| S3 | Prepare capture/example notes. | Example fixture links. | `../prompts/F3-flow-prompt-pack.md#S3` | completeness |

## Linked Outputs

| Output | Ref | Status |
|---|---|---|
| prompt pack | `../prompts/F3-flow-prompt-pack.md` | review_ready_degraded |
| raw flow dump | `../capture/raw-flow-dump-template.md#F3` | prepared_not_filled |
| FlowRecap handoff | `../handoff/FlowRecap-handoff.md#F3` | prepared_not_run |

## Operator Review Flags

| Flag ID | Severity | Flag | Action |
|---|---|---|---|
| F3-ORF-001 | medium | Example package is critique-ready. | Review all template files and request edits. |

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
