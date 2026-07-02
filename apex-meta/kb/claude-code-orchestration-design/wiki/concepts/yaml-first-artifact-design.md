---
title: "YAML-First Artifact Design"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "yaml-first-artifact-design"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 124-137; yaml-first artifact design"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C011, B04-C014; state blocks and proof"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# YAML-First Artifact Design

```yaml
pattern: "Use concise YAML fields for artifact identity, state, authority, reads, writes, and gates before explanatory prose."
used_when:
  - "A future agent must parse or route the artifact quickly."
not_used_when:
  - "The artifact is only narrative explanation for a human."
reads:
  - "frontmatter"
  - "machine-readable blocks"
writes:
  - "structured fields"
  - "short clarifying prose"
token_efficiency:
  - "Predictable fields reduce repeated interpretation overhead."
drift_controls:
  - "Required fields make missing authority or status visible."
unresolved_or_deferred:
  - "S7 can lint field shape; S6 supplies source-grounded content."
```
