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
