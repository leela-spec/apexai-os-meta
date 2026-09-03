---
type: Plan
title: Lika Charity — System Intent
description: Defines the charity operations outcomes, system boundaries, and acceptance conditions for the automation project.
status: current
---

# System Intent

## Outcomes

1. Volunteers can submit receipts from Telegram without learning bookkeeping software.
2. Each event has isolated Telegram topics for receipts, ideas, decisions, and operations.
3. Paperless preserves the original evidence and OCR.
4. Firefly provides an operational money view while a separate German accounting path remains possible.
5. OpenProject owns tasks, event planning, review work, and delivery status.
6. Group ideas move through a visible decision process before becoming event programme commitments.
7. Ticketing integrates through a documented API when the charity sells or allocates tickets.
8. Hermes assists and automates bounded work without becoming the legal or governance decision maker.

## Non-goals

- Do not infer Lika's legal form, charitable tax status, VAT status, or required chart of accounts.
- Do not treat Telegram polling as legally binding governance unless the applicable rules explicitly permit it.
- Do not let receipt OCR silently determine tax treatment when evidence is unclear.
- Do not store bot or finance secrets in Git.
- Do not add a second task tracker beside OpenProject.

## System-of-record boundaries

| Information | Owner |
|---|---|
| Original receipt/document | Paperless-ngx |
| Operational money view | Firefly III |
| Event/tasks/review queue | OpenProject |
| Volunteer conversation | Telegram + Hermes topic session |
| Ticketing | Selected ticket system |
| Accounting/tax ledger | To be selected after legal/accounting profile is confirmed |
| Formal organization decision | Human body defined by Lika's rules |

## Acceptance conditions

- A volunteer posts a receipt in the correct event topic and receives a clear acknowledgement.
- The original image is preserved and linked to its event.
- Duplicate uploads do not create duplicate expense records.
- Ambiguous receipts enter a review queue.
- Ideas can be collected, deduplicated, voted or deliberated, and converted into approved OpenProject work.
- The selected ticket system can be read and managed through a verified API.
- The selected accounting path can export records in a form accepted by the responsible tax workflow or adviser.
