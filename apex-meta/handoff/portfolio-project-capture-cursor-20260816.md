---
title: "Portfolio Project Capture Cursor — 2026-08-16"
document_role: next_session_gate_cursor
created: 2026-08-16
updated: 2026-08-16
status: apex_sync_execution_pending_local_executor
week: 2026-W34
---

# Portfolio Project Capture Cursor

## Current state

Apex Plan proposal work, operator review, and Apex Session canonicalization are complete. Nine new epics and 54 tasks are canonical under `apex-meta/epics/`.

Apex Sync is the next authority. The browser runtime cannot execute the deterministic Sync script because the exact repository is not locally checked out and `gh` is unavailable. Per the Apex Sync contract, a local-execution packet has been persisted instead of estimating results.

## Required restart reading order

1. `apex-meta/handoff/apex-sync-local-execution-packet-20260816-w34.okf.md`
2. committed files under `apex-meta/handoff/sync-reports/20260816-w34/` once present
3. `apex-meta/handoff/planning-feed-20260816-w34.md`
4. canonical task records under `apex-meta/epics/`

## Gate

```yaml
current_gate:
  from: Apex Session confirmed canonical state
  to: Apex Sync deterministic validation complete
  blocker_type: execution_environment
  operator_decision_required: false
  required_action: run persisted local executor packet in repository checkout
  precap_week_g1_allowed_now: false
```

## Exact next sequence

1. Run all six dry-run Sync commands from the persisted local-execution packet.
2. Commit/push generated JSON reports to main.
3. Read and validate the committed reports.
4. Route any proven structural corrections through Plan/Session.
5. Generate `artifacts/weekly-plans/project-status-overview-20260816.md`.
6. Collect W34-specific intent/calendar/capacity inputs.
7. Run PreCap Week G1 and stop at G1 operator gate.

## Do not do

- do not estimate Sync outputs with an LLM;
- do not run registry with `--dry-run false` yet;
- do not mutate task status from Sync;
- do not run ProjectStatus or G1 before deterministic reports are available.
