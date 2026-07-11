---
analysis_id: "operator-research-orchestration-20260711-architecturecheckclaudevshermesvsgpt-analysis"
kb_slug: "operator-research-orchestration-20260711"
source_slug: "architecturecheckclaudevshermesvsgpt"
source_path: "raw/notes/ArchitectureCheckClaudeVsHermesVsGPT.md"
source_hash: "NA"
hash_algorithm: "sha256"
created_at: "2026-07-11T09:09:51Z"
created_by: "apex-kb"
phase: ingest_phase_1
status: operator_review_needed
required_confirmation_phrase: "approve ingest"
---

# Phase 1 Ingest Analysis - architecturecheckclaudevshermesvsgpt

## Source Identity

Historical comparison document. It evaluates Claude, Hermes, and hybrid options, but the KB target is Claude only; retain it for constraints, tradeoffs, and rejected assumptions rather than architecture selection.

## Source Summary

Useful evidence includes the separation of persistent project artifacts from ephemeral runtime state, project isolation, token/cost implications, and the warning that scheduled or hosted execution choices have product boundaries. Its historical hybrid recommendation is superseded by the operator's Claude-only target.

## Extraction Candidates

Candidates: historical-architecture-comparison; durable-state-over-runtime-state; project-isolation; scheduler-boundary. Pointers: `Full Architecture Analysis`, `Recommended Default Pattern`, `Core Design Principle`, `Three-Layer Structure`, `Single Daily Driver Pattern`, `One Rule That Prevents Contamination`.

## Proposed Wiki Changes

Feeds `wiki/summaries/source-authority-and-connection-map.md`; classification: historical/model-specific assumption unless corroborated by Claude-targeted research.

## Operator Gate

```yaml
phase_2_allowed: false
required_confirmation_phrase: "approve ingest"
```
