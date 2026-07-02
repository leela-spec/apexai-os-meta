---
title: "Productive Agent Redundancy"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "productive-agent-redundancy"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 69-70; redundancy and conflicting doctrine questions"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-completion-report"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-completion-report.md"
    source_hash: "f604b3e31858da764eb2807084ca8282a1e4acc2"
    source_pointer: "lines 172-200; unresolved tensions"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "medium"
claim_label: "behavioral_inference"
status: "active"
---

# Productive Agent Redundancy

```yaml
pattern: "Limited overlap between roles is useful when it creates challenge, review, or verification rather than duplicate execution."
used_when:
  - "Two roles inspect the same output from different authorities or risk lenses."
not_used_when:
  - "Redundancy causes competing doctrine, duplicate work, or unclear ownership."
reads:
  - "role boundaries"
  - "claim status"
  - "risk profile"
writes:
  - "review notes"
  - "contradiction or escalation marker"
token_efficiency:
  - "Overlap should target high-risk decisions only."
drift_controls:
  - "One role owns production; another may validate but not silently execute."
unresolved_or_deferred:
  - "Which permanent roles should intentionally overlap remains future design work."
```
