## Missing-file / access status

No hard stop. I could read the installed Apex KB contract, deterministic lifecycle outputs, Phase 0 reports, source manifest segments, and selected high-signal source files. I did **not** read all 95/103 sources end-to-end in this response. The artifacts below are therefore **grouped Phase 1 ingest analyses** grounded in inspected source excerpts and Phase 0 navigation, with uninspected or noisy sources explicitly flagged.

The deterministic run confirms: clean pre-run state, 35 manifest entries before delta, 60 delta records added, 103 raw source candidates scanned, Phase 0 artifacts written, no Phase 2/wiki files modified, and a stop before LLM semantic ingest.

---

# Ingest-analysis artifact 1

Path:

```text
apex-meta/kb/lika-verein-taxes-accounting/ingest-analysis/group-1-core-tax-law.analysis.md
```

````markdown
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

````

---

# Ingest-analysis artifact 2

Path:

```text
apex-meta/kb/lika-verein-taxes-accounting/ingest-analysis/group-2-association-accounting.analysis.md
````

````markdown
---
title: "Association Accounting, Bookkeeping, Receipts, Reimbursements"
page_type: ingest_analysis
kb_slug: lika-verein-taxes-accounting
phase: ingest_phase_1
status: operator_review_needed
source_refs:
  - "raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.md"
  - "raw/notes/JudgementOfSources.md"
  - "raw/refs/DATEV_SKR42-Kontenrahmen.md"
  - "raw/refs/DATEV_Verfahrensdokumentation-GoBD.md"
  - "raw/refs/DeutschesEhrenamt_Rechnungslegung-Verein.md"
created_at: "2026-06-29T17:30:00Z"
updated_at: "2026-06-29T17:30:00Z"
confidence: medium
claim_label: source_grounded_analysis
phase_2_allowed: false
phase_2_requires: "approve ingest"
---

# Association Accounting, Bookkeeping, Receipts, Reimbursements

## source_scope

This group covers operational accounting custody: receipt classification, retention, scan/digital-original handling, process documentation, reimbursement records, EÜR/account assignment candidates, and source ranking for accounting workflows.

## source_quality_notes

```yaml
source_quality_notes:
  - source: "raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.md"
    clutter_status: moderate_noise
    usable_sections:
      - "0.1 Hinweise zum Inhalt und Anwendung"
      - "2.1 Zielsetzung und Anwendungsbereich"
      - "2.3 Rechtliche Grundlagen"
      - "2.4 Relevante Unterlagen mit Belegfunktion"
    suspected_noise_sections:
      - "PDF headers"
      - "table-of-contents artifacts"
    confidence_effect: lowered
    recommended_action: use_with_caution

  - source: "raw/notes/JudgementOfSources.md"
    clutter_status: clean
    usable_sections:
      - "Executive Summary"
      - "Canonical source list"
      - "Duplicate resolution"
      - "Ranking by groups"
    suspected_noise_sections: []
    confidence_effect: none
    recommended_action: use_as_operator_research_meta_source

  - source: "raw/refs/DATEV_SKR42-Kontenrahmen.md"
    clutter_status: high_noise
    usable_sections:
      - "keyword/topic presence only"
    suspected_noise_sections:
      - "high-volume web capture"
    confidence_effect: severe
    recommended_action: create_cleaned_snapshot_or_use_selectively

  - source: "raw/refs/DATEV_Verfahrensdokumentation-GoBD.md"
    clutter_status: high_noise
    usable_sections:
      - "topic presence only"
    suspected_noise_sections:
      - "high-volume web capture"
    confidence_effect: severe
    recommended_action: create_cleaned_snapshot_or_use_selectively
````

## relevance_summary

The accounting group is not mainly about legal interpretation. Its Phase 2 value is process architecture: what must be captured, where evidence lives, how documents remain complete, and how source data moves from payment/ticketing/email into bookkeeping.

The strongest inspected source is AWV. The operator/source-ranking note identifies DATEV, AWV, BMF, and BMJ/BZSt/KSK/DRV as the stronger source family, but it is a meta-source, not a legal authority.

## key_claims

```yaml
key_claims:
  - claim_id: C001
    claim: "A geordnete und sichere Belegablage is framed as the basis for the evidentiary strength of conventional or IT-supported bookkeeping and other retention duties."
    source_pointer: "raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.md lines 39-45"
    confidence: medium
    claim_label: source_backed_summary

  - claim_id: C002
    claim: "AWV states that retention-relevant records, including receipts, should be filed systematically, completely, timely, orderly, and unchanged, including digital and digitized receipts."
    source_pointer: "raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.md lines 47-53"
    confidence: medium
    claim_label: source_backed_summary

  - claim_id: C003
    claim: "AWV says the procedure should cover the full workflow from receipt creation or receipt entry and identification through orderly secure filing to destruction after retention periods."
    source_pointer: "raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.md lines 51-55"
    confidence: medium
    claim_label: source_backed_summary

  - claim_id: C004
    claim: "The AWV legal-basis section states 10-year retention for books, inventories, financial statements, organizational documents required to understand them, and Buchungsbelege."
    source_pointer: "raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.md lines 81-86"
    confidence: medium
    claim_label: source_backed_summary

  - claim_id: C005
    claim: "The operator source-evaluation note rates the source basis as usable but not playbook-ready and flags venue settlement, minimum bar revenue, 7%-vs-19% ticket VAT, and event-ticket invoice status as unresolved gaps."
    source_pointer: "raw/notes/JudgementOfSources.md lines 3-20"
    confidence: medium
    claim_label: source_backed_summary
```

## concepts

```yaml
concepts:
  - concept_slug: belegfunktion
    label: "Documents with receipt/evidence function"
    source_refs:
      - "raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.md"

  - concept_slug: accounting-source-custody
    label: "Accounting source custody workflow"
    source_refs:
      - "raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.md"

  - concept_slug: reimbursement-evidence
    label: "Reimbursement and expense evidence"
    source_refs:
      - "raw/notes/JudgementOfSources.md"
```

## entities

```yaml
entities:
  - entity_slug: datev
    entity_label: "DATEV"
    entity_type: organization
    source_refs:
      - "raw/refs/DATEV_SKR42-Kontenrahmen.md"
      - "raw/refs/DATEV_Verfahrensdokumentation-GoBD.md"

  - entity_slug: deutsches-ehrenamt
    entity_label: "Deutsches Ehrenamt"
    entity_type: organization
    source_refs:
      - "raw/refs/DeutschesEhrenamt_Rechnungslegung-Verein.md"

  - entity_slug: awv
    entity_label: "AWV"
    entity_type: organization
    source_refs:
      - "raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.md"
```

## obligations_or_process_implications

```yaml
obligations_or_process_implications:
  - implication_id: O001
    implication: "Create an accounting source-custody SOP before Phase 2 content is used as an operational playbook."
    source_refs:
      - "raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.md"

  - implication_id: O002
    implication: "Separate legal authority pages from internal process pages; the current source base contains both primary/legal sources and operator/meta-research notes."
    source_refs:
      - "raw/notes/JudgementOfSources.md"

  - implication_id: O003
    implication: "Treat SKR42/DATEV captures as potentially valuable but not yet clean enough for detailed account mapping claims."
    source_refs:
      - "raw/refs/DATEV_SKR42-Kontenrahmen.md"
      - "manifests/phase0/source-priority-candidates.md"
```

## contradictions_or_uncertainties

```yaml
contradictions_or_uncertainties:
  - id: U001
    issue: "Association-accounting sources may assume gemeinnützigkeit, while operator note says Lika/Safer Space is not gemeinnützig and has economic business operations."
    source_refs:
      - "raw/notes/JudgementOfSources.md"
    proposed_handling: "mark all gemeinnuetzigkeit-specific pages as conditional/not directly transferable"

  - id: U002
    issue: "DATEV SKR42 and DATEV GoBD sources appear important but require cleaned extraction before detailed account/process claims."
    source_refs:
      - "raw/refs/DATEV_SKR42-Kontenrahmen.md"
      - "raw/refs/DATEV_Verfahrensdokumentation-GoBD.md"
    proposed_handling: "create_cleaned_snapshot"
```

## open_questions

```yaml
open_questions:
  - question_id: Q001
    question: "Which exact chart of accounts or SKR42 subset will Lika use?"
    proposed_handling: planning_task_candidate

  - question_id: Q002
    question: "Which receipts are retained as original digital files, which as scans, and which as paper originals?"
    proposed_handling: audit_item

  - question_id: Q003
    question: "Which reimbursements are internal volunteer reimbursements versus contractor payments?"
    proposed_handling: ask_operator
```

