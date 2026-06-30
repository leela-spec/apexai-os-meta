---
title: "Lika KB Phase 2 Concept Compile Report"
page_type: audit_item
kb_slug: "lika-verein-taxes-accounting"
source_refs: []
created_at: "2026-06-30T15:10:00Z"
updated_at: "2026-06-30T15:10:00Z"
confidence: "unknown"
claim_label: "raw_source"
status: "needs_review"
---

# Lika Verein Apex KB — Phase 2 Output Evaluation and Deferred Concept Compile Report

```yaml
report_metadata:
  kb_slug: lika-verein-taxes-accounting
  generated_at: "2026-06-29T18:45:00Z"
  output_mode: sandbox_markdown_file
  source_basis:
    - "/mnt/data/LLM Phase 1 Ingest.txt"
    - "saved project-resource Phase 2 output snippets"
    - "installed apex-kb skill contract already reloaded in chat"
  repo_written: false
```

## 1. Executive verdict

The workflow is valuable, but the value is uneven by layer.

```yaml
verdict:
  phase0_deterministic_navigation: very_high_value
  phase1_grouped_ingest_analysis: high_value_but_not_final_source_specific
  phase2_summary_layer: high_value_as_navigation_layer
  deferred_concept_layer: critical_next_step
  current_limitation: "Not all 95/103 sources were read end-to-end; noisy/table-heavy sources remain needs_review."
```

**Bottom line:** the system now creates reusable context instead of forcing every future model to rediscover the corpus. The largest practical gain is not prose quality; it is routing: index -> summary page -> concept page -> raw source only when necessary.

## 2. What was tested

```yaml
test_scope:
  phase1_file_available_locally: True
  phase1_file_bytes: 80708
  phase1_estimated_tokens_at_4_chars_per_token: 20177
  raw_source_candidates_reported_by_phase1: 103
  summary_pages_generated_in_phase2: 6
  deferred_concept_pages_detected: 23
  deferred_concept_pages_generated_in_this_report: 23
  generated_concept_bundle_bytes: 33272
  generated_concept_bundle_estimated_tokens: 8318
```

### Simulation method

1. Treat raw corpus access as the expensive baseline: a future model must inspect many files, source names, and raw passages.
2. Treat Phase 2 summary pages as a mid-layer: a future model can start from six stable topic summaries.
3. Add the 23 concept pages generated below as a fine-grained retrieval layer.
4. Run representative query-routing tests and compare pages required.

This is not a legal/tax validation test. It is a KB-function test.

## 3. Token and retrieval value estimate

```yaml
token_value_model:
  baseline_raw_corpus:
    source_candidates: 103
    expected_behavior: "read/search many raw files and re-derive concepts"
    estimated_efficiency: low
  phase2_summary_layer:
    pages: 6
    expected_behavior: "read index plus 1-2 summaries"
    estimated_efficiency: high
  summary_plus_concept_layer:
    pages: 29
    expected_behavior: "read index plus 1 summary plus 1-3 concepts"
    estimated_efficiency: very_high
```

A conservative token-savings estimate for future queries is **5x-15x** against raw-source browsing. For narrow recurring questions, like invoice fields, KSK exposure, or noisy-source cleanup, the likely saving is higher because the concept page isolates the relevant claims and flags.

## 4. Query-routing simulation

| Test query | Pages selected after concept compile | Assessment |
| --- | --- | --- |
| What invoice fields do we need? | wiki/index.md<br>wiki/summaries/core-tax-law-invoicing-gobd.md<br>wiki/concepts/invoice-core-fields.md<br>wiki/concepts/kleinbetragsrechnung.md | Pass: small page set, no raw-source reread required unless final evidence needed |
| Does a ticket count as an invoice? | wiki/index.md<br>wiki/summaries/events-vat-tickets.md<br>wiki/concepts/ticket-as-invoice-gap.md<br>wiki/concepts/kleinbetragsrechnung.md<br>wiki/summaries/source-judgment-and-open-risks.md | Pass: small page set, no raw-source reread required unless final evidence needed |
| How should we handle artist payments? | wiki/index.md<br>wiki/summaries/artist-contractor-obligations.md<br>wiki/concepts/kuenstlersozialabgabe-event.md<br>wiki/concepts/artist-contract-source-of-truth.md<br>wiki/concepts/foreign-artist-50a.md | Pass: small page set, no raw-source reread required unless final evidence needed |
| What are the unresolved tax risks? | wiki/index.md<br>wiki/summaries/source-judgment-and-open-risks.md<br>wiki/concepts/unresolved-tax-risk-register.md<br>wiki/concepts/venue-settlement-gap.md<br>wiki/concepts/event-vat-rate-risk.md | Pass: small page set, no raw-source reread required unless final evidence needed |
| Which sources are noisy? | wiki/index.md<br>wiki/summaries/source-quality-and-custody.md<br>wiki/concepts/web-clutter-filter.md<br>wiki/concepts/duplicate-source-custody.md<br>wiki/concepts/table-heavy-pdf-risk.md | Pass: small page set, no raw-source reread required unless final evidence needed |

## 5. Self-observation of the process

