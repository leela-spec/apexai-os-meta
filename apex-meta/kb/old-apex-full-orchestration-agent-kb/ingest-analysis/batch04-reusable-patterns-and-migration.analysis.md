---
title: "Rerun Batch 04 — Reusable Patterns and Migration"
page_type: ingest_analysis
kb_slug: old-apex-full-orchestration-agent-kb
phase: ingest_phase_1_rerun
status: operator_gate_already_approved_for_rerun
created_at: "2026-07-06T22:45:00+02:00"
updated_at: "2026-07-06T22:45:00+02:00"
confidence: high
claim_label: source_grounded_analysis
phase_2_allowed: true
phase_2_approval_phrase: "approve ingest"
---

# Rerun Batch 04 — Reusable Patterns and Migration

## source_scope

This replacement Phase 1 batch extracts reusable patterns from the old managed agent KB and classifies them for current Apex/Claude-native use. It keeps old OpenClaw paths and role names as historical source evidence, not as active implementation authority.

## files_read

```yaml
files_read:
  - path: sources/primary/managed-agent-kb/AGENT_KB_INDEX.md
    pointer: "scaffold convention, role root map, working-surface boundaries"
  - path: sources/primary/managed-agent-kb/meta_detective/APPENDIX_INTERNAL_MODES.md
    pointer: "internal-mode anti-sprawl pattern"
  - path: sources/primary/managed-agent-kb/meta_detective/ESSENCE.md
    pointer: "adversarial validation and source authority discipline"
  - path: sources/primary/managed-agent-kb/special_ops__ai_handling_routing/ESSENCE.md
    pointer: "routing minimum, source authority, repo execution versus chat routing checks"
  - path: sources/primary/managed-agent-kb/special_ops__hygiene_clean/ESSENCE.md
    pointer: "mode lock, exact-span before rewrite, one-file-before-many, closure by evidence"
  - path: outputs/synthesis/apex-kb-semantic-continuation-after-lint-closure.md
    pointer: "finalized lint concepts and remaining semantic work"
```

## source_grounded_claims

```yaml
claims:
  - id: A04-C001
    claim: "The reusable unit is the doctrine pattern, not the old agent roster as a current runtime plan."
    source_pointer: "AGENT_KB_INDEX.md / Scaffold convention and Agent KB root map"
    confidence: high
    claim_label: source_backed_summary

  - id: A04-C002
    claim: "Strong specialized behavior can remain an internal mode or checklist inside one role instead of becoming a separate permanent agent."
    source_pointer: "meta_detective/APPENDIX_INTERNAL_MODES.md / Status and Doctrine statement"
    confidence: high
    claim_label: source_backed_summary

  - id: A04-C003
    claim: "Source, candidate, accepted doctrine, and active authority are distinct states; candidate material does not become truth by placement."
    source_pointer: "AGENT_KB_INDEX.md / LEARNING_QUEUE convention; special_ops__hygiene_clean/ESSENCE.md / Status vocabulary"
    confidence: high
    claim_label: source_backed_summary

  - id: A04-C004
    claim: "Repo-affecting work needs an explicit route contract before it is treated as an execution task."
    source_pointer: "special_ops__ai_handling_routing/ESSENCE.md / Core doctrine and routing minimum; semantic continuation report / lint-repo-execution-router"
    confidence: high
    claim_label: source_backed_summary

  - id: A04-C005
    claim: "Historical paths in old sources are valid evidence pointers but not current Apex path authority unless reverified in the current repo."
    source_pointer: "semantic continuation report / lint-historical-path-authority"
    confidence: high
    claim_label: source_backed_summary

  - id: A04-C006
    claim: "Exact-span repair, one-file-before-many, and closure-by-evidence are reusable controls for KB maintenance and patching workflows."
    source_pointer: "special_ops__hygiene_clean/ESSENCE.md / Operating doctrine"
    confidence: high
    claim_label: source_backed_summary

  - id: A04-C007
    claim: "Finalized lint concepts should be discoverable in the wiki as semantic doctrine, not only preserved in implementation reports."
    source_pointer: "semantic continuation report / remaining LLM-owned KB work"
    confidence: high
    claim_label: source_backed_summary
```

