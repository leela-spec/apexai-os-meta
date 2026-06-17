# FILE: .claude/skills/PrecapNextDay/examples/apex-only-template-example/prompts/F3-flow-prompt-pack.md

# Flow Prompt Pack — F3 — APEX output templates/examples

```yaml
flow_prompt_pack_status:
  pack_id: flow_prompt_pack_2026_06_18_F3
  artifact_name: flow_prompt_pack
  execution_day: "2026-06-18"
  flow_id: F3
  project: Apex
  APEX_operator_label: APEX_output_templates_examples
  generation_mode: degraded_generic_prompt_mode
  pack_status: operator_review_recommended
  prompt_execution_status: not_executed
  validation_status: operator_review_recommended
```

## Source Flow Packet

```yaml
source_flow_packet_ref:
  flow_packet_id: flow_packet_2026_06_18_F3
  flow_packet_path_or_slot: ../flows/F3-flow-packet.md
  daily_plan_ref: ../next-day-plan.md
  flow_id: F3
  project: Apex
```

## Sprint Prompt Sequences

| Sprint | Sprint goal | Prompt packet ref/placeholders | Provider/surface hint | Capture hint |
|---|---|---|---|---|
| S1 | Draft main next-day-plan template. | placeholder_prompt_packet_F3_S1_main_template | provider_unspecified | Capture layout decisions. |
| S2 | Draft flow and prompt pack templates. | placeholder_prompt_packet_F3_S2_per_flow_templates | provider_unspecified | Capture placeholder policy. |
| S3 | Draft example fixture links. | placeholder_prompt_packet_F3_S3_example_fixture | provider_unspecified | Capture generated refs. |

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
  handoff_ref: ../handoff/FlowRecap-handoff.md#F3
  FlowRecap_output_created: false
```

## Review Flags

| Flag ID | Flag |
|---|---|
| F3-PROMPT-ORF-001 | Prompt examples are intentionally placeholder-first to avoid prompt doctrine drift. |
