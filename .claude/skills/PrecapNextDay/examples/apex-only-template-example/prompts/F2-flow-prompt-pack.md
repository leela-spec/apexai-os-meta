# FILE: .claude/skills/PrecapNextDay/examples/apex-only-template-example/prompts/F2-flow-prompt-pack.md

# Flow Prompt Pack — F2 — APEX skill database contracts

```yaml
flow_prompt_pack_status:
  pack_id: flow_prompt_pack_2026_06_18_F2
  artifact_name: flow_prompt_pack
  execution_day: "2026-06-18"
  flow_id: F2
  project: Apex
  APEX_operator_label: APEX_skill_database_contracts
  generation_mode: degraded_generic_prompt_mode
  pack_status: operator_review_recommended
  prompt_execution_status: not_executed
  validation_status: operator_review_recommended
```

## Source Flow Packet

```yaml
source_flow_packet_ref:
  flow_packet_id: flow_packet_2026_06_18_F2
  flow_packet_path_or_slot: ../flows/F2-flow-packet.md
  daily_plan_ref: ../next-day-plan.md
  flow_id: F2
  project: Apex
```

## Sprint Prompt Sequences

| Sprint | Sprint goal | Prompt packet ref/placeholders | Provider/surface hint | Capture hint |
|---|---|---|---|---|
| S1 | Map contract authority. | placeholder_prompt_packet_F2_S1_contract_map | provider_unspecified | Capture contract-owned fields. |
| S2 | Identify schema vs presentation boundaries. | placeholder_prompt_packet_F2_S2_boundary_map | provider_unspecified | Capture presentation-only labels. |
| S3 | Prepare contract boundary notes. | placeholder_prompt_packet_F2_S3_boundary_handoff | provider_unspecified | Capture schema drift warnings. |

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
  handoff_ref: ../handoff/FlowRecap-handoff.md#F2
  FlowRecap_output_created: false
```

## Review Flags

| Flag ID | Flag |
|---|---|
| F2-PROMPT-ORF-001 | Contract mapping prompts remain placeholders until upstream prompt-engineering is applied. |
