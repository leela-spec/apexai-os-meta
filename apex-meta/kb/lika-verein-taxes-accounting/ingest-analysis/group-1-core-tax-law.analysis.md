---
title: "Core Tax Law, Invoicing, E-Rechnung, GoBD"
page_type: ingest_analysis
kb_slug: lika-verein-taxes-accounting
phase: ingest_phase_1
status: operator_review_needed
source_refs:
  - "raw/refs/BMJ_UStG_14_Rechnungen.md"
  - "raw/refs/BMJ_UStDV_33_Kleinbetragsrechnungen.md"
  - "raw/refs/BMF_FAQ-E-Rechnung.md"
  - "raw/refs/BMF_GoBD-2024.md"
  - "raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.md"
created_at: "2026-06-29T17:30:00Z"
updated_at: "2026-06-29T17:30:00Z"
confidence: medium
claim_label: source_grounded_analysis
phase_2_allowed: false
phase_2_requires: "approve ingest"
---

# Core Tax Law, Invoicing, E-Rechnung, GoBD

## source_scope

This group covers invoice definitions, mandatory invoice fields, small-value invoices, e-invoice transition rules, E-Rechnung impact on associations, GoBD/source custody, and document-retention process design.

Primary inspected source refs:

- `raw/refs/BMJ_UStG_14_Rechnungen.md`
- `raw/refs/BMJ_UStDV_33_Kleinbetragsrechnungen.md`
- `raw/refs/BMF_FAQ-E-Rechnung.md`
- `raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.md`

Included but high-noise / not substantively usable without cleaned snapshot:

- `raw/refs/BMF_GoBD-2024.md`

## source_quality_notes

```yaml
source_quality_notes:
  - source: "raw/refs/BMJ_UStG_14_Rechnungen.md"
    clutter_status: clean
    usable_sections:
      - "definition of invoice"
      - "e-invoice definition"
      - "invoice-issuance obligation"
      - "mandatory invoice fields"
    suspected_noise_sections: []
    confidence_effect: none
    recommended_action: use_as_is

  - source: "raw/refs/BMJ_UStDV_33_Kleinbetragsrechnungen.md"
    clutter_status: clean
    usable_sections:
      - "Kleinbetragsrechnung up to 250 EUR"
      - "minimum required invoice fields"
    suspected_noise_sections: []
    confidence_effect: none
    recommended_action: use_as_is

  - source: "raw/refs/BMF_FAQ-E-Rechnung.md"
    clutter_status: moderate_noise
    usable_sections:
      - "BMF FAQ date/status"
      - "E-Rechnung definition"
      - "exceptions"
      - "associations/Vereine"
      - "formats"
      - "transmission/receipt"
      - "transition rules"
    suspected_noise_sections:
      - "navigation links"
      - "page anchors"
    confidence_effect: lowered
    recommended_action: use_with_caution

  - source: "raw/refs/BMF_GoBD-2024.md"
    clutter_status: unusable_until_cleaned
    usable_sections: []
    suspected_noise_sections:
      - "cookie consent"
      - "navigation"
      - "footer/menu material"
    confidence_effect: severe
    recommended_action: create_cleaned_snapshot

  - source: "raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.md"
    clutter_status: moderate_noise
    usable_sections:
      - "scope of Belegablage"
      - "legal basis"
      - "process questions"
      - "Verfahrensdokumentation requirements"
      - "retention and original-format requirements"
    suspected_noise_sections:
      - "PDF page headers"
      - "table-of-contents artifacts"
      - "omitted pictures"
    confidence_effect: lowered
    recommended_action: use_with_caution
````

## relevance_summary

This group is central for a Lika Verein accounting KB because invoice handling, e-invoice readiness, receipt custody, and GoBD-style documentation are cross-cutting prerequisites for ticketing, contractor payments, reimbursements, and bookkeeping.

The strongest legal anchors are `BMJ_UStG_14_Rechnungen.md` and `BMJ_UStDV_33_Kleinbetragsrechnungen.md`. The strongest operational process source is `AWV_Muster-Verfahrensdokumentation-Belegablage.md`. The BMF e-invoice FAQ is directly relevant but should be used with caution because it is a web capture with navigation content.

## key_claims

```yaml
key_claims:
  - claim_id: C001
    claim: "A Rechnung is any document used to settle a delivery or other service, regardless of what the document is called."
    source_pointer: "raw/refs/BMJ_UStG_14_Rechnungen.md lines 7-8"
    confidence: high
    claim_label: source_backed_summary

  - claim_id: C002
    claim: "An electronic invoice under §14 UStG requires a structured electronic format that enables electronic processing; other electronic or paper invoices are classified as sonstige Rechnung."
    source_pointer: "raw/refs/BMJ_UStG_14_Rechnungen.md lines 8-14"
    confidence: high
    claim_label: source_backed_summary

  - claim_id: C003
    claim: "For domestic B2B services, §14 UStG generally requires electronic invoices when both supplier and recipient are domestic Unternehmer."
    source_pointer: "raw/refs/BMJ_UStG_14_Rechnungen.md lines 16-22"
    confidence: high
    claim_label: source_backed_summary

  - claim_id: C004
    claim: "The required invoice-field set includes names and addresses, tax number or VAT ID, issue date, sequential invoice number, quantity/type or service scope, service time, fee split by tax rate or exemption, VAT rate/tax amount or exemption note, and selected special notices."
    source_pointer: "raw/refs/BMJ_UStG_14_Rechnungen.md lines 37-69"
    confidence: high
    claim_label: source_backed_summary

  - claim_id: C005
    claim: "For invoices with a total amount not exceeding 250 EUR, §33 UStDV allows a reduced minimum field set."
    source_pointer: "raw/refs/BMJ_UStDV_33_Kleinbetragsrechnungen.md lines 7-22"
    confidence: high
    claim_label: source_backed_summary

  - claim_id: C006
    claim: "The BMF FAQ states that, from 2025, a simple PDF is no longer an E-Rechnung because it lacks a structured format."
    source_pointer: "raw/refs/BMF_FAQ-E-Rechnung.md lines 53-63"
    confidence: medium
    claim_label: source_backed_summary

  - claim_id: C007
    claim: "The BMF FAQ distinguishes a Verein’s entrepreneurial and non-entrepreneurial areas; E-Rechnung duties apply to the entrepreneurial area."
    source_pointer: "raw/refs/BMF_FAQ-E-Rechnung.md lines 1-7 in fetched continuation"
    confidence: medium
    claim_label: source_backed_summary

  - claim_id: C008
    claim: "The AWV Belegablage source frames ordered and secure receipt custody as a basis for evidentiary strength of bookkeeping and records."
    source_pointer: "raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.md lines 39-53"
    confidence: medium
    claim_label: source_backed_summary