```yaml
self_observation:
  what_improved:
    - "The saved index/summary structure immediately revealed the missing layer: concepts_deferred_to_next_compile_pass."
    - "The work was constrained by explicit source refs and confidence labels instead of open-ended rethinking."
    - "The concept list made the next action deterministic enough to execute without redesign."
  what_was_still_inefficient:
    - "The Phase 1 file exists locally, but the Phase 2 chat-output file exists in project-resource search rather than as repo files."
    - "The concept pages are compiled from grouped analyses, not source-specific analyses."
    - "Citations/source pointers are preserved but not yet postflight-linted."
  hallucination_risk_reduction:
    - "High: each concept inherits source_refs and parent summary."
    - "Medium: definitions are concise extrapolations from approved grouped analysis, not newly opened raw-source analysis."
  eloquence_vs_efficiency:
    - "The index sharply reduced task ambiguity."
    - "The concept-page template made generation more regular and less rhetorically freeform."
    - "The output is more machine-usable than prose-polished."
```

## 6. Quality scoring

| Layer | Value | Token saving | Trust | Weakness |
| --- | ---: | ---: | ---: | --- |
| Phase 0 corpus navigation | 9/10 | 8/10 | 8/10 | Needs richer source-inventory output |
| Phase 1 grouped analysis | 8/10 | 8/10 | 7/10 | Grouped, not source-specific for all files |
| Phase 2 summary pages | 8/10 | 9/10 | 7/10 | Concept/entity layer absent before this report |
| Concept pages generated here | 8/10 | 9/10 | 6.5/10 | Needs deterministic postflight and optional source-specific backfill |

## 7. Generated deferred concept pages

# FILE: `apex-meta/kb/lika-verein-taxes-accounting/wiki/concepts/invoice-core-fields.md`

```markdown
---
title: "Mandatory invoice fields"
page_type: concept
kb_slug: "lika-verein-taxes-accounting"
concept_slug: "invoice-core-fields"
source_refs:
  - "raw/refs/BMJ_UStG_14_Rechnungen.md"
created_at: "2026-06-29T18:45:00Z"
updated_at: "2026-06-29T18:45:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts: []
related_entities: []
review_flags: []
---

# Mandatory invoice fields

## Definition

Defines the normal invoice field set as the checklist anchor for Lika invoices and invoice-like records.

## Operating Rules

```yaml
rules:
  - "Use for full invoice checklist; do not use to decide whether an event ticket is sufficient evidence."
```

## Relationships

```yaml
parent_summary: "wiki/summaries/core-tax-law-invoicing-gobd.md"
source_refs:
  - "raw/refs/BMJ_UStG_14_Rechnungen.md"
```

## Evidence

```yaml
evidence:
  - supports: "Concept compiled from approved Phase 1 grouped analysis and Phase 2 summary layer."
    source_pointer: "Phase 1 grouped analysis / core-tax-law-invoicing-gobd"
```

## Contradictions and Open Questions

```yaml
contradictions: []
open_questions:
  - "Needs post-save deterministic lint/index rebuild and optional source-specific backfill before use as final playbook rule."
```
```

---

# FILE: `apex-meta/kb/lika-verein-taxes-accounting/wiki/concepts/kleinbetragsrechnung.md`

```markdown
---
title: "Small-value invoice up to 250 EUR"
page_type: concept
kb_slug: "lika-verein-taxes-accounting"
concept_slug: "kleinbetragsrechnung"
source_refs:
  - "raw/refs/BMJ_UStDV_33_Kleinbetragsrechnungen.md"
created_at: "2026-06-29T18:45:00Z"
updated_at: "2026-06-29T18:45:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts: []
related_entities: []
review_flags: []
---

# Small-value invoice up to 250 EUR

## Definition

Captures the reduced minimum field path for invoices not exceeding 250 EUR.

## Operating Rules

```yaml
rules:
  - "Use as a separate checklist branch; do not conflate with ticket-as-invoice."
```

## Relationships

```yaml
parent_summary: "wiki/summaries/core-tax-law-invoicing-gobd.md"
source_refs:
  - "raw/refs/BMJ_UStDV_33_Kleinbetragsrechnungen.md"
```

## Evidence

```yaml
evidence:
  - supports: "Concept compiled from approved Phase 1 grouped analysis and Phase 2 summary layer."
    source_pointer: "Phase 1 grouped analysis / core-tax-law-invoicing-gobd"
```

## Contradictions and Open Questions

```yaml
contradictions: []
open_questions:
  - "Needs post-save deterministic lint/index rebuild and optional source-specific backfill before use as final playbook rule."
```
```

---

# FILE: `apex-meta/kb/lika-verein-taxes-accounting/wiki/concepts/e-rechnung-verein.md`

```markdown
---
title: "E-Rechnung obligations for associations"
page_type: concept
kb_slug: "lika-verein-taxes-accounting"
concept_slug: "e-rechnung-verein"
source_refs:
  - "raw/refs/BMF_FAQ-E-Rechnung.md"
  - "raw/refs/BMJ_UStG_14_Rechnungen.md"
created_at: "2026-06-29T18:45:00Z"
updated_at: "2026-06-29T18:45:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "needs_review"
related_concepts: []
related_entities: []
review_flags: []
---

# E-Rechnung obligations for associations

## Definition

Tracks when structured e-invoice obligations may apply to association workflows.

## Operating Rules

```yaml
rules:
  - "Requires concrete entrepreneurial/non-entrepreneurial area and counterparty classification."
