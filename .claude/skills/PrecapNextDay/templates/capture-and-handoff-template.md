# FILE: .claude/skills/PrecapNextDay/templates/capture-and-handoff-template.md

# Capture and Handoff Template — <execution_day>

Template role: prepared capture scaffolding for after operator execution.

Schema authority: `references/flow-packet-contract.md` for raw flow dump, skipped flow marker, and FlowRecap handoff block.

Prepared by PreCap Next Day. Filled after execution. FlowRecap is not run here.

## 1. Capture Status

```yaml
capture_handoff_status:
  execution_day: "<YYYY-MM-DD>"
  source_plan_ref: "<next_day_plan_ref>"
  raw_flow_dump_template_status: prepared_not_filled
  skipped_flow_marker_template_status: prepared_if_needed
  FlowRecap_handoff_status: prepared_not_run
  project_execution_status: not_executed
  validation_status: "<valid|valid_with_warnings|operator_review_recommended|low_confidence_auto_generated|blocked_by_missing_operator_decision>"
```

## 2. Raw Flow Dump Template

```yaml
raw_flow_dump_template:
  flow_id: "<F1|F2|F3|F4>"
  flow_packet_ref: "<flow_packet_ref>"
  planned_goal: "<planned_goal>"
  actual_result: "<fill_after_execution>"
  decisions_made:
    - "<fill_after_execution>"
  blockers:
    - "<fill_after_execution>"
  artifacts_created:
    - "<fill_after_execution>"
  prompt_results:
    - "<fill_after_execution>"
  model_usage_notes:
    - "<fill_after_execution>"
  next_step_guess: "<fill_after_execution>"
  filled_by_PreCap: false
```

## 3. Skipped Flow Marker Template

```yaml
skipped_flow_marker_template:
  flow_id: "<F1|F2|F3|F4>"
  flow_packet_ref: "<flow_packet_ref>"
  skipped: "<true|false>"
  skip_reason: "<operator_or_execution_reason>"
  impact_on_plan: "<impact>"
  recovery_recommendation: "<recommendation>"
  filled_by_PreCap: false
```

## 4. Planned vs Actual Capture Table

| Flow | Planned output | Actual output | Delta | Needs follow-up? |
|---|---|---|---|---:|
| F1 | <planned> | <fill_after_execution> | <fill_after_execution> | <true/false> |
| F2 | <planned> | <fill_after_execution> | <fill_after_execution> | <true/false> |
| F3 | <planned> | <fill_after_execution> | <fill_after_execution> | <true/false> |
| F4 | <planned> | <fill_after_execution> | <fill_after_execution> | <true/false> |

## 5. FlowRecap Handoff Block

```yaml
FlowRecap_handoff_block:
  handoff_id: "FlowRecap_handoff_<execution_day>"
  source_next_day_plan_ref: "<next_day_plan_ref>"
  source_flow_packet_refs:
    - "<flow_packet_ref>"
  source_prompt_pack_refs:
    - "<flow_prompt_pack_ref>"
  capture_refs:
    raw_flow_dump_template: "<raw_flow_dump_template_ref>"
    skipped_flow_marker_template: "<skipped_flow_marker_template_ref>"
  planned_outputs_summary: "<summary>"
  operator_review_flags:
    - "<flag>"
  FlowRecap_output_created: false
  ready_for_later_FlowRecap: "<true|false>"
```

## 6. Operator Notes

| Note type | Note |
|---|---|
| Decision | <decision_after_execution> |
| Blocker | <blocker_after_execution> |
| Artifact | <artifact_after_execution> |
| Next step | <next_step_after_execution> |
