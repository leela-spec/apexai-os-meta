---
title: "Portfolio Project Capture Cursor — 2026-08-16"
document_role: next_session_gate_cursor
created: 2026-08-16
updated: 2026-08-16
status: apex_session_canonicalization_complete_sync_next
week: 2026-W34
---

# Portfolio Project Capture Cursor

## Current state

Apex Plan proposal work and operator review are complete. Apex Session canonicalization is complete for the approved W34 portfolio intake.

Canonical state now exists for nine newly approved epics and 54 tasks under `apex-meta/epics/`. The pre-existing NARM epic remains unchanged.

## Required restart reading order

1. `apex-meta/handoff/session-canonicalization-confirmation-20260816-w34.okf.md`
2. `apex-meta/handoff/planning-feed-20260816-w34.md`
3. `apex-meta/handoff/next-session.md`
4. canonical task records under `apex-meta/epics/`
5. `apex-meta/handoff/plan-packets/portfolio-project-capture-index-20260816-2026-W34.md` only when proposal/source history is needed

## Gate

```yaml
current_gate:
  from: Apex Session confirmed canonical project/task state
  to: Apex Sync deterministic validation
  operator_approval_required_now: false
  canonical_writes_done: true
  apex_sync_allowed: true
  project_status_allowed_after_sync: true
  precap_week_g1_allowed_now: false
```

## Exact next sequence

1. Read the current Apex Sync contract.
2. Run deterministic validation against canonical task files.
3. Persist dependency/next-action/blocker-staleness/focus/registry outputs.
4. Route proven structural corrections through the correct authority.
5. Generate `artifacts/weekly-plans/project-status-overview-20260816.md`.
6. Collect remaining W34-specific intent/calendar/capacity inputs.
7. Run PreCap Week G1 to `artifacts/weekly-plans/weekly_plan_packet-20260816-2026-W34.md`.
8. Stop at G1 operator approval.

## Do not do

- do not reconstruct canonical task state from chat memory;
- do not run Sync against proposal-only packets when canonical files now exist;
- do not silently resolve operator-decision blockers;
- do not duplicate existing Apex weekly-flow/PM initiatives;
- do not turn Dating into task records;
- do not run PreCap Week G1 before Sync, ProjectStatus, and W34 input readiness.
