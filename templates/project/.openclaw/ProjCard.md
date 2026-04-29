---
class: frame
role: ORCHESTRATION
surface: projcard
quality: developing
scope: project
purpose: Compact project-facing routing summary for the ApexAI_OS operating spine.
dependencies:
  - .openclaw/OpState.md
  - .openclaw/SSOT_INDEX.md
  - .openclaw/SigMat.md
  - .openclaw/MetaAdoption.md
---

# Project Card

## Boundary

ProjCard is a compact routing summary. It helps the meta layer understand the project as a controllable unit, but it is not a truth surface and must not replace `SSOT_INDEX.md`.

## Project identity

| Field | Value |
|---|---|
| `project_id` | `TBD` |
| `project_name` | `TBD` |
| `root_path` | `TBD` |
| `project_purpose` | `TBD` |
| `owning_project_repo` | `TBD` |

## Current priority and state

| Field | Value |
|---|---|
| `current_priority` | `TBD` |
| `current_operating_state` | `initializing` |
| `current_lane` | `progress` or `hygiene` |
| `last_reviewed` | `TBD` |

## Top blockers

| Blocker | Impact | Required disposition | Reference |
|---|---|---|---|
| `TBD` | `TBD` | `TBD` | `TBD` |

## Next session targets

| Target | Lane | Expected output | Reference |
|---|---|---|---|
| `TBD` | `progress` or `hygiene` | `TBD` | `TBD` |

## Control pointers

| Surface | Path | Status |
|---|---|---|
| OpState | `.openclaw/OpState.md` | required |
| SSOT index | `.openclaw/SSOT_INDEX.md` | required |
| Signal matrix | `.openclaw/SigMat.md` | required |
| Meta adoption record | `.openclaw/MetaAdoption.md` | required |
| Latest session export | `.openclaw/SessionExports/` | recommended once sessions exist |
| Latest QA/Hygiene | `.openclaw/QA/` | recommended once QA exists |
| Latest night report | `.openclaw/NightReports/` | recommended once night cycles exist |
| Local overlay | `user/AGENTS.md` or `none` | optional; may tighten only |

## Authority notes

- `ProjCard.md` summarizes state and routing; it does not create accepted truth.
- Accepted project truth is discovered through `SSOT_INDEX.md`.
- Live project state is tracked in `OpState.md` and must remain trace-backed.
- Meta releases move into this project only through reviewable adoption PRs.
- Project learnings move upward only as sanitized learning candidates.