```

## Relationships

```yaml
parent_summary: "wiki/summaries/core-tax-law-invoicing-gobd.md"
source_refs:
  - "raw/refs/BMF_FAQ-E-Rechnung.md"
  - "raw/refs/BMJ_UStG_14_Rechnungen.md"
```

## Evidence

```yaml
evidence:
  - supports: "Concept compiled from approved Phase 1 grouped analysis and Phase 2 summary layer."
    source_pointer: "Phase 1 grouped analysis / core-tax-law-invoicing-gobd"
```

## Contradictions and Open Questions

```yaml
contradictions: []
open_questions:
  - "Needs post-save deterministic lint/index rebuild and optional source-specific backfill before use as final playbook rule."
```
```

---

# FILE: `apex-meta/kb/lika-verein-taxes-accounting/wiki/concepts/belegablage-verfahrensdokumentation.md`

```markdown
---
title: "Receipt custody procedure documentation"
page_type: concept
kb_slug: "lika-verein-taxes-accounting"
concept_slug: "belegablage-verfahrensdokumentation"
source_refs:
  - "raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.md"
created_at: "2026-06-29T18:45:00Z"
updated_at: "2026-06-29T18:45:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "needs_review"
related_concepts: []
related_entities: []
review_flags: []
---

# Receipt custody procedure documentation

## Definition

Defines the documented receipt-custody workflow from entry/creation to filing, bookkeeping handoff, retention, and deletion.

## Operating Rules

```yaml
rules:
  - "Use as SOP backbone; table/PDF-sensitive claims remain review items."
```

## Relationships

```yaml
parent_summary: "wiki/summaries/core-tax-law-invoicing-gobd.md"
source_refs:
  - "raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.md"
```

## Evidence

```yaml
evidence:
  - supports: "Concept compiled from approved Phase 1 grouped analysis and Phase 2 summary layer."
    source_pointer: "Phase 1 grouped analysis / core-tax-law-invoicing-gobd"
```

## Contradictions and Open Questions

```yaml
contradictions: []
open_questions:
  - "Needs post-save deterministic lint/index rebuild and optional source-specific backfill before use as final playbook rule."
```
```

---

# FILE: `apex-meta/kb/lika-verein-taxes-accounting/wiki/concepts/belegfunktion.md`

```markdown
---
title: "Documents with receipt/evidence function"
page_type: concept
kb_slug: "lika-verein-taxes-accounting"
concept_slug: "belegfunktion"
source_refs:
  - "raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.md"
created_at: "2026-06-29T18:45:00Z"
updated_at: "2026-06-29T18:45:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "needs_review"
related_concepts: []
related_entities: []
review_flags: []
---

# Documents with receipt/evidence function

## Definition

Identifies documents that function as bookkeeping or tax evidence and therefore need custody rules.

## Operating Rules

```yaml
rules:
  - "Use to classify receipts, invoices, contracts, bank records, exports, and internal evidence."
```

## Relationships

```yaml
parent_summary: "wiki/summaries/association-accounting-process.md"
source_refs:
  - "raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.md"
```

## Evidence

```yaml
evidence:
  - supports: "Concept compiled from approved Phase 1 grouped analysis and Phase 2 summary layer."
    source_pointer: "Phase 1 grouped analysis / association-accounting-process"
```

## Contradictions and Open Questions

```yaml
contradictions: []
open_questions:
  - "Needs post-save deterministic lint/index rebuild and optional source-specific backfill before use as final playbook rule."
```
```

---

# FILE: `apex-meta/kb/lika-verein-taxes-accounting/wiki/concepts/accounting-source-custody.md`

```markdown
---
title: "Accounting source custody workflow"
page_type: concept
kb_slug: "lika-verein-taxes-accounting"
concept_slug: "accounting-source-custody"
source_refs:
  - "raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.md"
created_at: "2026-06-29T18:45:00Z"
updated_at: "2026-06-29T18:45:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "needs_review"
related_concepts: []
related_entities: []
review_flags: []
---

# Accounting source custody workflow

## Definition

Defines how evidence moves from source systems into stored records and bookkeeping review.

## Operating Rules

```yaml
rules:
  - "Create custody checkpoints before operational accounting playbooks."
```

## Relationships

```yaml
parent_summary: "wiki/summaries/association-accounting-process.md"
source_refs:
  - "raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.md"
```

## Evidence

```yaml
evidence:
  - supports: "Concept compiled from approved Phase 1 grouped analysis and Phase 2 summary layer."
    source_pointer: "Phase 1 grouped analysis / association-accounting-process"
```

## Contradictions and Open Questions

```yaml
contradictions: []
open_questions:
  - "Needs post-save deterministic lint/index rebuild and optional source-specific backfill before use as final playbook rule."
```
```

---

# FILE: `apex-meta/kb/lika-verein-taxes-accounting/wiki/concepts/reimbursement-evidence.md`

