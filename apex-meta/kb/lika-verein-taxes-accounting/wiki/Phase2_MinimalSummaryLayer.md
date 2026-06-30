Phase 2 gate accepted. I reloaded the live `apex-kb` skill contract and the saved Phase 1 artifact instead of relying on memory. The skill contract requires Phase 2 only after `approve ingest`, and Phase 2 may draft/update `wiki/summaries/`, `wiki/concepts/`, `wiki/entities/`, audit items, and semantic index sections with source pointers and confidence labels.

I am producing this as **chat-output only**. I did **not** write repo files. The current repo wiki index still has compiled page count `0` and “No LLM summary has been approved yet,” so the index block below is the intended Phase 2 replacement content.

---

# Phase 2 artifact set

```yaml
phase2_compile:
  kb_slug: lika-verein-taxes-accounting
  output_mode: chat_output_only
  generated_at: "2026-06-29T18:00:00Z"
  source_basis:
    - saved_phase_1_grouped_ingest_analysis
    - installed_apex_kb_contract
    - wiki_page_templates
  limitation:
    - "Phase 1 was grouped and sampled; not all 95/103 sources were read end-to-end."
    - "High-noise and table-heavy sources remain marked needs_review."
  artifacts:
    - "wiki/summaries/core-tax-law-invoicing-gobd.md"
    - "wiki/summaries/association-accounting-process.md"
    - "wiki/summaries/events-vat-tickets.md"
    - "wiki/summaries/artist-contractor-obligations.md"
    - "wiki/summaries/source-judgment-and-open-risks.md"
    - "wiki/summaries/source-quality-and-custody.md"
    - "wiki/index.md"
    - "log/llm-phase2-report_20260629_180000.md"
```

---

# FILE: `apex-meta/kb/lika-verein-taxes-accounting/wiki/summaries/core-tax-law-invoicing-gobd.md`

````markdown
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

````

---

# FILE: `apex-meta/kb/lika-verein-taxes-accounting/wiki/summaries/association-accounting-process.md`

```markdown
---
title: "Association Accounting Process and Receipt Custody"
page_type: summary
kb_slug: "lika-verein-taxes-accounting"
summary_slug: "association-accounting-process"
source_refs:
  - source_id: "raw-refs-awv-muster-verfahrensdokumentation-belegablage-md"
    source_path: "raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.md"
    source_hash: "362270a8ffe6c5f9b3e7493ac02fc2ebdd9443711d9cbbc0abf66c06c4e1a0c7"
    source_pointer: "Phase 1: group-2-association-accounting.analysis.md / key_claims C001-C004"
    source_storage_mode: "copy_into_kb"
  - source_id: "raw-notes-judgementofsources-md"
    source_path: "raw/notes/JudgementOfSources.md"
    source_hash: "98d6049ca76d470a4713a041f6bab67b45707d6616133cb7fda42aca1a3d1dbc"
    source_pointer: "Phase 1: group-2-association-accounting.analysis.md / key_claim C005"
    source_storage_mode: "copy_into_kb"
created_at: "2026-06-29T18:00:00Z"
updated_at: "2026-06-29T18:00:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "needs_review"
related_concepts:
  - "belegfunktion"
  - "accounting-source-custody"
  - "reimbursement-evidence"
related_entities:
  - "awv"
  - "datev"
  - "deutsches-ehrenamt"
review_flags:
  - "DATEV SKR42 and DATEV GoBD sources require cleaned extraction before account-mapping claims."
  - "Gemeinnützigkeit-specific sources must not be transferred blindly to Lika."
---

# Association Accounting Process and Receipt Custody

## Core Summary

This page defines the accounting-process layer of the KB: not tax conclusions, but source custody and bookkeeping evidence flow.

The AWV Belegablage source supports a structured process for all documents with receipt or evidence function. Relevant records should be handled systematically, completely, timely, orderly, and unchanged. The process needs to cover the full path from receipt creation/entry and identification to secure filing, bookkeeping handoff, and eventual destruction after retention periods.

For Lika, the immediate Phase 2 value is a durable operating model:

1. identify incoming/outgoing receipt sources;
2. classify whether each document has Belegfunktion;
3. preserve original digital or paper evidence as required;
4. connect each payment/revenue item to a stored receipt;
5. hand off records to the bookkeeper/tax advisor in a repeatable cadence;
6. preserve open questions and high-risk cases separately.

## What This Adds

```yaml
adds:
  - "A process-level accounting page separate from legal/tax interpretation."
  - "A custody-first model for receipts, reimbursements, platform exports, and contracts."
  - "A warning that account mapping must wait for cleaned DATEV/SKR42 sources."

