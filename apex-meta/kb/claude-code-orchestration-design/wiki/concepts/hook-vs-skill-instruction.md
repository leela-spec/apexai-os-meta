---
title: "Hook vs Skill Instruction"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "hook-vs-skill-instruction"
source_refs:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch02-claude-code-orchestration-surface.md"
    source_hash: "505c6297d2c7198cbf0e77800577ab8e18a25d73"
    source_pointer: "claims B02-C005 through B02-C007 and B02-C015; hooks and enforcement"
    source_storage_mode: "pointer_only"
  - source_id: "operator-phase1-review-decisions-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md"
    source_hash: "34d9c16967d2f7f49b716d75c8bb1a2a10eb96a7"
    source_pointer: "lines 54-68; hard vs soft enforcement"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "mechanism-ladder"
  - "mcp-decision-model"
related_entities:
  - "claude-code-hooks"
review_flags: []
---

# Hook vs Skill Instruction

## Definition

Hook-vs-skill instruction is the design distinction between two kinds of behavioral control in Claude Code: skill/prompt instructions, which guide model behavior through readable prose the model may or may not follow with perfect fidelity, and hooks, which are lifecycle-bound event handlers that can deterministically block, transform, verify, log, or trigger actions around tool calls and turns. The concept names the rule that hard boundaries should be implemented as hooks (or equivalent deterministic settings/permissions), not left to skill prose or `CLAUDE.md` guidance alone.

## Operating Rules

```yaml
rules:
  - "Use a hook (or settings/permissions enforcement) when a boundary must hold reliably before or after a tool action, regardless of model compliance."
  - "Use skill or CLAUDE.md prose only for guidance-level concerns: style, terminology, preferred source ordering, or other low-risk conventions."
  - "Reserve hard hook enforcement for the operator-designated high-risk gates: Phase 2 without the approval phrase, writes outside the KB root, raw source delete/mutation, KB schema overwrite without an explicit flag, and destructive archive delete."
  - "Do not encode a destructive-operation, Phase 2, or source-custody boundary only in skill prose or CLAUDE.md; treat that as a weaker, non-authoritative substitute for a hook."
  - "No hook files are authored during Phase 2 KB compile (S6); this page documents the design boundary, not a shipped hook."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    rationale: "Provides the primary-docs-grounded definition of hooks (B02-C005, B02-C006, B02-C007) and the explicit recommendation (B02-C015) that Apex reserve hooks for hard gates."
    coverage: "Hook lifecycle events, the PreToolUse blocking example, hook scope levels, and the soft-guidance-vs-hard-enforcement recommendation."
  - source_id: "operator-phase1-review-decisions-20260702"
    rationale: "Operator decision Q002 converts the B02-C015 recommendation into an explicit hard_enforce/soft_enforce list, making this the compile-policy anchor for the page."
    coverage: "Q002_hook_or_script_enforcement: enumerated hard_enforce and soft_enforce categories."
```

## Macro / Meso / Micro

### Macro

Claude Code deliberately separates guidance surfaces from enforcement surfaces. `CLAUDE.md`, rules, and skill prose shape what the model tends to do; settings, permissions, and hooks can constrain what actually happens at the tool-call boundary. Apex's compile policy adopts this separation directly: anything the KB or a downstream skill wants to be a genuine boundary, rather than a strong suggestion, must be expressed (eventually) as a hook or equivalent deterministic control, not as instructional text that a model could plausibly override or forget under pressure.

### Meso

The pattern shows up concretely in the `PreToolUse` hook example, which can deny a destructive `rm -rf` command before it executes — a decision that does not depend on the model choosing to comply with a warning. Hooks can also be scoped at user, project, local-override, managed-policy, plugin, or active skill/agent frontmatter level, making them a cross-cutting enforcement layer distinct from ordinary prompt guidance. The operator's Q002 decision operationalizes this for the Apex KB itself: five specific high-risk gates (Phase 2 gating, writes outside KB root, raw source mutation, schema overwrite, destructive archive delete) are marked hard_enforce, while style, terminology, source ordering, and other low-risk conventions are marked soft_enforce and can remain in prose.

### Micro

