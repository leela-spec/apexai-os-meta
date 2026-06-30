---
title: "Noisy, Duplicate, Low-Trust, and Cleanup-Needed Sources"
page_type: ingest_analysis
kb_slug: lika-verein-taxes-accounting
phase: ingest_phase_1
status: operator_review_needed
source_refs:
  - "log/web-clutter-audit_20260629_162739.md"
  - "manifests/phase0/corpus-profile.md"
  - "manifests/phase0/source-priority-candidates.md"
  - "manifests/source-manifest.json"
created_at: "2026-06-29T17:30:00Z"
updated_at: "2026-06-29T17:30:00Z"
confidence: high
claim_label: source_grounded_analysis
phase_2_allowed: false
phase_2_requires: "approve ingest"
---

# Noisy, Duplicate, Low-Trust, and Cleanup-Needed Sources

## source_scope

This group covers web-clutter candidates, duplicate source files, table-heavy PDF conversion risks, manifest/source-inventory gaps, placeholder Phase 1 outputs, and source-quality handling before Phase 2.

## source_quality_notes

```yaml
source_quality_notes:
  - source: "log/web-clutter-audit_20260629_162739.md"
    clutter_status: clean
    usable_sections:
      - "top candidates"
      - "future script improvement"
    suspected_noise_sections: []
    confidence_effect: none
    recommended_action: use_as_filter_not_deletion_list

  - source: "manifests/phase0/corpus-profile.md"
    clutter_status: clean
    usable_sections:
      - "source inventory status"
      - "file counts"
      - "largest files"
      - "duplicate hash groups"
      - "source group summary"
    suspected_noise_sections: []
    confidence_effect: none
    recommended_action: use_as_phase0_navigation_source

  - source: "manifests/phase0/source-priority-candidates.md"
    clutter_status: clean
    usable_sections:
      - "deterministic priority candidates"
    suspected_noise_sections: []
    confidence_effect: none
    recommended_action: use_as_navigation_hint_not_authority_ranking
````

## relevance_summary

This group is essential because the corpus contains many duplicated `raw/notes/...` and `raw/refs/...` pairs, high-noise web captures, table-heavy conversions, and placeholder ingest-analysis files. Phase 2 should not begin until the operator decides whether cleaned snapshots are needed for BMF GoBD, BZSt §50a, Finanzamt NRW, DATEV, IHK pages, and other high-noise captures.

## key_claims

```yaml
key_claims:
  - claim_id: C001
    claim: "The web-clutter audit scanned 77 Markdown files and reported 69 candidates."
    source_pointer: "log/web-clutter-audit_20260629_162739.md lines 3-8"
    confidence: high
    claim_label: source_backed_summary

  - claim_id: C002
    claim: "The web-clutter audit marks AWV GoBD, BMF GoBD, Buergergesellschaft, DATEV, DRV Minijob, Finanzamt NRW, IHK Koblenz, VUT, Vereinswelt, and other sources as high-noise candidates with cookie/datenschutz/impressum/menu/navigation signals."
    source_pointer: "log/web-clutter-audit_20260629_162739.md lines 10-32"
    confidence: high
    claim_label: source_backed_summary

  - claim_id: C003
    claim: "The corpus profile reports no JSON or CSV source inventory present/readable, despite 103 files scanned."
    source_pointer: "manifests/phase0/corpus-profile.md lines 7-18"
    confidence: high
    claim_label: source_backed_summary

  - claim_id: C004
    claim: "The corpus profile reports 81 Markdown files, 16 JSON files, and 6 YAML files."
    source_pointer: "manifests/phase0/corpus-profile.md lines 20-24"
    confidence: high
    claim_label: source_backed_summary

  - claim_id: C005
    claim: "The corpus profile lists multiple duplicate hash groups between raw/notes/New_Research_Taxes_Accounting/HTML-MD and raw/refs equivalents."
    source_pointer: "manifests/phase0/corpus-profile.md lines 53-75"
    confidence: high
    claim_label: source_backed_summary

  - claim_id: C006
    claim: "The lifecycle run report flags three table-heavy PDF conversion risks: IHK Niederbayern Kleinbetragsrechnungen, LfSt Bayern Festveranstaltungen 2025, and AWV Muster-Verfahrensdokumentation Belegablage."
    source_pointer: "log/lifecycle-run-report_20260629_162739.md lines 45-50"
    confidence: high
    claim_label: source_backed_summary
```

## concepts

```yaml
concepts:
  - concept_slug: web-clutter-filter
    label: "Web clutter filter"
    source_refs:
      - "log/web-clutter-audit_20260629_162739.md"

  - concept_slug: duplicate-source-custody
    label: "Duplicate source custody"
    source_refs:
      - "manifests/phase0/corpus-profile.md"
      - "manifests/source-manifest.json"

  - concept_slug: table-heavy-pdf-risk
    label: "Table-heavy PDF extraction risk"
    source_refs:
      - "log/lifecycle-run-report_20260629_162739.md"

  - concept_slug: phase1-placeholder-replacement
    label: "Placeholder Phase 1 analysis replacement"
    source_refs:
      - "ingest-analysis/bmf_faq-e-rechnung.analysis.md"