```markdown
---
title: "Reimbursement and expense evidence"
page_type: concept
kb_slug: "lika-verein-taxes-accounting"
concept_slug: "reimbursement-evidence"
source_refs:
  - "raw/notes/JudgementOfSources.md"
  - "raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.md"
created_at: "2026-06-29T18:45:00Z"
updated_at: "2026-06-29T18:45:00Z"
confidence: "low"
claim_label: "source_backed_summary"
status: "needs_review"
related_concepts: []
related_entities: []
review_flags: []
---

# Reimbursement and expense evidence

## Definition

Tracks the evidence needed to distinguish reimbursements, contractor payments, and internal expense records.

## Operating Rules

```yaml
rules:
  - "Do not finalize reimbursement policy until internal vs contractor payment types are known."
```

## Relationships

```yaml
parent_summary: "wiki/summaries/association-accounting-process.md"
source_refs:
  - "raw/notes/JudgementOfSources.md"
  - "raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.md"
```

## Evidence

```yaml
evidence:
  - supports: "Concept compiled from approved Phase 1 grouped analysis and Phase 2 summary layer."
    source_pointer: "Phase 1 grouped analysis / association-accounting-process"
```

## Contradictions and Open Questions

```yaml
contradictions: []
open_questions:
  - "Needs post-save deterministic lint/index rebuild and optional source-specific backfill before use as final playbook rule."
```
```

---

# FILE: `apex-meta/kb/lika-verein-taxes-accounting/wiki/concepts/event-business-area-assignment.md`

```markdown
---
title: "Event revenue and expense assignment to association areas"
page_type: concept
kb_slug: "lika-verein-taxes-accounting"
concept_slug: "event-business-area-assignment"
source_refs:
  - "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md"
created_at: "2026-06-29T18:45:00Z"
updated_at: "2026-06-29T18:45:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "needs_review"
related_concepts: []
related_entities: []
review_flags: []
---

# Event revenue and expense assignment to association areas

## Definition

Maps event revenues and expenses to association activity areas before tax treatment is inferred.

## Operating Rules

```yaml
rules:
  - "Record revenues and expenses separately; no salding as a default analytical shortcut."
```

## Relationships

```yaml
parent_summary: "wiki/summaries/events-vat-tickets.md"
source_refs:
  - "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md"
```

## Evidence

```yaml
evidence:
  - supports: "Concept compiled from approved Phase 1 grouped analysis and Phase 2 summary layer."
    source_pointer: "Phase 1 grouped analysis / events-vat-tickets"
```

## Contradictions and Open Questions

```yaml
contradictions: []
open_questions:
  - "Needs post-save deterministic lint/index rebuild and optional source-specific backfill before use as final playbook rule."
```
```

---

# FILE: `apex-meta/kb/lika-verein-taxes-accounting/wiki/concepts/event-vat-rate-risk.md`

```markdown
---
title: "7 percent versus 19 percent VAT risk for mixed cultural or club events"
page_type: concept
kb_slug: "lika-verein-taxes-accounting"
concept_slug: "event-vat-rate-risk"
source_refs:
  - "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md"
  - "raw/notes/JudgementOfSources.md"
created_at: "2026-06-29T18:45:00Z"
updated_at: "2026-06-29T18:45:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "needs_review"
related_concepts: []
related_entities: []
review_flags: []
---

# 7 percent versus 19 percent VAT risk for mixed cultural or club events

## Definition

Preserves the unresolved risk around VAT rate treatment for mixed DJ, club, cultural, and association-event formats.

## Operating Rules

```yaml
rules:
  - "Tax-advisor review field; do not generate a definitive rule."
```

## Relationships

```yaml
parent_summary: "wiki/summaries/events-vat-tickets.md"
source_refs:
  - "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md"
  - "raw/notes/JudgementOfSources.md"
```

## Evidence

```yaml
evidence:
  - supports: "Concept compiled from approved Phase 1 grouped analysis and Phase 2 summary layer."
    source_pointer: "Phase 1 grouped analysis / events-vat-tickets"
```

## Contradictions and Open Questions

```yaml
contradictions: []
open_questions:
  - "Needs post-save deterministic lint/index rebuild and optional source-specific backfill before use as final playbook rule."
```
```

---

# FILE: `apex-meta/kb/lika-verein-taxes-accounting/wiki/concepts/ticketing-tax-configuration.md`

```markdown
---
title: "Ticketing tax rules in pretix/Eventbrite/ticket.io"
page_type: concept
kb_slug: "lika-verein-taxes-accounting"
concept_slug: "ticketing-tax-configuration"
source_refs:
  - "raw/refs/pretix_Taxes-Guide.md"
  - "raw/refs/Eventbrite_Umsatzuebersicht-Export.md"
  - "raw/refs/ticketio_Event-Controlling-Reporting.md"
created_at: "2026-06-29T18:45:00Z"
updated_at: "2026-06-29T18:45:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "needs_review"
related_concepts: []
related_entities: []
review_flags: []
---

# Ticketing tax rules in pretix/Eventbrite/ticket.io

## Definition

Separates provider configuration from the underlying tax/legal classification decision.

## Operating Rules

```yaml
rules:
  - "Providers implement tax rules; they do not decide them."
