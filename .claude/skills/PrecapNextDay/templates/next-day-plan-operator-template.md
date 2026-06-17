# FILE: .claude/skills/PrecapNextDay/templates/next-day-plan-operator-template.md

# PreCap Next Day — <execution_day>

Template role: main operator dashboard for `next_day_plan`.

Schema authority: `references/daily-plan-output-contract.md`.

Do not embed full flow packets or full prompt packs. Link to them in the generated file index.

## 1. Plan Status

```yaml
plan_status:
  plan_id: "<next_day_plan_YYYY_MM_DD_short_slug>"
  artifact_name: next_day_plan
  execution_day: "<YYYY-MM-DD>"
  generation_mode: "<full_context_mode|standard_mode|recap_recovery_mode|bootstrap_mode|calendar_constrained_mode|prompt_heavy_mode>"
  review_status: "<operator_approved|operator_review_recommended|auto_generated|low_confidence_auto_generated|blocked_by_external_tool_unavailable>"
  project_execution_status: not_executed
  prompt_execution_status: not_executed
  calendar_write_status: "<no_write_requested|review_only|pending_operator_approval>"
  FlowRecap_status: handoff_prepared_not_run
  validation_status: "<valid|valid_with_warnings|operator_review_recommended|low_confidence_auto_generated|blocked_by_missing_operator_decision>"
```

## 2. Operator Review First

| Priority | Review item | Why it matters | Operator action |
|---:|---|---|---|
| 1 | <review_item> | <reason> | <approve/edit/reject/clarify> |

## 3. Input Context

| Input category | Status | Used for planning? | Confidence | Notes |
|---|---|---:|---|---|
| operator_day_intent | <supplied|missing|inferred|unclear> | <yes/no> | <high|medium|low|unknown> | <notes> |
| current_project_status_overview | <current|stale|missing|unknown> | <yes/no> | <high|medium|low|unknown> | <notes> |
| calendar_context | <available|manual_only|missing|unknown> | <yes/no> | <high|medium|low|unknown> | <notes> |
| usage_context | <available|partial|missing|unknown> | <yes/no> | <high|medium|low|unknown> | <notes> |

```yaml
input_resilience_summary:
  missing_inputs:
    - "<missing_input>"
  assumptions:
    - "<assumption>"
  degraded_mode_reasons:
    - "<reason_if_any>"
  planning_conflicts:
    - "<conflict_if_any>"
```

## 4. APEX Day Strategy

<Short operator-readable day frame. State what the APEX-only buildout is trying to produce, what is intentionally not executed, and how the flows relate.>

## 5. APEX Flow Overview

| Flow | APEX role | Status | Sprint count | Primary goal | Expected output | Flow packet | Prompt pack | Review flags |
|---|---|---|---:|---|---|---|---|---|
| F1 | APEX repo foundation | <planned|compressed|omitted|skipped|blocked|placeholder> | <1-3> | <goal> | <output> | <ref> | <ref> | <flags> |
| F2 | APEX skill database contracts | <planned|compressed|omitted|skipped|blocked|placeholder> | <1-3> | <goal> | <output> | <ref> | <ref> | <flags> |
| F3 | APEX output templates/examples | <planned|compressed|omitted|skipped|blocked|placeholder> | <1-3> | <goal> | <output> | <ref> | <ref> | <flags> |
| F4 | APEX validation/handover | <planned|compressed|omitted|skipped|blocked|placeholder> | <1-3> | <goal> | <output> | <ref> | <ref> | <flags> |

## 6. Generated File Index

| Artifact | Path/ref | Status | Depends on | Operator action |
|---|---|---|---|---|
| next_day_plan | <this_file_ref> | <draft|review_ready|approved> | daily-plan-output-contract | <review> |
| F1 flow_packet | <path> | <draft|review_ready|approved> | flow-packet-contract | <review> |
| F1 flow_prompt_pack | <path> | <draft|review_ready|approved> | flow-prompt-pack-contract | <review> |
| usage_tracking_summary | <path> | <draft|review_ready|degraded> | usage-tracking-dependency-contract | <review> |
| calendar_event_write_request | <path> | <not_requested|review_only|pending_approval> | calendar-event-write-contract | <review/approve_none> |
| FlowRecap_handoff | <path> | prepared_not_run | flow-packet-contract | <review> |

## 7. Usage / Calendar / Workflow Summaries

```yaml
usage_calendar_workflow_summary:
  usage_tracking_status: "<available|partial|missing|operator_review_needed>"
  routing_status: "<provided|generic_defaults_used|not_available>"
  calendar_request_status: "<not_requested|review_only|pending_operator_approval|blocked>"
  workflow_process_status: "<available|partial|missing|low_confidence_inferred>"
  review_required: true
```

## 8. Capture and FlowRecap Preparation

| Capture artifact | Prepared? | Filled by PreCap? | Notes |
|---|---:|---:|---|
| raw_flow_dump_template | <true/false> | false | <notes> |
| skipped_flow_marker_template | <true/false> | false | <notes> |
| FlowRecap_handoff_block | <true/false> | false | <notes> |

## 9. Operator Review Flags

| Flag ID | Severity | Flag | Suggested action |
|---|---|---|---|
| ORF-001 | <low|medium|high> | <flag> | <action> |

## 10. Completion Gate

```yaml
completion_gate:
  next_day_plan_exists: true
  fixed_flows_are_represented_or_explicitly_omitted: true
  represented_flows_have_flow_packet_references: true
  represented_flows_have_flow_prompt_pack_references: true
  prompt_packs_are_ready_or_marked_degraded_with_review_flags: true
  usage_tracking_hooks_exist_or_degraded_usage_review_flag_exists: true
  calendar_writes_are_request_based_and_not_claimed_completed_without_approval: true
  FlowRecap_handoff_exists_without_running_FlowRecap: true
  missing_inputs_are_review_flags_not_blockers: true
  no_project_execution_FlowRecap_output_or_status_merge_created: true
```