## recommended_phase2_wiki_pages

```yaml
recommended_phase2_wiki_pages:
  - "wiki/concepts/belegfunktion.md"
  - "wiki/concepts/accounting-source-custody.md"
  - "wiki/concepts/reimbursement-evidence.md"
  - "wiki/summaries/association-accounting-process.md"
  - "wiki/entities/datev.md"
  - "wiki/entities/deutsches-ehrenamt.md"
```

## audit_flags

```yaml
audit_flags:
  - flag_id: A001
    severity: high
    issue: "Do not treat sources written for gemeinnützige Vereine as automatically applicable to a non-profit/non-gemeinnützig or economic-activity context."
    source_ref: "raw/notes/JudgementOfSources.md"

  - flag_id: A002
    severity: medium
    issue: "Need clean DATEV extraction before mapping account logic."
    source_ref: "raw/refs/DATEV_SKR42-Kontenrahmen.md"
```

## source_refs

```yaml
source_refs:
  - "raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.md"
  - "raw/notes/JudgementOfSources.md"
  - "raw/refs/DATEV_SKR42-Kontenrahmen.md"
  - "raw/refs/DATEV_Verfahrensdokumentation-GoBD.md"
```

## confidence

```yaml
confidence: medium
rationale:
  - "AWV source is substantively useful but PDF-conversion artifacts lower exactness."
  - "Operator/source-ranking note is useful for scoping but not legal authority."
  - "DATEV sources were not read sufficiently for fine account-mapping claims."
```

## stop_status

```yaml
stop_status:
  phase: ingest_phase_1
  status: operator_review_needed
  phase_2_allowed: false
  phase_2_requires: "approve ingest"
```

````

---

# Ingest-analysis artifact 3

Path:

```text
apex-meta/kb/lika-verein-taxes-accounting/ingest-analysis/group-3-events-vat-tickets.analysis.md
````

````markdown
---
title: "Events, VAT, Tickets, Presale Fees, Ticketing Providers"
page_type: ingest_analysis
kb_slug: lika-verein-taxes-accounting
phase: ingest_phase_1
status: operator_review_needed
source_refs:
  - "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md"
  - "raw/refs/BFH_V-R-16-09_Vorverkaufsgebuehr.md"
  - "raw/refs/pretix_Taxes-Guide.md"
  - "raw/refs/pretix_Order-Lifecycle.md"
  - "raw/refs/Eventbrite_Umsatzuebersicht-Export.md"
  - "raw/refs/ticketio_Event-Controlling-Reporting.md"
created_at: "2026-06-29T17:30:00Z"
updated_at: "2026-06-29T17:30:00Z"
confidence: medium
claim_label: source_grounded_analysis
phase_2_allowed: false
phase_2_requires: "approve ingest"
---

# Events, VAT, Tickets, Presale Fees, Ticketing Providers

## source_scope

This group covers event/festival revenues and expenses, association business-area assignment, ticket/VAT treatment, ticketing-system tax configuration, payout/reporting, presale-fee questions, and provider-specific reconciliation.

## source_quality_notes

```yaml
source_quality_notes:
  - source: "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md"
    clutter_status: moderate_noise
    usable_sections:
      - "business-area assignment"
      - "Umsatzsteuer event treatment"
      - "Kleinunternehmerregelung"
      - "Vorsteuer"
      - "foreign artists VAT / reverse-charge-like risk"
      - "§50a notes"
    suspected_noise_sections:
      - "table extraction artifacts"
      - "page headers"
      - "omitted pictures"
    confidence_effect: lowered_for_table_sensitive_claims
    recommended_action: use_with_caution

  - source: "raw/refs/pretix_Taxes-Guide.md"
    clutter_status: clean
    usable_sections:
      - "tax rules"
      - "tax included in price"
      - "custom tax rules"
      - "reverse charge warning"
      - "product tax assignment"
    suspected_noise_sections:
      - "documentation UI wording"
    confidence_effect: none
    recommended_action: use_as_provider_configuration_source

  - source: "raw/refs/Eventbrite_Umsatzuebersicht-Export.md"
    clutter_status: not_inspected_in_detail
    usable_sections: []
    suspected_noise_sections: []
    confidence_effect: lowered
    recommended_action: inspect_before_phase2

  - source: "raw/refs/ticketio_Event-Controlling-Reporting.md"
    clutter_status: not_inspected_in_detail
    usable_sections: []
    suspected_noise_sections: []
    confidence_effect: lowered
    recommended_action: inspect_before_phase2
````

## relevance_summary

The LfSt Bayern event source is the strongest inspected source for association event-tax structure. It gives a practical classification framework for event income/expenses across ideeller Bereich, Vermögensverwaltung, Zweckbetrieb, and steuerpflichtiger wirtschaftlicher Geschäftsbetrieb. It also directly addresses VAT, Kleinunternehmer thresholds, Vorsteuer, and foreign artists.

The pretix source is useful only for software configuration and operational reconciliation; it explicitly says it is not legal or financial advice. Therefore, Phase 2 must separate “tax-law decision” pages from “ticketing-system configuration” pages.

## key_claims

```yaml
key_claims:
  - claim_id: C001
    claim: "LfSt Bayern states that associations generally need to assign event revenues and expenses to four areas: ideeller Bereich, Vermögensverwaltung, Zweckbetrieb, and steuerpflichtiger wirtschaftlicher Geschäftsbetrieb."
    source_pointer: "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md lines 76-84"
    confidence: medium
    claim_label: source_backed_summary

  - claim_id: C002
    claim: "LfSt Bayern says event income and expenses must be recorded individually and may not be simply netted/salded."
    source_pointer: "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md lines 80-83"
    confidence: medium
    claim_label: source_backed_summary

  - claim_id: C003
    claim: "The LfSt table classifies several event-revenue types differently; for example, entrance into a festival tent can be wirtschaftlicher Geschäftsbetrieb, while some purpose-related participation/festival-marker cases can be Zweckbetrieb."
    source_pointer: "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md lines 96-155"
    confidence: low
    claim_label: source_backed_summary

  - claim_id: C004
    claim: "LfSt Bayern states that, for event VAT, association revenue in Vermögensverwaltung, Zweckbetrieb, and steuerpflichtiger wirtschaftlicher Geschäftsbetrieb belongs to the association’s enterprise area, while ideeller Bereich is non-entrepreneurial."
    source_pointer: "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md lines 19-33 in fetched continuation"
    confidence: medium
    claim_label: source_backed_summary

  - claim_id: C005
    claim: "LfSt Bayern states that non-exempt economic-business revenues are taxable at 19%, while non-exempt revenues of Zweckbetrieb and Vermögensverwaltung can be subject to 7%."
    source_pointer: "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md lines 29-33 in fetched continuation"
    confidence: medium
    claim_label: source_backed_summary

  - claim_id: C006
    claim: "The LfSt source gives 2025 Kleinunternehmer thresholds of 25,000 EUR prior-year net revenue and 100,000 EUR current-year net revenue."
    source_pointer: "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md lines 35-59 in fetched continuation"
    confidence: medium
    claim_label: source_backed_summary

  - claim_id: C007
    claim: "pretix tax rules are configured per event and assigned to products; pretix warns that its documentation is not legal or financial advice."
    source_pointer: "raw/refs/pretix_Taxes-Guide.md lines 14-23 and 28-35"
    confidence: high
    claim_label: source_backed_summary

  - claim_id: C008
    claim: "pretix defaults to treating configured product prices as gross prices when the tax-included setting is active."
    source_pointer: "raw/refs/pretix_Taxes-Guide.md lines 46-56"
    confidence: high
    claim_label: source_backed_summary
```

## concepts

```yaml
concepts:
  - concept_slug: event-business-area-assignment
    label: "Event revenue and expense assignment to association areas"
    source_refs:
      - "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md"

  - concept_slug: event-vat-rate-risk
    label: "7% versus 19% VAT risk for mixed cultural/club events"
    source_refs:
      - "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md"
      - "raw/notes/JudgementOfSources.md"

  - concept_slug: ticketing-tax-configuration
    label: "Ticketing tax rules in pretix/Eventbrite/ticket.io"
    source_refs:
      - "raw/refs/pretix_Taxes-Guide.md"
      - "raw/refs/Eventbrite_Umsatzuebersicht-Export.md"
      - "raw/refs/ticketio_Event-Controlling-Reporting.md"

  - concept_slug: ticket-as-invoice-gap
    label: "Ticket as invoice / ticket receipt evidentiary gap"
    source_refs:
      - "raw/notes/JudgementOfSources.md"
      - "raw/refs/BMJ_UStDV_33_Kleinbetragsrechnungen.md"
```

