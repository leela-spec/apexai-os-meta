---
title: "Compact Activation File"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "compact-activation-file"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 124-137; what should be loaded every session"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch01-skill-package-contracts"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch01-skill-package-contracts.md"
    source_hash: "8a46dcf8bf15c18b0f0c6541cdf4e68475a777c1"
    source_pointer: "claims B01-C002 and B01-C010; concise entrypoints"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Compact Activation File

```yaml
pattern: "An activation file contains only stable triggers, boundary, procedure summary, and next-read pointers."
used_when:
  - "A model or role needs fast startup without loading deep references."
not_used_when:
  - "Detailed schema or source evidence is required immediately."
reads:
  - "trigger metadata"
  - "scope boundary"
  - "resource pointers"
writes:
  - "activated context"
token_efficiency:
  - "Keeps startup surfaces small and pushes details into referenced files."
drift_controls:
  - "Next-read pointers reduce invented procedure details."
unresolved_or_deferred:
  - "Exact activation-file syntax is implementation-specific."
```
