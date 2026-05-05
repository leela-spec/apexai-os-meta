# Trace, State, and Tracking Templates

## Purpose

Reusable Alfred forms for Session Export correction, OpState delta candidates, and minimal process tracking.

## Boundary

Session Export remains trace. OpState changes remain delta candidates until accepted. Tracking remains minimal in Alfred v1 and excludes mood, energy, BP, XP, and full analytics unless later promoted.

## ALFRED-TPL-014 — Operator-required Session Export correction

Use when a Session Export contains an operator-required correction and the correction must not directly mutate OpState.

```md
## Session Export Correction

- **Session export ref:** `<path or id>`
- **Correction source:** operator | verifier | trace audit
- **Correction:** <what was wrong>
- **Corrected trace statement:** <replacement trace statement>
- **OpState impact:** none | candidate_delta_required
- **Delta candidate ref:** `<id or none>`
- **Hard flags:** []
- **Stop condition:** Do not mutate OpState until delta is accepted.
```

## Session Export correction event

Use when a correction event needs machine-readable trace.

```yaml
session_export_correction_event_v1:
  correction_id:
  source_session_export_id:
  corrected_at:
  corrected_by: operator | Alfred | Night | MetaOps
  field_path:
  old_value:
  corrected_value:
  reason:
  affects_opstate_delta_candidate: true | false
```

## ALFRED-TPL-015 — OpState Delta Candidate v1

Use when trace or tracking suggests a live operating-state update.

```yaml
opstate_delta_candidate_v1:
  delta_id: OPD-YYYYMMDD-001
  source_trace: <Session Export, board item, or tracking record>
  proposed_change: <state change>
  reason: <why this may need to change>
  current_state_claim: <current known state>
  target_state_claim: <proposed state>
  evidence:
    EVD: <1-100>
    source_status: fully_read | partially_read | provisional | mixed | unknown
  impact:
    IMP: <1-100>
  risk:
    RSK: <1-100>
    hard_flags: []
  readiness: ready | partial | missing_input | blocked | operator_decision_needed
  validator: meta_ops | meta_detective | operator
  acceptance_needed: true
  stop_condition: Do not apply until accepted.
```

## ALFRED-TPL-016 — Tracking Record v1

Use for minimal Alfred v1 process tracking.

```yaml
tracking_record_v1:
  record_id: TRK-YYYYMMDD-001
  source: daily_board | session_export | handoff_return | operator_note
  item_ref: <id or path>
  action_taken: <what happened>
  result: done | partial | skipped | blocked | deferred
  friction_note: <short note or none>
  follow_up_candidate: <none or candidate id>
  exclusions:
    mood_energy_tracking: excluded_in_v1
    bp_xp_tracking: excluded_in_v1
```

## Extended tracking record

Use only when a Daily Command Board / craft-flow result needs a richer process-learning trace.

```yaml
tracking_record_extended_v1:
  tracking_id:
  date:
  flow_id: CF1 | CF2 | CF3 | CF4
  lane:
  project_id:
  source_board_id:
  session_export_id:
  planned:
    objective:
    outputs: []
    time_window:
    craft_template:
  actual:
    flow_completion: complete | partial | missed | aborted
    sprints_completed:
    outputs: []
    blockers: []
    deviation_reason:
  process_learning:
    process_worked: yes | mixed | no | unknown
    chat_flow_efficiency: high | medium | low | unknown
  candidates:
    pattern_candidates: []
    chunk_candidates: []
    kb_candidates: []
```

## Invalid use

- Do not let Session Export mutate OpState directly.
- Do not copy full Session Export trace into OpState.
- Do not treat tracking as Stats or Algorithm computation.
- Do not add mood, energy, BP, or XP tracking to Alfred v1 without promotion.
