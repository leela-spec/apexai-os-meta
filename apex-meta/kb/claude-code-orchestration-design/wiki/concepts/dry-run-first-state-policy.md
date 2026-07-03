---
title: "Dry-Run First State Policy"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "dry-run-first-state-policy"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 86-98; defaults to dry run"
    source_storage_mode: "pointer_only"
  - source_id: "operator-phase1-review-decisions-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md"
    source_hash: "34d9c16967d2f7f49b716d75c8bb1a2a10eb96a7"
    source_pointer: "lines 54-68; high-risk gates"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "medium"
claim_label: "behavioral_inference"
status: "active"
---

# Dry-Run First State Policy

```yaml
pattern: "Mutation-capable project actions first produce a preview before applying writes."
used_when:
  - "A workflow could alter canonical project, KB, or execution state."
not_used_when:
  - "The action is a read-only query or already approved deterministic write."
reads:
  - "target path"
  - "planned delta"
  - "permission gate"
writes:
  - "dry-run report"
  - "write only after approval"
token_efficiency:
  - "Preview summarizes change intent without dumping full file bodies."
drift_controls:
  - "Dry-run blocks accidental promotion and wrong-target writes."
unresolved_or_deferred:
  - "Exact script flags are deterministic S7+ concern, not S6."
```
