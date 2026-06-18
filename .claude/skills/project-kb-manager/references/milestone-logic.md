# Milestone Logic

```yaml id="m8p2q4"
purpose:
  file_role: milestone_progression_rules
  schema_authority: references/project-schema.md
  rule_boundary: rules_only_no_field_type_definitions

activation_rules:
  - A milestone becomes active only after every referenced depends_on milestone is done.
  - If any depends_on milestone is not done, keep it out of active_milestone_ids.
  - Do not activate a milestone from implication, enthusiasm, or partial progress alone.

completion_rules:
  - Move a milestone to done only when definition_of_done is confirmed by the operator.
  - On status change to done, set operator_review_needed: true for validation.
  - Do not treat generated output, confidence, or inferred completion as operator confirmation.

cycle_guard:
  trigger: milestone_cycle_detected
  correction: >
    Halt the write, preserve the previous record, surface the dependency
    conflict, and ask the operator to remove or rewrite the circular depends_on
    relationship before changing milestone state.

precap_priority_signal:
  - PrecapNextDay reads active_milestone_ids from base_record, not the full milestone list.
  - Keep active_milestone_ids compact so project-state loading stays low-token.
  - Surface only active milestone next_action values needed for the next planning pass.

ordering_rules:
  - When multiple milestones are active, higher priority_weight surfaces first.
  - project_status_summary_for_precap should mention the highest-priority active milestone first.
  - When deadline is absent, order active milestones by priority_weight only.
  - When deadline is present, treat it as urgency signal without replacing operator priority.

non_goals:
  - Do not define milestone fields or allowed values.
  - Do not write project records from this rules file.
  - Do not override operator confirmation.
```