```

## Relationships

```yaml
parent_summary: "wiki/summaries/events-vat-tickets.md"
source_refs:
  - "raw/refs/pretix_Taxes-Guide.md"
  - "raw/refs/Eventbrite_Umsatzuebersicht-Export.md"
  - "raw/refs/ticketio_Event-Controlling-Reporting.md"
```

## Evidence

```yaml
evidence:
  - supports: "Concept compiled from approved Phase 1 grouped analysis and Phase 2 summary layer."
    source_pointer: "Phase 1 grouped analysis / events-vat-tickets"
```

## Contradictions and Open Questions

```yaml
contradictions: []
open_questions:
  - "Needs post-save deterministic lint/index rebuild and optional source-specific backfill before use as final playbook rule."
```
```

---

# FILE: `apex-meta/kb/lika-verein-taxes-accounting/wiki/concepts/ticket-as-invoice-gap.md`

```markdown
---
title: "Ticket as invoice / ticket receipt evidentiary gap"
page_type: concept
kb_slug: "lika-verein-taxes-accounting"
concept_slug: "ticket-as-invoice-gap"
source_refs:
  - "raw/notes/JudgementOfSources.md"
  - "raw/refs/BMJ_UStDV_33_Kleinbetragsrechnungen.md"
created_at: "2026-06-29T18:45:00Z"
updated_at: "2026-06-29T18:45:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "needs_review"
related_concepts: []
related_entities: []
review_flags: []
---

# Ticket as invoice / ticket receipt evidentiary gap

## Definition

Keeps ticket-as-invoice status unresolved until source-specific legal/tax review confirms treatment.

## Operating Rules

```yaml
rules:
  - "Audit item, not an operational conclusion."
```

## Relationships

```yaml
parent_summary: "wiki/summaries/events-vat-tickets.md"
source_refs:
  - "raw/notes/JudgementOfSources.md"
  - "raw/refs/BMJ_UStDV_33_Kleinbetragsrechnungen.md"
```

## Evidence

```yaml
evidence:
  - supports: "Concept compiled from approved Phase 1 grouped analysis and Phase 2 summary layer."
    source_pointer: "Phase 1 grouped analysis / events-vat-tickets"
```

## Contradictions and Open Questions

```yaml
contradictions: []
open_questions:
  - "Needs post-save deterministic lint/index rebuild and optional source-specific backfill before use as final playbook rule."
```
```

---

# FILE: `apex-meta/kb/lika-verein-taxes-accounting/wiki/concepts/kuenstlersozialabgabe-event.md`

```markdown
---
title: "Kuenstlersozialabgabe for event contexts"
page_type: concept
kb_slug: "lika-verein-taxes-accounting"
concept_slug: "kuenstlersozialabgabe-event"
source_refs:
  - "raw/refs/DRV_K5001_Kuenstlersozialabgabe.md"
  - "raw/refs/KSK_Info04_Abgabepflicht-Veranstalter.md"
created_at: "2026-06-29T18:45:00Z"
updated_at: "2026-06-29T18:45:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "needs_review"
related_concepts: []
related_entities: []
review_flags: []
---

# Kuenstlersozialabgabe for event contexts

## Definition

Tracks KSK exposure for payments to self-employed artists and publicists in an association/event context.

## Operating Rules

```yaml
rules:
  - "Maintain annual payment ledger and counterparty clarity."
```

## Relationships

```yaml
parent_summary: "wiki/summaries/artist-contractor-obligations.md"
source_refs:
  - "raw/refs/DRV_K5001_Kuenstlersozialabgabe.md"
  - "raw/refs/KSK_Info04_Abgabepflicht-Veranstalter.md"
```

## Evidence

```yaml
evidence:
  - supports: "Concept compiled from approved Phase 1 grouped analysis and Phase 2 summary layer."
    source_pointer: "Phase 1 grouped analysis / artist-contractor-obligations"
```

## Contradictions and Open Questions

```yaml
contradictions: []
open_questions:
  - "Needs post-save deterministic lint/index rebuild and optional source-specific backfill before use as final playbook rule."
```
```

---

# FILE: `apex-meta/kb/lika-verein-taxes-accounting/wiki/concepts/foreign-artist-50a.md`

```markdown
---
title: "Foreign artist section 50a withholding workflow"
page_type: concept
kb_slug: "lika-verein-taxes-accounting"
concept_slug: "foreign-artist-50a"
source_refs:
  - "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md"
  - "raw/refs/BZSt_50a-Abzugsteuer.md"
created_at: "2026-06-29T18:45:00Z"
updated_at: "2026-06-29T18:45:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "needs_review"
related_concepts: []
related_entities: []
review_flags: []
---

# Foreign artist section 50a withholding workflow

## Definition

Separates foreign artist withholding-tax review from ordinary domestic contractor processing.

## Operating Rules

```yaml
rules:
  - "Clean BZSt source before detailed workflow; case facts required."
```

## Relationships

```yaml
parent_summary: "wiki/summaries/artist-contractor-obligations.md"
source_refs:
  - "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md"
  - "raw/refs/BZSt_50a-Abzugsteuer.md"
```

## Evidence

```yaml
evidence:
  - supports: "Concept compiled from approved Phase 1 grouped analysis and Phase 2 summary layer."
    source_pointer: "Phase 1 grouped analysis / artist-contractor-obligations"
