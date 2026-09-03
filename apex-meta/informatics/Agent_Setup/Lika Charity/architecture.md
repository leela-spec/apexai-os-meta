---
type: Reference
title: Lika Charity — Workflow Architecture
description: Maps the verified ki-basis stack to volunteer receipt intake, event topics, ticketing, group decisions, planning, and German accounting handoff.
status: current
---

# Workflow Architecture

## Current stack boundary

Use the existing `ki-basis` services as separate systems of record. Do not turn Hermes into a new database.

| Component | Charity role |
|---|---|
| Hermes | Telegram interaction, image understanding, extraction, API orchestration |
| Paperless-ngx | Original receipt evidence, OCR, tags, custom fields |
| Firefly III | Operational expense/income view; not tax authority |
| OpenProject | Event plan, volunteer tasks, receipt reviews, decision follow-through |
| PostgreSQL + pgvector | Existing substrate; use only for proven integration state or later retrieval needs |
| Nginx | Local edge; keep public exposure closed by default |

## W1 — Charity supergroup and event-topic system

```mermaid
flowchart TD
    A[Approved event in OpenProject] --> B[Event ID]
    B --> C[Telegram private supergroup]
    C --> D[Event Receipts topic]
    C --> E[Event Ideas & Decisions topic]
    C --> F[Event Operations topic]
    D --> G[Hermes receipt skill/prompt]
    E --> H[Hermes ideation skill/prompt]
    F --> I[Hermes operations session]
    G --> J[Paperless + finance workflow]
    H --> K[OpenProject + decision workflow]
```

For the first pilot, an admin creates topics and records thread IDs. Target automation may later call Telegram `createForumTopic` after the permissions and mapping workflow is proven.

## W2 — Volunteer receipt photo

```mermaid
flowchart TD
    A[Volunteer posts receipt photo] --> B[Hermes receives image in event Receipts topic]
    B --> C[Authorize sender/chat + resolve event_id]
    C --> D[Hash image + retain Telegram file_unique_id]
    D --> E{Duplicate?}
    E -->|Yes| F[Return existing receipt reference]
    E -->|No| G[Upload original to Paperless]
    G --> H[OCR + Paperless document ID]
    H --> I[Hermes extracts merchant/date/amount/VAT/currency/purpose]
    I --> J{Evidence complete and consistent?}
    J -->|No| K[OpenProject review work package]
    J -->|Yes| L[Create operational Firefly transaction]
    K --> M[Treasurer/authorized reviewer resolves]
    M --> L
    L --> N[Link event + Paperless document + finance record]
```

The photo should be easy for volunteers; review complexity belongs with the authorized finance role.

## W3 — Bookkeeping and German tax handoff

```mermaid
flowchart TD
    A[Paperless evidence] --> C[Reviewed expense/income set]
    B[Firefly operational view] --> C
    C --> D{Confirmed legal/accounting profile}
    D --> E{Ledger choice}
    E -->|German association candidate| F[GnuCash SKR49 if applicable]
    E -->|API-first organization accounting| G[Odoo Community + OCA Germany]
    E -->|Membership/banking candidate| H[JVerein + Hibiscus research lane]
    F --> I[Reconcile + export]
    G --> I
    H --> I
    I --> J[DATEV/CSV/required tax figures]
    J --> K{Human filing gate}
    K --> L[Steuerberater / DATEV]
    K --> M[Mein ELSTER where applicable]
```

GnuCash documents SKR49 for German associations. This is only a candidate until Lika's legal and tax profile is confirmed. JVerein is open-source association administration with Hibiscus integration, but it is not yet selected as the accounting/tax backbone.

## W4 — Ticketing

```mermaid
flowchart TD
    A[Approved event + capacity in OpenProject] --> B[pretix leading candidate]
    B --> C[Create event/items/quotas]
    C --> D[Ticket sale or allocation]
    D --> E[Order/invoice/check-in data]
    E --> F[API polling first]
    E --> G[Webhook later if secure ingress is approved]
    F --> H[Hermes summary]
    G --> H
    H --> I[OpenProject attendance/status tasks]
    H --> J[Finance reconciliation input]
```

pretix has the strongest verified API fit. Alf.io is an open-source ticketing alternative. `tixlr.de` remains an option only after official API evidence is obtained.

## W5 — Ideation, voting, and event programme

```mermaid
flowchart TD
    A[Members post ideas in event Ideas topic] --> B[Hermes creates concise idea cards]
    B --> C[OpenProject Idea work packages]
    C --> D[Merge duplicates + expose tradeoffs]
    D --> E{Decision need}
    E -->|Quick preference| F[Telegram poll]
    E -->|Rank/allocate/consent/consensus| G[Loomio candidate]
    F --> H[Record result and reasons]
    G --> H
    H --> I[Authorized human/body decides]
    I --> J[Accepted event programme]
    J --> K[OpenProject tasks + milestones]
```

Telegram remains the easy participation surface. OpenProject remains the execution surface. Loomio is the first challenger when decision quality needs more than a simple poll. Decidim is reserved for broader public participation.

## Security and governance rules

- Use Telegram user/chat allowlists.
- Grant only required bot admin permissions.
- Store tokens outside Git.
- Keep original receipts immutable in Paperless.
- Keep human review for ambiguous accounting fields.
- Keep formal governance authority with the organization, not Hermes.
- Prefer polling before opening public webhooks into the loopback-only stack.

## Evidence anchors

- Telegram Bot API: https://core.telegram.org/bots/api
- Hermes Telegram: https://hermes-agent.nousresearch.com/docs/user-guide/messaging/telegram
- Paperless API: https://docs.paperless-ngx.com/api/
- OpenProject API v3: https://www.openproject.org/docs/api/
- pretix API: https://docs.pretix.eu/dev/api/
- GnuCash German account frameworks: https://wiki.gnucash.org/wiki/De/Referenz
- JVerein: https://www.jverein.de/
- OCA Germany: https://github.com/OCA/l10n-germany
- Loomio: https://www.loomio.com/docs/en/user_manual/polls/intro_to_decisions
