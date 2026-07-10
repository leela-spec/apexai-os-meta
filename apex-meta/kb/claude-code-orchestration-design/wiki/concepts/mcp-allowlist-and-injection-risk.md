---
title: "MCP Allowlist and Injection Risk"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "mcp-allowlist-and-injection-risk"
source_refs:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch02-claude-code-orchestration-surface.md"
    source_hash: "505c6297d2c7198cbf0e77800577ab8e18a25d73"
    source_pointer: "B02-C013; MCP requires explicit trust evaluation and prompt-injection risk handling"
    source_storage_mode: "pointer_only"
  - source_id: "operator-phase1-review-decisions-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md"
    source_hash: "34d9c16967d2f7f49b716d75c8bb1a2a10eb96a7"
    source_pointer: "phase2_implications: MCP server allowlist and committed .mcp.json policy remain boundary/open question"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T14:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "needs_review"
related_concepts:
  - "mcp-config-boundary"
  - "mcp-decision-model"
related_entities:
  - "model-context-protocol"
review_flags:
  - "Concrete allowlist schema and injection-risk checklist remain unwritten; page documents the risk boundary, not an implementation."
---

# MCP Allowlist and Injection Risk

## Definition

MCP allowlist and injection risk is the concept that every Model Context Protocol server candidate available to Claude Code must clear an explicit allow/reject/defer decision and a prompt-injection risk review before it is treated as trusted infrastructure. Because MCP connects Claude Code to external tools, databases, APIs, and event channels, content returned through an MCP server is external content and can carry adversarial instructions; Claude Code's own documentation flags this as a trust concern rather than a theoretical one.

## Operating Rules

```yaml
rules:
  - "Treat every proposed MCP server as requiring an allowlist decision (allow, reject, or defer) before it is used or committed."
  - "Apply injection-risk review to any MCP server candidate that can read external content, write state, or expose privileged context."
  - "Do not treat a concept page or design discussion of an MCP server as equivalent to an operator trust decision; only an explicit decision record counts."
  - "Do not promote MCP tool output to KB doctrine without source and risk handling, per the KB's soft-guidance-vs-hard-enforcement distinction."
  - "No concrete allowlist schema, injection-risk checklist, or runtime enforcement mechanism is produced during Phase 2 KB compile (S6); MCP policy is explicitly deferred per operator decision Q005."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    rationale: "B02-C013 is the primary-docs-grounded claim establishing MCP's trust and injection-risk requirement, directly underpinning this page."
    coverage: "MCP purpose, use cases, trust/prompt-injection warning, and output/timeout limits."
  - source_id: "operator-phase1-review-decisions-20260702"
    rationale: "Operator decision Q005 explicitly defers MCP policy and committed .mcp.json rules, and phase2_implications names the MCP allowlist as an open boundary — the direct compile-policy basis for treating this as unresolved rather than doctrine."
    coverage: "Q005_mcp_policy decision and phase2_implications.write_as_boundary_or_open_question list."
```

## Macro / Meso / Micro

### Macro

MCP is the mechanism by which Claude Code reaches outside its own context into external systems, and that reach is exactly why it needs a trust gate. Apex's KB treats "an MCP server exists and could be useful" as a separate question from "an MCP server is approved and safe to use," and refuses to collapse the two. This page names the risk surface (allowlist plus injection risk) that any future MCP policy must address, without prematurely deciding what that policy is.

### Meso

The underlying mechanism is that MCP servers can expose tools, resources, and prompts backed by arbitrary external content — files, API responses, database rows, web content — any of which could contain adversarial instructions designed to manipulate the agent (prompt injection). Claude Code's documentation calls this out explicitly as a reason MCP servers require trust approval rather than silent connection. Apex extends this into a two-part gate: (1) an allowlist decision per server (should this server be usable at all, and in what scope), and (2) an injection-risk assessment per server (what external content does it expose, and how is that content handled once read). Operator decision Q005 defers building the actual policy and committed `.mcp.json` rules, meaning this page documents the risk shape, not a finished procedure.

### Micro

B02-C013 states MCP connects Claude Code to external tools, databases, APIs, and event channels, but requires explicit trust evaluation because external content can expose prompt-injection risk (`phase1-batch02-claude-code-orchestration-surface.md` claim B02-C013). The operator's phase2_implications section lists "MCP server allowlist and committed .mcp.json policy" under `write_as_boundary_or_open_question`, meaning it should not be written as settled doctrine in Phase 2 (`operator-phase1-review-decisions-20260702.md` phase2_implications). Contradiction B02-T002 captures the deeper tension: Apex wants repo-native, shareable orchestration surfaces, while Claude Code warns that untrusted projects should not silently inject instructions or tool surfaces (`phase1-batch02-claude-code-orchestration-surface.md` B02-T002).

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "MCP connects Claude Code to external tools, databases, APIs, and event channels, but requires explicit trust evaluation because external content can expose prompt-injection risk."
    source_pointer: "phase1-batch02-claude-code-orchestration-surface.md claim B02-C013"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "Apex defers MCP policy and committed .mcp.json rules; the MCP server allowlist remains a boundary/open question rather than Phase 2 doctrine."
    source_pointer: "operator-phase1-review-decisions-20260702.md Q005_mcp_policy and phase2_implications.write_as_boundary_or_open_question"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "Project-level MCP configuration is trust-sensitive: Apex wants repo-native orchestration, but untrusted projects should not silently inject instructions or tool surfaces through shared MCP config."
    source_pointer: "phase1-batch02-claude-code-orchestration-surface.md contradiction B02-T002"
    confidence: "medium"
    claim_label: "source_backed_summary"
```

## Routes Here

```yaml
routes:
  - question: "Is this MCP server safe to add, and what risk does it carry?"
    leads_to: "claude-code-orchestration-design/concepts/mcp-allowlist-and-injection-risk.md"
    rationale: "This page is the direct entry point for the allowlist/injection-risk question on any specific MCP server candidate."
  - related_page: "claude-code-orchestration-design/concepts/mcp-config-boundary.md"
    relation: "Companion concept describing where MCP configuration may live and why it is not generated during Phase 2 compile."
  - related_page: "claude-code-orchestration-design/concepts/mcp-decision-model.md"
    relation: "Broader decision model for whether MCP is the right mechanism at all, of which allowlist/injection-risk is one gating step."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_pointer: "B02-C013, B02-T002"
    supports: "MCP trust/injection-risk requirement and the repo-native-vs-trust-safety tension."
  - source_id: "operator-phase1-review-decisions-20260702"
    source_pointer: "Q005_mcp_policy, phase2_implications.write_as_boundary_or_open_question"
    supports: "MCP allowlist and .mcp.json policy explicitly deferred, not doctrine."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Open question: how should Apex distinguish MCP servers that are safe to commit in .mcp.json from user-local or operator-private MCP servers? No allowlist schema exists."
    source_pointer: "phase1-batch02-claude-code-orchestration-surface.md B02-Q004"
    proposed_handling: "planning_task_candidate"
  - id: U002
    description: "Contradiction: project-level skills/hooks/MCP configuration are shareable and useful but trust-sensitive; Apex wants repo-native orchestration while Claude Code warns against silent instruction/tool injection from untrusted projects."
    source_pointer: "phase1-batch02-claude-code-orchestration-surface.md B02-T002"
    proposed_handling: "audit_item"
  - id: U003
    description: "MCP policy is explicitly deferred (Q005: mcp_later); no concrete allowlist schema or injection-risk checklist has been produced yet."
    source_pointer: "operator-phase1-review-decisions-20260702.md Q005_mcp_policy"
    proposed_handling: "revisit_source"
```