clarifies:
  - "AWV is useful for Belegablage workflow."
  - "JudgementOfSources.md is a meta-source for curation and risk framing, not legal authority."
  - "Generic Verein accounting sources must be marked with transfer-safety warnings."

limits:
  - "No final SKR42 mapping is established."
  - "No concrete reimbursement policy is finalized."
  - "No claim is made that all association-accounting sources apply to a non-gemeinnützig event context."
````

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Ordered and secure receipt custody is a basis for evidentiary strength of bookkeeping and records."
    source_pointer: "raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.md lines 39-45, via Phase 1 group-2 C001"
    confidence: "medium"
    claim_label: "source_backed_summary"
    used_in_pages:
      - "wiki/concepts/accounting-source-custody.md"

  - claim_id: C002
    claim: "Retention-relevant records should be filed systematically, completely, timely, orderly, and unchanged."
    source_pointer: "raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.md lines 47-53, via Phase 1 group-2 C002"
    confidence: "medium"
    claim_label: "source_backed_summary"
    used_in_pages:
      - "wiki/concepts/belegfunktion.md"

  - claim_id: C003
    claim: "The accounting process should cover the full workflow from receipt creation/entry and identification through filing and destruction after retention periods."
    source_pointer: "raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.md lines 51-55, via Phase 1 group-2 C003"
    confidence: "medium"
    claim_label: "source_backed_summary"
    used_in_pages:
      - "wiki/concepts/accounting-source-custody.md"

  - claim_id: C004
    claim: "The current source base is usable but not yet playbook-ready because several tax/event gaps remain unresolved."
    source_pointer: "raw/notes/JudgementOfSources.md lines 3-20, via Phase 1 group-2 C005"
    confidence: "medium"
    claim_label: "source_backed_summary"
    used_in_pages:
      - "wiki/summaries/source-judgment-and-open-risks.md"
```

## Contradictions

```yaml
contradictions:
  - id: U001
    issue: "Association-accounting sources may assume gemeinnützigkeit, while the project note treats Lika/Safer Space as non-gemeinnützig with economic operations."
    handling: "Mark such sources conditional until operator/tax-advisor review."
    confidence: "medium"

  - id: U002
    issue: "DATEV/SKR42 sources are relevant but not clean enough for detailed account mapping."
    handling: "Create cleaned snapshots before operational chart-of-account pages."
    confidence: "medium"
```

## Open Questions

```yaml
open_questions:
  - question_id: Q001
    question: "Which exact chart of accounts or SKR42 subset will Lika use?"
    handling: "planning_task_candidate"

  - question_id: Q002
    question: "Which receipts are retained as original digital files, scans, and paper originals?"
    handling: "process_design"

  - question_id: Q003
    question: "Which payments are internal volunteer reimbursements versus contractor payments?"
    handling: "operator_review"
```

````

---

# FILE: `apex-meta/kb/lika-verein-taxes-accounting/wiki/summaries/events-vat-tickets.md`

```markdown
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

````

---

# FILE: `apex-meta/kb/lika-verein-taxes-accounting/wiki/summaries/artist-contractor-obligations.md`

