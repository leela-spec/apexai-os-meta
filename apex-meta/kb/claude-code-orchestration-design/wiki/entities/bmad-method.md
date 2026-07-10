---
title: "BMAD-METHOD"
page_type: entity
kb_slug: "claude-code-orchestration-design"
entity_slug: "bmad-method"
entity_type: "external_repo"
source_refs:
  - source_id: "phase1-batch03-external-orchestration-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch03-external-orchestration-patterns.md"
    source_hash: "dbe4e500d5c22cc61adc4e1364412da71d3db683"
    source_pointer: "claims B03-C005 through B03-C007; entities extracted"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "owner-validator-split"
  - "validator-as-non-executor"
review_flags: []
---

# BMAD-METHOD

## Identity

```yaml
entity:
  label: "bmad-code-org/BMAD-METHOD"
  type: "external_repo"
  aliases:
    - "BMAD-METHOD"
    - "BMAD"
```

## Source-Grounded Summary

BMAD-METHOD is read in this KB as a comparative source for two things: a platform-by-platform native-skill migration checklist (`tools/docs/native-skills-migration-checklist.md`, B03-C005) and a skill validator that runs deterministic checks before inference-level checks (`tools/skill-validator.md`, B03-C006, B03-C007). Both documents are secondary/comparative material, not authoritative over Claude Code/Agent Skills documentation. BMAD's validator pattern is the direct source for this KB's `deterministic-then-inference-validation` concept and is one of the two sources synthesized into `owner-validator-split` and `validator-as-non-executor`.

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch03-external-orchestration-patterns"
    rationale: "Sole ingested source for this entity; ranked first (and only) because all claims trace to this batch's reading of the migration checklist and skill validator."
    coverage: "B03-C005 (platform migration pattern), B03-C006 (deterministic-then-inference validation), B03-C007 (package encapsulation rules)."
```

## Macro / Meso / Micro

### Macro

BMAD-METHOD contributes two reusable comparative patterns: a disciplined platform-migration checklist (fresh install, reinstall/upgrade, legacy cleanup, path compatibility, ancestor conflict behavior — B03-C005) and a deterministic-then-inference validation model that is the single most load-bearing external pattern in this KB, feeding directly into the owner/validator-split and validator-as-non-executor concepts.

### Meso

The migration checklist (B03-C005) treats adopting native skills as a testable, platform-by-platform rollout problem rather than a single global switch — this is read as a comparative discipline pattern, not as a set of steps Apex should copy verbatim. The skill validator (B03-C006, B03-C007) is more directly useful: it runs mechanical/deterministic checks first, skips whatever already passed, and reserves LLM/inference judgment for semantic or ambiguous rules; it also enforces package encapsulation (relative internal references, no `installed_path` anti-pattern, no reaching into other skill directories by file path). Both patterns are explicitly flagged as needing filtering before Apex reuse: BMAD's validator carries BMAD-specific naming rules (e.g. a `bmad-` prefix convention) that should not be imported without an explicit Apex-specific decision (B03-T002).

### Micro

- B03-C005: "BMAD's migration checklist treats native skill adoption as a platform-by-platform migration problem with tests for fresh install, reinstall/upgrade, legacy cleanup, path compatibility, and ancestor conflict behavior." (`native-skills-migration-checklist.md` lines 3-28, 42-80, 194-208)
- B03-C006: "BMAD's validation pattern uses deterministic checks first and inference validation second..." (`skill-validator.md` lines 3-28)
- B03-C007: "BMAD's validator emphasizes package encapsulation: internal references should be relative from the originating file, `installed_path` is an anti-pattern, external references should use project-root/config variables, and skills should not reach into other skill directories by file path." (`skill-validator.md` lines 119-177)

## Key Claims

```yaml
key_claims:
  - claim_id: B03-C005
    claim: "BMAD's migration checklist treats native skill adoption as a platform-by-platform migration problem with tests for fresh install, reinstall/upgrade, legacy cleanup, path compatibility, and ancestor conflict behavior."
    source_pointer: "phase1-batch03-external-orchestration-patterns.md; native-skills-migration-checklist.md lines 3-28, 42-80, 194-208"
    confidence: "medium"
    claim_label: "source_backed_summary"
  - claim_id: B03-C006
    claim: "BMAD's validation pattern uses deterministic checks first and inference validation second, skipping rules that passed deterministically and reserving LLM judgment for semantic or ambiguous rules."
    source_pointer: "phase1-batch03-external-orchestration-patterns.md; skill-validator.md lines 3-28"
    confidence: "medium"
    claim_label: "source_backed_summary"
  - claim_id: B03-C007
    claim: "BMAD's validator emphasizes package encapsulation: internal references should be relative from the originating file, installed_path is an anti-pattern, external references should use project-root/config variables, and skills should not reach into other skill directories by file path."
    source_pointer: "phase1-batch03-external-orchestration-patterns.md; skill-validator.md lines 119-177"
    confidence: "medium"
    claim_label: "source_backed_summary"
```

## Routes Here

```yaml
routes:
  - question: "Where does the deterministic-then-inference validation pattern that Apex's owner/validator split borrows from actually come from?"
    leads_to: "claude-code-orchestration-design/entities/bmad-method.md"
    rationale: "BMAD's skill-validator.md is the direct source of that two-pass validation mechanic."
  - related_page: "claude-code-orchestration-design/concepts/owner-validator-split.md"
    relation: "Owner-validator-split synthesizes BMAD's B03-C006/C007 validation pattern with Apex's own artifact-contract and operator-gate doctrine."
  - related_page: "claude-code-orchestration-design/concepts/validator-as-non-executor.md"
    relation: "Validator-as-non-executor also draws on BMAD's two-pass validation mechanic as one of its two source lines."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch03-external-orchestration-patterns"
    source_pointer: "native-skills-migration-checklist.md lines 3-28, 42-80, 194-208 (B03-C005)"
    supports: "Platform-migration checklist pattern"
  - source_id: "phase1-batch03-external-orchestration-patterns"
    source_pointer: "skill-validator.md lines 3-28, 119-177 (B03-C006, B03-C007)"
    supports: "Deterministic-then-inference validation and package encapsulation patterns"
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "BMAD's skill validator has BMAD-specific naming rules (e.g. a bmad- prefix), which should not be imported into Apex unless Apex explicitly chooses a project-specific prefix policy."
    source_pointer: "phase1-batch03-external-orchestration-patterns.md; B03-T002, skill-validator.md lines 69-83"
    proposed_handling: "leave_as_gap"
  - id: U002
    description: "Which BMAD validator rules generalize to Apex skill packages without importing BMAD-specific naming/prefix assumptions is an open question."
    source_pointer: "phase1-batch03-external-orchestration-patterns.md; B03-Q002"
    proposed_handling: "planning_task_candidate"
  - id: U003
    description: "External repos optimize for their own runtime assumptions and may conflict with Apex's source-preserving KB lifecycle; BMAD's migration/validation patterns are useful but must not override Apex's operator gate, source custody, or Phase 1/Phase 2 separation."
    source_pointer: "phase1-batch03-external-orchestration-patterns.md; B03-C014"
    proposed_handling: "leave_as_gap"
```
