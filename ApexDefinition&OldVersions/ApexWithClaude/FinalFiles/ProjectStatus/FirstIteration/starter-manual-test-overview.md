# .claude/skills/project-status-overview/examples/starter-manual-test-overview.md

```
# Starter Manual Test Overview```yamloverview_metadata:  artifact_name: current_project_status_overview  schema_version: "0.1"  example_type: starter_manual_test  created_or_updated_at: "YYYY-MM-DD"  overview_status: operator_review_needed  ranking_rule: manual_override_then_deadline_first_priority_second_urgency_third  rating_format: "[priority/urgency/date]"  rating_note: "Starter ratings are invented for test purposes and must be reviewed by the operator."
```

# Project Sections

## Apex

```
Apex  - status-overview: define project status overview aggregation format and skill package [100/95/NA]  --- output-docs: define output documents for the file system [95/80/NA]  --- claude-automation: implement Claude-side automation after file logic is clear [85/60/NA]  --- supplemental-layer: supplement later with external runtime support [65/35/NA]
```

## Leela

```
Leela  - spatial-system: spatial design system [95/75/NA]  --- flutter-best-practices: research Flutter best practices for spatial design possibilities [80/55/NA]  --- spatial-formalization: create and formalize spatial design aspects [88/65/NA]  --- content-fill: fill Leela with content [75/50/NA]  --- moa-overlap: preserve overlap with MasterOfArts content [70/45/NA]
```

## MasterOfArts

```
MasterOfArts  - website-skeleton: create first website skeleton content [88/70/NA]  --- skeleton-meat: prepare representative content for website structure [84/68/NA]  --- website-execution: execute actual website build after skeleton content is ready [76/55/NA]  --- business-plan: develop business plan as priority basis for website and offer structure [82/62/NA]
```

## Investment

```
Investment  - paused-review: keep investment active but paused [55/20/NA]  --- reactivation-check: review when investment should become active again [50/18/NA]
```

## Others

```
Others  - inbox-container: hold unassigned infos, tasks, and project candidates [40/25/NA]  --- assignment-review: assign incoming items to a project when clear [45/30/NA]
```

# Ranked Task View

```
manual_override:  pinned: []  promoted: []  demoted: []  frozen: []
```

```
1. Apex / status-overview: define project status overview aggregation format and skill package [100/95/NA]2. Leela / spatial-system: spatial design system [95/75/NA]3. Apex / output-docs: define output documents for the file system [95/80/NA]4. MasterOfArts / website-skeleton: create first website skeleton content [88/70/NA]5. Leela / spatial-formalization: create and formalize spatial design aspects [88/65/NA]6. Apex / claude-automation: implement Claude-side automation after file logic is clear [85/60/NA]7. MasterOfArts / skeleton-meat: prepare representative content for website structure [84/68/NA]8. MasterOfArts / business-plan: develop business plan as priority basis for website and offer structure [82/62/NA]9. Leela / flutter-best-practices: research Flutter best practices for spatial design possibilities [80/55/NA]10. MasterOfArts / website-execution: execute actual website build after skeleton content is ready [76/55/NA]11. Leela / content-fill: fill Leela with content [75/50/NA]12. Leela / moa-overlap: preserve overlap with MasterOfArts content [70/45/NA]13. Apex / supplemental-layer: supplement later with external runtime support [65/35/NA]14. Investment / paused-review: keep investment active but paused [55/20/NA]15. Investment / reactivation-check: review when investment should become active again [50/18/NA]16. Others / assignment-review: assign incoming items to a project when clear [45/30/NA]17. Others / inbox-container: hold unassigned infos, tasks, and project candidates [40/25/NA]
```

# Unassigned

```
unassigned_items:  - item_type: info    item_label: starter-ratings    item_name: "All ratings in this example are starter estimates for manual test purposes."    rating: null    assignment_status: unassigned    review_note: "Operator should validate, edit, or replace all priority and urgency values."  - item_type: task    item_label: deadline-review    item_name: "Check whether any current tasks have real deadlines."    rating: "[70/50/NA]"    assignment_status: unassigned    review_note: "All dates are NA because no real deadline was supplied in the seed state."
```

# Operator Review Needed

```
operator_review_needed:  starter_ratings:    status: true    note: "All ratings were invented for first test-run calibration."  deadline_review:    status: true    note: "No real deadlines supplied. Every deadline is NA."  project_assignment_review:    status: true    note: "Confirm whether all starter tasks are assigned to the correct project."  ranking_review:    status: true    note: "Because all deadlines are NA, current automatic ranking is effectively priority-first, then urgency."  manual_override:    status: empty    note: "No pinned, promoted, demoted, or frozen tasks supplied."
```

# Validation Record

```
validation_record:  status: operator_review_needed  checks:    uses_all_five_initial_projects: true    project_task_subtask_only: true    no_workstreams: true    no_project_ids_required: true    no_heavy_task_ids_required: true    rating_format_valid: true    deadlines_use_NA_unless_known: true    ranked_task_view_present: true    manual_override_field_empty: true    unassigned_section_present: true    detailed_project_database_created: false
```

```
---# VALIDATION CHECKLIST- [ ] Exactly one file was produced.- [ ] Example uses all five initial projects.- [ ] Example uses `[prio/urgency/date]`.- [ ] Example has ranked task view.- [ ] Example marks starter ratings as review-needed.- [ ] Example does not use workstreams.
```