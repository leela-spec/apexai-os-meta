---
title: "Portfolio Project Capture Cursor — 2026-08-16"
document_role: next_session_gate_cursor
created: 2026-08-16
status: waiting_for_operator_approval_to_enter_apex_session
week: 2026-W34
---

# Portfolio Project Capture Cursor

## Current state

Apex Plan proposal work is complete for the first real W34 portfolio intake.

Start from:

- `apex-meta/handoff/plan-packets/portfolio-project-capture-index-20260816-2026-W34.md`

The index points to all supporting project packets and evidence checkpoints.

## Completed planning coverage

- Leela Core Interaction Development — evidence-checked v2 packet
- Leela Product Decisions — evidence-checked packet + decision checkpoints
- Leela Project Management Cleanup — evidence-checked packet
- MasterOfArts Website Definition — source-gap-aware packet
- TransenDance Concept — operator-grounded packet
- Business Invoicing — existing invoice SSOT-grounded packet
- Apex existing-initiative mapping — weekly pilot + PM infrastructure not duplicated
- ApexKB Evolution — prior value-audit-grounded packet
- Investment Intelligence Automation — three equal workstreams, existing Cron capability grounded
- Apartment Improvements — ambiguity-preserving packet
- Dating / meeting women — weekly capacity input only, no tasks

## Gate

```yaml
current_gate:
  from: Apex Plan proposal state
  to: Apex Session confirmed canonical project/task state
  required_authority: explicit operator approval
  canonical_writes_done: false
  apex_sync_allowed_on_new_projects_now: false
  precap_week_g1_allowed_now: false
```

## Exact next sequence after approval

1. Read the portfolio index and current Apex Session contract.
2. Produce Session before/after mutation preview for the nine proposed new epics and approved task records.
3. Apply only operator-approved canonical writes under `apex-meta/epics/`.
4. Refresh Session planning feed/handoff as required.
5. Run Apex Sync deterministic validation against canonical task files.
6. Repair only validated structural/dependency issues through the correct authority.
7. Generate `artifacts/weekly-plans/project-status-overview-20260816.md`.
8. Collect/resolve remaining week-specific intent/calendar inputs.
9. Run PreCap Week G1 to `artifacts/weekly-plans/weekly_plan_packet-20260816-2026-W34.md`.
10. Stop at G1 operator approval.

## Do not do before approval

- no new canonical epic/task files;
- no registry rebuild for proposal-only records;
- no fake Sync computation;
- no G1 packet;
- no OpenClaw project execution;
- no inference that this cursor itself constitutes Session mutation approval.

## Restart rule

Do not reconstruct the project inventory or decompositions from chat. Read the portfolio index and only the relevant current packet/source repository for the next action.
