---
title: "Rerun Batch 01 — Agent KB Architecture"
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

# Rerun Batch 01 — Agent KB Architecture

## source_scope

This replacement Phase 1 batch analyzes the old managed agent KB as an architecture for durable, source-preserving role doctrine. It focuses on the storage pattern rather than on current runtime authority.

The source corpus used for this rerun is the mirrored KB-local corpus under:

```text
apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/
```

The historical `OpenClaw` and Windows-local paths are treated only as source evidence. They are not current Apex runtime authority.

## files_read

```yaml
files_read:
  control:
    - path: .claude/skills/apex-kb/SKILL.md
      pointer: "Phase 2 page value contract and Apex KB lifecycle boundary"
    - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/wiki/index.md
      pointer: "current compiled page set"
    - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/log/phase2-wiki-compile-report.md
      pointer: "prior Phase 2 compile evidence"
    - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/manifests/phase0/corpus-profile.md
      pointer: "227 files scanned; 243 inventory entries; deterministic baseline"
    - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/manifests/phase0/source-priority-candidates.md
      pointer: "deterministic navigation hints"
  raw_sources:
    - path: sources/primary/managed-agent-kb/AGENT_KB_INDEX.md
      pointer: "Purpose; Scaffold convention; Agent KB root map; Working surface pointers; Boundary note"
    - path: sources/primary/managed-agent-kb/alfred/ESSENCE.md
      pointer: "operator-facing intake role boundary"
    - path: sources/primary/managed-agent-kb/meta_ops/ESSENCE.md
      pointer: "bounded orchestration and execution-control role boundary"
    - path: sources/primary/managed-agent-kb/meta_strategy/ESSENCE.md
      pointer: "option/recommendation role boundary"
    - path: sources/primary/managed-agent-kb/meta_detective/ESSENCE.md
      pointer: "adversarial validation role boundary"
    - path: sources/primary/managed-agent-kb/meta_detective/APPENDIX_INTERNAL_MODES.md
      pointer: "accepted appendix doctrine and anti-sprawl rule"
    - path: sources/primary/managed-agent-kb/special_ops__ai_handling_routing/ESSENCE.md
      pointer: "route states and repo-execution routing doctrine"
    - path: sources/primary/managed-agent-kb/special_ops__hygiene_clean/ESSENCE.md
      pointer: "structural QA, pointer integrity, closure-by-evidence doctrine"
```

## source_grounded_claims

```yaml
claims:
  - id: A01-C001
    claim: "The old system has an explicit KB root index for first-wave agents and maps each role to a KB root, default owner, and default validator."
    source_pointer: "AGENT_KB_INDEX.md / Purpose and Agent KB root map"
    confidence: high
    claim_label: raw_source

  - id: A01-C002
    claim: "Each durable agent KB root follows a five-file scaffold: ESSENCE.md, BEST_PRACTICES.md, MISTAKES.md, TEMPLATES.md, and LEARNING_QUEUE.md."
    source_pointer: "AGENT_KB_INDEX.md / Scaffold convention"
    confidence: high
    claim_label: raw_source

  - id: A01-C003
    claim: "LEARNING_QUEUE.md is explicitly candidate-only and is never runtime truth by placement alone."
    source_pointer: "AGENT_KB_INDEX.md / Scaffold convention; Hygiene Clean status vocabulary"
    confidence: high
    claim_label: raw_source

  - id: A01-C004
    claim: "ESSENCE.md is the compact activation and boundary surface: it states purpose, owns, does-not-own, read triggers, constraints, evidence status, owner, validator, source seed, and review horizon."
    source_pointer: "alfred/ESSENCE.md; meta_ops/ESSENCE.md; meta_strategy/ESSENCE.md; meta_detective/ESSENCE.md"
    confidence: high
    claim_label: source_backed_summary

  - id: A01-C005
    claim: "Appendices are the correct location for dense operational doctrine when detail would overload a compact role surface."
    source_pointer: "meta_detective/APPENDIX_INTERNAL_MODES.md / Purpose, Status, Doctrine statement"
    confidence: high
    claim_label: source_backed_summary

  - id: A01-C006
    claim: "The strongest reusable architecture is not the old role roster; it is the durable pattern of compact activation surfaces, explicit negative ownership, candidate/canon separation, and owner-validator metadata."
    source_pointer: "AGENT_KB_INDEX.md; all ESSENCE files read; meta_detective/APPENDIX_INTERNAL_MODES.md"
    confidence: high
    claim_label: source_backed_summary

  - id: A01-C007
    claim: "Historical OpenClaw paths in the mirrored sources are evidence pointers only; they do not establish current Apex or Claude-native runtime authority."
    source_pointer: "AGENT_KB_INDEX.md / Working surface pointers and Boundary note; old-agent semantic continuation report / historical path authority safety"
    confidence: high
    claim_label: source_backed_summary
```

