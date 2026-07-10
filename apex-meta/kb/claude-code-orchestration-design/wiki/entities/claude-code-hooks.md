---
title: "Claude Code Hooks"
page_type: entity
kb_slug: "claude-code-orchestration-design"
entity_slug: "claude-code-hooks"
entity_type: "tool"
source_refs:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch02-claude-code-orchestration-surface.md"
    source_hash: "505c6297d2c7198cbf0e77800577ab8e18a25d73"
    source_pointer: "claims B02-C005 through B02-C007; entities extracted"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "hook-vs-skill-instruction"
review_flags: []
---

# Claude Code Hooks

## Identity

```yaml
entity:
  label: "Claude Code Hooks"
  type: "runtime_component"
  aliases:
    - "hooks"
    - "hook enforcement gate"
```

## Source-Grounded Summary

Claude Code hooks are lifecycle-bound event handlers that can run shell commands, HTTP endpoints, MCP tools, prompts, or agents at defined points in a session: session start/end, turn boundaries, tool calls (`PreToolUse`/`PostToolUse`-style events), subagent invocation, context compaction, and file-change events. A `PreToolUse` hook can enforce a hard safety or policy decision before a tool call executes — the reference example blocks destructive `rm -rf` commands via a deny decision. Hook scope can be set at user, project, local project-override, managed-policy, plugin, or active skill/agent frontmatter level, which makes hooks a cross-cutting enforcement layer distinct from ordinary prompt guidance such as `CLAUDE.md`, rules, or skill instructions. Within the Apex KB, hooks are the designated mechanism for hard, deterministic gates (see `hook-vs-skill-instruction`), and operator decision Q002 names five specific high-risk gates that must be hard-enforced this way: Phase 2 without the approval phrase, writes outside the KB root, raw source delete/mutation, KB schema overwrite without an explicit flag, and destructive archive delete.

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    rationale: "Sole and sufficient source for this entity: primary-docs-grounded claims B02-C005 through B02-C007 define hooks' lifecycle events, enforcement example, and scope levels, and the entities_extracted block names hooks as a distinct runtime component."
    coverage: "Hook lifecycle definition, hook event table, PreToolUse blocking example, hook configuration/scope, matcher semantics."
```

## Macro / Meso / Micro

### Macro

Hooks are Claude Code's deterministic enforcement mechanism, sitting apart from the guidance mechanisms (`CLAUDE.md`, rules, skill prose) that only shape model behavior probabilistically. Any boundary Apex needs to hold reliably — regardless of whether the model "remembers" or "chooses" to comply — should ultimately be expressed as a hook rather than as an instruction.

### Meso

Hooks attach to specific lifecycle events (session, turn, tool-call, subagent, compaction, file-change) and can run a shell command, call an HTTP endpoint, invoke an MCP tool, or trigger a prompt/agent. The canonical example is a `PreToolUse` hook that intercepts a tool call before execution and can deny it outright — used in the reference docs to block destructive `rm -rf` commands. Hooks can be configured at multiple scope levels (user, project, local override, managed policy, plugin, or embedded in an active skill/agent's frontmatter), which lets Apex apply different hook sets depending on trust level and deployment context. Operator decision Q002 converts this general capability into a concrete Apex policy: five gates (Phase 2 gating, KB-root write boundary, raw source immutability, schema overwrite protection, destructive archive delete protection) are hard_enforce, while everything else (style, terminology, ordering, low-risk conventions) stays soft_enforce in prose.

### Micro

B02-C005: "Hooks are lifecycle-bound event handlers that can run shell commands, HTTP endpoints, MCP tools, prompts, or agents at session, turn, tool-call, subagent, compaction, and file-change events" (`phase1-batch02-claude-code-orchestration-surface.md` claim B02-C005). B02-C006: "A PreToolUse hook can enforce a hard safety or policy decision before a tool call executes; the example blocks destructive rm -rf commands through a deny decision" (claim B02-C006). B02-C007: "Hook scope can be user, project, local project override, managed policy, plugin, or active skill/agent frontmatter; this makes hooks a cross-cutting enforcement layer distinct from normal prompt guidance" (claim B02-C007). The entities_extracted block labels `claude-code-hooks` as a `runtime_component` with role "Lifecycle event enforcement and automation mechanism," confidence high.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Hooks are lifecycle-bound event handlers that can run shell commands, HTTP endpoints, MCP tools, prompts, or agents at session, turn, tool-call, subagent, compaction, and file-change events."
    source_pointer: "phase1-batch02-claude-code-orchestration-surface.md claim B02-C005"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "A PreToolUse hook can enforce a hard safety or policy decision before a tool call executes; the reference example blocks destructive rm -rf commands through a deny decision."
    source_pointer: "phase1-batch02-claude-code-orchestration-surface.md claim B02-C006"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "Hook scope can be user, project, local project override, managed policy, plugin, or active skill/agent frontmatter, making hooks a cross-cutting enforcement layer distinct from normal prompt guidance."
    source_pointer: "phase1-batch02-claude-code-orchestration-surface.md claim B02-C007"
    confidence: "high"
    claim_label: "source_backed_summary"
```

## Routes Here

```yaml
routes:
  - question: "What Claude Code mechanism enforces a rule deterministically instead of just suggesting it?"
    leads_to: "claude-code-orchestration-design/entities/claude-code-hooks.md"
    rationale: "This entity page is the canonical reference for the hooks mechanism itself."
  - related_page: "claude-code-orchestration-design/concepts/hook-vs-skill-instruction.md"
    relation: "Concept page built directly on this entity, contrasting hook enforcement with skill-prose guidance and naming Apex's hard_enforce gate list."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_pointer: "B02-C005"
    supports: "Definition of hooks as lifecycle-bound event handlers across multiple event types and action targets."
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_pointer: "B02-C006"
    supports: "PreToolUse deny-decision example demonstrating deterministic enforcement."
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_pointer: "B02-C007"
    supports: "Multi-level hook scope, establishing hooks as a cross-cutting enforcement layer."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Open question: which Apex gates require hook-level enforcement rather than skill-prose instruction only, beyond the five gates the operator has already named?"
    source_pointer: "phase1-batch02-claude-code-orchestration-surface.md B02-Q001"
    proposed_handling: "planning_task_candidate"
  - id: U002
    description: "Contradiction: guidance and enforcement are distinct surfaces; any Apex design encoding hard gates only in skill prose or CLAUDE.md is weaker than a hook-backed equivalent. Must be checked whenever a new boundary is proposed."
    source_pointer: "phase1-batch02-claude-code-orchestration-surface.md B02-T001"
    proposed_handling: "audit_item"
  - id: U003
    description: "No hook files are created during Phase 2 KB compile (S6); this entity page documents the mechanism, not a shipped hook. The exact hook enforcement scope beyond the five named high-risk gates is an explicit operator-flagged open question."
    source_pointer: "operator-phase1-review-decisions-20260702.md Q002_hook_or_script_enforcement; phase2_implications.write_as_boundary_or_open_question"
    proposed_handling: "revisit_source"
```
