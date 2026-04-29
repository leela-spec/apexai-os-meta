---
class: trace
role: AUDIT
surface: qa_report
quality: developing
scope: project
purpose: Compact signal matrix for evidence strength, impact, risk, confidence, disagreement, and recommended action.
dependencies:
  - .openclaw/ProjCard.md
  - .openclaw/OpState.md
  - .openclaw/SSOT_INDEX.md
---

# Signal Matrix

## Boundary

SigMat is a compact signal surface. It supports review, prioritization, QA, and routing, but it is not a reasoning substitute and not a truth surface.

Signals without references are invalid.

## Schema

| Field | Meaning | Allowed template value |
|---|---|---|
| `item_id` | Stable local identifier for the tracked signal item | `SIG-000` |
| `impact` | Expected effect on project progress, governance, quality, or risk | `low`, `medium`, `high`, `critical`, or `TBD` |
| `evidence_strength` | Strength of referenced evidence | `none`, `weak`, `moderate`, `strong`, or `TBD` |
| `risk` | Risk if the item is acted on or ignored | `low`, `medium`, `high`, `critical`, or `TBD` |
| `confidence` | Confidence in the signal assessment | `low`, `medium`, `high`, or `TBD` |
| `disagreement` | Known disagreement or unresolved uncertainty | `none`, `present`, `unresolved`, or `TBD` |
| `recommended_action` | Bounded next action | `monitor`, `verify`, `escalate`, `promote_candidate`, `defer`, or `TBD` |
| `reason_refs` | References supporting the signal | path, PR, session export, QA note, or `none_yet` |

## Signal items

| item_id | impact | evidence_strength | risk | confidence | disagreement | recommended_action | reason_refs |
|---|---|---|---|---|---|---|---|
| `SIG-000` | `TBD` | `none` | `TBD` | `low` | `TBD` | `verify` | `none_yet` |

## Use rules

- Every non-placeholder item must have `reason_refs`.
- Do not use unsupported scores.
- Do not treat a signal item as accepted truth.
- If a signal implies a truth change, create or reference a promotion candidate instead of mutating SSOT directly.
- If a signal implies a hold or escalation, surface it through the governed escalation path.
