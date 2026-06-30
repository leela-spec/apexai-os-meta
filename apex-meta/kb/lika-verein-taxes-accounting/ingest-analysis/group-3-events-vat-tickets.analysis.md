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
