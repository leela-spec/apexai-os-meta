---
title: "Repo Execution Routing Safety"
page_type: concept
kb_slug: "old-apex-full-orchestration-agent-kb"
concept_slug: "repo-execution-routing-safety"
source_refs:
  - source_id: "semantic-continuation-after-lint-closure"
    source_path: "apex-meta/kb/old-apex-full-orchestration-agent-kb/outputs/synthesis/apex-kb-semantic-continuation-after-lint-closure.md"
    source_hash: "NA"
    source_pointer: "semantic meaning of lint-repo-execution-router; remaining LLM-owned KB work"
    source_storage_mode: "copy_into_kb"
  - source_id: "final-combined-lint-audit-status-postflight-report"
    source_path: "apex-meta/kb/old-apex-full-orchestration-agent-kb/outputs/synthesis/final-combined-lint-audit-status-postflight-report.md"
    source_hash: "NA"
    source_pointer: "commands_validated; validation; notes"
    source_storage_mode: "copy_into_kb"
  - source_id: "validation-and-routing-guardrails"
    source_path: "apex-meta/kb/old-apex-full-orchestration-agent-kb/wiki/concepts/validation-and-routing-guardrails.md"
    source_hash: "NA"
    source_pointer: "Definition; Operating Rules; Evidence"
    source_storage_mode: "copy_into_kb"
created_at: "2026-07-03T00:00:00Z"
updated_at: "2026-07-03T00:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - validation-and-routing-guardrails
  - migration-safety-patterns
  - deterministic-execution-safety-after-lint-closure
related_entities: []
review_flags:
  - "This concept governs routing and boundary classification; it does not itself authorize repo mutation."
---

# Repo Execution Routing Safety

## Definition

Repo execution routing safety is the rule set that keeps repo-affecting instructions, deterministic validation, and LLM semantic synthesis from collapsing into one ambiguous execution lane.

After lint closure, `lint-repo-execution-router` is a finalized deterministic safety primitive. It detects handovers or synthesis surfaces that omit or blur target paths, operation class, forbidden actions, post-write checks, or stop conditions. Its purpose is to preserve executor boundaries and prevent semantic KB continuation from being accidentally converted into Codex implementation.

## Operating Rules

```yaml
rules:
  - "Route exact target paths before repo-affecting work."
  - "Separate operation classes: semantic wiki compile, deterministic validation, script mutation, repo patching, and final approval are not interchangeable."
  - "Do not allow advisory-only routing language to collapse into executable repo mutation."
  - "Do not collapse validator, executor, and final approver roles."
  - "For deterministic Codex handoffs, require target files, exact commands, expected result, commit/push policy, validation commands, and stop conditions."
  - "If the task is semantic KB continuation and codex_required is false, do not create a Codex prompt unless a later deterministic blocker requires it."
```

## Boundary Split

```yaml
boundary_split:
  llm_semantic_compiler:
    owns:
      - semantic synthesis
      - wiki summary/concept/entity drafting
      - contradiction interpretation
      - audit question framing
    does_not_own:
      - deterministic script modification
      - repo patch execution
      - final business approval
  deterministic_tools:
    own:
      - lint checks
      - audit reports
      - index and retrieval rebuilds
      - status and health checks
    do_not_own:
      - semantic claim generation
  codex_or_repo_executor:
    owns:
      - implementation when explicitly routed
      - command execution when required
    requires:
      - exact path scope
      - command list
      - expected result
      - commit and push instruction when requested
  operator:
    owns:
      - approval gates
      - authority promotion decisions
      - acceptance of unresolved risk
```

## Evidence

```yaml
evidence:
  - source_id: semantic-continuation-after-lint-closure
    source_pointer: "semantic_meaning / repo_execution_routing_safety"
    supports: "The lint protects executor boundaries and detects unclear or unsafe execution routing."
  - source_id: final-combined-lint-audit-status-postflight-report
    source_pointer: "commands_validated and validation"
    supports: "lint-repo-execution-router is part of the finalized validated command surface."
  - source_id: validation-and-routing-guardrails
    source_pointer: "Operating Rules"
    supports: "Validators produce findings and routing outputs; they do not implement the fix under review."
```

## Contradictions and Open Questions

```yaml
contradictions: []
open_questions:
  - "Which recorded repo-execution-router findings should be converted into future wiki edits versus deterministic cleanup tasks?"
  - "Should this concept later be linked to a stricter machine-readable handoff schema?"
```
