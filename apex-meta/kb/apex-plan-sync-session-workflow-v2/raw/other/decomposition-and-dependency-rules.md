# Decomposition and Dependency Rules

```yaml
decomposition_and_dependency_rules:
  file_role: decomposition_and_dependency_proposal_policy
  package_name: apex-plan
  purpose: >
    Define how Apex Plan decomposes project context into proposed task records
    and proposes dependency relationships without performing deterministic graph
    traversal or exact next-task computation.

  canonical_task_contract: "references/task-record-contract.md"

  dependency_field:
    name: depends_on
    type: integer_array
    rule: "All depended task ids must have status done before the task is actionable."

  validation_owner: apex-sync
```

## 1. Decomposition Rules

```yaml
decomposition_rules:
  grain:
    epic:
      purpose: "Project-level work container under apex-meta/epics/<slug>/."
      use_when: "The source describes a goal larger than one task."
    task:
      purpose: "Single actionable unit with acceptance criteria and definition of done."
      use_when: "The work can be reviewed as one discrete planning item."

  task_split_rules:
    - "Split tasks when acceptance criteria describe independent outcomes."
    - "Split tasks when one part must be completed before another can start."
    - "Keep tasks together when separation would create artificial bookkeeping without a real planning benefit."
    - "Use notes for unresolved details instead of inventing additional task layers."

  allowed_hierarchy:
    - epic
    - task

  forbidden_hierarchy:
    - workstream
    - nested_task_graph
    - registry_layer
    - execution_log_layer
```

## 2. Dependency Proposal Rules

```yaml
dependency_rules:
  use_depends_on_when:
    - "A task cannot start until another proposed task is complete."
    - "A task requires an artifact or decision produced by another task."
    - "The operator explicitly states a prerequisite relationship."

  do_not_use_depends_on_when:
    - "The relationship is only thematic."
    - "The order is a preference rather than a prerequisite."
    - "The task is blocked by an external person, missing input, or environment condition."

  use_blocked_by_when:
    - "The source names an external blocker."
    - "A missing decision or missing resource prevents progress."
    - "The task is blocked but no internal task id is the prerequisite."

  proposal_limit:
    apex_plan_may_propose_depends_on: true
    apex_plan_must_not_validate_full_graph: true
    apex_plan_must_not_compute_actionability: true
```

## 3. Circular Dependency Risk

```yaml
circular_dependency_risk_policy:
  apex_plan_detection_scope: obvious_direct_risk_only
  flag_when:
    - "Task A depends_on Task B and Task B depends_on Task A in the same proposal."
    - "A proposed chain is described in source notes as mutually blocking."
    - "A task appears to require its own output as an input."

  correction:
    - "Keep the task records."
    - "Add circular_dependency_risk to review_flags."
    - "Create a handoff request to apex-sync for dependency validation."

  non_scope:
    - "Do not traverse the full dependency graph."
    - "Do not compute transitive closure."
    - "Do not rewrite dependency edges automatically."
```

## 4. Dependency Plan Schema

```yaml
dependency_plan_schema:
  fields:
    proposed_depends_on_updates:
      type: object_array
      item_fields:
        task_id:
          type: integer
        depends_on:
          type: integer_array
        rationale:
          type: string
        confidence:
          type: string
          allowed:
            - high
            - medium
            - low
        review_flags:
          type: string_array

    blocked_by_notes:
      type: object_array
      item_fields:
        task_id:
          type: integer
        blocked_by:
          type: string_array
        source:
          type: string_array

    apex_sync_handoff_requests:
      type: string_array
      allowed:
        - validate_dependencies
        - compute_next_action
        - scan_blockers
        - compute_focus_candidates
```

## 5. Non-Goals

```yaml
non_goals:
  - "Do not compute exact next action."
  - "Do not scan all blockers."
  - "Do not validate the full dependency graph."
  - "Do not compute unlock depth."
  - "Do not rewrite durable task records."
  - "Do not call Python, Bash, or shell scripts."
```