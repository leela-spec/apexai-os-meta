---
analysis_id: "old-apex-full-orchestration-agent-kb-hygiene-clean-tier0-analysis"
kb_slug: "old-apex-full-orchestration-agent-kb"
source_slug: "hygiene-clean-tier0"
run_profile:
  output_tier: "analysis_only"
  safe_mode: "phase1_only"
source_payload_manifest_ref:
  path: "manifests/source-payload-manifest.json"
  status_at_analysis_time: "missing"
source_ref:
  source_path: "sources/primary/managed-agent-kb/special_ops__hygiene_clean/ESSENCE.md"
  source_type: "ref"
  source_hash: "NA"
  hash_algorithm: "NA"
  no_hash_reason: "pointer_only_tree_hash_only"
created_at: "2026-07-13T13:50:00+02:00"
created_by: "tier0-kb-validation"
phase: "ingest_phase_1"
status: "operator_review_needed"
operator_review_needed: true
---

# Phase 1 Ingest Analysis — Hygiene Clean Tier 0

## Source Identity and Custody

```yaml
source_identity:
  title: "Special Ops Hygiene Clean — ESSENCE"
  author_or_origin: "Old Apex managed agent KB"
  publication_or_creation_date: "unknown"
  source_authority_level: "primary"
  source_authority_rationale: "Direct accepted historical doctrine preserved in the v1 corpus."
  source_scope: "Structural QA, compact activation, targeted reads, bounded repair, and evidence-based closure."
  source_limitations:
    - "Historical doctrine, not direct Claude Code runtime evidence."
source_custody:
  storage_mode: "pointer_only_with_repository_copy"
  manifest_source_id: "old-apex-agent-kb-primary"
  repository_copy: "apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/special_ops__hygiene_clean/ESSENCE.md"
  custody_issue: "No source-payload manifest exists for this KB under the current contract."
```

## Source Summary

```yaml
source_summary:
  one_sentence_core: "Keep activation compact, load only the evidence needed for the current mode, repair the narrowest verified span, and close findings only with evidence."
  compact_summary: >
    The source defines a compression-only activation surface backed by targeted references and explicit
    read-budget profiles. It requires authority before action, exact-span repair before broad rewrite,
    one-file-before-many progression, and evidence-backed closure. It also prevents candidate findings
    and scaffold placement from silently becoming runtime truth.
  relevant_to_kb_because:
    - "Supports progressive disclosure and targeted context loading."
    - "Supports low-risk Tier 0 corrections rather than broad redesign."
    - "Supplies a verification discipline for relocation and deduplication."
  likely_not_relevant_for:
    - "Exact Claude token budgets or automatic skill-discovery behavior."
```

## Extraction Candidates and Claims

```yaml
extraction_candidates:
  high_value_sections:
    - section_ref: "Operating doctrine"
      reason: "Defines narrow repair and evidence-backed closure."
      extraction_priority: "high"
    - section_ref: "Read-budget profiles"
      reason: "Defines targeted loading instead of full-doctrine preload."
      extraction_priority: "high"
    - section_ref: "Core constraints"
      reason: "Prevents summary substitution and candidate-to-truth leakage."
      extraction_priority: "medium"
  reusable_definitions:
    - "compression-only activation surface"
    - "read-budget profile"
  reusable_processes:
    - "identify authority -> select read mode -> bounded repair -> evidence closure"
key_claims:
  - claim_id: "T0-V1-HYG-001"
    claim: "Detailed evidence should remain behind a compact activation surface and be loaded by task-specific read mode."
    source_pointer: "special_ops__hygiene_clean/ESSENCE.md#Purpose; #Read-budget-profiles"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: "T0-V1-HYG-002"
    claim: "Bounded defects should receive minimal-span repair unless rewrite authority is explicit."
    source_pointer: "special_ops__hygiene_clean/ESSENCE.md#Operating-doctrine"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: "T0-V1-HYG-003"
    claim: "A finding closes only when closure evidence exists."
    source_pointer: "special_ops__hygiene_clean/ESSENCE.md#Operating-doctrine"
    confidence: "high"
    claim_label: "source_backed_summary"
```

## Coverage, Contradictions, and Proposed Changes

```yaml
concept_candidates:
  - concept_slug: "targeted-context-loading"
    concept_label: "Targeted context loading"
    source_pointer: "Purpose; Read-budget profiles"
    summary: "Load the smallest source set needed for the active task or validation mode."
    confidence: "high"
entity_candidates: []
contradictions:
  - "The source supports targeted loading but does not establish a universal numerical token ceiling."
current_wiki_coverage:
  covered_by:
    - "wiki/summaries/reusable-old-agent-kb-patterns.md"
    - "wiki/concepts/validation-and-routing-guardrails.md"
  assessment: "verified_but_incomplete"
  gap: "The wiki captures exact-span repair and evidence closure but omits the explicit read-budget profile as a reusable Tier 0 mechanism."
proposed_wiki_changes:
  - target: "wiki/summaries/reusable-old-agent-kb-patterns.md"
    change_type: "extend_existing_page"
    proposed_change: "Add targeted read-budget profiles as a distinct reusable mechanism supporting progressive disclosure."
  - target: "wiki/concepts/validation-and-routing-guardrails.md"
    change_type: "add_qualification"
    proposed_change: "Clarify that structural closure requires evidence and that broad rewrites are not the default correction mechanism."
open_questions:
  - "Which current orchestration references should be loaded only on trigger rather than included in the activation file?"
source_pointers:
  - "sources/primary/managed-agent-kb/special_ops__hygiene_clean/ESSENCE.md#Operating-doctrine"
  - "sources/primary/managed-agent-kb/special_ops__hygiene_clean/ESSENCE.md#Read-budget-profiles"
operator_review_needed: true
```
