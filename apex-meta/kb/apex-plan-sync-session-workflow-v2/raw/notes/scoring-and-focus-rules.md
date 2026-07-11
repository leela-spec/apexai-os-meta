# Scoring and Focus Rules

## purpose

This file defines deterministic scoring and focus-candidate rules for
`apex-sync`.

The scoring layer computes numeric read-side signals from existing task files.
It does not decide strategy, validate operator intent, rewrite priorities, or
author planning prose.

## H7_priority_score

H7 priority values are:

```yaml
priority:
  high: 3
  medium: 2
  low: 1
```

Rules:

- `high` maps to `3`.
- `medium` maps to `2`.
- `low` maps to `1`.
- Missing priority is treated as `medium`.
- Unsupported priority values are treated as `medium` for computation.
- Priority scoring does not mutate task frontmatter.

## H7_urgency_score

Urgency score is computed from `due_date`.

```yaml
urgency:
  due_date_days_until_due_or_999: true
```

Rules:

- If `due_date` is present and parseable as `YYYY-MM-DD`, urgency is the number
  of days between today and the due date.
- If due date is today, urgency is `0`.
- If due date is in the past, urgency is negative.
- If `due_date` is missing or malformed, urgency is `999`.
- Lower urgency values sort earlier.
- Urgency scoring does not mutate task frontmatter.

## dependency_satisfied_actionability

A task is actionable only when all conditions are true:

```yaml
actionable_task:
  status:
    allowed:
      - open
      - in-progress
  depends_on:
    all_targets_exist: true
    all_targets_done: true
  blocked_by:
    empty_or_cleared: true
```

Dependency rules:

- Canonical dependency field is `depends_on`.
- `dependencies` is not canonical.
- Every `depends_on` item is interpreted as an integer task id.
- Every dependency target must exist.
- Every dependency target must have status `done`.
- Missing dependency targets are flagged.
- Circular dependency risk is flagged.

## blocker_semantics

A task appears in blocker reporting when any condition is true:

- Status is `blocked`.
- `blocked_by` is non-empty.
- One or more `depends_on` targets exists but is not `done`.
- One or more `depends_on` targets is missing.

`blocked_by` semantics:

- Empty `blocked_by` means no explicit blocker reason is present.
- Status `blocked` with empty `blocked_by` is flagged as
  `blocked_without_reason`.
- Numeric `blocked_by` entries are treated as task ids and are clear only when
  those tasks are `done`.
- Non-numeric `blocked_by` entries are treated as blocker reasons and keep the
  task blocked for read-side actionability.

## stale_task_semantics

A task is stale when:

- status is not `done`;
- status is not `deferred`;
- it has a parseable `updated_date` or `created_date`;
- the age in days is greater than or equal to the stale threshold.

Timestamp fields are read in this order:

1. `updated_date`
2. `updated`
3. `updated_at`
4. `created_date`
5. `created`
6. `created_at`

Default stale threshold:

```yaml
stale_days_default: 14
```

Stale detection emits `stale_task_candidate` and never mutates task status.

## unlock_depth_policy

Unlock depth measures how many downstream tasks depend directly or indirectly
on a task.

Rules:

- Build reverse edges from `depends_on`.
- Count every reachable downstream task once.
- Ignore missing dependency targets for unlock-depth counting.
- Do not count the task itself.
- Use unlock depth only as a sorting signal.
- Do not rewrite dependencies based on unlock depth.

Example:

```yaml
tasks:
  1:
    unlocks:
      - 2
      - 3
  2:
    unlocks:
      - 4

unlock_depth:
  1: 3
  2: 1
  3: 0
  4: 0
```

## focus_candidate_sort_policy

Focus candidates are actionable tasks sorted by:

1. Priority score descending.
2. Urgency score ascending.
3. Unlock depth descending.
4. Task id ascending.

```yaml
focus_candidate_sort_policy:
  primary: priority_score_desc
  secondary: urgency_score_asc
  tertiary: unlock_depth_desc
  quaternary: id_asc
```

This is a deterministic ordering policy, not a planning recommendation.

## score_report_schema

`score_report` must include:

- `report_name`
- `generated_at`
- `dry_run`
- `root`
- `script_exit_code`
- `review_flags`
- `tasks`

Each scored task should include:

- `id`
- `title`
- `status`
- `priority`
- `priority_score`
- `due_date`
- `urgency_score`
- `depends_on`
- `blocked_by`
- `updated_date`
- `created_date`
- `epic_slug`
- `task_path`
- `unlock_depth`
- `reason`

## focus_candidate_report_schema

`focus_candidate_report` must include:

- `report_name`
- `generated_at`
- `dry_run`
- `root`
- `script_exit_code`
- `review_flags`
- `candidates`

Each focus candidate should include the same task fields as a scored task.

A candidate must satisfy the actionability policy before appearing in this
report.

## no_planning_recommendation_boundary

`apex-sync` may say which existing tasks are deterministic focus candidates.
It must not say what the operator should choose strategically.

Allowed:

- “These are the focus candidates sorted by deterministic policy.”
- “Task 4 is blocked by unsatisfied `depends_on`.”
- “Task 7 has urgency score `2`.”

Forbidden:

- “You should work on this because it is strategically best.”
- “The operator decision is validated.”
- “Tomorrow’s plan should be…”
- “The next session should focus on…”

Strategic interpretation belongs outside `apex-sync`.