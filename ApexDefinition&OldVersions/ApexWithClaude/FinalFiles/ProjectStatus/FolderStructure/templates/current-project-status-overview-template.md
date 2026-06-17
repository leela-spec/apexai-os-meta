# Current Project Status Overview Template

```yaml
overview_metadata:
  artifact_name: current_project_status_overview
  schema_version: "0.1"
  created_or_updated_at: "YYYY-MM-DD"
  overview_status: operator_review_needed
  ranking_rule: manual_override_then_deadline_first_priority_second_urgency_third
  rating_format: "[priority/urgency/date]"
```

# Project Sections

```text
Leela
  - task-label: task-name [prio/urgency/date]
  --- subtask-label: subtask-name [prio/urgency/date]

Apex
  - task-label: task-name [prio/urgency/date]
  --- subtask-label: subtask-name [prio/urgency/date]

MasterOfArts
  - task-label: task-name [prio/urgency/date]
  --- subtask-label: subtask-name [prio/urgency/date]

Investment
  - task-label: task-name [prio/urgency/date]
  --- subtask-label: subtask-name [prio/urgency/date]

Others
  - task-label: task-name [prio/urgency/date]
  --- subtask-label: subtask-name [prio/urgency/date]
```

# Ranked Task View

```yaml
manual_override:
  pin: []
  promote: []
  demote: []
  freeze: []
```

```text
1. Project Name / task-label: task-name [prio/urgency/date]
2. Project Name / task-label: task-name [prio/urgency/date]
3. Project Name / task-label: task-name [prio/urgency/date]
4. Project Name / task-label: task-name [prio/urgency/date]
5. Project Name / task-label: task-name [prio/urgency/date]
```

# Unassigned

```yaml
unassigned_items: []
```

# Archive Optional

```yaml
optional_archive:
  enabled: false
  items: []
```

# Operator Validation

```yaml
operator_validation:
  status: operator_review_needed
  review_flags:
    uncertain_ratings: []
    invalid_ratings: []
    invalid_dates: []
    unresolved_unassigned_items: []
    possible_duplicates: []
    unclear_blockers: []
    ranking_conflicts: []
```