## concepts_extracted

```yaml
concepts_extracted:
  - slug: reusable-agent-doctrine-scaffold
    label: "Reusable agent doctrine scaffold"
    definition: "A compact, source-preserving scaffold for durable role or capability doctrine."
    source_pointer: "AGENT_KB_INDEX.md / Scaffold convention"
    phase2_value: high

  - slug: anti-agent-sprawl-internal-modes
    label: "Anti-agent-sprawl internal modes"
    definition: "Specialized checks can stay as internal modes when they do not need separate durable identity."
    source_pointer: "meta_detective/APPENDIX_INTERNAL_MODES.md"
    phase2_value: high

  - slug: phase-gated-knowledge-promotion
    label: "Phase-gated knowledge promotion"
    definition: "Candidate knowledge moves toward accepted doctrine only through evidence, owner, validator, and promotion route."
    source_pointer: "AGENT_KB_INDEX.md; special_ops__hygiene_clean/ESSENCE.md"
    phase2_value: high

  - slug: repo-write-preflight-contract
    label: "Repo write preflight contract"
    definition: "A pre-write route contract for repo-affecting work."
    source_pointer: "special_ops__ai_handling_routing/ESSENCE.md"
    phase2_value: high

  - slug: historical-path-authority-safety
    label: "Historical path authority safety"
    definition: "Old paths stay evidence-only until current path authority is independently established."
    source_pointer: "semantic continuation report / lint-historical-path-authority"
    phase2_value: high
```

## entities_extracted

```yaml
entities_extracted:
  - id: old_openclaw_agent_kb_system
    type: historical_system
    current_authority: evidence_only
    source_pointer: "mirrored source corpus; AGENT_KB_INDEX.md"

  - id: reusable_scaffold_files
    type: artifact_family
    members: [ESSENCE.md, BEST_PRACTICES.md, MISTAKES.md, TEMPLATES.md, LEARNING_QUEUE.md]
    source_pointer: "AGENT_KB_INDEX.md / Scaffold convention"

  - id: deterministic_lint_concepts
    type: finalized_process_doctrine
    members: [repo_execution_routing_safety, historical_path_authority_safety]
    source_pointer: "semantic continuation report"
```

## contradictions_or_tensions

```yaml
contradictions_or_tensions:
  - id: A04-T001
    tension: "The old role taxonomy is useful evidence but should not automatically become the current permanent agent set."
    disposition: "Compile as historical entities and reusable patterns."
    confidence: high

  - id: A04-T002
    tension: "The corpus is large enough to support strong synthesis but also large enough to overfit to old paths and old implementation surfaces."
    disposition: "Use ranked source sets and raw-source reopen triggers in Phase 2."
    confidence: high
```

## open_questions

```yaml
open_questions:
  - id: A04-Q001
    question: "Which reusable patterns should become Apex-native skill text, lint, workflow templates, or wiki doctrine only?"
    blocker: false
  - id: A04-Q002
    question: "Which historical path references need deterministic cleanup later, and which should remain explicit source evidence?"
    blocker: false
```

## proposed_phase_2_wiki_targets

```yaml
summaries:
  - reusable-old-agent-kb-patterns
  - migration-to-claude-native-orchestration
  - deterministic-execution-safety-after-lint-closure
concepts:
  - migration-safety-patterns
  - repo-execution-routing-safety
  - agent-doctrine-and-promotion-patterns
entities:
  - reusable-artifact-families
```

## phase_gate_statement

```yaml
phase_2_gate:
  required_phrase: approve ingest
  status_for_this_rerun: approved
```
