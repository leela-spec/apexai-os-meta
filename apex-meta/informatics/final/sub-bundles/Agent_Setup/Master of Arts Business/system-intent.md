---
type: Plan
title: Master of Arts Business — System Intent
description: Defines the intended business outcomes, system boundaries, and acceptance conditions for the automation project.
status: current
---

# System Intent

## Outcomes

1. Staff use Telegram as the low-friction operational front door.
2. Event topics keep receipts, ideas, and decisions scoped to the correct event.
3. Paperless stores original receipt evidence and OCR output.
4. Firefly provides the operational finance view.
5. OpenProject owns event and execution state.
6. Ticketing integrates through a documented API.
7. German accounting data can reach a tax-capable ledger or adviser workflow.
8. Hermes orchestrates these systems through explicit APIs and bounded skills.

## Non-goals

- Do not treat Firefly as a German tax-compliance system.
- Do not create a second project-management database.
- Do not expose PostgreSQL, Valkey, or Hermes' Docker socket.
- Do not make tax submissions or binding external decisions without an action-specific operator gate.
- Do not add a new application before a concrete workflow proves that the existing stack cannot cover the requirement.

## System-of-record boundaries

| Information | Owner |
|---|---|
| Original receipt/document | Paperless-ngx |
| Operational transaction view | Firefly III |
| Event, task, milestone, execution status | OpenProject |
| Conversation and event-topic context | Telegram + Hermes session |
| Ticket orders/check-in | Selected ticket system |
| German tax ledger | To be selected; not Firefly by assumption |
| Final tax submission | Operator / Steuerberater / approved tax channel |

## Acceptance conditions

- A receipt photo posted in an event topic reaches the correct event without manual retyping.
- The original receipt remains retrievable from Paperless.
- Duplicate receipt ingestion is detected before a second finance record is created.
- Ambiguous vendor, amount, VAT, or accounting category creates a review item instead of guessing.
- A ticketing proof can read event/order/check-in state through the selected product API.
- An event idea can move from discussion to a recorded decision and executable OpenProject work.
- A tested export path exists from operational finance to the selected German accounting/tax workflow.
