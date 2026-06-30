---
title: "Lika Verein Taxes Accounting Index"
page_type: index
kb_slug: "lika-verein-taxes-accounting"
source_refs:
  - source_id: "llm-phase1-grouped-ingest"
    source_path: "ingest-analysis/"
    source_hash: "NA"
    source_pointer: "Phase 1 grouped analyses approved for Phase 2"
    source_storage_mode: "copy_into_kb"
created_at: "2026-06-28T20:37:26Z"
updated_at: "2026-06-29T18:00:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "active"
---

# Lika Verein Taxes Accounting Index

<!-- BEGIN AUTO-GENERATED INDEX -->

Generated: `2026-06-29T16:34:08Z`

Compiled page count before Phase 2 chat-output compile: `0`

Deterministic index rebuild required after saving Phase 2 pages locally.

<!-- END AUTO-GENERATED INDEX -->

<!-- BEGIN LLM SUMMARY -->

## Phase 2 Semantic Index Summary

This KB currently compiles six approved Phase 2 summary pages from the grouped Phase 1 ingest analysis:

```yaml
compiled_summaries:
  - path: "wiki/summaries/core-tax-law-invoicing-gobd.md"
    covers:
      - invoices
      - Kleinbetragsrechnung
      - E-Rechnung
      - Belegablage
      - GoBD source-quality warning
    confidence: "medium"
    status: "needs_review"

  - path: "wiki/summaries/association-accounting-process.md"
    covers:
      - accounting source custody
      - receipt/evidence workflow
      - reimbursement evidence
      - DATEV/SKR42 cleanup requirement
    confidence: "medium"
    status: "needs_review"

  - path: "wiki/summaries/events-vat-tickets.md"
    covers:
      - event revenue/expense assignment
      - event VAT treatment risk
      - ticketing-provider configuration
      - ticket-as-invoice gap
    confidence: "medium"
    status: "needs_review"

  - path: "wiki/summaries/artist-contractor-obligations.md"
    covers:
      - Künstlersozialabgabe
      - foreign artist §50a
      - foreign artist VAT recipient liability
      - artist contract counterparty review
    confidence: "medium"
    status: "needs_review"

  - path: "wiki/summaries/source-judgment-and-open-risks.md"
    covers:
      - source authority hierarchy
      - transfer safety
      - unresolved tax risk register
      - venue settlement gap
    confidence: "medium"
    status: "needs_review"

  - path: "wiki/summaries/source-quality-and-custody.md"
    covers:
      - web clutter
      - duplicate source custody
      - table-heavy PDF risk
      - Phase 1 placeholder replacement
    confidence: "high"
    status: "active"
````

## Query Routing

```yaml
query_routing:
  invoice_or_e_rechnung:
    read_first:
      - "wiki/summaries/core-tax-law-invoicing-gobd.md"

  receipts_or_bookkeeping_process:
    read_first:
      - "wiki/summaries/association-accounting-process.md"
      - "wiki/summaries/source-quality-and-custody.md"

  event_vat_or_ticketing:
    read_first:
      - "wiki/summaries/events-vat-tickets.md"
      - "wiki/summaries/source-judgment-and-open-risks.md"

  artist_payments_or_ksk_or_foreign_artists:
    read_first:
      - "wiki/summaries/artist-contractor-obligations.md"

  source_quality_or_cleanup:
    read_first:
      - "wiki/summaries/source-quality-and-custody.md"

  unresolved_risks:
    read_first:
      - "wiki/summaries/source-judgment-and-open-risks.md"
```

## Highest-Risk Open Items

```yaml
high_risk_open_items:
  - id: R001
    title: "7% versus 19% VAT for mixed cultural/club event formats"
    status: "unresolved"
    handling: "tax_advisor_review"

  - id: R002
    title: "Ticket-as-invoice / platform receipt evidence"
    status: "unresolved"
    handling: "audit_item"

  - id: R003
    title: "Venue settlement / Mindestbarumsatz / Barumsatzgarantie"
    status: "unresolved"
    handling: "additional_research_or_tax_advisor_review"

  - id: R004
    title: "Foreign artist §50a and VAT workflow"
    status: "partially_mapped"
    handling: "separate_workflow_required"

  - id: R005
    title: "High-noise authority captures"
    status: "cleanup_required"
    handling: "create_cleaned_snapshots"
```
