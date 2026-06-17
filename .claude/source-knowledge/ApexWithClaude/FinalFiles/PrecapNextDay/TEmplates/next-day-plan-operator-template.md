# PreCap Next Day — {{execution_day}}

## 1. Plan Status

```yaml
plan_status:
  plan_id: {{plan_id}}
  artifact_name: next_day_plan
  created_or_updated_at: {{created_or_updated_at}}
  execution_day: {{execution_day}}
  generation_mode: {{full_context_mode|standard_mode|recap_recovery_mode|bootstrap_mode|calendar_constrained_mode|prompt_heavy_mode}}
  review_status: {{operator_approved|operator_review_recommended|auto_generated|low_confidence_auto_generated|blocked_by_external_tool_unavailable}}
  validation_status: {{valid|valid_with_warnings|operator_review_recommended|low_confidence_auto_generated|blocked_by_missing_operator_decision}}
```

## 2. Operator Action Needed

| Action | Required? | Reason | Target file/ref |
|---|---:|---|---|
| {{approve/edit/supply_missing_input/accept_calendar_write_request/execute_flow/run_FlowRecap_after_execution}} | {{true/false}} | {{reason}} | {{path_or_ref}} |

## 3. Input Context

| Input | Status | Handling | Confidence effect |
|---|---|---|---|
| operator_day_intent | {{supplied/missing/unknown}} | {{used/omitted/deferred_to_operator_review}} | {{none/low/medium/high}} |
| current_project_status_overview | {{supplied/missing/unknown}} | {{used/omitted/deferred_to_operator_review}} | {{none/low/medium/high}} |
| weekly_plan_packet | {{supplied/missing/unknown}} | {{used/omitted/deferred_to_operator_review}} | {{none/low/medium/high}} |
| flow_recap_packets | {{supplied/missing/unknown}} | {{used/omitted/deferred_to_operator_review}} | {{none/low/medium/high}} |
| calendar_events | {{available/missing/unavailable_tool/not_applicable}} | {{used/omitted/deferred_to_operator_review}} | {{none/low/medium/high}} |
| AI_surface_inventory | {{supplied/missing/unknown}} | {{used/omitted/deferred_to_operator_review}} | {{none/low/medium/high}} |
| model_usage_summary | {{supplied/missing/unknown}} | {{used/omitted/deferred_to_operator_review}} | {{none/low/medium/high}} |

## 4. Day Strategy Summary

```yaml
day_strategy_summary:
  day_intent: "{{operator-facing daily intent}}"
  strategic_focus: "{{one concise focus statement}}"
  capacity_assumption: "{{known or unknown capacity assumption}}"
  flow_balance_strategy: "{{how F1-F4 are represented, compressed, skipped, or omitted}}"
  recovery_logic: "{{how missing context/recovery is handled}}"
  main_risks:
    - {{risk_1}}
  operator_attention_needed:
    - {{operator_action_1}}
```

## 5. Flow Overview

| Flow | Project | Status | Goal | Sprints | Output refs | Review flags |
|---|---|---|---|---:|---|---|
| F1 | Leela | {{planned/compressed/omitted/skipped/blocked/low_confidence_auto_generated}} | {{goal_or_review_placeholder}} | {{0-3}} | {{flow_packet_ref}}, {{prompt_pack_ref}} | {{flags}} |
| F2 | MasterOfArts | {{planned/compressed/omitted/skipped/blocked/low_confidence_auto_generated}} | {{goal_or_review_placeholder}} | {{0-3}} | {{flow_packet_ref}}, {{prompt_pack_ref}} | {{flags}} |
| F3 | Apex | {{planned/compressed/omitted/skipped/blocked/low_confidence_auto_generated}} | {{goal_or_review_placeholder}} | {{0-3}} | {{flow_packet_ref}}, {{prompt_pack_ref}} | {{flags}} |
| F4 | Residual | {{planned/compressed/omitted/skipped/blocked/low_confidence_auto_generated}} | {{goal_or_review_placeholder}} | {{0-3}} | {{flow_packet_ref}}, {{prompt_pack_ref}} | {{flags}} |

## 6. Sprint Overview

