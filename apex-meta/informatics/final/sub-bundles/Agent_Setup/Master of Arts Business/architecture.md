---
type: Reference
title: Master of Arts Business — Workflow Architecture
description: Maps the verified ki-basis stack to Telegram, receipt, ticketing, ideation, event-planning, and German tax-handoff workflows.
status: current
---

# Workflow Architecture

## Current stack boundary

`ki-basis` currently provides PostgreSQL/pgvector, Valkey, Firefly III, Paperless-ngx, OpenProject, Nginx, and Hermes. Hermes already receives internal API URLs for Firefly, Paperless, and OpenProject in `compose.yaml`.

| Component | Current role | Workflow use |
|---|---|---|
| Hermes | Agent execution and messaging gateway | Telegram intake, extraction, routing, API orchestration |
| Paperless-ngx | Document storage and OCR | Receipt evidence and searchable source document |
| Firefly III | Personal-finance application with API | Operational expense/income view; not the tax ledger |
| OpenProject | Project/work-package system with API v3 | Event, task, review, milestone, and decision follow-through |
| PostgreSQL + pgvector | Internal data substrate | Reuse only when a concrete integration record is required; no new KB by default |
| Valkey | Internal cache | Existing application dependency |
| Nginx | Loopback edge proxy | Keep local by default; public webhook ingress is a separate decision |

## W1 — Event workspace and Telegram supergroup

Target: one Telegram supergroup with forum topics. Each event receives scoped operational topics.

```mermaid
flowchart TD
    A[OpenProject: approved event] --> B[Assign durable event_id]
    B --> C{Pilot or target automation?}
    C -->|Pilot| D[Admin creates Telegram forum topics]
    C -->|Target| E[Bot calls createForumTopic]
    D --> F[Register chat_id + thread_id + event_id]
    E --> F
    F --> G[Bind Hermes topic skill/prompt]
    G --> H[Receipts topic]
    G --> I[Ideas & decisions topic]
    G --> J[Operations topic]
    H --> K[Isolated Hermes session]
    I --> L[Isolated Hermes session]
    J --> M[Isolated Hermes session]
```

Telegram supports forum topics. Hermes already isolates group sessions by topic and supports topic skill bindings. The pilot should prove topic routing before automating topic creation.

## W2 — Receipt photo to evidence and operational bookkeeping

```mermaid
flowchart TD
    A[User posts receipt photo in event Receipts topic] --> B[Hermes receives image + chat/thread/message metadata]
    B --> C[Resolve event_id from topic mapping]
    C --> D[Download original image]
    D --> E[Compute SHA-256 + retain Telegram file_unique_id]
    E --> F{Already ingested?}
    F -->|Yes| G[Reply with existing record link]
    F -->|No| H[Upload original to Paperless]
    H --> I[Paperless OCR + document ID]
    I --> J[Hermes extracts vendor/date/gross/net/VAT/currency/purpose]
    J --> K{Required fields consistent?}
    K -->|No| L[Create OpenProject review work package]
    K -->|Yes| M[Create or update Firefly operational transaction]
    L --> N[Human resolves ambiguity]
    N --> M
    M --> O[Link Firefly record to Paperless document + event_id]
    O --> P[Receipt available for later tax-ledger handoff]
```

Do not infer tax category or VAT when evidence is ambiguous. Paperless owns the original document; Firefly owns only the operational finance view.

## W3 — Operational bookkeeping to German tax workflow

```mermaid
flowchart TD
    A[Paperless evidence] --> C[Reconciled transaction set]
    B[Firefly operational finance] --> C
    C --> D{Selected German ledger}
    D -->|Lean desktop candidate| E[GnuCash: SKR03/SKR04 as applicable]
    D -->|API-first candidate| F[Odoo Community + OCA Germany]
    E --> G[Period reconciliation + export]
    F --> G
    G --> H[DATEV/CSV/EÜR-ready handoff as supported]
    H --> I{Operator gate}
    I -->|Steuerberater| J[Adviser / DATEV workflow]
    I -->|Self filing where applicable| K[Mein ELSTER]
```

GnuCash and Odoo/OCA are candidates, not installed stack components. Select the ledger after a real export/import proof. Keep final filing outside autonomous execution for the first release.

## W4 — Ticketing integration

```mermaid
flowchart TD
    A[OpenProject event specification] --> B[Selected ticket system]
    B --> C[Create/update event, items, quotas, dates]
    C --> D[Public ticket sales]
    D --> E[Orders / invoices / check-in state]
    E --> F[API polling in Trial 1]
    E --> G[Webhook later if secure ingress is approved]
    F --> H[Hermes event digest]
    G --> H
    H --> I[OpenProject status / operational tasks]
    H --> J[Finance reconciliation inputs]
```

**Leading candidate:** pretix. Its documented REST API covers events, orders, invoices, transactions, check-in, exporters, and webhooks. `tixlr.de` currently has no public API documentation verified for this project. Alf.io is a valid open-source ticketing challenger, not an ideation tool.

## W5 — Ideation, voting, and final event programme

```mermaid
flowchart TD
    A[People post ideas in Telegram Ideas topic] --> B[Hermes extracts one idea card per proposal]
    B --> C[Create/update OpenProject Idea work packages]
    C --> D[Cluster duplicates + surface dependencies]
    D --> E{Decision complexity}
    E -->|Simple preference| F[Telegram poll]
    E -->|Structured consent/rank/allocate needed| G[Loomio candidate]
    F --> H[Hermes records outcome + rationale]
    G --> H
    H --> I[Operator / defined group decision gate]
    I --> J[Accepted programme in OpenProject]
    J --> K[Tasks, milestones, ticket configuration, communications]
```

Start with Telegram + OpenProject. Add Loomio only when the group needs richer proposals, ranking, allocation, consent, or an auditable decision process. Decidim is a later option for broad public participation, not the first internal-team tool.

## Integration rules

- Store secrets outside Git.
- Allowlist Telegram users/chats.
- Keep Telegram group privacy and bot admin permissions explicit.
- Use idempotency keys for receipt and ticket mutations.
- Prefer polling before opening public webhook ingress.
- Use OpenProject for review queues instead of inventing another task database.
- Keep `pgvector` unused until a measured retrieval need justifies a semantic index.

## Evidence anchors

- Telegram Bot API: https://core.telegram.org/bots/api
- Hermes Telegram: https://hermes-agent.nousresearch.com/docs/user-guide/messaging/telegram
- Paperless API: https://docs.paperless-ngx.com/api/
- OpenProject API v3: https://www.openproject.org/docs/api/
- pretix API: https://docs.pretix.eu/dev/api/
- GnuCash German account frameworks: https://wiki.gnucash.org/wiki/De/Referenz
- OCA German localization: https://github.com/OCA/l10n-germany
- Mein ELSTER: https://www.elster.de/