```markdown
---
title: "Artists, Contractors, KSK, Foreign Artists, §50a, and Reverse Charge"
page_type: summary
kb_slug: "lika-verein-taxes-accounting"
summary_slug: "artist-contractor-obligations"
source_refs:
  - source_id: "raw-refs-drv-k5001-kuenstlersozialabgabe-md"
    source_path: "raw/refs/DRV_K5001_Kuenstlersozialabgabe.md"
    source_hash: "a51afa72dc657ca9b935ef9518cd82ef88d541fb23e77202e648eb890fb5199e"
    source_pointer: "Phase 1: group-4-artist-contractor-obligations.analysis.md / key_claims C001-C006"
    source_storage_mode: "copy_into_kb"
  - source_id: "raw-refs-lfst-bayern-merkblatt-festveranstaltungen-2025-md"
    source_path: "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md"
    source_hash: "9273c60a549644f072463b4ee212afef39ee5f8072404dfcf8bcca3219125d8c"
    source_pointer: "Phase 1: group-4-artist-contractor-obligations.analysis.md / key_claims C007-C008"
    source_storage_mode: "copy_into_kb"
  - source_id: "raw-refs-bzst-50a-abzugsteuer-md"
    source_path: "raw/refs/BZSt_50a-Abzugsteuer.md"
    source_hash: "8974e947b5eba1862cc6ddc6a328ada0ebc18c3e5a68fbe3cd8ca6adc783bb97"
    source_pointer: "Phase 1: group-4-artist-contractor-obligations.analysis.md / source_quality_notes"
    source_storage_mode: "copy_into_kb"
created_at: "2026-06-29T18:00:00Z"
updated_at: "2026-06-29T18:00:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "needs_review"
related_concepts:
  - "kuenstlersozialabgabe-event"
  - "foreign-artist-50a"
  - "artist-contract-source-of-truth"
  - "foreign-artist-vat-recipient-liability"
related_entities:
  - "deutsche-rentenversicherung"
  - "kuenstlersozialkasse"
  - "bzst"
review_flags:
  - "Foreign artist payment workflow must be separate from domestic contractor workflow."
  - "KSK requires annual payment ledger and contract-counterparty clarity."
  - "BZSt §50a source requires cleaned snapshot before detailed page."
---

# Artists, Contractors, KSK, Foreign Artists, §50a, and Reverse Charge

## Core Summary

This page is the main risk page for artist and contractor payments.

The DRV K5001 source is the strongest inspected source for Künstlersozialabgabe. It supports the conclusion that associations can be liable, that gemeinnützigkeit does not eliminate KSK exposure, and that payments to self-employed artists or publicists should be tracked. It also supports an annual ledger model, including payments and relevant incidental/reimbursed costs, with certain exclusions only if separately shown.

Foreign artist payments require separate handling. The LfSt Bayern event source indicates that foreign artists can create VAT-recipient liability questions and §50a withholding questions independent of the Verein’s own tax status. The BZSt §50a source is authoritative in type, but the current capture is too noisy for detailed extraction.

## What This Adds

```yaml
adds:
  - "A distinct artist/contractor workflow separate from normal domestic expenses."
  - "A KSK annual payment ledger requirement."
  - "A foreign-artist review lane for §50a and VAT-recipient liability."

clarifies:
  - "KSK cannot be handled only through contract wording."
  - "Agency/manager/payment-chain cases require exact counterparty review."
  - "Foreign artist workflows are not the same as domestic contractor workflows."

limits:
  - "This page does not decide whether a concrete artist invoice triggers KSK, §50a, VAT, or employment classification."
  - "BZSt §50a details need a cleaned source snapshot."
  - "Foreign artist VAT rate/exemption/reverse-charge treatment requires case facts."
