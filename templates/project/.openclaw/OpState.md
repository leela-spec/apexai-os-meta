---
class: trace
role: HANDOVER
surface: opstate
quality: developing
scope: project
purpose: Live project operational state for bounded routing, handoff, and next-session planning.
dependencies:
  - .openclaw/ProjCard.md
  - .openclaw/SSOT_INDEX.md
  - .openclaw/SigMat.md
---

# Operational State

## Boundary

OpState is the live project control surface. It records current execution state and next actions, but it is not a truth surface and must not silently redefine accepted truth.

## active

| Item | Owner or surface | Lane | Trace reference | Notes |
|---|---|---|---|---|
| `TBD` | `TBD` | `progress` or `hygiene` | `TBD` | `TBD` |

## blocked

| Item | Blocker | Required disposition | Reference |
|---|---|---|---|
| `TBD` | `TBD` | `TBD` | `TBD` |

## next

| Item | Lane | Expected output | Ready state | Reference |
|---|---|---|---|---|
| `TBD` | `progress` or `hygiene` | `TBD` | `not_ready` | `TBD` |

## holds

| Hold ID | Hold state | Trigger | Clears when | Reference |
|---|---|---|---|---|
| `TBD` | `none` | `TBD` | `TBD` | `TBD` |

## recent_changes

| Date | Change | Source trace | State impact |
|---|---|---|---|
| `TBD` | `Initial template state` | `TBD` | `Project not active until initialized` |

## pending_recommendations

| Recommendation | Source | Target surface | Status | Notes |
|---|---|---|---|---|
| `TBD` | `TBD` | `TBD` | `pending_review` | `TBD` |

## night_ready

Night work is selected only from approved, merged, bounded items in this section. Unmerged day work does not authorize night execution.

| Queue ID | Task | Lane | Risk level | Approval reference | Expected output |
|---|---|---|---|---|---|
| `TBD` | `TBD` | `progress` or `hygiene` | `low` | `TBD` | `TBD` |

## last_session_export

| Field | Value |
|---|---|
| latest_session_export | `none_yet` |
| latest_session_export_date | `TBD` |
| operative_delta_applied | `no` |

## open_escalations

| Escalation ID | Level | Hold state | Required disposition | Reference |
|---|---|---|---|---|
| `TBD` | `none` | `none` | `TBD` | `TBD` |

## Update rules

- Update OpState from trace-backed session exports, explicit reviews, or bounded night recommendations.
- Do not treat pending recommendations as already accepted state.
- Do not treat OpState as SSOT.
- Keep `night_ready` minimal, merged, and review-gated.