| Flow | Sprint | Sprint role | Goal | Expected output | Prompt pack ref | Capture focus | Status |
|---|---|---|---|---|---|---|---|
| {{F1-F4}} | {{S1/S2/S3}} | {{first_work_sprint/second_work_or_deepening_sprint/recap_digest_preparation_sprint/compressed_work_sprint}} | {{sprint_goal}} | {{expected_output_type}} | {{prompt_pack_ref#sprint}} | {{capture_focus}} | {{not_started/blocked/skipped}} |

## 7. Generated File Index

| Artifact | Role | Path/ref | Status | Operator action |
|---|---|---|---|---|
| next_day_plan | main operator plan | {{path}} | {{created/defined_inline/referenced_existing}} | {{action_or_none}} |
| flow_packet | per-flow execution container | {{path}} | {{created/defined_inline/referenced_existing}} | {{action_or_none}} |
| flow_prompt_pack | per-flow prompt container | {{path}} | {{created/defined_inline/referenced_existing}} | {{action_or_none}} |
| raw_flow_dump_template | execution capture shell | {{path}} | {{created/defined_inline/referenced_existing}} | {{action_or_none}} |
| skipped_flow_marker_template | skipped-flow capture shell | {{path}} | {{created/defined_inline/referenced_existing}} | {{action_or_none}} |
| calendar_event_write_request | workflow block request | {{path}} | {{pending_operator_approval/not_needed}} | {{accept/reject/edit}} |
| usage_tracking_plan | usage planning summary | {{path}} | {{created/partial/missing_dependency}} | {{review_or_none}} |

## 8. Prompt Pack Index

| Flow | Prompt pack | Status | Provider confidence | Rationale present? | Failure hints present? |
|---|---|---|---|---:|---:|
| F1 | {{ref}} | {{ready/degraded/omitted}} | {{high/medium/low/unknown}} | {{true/false}} | {{true/false}} |
| F2 | {{ref}} | {{ready/degraded/omitted}} | {{high/medium/low/unknown}} | {{true/false}} | {{true/false}} |
| F3 | {{ref}} | {{ready/degraded/omitted}} | {{high/medium/low/unknown}} | {{true/false}} | {{true/false}} |
| F4 | {{ref}} | {{ready/degraded/omitted}} | {{high/medium/low/unknown}} | {{true/false}} | {{true/false}} |

## 9. Calendar Write Summary

```yaml
calendar_write_summary:
  calendar_context_status: {{calendar_read_available|manual_constraints_only|calendar_unavailable|calendar_not_requested}}
  workflow_blocks_defined: {{true|false}}
  write_requests_present: {{true|false}}
  operator_acceptance_required: true
  write_claim_status: {{request_only|no_write_needed|write_failed_operator_note_created}}
  note: "No calendar mutation is claimed unless operator approval and tool confirmation exist."
```

## 10. Usage Tracking Summary

```yaml
usage_tracking_summary:
  usage_plan_status: {{present|partial|missing_dependency|low_confidence_auto_generated}}
  routing_recommendation_status: {{present|partial|not_needed|missing_dependency|operator_review_recommended}}
  scarce_surface_use_policy: {{deliberate_monthly_quota_use|conserve_due_to_low_value_task|unknown_quota_operator_review|no_scarce_surface_planned}}
  usage_tracking_tags_present: {{true|false}}
```

## 11. FlowRecap Preparation Summary

```yaml
FlowRecap_preparation_summary:
  raw_flow_dump_templates_present: {{true|false}}
  skipped_flow_marker_templates_present: {{true|false}}
  FlowRecap_handoff_blocks_present: {{true|false}}
  recap_capture_scope:
    - what_was_done
    - outputs_created
    - decisions_made
    - blockers
    - skipped_or_partial_work
    - prompt_results
    - usage_delta
    - next_step_guess
    - operator_validation_notes
  FlowRecap_not_run: true
```

## 12. Operator Review Flags

| Flag | Severity | Affected output | Operator action |
|---|---|---|---|
| {{flag_id}} | {{low/medium/high}} | {{artifact/ref}} | {{approve/edit/supply_missing_context/choose_between_options/ignore_for_now}} |

## 13. Completion Gate

```yaml
day_level_completion_gate:
  next_day_plan_present: true
  each_active_flow_has_flow_packet_ref: {{true|false}}
  each_active_flow_has_prompt_pack_ref: {{true|false}}
  raw_flow_dump_capture_prepared: {{true|false}}
  skipped_flow_marker_capture_prepared: {{true|false}}
  FlowRecap_handoff_prepared: {{true|false}}
  operator_review_flags_present: {{true|false}}
  no_project_work_executed: true
  no_prompt_execution_performed: true
  no_calendar_write_performed: true
  no_FlowRecap_run: true
  no_status_merge_run: true
```
