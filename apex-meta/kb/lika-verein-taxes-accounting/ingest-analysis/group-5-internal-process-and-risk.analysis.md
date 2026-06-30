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
