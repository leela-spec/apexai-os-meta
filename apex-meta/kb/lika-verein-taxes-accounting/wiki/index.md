---
title: "Lika Verein Taxes Accounting Index"
page_type: "index"
kb_slug: "lika-verein-taxes-accounting"
source_refs:
  - source_id: "llm-phase1-grouped-ingest"
    source_path: "ingest-analysis/"
    source_hash: "NA"
    source_pointer: "Phase 1 grouped analyses approved for Phase 2"
    source_storage_mode: "derived_from_ingest_analysis"
created_at: "2026-06-28T20:37:26Z"
updated_at: "2026-06-30T12:15:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "active"
---

# Lika Verein Taxes Accounting Index

<!-- BEGIN AUTO-GENERATED INDEX -->

Generated manually in this continuation: `2026-06-30T12:15:00Z`

Compiled Phase 2 page count recorded here: `32`

Deterministic script rebuild still required in a real checkout:

```bash
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/lika-verein-taxes-accounting --json --allow-write index
```

<!-- END AUTO-GENERATED INDEX -->

<!-- BEGIN LLM SUMMARY -->

## Phase 2 Semantic Index Summary

This KB contains six Phase 2 summary pages plus the minimum required concept and entity pages compiled from the approved grouped Phase 1 ingest analyses.

### Summary pages

- `wiki/summaries/core-tax-law-invoicing-gobd.md`
- `wiki/summaries/association-accounting-process.md`
- `wiki/summaries/events-vat-tickets.md`
- `wiki/summaries/artist-contractor-obligations.md`
- `wiki/summaries/source-judgment-and-open-risks.md`
- `wiki/summaries/source-quality-and-custody.md`

### Concept pages

- `wiki/concepts/invoice-core-fields.md`
- `wiki/concepts/kleinbetragsrechnung.md`
- `wiki/concepts/e-rechnung-verein.md`
- `wiki/concepts/belegablage-verfahrensdokumentation.md`
- `wiki/concepts/verein-activity-areas.md`
- `wiki/concepts/ust-7-vs-19-event-context.md`
- `wiki/concepts/vorsteuer-zuordnung-aufteilung.md`
- `wiki/concepts/ticket-as-invoice-gap.md`
- `wiki/concepts/ticketing-provider-reconciliation.md`
- `wiki/concepts/kuenstlersozialabgabe-event.md`
- `wiki/concepts/foreign-artist-50a.md`
- `wiki/concepts/minijob-short-term-event-work.md`
- `wiki/concepts/source-quality-risk.md`
- `wiki/concepts/web-clutter-filter.md`
- `wiki/concepts/unresolved-tax-risk-register.md`

### Entity pages

- `wiki/entities/bmf.md`
- `wiki/entities/bmj-gesetze-im-internet.md`
- `wiki/entities/awv.md`
- `wiki/entities/datev.md`
- `wiki/entities/deutsche-rentenversicherung.md`
- `wiki/entities/kuenstlersozialkasse.md`
- `wiki/entities/lfst-bayern.md`
- `wiki/entities/bzst.md`
- `wiki/entities/pretix.md`
- `wiki/entities/eventbrite.md`
- `wiki/entities/ticketio.md`

## Query routing

- Invoice, e-invoice, and receipt custody: start with `wiki/summaries/core-tax-law-invoicing-gobd.md`, then `invoice-core-fields`, `kleinbetragsrechnung`, `e-rechnung-verein`, or `belegablage-verfahrensdokumentation`.
- Event VAT and ticketing: start with `wiki/summaries/events-vat-tickets.md`, then `verein-activity-areas`, `ust-7-vs-19-event-context`, `ticket-as-invoice-gap`, or `ticketing-provider-reconciliation`.
- Artists, KSK, foreign artists, and event work: start with `wiki/summaries/artist-contractor-obligations.md`, then `kuenstlersozialabgabe-event`, `foreign-artist-50a`, or `minijob-short-term-event-work`.
- Source quality and unresolved risks: start with `wiki/summaries/source-quality-and-custody.md` and `wiki/summaries/source-judgment-and-open-risks.md`, then `source-quality-risk`, `web-clutter-filter`, or `unresolved-tax-risk-register`.

## Highest-risk open items

- 7% versus 19% VAT for mixed cultural/club event formats.
- Ticket-as-invoice and platform receipt evidence.
- Foreign artist withholding and VAT workflow.
- KSK threshold/application details.
- Noisy web captures and table-heavy PDF sources.

<!-- END LLM SUMMARY -->
