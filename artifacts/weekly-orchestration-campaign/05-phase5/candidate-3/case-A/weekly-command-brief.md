# Weekly Command Brief — 2026-W36 (CANDIDATE-3 instantiation, Case A facts)

> **State:** READY | **Capacity:** STANDARD | **Changes vs W35:** 1
> **Next action:** APPROVE_WEEK
> **Decisions open:** provisional-vocabulary start for ACIM outline (bites THU)
> **Scope:** 3 projects; 2 outcomes

## Changed since last week

- ACIM moves from locked-content state to active outline work (lock completed W1) `[src: S1]`

## Weekly direction

**Intent:** Consolidate the W1 SSoT lock into stable canonical sets; open the ACIM workshop outline from locked content only. `[src: S1]`
**Success at week end:** Lika/ACIM indexes pass full validation walk; ACIM outline draft exists citing only canonical IDs.

## Priorities

| # | Project | Priority | Desired result | Depends on | Day emphasis |
| :-- | :-- | :-- | :-- | :-- | :-- |
| P1 | Lika | validation-walk | clean walk report, findings classified | — | MON lead, TUE parallel |
| P2 | ACIM | outline-skeleton | draft with canonical-ID citations | P1 | THU lead, FRI fallback |
| P3 | Apex | adr-hygiene | pointers resolve | — | WED single block |

Parked: Investment (standing), archives deletion (operator-reserved).

## Sequence and constraints

- P1 before P2 prose work (vocabulary dependency) — structured in handoff as depends_on.
- Parallel-safe: P3 alongside either lane.
- Capacity: standard four-block weekdays; personal fixed blocks protected. No constrained days this week.

## Review flags

### Provisional-vocabulary dependency
- Issue: outline may need rewrites when full glossary lands (W5).
- Operator action: approve provisional start OR hold until glossary.

## Sources ledger

| Tag | Source | Freshness |
| :-- | :-- | :-- |
| S1 | `apex-meta/orchestration/simulations/.../Week-01/weekly_plan.md` (historical input class per receipt) | STALE-CLASS |

All priorities trace to S1; no fact in this artifact lacks a tag.

## Compact downstream handoff

```yaml
presentation_handoff:
  schema_version: "candidate-3"
  artifact_type: "Weekly_Command_Brief"
  week: "2026-W36"
  result_state: READY
  capacity_class: STANDARD
  project_priorities:
    - {project_ref: lika, priority_id: P1-validation-walk, depends_on: null, day_emphasis: {MON: lead}}
    - {project_ref: acim, priority_id: P1-outline-skeleton, depends_on: P1-validation-walk, day_emphasis: {THU: lead}}
    - {project_ref: apex, priority_id: P3-adr-hygiene, depends_on: null, day_emphasis: {WED: single}}
  status_enum: [FULL, COMPRESSED, MINIMAL, OMITTED, BLOCKED]
  open_decisions: [{id: provisional-vocabulary, affects: acim, bite_day: THU}]
  next_consumer: "PreCap_Next_Day_Brief@candidate-3"
```
