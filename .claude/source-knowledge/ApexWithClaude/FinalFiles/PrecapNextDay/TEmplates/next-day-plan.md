# PreCap Next Day — 2026-06-18 — Apex/Hermes Skill Database Buildout

## 1. Plan Status

```yaml
plan_status:
  plan_id: next_day_plan_2026_06_18_apex_hermes_skill_database
  artifact_name: next_day_plan
  created_or_updated_at: "2026-06-17"
  execution_day: "2026-06-18"
  generation_mode: standard_mode
  review_status: operator_review_recommended
  validation_status: valid_with_warnings
```

## 2. Operator Action Needed

| Action | Required? | Reason | Target file/ref |
|---|---:|---|---|
| approve | true | F3 is selected as main flow because the supplied task is Apex/Hermes orchestration skill database buildout. | `flows/F3-flow-packet.md` |
| edit | true | F1 and F2 are compressed to supporting/reference roles, not full execution. | `next-day-plan.md#flow-overview` |
| accept_calendar_write_request | false | Calendar is review-only because no calendar context was supplied. | `calendar/calendar-event-write-request.md` |
| execute_flow | false | PreCap prepares work but does not execute project work. | all flow packets |
| run_FlowRecap_after_execution | false | FlowRecap is prepared but not run here. | `handoff/FlowRecap-handoff.md` |

## 3. Input Context

| Input | Status | Handling | Confidence effect |
|---|---|---|---|
| operator_day_intent | supplied | used | none |
| current_project_status_overview | partial | used_with_review_flag | medium |
| workflow_example_database | supplied | used | none |
| process_ranking | supplied | used | low |
| Apex orchestration research reference | supplied | used | low |
| weekly_plan_packet | missing | omitted_as_missing | medium |
| flow_recap_packets | missing | omitted_as_missing | medium |
| calendar_events | missing | deferred_to_operator_review | medium |
| AI_surface_inventory | missing | deferred_to_operator_review | medium |
| model_usage_summary | missing | deferred_to_operator_review | medium |

## 4. Day Strategy Summary

```yaml
day_strategy_summary:
  day_intent: "Create operator-facing PreCap Next Day templates and examples for the Apex/Hermes skill database buildout workflow."
  strategic_focus: "Move the orchestration-system template layer from contract-only artifacts into usable operator templates."
  capacity_assumption: "Standard planning day; no calendar constraints supplied."
  flow_balance_strategy: "Plan F3 as main flow; compress F1, F2, and F4 into support, reference, and cleanup roles."
  recovery_logic: "Keep unverified project state and missing routing/calendar context as review flags."
  main_risks:
    - source_drift_from_contracts
    - too_large_single_output
    - prompt_pack_bloat
    - missing_calendar_context
    - missing_usage_context
  operator_attention_needed:
    - approve_template_file_split
    - confirm_F3_main_flow
    - decide_later_whether_examples_become_package_files
```

## 5. Flow Overview

| Flow | Project | Status | Goal | Sprints | Output refs | Review flags |
|---|---|---|---|---:|---|---|
| F1 | Leela | compressed | Preserve a placeholder for Leela app/product relevance without inventing Leela work. | 1 | `flows/F1-flow-packet.md`, `prompts/F1-flow-prompt-pack.md` | `missing_current_leela_status`, `compressed_flow_requires_approval` |
| F2 | MasterOfArts | compressed | Use the attached Master of Arts workflow database only as source/context for examples. | 1 | `flows/F2-flow-packet.md`, `prompts/F2-flow-prompt-pack.md` | `supporting_context_only`, `compressed_flow_requires_approval` |
| F3 | Apex | planned | Create PreCap Next Day operator templates and Apex/Hermes skill database example files. | 3 | `flows/F3-flow-packet.md`, `prompts/F3-flow-prompt-pack.md` | `operator_review_recommended` |
| F4 | Residual | compressed | Capture unresolved template decisions, missing context, and follow-up review items. | 1 | `flows/F4-flow-packet.md`, `prompts/F4-flow-prompt-pack.md` | `missing_calendar_context`, `missing_usage_context` |

## 6. Sprint Overview

| Flow | Sprint | Sprint role | Goal | Expected output | Prompt pack ref | Capture focus | Status |
|---|---|---|---|---|---|---|---|
| F1 | S1 | compressed_work_sprint | Identify whether any Leela-facing note belongs in the template pack. | review_note | `prompts/F1-flow-prompt-pack.md#S1` | unresolved_question | not_started |
| F2 | S1 | compressed_work_sprint | Preserve source-grounded workflow examples from the Master of Arts database. | source_context_summary | `prompts/F2-flow-prompt-pack.md#S1` | source_context_used | not_started |
| F3 | S1 | first_work_sprint | Define the template file set and operator-output format rules. | template_file_set | `prompts/F3-flow-prompt-pack.md#S1` | artifact_created | not_started |
| F3 | S2 | second_work_or_deepening_sprint | Fill templates and the Apex/Hermes example pack. | filled_template_pack | `prompts/F3-flow-prompt-pack.md#S2` | artifact_created | not_started |
| F3 | S3 | recap_digest_preparation_sprint | Prepare capture and FlowRecap handoff without running FlowRecap. | recap_handoff_notes | `prompts/F3-flow-prompt-pack.md#S3` | next_step_guess | not_started |
| F4 | S1 | compressed_work_sprint | Collect unresolved decisions and missing inputs. | operator_review_list | `prompts/F4-flow-prompt-pack.md#S1` | unresolved_question | not_started |

