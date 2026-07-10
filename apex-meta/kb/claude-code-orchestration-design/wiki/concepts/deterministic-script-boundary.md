---
title: "Deterministic Script Boundary"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "deterministic-script-boundary"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 112-123; deterministic script or hook required"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch03-external-orchestration-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch03-external-orchestration-patterns.md"
    source_hash: "dbe4e500d5c22cc61adc4e1364412da71d3db683"
    source_pointer: "claims B03-C006, B03-C012; deterministic validation and tool-output discipline"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts: []
related_entities:
  - "claude-code-orchestration-design/entities/claude-code-skills.md"
review_flags: []
---

# Deterministic Script Boundary

## Definition

A deterministic script is a reproducible, non-semantic mechanism reserved for mechanical checks, indexes, and repeatable transformations that do not require judgment or interpretation. The boundary this concept names is the line between what a script/hook can safely decide (shape, presence, format, mechanical policy) and what requires LLM inference (meaning, contradiction, workflow clarity, scope judgment). This boundary is grounded in the compile plan's `claude_mechanism_mapping_index` question of "when a deterministic script or hook is required" (compile plan lines 118-119) and in BMAD's two-pass validation pattern, where deterministic checks run first and inference validation runs second, skipping rules that already passed deterministically (B03-C006).

## Operating Rules

```yaml
rules:
  - "Use deterministic scripts for mechanical checks, indexes, and repeatable transformations that do not require semantic judgment (concept source)."
  - "Do not use deterministic scripts for concept synthesis or contradiction interpretation; reserve those for LLM inference passes (concept source; B03-C006)."
  - "Run deterministic checks before inference-based validation so LLM judgment is spent only on genuinely ambiguous or semantic rules, not on shape/presence/format checks a script can already confirm (B03-C006)."
  - "Script/tool output should follow ACI-style discipline: bounded, succinct, and explicit even in edge cases (e.g. explicit success text for empty output) so downstream agents do not misread silence as failure (B03-C012)."
  - "Script output is derived and rebuildable, not semantic doctrine; do not treat a script's report as a source of new facts about the corpus."
  - "This KB compile step writes no scripts; the boundary is documented as design doctrine only."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Frames the mapping question this concept answers: when is a deterministic script or hook required versus when should the task remain semantic/LLM-driven."
    coverage: "lines 110-123 claude_mechanism_mapping_index core questions, specifically when_a_deterministic_script_or_hook_is_required and which_rules_are_soft_guidance_vs_hard_enforcement."
  - source_id: "phase1-batch03-external-orchestration-patterns"
    rationale: "Only source with concrete comparative evidence of a deterministic-then-inference validation pattern (BMAD) and ACI-style deterministic tool-output discipline (SWE-agent), both of which define the operating rules above."
    coverage: "B03-C006 deterministic-then-inference validation; B03-C011/B03-C012 Agent-Computer-Interface and deterministic guardrail design; concepts_extracted deterministic-then-inference-validation, agent-computer-interface."
```

## Macro / Meso / Micro

### Macro

Deterministic scripts are the enforcement rung of the mechanism ladder reserved for work that is mechanical rather than semantic: format checks, presence checks, index generation, and repeatable transformations. The boundary matters because it prevents two opposite failure modes — using expensive LLM judgment on questions a script could answer deterministically and reproducibly, and using a rigid script to make judgment calls it cannot reliably make (contradiction detection, workflow-clarity assessment, scope interpretation).

### Meso

BMAD's skill-validator pattern is the clearest external evidence for this boundary: it runs deterministic checks first and inference validation second, explicitly skipping rules that already passed the deterministic pass and reserving LLM judgment for the remaining semantic or ambiguous rules (B03-C006). This two-pass ordering is itself a token-economy and drift-prevention device — deterministic passes are cheap, reproducible, and auditable, so spending them first narrows what the more expensive and less-reproducible inference pass has to cover. SWE-agent's Agent-Computer-Interface documentation supplies a second, complementary piece of evidence: good deterministic tool design (linting before edits are accepted, a bounded file viewer, succinct search results, explicit success text for empty output) materially improves agent results by removing ambiguity from tool output itself (B03-C011, B03-C012). Both patterns converge on the same principle — deterministic surfaces should be narrow, mechanical, and unambiguous, freeing semantic judgment for what only semantic judgment can do.

### Micro

Source pointers: compile plan lines 112-123 (claude_mechanism_mapping_index); `skill-validator.md` lines 3-18 (deterministic first pass before inference validation), lines 19-28 (validation workflow); `princeton-nlp__SWE-agent/docs/background/aci.md` lines 3-10 (ACI definition and importance), lines 11-17 (linter, file viewer, search command, empty-output handling).

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "BMAD's validation pattern uses deterministic checks first and inference validation second, skipping rules that passed deterministically and reserving LLM judgment for semantic or ambiguous rules."
    source_pointer: "B03-C006; skill-validator.md lines 3-28"
    confidence: "medium"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "SWE-agent's ACI includes design details that resemble deterministic guardrails: linting before edits are accepted, a bounded file viewer, succinct full-directory search results, and explicit success text for empty command output."
    source_pointer: "B03-C012; princeton-nlp__SWE-agent/docs/background/aci.md lines 11-17"
    confidence: "medium"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "Apex should copy patterns, not full external repo architectures: deterministic-then-inference validation from BMAD and ACI/tool-output discipline from SWE-agent are named as reusable patterns rather than direct implementation targets."
    source_pointer: "B03-C013"
    confidence: "medium"
    claim_label: "source_backed_summary"
```

## Routes Here

```yaml
routes:
  - question: "When should Apex use a deterministic script or hook instead of relying on skill-prose or CLAUDE.md guidance?"
    leads_to: "claude-code-orchestration-design/summaries/claude-mechanism-decision-model.md"
    rationale: "The mechanism decision model places deterministic scripts/hooks as the rung reserved for high-risk, mechanically-checkable gates, directly above ephemeral/persistent agents."
  - related_page: "claude-code-orchestration-design/entities/claude-code-skills.md"
    relation: "Skills carry procedural guidance; this concept marks the point at which guidance is insufficient and a deterministic check or hook is required instead."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch03-external-orchestration-patterns"
    source_pointer: "B03-C006"
    supports: "Deterministic-then-inference validation ordering"
  - source_id: "phase1-batch03-external-orchestration-patterns"
    source_pointer: "B03-C011, B03-C012"
    supports: "Agent-Computer-Interface deterministic tool-output discipline"
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_pointer: "lines 112-123"
    supports: "Mapping question this concept answers within claude_mechanism_mapping_index"
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Which BMAD validator rules generalize to Apex skill packages without importing BMAD-specific naming/prefix assumptions? (B03-Q002, open question)"
    source_pointer: "B03-Q002"
    proposed_handling: "planning_task_candidate"
  - id: U002
    description: "What is the minimum ACI/tool-output contract Apex should require for local agents or Codex-style repo executors? (B03-Q004, open question)"
    source_pointer: "B03-Q004"
    proposed_handling: "planning_task_candidate"
  - id: U003
    description: "BMAD's skill validator has BMAD-specific naming rules such as a bmad- prefix, which should not be imported into Apex unless Apex explicitly chooses a project-specific prefix policy (B03-T002, contradiction)."
    source_pointer: "B03-T002"
    proposed_handling: "revisit_source"
  - id: U004
    description: "S6 writes no scripts in this KB compile step; this concept remains design doctrine until an actual deterministic script or hook is proposed and reviewed."
    source_pointer: "compile plan section 7 (phase2_non_goals)"
    proposed_handling: "leave_as_gap"
```
