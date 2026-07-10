---
analysis_id: "claude-code-orchestration-design-status-merge-package-analysis"
kb_slug: "claude-code-orchestration-design"
source_slug: "status-merge-package"
run_profile:
  output_tier: "compiled_minimal"
  safe_mode: "none"
source_payload_manifest_ref:
  path: "manifests/source-payload-manifest.json"
  status_at_analysis_time: "missing"
source_refs:
  - source_id: "status-merge-skill"
    source_path: ".claude/skills/status-merge/SKILL.md"
    source_hash: "228c92fc2db9e8fdf6ac32aece8a741b218e58d6"
    hash_algorithm: "git-blob-sha1"
  - source_id: "status-merge-packet-contract"
    source_path: ".claude/skills/status-merge/references/status-merge-packet-contract.md"
    source_hash: "d917c130aafcdbea6f4c98d909099c523755f424"
    hash_algorithm: "git-blob-sha1"
  - source_id: "next-precap-context-contract"
    source_path: ".claude/skills/status-merge/references/next-precaphandoff-context-contract.md"
    source_hash: "a5551276402f62f14ec8e853660d8015fe7f41d9"
    hash_algorithm: "git-blob-sha1"
created_at: "2026-07-10T14:30:00Z"
created_by: "apex-kb"
phase: ingest_phase_1
status: compiled_to_phase_2
---

# Phase 1 Ingest Analysis — StatusMerge Package

## 1. Source Identity

```yaml
source_identity:
  title: "StatusMerge skill package and core contracts"
  author_or_origin: "apexai-os-meta repository"
  publication_or_creation_date: "2026"
  source_authority_level: "primary"
  source_authority_rationale: >
    The selected files are the active skill entrypoint and the two contracts that
    define its primary output and downstream handoff. They are implementation
    authority for package ownership, packet shape, and negative boundaries.
  source_scope: >
    Proposal-only reconciliation of validated recap-derived deltas, conflict
    handling, owner-safe durable-write routing, and compact next-day planning context.
  source_limitations:
    - "The slice does not inspect the upstream FlowRecap schema in detail."
    - "The slice does not inspect project-kb-manager write implementation."
    - "The source-payload manifest is empty, so repository paths and blob SHAs are used directly."
```

## 2. Source Summary

```yaml
source_summary:
  one_sentence_core: >
    StatusMerge is a non-runtime, proposal-only interface that reconciles validated
    recap candidates against previous state, exposes conflicts before acceptance,
    routes durable updates to project-kb-manager, and emits a bounded planning seed.
  compact_summary: >
    The package sits between recap generation and durable project-state mutation.
    It receives FlowRecap and prior-state references, classifies each candidate as
    accepted-for-proposal, rejected, deferred, duplicate, superseded, conflicting,
    or insufficiently evidenced, and preserves evidence and confidence. Conflicts
    are processed before accepted deltas so ambiguous state cannot silently become
    durable truth. The package may draft a proposed project-KB update and an updated
    status view, but both remain proposals; project-kb-manager retains the durable
    write boundary. Its downstream next_PreCapNextDay_input_context is deliberately
    smaller than a plan: it carries focus, candidate next actions, blockers,
    unresolved decisions, evidence refs, and confidence to PreCapNextDay.
  relevant_to_kb_because:
    - "It demonstrates a concrete owner-validator-write-boundary pattern."
    - "It defines how orchestration state moves without allowing silent overwrite."
    - "It shows how conflicts and uncertainty remain visible across handoffs."
  likely_not_relevant_for:
    - "Runtime scheduling or autonomous execution."
    - "The internal schema of FlowRecap, ProjectStatus, or project-kb-manager."
```

## 3. Extraction Candidates

```yaml
extraction_candidates:
  high_value_sections:
    - section_ref: ".claude/skills/status-merge/SKILL.md#Procedure, lines 69-83"
      reason: "Defines the end-to-end semantic workflow and completion gate."
      extraction_priority: "high"
    - section_ref: ".claude/skills/status-merge/SKILL.md#Boundary Rules, lines 96-112"
      reason: "Defines the package's negative ownership and proposal-only status."
      extraction_priority: "high"
    - section_ref: ".claude/skills/status-merge/references/status-merge-packet-contract.md#Contract Role, lines 5-73"
      reason: "Defines owned artifacts, forbidden ownership, consumers, and global invariants."
      extraction_priority: "high"
    - section_ref: ".claude/skills/status-merge/references/status-merge-packet-contract.md#Schema, lines 120-253"
      reason: "Defines the packet fields and validation states."
      extraction_priority: "high"
    - section_ref: ".claude/skills/status-merge/references/next-precaphandoff-context-contract.md#Contract Role, lines 5-61"
      reason: "Separates context seed from plan generation and runtime triggering."
      extraction_priority: "high"
    - section_ref: ".claude/skills/status-merge/references/next-precaphandoff-context-contract.md#Schema, lines 120-216"
      reason: "Defines the exact bounded information transferred downstream."
      extraction_priority: "high"
  reusable_definitions:
    - "status_merge_packet"
    - "proposal-only durable-state view"
    - "next_PreCapNextDay_input_context"
    - "blocked_by_conflict"
  reusable_processes:
    - "classify candidate deltas"
    - "surface conflicts before acceptance"
    - "route durable writes through the owning package"
    - "compress accepted state into a downstream planning seed"
```