## entities

```yaml
entities:
  - entity_slug: lfst-bayern
    entity_label: "Bayerisches Landesamt für Steuern"
    entity_type: organization
    source_refs:
      - "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md"

  - entity_slug: pretix
    entity_label: "pretix"
    entity_type: tool
    source_refs:
      - "raw/refs/pretix_Taxes-Guide.md"
      - "raw/refs/pretix_Order-Lifecycle.md"

  - entity_slug: eventbrite
    entity_label: "Eventbrite"
    entity_type: tool
    source_refs:
      - "raw/refs/Eventbrite_Umsatzuebersicht-Export.md"

  - entity_slug: ticketio
    entity_label: "ticket.io"
    entity_type: tool
    source_refs:
      - "raw/refs/ticketio_Event-Controlling-Reporting.md"
```

## obligations_or_process_implications

```yaml
obligations_or_process_implications:
  - implication_id: O001
    implication: "Build an event settlement model that captures each revenue/expense type separately and assigns it to association area before VAT/accounting treatment."
    source_refs:
      - "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md"

  - implication_id: O002
    implication: "Ticketing provider tax settings must not be used as legal authority; they implement a tax decision made elsewhere."
    source_refs:
      - "raw/refs/pretix_Taxes-Guide.md"

  - implication_id: O003
    implication: "Phase 2 should include a clear warning that 7%-vs-19% ticket VAT and mixed event formats remain tax-advisor review fields."
    source_refs:
      - "raw/notes/JudgementOfSources.md"
      - "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md"
```

## contradictions_or_uncertainties

```yaml
contradictions_or_uncertainties:
  - id: U001
    issue: "The LfSt Bayern event source is focused on Festveranstaltungen, often in gemeinnützigkeits contexts; transfer to a non-gemeinnützig cultural/club event may be limited."
    source_refs:
      - "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md"
      - "raw/notes/JudgementOfSources.md"
    proposed_handling: "phase2_warning_and_tax_advisor_review"

  - id: U002
    issue: "Provider reports and tax rules may support reconciliation, but they do not decide the correct tax treatment."
    source_refs:
      - "raw/refs/pretix_Taxes-Guide.md"
    proposed_handling: "separate_provider_configuration_from_tax_law"
```

## open_questions

```yaml
open_questions:
  - question_id: Q001
    question: "Are Lika events economically operated as taxable wirtschaftlicher Geschäftsbetrieb, cultural Zweckbetrieb, or another category?"
    proposed_handling: audit_item

  - question_id: Q002
    question: "Which ticket products exist: entrance, donation, membership, merchandise, presale fee, service fee, refund, voucher?"
    proposed_handling: planning_task_candidate

  - question_id: Q003
    question: "Can a ticket or platform receipt satisfy invoice/minimum invoice evidence requirements in the specific Lika workflow?"
    proposed_handling: audit_item
```

## recommended_phase2_wiki_pages

```yaml
recommended_phase2_wiki_pages:
  - "wiki/concepts/event-business-area-assignment.md"
  - "wiki/concepts/event-vat-rate-risk.md"
  - "wiki/concepts/ticketing-tax-configuration.md"
  - "wiki/concepts/ticket-as-invoice-gap.md"
  - "wiki/summaries/events-vat-tickets.md"
  - "wiki/entities/lfst-bayern.md"
  - "wiki/entities/pretix.md"
  - "wiki/entities/eventbrite.md"
  - "wiki/entities/ticketio.md"
```

## audit_flags

```yaml
audit_flags:
  - flag_id: A001
    severity: high
    issue: "7% versus 19% for Lika’s mixed cultural/club event format remains unresolved."
    source_ref: "raw/notes/JudgementOfSources.md"

  - flag_id: A002
    severity: high
    issue: "Ticket-as-invoice evidence is not settled by inspected sources."
    source_ref: "raw/notes/JudgementOfSources.md"

  - flag_id: A003
    severity: medium
    issue: "LfSt Bayern table-heavy conversion may distort exact rows; table-sensitive claims need PDF/manual review."
    source_ref: "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md"
```

## source_refs

```yaml
source_refs:
  - "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md"
  - "raw/refs/BFH_V-R-16-09_Vorverkaufsgebuehr.md"
  - "raw/refs/pretix_Taxes-Guide.md"
  - "raw/refs/pretix_Order-Lifecycle.md"
  - "raw/refs/Eventbrite_Umsatzuebersicht-Export.md"
  - "raw/refs/ticketio_Event-Controlling-Reporting.md"
  - "raw/notes/JudgementOfSources.md"
```

## confidence

```yaml
confidence: medium
rationale:
  - "LfSt source is high-value but table-heavy."
  - "pretix source is clean but explicitly not legal advice."
  - "Eventbrite/ticket.io sources were not inspected deeply enough for final claims."
```

## stop_status

```yaml
stop_status:
  phase: ingest_phase_1
  status: operator_review_needed
  phase_2_allowed: false
  phase_2_requires: "approve ingest"
```

````

---

# Ingest-analysis artifact 4

Path:

```text
apex-meta/kb/lika-verein-taxes-accounting/ingest-analysis/group-4-artist-contractor-obligations.analysis.md
````

````markdown
---
title: "Artists, Contractors, KSK, Foreign Artists, §50a, Reverse Charge"
page_type: ingest_analysis
kb_slug: lika-verein-taxes-accounting
phase: ingest_phase_1
status: operator_review_needed
source_refs:
  - "raw/refs/DRV_K5001_Kuenstlersozialabgabe.md"
  - "raw/refs/KSK_Info04_Abgabepflicht-Veranstalter.md"
  - "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md"
  - "raw/refs/BZSt_50a-Abzugsteuer.md"
  - "raw/refs/DRV_Minijob-Kurzfristige-Beschaeftigung.md"
created_at: "2026-06-29T17:30:00Z"
updated_at: "2026-06-29T17:30:00Z"
confidence: medium
claim_label: source_grounded_analysis
phase_2_allowed: false
phase_2_requires: "approve ingest"
---

# Artists, Contractors, KSK, Foreign Artists, §50a, Reverse Charge

## source_scope

This group covers payments to artists, DJs, musicians, performers, designers, public-relations creatives, foreign artists, short-term/minijob-like crew, agency structures, KSK reporting, §50a withholding, and reverse-charge/VAT issues for foreign performers.

## source_quality_notes

```yaml
source_quality_notes:
  - source: "raw/refs/DRV_K5001_Kuenstlersozialabgabe.md"
    clutter_status: clean
    usable_sections:
      - "who is liable"
      - "bagatellgrenze"
      - "who is artist/publisher"
      - "calculation"
      - "which payments are included"
      - "contract clarity"
      - "monitoring"
    suspected_noise_sections:
      - "PDF page markers"
      - "omitted pictures"
    confidence_effect: none
    recommended_action: use_as_is

  - source: "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md"
    clutter_status: moderate_noise
    usable_sections:
      - "foreign artist VAT"
      - "§50a foreign artist tax deduction"
      - "Milderungsregelung"
    suspected_noise_sections:
      - "table/page extraction"
    confidence_effect: lowered
    recommended_action: use_with_caution

  - source: "raw/refs/BZSt_50a-Abzugsteuer.md"
    clutter_status: high_noise
    usable_sections:
      - "authority/source pointer only"
    suspected_noise_sections:
      - "navigation"
      - "cookie"
      - "page menu"
    confidence_effect: severe
    recommended_action: create_cleaned_snapshot
````

## relevance_summary

For Lika event accounting, artist/contractor payments are high-risk because a payment may create KSK obligations, withholding obligations for foreign artists, VAT/reverse-charge obligations, or employment/minijob classification issues. DRV K5001 is the strongest inspected KSK source. LfSt Bayern is directly relevant for event-specific foreign-artist VAT and §50a risks. BZSt is authoritative for §50a but the current capture is too noisy for detailed claims.

## key_claims

