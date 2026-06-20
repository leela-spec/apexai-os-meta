# Epic Template

Use this template as proposed content for `apex-meta/epics/<slug>/epic.md`. This template is not a command to write the file.

```yaml
epic_record:
  slug: "<epic-slug>"
  title: "<epic-title>"
  status: open

  project_capture_record:
    goal: "<project goal>"
    scope:
      in_scope:
        - "<in-scope item>"
      out_of_scope:
        - "<out-of-scope item>"
    constraints:
      - "<constraint>"
    source:
      - "<operator note or context reference>"
    review_flags:
      - operator_review_needed

  planning_context:
    assumptions:
      - "<assumption>"
    unresolved_questions:
      - "<question>"
    risks:
      - "<risk>"

  proposed_task_records:
    path_pattern: "apex-meta/epics/<slug>/<id>.md"
    tasks:
      - id: 1
        title: "<first task title>"
        status: open
        priority: medium
        due_date: null
        depends_on: []
        blocked_by: []
        acceptance_criteria:
          - "<criterion>"
        definition_of_done:
          - "<done check>"
        notes:
          - "<planning note>"
        source:
          - "<source reference>"

  dependency_plan:
    proposed_depends_on_updates: []
    blocked_by_notes: []
    apex_sync_handoff_requests:
      - validate_dependencies

  priority_urgency_focus_rationale:
    priority_summary: "<qualitative priority rationale>"
    urgency_summary: "<qualitative urgency rationale>"
    provisional_focus_recommendation:
      focus_candidate_title: "<candidate>"
      rationale: "<rationale>"
      confidence: medium
      assumptions: []
      handoff_needed:
        - compute_focus_candidates

  operator_gate:
    status: operator_review_needed
    allowed_next_states:
      - approved_for_handoff
      - needs_revision
```