B02-C005 defines hooks as lifecycle-bound event handlers running shell commands, HTTP endpoints, MCP tools, prompts, or agents at session/turn/tool-call/subagent/compaction/file-change events (`phase1-batch02-claude-code-orchestration-surface.md` claim B02-C005). B02-C006 gives the concrete `PreToolUse` deny-decision example for destructive `rm -rf` commands (claim B02-C006). B02-C015 is the direct recommendation: "Apex should reserve hooks and permissions for hard gates, and avoid relying on CLAUDE.md, rules, or skill prose to enforce destructive-operation, Phase 2, or source-custody boundaries" (claim B02-C015). Contradiction B02-T001 states this as a tension to actively guard against: any Apex design that encodes hard gates only in skill prose or CLAUDE.md is weaker than one backed by hooks or deterministic scripts (`phase1-batch02-claude-code-orchestration-surface.md` B02-T001). Operator decision Q002 (`operator-phase1-review-decisions-20260702.md` lines 52-65) lists the exact hard_enforce set: `phase2_without_approve_ingest`, `write_outside_kb_root`, `raw_source_delete_or_mutation`, `kb_schema_overwrite_without_explicit_flag`, `destructive_archive_delete`.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Hooks are lifecycle-bound event handlers that can run shell commands, HTTP endpoints, MCP tools, prompts, or agents at session, turn, tool-call, subagent, compaction, and file-change events."
    source_pointer: "phase1-batch02-claude-code-orchestration-surface.md claim B02-C005"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "Apex should reserve hooks and permissions for hard gates, and avoid relying on CLAUDE.md, rules, or skill prose to enforce destructive-operation, Phase 2, or source-custody boundaries."
    source_pointer: "phase1-batch02-claude-code-orchestration-surface.md claim B02-C015"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "Operator decision Q002 hard-enforces exactly five high-risk gates via hook/script mechanisms (Phase 2 without approve-ingest, writes outside KB root, raw source delete/mutation, KB schema overwrite without explicit flag, destructive archive delete) and soft-enforces style/terminology/ordering conventions in prose."
    source_pointer: "operator-phase1-review-decisions-20260702.md Q002_hook_or_script_enforcement"
    confidence: "high"
    claim_label: "source_backed_summary"
```

## Routes Here

```yaml
routes:
  - question: "Should this boundary be written as a hook, or is a skill instruction enough?"
    leads_to: "claude-code-orchestration-design/concepts/hook-vs-skill-instruction.md"
    rationale: "This page is the direct decision point for choosing enforcement mechanism."
  - related_page: "claude-code-orchestration-design/entities/claude-code-hooks.md"
    relation: "Entity page describing the underlying hooks mechanism this concept relies on."
  - related_page: "claude-code-orchestration-design/concepts/mechanism-ladder.md"
    relation: "Hook-vs-skill selection is one instance of the broader layered-mechanism selection pattern."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_pointer: "B02-C005, B02-C006, B02-C007, B02-C015, B02-T001"
    supports: "Definition of hooks as enforcement mechanism and the recommendation to reserve them for hard gates."
  - source_id: "operator-phase1-review-decisions-20260702"
    source_pointer: "Q002_hook_or_script_enforcement (lines 52-65)"
    supports: "Concrete hard_enforce / soft_enforce boundary for the Apex KB."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Open question: which Apex gates require hook-level enforcement rather than skill-prose instruction only, beyond the five gates the operator has already named? The full enforcement surface is not yet enumerated."
    source_pointer: "phase1-batch02-claude-code-orchestration-surface.md B02-Q001"
    proposed_handling: "planning_task_candidate"
  - id: U002
    description: "Contradiction: guidance and enforcement are distinct surfaces; any Apex design that encodes hard gates only in skill prose or CLAUDE.md is weaker than a hook-backed one. Must be checked against future skill/CLAUDE.md drafts."
    source_pointer: "phase1-batch02-claude-code-orchestration-surface.md B02-T001"
    proposed_handling: "audit_item"
  - id: U003
    description: "No hook files exist yet; the exact hook enforcement scope beyond the five high-risk gates remains an explicit operator-flagged boundary/open question for Phase 2 implications."
    source_pointer: "operator-phase1-review-decisions-20260702.md phase2_implications.write_as_boundary_or_open_question"
    proposed_handling: "revisit_source"
```