```

## entities

```yaml
entities:
  - entity_slug: apex-kb-python-layer
    entity_label: "Apex KB deterministic Python layer"
    entity_type: tool
    source_refs:
      - "log/lifecycle-run-report_20260629_162739.md"

  - entity_slug: web-clutter-audit
    entity_label: "Web clutter audit"
    entity_type: artifact
    source_refs:
      - "log/web-clutter-audit_20260629_162739.md"

  - entity_slug: phase0-corpus-profile
    entity_label: "Phase 0 corpus profile"
    entity_type: artifact
    source_refs:
      - "manifests/phase0/corpus-profile.md"
```

## obligations_or_process_implications

```yaml
obligations_or_process_implications:
  - implication_id: O001
    implication: "Phase 2 should use canonical `raw/refs` copies over duplicate `raw/notes/New_Research_Taxes_Accounting/HTML-MD` copies unless the notes copy is explicitly needed."
    source_refs:
      - "manifests/phase0/corpus-profile.md"

  - implication_id: O002
    implication: "High-noise web captures should be excluded from Phase 2 substantive claims until cleaned or reviewed, but should remain in custody."
    source_refs:
      - "log/web-clutter-audit_20260629_162739.md"

  - implication_id: O003
    implication: "Table-heavy claims involving exact thresholds, rows, or category assignment should be verified against PDF/manual table review."
    source_refs:
      - "log/lifecycle-run-report_20260629_162739.md"

  - implication_id: O004
    implication: "Existing placeholder ingest-analysis files should be superseded by substantive group analyses or replaced by source-specific analyses later."
    source_refs:
      - "ingest-analysis/bmf_faq-e-rechnung.analysis.md"
```

## contradictions_or_uncertainties

```yaml
contradictions_or_uncertainties:
  - id: U001
    issue: "Phase 0 reported 'likely_generated_or_noise_files: none detected' while the separate web-clutter audit reports 69 candidates."
    source_refs:
      - "manifests/phase0/corpus-profile.md"
      - "log/web-clutter-audit_20260629_162739.md"
    proposed_handling: "treat phase0 profile as structural only; web-clutter audit as noise filter"

  - id: U002
    issue: "Source manifest has 95 entries after delta merge, but Phase 0 scanned 103 files and source-inventory JSON/CSV is absent."
    source_refs:
      - "log/lifecycle-run-report_20260629_162739.md"
      - "manifests/phase0/corpus-profile.md"
    proposed_handling: "deterministic_script_improvement"

  - id: U003
    issue: "Some source IDs exist as both PDF and extracted Markdown; semantic analysis should prefer extractable Markdown but mark table-sensitive claims for PDF verification."
    source_refs:
      - "manifests/source-manifest.json"
      - "log/lifecycle-run-report_20260629_162739.md"
    proposed_handling: "pdf_table_qc"
```

## open_questions

```yaml
open_questions:
  - question_id: Q001
    question: "Should cleaned snapshots be created before Phase 2 for every score=100 web-clutter candidate, or only for high-authority sources?"
    proposed_handling: ask_operator

  - question_id: Q002
    question: "Should Phase 1 produce one group-level analysis per topic, or also backfill one source-specific analysis per P0/P1 source?"
    proposed_handling: ask_operator

  - question_id: Q003
    question: "Should the source-manifest merge create source-inventory.json/csv as a standard deterministic artifact?"
    proposed_handling: planning_task_candidate
```

## recommended_phase2_wiki_pages

```yaml
recommended_phase2_wiki_pages:
  - "wiki/concepts/web-clutter-filter.md"
  - "wiki/concepts/duplicate-source-custody.md"
  - "wiki/concepts/table-heavy-pdf-risk.md"
  - "wiki/concepts/phase1-placeholder-replacement.md"
  - "wiki/summaries/source-quality-and-custody.md"
```

## audit_flags

```yaml
audit_flags:
  - flag_id: A001
    severity: high
    issue: "Do not use BMF GoBD markdown capture as semantic authority without cleanup."
    source_ref: "raw/refs/BMF_GoBD-2024.md"

  - flag_id: A002
    severity: high
    issue: "Do not use BZSt §50a capture for detailed claims without cleanup."
    source_ref: "raw/refs/BZSt_50a-Abzugsteuer.md"

  - flag_id: A003
    severity: medium
    issue: "Duplicate raw/notes and raw/refs sources should be resolved by canonical source policy before Phase 2."
    source_ref: "manifests/phase0/corpus-profile.md"

  - flag_id: A004
    severity: medium
    issue: "Table-heavy PDF conversion needs QC for LfSt Bayern, AWV, and IHK Niederbayern."
    source_ref: "log/lifecycle-run-report_20260629_162739.md"
```

## source_refs

```yaml
source_refs:
  - "log/web-clutter-audit_20260629_162739.md"
  - "manifests/phase0/corpus-profile.md"
  - "manifests/phase0/source-priority-candidates.md"
  - "manifests/source-manifest.json"
  - "log/lifecycle-run-report_20260629_162739.md"
  - "ingest-analysis/bmf_faq-e-rechnung.analysis.md"
```

## confidence

```yaml
confidence: high
rationale:
  - "This artifact mainly analyzes deterministic quality metadata, not tax law."
  - "Lifecycle, web clutter, and corpus profile reports were directly inspected."
```

## stop_status

```yaml
stop_status:
  phase: ingest_phase_1
  status: operator_review_needed
  phase_2_allowed: false
  phase_2_requires: "approve ingest"
```
