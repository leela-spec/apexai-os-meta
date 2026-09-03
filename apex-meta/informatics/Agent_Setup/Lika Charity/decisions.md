---
type: Plan
title: Lika Charity — Decision Gates
description: Current operator and governance decisions required before specific charity automation integrations become authoritative.
status: current
---

# Decision Gates

| ID | Decision | Recommendation | Why it is open |
|---|---|---|---|
| D01 | Telegram structure | One private supergroup with forum topics per event/workstream | Lowest-friction volunteer UX and native Hermes topic isolation. |
| D02 | Ticketing | pretix first; Alf.io challenger; tixlr requires API evidence | pretix has the strongest verified API and webhook surface. |
| D03 | Decision method | Telegram polls for advisory/simple choices; Loomio for structured group decisions | Formal authority depends on Lika's actual rules and decision type. |
| D04 | Accounting profile | Confirm legal form, tax status, VAT treatment, and reporting duties before selecting ledger | Avoid assuming that a charity or association uses one universal chart or tax process. |
| D05 | German ledger | GnuCash SKR49 only if applicable; Odoo/OCA if API automation is worth added complexity | Both are real options with different operating models. |
| D06 | Tax submission | Human-gated only | Consequential external action and organization responsibility. |
| D07 | Receipt auto-posting | Auto only after required-field checks; reviewer resolves ambiguity | Volunteers should not carry accounting classification burden. |
| D08 | Public webhook ingress | Polling first | Current stack is intentionally loopback-bound. |

## Tool placement

- **pretix:** leading ticketing integration.
- **Alf.io:** open-source ticketing challenger; not an ideation tool.
- **tixlr:** commercial candidate; API is unverified here.
- **Loomio:** best-fit optional internal decision layer when polls are too weak.
- **Decidim:** consider only for larger public/community participation.
- **JVerein:** research candidate for association administration and Hibiscus banking integration, not selected as tax authority.
- **Firefly:** operational finance, not final tax ledger.