```

## concepts

```yaml
concepts:
  - concept_slug: invoice-core-fields
    label: "Mandatory invoice fields"
    source_refs:
      - "raw/refs/BMJ_UStG_14_Rechnungen.md"
    phase2_value: high

  - concept_slug: kleinbetragsrechnung
    label: "Small-value invoice up to 250 EUR"
    source_refs:
      - "raw/refs/BMJ_UStDV_33_Kleinbetragsrechnungen.md"
    phase2_value: high

  - concept_slug: e-rechnung-verein
    label: "E-Rechnung obligations for associations"
    source_refs:
      - "raw/refs/BMF_FAQ-E-Rechnung.md"
    phase2_value: high

  - concept_slug: belegablage-verfahrensdokumentation
    label: "Receipt custody procedure documentation"
    source_refs:
      - "raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.md"
    phase2_value: high
```

## entities

```yaml
entities:
  - entity_slug: bmf
    entity_label: "Bundesministerium der Finanzen"
    entity_type: organization
    source_refs:
      - "raw/refs/BMF_FAQ-E-Rechnung.md"
      - "raw/refs/BMF_GoBD-2024.md"

  - entity_slug: bmj-gesetze-im-internet
    entity_label: "BMJ / Gesetze im Internet"
    entity_type: organization
    source_refs:
      - "raw/refs/BMJ_UStG_14_Rechnungen.md"
      - "raw/refs/BMJ_UStDV_33_Kleinbetragsrechnungen.md"

  - entity_slug: awv
    entity_label: "Arbeitsgemeinschaft für wirtschaftliche Verwaltung e.V."
    entity_type: organization
    source_refs:
      - "raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.md"