```

## Contradictions and Open Questions

```yaml
contradictions: []
open_questions:
  - "Needs post-save deterministic lint/index rebuild and optional source-specific backfill before use as final playbook rule."
```
```

---

# FILE: `apex-meta/kb/lika-verein-taxes-accounting/wiki/concepts/artist-contract-source-of-truth.md`

```markdown
---
title: "Artist contract source of truth"
page_type: concept
kb_slug: "lika-verein-taxes-accounting"
concept_slug: "artist-contract-source-of-truth"
source_refs:
  - "raw/refs/DRV_K5001_Kuenstlersozialabgabe.md"
created_at: "2026-06-29T18:45:00Z"
updated_at: "2026-06-29T18:45:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "needs_review"
related_concepts: []
related_entities: []
review_flags: []
---

# Artist contract source of truth

## Definition

Defines the contract and payment records needed to decide KSK, agency-chain, VAT, and withholding questions.

## Operating Rules

```yaml
rules:
  - "Contract wording cannot override statutory allocation; use facts and counterparty structure."
```

## Relationships

```yaml
parent_summary: "wiki/summaries/artist-contractor-obligations.md"
source_refs:
  - "raw/refs/DRV_K5001_Kuenstlersozialabgabe.md"
```

## Evidence

```yaml
evidence:
  - supports: "Concept compiled from approved Phase 1 grouped analysis and Phase 2 summary layer."
    source_pointer: "Phase 1 grouped analysis / artist-contractor-obligations"
```

## Contradictions and Open Questions

```yaml
contradictions: []
open_questions:
  - "Needs post-save deterministic lint/index rebuild and optional source-specific backfill before use as final playbook rule."
```
```

---

# FILE: `apex-meta/kb/lika-verein-taxes-accounting/wiki/concepts/foreign-artist-vat-recipient-liability.md`

```markdown
---
title: "Foreign artist VAT recipient liability"
page_type: concept
kb_slug: "lika-verein-taxes-accounting"
concept_slug: "foreign-artist-vat-recipient-liability"
source_refs:
  - "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md"
created_at: "2026-06-29T18:45:00Z"
updated_at: "2026-06-29T18:45:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "needs_review"
related_concepts: []
related_entities: []
review_flags: []
---

# Foreign artist VAT recipient liability

## Definition

Captures cases where foreign artist performance services may create VAT recipient-liability or reverse-charge review.

## Operating Rules

```yaml
rules:
  - "Treat as separate review lane requiring case details."
```

## Relationships

```yaml
parent_summary: "wiki/summaries/artist-contractor-obligations.md"
source_refs:
  - "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md"
```

## Evidence

```yaml
evidence:
  - supports: "Concept compiled from approved Phase 1 grouped analysis and Phase 2 summary layer."
    source_pointer: "Phase 1 grouped analysis / artist-contractor-obligations"
```

## Contradictions and Open Questions

```yaml
contradictions: []
open_questions:
  - "Needs post-save deterministic lint/index rebuild and optional source-specific backfill before use as final playbook rule."
```
```

---

# FILE: `apex-meta/kb/lika-verein-taxes-accounting/wiki/concepts/source-authority-hierarchy.md`

```markdown
---
title: "Source authority hierarchy"
page_type: concept
kb_slug: "lika-verein-taxes-accounting"
concept_slug: "source-authority-hierarchy"
source_refs:
  - "raw/notes/JudgementOfSources.md"
created_at: "2026-06-29T18:45:00Z"
updated_at: "2026-06-29T18:45:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "needs_review"
related_concepts: []
related_entities: []
review_flags: []
---

# Source authority hierarchy

## Definition

Ranks source families by use: statutory/official sources first, operator notes as meta-source, provider docs as configuration evidence.

## Operating Rules

```yaml
rules:
  - "Do not promote internal notes or provider docs into legal authority."
```

## Relationships

```yaml
parent_summary: "wiki/summaries/source-judgment-and-open-risks.md"
source_refs:
  - "raw/notes/JudgementOfSources.md"
```

## Evidence

```yaml
evidence:
  - supports: "Concept compiled from approved Phase 1 grouped analysis and Phase 2 summary layer."
    source_pointer: "Phase 1 grouped analysis / source-judgment-and-open-risks"
```

## Contradictions and Open Questions

```yaml
contradictions: []
open_questions:
  - "Needs post-save deterministic lint/index rebuild and optional source-specific backfill before use as final playbook rule."
```
```

---

# FILE: `apex-meta/kb/lika-verein-taxes-accounting/wiki/concepts/transfer-safety.md`

```markdown
---
title: "Transfer safety from generic association sources to Lika"
page_type: concept
kb_slug: "lika-verein-taxes-accounting"
concept_slug: "transfer-safety"
source_refs:
  - "raw/notes/JudgementOfSources.md"
created_at: "2026-06-29T18:45:00Z"
updated_at: "2026-06-29T18:45:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "needs_review"
related_concepts: []
related_entities: []
review_flags: []
---

# Transfer safety from generic association sources to Lika

## Definition

Flags when sources written for gemeinnuetzige Vereine, Zweckbetrieb, donation logic, or generic associations may not transfer directly to Lika.

## Operating Rules

```yaml
rules:
  - "Use page-level warning where source context differs from Lika."