````

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Private companies, public-law bodies, registered associations, and other groups can be liable for Künstlersozialabgabe."
    source_pointer: "raw/refs/DRV_K5001_Kuenstlersozialabgabe.md lines 13-16, via Phase 1 group-4 C001"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages:
      - "wiki/concepts/kuenstlersozialabgabe-event.md"

  - claim_id: C002
    claim: "Recognized gemeinnützigkeit does not remove Künstlersozialabgabe liability."
    source_pointer: "raw/refs/DRV_K5001_Kuenstlersozialabgabe.md lines 13-16, via Phase 1 group-4 C002"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages:
      - "wiki/concepts/kuenstlersozialabgabe-event.md"
      - "wiki/concepts/transfer-safety.md"

  - claim_id: C003
    claim: "DRV K5001 gives annual de-minimis thresholds of 450 EUR through 2024, 700 EUR in 2025, and 1,000 EUR from 2026."
    source_pointer: "raw/refs/DRV_K5001_Kuenstlersozialabgabe.md lines 49-53, via Phase 1 group-4 C004"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages:
      - "wiki/concepts/kuenstlersozialabgabe-event.md"

  - claim_id: C004
    claim: "Payments to foreign-resident artists/publicists are also recorded and reported for KSK purposes."
    source_pointer: "raw/refs/DRV_K5001_Kuenstlersozialabgabe.md lines 119-128, via Phase 1 group-4 C006"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages:
      - "wiki/concepts/kuenstlersozialabgabe-event.md"

  - claim_id: C005
    claim: "Foreign artists at a festival event may create VAT-recipient liability and §50a withholding questions for the Verein."
    source_pointer: "raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md lines 87-119 in fetched continuation, via Phase 1 group-4 C007-C008"
    confidence: "medium"
    claim_label: "source_backed_summary"
    used_in_pages:
      - "wiki/concepts/foreign-artist-50a.md"
      - "wiki/concepts/foreign-artist-vat-recipient-liability.md"
```

## Contradictions

```yaml
contradictions:
  - id: U001
    issue: "BZSt §50a source is likely authoritative but current Markdown capture is noisy."
    handling: "Do not create detailed §50a operational instructions until cleaned."
    confidence: "medium"

  - id: U002
    issue: "Agency/manager chains complicate who is contract counterparty and who owes what."
    handling: "Require contract-counterparty review for artist payments."
    confidence: "medium"
```

## Open Questions

```yaml
open_questions:
  - question_id: Q001
    question: "Will Lika pay foreign artists, domestic self-employed artists, agencies, collectives, GmbHs, or private hobby/amateur performers?"
    handling: "operator_inventory"

  - question_id: Q002
    question: "Which 2025/2026 artist and creative-service payments exceed KSK thresholds?"
    handling: "ledger_build"

  - question_id: Q003
    question: "Which invoices separately state VAT, travel, hospitality, GEMA, or other exclusions?"
    handling: "audit_item"
```

````

---

# FILE: `apex-meta/kb/lika-verein-taxes-accounting/wiki/summaries/source-judgment-and-open-risks.md`

```markdown
---
title: "Source Judgment and Open Tax/Accounting Risks"
page_type: summary
kb_slug: "lika-verein-taxes-accounting"
summary_slug: "source-judgment-and-open-risks"
source_refs:
  - source_id: "raw-notes-judgementofsources-md"
    source_path: "raw/notes/JudgementOfSources.md"
    source_hash: "98d6049ca76d470a4713a041f6bab67b45707d6616133cb7fda42aca1a3d1dbc"
    source_pointer: "Phase 1: group-5-internal-process-and-risk.analysis.md / key_claims C001-C004 and audit_flags A001-A003"
    source_storage_mode: "copy_into_kb"
created_at: "2026-06-29T18:00:00Z"
updated_at: "2026-06-29T18:00:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "needs_review"
related_concepts:
  - "source-authority-hierarchy"
  - "transfer-safety"
  - "unresolved-tax-risk-register"
  - "venue-settlement-gap"
related_entities:
  - "lika-verein"
  - "safer-space"
