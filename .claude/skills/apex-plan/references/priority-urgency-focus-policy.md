# Priority, Urgency, and Focus Policy

```yaml
priority_urgency_focus_policy:
  file_role: qualitative_priority_urgency_focus_policy
  package_name: apex-plan
  purpose: >
    Define how Apex Plan records priority, due_date, urgency rationale, and
    provisional focus rationale without computing exact deterministic ranking.

  computation_boundary:
    apex_plan: "qualitative rationale and policy assignment only"
    apex_sync: "exact priority, urgency, unlock, and dependency-aware sorting"
```

## 1. Priority Policy

```yaml
priority_policy:
  field: priority
  allowed_values:
    high:
      weight: 3
      meaning: "Strategically important, high leverage, or required soon by operator intent."
    medium:
      weight: 2
      meaning: "Useful and relevant but not the top planning constraint."
    low:
      weight: 1
      meaning: "Valid work that can wait or depends on future context."

  apex_plan_rules:
    - "Assign high, medium, or low when source context supports it."
    - "Add a one-sentence priority rationale."
    - "Use medium when priority evidence is unclear."
    - "Add uncertain_priority to review_flags when priority is defaulted."

  apex_plan_must_not:
    - "Do not sort all tasks by priority weight."
    - "Do not compute exact priority score beyond the allowed value."
    - "Do not decide final next action from priority alone."
```

## 2. Urgency Policy

```yaml
urgency_policy:
  field: due_date
  stored_type: string_or_null
  accepted_values:
    - "YYYY-MM-DD"
    - null
  computation_owner: apex-sync

  apex_plan_rules:
    - "Record due_date only when the operator or source context provides a date."
    - "Use null when no real date is known."
    - "Explain urgency qualitatively in urgency_rationale."
    - "Add missing_due_date to review_flags when a task appears time-sensitive but no date is known."

  apex_plan_must_not:
    - "Do not calculate days until due_date."
    - "Do not assign numeric urgency score."
    - "Do not sort tasks by due_date."
    - "Do not treat null due_date as low priority."
```

## 3. Provisional Focus Recommendation

```yaml
focus_recommendation_policy:
  output_name: provisional_focus_recommendation
  apex_plan_role: "Draft qualitative focus rationale for operator review."
  apex_sync_role: "Compute exact focus candidates from status, dependencies, priority, due_date, blockers, and registry data."

  apex_plan_may_consider:
    - operator_goal
    - visible_task_scope
    - qualitative_priority
    - known_due_date
    - explicit_blockers
    - dependency_uncertainty
    - source_confidence

  required_fields:
    focus_candidate_title:
      type: string
    rationale:
      type: string
    confidence:
      type: string
      allowed:
        - high
        - medium
        - low
    assumptions:
      type: string_array
    handoff_needed:
      type: string_array
      allowed:
        - compute_focus_candidates
        - validate_dependencies
        - compute_next_action
        - scan_blockers

  apex_plan_must_not:
    - "Do not produce deterministic ranked task order."
    - "Do not claim a task is actionable unless apex-sync has validated dependencies."
    - "Do not compute unlock depth."
    - "Do not replace operator judgment."
```

## 4. Handoff Rules

```yaml
handoff_rules:
  to_apex_sync:
    exact_priority_urgency_unlock_sorting:
      trigger: "Operator asks for exact ranking, next action, or computed focus candidates."
    compute_focus_candidates:
      trigger: "Provisional focus rationale needs registry-wide validation."
    validate_dependencies:
      trigger: "Any depends_on relationship has uncertainty or circular dependency risk."
    scan_blockers:
      trigger: "Operator asks whether tasks are blocked across the system."

  to_apex_session:
    request_operator_confirmed_write:
      trigger: "Operator approves priority, due_date, or task-record changes for durable write."
    request_status_mutation:
      trigger: "Operator asks to change a task status after reviewing planning output."
```

## 5. Non-Goals

```yaml
non_goals:
  - "Do not compute exact urgency score."
  - "Do not compute exact next task."
  - "Do not traverse dependencies to determine actionability."
  - "Do not produce registry-wide focus ranking."
  - "Do not mutate task files."
```