# Ranking and Validation Rules

```yaml
rating_parser:
  syntax: "[priority/urgency/date]"
  valid_pattern:
    plain_text_description: "A bracketed triplet with two integers and one date-or-NA field."
    examples:
      - "[100/95/NA]"
      - "[77/30/14-08]"
      - "[1/1/NA]"
  fields:
    priority:
      position: 1
      type: integer
      minimum: 1
      maximum: 100
      meaning: strategic_importance
    urgency:
      position: 2
      type: integer
      minimum: 1
      maximum: 100
      meaning: time_pressure
    date:
      position: 3
      type: string
      allowed_values:
        - "DD-MM"
        - "NA"
      meaning: real_deadline_if_known
  invalid_examples:
    - "[high/low/NA]"
    - "[101/50/NA]"
    - "[80/0/NA]"
    - "[80/50/2026-08-14]"
    - "80/50/NA"
    - "[80/50]"

ranking_rule:
  name: manual_override_then_deadline_first_priority_second_urgency_third
  order:
    1: manual_override_or_pinned_order_if_present
    2: deadline_first
    3: priority_second
    4: urgency_third
  manual_override:
    beats_automatic_ranking: true
    allowed_actions:
      pin: "Force task into operator-defined top position."
      promote: "Move task higher than automatic ranking would place it."
      demote: "Move task lower than automatic ranking would place it."
      freeze: "Keep task in its current rank until operator changes it."
  automatic_ranking:
    applies_when: "No manual override affects the compared tasks."
    compare_sequence:
      - compare_deadline_pressure
      - compare_priority
      - compare_urgency
  tie_breaking:
    first: "higher priority"
    second: "higher urgency"
    third: "existing order in project section"
    fourth: "operator_review_needed"

deadline_pressure:
  purpose: "Convert the date field into ranking pressure without turning the overview into a calendar planner."
  reference_time_rule: "Apply deadline pressure relative to the date at skill execution time unless the operator supplies another reference date."
  assumptions:
    date_format: "DD-MM"
    active_year: "current planning year unless operator supplies another year"
    na_deadline: "No fixed date known."
  rules:
    overdue:
      pressure: highest
      ranking_effect: "Rises above future dated tasks unless manual override says otherwise."
    due_today:
      pressure: highest
      ranking_effect: "Rises near top unless manual override says otherwise."
    near_deadline:
      pressure: high
      suggested_window: "1-7 days"
      ranking_effect: "Real date beats NA when soon."
    medium_deadline:
      pressure: medium
      suggested_window: "8-30 days"
      ranking_effect: "Can outrank NA when priority is comparable."
    distant_deadline:
      pressure: low
      suggested_window: "more than 30 days"
      ranking_effect: "Deadline exists but should not dominate high-priority NA tasks automatically."
    no_deadline:
      value: "NA"
      pressure: none
      ranking_effect: "Does not mean unimportant."
  important_rule:
    - "A real soon date beats NA."
    - "Overdue or near-deadline tasks rise highest."
    - "NA means no known fixed deadline, not low priority."

validation_checks:
  rating_checks:
    every_task_has_rating:
      required: true
      rule: "Every task must include [priority/urgency/date]."
    every_subtask_has_rating:
      required: true
      rule: "Every subtask must include [priority/urgency/date]."
    rating_pattern_valid:
      required: true
      rule: "Every rating must match [number/number/date-or-NA]."
    priority_range_valid:
      required: true
      rule: "Priority must be an integer from 1 to 100."
    urgency_range_valid:
      required: true
      rule: "Urgency must be an integer from 1 to 100."
    date_valid:
      required: true
      rule: "Date must be DD-MM or NA."
  placement_checks:
    every_task_belongs_somewhere:
      required: true
      rule: "Every task must belong to a project or to unassigned."
    every_subtask_belongs_to_task:
      required: true
      rule: "Every subtask must sit under exactly one task."
    unassigned_removed_after_assignment:
      required: true
      rule: "Once an item is assigned to a project, remove it from unassigned."
    no_duplicate_after_assignment:
      required: true
      rule: "Do not keep the same item in unassigned and project sections."
  structure_checks:
    project_task_subtask_only:
      required: true
      rule: "Use only project, task, and subtask as structural layers."
    no_workstream_section:
      required: true
      rule: "Do not create a workstream section or workstream layer."
    no_project_ids_required:
      required: true
      rule: "Human-facing project sections use project name only."
    no_heavy_task_ids_required:
      required: true
      rule: "Use compact labels, not heavy ID systems."
    no_detailed_project_state_expansion:
      required: true
      rule: "Do not expand into detailed project history, full decision records, artifact registries, or execution logs."
  blocker_checks:
    blockers_only_when_present:
      required: true
      rule: "Blockers may appear only when the source context names a real blocker."
    no_invented_blockers:
      required: true
      rule: "Do not infer or invent blockers from vague uncertainty."
  ranking_checks:
    manual_override_preserved:
      required: true
      rule: "Pinned, promoted, demoted, or frozen tasks must keep operator override."
    deadline_first_applied:
      required: true
      rule: "When no manual override applies, deadline pressure is compared first."
    priority_second_applied:
      required: true
      rule: "After deadline pressure, compare priority."
    urgency_third_applied:
      required: true
      rule: "After priority, compare urgency."
    ranking_conflict_flagged:
      required: true
      rule: "If automatic ranking conflicts with manual override, preserve override and flag the conflict."

failure_modes:
  missing_metrics:
    trigger: "Task or subtask lacks a valid rating."
    correction: "Estimate only when supported by source context; otherwise mark operator-review-needed."
  invalid_date:
    trigger: "Date is not DD-MM, NA, or is calendar-impossible."
    correction: "Replace with NA only if no reliable date exists; otherwise mark operator-review-needed."
  unassigned_duplicate_after_assignment:
    trigger: "Same item appears in a project section and in unassigned."
    correction: "Keep the assigned project item and remove the unassigned duplicate unless assignment is uncertain."
  invented_blocker:
    trigger: "A blocker appears without source support."
    correction: "Remove blocker or mark blocker status operator-review-needed."
  workstream_layer_created:
    trigger: "A workstream heading or workstream-like layer appears."
    correction: "Remove workstream layer and compress its children into project tasks."
  over_detailed_project_expansion:
    trigger:
      - detailed_project_history_added
      - decision_registry_added
      - artifact_registry_added
      - execution_log_added
      - full_status_merge_behavior_added
    correction:
      - "Compress back to project → task → subtask."
      - "Move detailed material out of the overview or summarize as a task/subtask."
      - "Mark source context as too detailed if needed."
  ranking_conflict_between_deadline_and_manual_override:
    trigger:
      - manual_override_places_task_against_deadline_first_order
      - pinned_task_has_lower_deadline_pressure_than_auto_top_task
    correction:
      - "Preserve operator override."
      - "Flag ranking_conflict for operator review."
      - "Do not silently reorder overridden tasks."
```