## 7. Generated File Index

| Artifact | Role | Path/ref | Status | Operator action |
|---|---|---|---|---|
| next_day_plan | main operator plan | `next-day-plan.md` | created | approve/edit |
| flow_packet | F1 support flow | `flows/F1-flow-packet.md` | created | approve/edit |
| flow_packet | F2 source-context flow | `flows/F2-flow-packet.md` | created | approve/edit |
| flow_packet | F3 main Apex work flow | `flows/F3-flow-packet.md` | created | approve |
| flow_packet | F4 residual cleanup flow | `flows/F4-flow-packet.md` | created | approve/edit |
| flow_prompt_pack | F1 prompt shell | `prompts/F1-flow-prompt-pack.md` | created | review |
| flow_prompt_pack | F2 prompt shell | `prompts/F2-flow-prompt-pack.md` | created | review |
| flow_prompt_pack | F3 prompt shell | `prompts/F3-flow-prompt-pack.md` | created | review |
| flow_prompt_pack | F4 prompt shell | `prompts/F4-flow-prompt-pack.md` | created | review |
| raw_flow_dump_template | capture shell | `capture/raw-flow-dump-template.md` | created | fill_after_execution |
| skipped_flow_marker_template | skipped-flow shell | `capture/skipped-flow-marker-template.md` | created | fill_if_skipped |
| calendar_event_write_request | review-only calendar shell | `calendar/calendar-event-write-request.md` | created | optional |
| usage_tracking_plan | usage/routing shell | `usage/usage-tracking-summary.md` | created | review |
| FlowRecap_handoff_block | recap handoff shell | `handoff/FlowRecap-handoff.md` | created | use_after_execution |

## 8. Prompt Pack Index

| Flow | Prompt pack | Status | Provider confidence | Rationale present? | Failure hints present? |
|---|---|---|---|---:|---:|
| F1 | `prompts/F1-flow-prompt-pack.md` | generic_degraded_mode | low | true | true |
| F2 | `prompts/F2-flow-prompt-pack.md` | generic_degraded_mode | medium | true | true |
| F3 | `prompts/F3-flow-prompt-pack.md` | operator_review_recommended | medium | true | true |
| F4 | `prompts/F4-flow-prompt-pack.md` | generic_degraded_mode | low | true | true |

## 9. Calendar Write Summary

```yaml
calendar_write_summary:
  calendar_context_status: calendar_unavailable
  workflow_blocks_defined: false
  write_requests_present: true
  operator_acceptance_required: true
  write_claim_status: request_only
  note: "No calendar mutation has been performed."
```

## 10. Usage Tracking Summary

```yaml
usage_tracking_summary:
  usage_plan_status: low_confidence_auto_generated
  routing_recommendation_status: missing_dependency
  scarce_surface_use_policy: unknown_quota_operator_review
  usage_tracking_tags_present: true
```

## 11. FlowRecap Preparation Summary

```yaml
FlowRecap_preparation_summary:
  raw_flow_dump_templates_present: true
  skipped_flow_marker_templates_present: true
  FlowRecap_handoff_blocks_present: true
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
| confirm_F3_main_flow | medium | next_day_plan | approve/edit |
| compressed_F1_requires_approval | low | F1-flow-packet | approve/edit |
| compressed_F2_requires_approval | low | F2-flow-packet | approve/edit |
| missing_calendar_context | medium | calendar-event-write-request | supply_missing_context/ignore_for_now |
| missing_usage_context | medium | usage-tracking-summary | supply_missing_context/ignore_for_now |
| examples_not_canonical_package_files_yet | medium | examples folder | choose_between_options |
| prompt_engineering_dependency_missing | medium | prompt packs | approve degraded mode or supply dependency |

## 13. Completion Gate

```yaml
day_level_completion_gate:
  next_day_plan_present: true
  each_active_flow_has_flow_packet_ref: true
  each_active_flow_has_prompt_pack_ref: true
  raw_flow_dump_capture_prepared: true
  skipped_flow_marker_capture_prepared: true
  FlowRecap_handoff_prepared: true
  operator_review_flags_present: true
  no_project_work_executed: true
  no_prompt_execution_performed: true
  no_calendar_write_performed: true
  no_FlowRecap_run: true
  no_status_merge_run: true
```
