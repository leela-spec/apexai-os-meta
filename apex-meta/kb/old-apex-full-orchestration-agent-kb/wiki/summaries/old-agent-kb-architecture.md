---
title: "Old Agent KB Architecture"
page_type: summary
kb_slug: "old-apex-full-orchestration-agent-kb"
summary_slug: "old-agent-kb-architecture"
source_refs:
  - source_id: "phase1-rerun-batch01"
    source_path: "apex-meta/kb/old-apex-full-orchestration-agent-kb/ingest-analysis/batch01-agent-kb-architecture.analysis.md"
    source_pointer: "source_grounded_claims A01-C001-A01-C007"
    source_storage_mode: "copy_into_kb"
  - source_id: "agent-kb-index"
    source_path: "apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/AGENT_KB_INDEX.md"
    source_pointer: "Purpose; Scaffold convention; Agent KB root map"
    source_storage_mode: "copy_into_kb"
created_at: "2026-07-03T00:00:00Z"
updated_at: "2026-07-06T22:45:00+02:00"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Old Agent KB Architecture

## Adaptive Ranked Source Set

```yaml
ranked_source_set:
  tier_1:
    - source: "AGENT_KB_INDEX.md"
      why_relevant: "Defines the first-wave agent KB root map and five-file scaffold."
      supports: ["macro architecture", "scaffold convention", "role root map"]
      reopen_raw_source_when: "deciding whether old role roots should influence current Apex package structure"
    - source: "ingest-analysis/batch01-agent-kb-architecture.analysis.md"
      why_relevant: "Replacement Phase 1 synthesis for architecture."
      supports: ["claims", "concepts", "entities", "tensions"]
      reopen_raw_source_when: "claim-level evidence needs exact source wording"
  tier_2:
    - source: "role ESSENCE.md files"
      why_relevant: "Show compact boundary surfaces across roles."
      supports: ["compact activation", "owns / does-not-own pattern"]
    - source: "meta_detective/APPENDIX_INTERNAL_MODES.md"
      why_relevant: "Shows accepted appendix doctrine without agent sprawl."
      supports: ["appendix doctrine", "internal mode pattern"]
```

## Macro Synthesis

The old agent KB is best understood as a durable role-doctrine architecture. Its value is not the exact old OpenClaw roster; its reusable pattern is a source-preserving structure for keeping role boundaries, practices, mistakes, templates, and candidate learning stable across sessions.

## Meso Synthesis

The architecture has five interacting mechanisms:

1. A root index maps every first-wave agent to a KB root, owner, validator, and notes.
2. Every durable role uses the same five-file scaffold: `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md`, and `LEARNING_QUEUE.md`.
3. `ESSENCE.md` is the compact activation surface; it keeps the role small enough for retrieval and routing.
4. `LEARNING_QUEUE.md` is candidate-only, preventing learning entries from becoming accepted truth by placement.
5. Accepted appendices carry dense doctrine when a compact file would be overloaded.

## Micro Synthesis

```yaml
micro_claims:
  - claim_id: OKB-ARCH-001
    claim: "The root index maps first-wave agents to KB roots and owner/validator relationships."
    source_pointer: "AGENT_KB_INDEX.md / Purpose and Agent KB root map"
    confidence: high
    claim_label: raw_source
  - claim_id: OKB-ARCH-002
    claim: "The five-file scaffold is the core reusable storage pattern."
    source_pointer: "AGENT_KB_INDEX.md / Scaffold convention"
    confidence: high
    claim_label: raw_source
  - claim_id: OKB-ARCH-003
    claim: "Candidate material is not runtime truth."
    source_pointer: "AGENT_KB_INDEX.md / Scaffold convention"
    confidence: high
    claim_label: raw_source
  - claim_id: OKB-ARCH-004
    claim: "Accepted appendix doctrine can preserve detailed operating modes without creating new agents."
    source_pointer: "meta_detective/APPENDIX_INTERNAL_MODES.md / Purpose and Status"
    confidence: high
    claim_label: source_backed_summary
```

## Routes Here

Use this page when asking:

- “What did the old agent KB architecture actually contribute?”
- “Should we preserve the five-file scaffold?”
- “How does old agent doctrine avoid candidate-to-truth leakage?”
- “What should be copied as pattern versus left as historical evidence?”

## Uncertainty / Raw Source Triggers

Reopen raw sources when making implementation decisions about current Apex skills, current agents, or active runtime paths. This page is a migration and retrieval summary, not authority to recreate the old OpenClaw system.