```

## Relationships

```yaml
parent_summary: "wiki/summaries/source-judgment-and-open-risks.md"
source_refs:
  - "raw/notes/JudgementOfSources.md"
```

## Evidence

```yaml
evidence:
  - supports: "Concept compiled from approved Phase 1 grouped analysis and Phase 2 summary layer."
    source_pointer: "Phase 1 grouped analysis / source-judgment-and-open-risks"
```

## Contradictions and Open Questions

```yaml
contradictions: []
open_questions:
  - "Needs post-save deterministic lint/index rebuild and optional source-specific backfill before use as final playbook rule."
```
```

---

# FILE: `apex-meta/kb/lika-verein-taxes-accounting/wiki/concepts/unresolved-tax-risk-register.md`

```markdown
---
title: "Unresolved tax and accounting risk register"
page_type: concept
kb_slug: "lika-verein-taxes-accounting"
concept_slug: "unresolved-tax-risk-register"
source_refs:
  - "raw/notes/JudgementOfSources.md"
created_at: "2026-06-29T18:45:00Z"
updated_at: "2026-06-29T18:45:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "needs_review"
related_concepts: []
related_entities: []
review_flags: []
---

# Unresolved tax and accounting risk register

## Definition

Collects high-risk unresolved issues before any practical playbook is treated as stable.

## Operating Rules

```yaml
rules:
  - "Venue settlement, VAT-rate, ticket-as-invoice, and foreign artist workflows stay visible."
```

## Relationships

```yaml
parent_summary: "wiki/summaries/source-judgment-and-open-risks.md"
source_refs:
  - "raw/notes/JudgementOfSources.md"
```

## Evidence

```yaml
evidence:
  - supports: "Concept compiled from approved Phase 1 grouped analysis and Phase 2 summary layer."
    source_pointer: "Phase 1 grouped analysis / source-judgment-and-open-risks"
```

## Contradictions and Open Questions

```yaml
contradictions: []
open_questions:
  - "Needs post-save deterministic lint/index rebuild and optional source-specific backfill before use as final playbook rule."
```
```

---

# FILE: `apex-meta/kb/lika-verein-taxes-accounting/wiki/concepts/venue-settlement-gap.md`

```markdown
---
title: "Venue settlement and Mindestbarumsatz gap"
page_type: concept
kb_slug: "lika-verein-taxes-accounting"
concept_slug: "venue-settlement-gap"
source_refs:
  - "raw/notes/JudgementOfSources.md"
created_at: "2026-06-29T18:45:00Z"
updated_at: "2026-06-29T18:45:00Z"
confidence: "low"
claim_label: "source_backed_summary"
status: "needs_review"
related_concepts: []
related_entities: []
review_flags: []
---

# Venue settlement and Mindestbarumsatz gap

## Definition

Isolates venue settlement, minimum bar revenue, and bar revenue guarantee questions as under-sourced high-risk topics.

## Operating Rules

```yaml
rules:
  - "Research or tax-advisor-only page before operational treatment."
```

## Relationships

```yaml
parent_summary: "wiki/summaries/source-judgment-and-open-risks.md"
source_refs:
  - "raw/notes/JudgementOfSources.md"
```

## Evidence

```yaml
evidence:
  - supports: "Concept compiled from approved Phase 1 grouped analysis and Phase 2 summary layer."
    source_pointer: "Phase 1 grouped analysis / source-judgment-and-open-risks"
```

## Contradictions and Open Questions

```yaml
contradictions: []
open_questions:
  - "Needs post-save deterministic lint/index rebuild and optional source-specific backfill before use as final playbook rule."
```
```

---

# FILE: `apex-meta/kb/lika-verein-taxes-accounting/wiki/concepts/web-clutter-filter.md`

```markdown
---
title: "Web clutter filter"
page_type: concept
kb_slug: "lika-verein-taxes-accounting"
concept_slug: "web-clutter-filter"
source_refs:
  - "log/web-clutter-audit_20260629_162739.md"
created_at: "2026-06-29T18:45:00Z"
updated_at: "2026-06-29T18:45:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts: []
related_entities: []
review_flags: []
---

# Web clutter filter

## Definition

Defines how to treat captured web pages with cookie, navigation, footer, menu, or duplicate boilerplate noise.

## Operating Rules

```yaml
rules:
  - "Use as filter and cleanup queue, not as deletion list."
```

## Relationships

```yaml
parent_summary: "wiki/summaries/source-quality-and-custody.md"
source_refs:
  - "log/web-clutter-audit_20260629_162739.md"
```

## Evidence

```yaml
evidence:
  - supports: "Concept compiled from approved Phase 1 grouped analysis and Phase 2 summary layer."
    source_pointer: "Phase 1 grouped analysis / source-quality-and-custody"
```

## Contradictions and Open Questions

```yaml
contradictions: []
open_questions:
  - "Needs post-save deterministic lint/index rebuild and optional source-specific backfill before use as final playbook rule."
```
```

---

# FILE: `apex-meta/kb/lika-verein-taxes-accounting/wiki/concepts/duplicate-source-custody.md`

