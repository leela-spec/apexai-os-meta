---
title: "Refs Not Copies"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "refs-not-copies"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 124-137; refs_not_copies"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C009, B04-C014; clean handoffs and proof"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Refs Not Copies

```yaml
pattern: "Artifacts should carry pointers to sources, pages, and files instead of duplicating full content."
used_when:
  - "A page or packet needs evidence without loading the evidence body."
not_used_when:
  - "A short quote or exact field is necessary for local clarity."
reads:
  - "source_refs"
  - "paths"
  - "anchors or line pointers"
writes:
  - "references"
  - "minimal excerpts only when needed"
token_efficiency:
  - "Pointers keep packets small and preserve audit paths."
drift_controls:
  - "Future agents can follow evidence instead of trusting copied summaries."
unresolved_or_deferred:
  - "Line-accurate source validation is a deterministic postflight concern."
```
