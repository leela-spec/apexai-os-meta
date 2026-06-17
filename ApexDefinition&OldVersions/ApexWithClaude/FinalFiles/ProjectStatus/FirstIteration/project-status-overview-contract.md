# project-status-overview/references/project-status-overview-contract.md

```
# Project Status Overview Contract```yamlartifact_contract:  artifact_name: current_project_status_overview  purpose: compact_cross_project_status_aggregator  hierarchy:    - project    - task    - subtask  compact_output_format: |    Project Name      - task-label: task-name [prio/urgency/date]      --- subtask-label: subtask-name [prio/urgency/date]  required_sections:    - overview_metadata    - project_sections    - ranked_task_view    - unassigned_items    - validation_record  optional_sections:    - optional_archive  non_goals:    - no_detailed_project_database    - no_workstreams    - no_status_merge    - no_weekly_plan    - no_next_day_plan    - no_automatic_project_execution
```

## 1. Normalized Structure

```
current_project_status_overview:  overview_metadata:    schema_version: "0.1"    created_or_updated_at: "YYYY-MM-DD"    overview_status: "operator_review_needed | validated"    ranking_rule: "manual_override_then_deadline_first_priority_second_urgency_third"    rating_format: "[priority/urgency/date]"  project_sections:    - project_name: "Project Name"      tasks:        - task_label: "short-code-word"          task_name: "human-readable task name"          rating: "[priority/urgency/date]"          subtasks:            - subtask_label: "short-code-word"              subtask_name: "human-readable subtask name"              rating: "[priority/urgency/date]"              blocker: null          blocker: null          source_note: null  ranked_task_view:    - rank: 1      project_name: "Project Name"      task_label: "short-code-word"      task_name: "human-readable task name"      rating: "[priority/urgency/date]"      ranking_basis: "manual_override | deadline | priority | urgency"  unassigned_items:    - item_type: "info | task | project_candidate"      item_label: "short-code-word"      item_name: "human-readable incoming item"      rating: "[priority/urgency/date] | null"      assignment_status: "unassigned"      review_note: "why this is not assigned yet"  optional_archive:    enabled: false    items: []  validation_record:    status: "operator_review_needed | valid | invalid"    checks:      project_task_subtask_only: true      no_workstreams: true      no_project_ids_required: true      rating_format_valid: true      unassigned_policy_valid: true      archive_optional_only: true      no_detailed_project_database: true
```

## 2. Section Contracts

```
overview_metadata:  required: true  fields:    schema_version:      type: string      required: true      example: "0.1"    created_or_updated_at:      type: date      required: true      format: "YYYY-MM-DD"    overview_status:      type: enum      required: true      allowed_values:        - operator_review_needed        - validated    ranking_rule:      type: string      required: true      default: "manual_override_then_deadline_first_priority_second_urgency_third"    rating_format:      type: string      required: true      fixed_value: "[priority/urgency/date]"
```

```
project_sections:  required: true  rule: "Use project name, not project ID."  item_fields:    project_name:      type: string      required: true      examples:        - Leela        - Apex        - MasterOfArts        - Investment        - Others    tasks:      type: list      required: true      item_contract: task_contract
```

```
task_contract:  required_fields:    task_label:      type: string      required: true      purpose: "Compact code word for the task."    task_name:      type: string      required: true      purpose: "Human-readable task name."    rating:      type: string      required: true      format: "[priority/urgency/date]"  optional_fields:    subtasks:      type: list      required: false      item_contract: subtask_contract    blocker:      type: string_or_null      required: false      rule: "Include only when a real blocker exists."    source_note:      type: string_or_null      required: false      rule: "Use only when source context matters for operator review."
```

```
subtask_contract:  required_fields:    subtask_label:      type: string      required: true      purpose: "Compact code word for the subtask."    subtask_name:      type: string      required: true      purpose: "Human-readable subtask name."    rating:      type: string      required: true      format: "[priority/urgency/date]"  optional_fields:    blocker:      type: string_or_null      required: false      rule: "Include only when a real blocker exists."
```

```
ranked_task_view:  required: true  purpose: "Cross-project task ranking for planning visibility."  ranking_order:    - manual_override_if_supplied    - deadline_first    - priority_second    - urgency_third  item_fields:    rank:      type: integer      required: true    project_name:      type: string      required: true    task_label:      type: string      required: true    task_name:      type: string      required: true    rating:      type: string      required: true      format: "[priority/urgency/date]"    ranking_basis:      type: enum      required: true      allowed_values:        - manual_override        - deadline        - priority        - urgency        - operator_review_needed
```

```
unassigned_items:  required: true  purpose: "Temporary holding area for material not yet assigned to a project."  allowed_item_types:    - info    - task    - project_candidate  policy:    - "Use only for unresolved incoming material."    - "Remove item from unassigned once assigned to a project."    - "Do not duplicate an item in both unassigned_items and project_sections."    - "Do not treat unassigned_items as a permanent backlog."  item_fields:    item_type:      type: enum      required: true      allowed_values:        - info        - task        - project_candidate    item_label:      type: string      required: true    item_name:      type: string      required: true    rating:      type: string_or_null      required: false      format: "[priority/urgency/date]"    assignment_status:      type: enum      required: true      allowed_values:        - unassigned    review_note:      type: string      required: false
```

```
optional_archive:  required: false  purpose: "Optional lightweight place for completed, superseded, or intentionally retired items."  policy:    - "Archive is optional only."    - "Do not require archive for normal operation."    - "Do not turn archive into detailed historical database."
```

```
validation_record:  required: true  fields:    status:      type: enum      required: true      allowed_values:        - operator_review_needed        - valid        - invalid    checks:      type: object      required: true      required_checks:        project_task_subtask_only:          expected: true        no_workstreams:          expected: true        no_project_ids_required:          expected: true        rating_format_valid:          expected: true        unassigned_policy_valid:          expected: true        archive_optional_only:          expected: true        no_detailed_project_database:          expected: true
```

## 3. Rating Contract

```
rating_contract:  syntax: "[priority/urgency/date]"  examples:    - "[77/30/14-08]"    - "[95/80/NA]"  priority:    type: integer    minimum: 1    maximum: 100    meaning: "Strategic importance."  urgency:    type: integer    minimum: 1    maximum: 100    meaning: "Time pressure."  date:    type: string    allowed_formats:      - "DD-MM"      - "NA"    meaning: "Deadline if known. Use NA when no real deadline exists."  invalid_examples:    - "[high/low/NA]"    - "[101/50/NA]"    - "[80/0/NA]"    - "[80/50/2026-08-14]"
```

## 4. Human-Readable Output Contract

```
Project Name  - task-label: task-name [prio/urgency/date]  --- subtask-label: subtask-name [prio/urgency/date]
```

```
human_readable_output_rules:  project_line:    format: "Project Name"    project_id_allowed: false  task_line:    format: "  - task-label: task-name [prio/urgency/date]"    required: true  subtask_line:    format: "  --- subtask-label: subtask-name [prio/urgency/date]"    required: false  blocker_line:    format: "      blocker: blocker text"    required: false    rule: "Only include when present."  source_note_line:    format: "      source: source note"    required: false    rule: "Only include when useful for operator review."
```

## 5. Non-Goals

```
non_goals:  no_detailed_project_database:    rule: "Do not expand into full project-state history, decisions, artifacts, or detailed execution records."  no_workstreams:    rule: "Do not create a workstream layer between project and task."  no_status_merge:    rule: "Do not merge flow recap evidence into canonical status as a status-merge process."  no_weekly_plan:    rule: "Do not allocate work across a week."  no_next_day_plan:    rule: "Do not generate daily flows, prompt packets, or execution blocks."  no_automatic_project_execution:    rule: "Do not perform project work or trigger execution."
```

```
---# VALIDATION CHECKLIST- [ ] Exactly one file was produced.- [ ] Contract uses project → task → subtask.- [ ] No workstream layer exists.- [ ] No project IDs are required.- [ ] Rating format is defined.- [ ] Unassigned policy is defined.- [ ] Archive is optional only.
```