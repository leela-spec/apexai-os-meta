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
