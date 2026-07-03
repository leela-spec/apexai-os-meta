---
title: "Compiled KB Before Raw Source"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "compiled-kb-before-raw-source"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 124-137; compiled KB pages vs raw sources"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-process-retrospective-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase1-process-retrospective-20260702.md"
    source_hash: "8b011af3de9d3dc7ef5859964437603717d4b9a7"
    source_pointer: "lines 77-123; source-routed not exhaustive"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Compiled KB Before Raw Source

```yaml
pattern: "Queries should start at the compiled KB index and pages before opening full source material."
used_when:
  - "A future agent asks an orchestration design question."
not_used_when:
  - "The compiled page flags low confidence or missing evidence."
reads:
  - "wiki/index.md"
  - "summary/concept/entity pages"
  - "source material only when source_refs require it"
writes:
  - "query packet or answer context"
token_efficiency:
  - "Compiled pages reduce repeated corpus reads."
drift_controls:
  - "Source material remains reachable through source_refs for verification."
unresolved_or_deferred:
  - "S7 will build deterministic index support."
```
