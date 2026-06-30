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
