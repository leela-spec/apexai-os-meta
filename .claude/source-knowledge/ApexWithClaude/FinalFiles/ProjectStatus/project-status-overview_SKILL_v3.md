---
name: project-status-overview
description: >
  Use this skill when the operator asks to create, update, normalize, rank, or
  validate a compact cross-project project status overview. Accepts manual
  notes, project-specific summaries, previous overview text, or unassigned
  incoming items. Produces a project → task → subtask overview with
  [priority/urgency/date] ratings, ranked task view, temporary unassigned
  section, and operator review flags. Does not create weekly plans, next-day
  plans, status merges, project execution, workstreams, or detailed project
  databases.
---

# Project Status Overview

## Skill Contract

```yaml
skill_contract:
  primary_output: current_project_status_overview
  output_role: compact_cross_project_aggregator
  hierarchy:
    - project
    - task
    - subtask
  compact_format: |
    Project Name
      - task-label: task-name [prio/urgency/date]
      --- subtask-label: subtask-name [prio/urgency/date]

  default_projects:
    - Leela
    - Apex
    - MasterOfArts
    - Investment
    - Others

  rating_format:
    syntax: "[priority/urgency/date]"
    priority:
      type: integer
      min: 1
      max: 100
    urgency:
      type: integer
      min: 1
      max: 100
    date:
      type: string
      allowed: ["DD-MM", "NA"]

  ranking_order:
    - manual_override_if_present
    - deadline_first
    - priority_second
    - urgency_third

  boundaries:
    must_not_create:
      - workstreams
      - project_ids_in_human_output
      - heavy_task_ids
      - detailed_project_database
      - weekly_plan
      - next_day_plan
      - status_merge
      - project_execution
      - decision_registry
      - artifact_registry
```

## Supporting Files

```yaml
supporting_files:
  - path: references/project-status-overview-contract.md
    read_when:
      - operator_asks_for_contract
      - output_structure_is_unclear
      - validating_project_task_subtask_fields

  - path: templates/current-project-status-overview-template.md
    read_when:
      - operator_requests_blank_template
      - creating_first_empty_overview
      - output_format_needs_copy_paste_template

  - path: examples/starter-manual-test-overview.md
    read_when:
      - testing_skill_for_first_time
      - operator_requests_example
      - calibrating_initial_project_ratings

  - path: references/ranking-and-validation-rules.md
    read_when:
      - ranking_tasks
      - validating_rating_format
      - handling_manual_override
      - correcting_invalid_or_over_detailed_input

  - path: package-manifest.md
    read_when:
      - operator_inspects_package_structure
      - validating_package_files
```

## Procedure

1. **Load context.** Read the supplied manual notes, project summaries, previous overview text, or incoming unassigned items. If no usable context is supplied, use the failure mode `no_context`.

2. **Sort material.** Assign clearly project-specific material to the correct project. Put unresolved infos, tasks, or project candidates into `Unassigned`. Once an item is assigned to a project, remove it from `Unassigned`.

3. **Normalize shape.** Convert assigned material into project → task → subtask. Use compact labels only. Do not add workstreams, project IDs, heavy IDs, decision registries, artifact registries, or detailed project history.

4. **Apply ratings.** Preserve valid `[priority/urgency/date]` ratings. Estimate missing ratings only when source context supports it. Use `NA` when no real deadline is known. Mark estimated or uncertain ratings as `operator-review-needed`.

5. **Rank tasks.** Build a ranked task view. Manual override wins first. Otherwise rank by deadline pressure, then priority, then urgency. `NA` means no known fixed deadline; it does not mean low importance.

6. **Validate and present.** If any failure mode from the Failure Modes block is triggered, apply the correction before presenting the final output. Output the compact overview plus a short `Operator Validation` section containing only unresolved unassigned items, uncertain ratings, possible duplicates, unclear blockers, invalid dates, or ranking conflicts.

## Failure Modes

```yaml
failure_modes:
  no_context:
    trigger: "No project notes, prior overview, or incoming items supplied."
    correction: "Ask for source notes or offer the blank template."

  missing_metrics:
    trigger: "Task or subtask lacks [priority/urgency/date]."
    correction: "Estimate only if supported; otherwise mark operator-review-needed."

  invalid_rating:
    trigger: "Rating is not [number/number/DD-MM] or [number/number/NA], or priority/urgency is outside 1-100."
    correction: "Keep item, mark rating invalid, and request operator review."

  invalid_date:
    trigger: "Date is not DD-MM, NA, or is calendar-impossible."
    correction: "Use NA only if no reliable date exists; otherwise mark operator-review-needed."

  over_detailed_expansion:
    trigger: "Output expands into project database, workstream tree, artifact registry, decision log, or status-merge packet."
    correction: "Compress back to project → task → subtask and move detail into source_note only if needed."

  duplicate_unassigned_item:
    trigger: "Same item appears in a project and in Unassigned."
    correction: "Keep the assigned project item and remove the Unassigned duplicate unless assignment is uncertain."

  invented_blocker:
    trigger: "A blocker appears without source support."
    correction: "Remove blocker or mark blocker status operator-review-needed."

  ranking_conflict:
    trigger: "Manual override conflicts with automatic deadline-first ranking."
    correction: "Preserve manual override and flag the conflict for operator review."
```

## Output Requirements

```yaml
output_requirements:
  required_sections:
    - overview_metadata
    - project_sections
    - ranked_task_view
    - unassigned
    - operator_validation

  project_sections:
    format: compact_human_readable
    use_project_name_not_project_id: true

  ranked_task_view:
    include: true
    include_manual_override_status: true

  unassigned:
    include_only_when_unresolved_items_exist: true

  operator_validation:
    include_only_relevant_flags: true
    allowed_flags:
      - uncertain_ratings
      - invalid_ratings
      - invalid_dates
      - unresolved_unassigned_items
      - possible_duplicates
      - unclear_blockers
      - ranking_conflicts
```

## Completion Gate

The skill is complete only when the produced overview:

```yaml
completion_gate:
  hierarchy_is_project_task_subtask: true
  ratings_use_priority_urgency_date: true
  ranked_task_view_present: true
  manual_override_preserved: true
  unassigned_items_are_temporary: true
  blockers_only_when_present: true
  no_workstreams: true
  no_detailed_project_database: true
  no_weekly_or_next_day_plan: true
  operator_review_flags_present_when_needed: true
```
