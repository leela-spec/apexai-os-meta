# Starter Manual Test Overview

```yaml
overview_metadata:
  artifact_name: current_project_status_overview
  schema_version: "0.1"
  example_type: starter_manual_test
  created_or_updated_at: "YYYY-MM-DD"
  overview_status: operator_review_needed
  ranking_rule: manual_override_then_deadline_first_priority_second_urgency_third
  rating_format: "[priority/urgency/date]"
  rating_note: "Starter ratings are invented for test purposes and must be reviewed by the operator."
```

# Project Sections

```text
Apex
  - status-overview: define project status overview aggregation format and skill package [100/95/NA]
  --- output-docs: define output documents for the file system [95/80/NA]
  --- claude-automation: implement Claude-side automation after file logic is clear [85/60/NA]
  --- supplemental-layer: supplement later with external runtime support [65/35/NA]

Leela
  - spatial-system: spatial design system [95/75/NA]
  --- flutter-best-practices: research Flutter best practices for spatial design possibilities [80/55/NA]
  --- spatial-formalization: create and formalize spatial design aspects [88/65/NA]
  --- content-fill: fill Leela with content [75/50/NA]
  --- moa-overlap: preserve overlap with MasterOfArts content [70/45/NA]

MasterOfArts
  - website-skeleton: create first website skeleton content [88/70/NA]
  --- skeleton-meat: prepare representative content for website structure [84/68/NA]
  --- website-execution: execute actual website build after skeleton content is ready [76/55/NA]
  --- business-plan: develop business plan as priority basis for website and offer structure [82/62/NA]

Investment
  - paused-review: keep investment active but paused [55/20/NA]
  --- reactivation-check: review when investment should become active again [50/18/NA]

Others
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
1. Apex / status-overview: define project status overview aggregation format and skill package [100/95/NA]
2. Leela / spatial-system: spatial design system [95/75/NA]
3. Apex / output-docs: define output documents for the file system [95/80/NA]
4. MasterOfArts / website-skeleton: create first website skeleton content [88/70/NA]
5. Leela / spatial-formalization: create and formalize spatial design aspects [88/65/NA]
6. Apex / claude-automation: implement Claude-side automation after file logic is clear [85/60/NA]
7. MasterOfArts / skeleton-meat: prepare representative content for website structure [84/68/NA]
8. MasterOfArts / business-plan: develop business plan as priority basis for website and offer structure [82/62/NA]
9. Leela / flutter-best-practices: research Flutter best practices for spatial design possibilities [80/55/NA]
10. MasterOfArts / website-execution: execute actual website build after skeleton content is ready [76/55/NA]
11. Leela / content-fill: fill Leela with content [75/50/NA]
12. Leela / moa-overlap: preserve overlap with MasterOfArts content [70/45/NA]
13. Apex / supplemental-layer: supplement later with external runtime support [65/35/NA]
14. Investment / paused-review: keep investment active but paused [55/20/NA]
15. Investment / reactivation-check: review when investment should become active again [50/18/NA]
```

# Unassigned

```yaml
unassigned_items:
  - item_type: info
    item_label: starter-ratings
    item_name: "All ratings in this example are starter estimates for manual test purposes."
    rating: null
    assignment_status: unassigned
    review_note: "Operator should validate, edit, or replace all priority and urgency values."

  - item_type: task
    item_label: deadline-review
    item_name: "Check whether any current tasks have real deadlines."
    rating: "[70/50/NA]"
    assignment_status: unassigned
    review_note: "All dates are NA because no real deadline was supplied in the seed state."

  - item_type: task
    item_label: inbox-container
    item_name: "Hold unassigned infos, tasks, and project candidates until they can be assigned."
    rating: "[40/25/NA]"
    assignment_status: unassigned
    review_note: "Moved out of Others because unresolved incoming material belongs in Unassigned."

  - item_type: task
    item_label: assignment-review
    item_name: "Assign incoming items to a project when clear."
    rating: "[45/30/NA]"
    assignment_status: unassigned
    review_note: "Moved out of Others because assignment-review is part of the temporary unassigned policy."
```

# Operator Validation

```yaml
operator_validation:
  status: operator_review_needed
  review_flags:
    starter_ratings:
      status: true
      note: "All ratings were invented for first test-run calibration."
    deadline_review:
      status: true
      note: "No real deadlines supplied. Every deadline is NA."
    project_assignment_review:
      status: true
      note: "Confirm whether all starter tasks are assigned to the correct project."
    ranking_review:
      status: true
      note: "Because all deadlines are NA, current automatic ranking is effectively priority-first, then urgency."
    manual_override:
      status: empty
      note: "No pin, promote, demote, or freeze overrides supplied."
```

# First Manual Test Instruction

```yaml
first_manual_test:
  instruction:
    - "Run the skill using this starter manual test example."
    - "Ask it to produce a compact current project status overview."
    - "Check that output uses project → task → subtask."
    - "Check ranked task view."
    - "Check unassigned section."
    - "Check that no workstream layer appears."
  suggested_operator_prompt: >
    Use the project-status-overview skill with this starter manual test example.
    Produce a compact current_project_status_overview. Preserve project → task →
    subtask structure, use [priority/urgency/date], rank tasks deadline-first
    then priority then urgency, keep manual override empty, include unassigned
    items, and mark starter ratings as operator-review-needed.
```
