---
title: "Deterministic Read-Side Report"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "deterministic-read-side-report"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 86-98; deterministic read-side computation"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-process-retrospective-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase1-process-retrospective-20260702.md"
    source_hash: "8b011af3de9d3dc7ef5859964437603717d4b9a7"
    source_pointer: "lines 77-123; Phase 0 source-routed reports"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Deterministic Read-Side Report

```yaml
pattern: "A deterministic report computes facts about files, indexes, or state without interpreting semantic truth or mutating canonical state."
used_when:
  - "The system needs inventory, status, lint, profile, or navigation facts."
not_used_when:
  - "The task requires judgment-heavy concept extraction or doctrine drafting."
reads:
  - "files"
  - "manifests"
  - "compiled pages"
writes:
  - "derived report"
  - "no semantic doctrine"
token_efficiency:
  - "Reports route the LLM toward small high-signal source sets."
drift_controls:
  - "Deterministic outputs are rebuildable and not canonical source truth."
unresolved_or_deferred:
  - "S7 validates these pages; S6 does not run scripts."
```