review_flags:
  - "JudgementOfSources.md is a meta-source and not legal authority."
  - "Venue settlement / Mindestbarumsatz remains unresolved."
  - "7% versus 19% for mixed cultural/club events remains unresolved."
  - "Ticket-as-invoice remains unresolved."
---

# Source Judgment and Open Tax/Accounting Risks

## Core Summary

This page records the KB’s meta-risk layer.

The source base is usable but not yet playbook-ready. The highest-risk unresolved gaps are:

1. venue settlement / Mindestbarumsatz / Barumsatzgarantie;
2. concrete 7%-versus-19% VAT treatment for club/DJ/cultural mixed formats;
3. whether platform tickets/receipts satisfy invoice or small-invoice requirements in Lika’s actual workflow.

This page must not be treated as legal authority. Its role is curation, ranking, risk framing, and Phase 2 warning placement.

## What This Adds

```yaml
adds:
  - "A central risk register for unresolved tax/accounting questions."
  - "A source-authority hierarchy requirement."
  - "A transfer-safety warning for generic Verein/gemeinnützigkeit/Zweckbetrieb sources."

clarifies:
  - "Internal notes can guide KB design but cannot decide legal/tax questions."
  - "Pages involving gemeinnützigkeit, donations, or Zweckbetrieb require explicit applicability warnings."
  - "Operational checklists should not be finalized until high-risk gaps are marked or resolved."

limits:
  - "No final tax conclusion is produced."
  - "No unresolved gap is silently resolved."
  - "No internal note is promoted to authority."
````

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "The source base is usable but not yet playbook-ready."
    source_pointer: "raw/notes/JudgementOfSources.md lines 3-9, via Phase 1 group-5 C001"
    confidence: "medium"
    claim_label: "source_backed_summary"
    used_in_pages:
      - "wiki/summaries/source-judgment-and-open-risks.md"

  - claim_id: C002
    claim: "The largest open gaps include venue settlement/Mindestbarumsatz, 7%-vs-19% VAT for mixed club/DJ/cultural formats, and ticket-as-invoice."
    source_pointer: "raw/notes/JudgementOfSources.md lines 3-20, via Phase 1 group-5 C002"
    confidence: "medium"
    claim_label: "source_backed_summary"
    used_in_pages:
      - "wiki/concepts/unresolved-tax-risk-register.md"

  - claim_id: C003
    claim: "Sources with gemeinnützigkeit, Zweckbetrieb, or donation logic are risky for direct transfer where the project context is non-gemeinnützig with economic operations."
    source_pointer: "raw/notes/JudgementOfSources.md lines 5-8, via Phase 1 group-5 C003"
    confidence: "medium"
    claim_label: "source_backed_summary"
    used_in_pages:
      - "wiki/concepts/transfer-safety.md"
```

## Contradictions

```yaml
contradictions:
  - id: U001
    issue: "Some sources are useful but assume tax-privileged association contexts."
    handling: "Use transfer-safety markers on relevant pages."
    confidence: "medium"

  - id: U002
    issue: "JudgementOfSources.md is useful for ranking and curation but not legal authority."
    handling: "Keep as meta-source only."
    confidence: "high"
```

## Open Questions

```yaml
open_questions:
  - question_id: Q001
    question: "Is Lika non-gemeinnützig for all relevant event/tax workflows, or are any sub-activities tax-privileged?"
    handling: "operator_or_tax_advisor_review"

  - question_id: Q002
    question: "Should high-risk pages carry a standard tax-advisor-review banner?"
    handling: "template_decision"

  - question_id: Q003
    question: "Which unresolved gap gets researched first: venue settlement, VAT rate, ticket invoice, or foreign artist obligations?"
    handling: "priority_decision"
```

````

---

# FILE: `apex-meta/kb/lika-verein-taxes-accounting/wiki/summaries/source-quality-and-custody.md`