```yaml
key_claims:
  - claim_id: C001
    claim: "DRV K5001 states that private companies, public-law bodies, registered associations, and other groups can be liable for Künstlersozialabgabe."
    source_pointer: "raw/refs/DRV_K5001_Kuenstlersozialabgabe.md lines 13-16"
    confidence: high
    claim_label: source_backed_summary

  - claim_id: C002
    claim: "DRV K5001 states that tax-recognized gemeinnützigkeit does not remove Künstlersozialabgabe liability."
    source_pointer: "raw/refs/DRV_K5001_Kuenstlersozialabgabe.md lines 13-16"
    confidence: high
    claim_label: source_backed_summary

  - claim_id: C003
    claim: "DRV K5001 says Eigenwerber can be liable when they regularly commission self-employed artists or publicists for their own advertising/public-relations purposes."
    source_pointer: "raw/refs/DRV_K5001_Kuenstlersozialabgabe.md lines 39-44"
    confidence: high
    claim_label: source_backed_summary

  - claim_id: C004
    claim: "DRV K5001 states the annual de-minimis thresholds: 450 EUR through 2024, 700 EUR in 2025, and 1,000 EUR from 2026."
    source_pointer: "raw/refs/DRV_K5001_Kuenstlersozialabgabe.md lines 49-53"
    confidence: high
    claim_label: source_backed_summary

  - claim_id: C005
    claim: "DRV K5001 says the assessment base includes all annual payments for artistic/publishing services and generally includes reimbursed expenses/incidental costs, with specified exclusions if separately shown."
    source_pointer: "raw/refs/DRV_K5001_Kuenstlersozialabgabe.md lines 97-113"
    confidence: high
    claim_label: source_backed_summary

  - claim_id: C006
    claim: "DRV K5001 states that payments to foreign-resident artists/publicists are also recorded and reported."
    source_pointer: "raw/refs/DRV_K5001_Kuenstlersozialabgabe.md lines 119-128"
    confidence: high
    claim_label: source_backed_summary

  - claim_id: C007
    claim: "LfSt Bayern states that for foreign artists at a festival event, VAT may shift to the Verein as recipient if the artist’s fee is taxable under §13b UStG."
    source_pointer: "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md lines 87-94 in fetched continuation"
    confidence: medium
    claim_label: source_backed_summary

  - claim_id: C008
    claim: "LfSt Bayern states that a Verein may have to withhold and remit tax under §50a EStG on foreign artists’ fees, independent of the Verein’s own tax status."
    source_pointer: "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md lines 95-119 in fetched continuation"
    confidence: medium
    claim_label: source_backed_summary
```

## concepts

```yaml
concepts:
  - concept_slug: kuenstlersozialabgabe-event
    label: "Künstlersozialabgabe for event organizers"
    source_refs:
      - "raw/refs/DRV_K5001_Kuenstlersozialabgabe.md"
      - "raw/refs/KSK_Info04_Abgabepflicht-Veranstalter.md"

  - concept_slug: foreign-artist-50a
    label: "§50a withholding for foreign artists"
    source_refs:
      - "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md"
      - "raw/refs/BZSt_50a-Abzugsteuer.md"

  - concept_slug: artist-contract-source-of-truth
    label: "Contractual counterparty determines evidence and obligation route"
    source_refs:
      - "raw/refs/DRV_K5001_Kuenstlersozialabgabe.md"

  - concept_slug: foreign-artist-vat-recipient-liability
    label: "Foreign artist VAT / recipient liability"
    source_refs:
      - "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md"
```

## entities

```yaml
entities:
  - entity_slug: deutsche-rentenversicherung
    entity_label: "Deutsche Rentenversicherung"
    entity_type: organization
    source_refs:
      - "raw/refs/DRV_K5001_Kuenstlersozialabgabe.md"

  - entity_slug: kuenstlersozialkasse
    entity_label: "Künstlersozialkasse"
    entity_type: organization
    source_refs:
      - "raw/refs/KSK_Info04_Abgabepflicht-Veranstalter.md"
      - "raw/refs/DRV_K5001_Kuenstlersozialabgabe.md"

  - entity_slug: bzst
    entity_label: "Bundeszentralamt für Steuern"
    entity_type: organization
    source_refs:
      - "raw/refs/BZSt_50a-Abzugsteuer.md"

  - entity_slug: foreign-artist
    entity_label: "Foreign artist / foreign performer"
    entity_type: other
    source_refs:
      - "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md"
```

## obligations_or_process_implications

```yaml
obligations_or_process_implications:
  - implication_id: O001
    implication: "Create an artist-payment intake form capturing natural person vs legal entity, self-employed status, country of residence, agency/manager chain, service type, fee, reimbursed costs, VAT, and contract counterparty."
    source_refs:
      - "raw/refs/DRV_K5001_Kuenstlersozialabgabe.md"
      - "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md"

  - implication_id: O002
    implication: "Create a KSK annual tracking ledger for payments to self-employed artists/publicists."
    source_refs:
      - "raw/refs/DRV_K5001_Kuenstlersozialabgabe.md"

  - implication_id: O003
    implication: "Foreign artists require a separate §50a/VAT review workflow, not a normal domestic contractor workflow."
    source_refs:
      - "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md"
      - "raw/refs/BZSt_50a-Abzugsteuer.md"

  - implication_id: O004
    implication: "Contract templates should not attempt to allocate KSK liability contractually against statutory allocation; they should clarify factual and contractual relationships."
    source_refs:
      - "raw/refs/DRV_K5001_Kuenstlersozialabgabe.md"
```

## contradictions_or_uncertainties

```yaml
contradictions_or_uncertainties:
  - id: U001
    issue: "The BZSt §50a source is likely authoritative but current capture is too noisy for detailed semantic extraction."
    source_refs:
      - "raw/refs/BZSt_50a-Abzugsteuer.md"
      - "log/web-clutter-audit_20260629_162739.md"
    proposed_handling: "create_cleaned_snapshot"

  - id: U002
    issue: "Agency/manager/payment-chain cases can shift or complicate KSK analysis and need exact contract review."
    source_refs:
      - "raw/refs/DRV_K5001_Kuenstlersozialabgabe.md"
    proposed_handling: "audit_item"

  - id: U003
    issue: "Whether a foreign artist is VAT-exempt, Kleinunternehmer-like under §19(4), subject to 7%, 19%, or reverse-charge treatment requires case facts not present in the source corpus."
    source_refs:
      - "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md"
    proposed_handling: "tax_advisor_review_flag"
```

## open_questions

```yaml
open_questions:
  - question_id: Q001
    question: "Will Lika pay foreign artists, domestic self-employed artists, agencies, collectives, GmbHs, or private hobby/amateur performers?"
    proposed_handling: ask_operator

  - question_id: Q002
    question: "Which artist/contractor payments in 2025/2026 exceed the KSK bagatell thresholds?"
    proposed_handling: planning_task_candidate

  - question_id: Q003
    question: "Which payment records show separately stated VAT, travel costs, hospitality costs, GEMA, or other exclusions from KSK base?"
    proposed_handling: audit_item
```

## recommended_phase2_wiki_pages

```yaml
recommended_phase2_wiki_pages:
  - "wiki/concepts/kuenstlersozialabgabe-event.md"
  - "wiki/concepts/foreign-artist-50a.md"
  - "wiki/concepts/artist-contract-source-of-truth.md"
  - "wiki/concepts/foreign-artist-vat-recipient-liability.md"
  - "wiki/summaries/artist-contractor-obligations.md"
  - "wiki/entities/deutsche-rentenversicherung.md"
  - "wiki/entities/kuenstlersozialkasse.md"
  - "wiki/entities/bzst.md"
```

## audit_flags

```yaml
audit_flags:
  - flag_id: A001
    severity: high
    issue: "Foreign artist payment workflow must be separated from domestic contractor workflow."
    source_refs:
      - "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md"

  - flag_id: A002
    severity: high
    issue: "KSK capture requires annual payment ledger and contract-counterparty clarity."
    source_refs:
      - "raw/refs/DRV_K5001_Kuenstlersozialabgabe.md"

  - flag_id: A003
    severity: medium
    issue: "BZSt §50a source requires cleaned snapshot before Phase 2 detailed page."
    source_refs:
      - "raw/refs/BZSt_50a-Abzugsteuer.md"
```

## source_refs

```yaml
source_refs:
  - "raw/refs/DRV_K5001_Kuenstlersozialabgabe.md"
  - "raw/refs/KSK_Info04_Abgabepflicht-Veranstalter.md"
  - "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md"
  - "raw/refs/BZSt_50a-Abzugsteuer.md"
```

## confidence

```yaml
confidence: medium
rationale:
  - "DRV K5001 was clean and directly relevant."
  - "LfSt source was relevant but table/PDF conversion lowers precision."
  - "BZSt source is authoritative but current capture is noisy."
```

## stop_status

```yaml
stop_status:
  phase: ingest_phase_1
  status: operator_review_needed
  phase_2_allowed: false
  phase_2_requires: "approve ingest"
```

````

---

# Ingest-analysis artifact 5

Path:

```text
apex-meta/kb/lika-verein-taxes-accounting/ingest-analysis/group-5-internal-process-and-risk.analysis.md
````

````markdown
---
title: "Internal Process, Source Judgment, Open Risks"
page_type: ingest_analysis
kb_slug: lika-verein-taxes-accounting
phase: ingest_phase_1
status: operator_review_needed
source_refs:
  - "raw/notes/JudgementOfSources.md"
  - "raw/notes/GapResearch_claude.md"
  - "raw/notes/New_Research_Taxes_Accounting/Research2_gem.md"
  - "raw/notes/New_Research_Taxes_Accounting/Research2Fail_gpt.md"
  - "raw/notes/New_Research_Taxes_Accounting/Research3Tickets_gpt.md"
  - "raw/notes/New_Research_Taxes_Accounting/Research4_perpDR.md"
created_at: "2026-06-29T17:30:00Z"
updated_at: "2026-06-29T17:30:00Z"
confidence: medium
claim_label: source_grounded_analysis
phase_2_allowed: false
phase_2_requires: "approve ingest"
---

# Internal Process, Source Judgment, Open Risks

## source_scope

This group covers operator-supplied research notes, source evaluation, unresolved tax/accounting risks, prioritization, duplicate-resolution decisions, and KB source-custody strategy.

## source_quality_notes

```yaml
source_quality_notes:
  - source: "raw/notes/JudgementOfSources.md"
    clutter_status: clean
    usable_sections:
      - "Executive Summary"
      - "Canonical Sources"
      - "Duplicate Resolution"
      - "Group Ranking"
    suspected_noise_sections: []
    confidence_effect: none
    recommended_action: use_as_meta_source_not_legal_authority

  - source: "raw/notes/GapResearch_claude.md"
    clutter_status: not_inspected_in_detail
    usable_sections: []
    suspected_noise_sections: []
    confidence_effect: lowered
    recommended_action: inspect_before_phase2

  - source: "raw/notes/New_Research_Taxes_Accounting/Research2_gem.md"
    clutter_status: not_inspected_in_detail
    usable_sections: []
    suspected_noise_sections: []
    confidence_effect: lowered
    recommended_action: inspect_before_phase2
````

## relevance_summary

Internal notes should not become legal authority pages. Their value is source selection, issue framing, risk registers, and process design. `JudgementOfSources.md` is the strongest inspected internal source because it ranks sources, records duplicate decisions, and explicitly names unresolved gaps.

## key_claims

```yaml
key_claims:
  - claim_id: C001
    claim: "The source-evaluation note says the source base is usable but not yet playbook-ready."
    source_pointer: "raw/notes/JudgementOfSources.md lines 3-9"
    confidence: medium
    claim_label: source_backed_summary

  - claim_id: C002
    claim: "The same note identifies venue settlement / minimum bar revenue, concrete 7%-vs-19% VAT for club/DJ/cultural mixed formats, and ticket-as-invoice as the largest open gaps."
    source_pointer: "raw/notes/JudgementOfSources.md lines 3-20"
    confidence: medium
    claim_label: source_backed_summary

  - claim_id: C003
    claim: "The note warns that sources with gemeinnützigkeit, Zweckbetrieb, or donation logic are dangerous for direct transfer if the project is treated as non-gemeinnützig with economic business operations."
    source_pointer: "raw/notes/JudgementOfSources.md lines 5-8"
    confidence: medium
    claim_label: source_backed_summary

  - claim_id: C004
    claim: "The source list ranks §33 UStDV, KSK/DRV, BMF GoBD, AWV, BMF E-Rechnung, Finanzverwaltung NRW, pretix, Minijob, BZSt §50a, and LfSt Bayern among the key source families."
    source_pointer: "raw/notes/JudgementOfSources.md lines 67-107"
    confidence: medium
    claim_label: source_backed_summary
```

## concepts

```yaml
concepts:
  - concept_slug: source-authority-hierarchy
    label: "Source authority hierarchy"
    source_refs:
      - "raw/notes/JudgementOfSources.md"

  - concept_slug: transfer-safety
    label: "Transfer safety from generic association sources to Lika"
    source_refs:
      - "raw/notes/JudgementOfSources.md"

  - concept_slug: unresolved-tax-risk-register
    label: "Unresolved tax/accounting risk register"
    source_refs:
      - "raw/notes/JudgementOfSources.md"

  - concept_slug: venue-settlement-gap
    label: "Venue settlement and Mindestbarumsatz gap"
    source_refs:
      - "raw/notes/JudgementOfSources.md"
```

## entities

```yaml
entities:
  - entity_slug: lika-verein
    entity_label: "Lika Verein"
    entity_type: project
    source_refs:
      - "raw/notes/JudgementOfSources.md"

  - entity_slug: safer-space
    entity_label: "Safer Space"
    entity_type: project
    source_refs:
      - "raw/notes/JudgementOfSources.md"
```

## obligations_or_process_implications

```yaml
obligations_or_process_implications:
  - implication_id: O001
    implication: "Phase 2 must include an explicit authority hierarchy and transfer-safety warning on every page involving gemeinnützigkeit, Zweckbetrieb, donations, or association tax examples."
    source_refs:
      - "raw/notes/JudgementOfSources.md"

  - implication_id: O002
    implication: "Do not compile a practical playbook until the three high-risk gaps are either researched, marked as tax-advisor-only, or excluded."
    source_refs:
      - "raw/notes/JudgementOfSources.md"

  - implication_id: O003
    implication: "Phase 2 should generate an audit/risk register page before generating operational checklists."
    source_refs:
      - "raw/notes/JudgementOfSources.md"
```

## contradictions_or_uncertainties

```yaml
contradictions_or_uncertainties:
  - id: U001
    issue: "Some sources assume gemeinnützigkeit; project note says that transfer may be unsafe."
    source_refs:
      - "raw/notes/JudgementOfSources.md"
    proposed_handling: "transfer_safety_marker"

  - id: U002
    issue: "The source-evaluation note itself is not a legal authority; it should govern KB curation, not tax conclusions."
    source_refs:
      - "raw/notes/JudgementOfSources.md"
    proposed_handling: "page_type_meta_source"
```

## open_questions

```yaml
open_questions:
  - question_id: Q001
    question: "Is Lika actually non-gemeinnützig for all relevant event/tax workflows, or are any sub-activities tax-privileged?"
    proposed_handling: ask_operator

  - question_id: Q002
    question: "Should Phase 2 create a 'not legal advice / tax advisor review' banner template for high-risk pages?"
    proposed_handling: ask_operator

  - question_id: Q003
    question: "Which source gaps should be researched before Phase 2: venue settlement, VAT rate, ticket invoice, or foreign artist obligations?"
    proposed_handling: planning_task_candidate
```

## recommended_phase2_wiki_pages

```yaml
recommended_phase2_wiki_pages:
  - "wiki/concepts/source-authority-hierarchy.md"
  - "wiki/concepts/transfer-safety.md"
  - "wiki/concepts/unresolved-tax-risk-register.md"
  - "wiki/concepts/venue-settlement-gap.md"
  - "wiki/summaries/source-judgment-and-open-risks.md"
  - "wiki/entities/lika-verein.md"
  - "wiki/entities/safer-space.md"
```

## audit_flags

```yaml
audit_flags:
  - flag_id: A001
    severity: high
    issue: "Venue settlement / Mindestbarumsatz remains a major missing official-source area."
    source_ref: "raw/notes/JudgementOfSources.md"

  - flag_id: A002
    severity: high
    issue: "7% versus 19% for club/DJ/cultural mixed event formats remains unresolved."
    source_ref: "raw/notes/JudgementOfSources.md"

  - flag_id: A003
    severity: high
    issue: "Ticket-as-invoice remains only indirectly supported."
    source_ref: "raw/notes/JudgementOfSources.md"
```

## source_refs

```yaml
source_refs:
  - "raw/notes/JudgementOfSources.md"
  - "raw/notes/GapResearch_claude.md"
  - "raw/notes/New_Research_Taxes_Accounting/Research2_gem.md"
  - "raw/notes/New_Research_Taxes_Accounting/Research2Fail_gpt.md"
  - "raw/notes/New_Research_Taxes_Accounting/Research3Tickets_gpt.md"
  - "raw/notes/New_Research_Taxes_Accounting/Research4_perpDR.md"
```

## confidence

```yaml
confidence: medium
rationale:
  - "JudgementOfSources.md was inspected and is highly useful for source curation."
  - "Other internal research notes were inventoried but not analyzed end-to-end."
  - "Internal notes are not legal/tax authority."
```