```markdown
---
title: "Duplicate source custody"
page_type: concept
kb_slug: "lika-verein-taxes-accounting"
concept_slug: "duplicate-source-custody"
source_refs:
  - "manifests/phase0/corpus-profile.md"
created_at: "2026-06-29T18:45:00Z"
updated_at: "2026-06-29T18:45:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts: []
related_entities: []
review_flags: []
---

# Duplicate source custody

## Definition

Tracks duplicate raw/notes and raw/refs copies and forces canonical-source choice before detailed semantic use.

## Operating Rules

```yaml
rules:
  - "Prefer canonical raw/refs where duplicate source content exists unless operator decides otherwise."
```

## Relationships

```yaml
parent_summary: "wiki/summaries/source-quality-and-custody.md"
source_refs:
  - "manifests/phase0/corpus-profile.md"
```

## Evidence

```yaml
evidence:
  - supports: "Concept compiled from approved Phase 1 grouped analysis and Phase 2 summary layer."
    source_pointer: "Phase 1 grouped analysis / source-quality-and-custody"
```

## Contradictions and Open Questions

```yaml
contradictions: []
open_questions:
  - "Needs post-save deterministic lint/index rebuild and optional source-specific backfill before use as final playbook rule."
```
```

---

# FILE: `apex-meta/kb/lika-verein-taxes-accounting/wiki/concepts/table-heavy-pdf-risk.md`

```markdown
---
title: "Table-heavy PDF risk"
page_type: concept
kb_slug: "lika-verein-taxes-accounting"
concept_slug: "table-heavy-pdf-risk"
source_refs:
  - "log/lifecycle-run-report_20260629_162739.md"
created_at: "2026-06-29T18:45:00Z"
updated_at: "2026-06-29T18:45:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts: []
related_entities: []
review_flags: []
---

# Table-heavy PDF risk

## Definition

Marks sources where table conversion can distort thresholds, classifications, or row relationships.

## Operating Rules

```yaml
rules:
  - "Use only clear text claims until PDF/manual or better table extraction review."
```

## Relationships

```yaml
parent_summary: "wiki/summaries/source-quality-and-custody.md"
source_refs:
  - "log/lifecycle-run-report_20260629_162739.md"
```

## Evidence

```yaml
evidence:
  - supports: "Concept compiled from approved Phase 1 grouped analysis and Phase 2 summary layer."
    source_pointer: "Phase 1 grouped analysis / source-quality-and-custody"
```

## Contradictions and Open Questions

```yaml
contradictions: []
open_questions:
  - "Needs post-save deterministic lint/index rebuild and optional source-specific backfill before use as final playbook rule."
```
```

---

# FILE: `apex-meta/kb/lika-verein-taxes-accounting/wiki/concepts/phase1-placeholder-replacement.md`

```markdown
---
title: "Phase 1 placeholder replacement"
page_type: concept
kb_slug: "lika-verein-taxes-accounting"
concept_slug: "phase1-placeholder-replacement"
source_refs:
  - "ingest-analysis/"
  - "log/lifecycle-run-report_20260629_162739.md"
created_at: "2026-06-29T18:45:00Z"
updated_at: "2026-06-29T18:45:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "needs_review"
related_concepts: []
related_entities: []
review_flags: []
---

# Phase 1 placeholder replacement

## Definition

Tracks placeholder ingest-analysis files that should be replaced or superseded by substantive group/source analysis.

## Operating Rules

```yaml
rules:
  - "Lint should detect placeholder analysis before Phase 2 reliance."
```

## Relationships

```yaml
parent_summary: "wiki/summaries/source-quality-and-custody.md"
source_refs:
  - "ingest-analysis/"
  - "log/lifecycle-run-report_20260629_162739.md"
```

## Evidence

```yaml
evidence:
  - supports: "Concept compiled from approved Phase 1 grouped analysis and Phase 2 summary layer."
    source_pointer: "Phase 1 grouped analysis / source-quality-and-custody"
```

## Contradictions and Open Questions

```yaml
contradictions: []
open_questions:
  - "Needs post-save deterministic lint/index rebuild and optional source-specific backfill before use as final playbook rule."
```
```


## 8. Recommended next postflight

```powershell
python apex-meta\scripts\apex_kb.py --kb-root apex-meta\kb\lika-verein-taxes-accounting --json index --write
python apex-meta\scripts\apex_kb.py --kb-root apex-meta\kb\lika-verein-taxes-accounting --json lint
python apex-meta\scripts\apex_kb.py --kb-root apex-meta\kb\lika-verein-taxes-accounting --json audit
python apex-meta\scripts\apex_kb.py --kb-root apex-meta\kb\lika-verein-taxes-accounting --json status
```

## 9. Final assessment

```yaml
final_assessment:
  are_steps_amazingly_valuable: true_with_qualification
  why:
    - "They convert a raw, noisy, duplicated, partly table-heavy corpus into a reusable knowledge-routing layer."
    - "They preserve unresolved risk instead of producing false certainty."
    - "They create a deterministic next compile target from the deferred concept list."
  qualification:
    - "The current Lika KB is not yet a tax/accounting playbook. It is a source-grounded navigation and risk-control layer."
    - "The next quality jump requires postflight lint/index and source-specific backfill for high-risk pages."
```
