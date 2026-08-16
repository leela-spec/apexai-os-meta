---
title: "Portfolio Project Capture Cursor — 2026-08-16"
document_role: next_session_gate_cursor
created: 2026-08-16
updated: 2026-08-16
status: subscription_ai_projectstatus_and_g1_pending
week: 2026-W34
---

# Portfolio Project Capture Cursor

## Current state

Apex Plan proposal work, operator review, Apex Session canonicalization, and Apex Sync deterministic validation are complete. Nine new epics and 54 tasks are canonical under `apex-meta/epics/`; the full graph contains 62 tasks including the pre-existing NARM epic.

The six W34 Sync reports are committed under `apex-meta/handoff/sync-reports/20260816-w34/`. All commands exited `0`, dependency validation found no structural errors, and eight globally unambiguous next candidates use `epic_slug:NNN` task keys. The next actor is the operator's subscription AI, which must build ProjectStatus, collect week-specific inputs from the operator, run PreCap Week G1, and stop for approval.

## Required restart reading order

1. `apex-meta/handoff/plan-packets/subscription-ai-projectstatus-precap-g1-handoff-20260816-w34.okf.md`
2. `apex-meta/handoff/planning-feed-20260816-w34.md`
3. committed files under `apex-meta/handoff/sync-reports/20260816-w34/`
4. `.claude/skills/ProjectStatus/SKILL.md`
5. `.claude/skills/PrecapWeek/SKILL.md`
6. `.claude/skills/weekly-orchestrator/SKILL.md`

## Gate

```yaml
current_gate:
  from: Apex Sync deterministic validation complete
  to: PreCap Week G1 candidate ready for operator review
  blocker_type: operator_week_context_required
  operator_decision_required: false
  required_action: subscription AI generates ProjectStatus, collects W34-only context from operator, dispatches PreCap Week G1, and stops
  precap_week_g1_allowed_now: true_after_week_context_collection
```

## Exact next sequence

1. Open the subscription-AI handoff packet in a subscription AI with repository access.
2. Generate `artifacts/weekly-plans/project-status-overview-20260816.md` from confirmed Session and Sync sources.
3. Ask the operator only for missing W34 intent, minimum success, capacity, calendar constraints, Dating allocation, and priority overrides.
4. Dispatch PreCap Week for `run_date: 20260816` and `week_id: 2026-W34`.
5. Write `artifacts/weekly-plans/weekly_plan_packet-20260816-2026-W34.md` with `operator_validation: not_requested`.
6. Commit/push the two artifacts and stop at G1. Do not run G2.

## Do not do

- do not replace committed Sync evidence with LLM estimates;
- do not run registry with `--dry-run false`;
- do not mutate canonical task status;
- do not infer missing operator week inputs;
- do not run G2 or execute project work.