## stop_status

```yaml
stop_status:
  phase: ingest_phase_1
  status: operator_review_needed
  phase_2_allowed: false
  phase_2_requires: "approve ingest"
```

````

---

# Ingest-analysis artifact 6

Path:

```text
apex-meta/kb/lika-verein-taxes-accounting/ingest-analysis/group-6-noisy-or-low-trust-sources.analysis.md
````

````markdown
---
title: "Noisy, Duplicate, Low-Trust, and Cleanup-Needed Sources"
page_type: ingest_analysis
kb_slug: lika-verein-taxes-accounting
phase: ingest_phase_1
status: operator_review_needed
source_refs:
  - "log/web-clutter-audit_20260629_162739.md"
  - "manifests/phase0/corpus-profile.md"
  - "manifests/phase0/source-priority-candidates.md"
  - "manifests/source-manifest.json"
created_at: "2026-06-29T17:30:00Z"
updated_at: "2026-06-29T17:30:00Z"
confidence: high
claim_label: source_grounded_analysis
phase_2_allowed: false
phase_2_requires: "approve ingest"
---

# Noisy, Duplicate, Low-Trust, and Cleanup-Needed Sources

## source_scope

This group covers web-clutter candidates, duplicate source files, table-heavy PDF conversion risks, manifest/source-inventory gaps, placeholder Phase 1 outputs, and source-quality handling before Phase 2.

## source_quality_notes

```yaml
source_quality_notes:
  - source: "log/web-clutter-audit_20260629_162739.md"
    clutter_status: clean
    usable_sections:
      - "top candidates"
      - "future script improvement"
    suspected_noise_sections: []
    confidence_effect: none
    recommended_action: use_as_filter_not_deletion_list

  - source: "manifests/phase0/corpus-profile.md"
    clutter_status: clean
    usable_sections:
      - "source inventory status"
      - "file counts"
      - "largest files"
      - "duplicate hash groups"
      - "source group summary"
    suspected_noise_sections: []
    confidence_effect: none
    recommended_action: use_as_phase0_navigation_source

  - source: "manifests/phase0/source-priority-candidates.md"
    clutter_status: clean
    usable_sections:
      - "deterministic priority candidates"
    suspected_noise_sections: []
    confidence_effect: none
    recommended_action: use_as_navigation_hint_not_authority_ranking
````

## relevance_summary

This group is essential because the corpus contains many duplicated `raw/notes/...` and `raw/refs/...` pairs, high-noise web captures, table-heavy conversions, and placeholder ingest-analysis files. Phase 2 should not begin until the operator decides whether cleaned snapshots are needed for BMF GoBD, BZSt §50a, Finanzamt NRW, DATEV, IHK pages, and other high-noise captures.

## key_claims

```yaml
key_claims:
  - claim_id: C001
    claim: "The web-clutter audit scanned 77 Markdown files and reported 69 candidates."
    source_pointer: "log/web-clutter-audit_20260629_162739.md lines 3-8"
    confidence: high
    claim_label: source_backed_summary

  - claim_id: C002
    claim: "The web-clutter audit marks AWV GoBD, BMF GoBD, Buergergesellschaft, DATEV, DRV Minijob, Finanzamt NRW, IHK Koblenz, VUT, Vereinswelt, and other sources as high-noise candidates with cookie/datenschutz/impressum/menu/navigation signals."
    source_pointer: "log/web-clutter-audit_20260629_162739.md lines 10-32"
    confidence: high
    claim_label: source_backed_summary

  - claim_id: C003
    claim: "The corpus profile reports no JSON or CSV source inventory present/readable, despite 103 files scanned."
    source_pointer: "manifests/phase0/corpus-profile.md lines 7-18"
    confidence: high
    claim_label: source_backed_summary

  - claim_id: C004
    claim: "The corpus profile reports 81 Markdown files, 16 JSON files, and 6 YAML files."
    source_pointer: "manifests/phase0/corpus-profile.md lines 20-24"
    confidence: high
    claim_label: source_backed_summary

  - claim_id: C005
    claim: "The corpus profile lists multiple duplicate hash groups between raw/notes/New_Research_Taxes_Accounting/HTML-MD and raw/refs equivalents."
    source_pointer: "manifests/phase0/corpus-profile.md lines 53-75"
    confidence: high
    claim_label: source_backed_summary

  - claim_id: C006
    claim: "The lifecycle run report flags three table-heavy PDF conversion risks: IHK Niederbayern Kleinbetragsrechnungen, LfSt Bayern Festveranstaltungen 2025, and AWV Muster-Verfahrensdokumentation Belegablage."
    source_pointer: "log/lifecycle-run-report_20260629_162739.md lines 45-50"
    confidence: high
    claim_label: source_backed_summary
```

## concepts

```yaml
concepts:
  - concept_slug: web-clutter-filter
    label: "Web clutter filter"
    source_refs:
      - "log/web-clutter-audit_20260629_162739.md"

  - concept_slug: duplicate-source-custody
    label: "Duplicate source custody"
    source_refs:
      - "manifests/phase0/corpus-profile.md"
      - "manifests/source-manifest.json"

  - concept_slug: table-heavy-pdf-risk
    label: "Table-heavy PDF extraction risk"
    source_refs:
      - "log/lifecycle-run-report_20260629_162739.md"

  - concept_slug: phase1-placeholder-replacement
    label: "Placeholder Phase 1 analysis replacement"
    source_refs:
      - "ingest-analysis/bmf_faq-e-rechnung.analysis.md"
```

## entities

```yaml
entities:
  - entity_slug: apex-kb-python-layer
    entity_label: "Apex KB deterministic Python layer"
    entity_type: tool
    source_refs:
      - "log/lifecycle-run-report_20260629_162739.md"

  - entity_slug: web-clutter-audit
    entity_label: "Web clutter audit"
    entity_type: artifact
    source_refs:
      - "log/web-clutter-audit_20260629_162739.md"

  - entity_slug: phase0-corpus-profile
    entity_label: "Phase 0 corpus profile"
    entity_type: artifact
    source_refs:
      - "manifests/phase0/corpus-profile.md"
```

## obligations_or_process_implications

```yaml
obligations_or_process_implications:
  - implication_id: O001
    implication: "Phase 2 should use canonical `raw/refs` copies over duplicate `raw/notes/New_Research_Taxes_Accounting/HTML-MD` copies unless the notes copy is explicitly needed."
    source_refs:
      - "manifests/phase0/corpus-profile.md"

  - implication_id: O002
    implication: "High-noise web captures should be excluded from Phase 2 substantive claims until cleaned or reviewed, but should remain in custody."
    source_refs:
      - "log/web-clutter-audit_20260629_162739.md"

  - implication_id: O003
    implication: "Table-heavy claims involving exact thresholds, rows, or category assignment should be verified against PDF/manual table review."
    source_refs:
      - "log/lifecycle-run-report_20260629_162739.md"

  - implication_id: O004
    implication: "Existing placeholder ingest-analysis files should be superseded by substantive group analyses or replaced by source-specific analyses later."
    source_refs:
      - "ingest-analysis/bmf_faq-e-rechnung.analysis.md"
```

## contradictions_or_uncertainties

```yaml
contradictions_or_uncertainties:
  - id: U001
    issue: "Phase 0 reported 'likely_generated_or_noise_files: none detected' while the separate web-clutter audit reports 69 candidates."
    source_refs:
      - "manifests/phase0/corpus-profile.md"
      - "log/web-clutter-audit_20260629_162739.md"
    proposed_handling: "treat phase0 profile as structural only; web-clutter audit as noise filter"

  - id: U002
    issue: "Source manifest has 95 entries after delta merge, but Phase 0 scanned 103 files and source-inventory JSON/CSV is absent."
    source_refs:
      - "log/lifecycle-run-report_20260629_162739.md"
      - "manifests/phase0/corpus-profile.md"
    proposed_handling: "deterministic_script_improvement"

  - id: U003
    issue: "Some source IDs exist as both PDF and extracted Markdown; semantic analysis should prefer extractable Markdown but mark table-sensitive claims for PDF verification."
    source_refs:
      - "manifests/source-manifest.json"
      - "log/lifecycle-run-report_20260629_162739.md"
    proposed_handling: "pdf_table_qc"
```

## open_questions

```yaml
open_questions:
  - question_id: Q001
    question: "Should cleaned snapshots be created before Phase 2 for every score=100 web-clutter candidate, or only for high-authority sources?"
    proposed_handling: ask_operator

  - question_id: Q002
    question: "Should Phase 1 produce one group-level analysis per topic, or also backfill one source-specific analysis per P0/P1 source?"
    proposed_handling: ask_operator

  - question_id: Q003
    question: "Should the source-manifest merge create source-inventory.json/csv as a standard deterministic artifact?"
    proposed_handling: planning_task_candidate
```

