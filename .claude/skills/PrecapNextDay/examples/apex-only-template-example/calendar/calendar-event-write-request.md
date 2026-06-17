# FILE: .claude/skills/PrecapNextDay/examples/apex-only-template-example/calendar/calendar-event-write-request.md

# Calendar Event Write Request — APEX example

This example is review-only. No calendar event was created or updated.

```yaml
calendar_event_write_request_status:
  request_id: calendar_event_write_request_2026_06_18_apex_template_layer
  request_role: workflow_block_review_only_request
  request_status: review_ready
  write_mode: review_only
  request_scope: workflow_blocks_only
  calendar_context_status: unknown
  actual_calendar_mutation_performed: false
  validation_status: operator_review_recommended
```

## Source Plan Reference

```yaml
source_plan_ref:
  next_day_plan_id: next_day_plan_2026_06_18_apex_template_layer
  execution_day: "2026-06-18"
  source_status: bootstrap_plan_generated
```

## Approval Gate

```yaml
approval_gate:
  approval_required: false
  approval_status: not_required_no_write_requested
  approval_scope: none
  explicit_operator_action_required: false
  approval_text_to_show_operator: "This is a review-only block list. No calendar write is requested."
```

## Workflow Blocks for Review

| Block ID | Flow | Title | Timing | Write intent | Approval status | Notes |
|---|---|---|---|---|---|---|
| calendar_block_F1_repo_foundation | F1 | APEX repo foundation review | unscheduled | review_only | not_required | Use if operator wants to time-block later. |
| calendar_block_F2_contracts | F2 | APEX contract boundary review | unscheduled | review_only | not_required | Use if operator wants to time-block later. |
| calendar_block_F3_templates | F3 | APEX template/example creation | unscheduled | review_only | not_required | Use if operator wants to time-block later. |
| calendar_block_F4_validation | F4 | APEX validation and handoff | unscheduled | review_only | not_required | Use if operator wants to time-block later. |

## Operator Review Flags

| Flag ID | Severity | Flag | Required action |
|---|---|---|---|
| CAL-ORF-001 | low | Calendar context was not supplied. | Keep review-only unless operator provides approval and timing. |
