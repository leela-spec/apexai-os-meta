---
title: "Investment Intelligence and Decision Automation"
status: open
priority: medium
due_date: null
created_date: 2026-08-16
updated_date: 2026-08-16
source:
  - "apex-meta/handoff/plan-packets/apex_plan_packet-20260816-investment-intelligence-automation.md"
review_flags:
  - missing_operator_specific_search_contract
  - missing_operator_specific_alert_contract
  - missing_current_decision_journal_contract
  - no_autonomous_trade_execution_authority
  - three_workstreams_equal_priority
---

# Investment Intelligence and Decision Automation

## Goal

Establish three equally important investment-support loops: scheduled discovery of relevant information, useful low-noise alerts, and structured feedback on operator portfolio/trading decisions.

## Constraints

- Do not rank the three workstreams against each other.
- Use existing OpenClaw/Hermes Cron capability rather than inventing a scheduler.
- Do not infer autonomous trade execution authority.
