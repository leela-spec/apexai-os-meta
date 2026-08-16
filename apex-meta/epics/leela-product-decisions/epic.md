---
title: "Close Leela Decisions and Questions"
status: open
priority: high
due_date: null
created_date: 2026-08-16
updated_date: 2026-08-16
source:
  - "apex-meta/handoff/plan-packets/apex_plan_packet-20260816-leela-product-decisions.md"
review_flags:
  - operator_answers_required_for_actual_QA_closure
  - QA-130_confirmed_ledger_drift_example
  - do_not_bulk_close_open_rows
  - do_not_merge_QA100_and_QA131
---

# Close Leela Decisions and Questions

## Goal

Reconcile and systematically close Leela's unresolved decision queue using current evidence and bounded operator decision batches, without asking the operator to re-answer stale or already-resolved questions.

## Constraints

- Open QA rows cannot be resolved by AI inference.
- Every closed QA must point to the authoritative answer artifact.
- Current decision records/spec/code outrank stale question wording.
