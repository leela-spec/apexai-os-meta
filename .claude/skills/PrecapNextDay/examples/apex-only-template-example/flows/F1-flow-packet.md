# FILE: .claude/skills/PrecapNextDay/examples/apex-only-template-example/flows/F1-flow-packet.md

# Flow Packet — F1 — APEX repo foundation

```yaml
flow_packet_status:
  packet_id: flow_packet_2026_06_18_F1
  artifact_name: flow_packet
  execution_day: "2026-06-18"
  flow_id: F1
  project: Apex
  APEX_operator_label: APEX_repo_foundation
  generation_mode: bootstrap_mode
  review_status: operator_review_recommended
  flow_status: planned
  validation_status: operator_review_recommended
```

## Flow Identity

| Field | Value | Notes |
|---|---|---|
| Flow ID | F1 | Contract flow slot retained. |
| Project | Apex | APEX-only example. |
| Contract-safe flow role | operator_defined | Presentation override; do not change schema authority. |
| Operator label | APEX_repo_foundation | Presentation-only. |
| Override reason | Template buildout uses all F1-F4 slots for APEX slices. | Prevents old non-APEX example leakage. |

## Context Summary

```yaml
flow_context_summary:
  primary_goal: Resolve repo package path and target file placement for the PreCap template layer.
  source_context_used:
    - Phase A repo inspection
    - operator handover
  missing_context:
    - final path normalization decision
  assumptions:
    - Preserve current `.claude/skills/PrecapNextDay/` path for this pass.
  confidence: medium
```

## Sprint Plan

| Sprint | Focus | Expected output | Prompt pack ref | Review flag |
|---|---|---|---|---|
| S1 | Confirm actual package paths. | Repo state summary. | `../prompts/F1-flow-prompt-pack.md#S1` | path mismatch |
| S2 | Define template integration boundary. | Path strategy note. | `../prompts/F1-flow-prompt-pack.md#S2` | preserve vs normalize |
| S3 | Prepare capture notes. | Capture/handoff refs. | `../prompts/F1-flow-prompt-pack.md#S3` | none |

## Linked Outputs

| Output | Ref | Status |
|---|---|---|
| prompt pack | `../prompts/F1-flow-prompt-pack.md` | review_ready_degraded |
| raw flow dump | `../capture/raw-flow-dump-template.md#F1` | prepared_not_filled |
| FlowRecap handoff | `../handoff/FlowRecap-handoff.md#F1` | prepared_not_run |

## Operator Review Flags

| Flag ID | Severity | Flag | Action |
|---|---|---|---|
| F1-ORF-001 | high | Current repo path and manifest path differ. | Decide path normalization in a later cleanup pass. |

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
