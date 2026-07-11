---
analysis_id: old-apex-full-orchestration-agent-kb-v2-failure-evidence
kb_slug: old-apex-full-orchestration-agent-kb-v2
source_slug: failure-evidence
run_profile: {output_tier: compiled_full, safe_mode: none}
source_payload_manifest_ref: {path: manifests/source-payload-manifest.json, status_at_analysis_time: fresh}
source_ref: {source_path: raw/other/managed/agent_kb/special_ops__prompts_workflows/MISTAKES.md, source_type: other, source_hash: NA, hash_algorithm: sha256-file, no_hash_reason: NA}
created_at: 2026-07-10T22:00:00Z
created_by: apex-kb
phase: ingest_phase_1
status: analyzed
---
# Phase 1 Ingest Analysis - Failure Evidence

## Source Summary
Failure evidence is distributed across agent MISTAKES files, QA/hygiene reports, patch workflows, source manifests, and audit appendices. Repeated failure families include drift, unclear authority, self-review, weak handoffs, source-pointer loss, and treating candidate or staging content as runtime truth.

## Concept Candidates
- authority-drift
- self-review-and-role-conflation
- source-custody-and-pointer-loss
- candidate-to-canonization-leak

## Key Claims
- claim_id: F01; claim: Source, candidate, canon, validation, and promotion must remain separate.; source_pointer: KB_STARTING_SOURCE_MAP.md#Anti-canonization-safeguards; confidence: high
- claim_id: F02; claim: Build and review of the same load-bearing change should remain separated.; source_pointer: AGENT_SWARM_INTERACTION_CANON.md#Role-switching-and-separation-rules; confidence: high
- claim_id: F03; claim: Conflicting authority classes must not be averaged or silently resolved.; source_pointer: KB_STARTING_SOURCE_MAP.md#Conflict-handling; confidence: high

## Uncertainty / Raw Source Triggers
- id: U-F01; description: Historical logs contain multiple remediation generations and may describe superseded procedures.; source_pointer: managed/agent_kb/*/MISTAKES.md; proposed_handling: revisit_source

## Proposed Phase 2 Changes
- summaries: [failure-patterns-and-recovery, evidence-and-authority-conflicts]
- concepts: [authority-drift, self-review-and-role-conflation, source-custody-and-pointer-loss]
