---
title: "Core Tax Law, Invoicing, E-Rechnung, and GoBD"
page_type: summary
kb_slug: "lika-verein-taxes-accounting"
summary_slug: "core-tax-law-invoicing-gobd"
source_refs:
  - source_id: "raw-refs-bmj-ustg-14-rechnungen-md"
    source_path: "raw/refs/BMJ_UStG_14_Rechnungen.md"
    source_hash: "df72475e17f140cd1fea087ea6e5956bb9c59a586e375265e19a30edbb3769f8"
    source_pointer: "Phase 1: group-1-core-tax-law.analysis.md / key_claims C001-C004"
    source_storage_mode: "copy_into_kb"
  - source_id: "raw-refs-bmj-ustdv-33-kleinbetragsrechnungen-md"
    source_path: "raw/refs/BMJ_UStDV_33_Kleinbetragsrechnungen.md"
    source_hash: "25b91a7533394bcd94b3e035f55609649ddff7a933f00342d4b0dfbef4b4fb08"
    source_pointer: "Phase 1: group-1-core-tax-law.analysis.md / key_claim C005"
    source_storage_mode: "copy_into_kb"
  - source_id: "raw-refs-bmf-faq-e-rechnung-md"
    source_path: "raw/refs/BMF_FAQ-E-Rechnung.md"
    source_hash: "6a839e4c677fec795ed977e458f5fc0f939397047aca4d2908801f8c003d53dc"
    source_pointer: "Phase 1: group-1-core-tax-law.analysis.md / key_claims C006-C007"
    source_storage_mode: "copy_into_kb"
  - source_id: "raw-refs-awv-muster-verfahrensdokumentation-belegablage-md"
    source_path: "raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.md"
    source_hash: "362270a8ffe6c5f9b3e7493ac02fc2ebdd9443711d9cbbc0abf66c06c4e1a0c7"
    source_pointer: "Phase 1: group-1-core-tax-law.analysis.md / key_claim C008"
    source_storage_mode: "copy_into_kb"
created_at: "2026-06-29T18:00:00Z"
updated_at: "2026-06-29T18:00:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "needs_review"
related_concepts:
  - "invoice-core-fields"
  - "kleinbetragsrechnung"
  - "e-rechnung-verein"
  - "belegablage-verfahrensdokumentation"
related_entities:
  - "bmj-gesetze-im-internet"
  - "bmf"
  - "awv"
review_flags:
  - "BMF_GoBD-2024.md is high-noise and should not be used as semantic authority until cleaned."
  - "E-Rechnung applicability depends on Lika's concrete entrepreneurial/non-entrepreneurial activity split."
---

# Core Tax Law, Invoicing, E-Rechnung, and GoBD

## Core Summary

This page is the entry point for invoice, small-invoice, e-invoice, and receipt-custody questions in the Lika Verein Taxes Accounting KB.

The strongest inspected anchors are the statutory invoice sources from BMJ/Gesetze im Internet and the small-invoice rule under §33 UStDV. These support a practical distinction between normal invoice requirements and `Kleinbetragsrechnung` handling.

The BMF E-Rechnung FAQ is relevant for 2025+ e-invoicing, especially for distinguishing structured electronic invoices from PDFs and for separating a Verein’s entrepreneurial and non-entrepreneurial areas. It should be used with caution because it was captured as a web page and contains navigation artifacts.

The AWV Belegablage source is the main process source for evidence custody. It supports a KB workflow in which Lika documents receipt intake, identification, completeness checks, storage order, protection against loss/change, handoff to bookkeeping/tax advisor, and retention/destruction rules.

## What This Adds

```yaml
adds:
  - "A single navigation page for invoice, e-invoice, and receipt-custody logic."
  - "A split between statutory invoice requirements and operational Belegablage process design."
  - "A warning that BMF_GoBD-2024.md requires cleaned extraction before use."

clarifies:
  - "Invoice-field requirements are not the same thing as ticket-as-invoice certainty."
  - "E-Rechnung relevance depends on whether Lika acts in an entrepreneurial area and whether the counterparty is Unternehmer."
  - "AWV is process guidance, not a substitute for tax-law interpretation."

limits:
  - "This page is not legal advice."
  - "This page does not resolve the ticket-as-invoice gap."
  - "GoBD claims should not rely on the current high-noise BMF GoBD Markdown capture."
````

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "A Rechnung is any document used to settle a delivery or other service, regardless of the document name."
    source_pointer: "raw/refs/BMJ_UStG_14_Rechnungen.md lines 7-8, via Phase 1 group-1 C001"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages:
      - "wiki/concepts/invoice-core-fields.md"

  - claim_id: C002
    claim: "A structured electronic format is required for an E-Rechnung; simple paper/PDF-like invoices remain separate from structured electronic invoices."
    source_pointer: "raw/refs/BMJ_UStG_14_Rechnungen.md lines 8-14; raw/refs/BMF_FAQ-E-Rechnung.md lines 53-63, via Phase 1 group-1 C002/C006"
    confidence: "medium"
    claim_label: "source_backed_summary"
    used_in_pages:
      - "wiki/concepts/e-rechnung-verein.md"

  - claim_id: C003
    claim: "For invoices not exceeding 250 EUR, §33 UStDV allows reduced minimum invoice fields."
    source_pointer: "raw/refs/BMJ_UStDV_33_Kleinbetragsrechnungen.md lines 7-22, via Phase 1 group-1 C005"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages:
      - "wiki/concepts/kleinbetragsrechnung.md"

  - claim_id: C004
    claim: "A durable Belegablage procedure should cover receipt entry/creation, identification, completeness, ordering, protection, bookkeeping handoff, retention, and destruction."
    source_pointer: "raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.md lines 39-55, via Phase 1 group-1 C008 and group-2 C001-C003"
    confidence: "medium"
    claim_label: "source_backed_summary"
    used_in_pages:
      - "wiki/concepts/belegablage-verfahrensdokumentation.md"
```

## Contradictions

```yaml
contradictions:
  - id: U001
    issue: "BMF GoBD source is high-noise in current Markdown form."
    handling: "Do not use for detailed GoBD claims until cleaned snapshot or PDF-derived review exists."
    confidence: "high"

  - id: U002
    issue: "The available invoice sources do not by themselves establish that every event ticket qualifies as a sufficient invoice or small-value invoice in Lika's concrete workflow."
    handling: "Keep ticket-as-invoice as a separate audit item."
    confidence: "medium"
```

## Open Questions

```yaml
open_questions:
  - question_id: Q001
    question: "Which Lika activities are entrepreneurial for E-Rechnung purposes?"
    handling: "audit_item"

  - question_id: Q002
    question: "Should Lika preserve structured XML plus human-readable rendering for E-Rechnung inputs/outputs?"
    handling: "process_design"

  - question_id: Q003
    question: "Which cleaned GoBD source should become canonical?"
    handling: "source_custody_decision"
```
