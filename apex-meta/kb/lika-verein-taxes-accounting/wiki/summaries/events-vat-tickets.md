---
title: "Events, VAT, Tickets, Presale Fees, and Ticketing Providers"
page_type: summary
kb_slug: "lika-verein-taxes-accounting"
summary_slug: "events-vat-tickets"
source_refs:
  - source_id: "raw-refs-lfst-bayern-merkblatt-festveranstaltungen-2025-md"
    source_path: "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md"
    source_hash: "9273c60a549644f072463b4ee212afef39ee5f8072404dfcf8bcca3219125d8c"
    source_pointer: "Phase 1: group-3-events-vat-tickets.analysis.md / key_claims C001-C006"
    source_storage_mode: "copy_into_kb"
  - source_id: "raw-refs-pretix-taxes-guide-md"
    source_path: "raw/refs/pretix_Taxes-Guide.md"
    source_hash: "ff599bd5414638fa4fb1bf3fa7bd80f2eb1a9543"
    source_pointer: "Phase 1: group-3-events-vat-tickets.analysis.md / key_claims C007-C008"
    source_storage_mode: "copy_into_kb"
  - source_id: "raw-notes-judgementofsources-md"
    source_path: "raw/notes/JudgementOfSources.md"
    source_hash: "98d6049ca76d470a4713a041f6bab67b45707d6616133cb7fda42aca1a3d1dbc"
    source_pointer: "Phase 1: group-3-events-vat-tickets.analysis.md / audit_flags A001-A002"
    source_storage_mode: "copy_into_kb"
created_at: "2026-06-29T18:00:00Z"
updated_at: "2026-06-29T18:00:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "needs_review"
related_concepts:
  - "event-business-area-assignment"
  - "event-vat-rate-risk"
  - "ticketing-tax-configuration"
  - "ticket-as-invoice-gap"
related_entities:
  - "lfst-bayern"
  - "pretix"
  - "eventbrite"
  - "ticketio"
review_flags:
  - "7% versus 19% for mixed cultural/club event formats remains unresolved."
  - "Ticket-as-invoice remains unresolved."
  - "LfSt Bayern source is table-heavy and table-sensitive claims require PDF/manual review."
---

# Events, VAT, Tickets, Presale Fees, and Ticketing Providers

## Core Summary

This page is the central event-revenue and ticketing page.

The LfSt Bayern event source is the strongest inspected source for assigning event revenues and expenses across association areas: `ideeller Bereich`, `Vermögensverwaltung`, `Zweckbetrieb`, and `steuerpflichtiger wirtschaftlicher Geschäftsbetrieb`. It also supports the principle that event income and expenses must be recorded individually rather than simply netted.

For VAT, the inspected Phase 1 analysis supports a cautious model: ideeller Bereich is non-entrepreneurial, while Vermögensverwaltung, Zweckbetrieb, and steuerpflichtiger wirtschaftlicher Geschäftsbetrieb belong to the enterprise area. The Phase 1 analysis also records that non-exempt economic-business revenues are generally treated differently from Zweckbetrieb/Vermögensverwaltung revenues.

The pretix documentation is useful for implementing tax rules in a ticketing system, but explicitly not a legal authority. Ticketing tools should implement a tax decision made elsewhere; they should not decide whether 7%, 19%, exemption, reverse charge, or another rule applies.

## What This Adds

```yaml
adds:
  - "A clear separation between event-tax decision and ticketing-provider configuration."
  - "A warning register for 7%-vs-19%, ticket-as-invoice, and mixed-format event treatment."
  - "A process requirement to record event income and expenses individually."

clarifies:
  - "LfSt Bayern is useful for event-area assignment but may not transfer cleanly to Lika's mixed cultural/club model."
  - "pretix can model tax rules per event/product but is not legal or financial advice."
  - "Provider reports support reconciliation, not tax classification."

limits:
  - "This page does not resolve Lika's correct VAT rate."
  - "This page does not establish whether each ticket is a valid invoice."
  - "This page does not finalize venue settlement or minimum bar revenue treatment."
````

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Association event revenue and expenses may need assignment to ideeller Bereich, Vermögensverwaltung, Zweckbetrieb, or steuerpflichtiger wirtschaftlicher Geschäftsbetrieb."
    source_pointer: "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md lines 76-84, via Phase 1 group-3 C001"
    confidence: "medium"
    claim_label: "source_backed_summary"
    used_in_pages:
      - "wiki/concepts/event-business-area-assignment.md"

  - claim_id: C002
    claim: "Event income and expenses should be recorded individually and not simply salded."
    source_pointer: "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md lines 80-83, via Phase 1 group-3 C002"
    confidence: "medium"
    claim_label: "source_backed_summary"
    used_in_pages:
      - "wiki/concepts/event-business-area-assignment.md"

  - claim_id: C003
    claim: "pretix tax rules are configured per event and assigned to products, but pretix documentation is not legal or financial advice."
    source_pointer: "raw/refs/pretix_Taxes-Guide.md lines 14-23 and 28-35, via Phase 1 group-3 C007"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages:
      - "wiki/concepts/ticketing-tax-configuration.md"

  - claim_id: C004
    claim: "pretix can treat configured product prices as gross prices when the tax-included setting is active."
    source_pointer: "raw/refs/pretix_Taxes-Guide.md lines 46-56, via Phase 1 group-3 C008"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages:
      - "wiki/concepts/ticketing-tax-configuration.md"
```

## Contradictions

```yaml
contradictions:
  - id: U001
    issue: "LfSt Bayern Festveranstaltungen may assume contexts that do not transfer cleanly to non-gemeinnützig mixed cultural/club events."
    handling: "Use as structured reference, not final Lika ruling."
    confidence: "medium"

  - id: U002
    issue: "Provider tax configuration can look precise while the underlying tax decision remains unresolved."
    handling: "Keep provider pages operational only."
    confidence: "high"
```

## Open Questions

```yaml
open_questions:
  - question_id: Q001
    question: "Are Lika events taxable wirtschaftlicher Geschäftsbetrieb, cultural Zweckbetrieb, or another category?"
    handling: "tax_advisor_review"

  - question_id: Q002
    question: "Which ticket products exist: entrance, donation, membership, merchandise, presale fee, service fee, refund, voucher?"
    handling: "operator_inventory"

  - question_id: Q003
    question: "Can a ticket or platform receipt satisfy invoice/minimum invoice evidence requirements in Lika's actual workflow?"
    handling: "audit_item"
```
