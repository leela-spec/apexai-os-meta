# FILE: .claude/skills/PrecapNextDay/templates/flow-prompt-pack-template.md

# Flow Prompt Pack — <flow_id> — <execution_day>

Template role: per-flow prompt container.

Schema authority: `references/flow-prompt-pack-contract.md`.

Do not redefine prompt packets, prompt doctrine, routing schema, or provider-specific prompting rules. Use placeholders or refs.

## 1. Pack Status

```yaml
flow_prompt_pack_status:
  pack_id: "flow_prompt_pack_<execution_day>_<flow_id>"
  artifact_name: flow_prompt_pack
  execution_day: "<YYYY-MM-DD>"
  flow_id: "<F1|F2|F3|F4>"
  project: "Apex"
  APEX_operator_label: "<APEX_operator_label>"
  generation_mode: "<standard_mode|bootstrap_mode|prompt_heavy_mode|degraded_generic_prompt_mode>"
  pack_status: "<ready_for_operator_review|operator_review_recommended|auto_generated|low_confidence_auto_generated|blocked_by_missing_operator_decision>"
  prompt_execution_status: not_executed
  validation_status: "<valid|valid_with_warnings|operator_review_recommended|low_confidence_auto_generated|blocked_by_missing_operator_decision>"
```

## 2. Source Flow Packet

```yaml
source_flow_packet_ref:
  flow_packet_id: "<flow_packet_id>"
  flow_packet_path_or_slot: "<flow_packet_ref>"
  daily_plan_ref: "<next_day_plan_ref>"
  flow_id: "<flow_id>"
  project: "Apex"
```

## 3. Prompt Pack Policy

```yaml
prompt_pack_policy:
  one_file_per_flow_prompt_pack: true
  embedded_in_daily_plan: false
  referenced_from_flow_packet: true
  one_primary_prompt_system_only: true
  alternatives_allowed_by_default: false
  light_capture_hints_allowed: true
  prompt_packets_are_referenced_not_redefined: true
  degraded_generic_prompt_mode_allowed_when_dependencies_missing: true
```

## 4. Sprint Prompt Sequences

| Sprint | Sprint goal | Prompt packet ref/placeholders | Provider/surface hint | Routing/usage note | Capture hint | Review flag |
|---|---|---|---|---|---|---|
| S1 | <goal> | <prompt_packet_ref_or_placeholder> | <provider_hint> | <usage_note> | <capture_hint> | <flag> |
| S2 | <goal> | <prompt_packet_ref_or_placeholder> | <provider_hint> | <usage_note> | <capture_hint> | <flag> |
| S3 | <goal> | <prompt_packet_ref_or_placeholder> | <provider_hint> | <usage_note> | <capture_hint> | <flag> |

## 5. Prompt Packet Placeholder Pattern

Use this when prompt-engineering outputs are missing.

```yaml
prompt_packet_placeholder:
  prompt_packet_id: "<prompt_packet_<flow_id>_<sprint_id>_<short_slug>>"
  source_authority: prompt-engineering
  status: "<referenced|placeholder|degraded_generic_prompt_mode>"
  prompt_task_type_request: "<research|synthesis|planning|coding|critique|file_generation|validation|operator_defined|infer_from_context>"
  expected_output_type: "<expected_output_type_or_unknown>"
  final_prompt_text: "<not_defined_here>"
  review_required: true
```

## 6. Routing and Usage Summary

```yaml
routing_usage_summary:
  routing_recommendation_ref: "<routing_ref_or_missing>"
  planned_usage_budget_ref: "<planned_usage_ref_or_missing>"
  usage_tracking_summary_ref: "<usage_summary_ref>"
  high_value_scarce_mode_candidate: "<true|false|unknown>"
  low_cost_candidate: "<true|false|unknown>"
  quota_or_price_claims_made: false
  review_flags:
    - "<usage_or_routing_flag>"
```

## 7. Workflow Alignment Summary

```yaml
workflow_alignment_summary:
  workflow_process_validation_ref: "<workflow_process_validation_ref_or_missing>"
  workflow_stage: "<source_authority_value_or_unknown>"
  process_stage: "<source_authority_value_or_unknown>"
  expected_output_type: "<source_authority_value_or_unknown>"
  dependency_status: "<available|partial|missing|low_confidence_inferred>"
```

## 8. Light Capture Hints

| Sprint | What to capture after execution | Capture destination |
|---|---|---|
| S1 | <planned_vs_actual_result> | raw_flow_dump_template |
| S2 | <decisions_outputs_blockers> | raw_flow_dump_template |
| S3 | <handoff_notes_and_next_step_guess> | FlowRecap_handoff_block |

## 9. FlowRecap Preparation

```yaml
FlowRecap_preparation:
  status: prepared_not_run
  handoff_ref: "<FlowRecap_handoff_ref>"
  prompt_results_expected_after_execution: true
  FlowRecap_output_created: false
```

## 10. Completion Gate

```yaml
flow_prompt_pack_completion_gate:
  source_flow_packet_ref_present: true
  sprint_prompt_sequences_present_or_degraded: true
  prompt_packets_referenced_not_redefined: true
  routing_usage_summary_present_or_degraded: true
  workflow_alignment_summary_present_or_degraded: true
  light_capture_hints_present: true
  FlowRecap_preparation_present_without_running_FlowRecap: true
  prompts_not_executed_by_PreCap: true
```