## concepts_extracted

```yaml
concepts_extracted:
  - slug: five-file-agent-kb-scaffold
    label: "Five-file agent KB scaffold"
    definition: "Durable role doctrine stored as ESSENCE, BEST_PRACTICES, MISTAKES, TEMPLATES, and LEARNING_QUEUE."
    phase2_value: high
    source_pointer: "AGENT_KB_INDEX.md / Scaffold convention"

  - slug: compact-essence-activation-surface
    label: "Compact ESSENCE activation surface"
    definition: "A small, role-specific entrypoint that activates a boundary without pulling all evidence into the prompt."
    phase2_value: high
    source_pointer: "role ESSENCE files"

  - slug: owner-validator-agent-kb-model
    label: "Owner/validator agent KB model"
    definition: "A governance pattern where each durable role has an owner and a separate validator to avoid self-validation."
    phase2_value: high
    source_pointer: "AGENT_KB_INDEX.md / Agent KB root map"

  - slug: candidate-only-learning-queue
    label: "Candidate-only learning queue"
    definition: "A capture surface for useful future lessons that cannot become runtime truth without promotion."
    phase2_value: high
    source_pointer: "AGENT_KB_INDEX.md / Scaffold convention; Hygiene Clean status vocabulary"

  - slug: accepted-appendix-doctrine
    label: "Accepted appendix doctrine"
    definition: "Dense doctrine can be accepted as an appendix without becoming a new agent, KB root, config authority, or execution surface."
    phase2_value: high
    source_pointer: "meta_detective/APPENDIX_INTERNAL_MODES.md"
```

## entities_extracted

```yaml
entities_extracted:
  - id: old_openclaw_agent_kb_system
    type: historical_system
    current_authority: evidence_only
    source_pointer: "AGENT_KB_INDEX.md and mirrored source path structure"

  - id: reusable_scaffold_files
    type: artifact_family
    members: [ESSENCE.md, BEST_PRACTICES.md, MISTAKES.md, TEMPLATES.md, LEARNING_QUEUE.md]
    source_pointer: "AGENT_KB_INDEX.md / Scaffold convention"

  - id: compact_role_surfaces
    type: artifact_family
    members: [alfred/ESSENCE.md, meta_ops/ESSENCE.md, meta_strategy/ESSENCE.md, meta_detective/ESSENCE.md]
    source_pointer: "role ESSENCE files"
```

## contradictions_or_tensions

```yaml
contradictions_or_tensions:
  - id: A01-T001
    tension: "The five-file scaffold is reusable, but recreating every old role as a current permanent agent would create agent sprawl."
    disposition: "Preserve as doctrine/page pattern; do not promote roster to current runtime authority."
    confidence: high

  - id: A01-T002
    tension: "Appendices provide valuable depth but can recreate source sprawl unless routed through index-first retrieval pages."
    disposition: "Use adaptive ranked source sets and route-by-question sections in Phase 2 pages."
    confidence: medium
```

## open_questions

```yaml
open_questions:
  - id: A01-Q001
    question: "Which scaffold files should become reusable templates for Apex-native skills versus only historical wiki pages?"
    blocker: false
  - id: A01-Q002
    question: "Should accepted appendix doctrine map to concept pages, checklists, subagents, or skill references in future implementation?"
    blocker: false
```

## proposed_phase_2_wiki_targets

```yaml
summaries:
  - old-agent-kb-architecture
  - reusable-old-agent-kb-patterns
concepts:
  - agent-doctrine-and-promotion-patterns
  - migration-safety-patterns
entities:
  - reusable-artifact-families
```

## phase_gate_statement

```yaml
phase_2_gate:
  required_phrase: approve ingest
  status_for_this_rerun: approved
  note: "Operator provided approval in the initiating request; Phase 2 may proceed after this replacement Phase 1 set exists."
```
