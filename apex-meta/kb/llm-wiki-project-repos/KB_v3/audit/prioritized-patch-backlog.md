---
title: "Prioritized Patch Backlog"
page_type: audit_item
kb_slug: "llm-wiki-project-repos"
kb_v3_scope: "apex_kb_lifecycle_patch_backlog"
created_at: "2026-07-06"
status: "needs_review"
confidence: "high"
claim_label: "source_backed_summary"
---

# Prioritized Patch Backlog

## Backlog Summary

This backlog consolidates the strongest patch ideas from the lifecycle-analysis folder. Priority reflects recurring failure frequency, implementation leverage, and source-grounded evidence across the handoff index, failure-learning files, execution audits, update plan, and V2 planning handover.

## Ranked Patches

```yaml
patch_backlog:
  - id: P0-001
    title: "Add generate-source-payload-manifest"
    target: "apex-meta/scripts/apex_kb.py"
    priority: P0
    why: "Creates deterministic payload custody before Phase 0/1/2."
    acceptance: "Stable source-payload-manifest.json with per-file, group, and root SHA-256."

  - id: P0-002
    title: "Accept subcommand-level --allow-write and --json where safe"
    target:
      - "apex-meta/scripts/apex_kb.py"
      - "apex-meta/scripts/apex_kb_retrieval.py"
    priority: P0
    why: "Repeated handovers failed due to flag placement mismatch."
    acceptance: "Canonical and handover-style flag placements both work."

  - id: P0-003
    title: "Make Phase 0 traverse repo-internal pointer_only sources or warn clearly"
    target: "apex-meta/scripts/apex_kb.py"
    priority: P0
    why: "Pointer-only custody produced empty Phase 0 navigation in real runs."
    acceptance: "Accessible pointer_only source paths produce navigation artifacts or explicit pointer-only warnings."

  - id: P0-004
    title: "Enforce target-drift gates in lifecycle indexes"
    target: "Apex KB handover/index prompts"
    priority: P0
    why: "A critical failure ranked domain-only files as lifecycle read-first."
    acceptance: "Read-first lists contain zero domain-only files."

  - id: P1-001
    title: "Add lifecycle state-lock header"
    target: "handover templates"
    priority: P1
    why: "Prevents phase rewind, option sprawl, and executor confusion."
    acceptance: "Each next-step handoff declares lifecycle_position, executor, artifact, output_path, stop_condition."

  - id: P1-002
    title: "Add overlap-aware dirty-file policy"
    target: "handover templates or preflight helper"
    priority: P1
    why: "Unrelated dirt caused false stops."
    acceptance: "Execution continues when dirty files do not overlap touched paths."

  - id: P1-003
    title: "Split wiki_index_status from retrieval_index_status"
    target:
      - "apex-meta/scripts/apex_kb.py"
      - "apex-meta/scripts/apex_kb_retrieval.py"
    priority: P1
    why: "Retrieval freshness and wiki index freshness were confused."
    acceptance: "status/lint report both surfaces distinctly."

  - id: P1-004
    title: "PowerShell-safe JSON output path"
    target: "scripts and command examples"
    priority: P1
    why: "PowerShell redirection caused UTF-16 JSON parse failures."
    acceptance: "JSON captures validate as UTF-8 on PowerShell."

  - id: P2-001
    title: "Add query-eval pack"
    target: "outputs/queries/evals or log/quality-report"
    priority: P2
    why: "KB value depends on answer quality, not only file validity."
    acceptance: "5-10 canned queries answer from index plus minimal page set."

  - id: P2-002
    title: "Add quality/coverage command"
    target: "apex-meta/scripts/apex_kb.py"
    priority: P2
    why: "V2 should measure redundancy, coverage, source-to-page mapping, and claim density."
    acceptance: "quality report lists sources without pages, pages without sources, review flags, and structural density metrics."
```

## Operator Review Questions

```yaml
operator_review:
  - "Should P0-001 source-payload manifest be the next implementation task before more semantic KB runs?"
  - "Should CLI flag compatibility be patched before or together with P0-001?"
  - "Should target-drift gates live in Apex KB skill references, templates, or both?"
  - "Should query-eval be deterministic-only first, or LLM-plus-deterministic from the start?"
```
