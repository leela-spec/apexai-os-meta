# FILE: .claude/skills/PrecapNextDay/templates/calendar-event-write-request-template.md

# Calendar Event Write Request — <execution_day>

Template role: reviewable calendar workflow-block request.

Schema authority: `references/calendar-event-write-contract.md`.

Default to `no_write_requested` or `review_only`. Do not imply calendar events were created.

## 1. Request Status

```yaml
calendar_event_write_request_status:
  request_id: "calendar_event_write_request_<execution_day>"
  request_role: "<workflow_block_review_only_request|next_day_workflow_block_write_request|degraded_calendar_request>"
  request_status: "<not_requested|draft|review_ready|pending_operator_approval|blocked>"
  write_mode: "<no_write_requested|review_only|create_new_events|update_existing_events|create_or_update|blocked>"
  request_scope: workflow_blocks_only
  calendar_context_status: "<calendar_read_available|manual_constraints_only|unavailable|stale|unknown>"
  actual_calendar_mutation_performed: false
  validation_status: "<valid|valid_with_warnings|operator_review_recommended|low_confidence_auto_generated|blocked_by_missing_operator_decision>"
```

## 2. Source Plan Reference

```yaml
source_plan_ref:
  next_day_plan_id: "<next_day_plan_id>"
  execution_day: "<YYYY-MM-DD>"
  source_status: "<next_day_plan_generated|partial_plan_generated|bootstrap_plan_generated|unknown>"
```

## 3. Approval Gate

```yaml
approval_gate:
  approval_required: "<true|false>"
  approval_status: "<not_required_no_write_requested|pending_operator_approval|approved_for_write|rejected|blocked_by_missing_time|blocked_by_unclear_target|blocked_by_tool_unavailable>"
  approval_scope: "<none|one_event|one_flow|all_workflow_blocks_in_request|partial_selection|unknown>"
  explicit_operator_action_required: "<true|false>"
  acceptable_operator_actions:
    - approve_all
    - approve_selected
    - reject_all
    - edit_times
    - switch_to_review_only
```

## 4. Workflow Blocks

| Block ID | Flow | Title | Timing | Write intent | Approval status | Notes |
|---|---|---|---|---|---|---|
| <calendar_block_id> | <F1-F4> | <title> | <unscheduled_or_time_range> | <review_only|create|update|none> | <pending|not_required|blocked> | <notes> |

## 5. Operator Review Flags

| Flag ID | Severity | Flag | Required action |
|---|---|---|---|
| CAL-ORF-001 | <low|medium|high> | <flag> | <action> |

## 6. Completion Gate

```yaml
calendar_request_completion_gate:
  request_scope_is_workflow_blocks_only: true
  write_mode_is_explicit: true
  approval_gate_present: true
  no_actual_calendar_mutation_claimed: true
  operator_review_flags_present_when_context_missing: true
```
