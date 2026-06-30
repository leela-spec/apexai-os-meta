---
title: "Query: Verein Steuer Buchhaltung Spenden Rechnung Gemeinnützigkeit"
page_type: query_output
kb_slug: "lika-verein-taxes-accounting"
created_at: "2026-06-30T15:10:16Z"
confidence: "unknown"
claim_label: "source_backed_summary"
status: "active"
---

# Query: Verein Steuer Buchhaltung Spenden Rechnung Gemeinnützigkeit

- KB: `lika-verein-taxes-accounting`
- Backend: `sqlite_fts5_bm25`
- Stale status: `fresh`
- Generated: `2026-06-30T15:10:16Z`

## Evidence results

### 1. E-Rechnung for a Verein

- Path: `wiki/concepts/e-rechnung-verein.md`
- Heading: `E-Rechnung for a Verein`
- Lines: `18-19`
- Confidence: `medium`
- Claim label: `source_backed_summary`

> # E-[Rechnung] for a [Verein]

### 2. E-Rechnung for a Verein

- Path: `wiki/concepts/e-rechnung-verein.md`
- Heading: `What this is`
- Lines: `20-23`
- Confidence: `medium`
- Claim label: `source_backed_summary`

> ## What this is  Structured electronic invoice relevance for a [Verein], especially where Lika acts in an entrepreneurial area.

### 3. E-Rechnung for a Verein

- Path: `wiki/concepts/e-rechnung-verein.md`
- Heading: `Practical implication for Lika`
- Lines: `24-27`
- Confidence: `medium`
- Claim label: `source_backed_summary`

> ## Practical implication for Lika  Use as an e-invoice readiness decision node. Split entrepreneurial and non-entrepreneurial [Verein] areas before applying B2B e-invoice assumptions.

### 4. Bundesministerium der Finanzen

- Path: `wiki/entities/bmf.md`
- Heading: `Pages depending on it`
- Lines: `24-29`
- Confidence: `high`
- Claim label: `source_backed_summary`

> ## Pages depending on it  - `wiki/summaries/core-tax-law-invoicing-gobd.md` - `wiki/concepts/e-[rechnung]-[verein].md` - `wiki/concepts/source-quality-risk.md`

### 5. E-Rechnung for a Verein

- Path: `wiki/concepts/e-rechnung-verein.md`
- Heading: `Review posture`
- Lines: `32-34`
- Confidence: `medium`
- Claim label: `source_backed_summary`

> ## Review posture  Confidence: `medium`. Status: `needs_review`. Claims derived from grouped analysis should be backfilled with source-specific page pointers where this concept becomes operationally critical.

### 6. E-Rechnung for a Verein

- Path: `wiki/concepts/e-rechnung-verein.md`
- Heading: `Source basis`
- Lines: `28-31`
- Confidence: `medium`
- Claim label: `source_backed_summary`

> ## Source basis  This page is compiled from `ingest-analysis/group-1-core-tax-law.analysis.md` and should be read as a Phase 2 navigation layer over the ... 

### 7. Phase 2 Minimal Summary Layer Chat Output

- Path: `wiki/Phase2_MinimalSummaryLayer.md`
- Heading: `FILE: `apex-meta/kb/lika-verein-taxes-accounting/wiki/summaries/core-tax-law-invoicing-gobd.md``
- Lines: `46-197`
- Confidence: `unknown`
- Claim label: `raw_source`

> # FILE: `apex-meta/kb/lika-[verein]-taxes-accounting/wiki/summaries/core-tax-law-invoicing-gobd.md`  ````markdown --- title: "Core Tax Law, Invoicing, E-[Rechnung], and GoBD" page_type ... 

### 8. Core Tax Law, Invoicing, E-Rechnung, and GoBD

- Path: `wiki/summaries/core-tax-law-invoicing-gobd.md`
- Heading: `Core Summary`
- Lines: `48-57`
- Confidence: `medium`
- Claim label: `source_backed_summary`

>  ... The BMF E-[Rechnung] FAQ is relevant for 2025+ e-invoicing, especially for distinguishing structured electronic invoices from PDFs and for separating a [Verein]’s entrepreneurial and non ... 

## Raw JSON

