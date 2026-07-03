---
title: "Deterministic Script Boundary"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "deterministic-script-boundary"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 112-123; deterministic script or hook required"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch03-external-orchestration-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch03-external-orchestration-patterns.md"
    source_hash: "dbe4e500d5c22cc61adc4e1364412da71d3db683"
    source_pointer: "claims B03-C006, B03-C012; deterministic validation and tool-output discipline"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Deterministic Script Boundary

```yaml
pattern: "Use deterministic scripts for mechanical checks, indexes, and repeatable transformations that do not require semantic judgment."
used_when:
  - "A result must be reproducible and auditable."
not_used_when:
  - "The task requires concept synthesis or contradiction interpretation."
reads:
  - "files"
  - "manifests"
  - "arguments"
writes:
  - "deterministic artifacts only after explicit write permission"
token_efficiency:
  - "Scripts produce compact reports that route later LLM reads."
drift_controls:
  - "Script output is derived and rebuildable, not semantic doctrine."
unresolved_or_deferred:
  - "S6 writes no scripts."
```
