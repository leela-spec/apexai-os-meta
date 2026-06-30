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
