# FILE: .claude/skills/PrecapNextDay/examples/apex-only-template-example/prompts/F4-flow-prompt-pack.md

# Flow Prompt Pack — F4 — APEX validation/handover

```yaml
flow_prompt_pack_status:
  pack_id: flow_prompt_pack_2026_06_18_F4
  artifact_name: flow_prompt_pack
  execution_day: "2026-06-18"
  flow_id: F4
  project: Apex
  APEX_operator_label: APEX_validation_handover
  generation_mode: degraded_generic_prompt_mode
  pack_status: operator_review_recommended
  prompt_execution_status: not_executed
  validation_status: operator_review_recommended
```

## Source Flow Packet

```yaml
source_flow_packet_ref:
  flow_packet_id: flow_packet_2026_06_18_F4
  flow_packet_path_or_slot: ../flows/F4-flow-packet.md
  daily_plan_ref: ../next-day-plan.md
  flow_id: F4
  project: Apex
```

## Sprint Prompt Sequences

| Sprint | Sprint goal | Prompt packet ref/placeholders | Provider/surface hint | Capture hint |
|---|---|---|---|---|
| S1 | Check templates against contracts. | placeholder_prompt_packet_F4_S1_template_check | provider_unspecified | Capture contract checks. |
| S2 | Check examples for APEX-only scope. | placeholder_prompt_packet_F4_S2_scope_check | provider_unspecified | Capture boundary checks. |
| S3 | Prepare review handoff. | placeholder_prompt_packet_F4_S3_handoff | provider_unspecified | Capture critique queue. |

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
  handoff_ref: ../handoff/FlowRecap-handoff.md#F4
  FlowRecap_output_created: false
```

## Review Flags

| Flag ID | Flag |
|---|---|
| F4-PROMPT-ORF-001 | Handoff prompt placeholders need operator critique before reuse. |
