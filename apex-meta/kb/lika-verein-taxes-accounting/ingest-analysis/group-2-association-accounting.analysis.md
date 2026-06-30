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
