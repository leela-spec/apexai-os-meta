---
title: "Next-Cycle Context"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "next-cycle-context"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 99-111; next cycle context"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C009, B04-C011, B04-C017"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "medium"
claim_label: "behavioral_inference"
status: "active"
---

# Next-Cycle Context

```yaml
pattern: "Next-cycle context is the compact accepted input for the next planning cycle."
used_when:
  - "A planning loop continues after status merge."
not_used_when:
  - "No accepted state or priorities changed."
reads:
  - "updated status"
  - "open decisions"
  - "operator constraints"
writes:
  - "next planning seed"
token_efficiency:
  - "The next cycle reads accepted context instead of all previous artifacts."
drift_controls:
  - "Candidate and raw evidence are excluded unless explicitly referenced."
unresolved_or_deferred:
  - "No scheduler or auto-trigger is created in S6."
```
