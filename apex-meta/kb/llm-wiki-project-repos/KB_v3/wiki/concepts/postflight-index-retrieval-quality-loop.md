---
title: "Postflight Index Retrieval Quality Loop"
page_type: concept
kb_slug: "llm-wiki-project-repos"
concept_slug: "postflight-index-retrieval-quality-loop"
created_at: "2026-07-06"
status: "active"
confidence: "high"
claim_label: "source_backed_summary"
---

# Postflight Index Retrieval Quality Loop

## Definition

The postflight loop makes semantic KB output usable: rebuild wiki index, rebuild retrieval index, test stale status, lint/audit structure, and run query simulations. The lifecycle-analysis folder shows that wiki index freshness and retrieval freshness are separate surfaces and must not be conflated.

## Required Order

```yaml
postflight_order:
  - "apex_kb.py index --allow-write"
  - "apex_kb_retrieval.py build-index --allow-write"
  - "apex_kb_retrieval.py stale"
  - "apex_kb.py lint"
  - "apex_kb.py audit"
  - "apex_kb.py status"
  - "query simulations and saved query packets when useful"
```

## Known Failure Patterns

```yaml
failures:
  - id: PF-001
    issue: "retrieval stale reported fresh while wiki index was stale"
    cause: "wiki index and retrieval index are distinct derived artifacts"
  - id: PF-002
    issue: "real-surface lint findings could look like task failure"
    cause: "finding-producing audits need report-only mode or clear exit semantics"
  - id: PF-003
    issue: "Phase 2 outputs existed remotely but not locally"
    cause: "local/origin synchronization not verified before failure report"
```

## Patch Ideas

```yaml
patches:
  - id: PF-001
    title: "Split wiki_index_status and retrieval_index_status"
    priority: P0
    target:
      - "apex-meta/scripts/apex_kb.py"
      - "apex-meta/scripts/apex_kb_retrieval.py"
    acceptance: "status/lint distinguish stale wiki index from stale retrieval index."
  - id: PF-002
    title: "Add report-only lint mode"
    priority: P1
    target: "apex-meta/scripts/apex_kb.py"
    acceptance: "Surface scans can record findings without failing the whole task."
  - id: PF-003
    title: "Add query eval pack"
    priority: P1
    target: "KB outputs/queries/evals or log/quality-report"
    acceptance: "Each KB has 5-10 canned query simulations from index + minimal page set."
  - id: PF-004
    title: "Add coverage dashboard"
    priority: P2
    target: "deterministic quality/coverage command"
    acceptance: "Reports sources without pages, pages without sources, review flags by source."
```

## Routes Here

Use this concept after Phase 2 wiki updates and before claiming the KB is query-ready.
