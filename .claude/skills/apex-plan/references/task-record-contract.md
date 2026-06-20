# Task Record Contract

```yaml
task_record_contract:
  file_role: canonical_task_record_contract
  package_name: apex-plan
  durable_home_pattern: "apex-meta/epics/<slug>/<id>.md"
  purpose: >
    Define the minimum valid task record proposed by Apex Plan. Apex Plan drafts
    task records for operator review; apex-session owns confirmed durable writes
    and status mutations.

  required_fields:
    - id
    - title
    - status
    - priority
    - due_date
    - depends_on
    - blocked_by
    - acceptance_criteria
    - definition_of_done
    - notes
    - source
```

## 1. Field Definitions

```yaml
field_definitions:
  id:
    type: integer
    required: true
    rule: "Use a positive integer unique within the epic folder."

  title:
    type: string
    required: true
    rule: "Use a concise human-readable task title."

  status:
    type: string
    required: true
    allowed:
      - open
      - in-progress
      - blocked
      - done
      - deferred
    default: open
    mutation_owner: apex-session

  priority:
    type: string
    required: true
    allowed:
      - high
      - medium
      - low
    default: medium
    rule: "Apex Plan may assign priority with rationale; exact ranking belongs to apex-sync."

  due_date:
    type: string_or_null
    required: true
    accepted:
      - "YYYY-MM-DD"
      - null
    rule: "Apex Plan records known due_date only; exact urgency scoring belongs to apex-sync."

  depends_on:
    type: integer_array
    required: true
    default: []
    rule: "All depended task ids must have status done before this task is actionable."
    validation_owner: apex-sync

  blocked_by:
    type: string_array
    required: true
    default: []
    rule: "Use for explicit blockers named by the source or operator; do not infer blockers silently."

  acceptance_criteria:
    type: string_array
    required: true
    default: []
    rule: "List observable conditions that must be true for the task to be accepted."

  definition_of_done:
    type: string_array
    required: true
    default: []
    rule: "List concrete completion checks for the task."

  notes:
    type: string_array
    required: true
    default: []
    rule: "Use for planning assumptions, uncertainty, and non-blocking context."

  source:
    type: string_array
    required: true
    default: []
    rule: "Reference operator notes, prior planning context, or supplied artifacts that justify the record."
```

## 2. Actionability Rule

```yaml
actionability_rule:
  stored_field: depends_on
  computed_state_owner: apex-sync
  rule: "A task is actionable only when every task id in depends_on resolves to a task with status done."
  apex_plan_limit: "Apex Plan may explain the rule and propose dependencies, but must not compute exact actionable task sets."
```

## 3. Review Flags

```yaml
review_flags:
  allowed_flags:
    - missing_source
    - unclear_scope
    - uncertain_priority
    - missing_due_date
    - dependency_uncertainty
    - circular_dependency_risk
    - possible_duplicate_task
    - blocked_by_unclear
    - operator_review_needed

  rules:
    - "Add missing_source when the task cannot be traced to supplied context."
    - "Add dependency_uncertainty when a depends_on relationship is plausible but not proven."
    - "Add circular_dependency_risk when direct mutual dependency appears in proposed records."
    - "Add operator_review_needed when a required field is defaulted because context is incomplete."
```

## 4. Mutation Boundary

```yaml
mutation_boundary:
  apex_plan:
    may_propose:
      - new_task_record
      - revised_task_record
      - dependency_plan
      - review_flags
    must_not_mutate:
      - status
      - durable_task_file
      - registry_index
      - session_handoff

  apex_session:
    owns:
      - operator_confirmed_write
      - status_mutation
      - entity_update
      - session_progress_log
```

## 5. Non-Goals

```yaml
non_goals:
  - "Do not compute the next actionable task."
  - "Do not update existing task status."
  - "Do not rebuild the registry index."
  - "Do not silently invent missing source evidence."
  - "Do not replace apex-sync dependency validation."
```