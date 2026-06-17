# FILE: .claude/skills/PrecapNextDay/examples/apex-only-template-example/flows/F2-flow-packet.md

# Flow Packet — F2 — APEX skill database contracts

```yaml
flow_packet_status:
  packet_id: flow_packet_2026_06_18_F2
  artifact_name: flow_packet
  execution_day: "2026-06-18"
  flow_id: F2
  project: Apex
  APEX_operator_label: APEX_skill_database_contracts
  generation_mode: bootstrap_mode
  review_status: operator_review_recommended
  flow_status: planned
  validation_status: operator_review_recommended
```

## Flow Identity

| Field | Value | Notes |
|---|---|---|
| Flow ID | F2 | Contract flow slot retained. |
| Project | Apex | APEX-only example. |
| Contract-safe flow role | operator_defined | Presentation override; schema authority unchanged. |
| Operator label | APEX_skill_database_contracts | Presentation-only. |
| Override reason | All active example flows are APEX buildout slices. | Prevents multi-project example drift. |

## Context Summary

```yaml
flow_context_summary:
  primary_goal: Map contract authority versus template authority for the PreCap template layer.
  source_context_used:
    - daily-plan-output-contract
    - flow-packet-contract
    - flow-prompt-pack-contract
    - validation-checklist
  missing_context:
    - none_blocking
  assumptions:
    - Templates surface fields but do not define schemas.
  confidence: medium
```

## Sprint Plan

| Sprint | Focus | Expected output | Prompt pack ref | Review flag |
|---|---|---|---|---|
| S1 | Map contract authority. | Contract-to-template surface map. | `../prompts/F2-flow-prompt-pack.md#S1` | schema drift risk |
| S2 | Identify presentation-only labels. | Boundary notes for APEX labels. | `../prompts/F2-flow-prompt-pack.md#S2` | field placement |
| S3 | Prepare capture notes. | Contract boundary handoff notes. | `../prompts/F2-flow-prompt-pack.md#S3` | none |

## Linked Outputs

| Output | Ref | Status |
|---|---|---|
| prompt pack | `../prompts/F2-flow-prompt-pack.md` | review_ready_degraded |
| raw flow dump | `../capture/raw-flow-dump-template.md#F2` | prepared_not_filled |
| FlowRecap handoff | `../handoff/FlowRecap-handoff.md#F2` | prepared_not_run |

## Operator Review Flags

| Flag ID | Severity | Flag | Action |
|---|---|---|---|
| F2-ORF-001 | medium | Contract fields must not be duplicated as template schemas. | Review templates for schema drift. |

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
