---
title: "Ephemeral Subagent Boundary"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "ephemeral-subagent-boundary"
source_refs:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch02-claude-code-orchestration-surface.md"
    source_hash: "505c6297d2c7198cbf0e77800577ab8e18a25d73"
    source_pointer: "claims B02-C008 through B02-C009; subagent context isolation"
    source_storage_mode: "pointer_only"
  - source_id: "operator-phase1-review-decisions-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md"
    source_hash: "34d9c16967d2f7f49b716d75c8bb1a2a10eb96a7"
    source_pointer: "lines 76-87; ephemeral subagent policy"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "persistent-agent-vs-ephemeral-subagent"
  - "mechanism-ladder"
related_entities:
  - "claude-code-subagents"
review_flags: []
---

# Ephemeral Subagent Boundary

## Definition

An ephemeral subagent is a Claude Code subagent invocation that exists only for the duration of a single delegated task. It runs in an isolated context window, performs exploratory, comparison, or scouting work, and returns a compact summary to the main conversation without persisting as a named, reusable role. This is distinct from a persistent subagent definition that is checked into the project as a stable, repeatedly invoked role (see `persistent-agent-vs-ephemeral-subagent`).

## Operating Rules

```yaml
rules:
  - "Use an ephemeral subagent when the task benefits from a separate context window and a compact returned summary, rather than polluting the main thread with exploration traces."
  - "Do not promote ephemeral subagent output directly to doctrine; treat findings as candidate results pending review."
  - "Do not create a persistent subagent definition for a task that only needs one-off scouting or comparison reading."
  - "Ephemeral subagents read only the task prompt and a limited set of source references, not the full project context."
  - "No subagent definition files are written during Phase 2 KB compile (S6); this concept describes a design pattern, not a shipped runtime artifact."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    rationale: "Primary-docs-grounded claims (B02-C008, B02-C009) establish subagent context isolation as the mechanism this concept specializes."
    coverage: "Defines subagent isolation, built-in Explore/Plan subagent behavior, and general-purpose subagent scope."
  - source_id: "operator-phase1-review-decisions-20260702"
    rationale: "Operator decision Q004 explicitly enumerates when a subagent role should be ephemeral rather than persistent, which is the direct compile-policy basis for this page."
    coverage: "Q004_subagent_persistence: ephemeral_when list (one-off source scouting, temporary comparison reading, broad exploration)."
```

## Macro / Meso / Micro

### Macro

Claude Code's subagent mechanism supports two very different usage shapes: a small number of stable, named roles that recur across many tasks, and a much larger, unbounded set of one-off delegations used to keep exploratory work out of the main context. Apex's Phase 2 compile policy treats these as separate design points rather than one undifferentiated "subagent" concept, so that KB pages and later implementation work do not default to creating a permanent agent definition for every delegated task.

### Meso

The boundary is drawn on repeatability and stability: if a role does one-off source scouting, temporary comparison reading, or broad exploration, it stays ephemeral — invoked ad hoc with a scoped prompt and no persisted definition. If a role instead performs a repeated domain function, a stable validation/audit function, or a security-sensitive repo-executor function with explicit constraints, it graduates to a persistent, validated subagent definition. This mirrors the underlying Claude Code mechanism, where subagents isolate exploratory or specialized work in a separate context window and return summaries to the main conversation, regardless of whether the subagent definition itself is persistent or improvised per task.

### Micro

Per B02-C008 and B02-C009, subagents isolate exploratory or specialized work in a separate context window, return summaries to preserve main-thread context, and built-in Explore/Plan subagents are read-only/research-oriented while general-purpose subagents can use broader tools for multi-step operations (`phase1-batch02-claude-code-orchestration-surface.md` claims B02-C008, B02-C009). Operator decision Q004 (`operator-phase1-review-decisions-20260702.md` lines 74-84) lists "one-off source scouting," "temporary comparison reading," and "broad exploration" as the ephemeral trigger conditions, contrasted with the persistent_when conditions used on the companion concept page.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Subagents isolate exploratory or specialized work in separate context windows and return summaries to the main conversation, preserving main-thread context and enabling tool/model specialization."
    source_pointer: "phase1-batch02-claude-code-orchestration-surface.md claim B02-C008"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "Built-in Explore and Plan subagents are read-only/research-oriented and keep exploration results out of the main context, while general-purpose subagents can perform complex multi-step operations with broader tools."
    source_pointer: "phase1-batch02-claude-code-orchestration-surface.md claim B02-C009"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "A subagent role should remain ephemeral (invoked ad hoc, no persistent definition) when it performs one-off source scouting, temporary comparison reading, or broad exploration."
    source_pointer: "operator-phase1-review-decisions-20260702.md Q004_subagent_persistence.ephemeral_when"
    confidence: "high"
    claim_label: "source_backed_summary"
```

## Routes Here

```yaml
routes:
  - question: "When should a Claude Code delegation just be a one-off subagent call instead of a checked-in agent definition?"
    leads_to: "claude-code-orchestration-design/concepts/ephemeral-subagent-boundary.md"
    rationale: "Directly answers the ephemeral-vs-persistent trigger question for a single delegation."
  - related_page: "claude-code-orchestration-design/concepts/persistent-agent-vs-ephemeral-subagent.md"
    relation: "Companion concept page covering the full persistent/ephemeral decision, including the persistent_when conditions."
  - related_page: "claude-code-orchestration-design/concepts/mechanism-ladder.md"
    relation: "Ephemeral subagent use is one rung on the broader least-powerful-mechanism selection ladder."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_pointer: "B02-C008, B02-C009"
    supports: "Subagent context isolation mechanism underlying ephemeral use."
  - source_id: "operator-phase1-review-decisions-20260702"
    source_pointer: "Q004_subagent_persistence.ephemeral_when"
    supports: "Explicit trigger conditions for treating a subagent as ephemeral."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Open question: which Apex subagent definitions should be persistent project files, and which should remain ephemeral CLI/session definitions? No concrete roster exists yet."
    source_pointer: "phase1-batch02-claude-code-orchestration-surface.md B02-Q003"
    proposed_handling: "planning_task_candidate"
  - id: U002
    description: "No subagent definition is written during S6; this page describes a design pattern only, not a shipped runtime artifact. Revisit once actual subagent files are authored."
    source_pointer: "operator-phase1-review-decisions-20260702.md phase2_implications.write_as_boundary_or_open_question (full_subagent_roster)"
    proposed_handling: "revisit_source"
```