## 4. Concept Candidates

```yaml
concept_candidates:
  - concept_slug: "proposal-only-state-transition"
    concept_label: "Proposal-Only State Transition"
    source_pointer: "SKILL.md lines 69-83 and 96-112; packet contract lines 193-235"
    summary: >
      A state transition may be semantically prepared and reviewed without becoming
      durable state; ownership and operator confirmation remain explicit.
    confidence: "high"
  - concept_slug: "conflict-before-acceptance"
    concept_label: "Conflict Before Acceptance"
    source_pointer: "SKILL.md lines 75-83 and 114-140; packet contract lines 207-220 and 297-314"
    summary: >
      Conflicts are first-class blockers or review flags and must be exposed before
      candidate deltas are placed in an accepted proposal set.
    confidence: "high"
```

## 5. Entity Candidates

```yaml
entity_candidates:
  - entity_slug: "status-merge"
    entity_label: "StatusMerge"
    entity_type: "artifact"
    source_pointer: "SKILL.md lines 8-30 and 47-67"
    summary: >
      A Claude skill package that converts validated recap candidates into an
      operator-reviewable merge packet and compact next-planning context.
    confidence: "high"
```

## 6. Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "StatusMerge does not directly mutate durable project state."
    source_pointer: ".claude/skills/status-merge/SKILL.md lines 10-15 and 96-112"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "Conflicts must be surfaced before candidate deltas are accepted into the proposal."
    source_pointer: ".claude/skills/status-merge/SKILL.md lines 75-83; status-merge-packet-contract.md lines 63-72"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "Durable updates are routed through project-kb-manager and remain operator-gated."
    source_pointer: "status-merge-packet-contract.md lines 20-41, 63-72, and 214-227"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C004
    claim: "The next PreCap handoff is a compact context seed, not a next-day plan or autonomous trigger."
    source_pointer: "next-precaphandoff-context-contract.md lines 7-16 and 52-61"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C005
    claim: "The packet preserves rejected, deferred, and conflicting candidates for auditability instead of silently dropping them."
    source_pointer: "status-merge-packet-contract.md lines 193-212 and 280-314"
    confidence: "high"
    claim_label: "source_backed_summary"
```

## 7. Uncertainty / Raw Source Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "The upstream definition of a validated FlowRecap candidate is outside this bounded source slice."
    source_pointer: "SKILL.md lines 32-45 and 183-192"
    proposed_handling: "revisit_source"
  - id: U002
    description: "The package contract makes source_usage_summary_refs required while the skill entrypoint describes usage summaries as optional."
    source_pointer: "SKILL.md lines 32-45; status-merge-packet-contract.md lines 43-52 and 123-170"
    proposed_handling: "audit_item"
  - id: U003
    description: "Validation status names describe packet readiness but do not themselves prove that downstream durable writes occurred."
    source_pointer: "SKILL.md lines 85-94; packet contract lines 244-252"
    proposed_handling: "leave_as_gap"
```

## 8. Proposed Phase 2 Changes

```yaml
proposed_wiki_pages:
  summaries:
    - "wiki/summaries/trial-20260710-status-merge/status-merge-flow.md"
  concepts:
    - "wiki/concepts/trial-20260710-status-merge/proposal-only-state-transition.md"
    - "wiki/concepts/trial-20260710-status-merge/conflict-before-acceptance.md"
  entities:
    - "wiki/entities/trial-20260710-status-merge/status-merge.md"
audit_items:
  - "Required-versus-optional usage summary reference mismatch"
manifest_updates: []
```

## 9. Compile Decision

The selected output tier is `compiled_minimal`. Continue into Phase 2 using only the bounded source slice above. Existing wiki pages may inform terminology and comparison, but the active package files remain primary authority.