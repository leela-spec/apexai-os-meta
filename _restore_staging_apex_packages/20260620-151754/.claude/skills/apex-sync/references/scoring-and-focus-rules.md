# Scoring and Focus Rules

```yaml
scoring_and_focus_rules:
  canonical_source: ".claude/skills/apex-sync/references/scoring-and-focus-rules.md"

  priority_score_policy:
    field: priority
    type: enum
    allowed:
      - high
      - medium
      - low
    values:
      high: 3
      medium: 2
      low: 1
    invalid_priority_behavior: "Use medium for score computation and keep the original task visible in reports."

  urgency_score_policy:
    field: due_date
    type: string
    accepted_format: "YYYY-MM-DD"
    computation: days_until_due_or_999
    no_due_date_score: 999
    invalid_due_date_score: 999
    lower_is_more_urgent: true
    examples:
      - due_date: "2026-06-20"
        today: "2026-06-19"
        urgency_score: 1
      - due_date: null
        today: "2026-06-19"
        urgency_score: 999

  unlock_depth_policy:
    source_field: depends_on
    graph_direction: "Task A unlocks Task B when Task B depends_on includes A."
    computation: "Count unique downstream unfinished task ids reachable through reverse depends_on traversal."
    type: integer
    min: 0
    cycle_behavior: "Report circular_dependency_risk and count each reachable task id only once."

  focus_candidate_sort_policy:
    candidate_filter:
      status_allowed:
        - open
        - in-progress
      depends_on_rule: "All ids in depends_on must resolve to tasks with status done."
      blocked_by_rule: "blocked_by must be empty or contain only ids whose status is done."
      excluded_status:
        - blocked
        - done
        - deferred
    sort_order:
      - field: priority_score
        direction: descending
      - field: urgency_score
        direction: ascending
      - field: unlock_depth
        direction: descending
      - field: id
        direction: ascending
    output: focus_candidate_report

  next_action_policy:
    output: next_action_report
    relation_to_focus: "next_action_report uses the same eligible candidate filter and ordering substrate as focus_candidate_report."
    explanation_limit: "Use only short machine-readable reason strings."
    
## Scoring Notes

`priority_score`, `urgency_score`, and `unlock_depth` are exact computations over current task files. `apex-sync` does not decide strategic importance; it only applies the accepted numeric policy to the existing `priority`, `due_date`, and `depends_on` fields.

Focus candidates are ordered task records, not a planning recommendation. Any narrative recommendation or operator-facing rationale belongs to `apex-plan`.