```

## obligations_or_process_implications

```yaml
obligations_or_process_implications:
  - implication_id: O001
    implication: "Create a Lika invoice checklist with separate full-invoice and Kleinbetragsrechnung paths."
    source_refs:
      - "raw/refs/BMJ_UStG_14_Rechnungen.md"
      - "raw/refs/BMJ_UStDV_33_Kleinbetragsrechnungen.md"

  - implication_id: O002
    implication: "Create an e-invoice readiness decision tree: B2B domestic Unternehmer area, non-entrepreneurial Verein area, B2C tickets, B2G cases, exceptions, transition periods."
    source_refs:
      - "raw/refs/BMF_FAQ-E-Rechnung.md"
      - "raw/refs/BMJ_UStG_14_Rechnungen.md"

  - implication_id: O003
    implication: "Create a Belegablage SOP covering Belegeingang, identification, completeness, ordering system, access protection, handoff to bookkeeping/tax advisor, retention, and deletion."
    source_refs:
      - "raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.md"

  - implication_id: O004
    implication: "Do not use `raw/refs/BMF_GoBD-2024.md` as substantive evidence until a cleaned snapshot or PDF-derived text is available."
    source_refs:
      - "raw/refs/BMF_GoBD-2024.md"
      - "log/web-clutter-audit_20260629_162739.md"
```

## contradictions_or_uncertainties

```yaml
contradictions_or_uncertainties:
  - id: U001
    issue: "The BMF GoBD markdown capture is mostly web boilerplate; it should not be used as a GoBD semantic authority in current form."
    source_refs:
      - "raw/refs/BMF_GoBD-2024.md"
      - "log/web-clutter-audit_20260629_162739.md"
    proposed_handling: "create_cleaned_snapshot_or_use_pdf"

  - id: U002
    issue: "E-Rechnung applicability to concrete Lika workflows depends on whether the Verein acts in its entrepreneurial area, whether the counterparty is Unternehmer, and whether exceptions/transition periods apply."
    source_refs:
      - "raw/refs/BMF_FAQ-E-Rechnung.md"
      - "raw/refs/BMJ_UStG_14_Rechnungen.md"
    proposed_handling: "phase2_decision_tree"
```

## open_questions

```yaml
open_questions:
  - question_id: Q001
    question: "Which Lika activities are explicitly entrepreneurial versus non-entrepreneurial for E-Rechnung purposes?"
    proposed_handling: audit_item

  - question_id: Q002
    question: "Should Lika preserve E-Rechnung XML plus human-readable rendering, and where is that process documented?"
    proposed_handling: planning_task_candidate

  - question_id: Q003
    question: "Which source should become the canonical GoBD authority after BMF capture cleanup?"
    proposed_handling: ask_operator
```

## recommended_phase2_wiki_pages

```yaml
recommended_phase2_wiki_pages:
  - "wiki/concepts/invoice-core-fields.md"
  - "wiki/concepts/kleinbetragsrechnung.md"
  - "wiki/concepts/e-rechnung-verein.md"
  - "wiki/concepts/belegablage-verfahrensdokumentation.md"
  - "wiki/summaries/core-tax-law-invoicing-gobd.md"
  - "wiki/entities/bmf.md"
  - "wiki/entities/bmj-gesetze-im-internet.md"
  - "wiki/entities/awv.md"
```

## audit_flags

```yaml
audit_flags:
  - flag_id: A001
    severity: high
    issue: "BMF GoBD markdown is high-noise and should not be relied on for legal-process claims."
    source_ref: "raw/refs/BMF_GoBD-2024.md"
    recommended_action: "create_cleaned_snapshot"

  - flag_id: A002
    severity: medium
    issue: "Existing placeholder analysis files in ingest-analysis/ were not substantive."
    source_ref: "ingest-analysis/bmf_faq-e-rechnung.analysis.md"
    recommended_action: "replace_or_supersede_with_group_analysis"
```

## source_refs

```yaml
source_refs:
  - "raw/refs/BMJ_UStG_14_Rechnungen.md"
  - "raw/refs/BMJ_UStDV_33_Kleinbetragsrechnungen.md"
  - "raw/refs/BMF_FAQ-E-Rechnung.md"
  - "raw/refs/BMF_GoBD-2024.md"
  - "raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.md"
  - "log/web-clutter-audit_20260629_162739.md"
```

## confidence

```yaml
confidence: medium
rationale:
  - "Strong statutory sources inspected for invoice and small invoice requirements."
  - "Strong AWV process source inspected for Belegablage."
  - "BMF GoBD source capture is unusable until cleanup."
  - "Not all related sources were read end-to-end."
```

## stop_status

```yaml
stop_status:
  phase: ingest_phase_1
  status: operator_review_needed
  phase_2_allowed: false
  phase_2_requires: "approve ingest"
```