```markdown
---
title: "Source Quality, Web Clutter, Duplicates, and Custody"
page_type: summary
kb_slug: "lika-verein-taxes-accounting"
summary_slug: "source-quality-and-custody"
source_refs:
  - source_id: "log-web-clutter-audit-20260629-162739"
    source_path: "log/web-clutter-audit_20260629_162739.md"
    source_hash: "NA"
    source_pointer: "Phase 1: group-6-noisy-or-low-trust-sources.analysis.md / key_claims C001-C002"
    source_storage_mode: "copy_into_kb"
  - source_id: "manifests-phase0-corpus-profile"
    source_path: "manifests/phase0/corpus-profile.md"
    source_hash: "NA"
    source_pointer: "Phase 1: group-6-noisy-or-low-trust-sources.analysis.md / key_claims C003-C005"
    source_storage_mode: "copy_into_kb"
  - source_id: "log-lifecycle-run-report-20260629-162739"
    source_path: "log/lifecycle-run-report_20260629_162739.md"
    source_hash: "NA"
    source_pointer: "Phase 1: group-6-noisy-or-low-trust-sources.analysis.md / key_claim C006"
    source_storage_mode: "copy_into_kb"
created_at: "2026-06-29T18:00:00Z"
updated_at: "2026-06-29T18:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "web-clutter-filter"
  - "duplicate-source-custody"
  - "table-heavy-pdf-risk"
  - "phase1-placeholder-replacement"
related_entities:
  - "apex-kb-python-layer"
  - "web-clutter-audit"
  - "phase0-corpus-profile"
review_flags:
  - "High-noise source cleanup should prioritize BMF GoBD, BZSt §50a, Finanzamt NRW, DATEV, and IHK captures."
  - "Duplicate raw/notes and raw/refs copies require canonical-source policy."
  - "Table-heavy PDF conversions require manual/PDF review before exact thresholds or table rows are operationalized."
---

# Source Quality, Web Clutter, Duplicates, and Custody

## Core Summary

This page is the KB’s source-quality control page.

The Phase 0 and Phase 1 process found three structural risks:

1. many high-noise web captures;
2. duplicate source copies between `raw/notes/...` and `raw/refs/...`;
3. table-heavy PDF conversion risks.

The current rule is: keep all source custody, but do not treat high-volume web text as evidence merely because it is long. Prefer canonical `raw/refs` copies where duplicates exist. Create cleaned snapshots for high-authority noisy sources before detailed Phase 2 pages. Verify table-sensitive claims against the original PDF or a better conversion pass.

## What This Adds

```yaml
adds:
  - "A single source-quality and custody page."
  - "A canonical-source policy for duplicate notes/refs pairs."
  - "A cleaned-snapshot queue for noisy high-authority sources."

clarifies:
  - "Web-clutter audit is a filter, not a deletion list."
  - "Phase 0 artifacts are navigation aids, not semantic truth."
  - "Table-heavy claims need PDF/manual review before operational use."

limits:
  - "This page does not delete or rewrite sources."
  - "This page does not decide legal/tax content."
  - "This page does not replace deterministic postflight lint/audit."
````

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "The web-clutter audit scanned 77 Markdown files and reported 69 candidates."
    source_pointer: "log/web-clutter-audit_20260629_162739.md lines 3-8, via Phase 1 group-6 C001"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages:
      - "wiki/concepts/web-clutter-filter.md"

  - claim_id: C002
    claim: "The corpus profile reported no JSON or CSV source inventory present/readable despite 103 files scanned."
    source_pointer: "manifests/phase0/corpus-profile.md lines 7-18, via Phase 1 group-6 C003"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages:
      - "wiki/concepts/duplicate-source-custody.md"

  - claim_id: C003
    claim: "The corpus profile listed duplicate hash groups between raw/notes/New_Research_Taxes_Accounting/HTML-MD and raw/refs equivalents."
    source_pointer: "manifests/phase0/corpus-profile.md lines 53-75, via Phase 1 group-6 C005"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages:
      - "wiki/concepts/duplicate-source-custody.md"

  - claim_id: C004
    claim: "The lifecycle run report flagged IHK Niederbayern, LfSt Bayern, and AWV as table-heavy PDF conversion risks."
    source_pointer: "log/lifecycle-run-report_20260629_162739.md lines 45-50, via Phase 1 group-6 C006"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages:
      - "wiki/concepts/table-heavy-pdf-risk.md"