```json
{
  "backend": "sqlite_fts5_bm25",
  "fallback_error": null,
  "generated_at": "2026-06-30T15:10:16Z",
  "kb_slug": "lika-verein-taxes-accounting",
  "policy": "read_only; derived indexes are not canonical",
  "query": "Verein Steuer Buchhaltung Spenden Rechnung Gemeinnützigkeit",
  "result_count": 8,
  "results": [
    {
      "chunk_id": "d0e22ca3ba3f5c49911e5d4b",
      "claim_label": "source_backed_summary",
      "confidence": "medium",
      "end_line": 19,
      "heading": "E-Rechnung for a Verein",
      "kb_slug": "lika-verein-taxes-accounting",
      "page_type": "concept",
      "rel_path": "wiki/concepts/e-rechnung-verein.md",
      "score": -6.687360999444612,
      "snippet": "# E-[Rechnung] for a [Verein]",
      "start_line": 18,
      "status": "needs_review",
      "title": "E-Rechnung for a Verein"
    },
    {
      "chunk_id": "9d0c884b698ae70f83912045",
      "claim_label": "source_backed_summary",
      "confidence": "medium",
      "end_line": 23,
      "heading": "What this is",
      "kb_slug": "lika-verein-taxes-accounting",
      "page_type": "concept",
      "rel_path": "wiki/concepts/e-rechnung-verein.md",
      "score": -5.53611344593469,
      "snippet": "## What this is\n\nStructured electronic invoice relevance for a [Verein], especially where Lika acts in an entrepreneurial area.",
      "start_line": 20,
      "status": "needs_review",
      "title": "E-Rechnung for a Verein"
    },
    {
      "chunk_id": "a0914f620fd056d7392508ae",
      "claim_label": "source_backed_summary",
      "confidence": "medium",
      "end_line": 27,
      "heading": "Practical implication for Lika",
      "kb_slug": "lika-verein-taxes-accounting",
      "page_type": "concept",
      "rel_path": "wiki/concepts/e-rechnung-verein.md",
      "score": -5.376709842511207,
      "snippet": "## Practical implication for Lika\n\nUse as an e-invoice readiness decision node. Split entrepreneurial and non-entrepreneurial [Verein] areas before applying B2B e-invoice assumptions.",
      "start_line": 24,
      "status": "needs_review",
      "title": "E-Rechnung for a Verein"
    },
    {
      "chunk_id": "2216ba247a253cf7320366a4",
      "claim_label": "source_backed_summary",
      "confidence": "high",
      "end_line": 29,
      "heading": "Pages depending on it",
      "kb_slug": "lika-verein-taxes-accounting",
      "page_type": "entity",
      "rel_path": "wiki/entities/bmf.md",
      "score": -5.03160538356155,
      "snippet": "## Pages depending on it\n\n- `wiki/summaries/core-tax-law-invoicing-gobd.md`\n- `wiki/concepts/e-[rechnung]-[verein].md`\n- `wiki/concepts/source-quality-risk.md`",
      "start_line": 24,
      "status": "active",
      "title": "Bundesministerium der Finanzen"
    },
    {
      "chunk_id": "56e1fe01977233df411f4aa0",
      "claim_label": "source_backed_summary",
      "confidence": "medium",
      "end_line": 34,
      "heading": "Review posture",
      "kb_slug": "lika-verein-taxes-accounting",
      "page_type": "concept",
      "rel_path": "wiki/concepts/e-rechnung-verein.md",
      "score": -4.987558303653131,
      "snippet": "## Review posture\n\nConfidence: `medium`. Status: `needs_review`. Claims derived from grouped analysis should be backfilled with source-specific page pointers where this concept becomes operationally critical.",
      "start_line": 32,
      "status": "needs_review",
      "title": "E-Rechnung for a Verein"
    },
    {
      "chunk_id": "d2ad572c42430e5eccb41015",
      "claim_label": "source_backed_summary",
      "confidence": "medium",
      "end_line": 31,
      "heading": "Source basis",
      "kb_slug": "lika-verein-taxes-accounting",
      "page_type": "concept",
      "rel_path": "wiki/concepts/e-rechnung-verein.md",
      "score": -4.661127229823531,
      "snippet": "## Source basis\n\nThis page is compiled from `ingest-analysis/group-1-core-tax-law.analysis.md` and should be read as a Phase 2 navigation layer over the ... ",
      "start_line": 28,
      "status": "needs_review",
      "title": "E-Rechnung for a Verein"
    },
    {
      "chunk_id": "6e0168ea906a421c310ba696",
      "claim_label": "raw_source",
      "confidence": "unknown",
      "end_line": 197,
      "heading": "FILE: `apex-meta/kb/lika-verein-taxes-accounting/wiki/summaries/core-tax-law-invoicing-gobd.md`",
      "kb_slug": "lika-verein-taxes-accounting",
      "page_type": "audit_item",
      "rel_path": "wiki/Phase2_MinimalSummaryLayer.md",
      "score": -4.647343800974329,
      "snippet": "# FILE: `apex-meta/kb/lika-[verein]-taxes-accounting/wiki/summaries/core-tax-law-invoicing-gobd.md`\n\n````markdown\n---\ntitle: \"Core Tax Law, Invoicing, E-[Rechnung], and GoBD\"\npage_type ... ",
      "start_line": 46,
      "status": "active",
      "title": "Phase 2 Minimal Summary Layer Chat Output"
    },
    {
      "chunk_id": "ae1d3ffcffb8e6bd341ea723",
      "claim_label": "source_backed_summary",
      "confidence": "medium",
      "end_line": 57,
      "heading": "Core Summary",
      "kb_slug": "lika-verein-taxes-accounting",
      "page_type": "summary",
      "rel_path": "wiki/summaries/core-tax-law-invoicing-gobd.md",
      "score": -4.52334682655409,
      "snippet": " ... The BMF E-[Rechnung] FAQ is relevant for 2025+ e-invoicing, especially for distinguishing structured electronic invoices from PDFs and for separating a [Verein]’s entrepreneurial and non ... ",
      "start_line": 48,
      "status": "needs_review",
      "title": "Core Tax Law, Invoicing, E-Rechnung, and GoBD"
    }
  ],
  "stale": {
    "added": [],
    "deleted": [],
    "generated_at": "2026-06-30T15:10:07Z",
    "modified": [],
    "status": "fresh"
  }
}
```
