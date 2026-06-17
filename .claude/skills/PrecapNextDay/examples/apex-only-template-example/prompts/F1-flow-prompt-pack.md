# FILE: .claude/skills/PrecapNextDay/examples/apex-only-template-example/prompts/F1-flow-prompt-pack.md

# Flow Prompt Pack — F1 — APEX repo foundation

```yaml
flow_prompt_pack_status:
  pack_id: flow_prompt_pack_2026_06_18_F1
  artifact_name: flow_prompt_pack
  execution_day: "2026-06-18"
  flow_id: F1
  project: Apex
  APEX_operator_label: APEX_repo_foundation
  generation_mode: degraded_generic_prompt_mode
  pack_status: operator_review_recommended
  prompt_execution_status: not_executed
  validation_status: operator_review_recommended
```

## Source Flow Packet

```yaml
source_flow_packet_ref:
  flow_packet_id: flow_packet_2026_06_18_F1
  flow_packet_path_or_slot: ../flows/F1-flow-packet.md
  daily_plan_ref: ../next-day-plan.md
  flow_id: F1
  project: Apex
```

## Sprint Prompt Sequences

| Sprint | Sprint goal | Prompt packet ref/placeholders | Provider/surface hint | Capture hint |
|---|---|---|---|---|
| S1 | Inspect actual package paths. | placeholder_prompt_packet_F1_S1_repo_scan | provider_unspecified | Capture found/missing paths. |
| S2 | Decide preserve-vs-normalize boundary. | placeholder_prompt_packet_F1_S2_path_strategy | provider_unspecified | Capture decision and risks. |
| S3 | Prepare capture notes. | placeholder_prompt_packet_F1_S3_capture_notes | provider_unspecified | Capture handoff notes. |

## Routing / Usage / Workflow

```yaml
routing_usage_summary:
  routing_recommendation_ref: missing
  planned_usage_budget_ref: missing
  usage_tracking_summary_ref: ../usage/usage-tracking-summary.md
  quota_or_price_claims_made: false
workflow_alignment_summary:
  workflow_process_validation_ref: ../handoff/template-layer-final-audit-summary.md
  dependency_status: low_confidence_inferred
FlowRecap_preparation:
  status: prepared_not_run
  handoff_ref: ../handoff/FlowRecap-handoff.md#F1
  FlowRecap_output_created: false
```

## Review Flags

| Flag ID | Flag |
|---|---|
| F1-PROMPT-ORF-001 | Prompt packets are placeholders until prompt-engineering dependency is applied. |