```

## Contradictions

```yaml
contradictions:
  - id: U001
    issue: "Phase 0 profile reported no likely generated/noise files while web-clutter audit found 69 candidates."
    handling: "Treat Phase 0 profile as structural navigation and web-clutter audit as noise filter."
    confidence: "high"

  - id: U002
    issue: "Manifest entries and scanned file count differ."
    handling: "Record deterministic script/source-inventory improvement."
    confidence: "medium"
```

## Open Questions

```yaml
open_questions:
  - question_id: Q001
    question: "Should cleaned snapshots be created for all score=100 web-clutter candidates or only high-authority sources?"
    handling: "operator_policy_decision"

  - question_id: Q002
    question: "Should future Phase 1 backfill source-specific analysis for P0/P1 sources?"
    handling: "kb_lifecycle_decision"

  - question_id: Q003
    question: "Should source-inventory.json/csv become a mandatory Phase 0 deterministic artifact?"
    handling: "script_improvement"
```

````

---

# FILE: `apex-meta/kb/lika-verein-taxes-accounting/wiki/index.md`

```markdown
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

````

---

# FILE: `apex-meta/kb/lika-verein-taxes-accounting/log/llm-phase2-report_20260629_180000.md`

```markdown
---
title: "LLM Phase 2 Report - Lika Verein Taxes Accounting"
page_type: phase2_report
kb_slug: "lika-verein-taxes-accounting"
phase: ingest_phase_2_wiki_compile
status: chat_output_only
created_at: "2026-06-29T18:00:00Z"
updated_at: "2026-06-29T18:00:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
---

# LLM Phase 2 Report - Lika Verein Taxes Accounting

## execution_summary

The operator supplied the Phase 2 gate phrase in a separate turn after Phase 1 existed.

This report compiles the approved grouped Phase 1 analysis into a minimal, source-grounded Phase 2 wiki layer.

No repository files were written in this chat. All artifacts are chat-output only.

## artifacts_created_in_chat

```yaml
artifacts_created_in_chat:
  - path: "apex-meta/kb/lika-verein-taxes-accounting/wiki/summaries/core-tax-law-invoicing-gobd.md"
    status: "chat_output_only"
  - path: "apex-meta/kb/lika-verein-taxes-accounting/wiki/summaries/association-accounting-process.md"
    status: "chat_output_only"
  - path: "apex-meta/kb/lika-verein-taxes-accounting/wiki/summaries/events-vat-tickets.md"
    status: "chat_output_only"
  - path: "apex-meta/kb/lika-verein-taxes-accounting/wiki/summaries/artist-contractor-obligations.md"
    status: "chat_output_only"
  - path: "apex-meta/kb/lika-verein-taxes-accounting/wiki/summaries/source-judgment-and-open-risks.md"
    status: "chat_output_only"
  - path: "apex-meta/kb/lika-verein-taxes-accounting/wiki/summaries/source-quality-and-custody.md"
    status: "chat_output_only"
  - path: "apex-meta/kb/lika-verein-taxes-accounting/wiki/index.md"
    status: "chat_output_only"
  - path: "apex-meta/kb/lika-verein-taxes-accounting/log/llm-phase2-report_20260629_180000.md"
    status: "chat_output_only"
````

## pages_generated

