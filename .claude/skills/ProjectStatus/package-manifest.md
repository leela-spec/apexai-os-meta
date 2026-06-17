# Project Status Overview Package Manifest

```yaml
package_manifest:
  package_name: project-status-overview
  package_path: ".claude/skills/project-status-overview/"
  read_when: "operator_inspects_package_structure_or_validates_package_files"
  purpose: compact_cross_project_status_aggregator
  primary_artifact: current_project_status_overview

  file_list:
    - path: ".claude/skills/project-status-overview/SKILL.md"
      purpose: "Skill entrypoint, routing, compact procedure, boundaries, and completion gate."
      read_when: "skill invocation or entrypoint review"
      validation_role: "Confirms compact aggregator behavior and no planning/status-merge drift."
    - path: ".claude/skills/project-status-overview/references/project-status-overview-contract.md"
      purpose: "Artifact contract for current_project_status_overview."
      read_when: "contract structure or field validation is needed"
      validation_role: "Confirms project → task → subtask structure and unassigned policy."
    - path: ".claude/skills/project-status-overview/templates/current-project-status-overview-template.md"
      purpose: "Blank copy-paste overview template."
      read_when: "blank template or initial overview shell is requested"
      validation_role: "Confirms required output sections are available without embedding full schemas."
    - path: ".claude/skills/project-status-overview/examples/starter-manual-test-overview.md"
      purpose: "Filled starter example and first manual test instruction."
      read_when: "first manual test or example calibration is requested"
      validation_role: "Confirms realistic starter data, review flags, and no workstream layer."
    - path: ".claude/skills/project-status-overview/references/ranking-and-validation-rules.md"
      purpose: "Rating parser, ranking rule, validation checks, and failure modes."
      read_when: "ranking, rating validation, manual override, or failure correction is needed"
      validation_role: "Confirms deadline-first ranking, manual override, and compact correction behavior."
    - path: ".claude/skills/project-status-overview/package-manifest.md"
      purpose: "Lightweight package index and acceptance checklist."
      read_when: "operator inspects package structure or validates file inventory"
      validation_role: "Confirms all package files and package-level boundaries."

  package_boundaries:
    must_do:
      - create_compact_cross_project_overview
      - normalize_manual_notes_or_project_summaries
      - use_project_task_subtask_hierarchy
      - use_compact_rating_format
      - rank_tasks_for_cross_project_visibility
      - preserve_manual_override
      - keep_unassigned_items_temporary
      - surface_blockers_only_when_present
      - mark_uncertainty_for_operator_review
    must_not_do:
      - create_workstreams
      - create_detailed_project_database
      - create_weekly_plan
      - create_next_day_plan
      - perform_status_merge
      - execute_project_work
      - require_project_ids
      - require_heavy_chunk_ids
      - create_decision_registry
      - create_artifact_registry
      - create_patch_registry
      - invent_missing_project_state

  acceptance_checks:
    required_files_present: true
    hierarchy_is_project_task_subtask: true
    rating_format_is_priority_urgency_date: true
    ranking_is_deadline_first_priority_second_urgency_third: true
    manual_override_always_true: true
    unassigned_items_removed_when_assigned: true
    blockers_only_when_present: true
    no_workstreams: true
    no_project_id_requirement: true
    no_heavy_chunk_id_requirement: true
    no_detailed_project_database: true
    no_weekly_plan: true
    no_next_day_plan: true
    no_status_merge: true
```
