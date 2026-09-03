---
type: Plan
title: Master of Arts Business — Decision Gates
description: Current operator decisions and evidence gates that must be resolved before specific integrations become authoritative.
status: current
---

# Decision Gates

| ID | Decision | Recommendation | Why it is open |
|---|---|---|---|
| D01 | Telegram structure | One private supergroup with forum topics per event/workstream | Native Telegram/Hermes fit is strong; test permissions and topic routing first. |
| D02 | Ticketing | pretix first; Alf.io challenger; tixlr blocked until API evidence exists | pretix has the broadest verified REST/webhook surface. |
| D03 | German accounting ledger | Bake off GnuCash against Odoo Community + OCA Germany | GnuCash is lean; Odoo/OCA is more automatable. Legal/tax profile determines chart and reports. |
| D04 | Ideation/decision tool | Telegram + OpenProject first; Loomio only if richer governance is needed | Avoid another service until basic workflow proves insufficient. |
| D05 | Receipt auto-posting threshold | Auto-post only after deterministic required-field checks; route ambiguity to review | Accounting/VAT guesses must not silently become records. |
| D06 | Tax submission automation | Human-gated only in v1 | Filing is an external consequential action. |
| D07 | Public webhook ingress | Polling first | Current stack is loopback-bound; do not weaken that boundary for convenience. |

## Product clarifications

- **Alf.io:** ticket reservation and attendance management. It does not solve ideation.
- **Loomio:** dedicated discussion, proposal, poll, ranking, allocation, consent, and outcome tooling. Treat it as an optional decision layer.
- **Firefly III:** keep for operational finance. Do not equate its double-entry model with German tax compliance.
- **pgvector:** available infrastructure. Do not create a receipt vector index until retrieval value is demonstrated.
