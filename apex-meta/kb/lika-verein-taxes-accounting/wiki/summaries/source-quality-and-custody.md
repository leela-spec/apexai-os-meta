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
