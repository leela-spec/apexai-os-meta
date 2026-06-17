# Project Status Overview Contract

```yaml
project_status_overview_contract:
  artifact_name: current_project_status_overview
  file_role: compact_cross_project_status_contract
  purpose: >
    Define the minimum valid structure for the compact Project Status Overview.
    This contract is a reference file, not a template, not a ranking engine, and
    not a detailed project database.

  hierarchy:
    allowed_levels:
      - project
      - task
      - subtask
    forbidden_levels:
      - workstream
      - project_id_layer
      - heavy_task_id_layer
      - decision_registry
      - artifact_registry
      - patch_registry

  compact_human_format: |
    Project Name
      - task-label: task-name [prio/urgency/date]
      --- subtask-label: subtask-name [prio/urgency/date]

  rating_contract:
    canonical_home: references/ranking-and-validation-rules.md
    visible_syntax: "[prio/urgency/date]"
    semantic_syntax: "[priority/urgency/date]"
    priority: "integer 1-100"
    urgency: "integer 1-100"
    date: "DD-MM or NA"

  initial_projects:
    - Leela
    - Apex
    - MasterOfArts
    - Investment
    - Others

  required_sections:
    overview_metadata:
      required: true
      fields:
        schema_version: "string"
        created_or_updated_at: "YYYY-MM-DD"
        overview_status: "operator_review_needed | validated"
        ranking_rule: "manual_override_then_deadline_first_priority_second_urgency_third"
        rating_format: "[priority/urgency/date]"

    project_sections:
      required: true
      rule: "Use project names in human-facing output; do not require project IDs."
      project_fields:
        project_name: "string"
        tasks: "list of task_contract"
      task_contract:
        task_label: "short compact label"
        task_name: "human-readable task name"
        rating: "[priority/urgency/date]"
        subtasks: "optional list of subtask_contract"
        blocker: "optional string; only when source context names a blocker"
        source_note: "optional short note; only when useful for operator review"
      subtask_contract:
        subtask_label: "short compact label"
        subtask_name: "human-readable subtask name"
        rating: "[priority/urgency/date]"
        blocker: "optional string; only when source context names a blocker"

    ranked_task_view:
      required: true
      ranking_source: references/ranking-and-validation-rules.md
      item_fields:
        rank: "integer"
        project_name: "string"
        task_label: "short compact label"
        task_name: "human-readable task name"
        rating: "[priority/urgency/date]"
        ranking_basis: "manual_override | deadline | priority | urgency | operator_review_needed"

    unassigned_items:
      required: "only when unresolved incoming material exists"
      purpose: "Temporary holding area for infos, tasks, or project candidates."
      policy:
        - "Use only for unresolved incoming material."
        - "Remove item from unassigned once assigned to a project."
        - "Do not duplicate an item in both unassigned_items and project_sections."
      item_fields:
        item_type: "info | task | project_candidate"
        item_label: "short compact label"
        item_name: "human-readable incoming item"
        rating: "[priority/urgency/date] | null"
        assignment_status: "unassigned"
        review_note: "optional reason assignment is unresolved"

    operator_validation:
      required: true
      include_only_relevant_flags: true
      allowed_flags:
        - uncertain_ratings
        - invalid_ratings
        - invalid_dates
        - unresolved_unassigned_items
        - possible_duplicates
        - unclear_blockers
        - ranking_conflicts

  optional_sections:
    optional_archive:
      required: false
      purpose: "Lightweight place for completed, superseded, or intentionally retired items."
      rule: "Do not turn archive into a historical project database."

  non_goals:
    - no_detailed_project_database
    - no_workstreams
    - no_project_ids_required_in_human_output
    - no_heavy_chunk_ids_required
    - no_status_merge
    - no_weekly_plan
    - no_next_day_plan
    - no_automatic_project_execution
    - no_decision_registry
    - no_artifact_registry
    - no_patch_registry

  validation_summary:
    must_pass:
      - hierarchy_is_project_task_subtask
      - every_task_and_subtask_has_valid_rating_or_review_flag
      - ranked_task_view_present
      - manual_override_preserved_when_supplied
      - unassigned_items_removed_when_assigned
      - blockers_only_when_present
      - archive_optional_only
      - no_workstreams
      - no_detailed_project_state_expansion
```