```yaml
pages_generated:
  summaries:
    - "core-tax-law-invoicing-gobd"
    - "association-accounting-process"
    - "events-vat-tickets"
    - "artist-contractor-obligations"
    - "source-judgment-and-open-risks"
    - "source-quality-and-custody"

  concepts_deferred_to_next_compile_pass:
    - "invoice-core-fields"
    - "kleinbetragsrechnung"
    - "e-rechnung-verein"
    - "belegablage-verfahrensdokumentation"
    - "belegfunktion"
    - "accounting-source-custody"
    - "reimbursement-evidence"
    - "event-business-area-assignment"
    - "event-vat-rate-risk"
    - "ticketing-tax-configuration"
    - "ticket-as-invoice-gap"
    - "kuenstlersozialabgabe-event"
    - "foreign-artist-50a"
    - "artist-contract-source-of-truth"
    - "foreign-artist-vat-recipient-liability"
    - "source-authority-hierarchy"
    - "transfer-safety"
    - "unresolved-tax-risk-register"
    - "venue-settlement-gap"
    - "web-clutter-filter"
    - "duplicate-source-custody"
    - "table-heavy-pdf-risk"
    - "phase1-placeholder-replacement"
```

## source_grounding

```yaml
source_grounding:
  source_basis:
    - "group-1-core-tax-law.analysis.md"
    - "group-2-association-accounting.analysis.md"
    - "group-3-events-vat-tickets.analysis.md"
    - "group-4-artist-contractor-obligations.analysis.md"
    - "group-5-internal-process-and-risk.analysis.md"
    - "group-6-noisy-or-low-trust-sources.analysis.md"

  note: >
    Because Phase 1 used grouped analyses and did not read all 95/103 sources
    end-to-end, this Phase 2 output generates summary pages first. More granular
    concept/entity pages should be compiled after either source-specific Phase 1
    backfill or operator acceptance of grouped-page granularity.
```

## unresolved_risks

```yaml
unresolved_risks:
  - id: R001
    severity: "high"
    title: "7% versus 19% VAT for mixed cultural/club events"
    handling: "tax_advisor_review"

  - id: R002
    severity: "high"
    title: "Ticket-as-invoice / platform receipt evidence"
    handling: "audit_item"

  - id: R003
    severity: "high"
    title: "Venue settlement / Mindestbarumsatz / Barumsatzgarantie"
    handling: "additional_research_or_tax_advisor_review"

  - id: R004
    severity: "medium"
    title: "High-noise BMF/BZSt/DATEV/Finanzamt/IHK captures"
    handling: "cleaned_snapshot_workflow"

  - id: R005
    severity: "medium"
    title: "Table-heavy PDF extraction risk"
    handling: "manual_pdf_or_marker_review"
```

## deterministic_postflight_required_after_saving

```powershell
python apex-meta\scripts\apex_kb.py --kb-root apex-meta\kb\lika-verein-taxes-accounting --json index --write
python apex-meta\scripts\apex_kb.py --kb-root apex-meta\kb\lika-verein-taxes-accounting --json lint
python apex-meta\scripts\apex_kb.py --kb-root apex-meta\kb\lika-verein-taxes-accounting --json audit
python apex-meta\scripts\apex_kb.py --kb-root apex-meta\kb\lika-verein-taxes-accounting --json status
```

## completion_status

```yaml
phase2_status:
  phase_2_wiki_compile_started: true
  minimal_summary_layer_created: true
  concept_entity_backfill_complete: false
  repo_written: false
  deterministic_postflight_run: false
  recommended_local_next_action: "save generated Markdown files, then run deterministic postflight"
```

````

---

# Phase 2 stop/gate status

```yaml
phase_2_gate_status:
  approved: true
  phase2_compile_status: "minimal_summary_layer_created_in_chat"
  repo_write_status: "not_written"
  deterministic_postflight_status: "not_run_from_chat"
  remaining_work:
    - "Save files into the repo."
    - "Run deterministic index/lint/audit/status postflight."
    - "Backfill concept/entity pages if the summary layer is accepted."
````

Phase 2 wiki compilation has started and produced the minimal summary layer in chat output.