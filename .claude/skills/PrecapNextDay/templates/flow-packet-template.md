# FILE: .claude/skills/PrecapNextDay/templates/flow-packet-template.md

# Flow Packet — <flow_id> — <execution_day>

Template role: per-flow execution container prepared by PreCap Next Day.

Schema authority: `references/flow-packet-contract.md`.

Do not execute work. Do not fill raw-flow dump results. Do not run FlowRecap.

## 1. Packet Status

```yaml
flow_packet_status:
  packet_id: "flow_packet_<execution_day>_<flow_id>"
  artifact_name: flow_packet
  execution_day: "<YYYY-MM-DD>"
  flow_id: "<F1|F2|F3|F4>"
  project: "Apex"
  APEX_operator_label: "<APEX_repo_foundation|APEX_skill_database_contracts|APEX_output_templates_examples|APEX_validation_handover>"
  generation_mode: "<standard_mode|bootstrap_mode|low_confidence_degraded_mode>"
  review_status: "<operator_review_recommended|auto_generated|low_confidence_auto_generated>"
  flow_status: "<planned|compressed|omitted|skipped|blocked|placeholder>"
  validation_status: "<valid|valid_with_warnings|operator_review_recommended|low_confidence_auto_generated|blocked_by_missing_operator_decision>"
```

## 2. Flow Identity

| Field | Value | Notes |
|---|---|---|
| Flow ID | <flow_id> | Contract flow slot. |
| Project | Apex | APEX-only template build phase. |
| Contract-safe flow role | <flow_role> | Use allowed contract value if constrained. |
| Operator label | <APEX_operator_label> | Presentation-only APEX label. |
| Default flow? | <true/false> | <notes> |
| Override reason | <reason_if_any> | Use when APEX-only label overrides historical default example role. |

## 3. Flow Context Summary

```yaml
flow_context_summary:
  primary_goal: "<goal>"
  source_context_used:
    - "<source_or_note>"
  missing_context:
    - "<missing_context>"
  assumptions:
    - "<assumption>"
  confidence: "<high|medium|low|unknown>"
```

## 4. Sprint Plan

| Sprint | Sprint focus | Expected output | Workflow/process label | Prompt pack ref | Review flag |
|---|---|---|---|---|---|
| S1 | <focus> | <output> | <workflow_process_label_or_unknown> | <prompt_pack_ref#S1> | <flag> |
| S2 | <focus> | <output> | <workflow_process_label_or_unknown> | <prompt_pack_ref#S2> | <flag> |
| S3 | <capture_or_handoff_focus> | <output> | <workflow_process_label_or_unknown> | <prompt_pack_ref#S3> | <flag> |

## 5. Expected Outputs

| Output | Path/ref | Status | Filled now? |
|---|---|---|---:|
| flow_packet | <this_file_ref> | <draft|review_ready> | true |
| flow_prompt_pack | <prompt_pack_ref> | <draft|review_ready|degraded> | false |
| raw_flow_dump_template | <raw_flow_dump_template_ref> | prepared | false |
| skipped_flow_marker_template | <skipped_flow_marker_template_ref> | prepared_if_needed | false |
| FlowRecap_handoff_block | <FlowRecap_handoff_ref> | prepared_not_run | false |

## 6. Usage and Routing References

```yaml
usage_tracking_refs:
  usage_summary_ref: "<usage_tracking_summary_ref>"
  routing_recommendation_ref: "<routing_ref_or_missing>"
  planned_usage_budget_ref: "<planned_usage_ref_or_missing>"
  usage_tracking_confidence: "<high|medium|low|unknown>"
  quota_claims_avoided: true
```

## 7. Capture Preparation

```yaml
flow_execution_capture_preparation:
  raw_flow_dump_template_ref: "<raw_flow_dump_template_ref>"
  skipped_flow_marker_template_ref: "<skipped_flow_marker_template_ref>"
  planned_vs_actual_capture_required: true
  prepared_by_PreCap: true
  filled_by_PreCap: false
```

## 8. FlowRecap Handoff Preparation

```yaml
FlowRecap_handoff_block:
  handoff_ref: "<FlowRecap_handoff_ref>"
  handoff_status: prepared_not_run
  includes:
    - planned_goal
    - sprint_plan
    - expected_outputs
    - capture_refs
    - review_flags
  FlowRecap_output_created: false
```

## 9. Operator Review Flags

| Flag ID | Severity | Flag | Suggested action |
|---|---|---|---|
| <flow_id>-ORF-001 | <low|medium|high> | <flag> | <action> |

## 10. Completion Gate

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
