# Daily Board Templates

## Purpose

Reusable Alfred Daily Command Board forms.

These templates support compact day-level command surfaces, board lock controls, CF1-CF4 craft-flow slots, and daily priority display.

## Boundary

The Daily Command Board is a compact Alfred-owned operating model. It is not a dashboard, not a calendar mutation surface, not downstream execution, and not a source of silent OpState or KB mutation.

## ALFRED-TPL-012 — Daily Command Board v1

Use when Alfred needs to present today's bounded command surface.

```md
## Daily Command Board

| Class | Item | Lane | Readiness | EVD | IMP | RSK | URG | Hard flags | Next action |
|---|---|---|---|---:|---:|---:|---:|---|---|
| P1 | <item> | <lane> | <readiness> | <1-100> | <1-100> | <1-100> | <1-100> | <flags> | <action> |

### Board controls

- **P0:** operator-confirmed or true stop-the-line only.
- **P1 cap:** maximum four normal-day craft-flow items.
- **Lock status:** draft | operator_locked | needs_revision.
- **Mutation rule:** after lock, add proposed deltas only.
```

## Daily Command Board compact fields

Use when a machine-readable compact board surface is needed.

```yaml
daily_command_board_compact_v1:
  board_id:
  date:
  source_window:
  operator_locked: false
  calendar_reality:
    hard_locks: []
    available_work_windows: []
    conflicts: []
  risks_and_repairs: []
  priority_stack: []
  craft_flows:
    CF1:
    CF2:
    CF3:
    CF4:
  deferred_or_not_today: []
  rhythm_profile_ref:
  tracking_seed:
```

## Board lock controls

```yaml
board_lock_controls_v1:
  lock_status: draft | operator_locked | needs_revision
  mutation_rule:
    before_lock: update_draft
    after_lock: preserve_locked_board_and_create_proposed_delta
  p0_rule: operator_confirmed_or_true_stop_the_line_only
  p1_normal_day_cap: 4
  silent_mutation_forbidden:
    - SSOT
    - OpState
    - calendar
    - canonical_KB
    - operator_locked_board
```

## Invalid use

- Do not use the board as a giant analytics dashboard.
- Do not auto-assign P0 because an item feels important.
- Do not assign more than four normal-day P1 craft-flow items.
- Do not mutate locked boards silently.
- Do not use board entries as direct OpState mutation.
