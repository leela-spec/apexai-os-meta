---
analysis_id: "old-apex-full-orchestration-agent-kb-agent-kb-index-tier0-analysis"
kb_slug: "old-apex-full-orchestration-agent-kb"
source_slug: "agent-kb-index-tier0"
run_profile:
  output_tier: "analysis_only"
  safe_mode: "phase1_only"
source_payload_manifest_ref:
  path: "manifests/source-payload-manifest.json"
  status_at_analysis_time: "missing"
source_ref:
  source_path: "sources/primary/managed-agent-kb/AGENT_KB_INDEX.md"
  source_type: "ref"
  source_hash: "NA"
  hash_algorithm: "NA"
  no_hash_reason: "pointer_only_tree_hash_only"
created_at: "2026-07-13T13:23:07+02:00"
created_by: "tier0-kb-validation"
phase: "ingest_phase_1"
status: "operator_review_needed"
operator_review_needed: true
---

# Phase 1 Ingest Analysis — AGENT_KB_INDEX Tier 0

## Source Identity

```yaml
source_identity:
  title: "AGENT_KB_INDEX"
  author_or_origin: "Old Apex managed agent KB"
  publication_or_creation_date: "unknown"
  source_authority_level: "primary"
  source_authority_rationale: "Direct historical system index preserved inside the KB source corpus."
  source_scope: "Agent-KB scaffold, compact seed boundaries, owner-validator mapping, and working-surface status."
  source_limitations:
    - "Historical OpenClaw/Apex design; not current Claude Code runtime authority."
    - "The v1 source manifest records only tree-level pointer hashes, not this file's current SHA-256."
```

## Source Custody

```yaml
source_custody:
  storage_mode: "pointer_only_with_repository_copy"
  manifest_source_id: "old-apex-agent-kb-primary"
  manifest_pointer: "ApexDefinition&OldVersions/OldApexFullOrchestrationSystem/managed/agent_kb"
  repository_copy: "apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/AGENT_KB_INDEX.md"
  custody_issue: "Current Apex KB contract expects a source-payload manifest, but this KB has none."
```

## Source Summary

```yaml
source_summary:
  one_sentence_core: "Keep activation seeds compact, place rich doctrine in owned KB roots, and keep candidate learning separate from runtime truth."
  compact_summary: >
    The index defines a common five-file doctrine scaffold and explicitly states that
    LEARNING_QUEUE material is candidate-only. It maps role roots, owners, and validators,
    while repeatedly preserving compact activation seeds. It also distinguishes accepted
    appendices from working files and states that the index does not replace activation seeds
    or shared governance.
  relevant_to_kb_because:
    - "Directly supports compact activation and canonical ownership."
    - "Provides a historical anti-duplication pattern: seed, doctrine root, and governance have distinct owners."
  likely_not_relevant_for:
    - "Numeric Claude skill-description limits or CLAUDE.md token targets."
```

## Extraction Candidates

```yaml
extraction_candidates:
  high_value_sections:
    - section_ref: "Scaffold convention"
      reason: "Defines the reusable compact-seed-plus-references pattern."
      extraction_priority: "high"
    - section_ref: "Agent KB root map"
      reason: "Separates activation role, doctrine root, owner, and validator."
      extraction_priority: "high"
    - section_ref: "Working surface pointers"
      reason: "Prevents storage location from being mistaken for accepted authority."
      extraction_priority: "medium"
  reusable_definitions:
    - "compact activation seed"
    - "candidate-only learning queue"
  reusable_processes:
    - "activation seed -> owned doctrine root -> independent validator"
```

## Key Claims

```yaml
key_claims:
  - claim_id: "T0-V1-AKI-001"
    claim: "A compact activation seed should point to richer owned doctrine instead of absorbing it."
    source_pointer: "AGENT_KB_INDEX.md#Agent-KB-root-map"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: "T0-V1-AKI-002"
    claim: "Candidate learning is not runtime truth by placement alone."
    source_pointer: "AGENT_KB_INDEX.md#Scaffold-convention"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: "T0-V1-AKI-003"
    claim: "The index maps ownership but does not replace activation or governance surfaces."
    source_pointer: "AGENT_KB_INDEX.md#Boundary-note"
    confidence: "high"
    claim_label: "source_backed_summary"
```

## Concept and Entity Candidates

```yaml
concept_candidates:
  - concept_slug: "compact-activation-with-owned-doctrine"
    concept_label: "Compact activation with owned doctrine"
    source_pointer: "Scaffold convention; Agent KB root map; Boundary note"
    summary: "Activation metadata stays small while detailed rules live in one canonical owned location."
    confidence: "high"
entity_candidates: []
```

## Contradictions and Current Wiki Coverage

```yaml
contradictions:
  - "The source supports compact activation but does not establish Claude-specific filenames, token budgets, or description word caps."
current_wiki_coverage:
  covered_by:
    - "wiki/summaries/reusable-old-agent-kb-patterns.md"
    - "wiki/concepts/agent-doctrine-and-promotion-patterns.md"
  assessment: "verified_but_incomplete"
  gap: "The existing summary names compact doctrine surfaces but does not explicitly model activation seed, doctrine owner, and governance owner as separate canonical layers."
```

## Proposed Wiki Changes

```yaml
proposed_wiki_changes:
  - target: "wiki/summaries/reusable-old-agent-kb-patterns.md"
    change_type: "extend_existing_page"
    proposed_change: "Add the three-layer ownership distinction: activation seed, owned detailed doctrine, shared governance."
    source_basis: "AGENT_KB_INDEX.md#Scaffold-convention; #Agent-KB-root-map; #Boundary-note"
  - target: "wiki/summaries/migration-to-claude-native-orchestration.md"
    change_type: "add_qualification"
    proposed_change: "State that the source supports the architecture pattern only, not Claude-specific path or token claims."
```

## Open Questions

```yaml
open_questions:
  - "Should the current Apex activation file point to the weekly skill, the final orchestration start page, or both, with each detail owned once?"
  - "Which current file is the canonical inventory owner for skills, agents, state paths, and artifact paths?"
source_pointers:
  - "sources/primary/managed-agent-kb/AGENT_KB_INDEX.md#Scaffold-convention"
  - "sources/primary/managed-agent-kb/AGENT_KB_INDEX.md#Agent-KB-root-map"
  - "sources/primary/managed-agent-kb/AGENT_KB_INDEX.md#Boundary-note"
operator_review_needed: true
```
