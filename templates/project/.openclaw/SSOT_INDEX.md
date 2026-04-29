---
class: frame
role: CANON
surface: ssot
quality: developing
scope: project
purpose: Map accepted project truth surfaces and their authority boundaries.
dependencies:
  - .openclaw/ProjCard.md
  - .openclaw/MetaAdoption.md
---

# SSOT Index

## Boundary

SSOT_INDEX maps accepted truth locations. It is not a substitute for the truth files it points to.

For a new project created from this template, mature project truth surfaces are not registered yet. Add truth surfaces only through the project promotion path and update this index when ownership is clear.

## truth_domains

| Domain | Truth owner surface | Status | Notes |
|---|---|---|---|
| `project_identity` | `.openclaw/ProjCard.md` as summary only | `developing` | ProjCard summarizes identity; promote durable project truth separately if needed. |
| `operational_state` | `.openclaw/OpState.md` | `state_only` | Live state, not accepted truth. |
| `meta_adoption` | `.openclaw/MetaAdoption.md` | `trace_record` | Records adopted meta release or commit. |
| `project_domain_truth` | `none_yet` | `unregistered` | Add after promotion creates or accepts a truth surface. |

## truth_files

| File | Domain or module | Authority status | Review cadence | Notes |
|---|---|---|---|---|
| `none_yet` | `TBD` | `unregistered` | `TBD` | No mature project truth file is declared by the empty template. |

## module_or_domain_scope

| Scope | Included | Excluded | Truth owner |
|---|---|---|---|
| `TBD` | `TBD` | `TBD` | `none_yet` |

## authority_notes

- Do not invent project truth during scaffold creation.
- Do not use OpState, Session Export, Night Report, or QA/Hygiene output as accepted truth by convenience.
- Every future truth owner must have a clear domain boundary.
- Every truth ownership change must be traceable through the promotion path.

## last_truth_review

| Field | Value |
|---|---|
| last_truth_reviewed_at | `none_yet` |
| reviewed_by | `TBD` |
| review_status | `initial_template_no_truth_registered` |
| next_review_trigger | `first project initialization or first truth promotion` |