## recommended_phase2_wiki_pages

```yaml
recommended_phase2_wiki_pages:
  - "wiki/concepts/web-clutter-filter.md"
  - "wiki/concepts/duplicate-source-custody.md"
  - "wiki/concepts/table-heavy-pdf-risk.md"
  - "wiki/concepts/phase1-placeholder-replacement.md"
  - "wiki/summaries/source-quality-and-custody.md"
```

## audit_flags

```yaml
audit_flags:
  - flag_id: A001
    severity: high
    issue: "Do not use BMF GoBD markdown capture as semantic authority without cleanup."
    source_ref: "raw/refs/BMF_GoBD-2024.md"

  - flag_id: A002
    severity: high
    issue: "Do not use BZSt §50a capture for detailed claims without cleanup."
    source_ref: "raw/refs/BZSt_50a-Abzugsteuer.md"

  - flag_id: A003
    severity: medium
    issue: "Duplicate raw/notes and raw/refs sources should be resolved by canonical source policy before Phase 2."
    source_ref: "manifests/phase0/corpus-profile.md"

  - flag_id: A004
    severity: medium
    issue: "Table-heavy PDF conversion needs QC for LfSt Bayern, AWV, and IHK Niederbayern."
    source_ref: "log/lifecycle-run-report_20260629_162739.md"
```

## source_refs

```yaml
source_refs:
  - "log/web-clutter-audit_20260629_162739.md"
  - "manifests/phase0/corpus-profile.md"
  - "manifests/phase0/source-priority-candidates.md"
  - "manifests/source-manifest.json"
  - "log/lifecycle-run-report_20260629_162739.md"
  - "ingest-analysis/bmf_faq-e-rechnung.analysis.md"
```

## confidence

```yaml
confidence: high
rationale:
  - "This artifact mainly analyzes deterministic quality metadata, not tax law."
  - "Lifecycle, web clutter, and corpus profile reports were directly inspected."
```

## stop_status

```yaml
stop_status:
  phase: ingest_phase_1
  status: operator_review_needed
  phase_2_allowed: false
  phase_2_requires: "approve ingest"
```

````

---

# Final report

Path:

```text
apex-meta/kb/lika-verein-taxes-accounting/log/llm-phase1-report_20260629_173000.md
````

````markdown
---
title: "LLM Phase 1 Report - Lika Verein Taxes Accounting"
page_type: phase1_report
kb_slug: lika-verein-taxes-accounting
phase: ingest_phase_1
status: operator_review_needed
created_at: "2026-06-29T17:30:00Z"
updated_at: "2026-06-29T17:30:00Z"
confidence: medium
claim_label: source_grounded_analysis
phase_2_allowed: false
phase_2_requires: "approve ingest"
---

# LLM Phase 1 Report - Lika Verein Taxes Accounting

## execution_summary

Executed grouped LLM-owned Phase 1 semantic ingest analysis in chat for `apex-meta/kb/lika-verein-taxes-accounting/`.

No repo files were written. No Phase 2 wiki pages were generated. No GitHub PRs, issues, comments, reviewers, assignees, or external sharing were used.

The installed Apex KB contract confirms that Phase 1 creates semantic analysis under `ingest-analysis/` and must halt before Phase 2; Phase 2 requires the exact operator phrase `approve ingest`. The installed skill also defines the deterministic/LLM ownership split: Python owns scaffold/hash/manifest/Phase 0/index/lint/retrieval mechanics, while the LLM owns relevance judgment, source summary, concept extraction, entity synthesis, contradiction interpretation, Phase 1 analysis, and Phase 2 wiki drafting. 

## artifacts_created_in_chat

```yaml
artifacts_created_in_chat:
  - path: "apex-meta/kb/lika-verein-taxes-accounting/ingest-analysis/group-1-core-tax-law.analysis.md"
    status: chat_output_only
  - path: "apex-meta/kb/lika-verein-taxes-accounting/ingest-analysis/group-2-association-accounting.analysis.md"
    status: chat_output_only
  - path: "apex-meta/kb/lika-verein-taxes-accounting/ingest-analysis/group-3-events-vat-tickets.analysis.md"
    status: chat_output_only
  - path: "apex-meta/kb/lika-verein-taxes-accounting/ingest-analysis/group-4-artist-contractor-obligations.analysis.md"
    status: chat_output_only
  - path: "apex-meta/kb/lika-verein-taxes-accounting/ingest-analysis/group-5-internal-process-and-risk.analysis.md"
    status: chat_output_only
  - path: "apex-meta/kb/lika-verein-taxes-accounting/ingest-analysis/group-6-noisy-or-low-trust-sources.analysis.md"
    status: chat_output_only
  - path: "apex-meta/kb/lika-verein-taxes-accounting/log/llm-phase1-report_20260629_173000.md"
    status: chat_output_only
````

## sources_analyzed

```yaml
directly_inspected_sources:
  deterministic_outputs:
    - ".claude/skills/apex-kb/SKILL.md"
    - ".claude/skills/apex-kb/references/kb-contract.md"
    - ".claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md"
    - ".claude/skills/apex-kb/templates/ingest-analysis-template.md"
    - "log/lifecycle-run-report_20260629_162739.md"
    - "log/lifecycle-preflight-inventory_20260629_162739.md"
    - "log/web-clutter-audit_20260629_162739.md"
    - "manifests/source-manifest.json"
    - "manifests/source-manifest-deltas/source-manifest-delta_20260629_162739.jsonl"
    - "manifests/phase0/phase0-navigation-report.md"
    - "manifests/phase0/source-priority-candidates.md"
    - "manifests/phase0/corpus-profile.md"
    - "manifests/phase0/topic-file-map.json"

  source_files_sampled:
    - "raw/refs/BMJ_UStG_14_Rechnungen.md"
    - "raw/refs/BMJ_UStDV_33_Kleinbetragsrechnungen.md"
    - "raw/refs/BMF_FAQ-E-Rechnung.md"
    - "raw/refs/BMF_GoBD-2024.md"
    - "raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.md"
    - "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md"
    - "raw/refs/DRV_K5001_Kuenstlersozialabgabe.md"
    - "raw/refs/BZSt_50a-Abzugsteuer.md"
    - "raw/refs/pretix_Taxes-Guide.md"
    - "raw/refs/IHK-Koblenz_Reverse-Charge-Auslaendische-Dienstleister.md"
    - "raw/refs/FinanzamtNRW_Vereine-Umsatzsteuer.md"
    - "raw/notes/JudgementOfSources.md"
```

## sources_not_analyzed_and_why

```yaml
sources_not_analyzed_and_why:
  - reason: "Context and response budget; grouped Phase 1 strategy used instead of one-by-one analysis of all 95/103 sources."
    examples:
      - "most raw/notes/New_Research_Taxes_Accounting/HTML-MD duplicates"
      - "all provider pages not directly fetched"
      - "all YAML research source lists not directly parsed"

  - reason: "High-noise web captures; substantive use deferred until cleaned snapshots."
    examples:
      - "raw/refs/BMF_GoBD-2024.md"
      - "raw/refs/BZSt_50a-Abzugsteuer.md"
      - "raw/refs/FinanzamtNRW_Vereine-Umsatzsteuer.md"
      - "raw/refs/IHK-Koblenz_Reverse-Charge-Auslaendische-Dienstleister.md"

  - reason: "Table-heavy PDF conversion risk; exact table claims require PDF/manual review."
    examples:
      - "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md"
      - "raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.md"
      - "raw/refs/IHK-Niederbayern_Checkliste-Kleinbetragsrechnungen.md"
```

## source_quality_problems

```yaml
source_quality_problems:
  - issue: "No source-inventory JSON/CSV artifact exists."
    evidence: "manifests/phase0/corpus-profile.md"
    impact: "LLM must rely on manifest, corpus profile, and source-priority output rather than a richer inventory."

  - issue: "Large duplicate groups between raw/notes and raw/refs."
    evidence: "manifests/phase0/corpus-profile.md"
    impact: "Phase 2 needs canonical-source policy."

  - issue: "Existing five ingest-analysis files are placeholders."
    evidence: "ingest-analysis/bmf_faq-e-rechnung.analysis.md"
    impact: "Should be replaced/superseded by substantive analyses."

  - issue: "High-noise sources with navigation/cookie/footer capture."
    evidence: "log/web-clutter-audit_20260629_162739.md"
    impact: "Do not use as authority until cleaned."
```

