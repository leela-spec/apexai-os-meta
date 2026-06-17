# .claude/skills/project-status-overview/templates/current-project-status-overview-template.md

```
# Current Project Status Overview Template```yamloverview_metadata:  artifact_name: current_project_status_overview  schema_version: "0.1"  created_or_updated_at: "YYYY-MM-DD"  overview_status: operator_review_needed  ranking_rule: manual_override_then_deadline_first_priority_second_urgency_third  rating_format: "[priority/urgency/date]"
```

# Project Sections

## Leela

```
Leela  - task-label: task-name [prio/urgency/date]  --- subtask-label: subtask-name [prio/urgency/date]
```

## Apex

```
Apex  - task-label: task-name [prio/urgency/date]  --- subtask-label: subtask-name [prio/urgency/date]
```

## MasterOfArts

```
MasterOfArts  - task-label: task-name [prio/urgency/date]  --- subtask-label: subtask-name [prio/urgency/date]
```

## Investment

```
Investment  - task-label: task-name [prio/urgency/date]  --- subtask-label: subtask-name [prio/urgency/date]
```

## Others

```
Others  - task-label: task-name [prio/urgency/date]  --- subtask-label: subtask-name [prio/urgency/date]
```

# Ranked Task View

```
1. Project Name / task-label: task-name [prio/urgency/date]2. Project Name / task-label: task-name [prio/urgency/date]3. Project Name / task-label: task-name [prio/urgency/date]4. Project Name / task-label: task-name [prio/urgency/date]5. Project Name / task-label: task-name [prio/urgency/date]
```

```
ranking_notes:  manual_override:    pinned: []    promoted: []    demoted: []    frozen: []  operator_review_needed: []
```

# Unassigned

```
unassigned_items:  - item_type: "info | task | project_candidate"    item_label: "short-label"    item_name: "unassigned item name"    rating: "[prio/urgency/date] | null"    review_note: "why this is not assigned yet"
```

# Archive Optional

```
optional_archive:  enabled: false  items:    - archived_label: "short-label"      archived_name: "archived item name"      previous_project: "Project Name | unknown"      archive_reason: "completed | superseded | intentionally_retired"      archived_at: "YYYY-MM-DD"
```

# Operator Validation

```
operator_validation:  status: operator_review_needed  review_needed:    uncertain_ratings: []    unresolved_unassigned_items: []    possible_duplicates: []    blocker_checks: []    ranking_conflicts: []  checks:    project_task_subtask_only: true    no_workstreams: true    no_project_ids_required: true    rating_format_valid: true    unassigned_policy_valid: true    archive_optional_only: true    no_detailed_project_database: true
```

```
---# VALIDATION CHECKLIST- [ ] Exactly one file was produced.- [ ] Template contains Leela, Apex, MasterOfArts, Investment, Others.- [ ] Template uses compact task/subtask syntax.- [ ] Template includes ranked task view.- [ ] Template includes unassigned section.- [ ] Archive is optional.
```