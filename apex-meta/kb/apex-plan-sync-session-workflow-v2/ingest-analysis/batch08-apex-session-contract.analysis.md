---
analysis_id: "apex-plan-sync-session-workflow-v2-apex-session-contract-analysis"
kb_slug: "apex-plan-sync-session-workflow-v2"
source_slug: "apex-session-contract"
run_profile:
  output_tier: "compiled_full"
  safe_mode: "none"
source_payload_manifest_ref:
  path: "manifests/source-payload-manifest.json"
  status_at_analysis_time: "fresh"
created_at: "2026-07-11T09:44:00Z"
created_by: "apex-kb"
phase: ingest_phase_1
status: operator_review_needed
supersedes: "ingest-analysis/batch04-apex-session.analysis.md (pointer_only, unverifiable; content cross-checked and confirmed below)"
---

# Phase 1 Ingest Analysis — apex-session contract

## 1. Source Identity

```yaml
source_identity:
  title: "apex-session skill package"
  author_or_origin: "repo .claude/skills/apex-session/, this repo, current HEAD"
  source_authority_level: "primary"
  source_authority_rationale: "Live skill definition, canonical for the C_SESSION cluster."
  source_scope: "Session artifact creation, gated status mutation, state delta extraction, entity maintenance, H6 handoff artifacts."
  source_limitations:
    - "No .dr/.pro/.v1 variant sprawl — clean 12-file package like apex-sync."
```

## 2. Source Summary

```yaml
source_summary:
  one_sentence_core: "apex-session converts task/session evidence into gated status-mutation records and the final H6 handoff artifact set (task_plan.md, findings.md, progress.md, next-session.md), and is the only one of the three packages permitted to record confirmed mutations."
  compact_summary: >
    apex-session owns status mutation (validated against the shared H1 enum), session progress
    logging, state-delta extraction, entity update maintenance, and next-session context. Every
    consequential mutation requires an explicit operator_validation: confirmed before being treated
    as final; unconfirmed changes stay visible but unconfirmed. It preserves raw_source_ref/
    raw_source_path rather than silently resolving gaps, and explicitly must not rank tasks, scan
    blockers, rebuild registries, compute scores, run scripts, or decompose new work — those remain
    apex-sync's and apex-plan's territory respectively.
  relevant_to_kb_because:
    - "The mutation-authority layer of the three-package system — the only place where 'confirmed' state changes are recorded."
  likely_not_relevant_for:
    - "Master-of-Arts workflow content."
```

## 3. Extraction Candidates

```yaml
extraction_candidates:
  high_value_sections:
    - section_ref: "raw/refs/SKILL.md lines 20-67 (Skill Contract yaml)"
      reason: "owns list (PM6, KB1-KB3, KB6, PD5, PD6), final_handoff_files, allowed_status_values, operator_validation_values, review_flag_values."
      extraction_priority: high
    - section_ref: "raw/refs/SKILL.md lines 186-208 (Procedure)"
      reason: "11-step procedure; step 1 explicitly routes decomposition asks to apex-plan and ranking/blocker/registry/drift/score asks to apex-sync — this is the routing logic that makes the triangle self-correcting."
      extraction_priority: high
    - section_ref: "raw/refs/SKILL.md lines 210-262 (Validation Rules, esp. boundary_validation)"
      reason: "12 explicit no_* boundary flags (no_new_project_decomposition through no_public_web_research) — the most exhaustive boundary list of the three skills."
      extraction_priority: high
  reusable_definitions:
    - "operator_validation_values: confirmed, rejected, needs_revision, not_requested (raw/refs/SKILL.md lines 52-56) — the gate vocabulary that makes mutation consequential-only-when-confirmed."
  reusable_processes:
    - "next-session.md must contain exactly 5 sections: Current Step, Open Items, Risks, Decisions Made, Next Actions (raw/refs/SKILL.md lines 229-234) — a hard structural contract, not a suggestion."
```

## 4. Concept Candidates

```yaml
concept_candidates:
  - concept_slug: "operator-validation-gate"
    concept_label: "Consequential mutation requires operator_validation: confirmed"
    source_pointer: "raw/refs/SKILL.md lines 196-198, 236-240"
    summary: "A status mutation record and before_after_preview exist even when validation is missing/rejected/needs_revision, but the record stays visible-and-unconfirmed rather than being silently applied — the gate blocks confirmation, not visibility."
    confidence: high
  - concept_slug: "raw-source-preservation"
    concept_label: "Preserve, don't resolve, unresolved context"
    source_pointer: "raw/refs/SKILL.md lines 190-192, 242-246"
    summary: "apex-session must carry raw_source_ref/raw_source_path forward and flag raw_source_missing rather than filling gaps from memory or silently resolving source_conflict."
    confidence: high
```

## 5. Entity Candidates

```yaml
entity_candidates:
  - entity_slug: "h6-handoff-artifacts"
    entity_label: "H6 handoff artifact set"
    entity_type: artifact
    source_pointer: "raw/refs/SKILL.md lines 39-43, 122-127, 223-234"
    summary: "task_plan.md, findings.md, progress.md, next-session.md — the four files apex-session must produce or refresh; next-session.md has a fixed 5-section structure."
    confidence: high
```

## 6. Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "apex-session's step 1 procedure explicitly routes new-decomposition requests to apex-plan and ranking/blocker-scan/registry-rebuild/drift-detection/stale-detection/score-computation requests to apex-sync, before doing any apex-session work."
    source_pointer: "raw/refs/SKILL.md line 188"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C002
    claim: "apex-session's boundary_validation block lists 12 distinct forbidden operations, the largest explicit boundary list of the three skills — a superset that includes apex-plan's forbidden decomposition AND apex-sync's forbidden scoring/registry/drift/stale operations."
    source_pointer: "raw/refs/SKILL.md lines 248-261"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C003
    claim: "The three skills share one identical status enum (open, in-progress, blocked, done, deferred) verified letter-for-letter across all three SKILL.md files: apex-plan lines 46-53, apex-sync lines 155-160, apex-session lines 45-50/214-220."
    source_pointer: "raw/other/SKILL.md lines 46-53; raw/notes/SKILL.md lines 155-160; raw/refs/SKILL.md lines 45-50"
    confidence: high
    claim_label: source_backed_summary
```

## 7. Uncertainty / Raw Source Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: >
      apex-session's boundary_validation being a strict superset of apex-plan's and apex-sync's
      individual forbidden lists (C002) is presented here as a design observation, not a verified
      claim about runtime enforcement — this KB has no evidence of an actual apex-session
      invocation to confirm the boundary holds in practice, only that it is declared in the
      skill's own text. Flagged for revisit if runtime session-transcript evidence becomes
      available.
    source_pointer: "raw/refs/SKILL.md lines 248-261"
    proposed_handling: revisit_source
```

## 8. Proposed Phase 2 Changes

```yaml
proposed_wiki_pages:
  entities:
    - "entities/apex-session.md (update source_refs to real hashes; add C001-C003 with precise line pointers)"
audit_items: []
manifest_updates: []
```

## 9. Compile Decision

Output tier is `compiled_full`. Continue into Phase 2 wiki compile once the operator issues `approve ingest`.