The web-clutter audit explicitly reports 69 candidate files and lists high-noise candidates with cookie/datenschutz/impressum/menu/navigation signals. The corpus profile reports missing JSON/CSV inventory, 103 files scanned, and extensive duplicate hash groups between notes and refs.

## web_clutter_findings

```yaml
web_clutter_findings:
  use_as_filter_not_deletion_list: true
  highest_priority_cleanup_candidates:
    - "raw/refs/BMF_GoBD-2024.md"
    - "raw/refs/BZSt_50a-Abzugsteuer.md"
    - "raw/refs/FinanzamtNRW_Vereine-Umsatzsteuer.md"
    - "raw/refs/IHK-Koblenz_Reverse-Charge-Auslaendische-Dienstleister.md"
    - "raw/refs/DATEV_SKR42-Kontenrahmen.md"
    - "raw/refs/DATEV_Verfahrensdokumentation-GoBD.md"
  recommended_action: "create cleaned snapshots for high-authority sources before Phase 2."
```

## table_heavy_pdf_findings

```yaml
table_heavy_pdf_findings:
  flagged_by_lifecycle_report:
    - "raw/refs/IHK-Niederbayern_Checkliste-Kleinbetragsrechnungen.md"
    - "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md"
    - "raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.md"

  handling:
    - "Use text-level claims where clear."
    - "Mark table-sensitive claims as needs_verification."
    - "Review original PDFs or better table extraction before Phase 2 checklists."
```

The lifecycle report explicitly flags these three table-heavy PDF risks.

## contradictions_and_uncertainties

```yaml
contradictions_and_uncertainties:
  - title: "Non-gemeinnützig transfer risk"
    issue: "Some Verein sources assume gemeinnützigkeit/Zweckbetrieb/spenden logic; operator source note warns that Lika/Safer Space context may be non-gemeinnützig and economic."
    category: "lika_kb_content"
    severity_or_value: high
    evidence: "raw/notes/JudgementOfSources.md"
    recommended_change: "Add transfer-safety page and page-level warning."

  - title: "7% versus 19% event VAT unresolved"
    issue: "Mixed club/DJ/cultural events remain a tax-advisor review field."
    category: "lika_kb_content"
    severity_or_value: high
    evidence: "raw/notes/JudgementOfSources.md; raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md"
    recommended_change: "Create risk register entry and do not create definitive rule."

  - title: "Ticket-as-invoice unresolved"
    issue: "Sources inspected support invoice and Kleinbetragsrechnung requirements but do not settle event-ticket-as-invoice treatment."
    category: "lika_kb_content"
    severity_or_value: high
    evidence: "raw/notes/JudgementOfSources.md; raw/refs/BMJ_UStDV_33_Kleinbetragsrechnungen.md"
    recommended_change: "Create dedicated audit item."

  - title: "Venue settlement / Mindestbarumsatz gap"
    issue: "Major open question in operator source note; not resolved by inspected sources."
    category: "lika_kb_content"
    severity_or_value: high
    evidence: "raw/notes/JudgementOfSources.md"
    recommended_change: "Research or tax-advisor-only page before playbook."
```

`JudgementOfSources.md` explicitly identifies venue settlement/minimum bar revenue, 7%-vs-19% VAT for club/DJ/cultural mixed formats, and ticket-as-invoice as core gaps.

## high_potential_wiki_pages_for_phase2

```yaml
high_potential_wiki_pages_for_phase2:
  concept_pages:
    - "invoice-core-fields"
    - "kleinbetragsrechnung"
    - "e-rechnung-verein"
    - "belegablage-verfahrensdokumentation"
    - "event-business-area-assignment"
    - "event-vat-rate-risk"
    - "kuenstlersozialabgabe-event"
    - "foreign-artist-50a"
    - "source-authority-hierarchy"
    - "web-clutter-filter"

  summary_pages:
    - "core-tax-law-invoicing-gobd"
    - "association-accounting-process"
    - "events-vat-tickets"
    - "artist-contractor-obligations"
    - "source-judgment-and-open-risks"
    - "source-quality-and-custody"

  entity_pages:
    - "bmf"
    - "bmj-gesetze-im-internet"
    - "awv"
    - "lfst-bayern"
    - "deutsche-rentenversicherung"
    - "kuenstlersozialkasse"
    - "bzst"
    - "pretix"
```

## high_potential_deterministic_script_improvements

```yaml
potential_items:
  - title: "Add source-inventory output"
    category: "deterministic_scripts"
    severity_or_value: high
    evidence: "Phase 0 JSON output reports source-inventory JSON/CSV absent."
    recommended_change: "Emit manifests/source-inventory.json and .csv during phase0."
    target_path_or_component: "apex-meta/scripts/apex_kb.py phase0"

  - title: "Add web-clutter-audit command"
    category: "deterministic_scripts"
    severity_or_value: high
    evidence: "Lifecycle report recommends dedicated web-clutter-audit command."
    recommended_change: "Turn current sidecar audit into installed apex_kb.py subcommand."
    target_path_or_component: "apex-meta/scripts/apex_kb.py"

  - title: "Add cleaned-snapshot workflow"
    category: "deterministic_scripts"
    severity_or_value: high
    evidence: "69 web-clutter candidates, including high-authority BMF/BZSt/DATEV sources."
    recommended_change: "Create deterministic cleaned snapshot path with before/after hash custody."
    target_path_or_component: "apex-meta/kb/<kb-slug>/raw/cleaned/ or manifests/cleaned-snapshots/"

  - title: "Add table-extraction QC"
    category: "deterministic_scripts"
    severity_or_value: high
    evidence: "Lifecycle report flags LfSt, AWV, IHK Niederbayern table-heavy conversion risks."
    recommended_change: "Create table-sensitive-source flag and require manual/PDF review before Phase 2 checklists."
    target_path_or_component: "apex-meta/scripts/apex_kb.py phase0/lint"
```

The lifecycle report records both the missing source-inventory output and argument-order issue, and recommends a future `web-clutter-audit` command.

## package_or_contract_problems

```yaml
package_or_contract_problems:
  - issue: "Phase 1 template is source-specific, but this run required group-level analysis."
    severity_or_value: medium
    recommended_change: "Add official group-level ingest-analysis template."

  - issue: "No explicit web-clutter source-quality note field in current template."
    severity_or_value: medium
    recommended_change: "Add source_quality_notes block with clutter_status, usable_sections, suspected_noise_sections, confidence_effect, recommended_action."

  - issue: "No explicit table-heavy PDF handling field in current template."
    severity_or_value: medium
    recommended_change: "Add table_sensitive_claims and needs_pdf_review fields."
```

## recommended_changes_to_apex_kb

```yaml
recommended_changes_to_apex_kb:
  - "Add group-level Phase 1 artifact contract."
  - "Add web-clutter source-quality block to ingest-analysis template."
  - "Add table-heavy PDF QC block."
  - "Add source-inventory output to Phase 0."
  - "Add cleaned-snapshot custody workflow."
  - "Add placeholder-analysis detection lint check."
```

## recommended_changes_to_lika_kb_source_custody

```yaml
recommended_changes_to_lika_kb_source_custody:
  - "Prefer canonical raw/refs source where duplicate raw/notes copy exists."
  - "Create cleaned snapshots for BMF GoBD, BZSt §50a, Finanzamt NRW, DATEV, and IHK high-noise sources."
  - "Create PDF/manual review notes for LfSt Bayern, AWV, and IHK Niederbayern table-heavy sources."
  - "Mark internal research notes as meta-source/source-judgment, not legal authority."
  - "Mark gemeinnützigkeit-specific sources with transfer-safety warning."
```

## readiness_for_phase2

```yaml
readiness_for_phase2:
  overall: "not_ready_without_operator_review"
  phase1_group_analysis_complete: true
  source_specific_backfill_needed: true
  cleaned_snapshots_needed_before_strong_playbook: true
  high_risk_tax_questions_unresolved: true
  recommended_phase2_mode: "limited compile only after operator approves, with high-risk pages marked needs_review"
```

## exact_operator_gate

```yaml
phase_2_allowed: false
required_operator_phrase: "approve ingest"
must_be_separate_operator_turn: true
```

Phase 1 LLM ingest analysis complete. Phase 2 wiki creation remains blocked until the operator provides the separate exact phrase: approve ingest

```

---

**Gate status:** Phase 1 LLM ingest analysis complete. Phase 2 wiki creation remains blocked until the operator provides the separate exact phrase: `approve ingest`
```