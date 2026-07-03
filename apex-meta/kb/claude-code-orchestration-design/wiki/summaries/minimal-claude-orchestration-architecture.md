---
title: "Minimal Claude Orchestration Architecture"
page_type: summary
kb_slug: "claude-code-orchestration-design"
summary_slug: "minimal-claude-orchestration-architecture"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 38-137; corrected compile objective and specialized indexes"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-completion-report"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-completion-report.md"
    source_hash: "f604b3e31858da764eb2807084ca8282a1e4acc2"
    source_pointer: "lines 104-138; major concepts found"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch02-claude-code-orchestration-surface.md"
    source_hash: "505c6297d2c7198cbf0e77800577ab8e18a25d73"
    source_pointer: "claims B02-C001 through B02-C016"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Minimal Claude Orchestration Architecture

```yaml
summary_id: minimal_claude_orchestration_architecture
specialized_indexes:
  - agent_orchestration_index
  - claude_mechanism_mapping_index
  - token_economy_and_information_design_index
pattern: >
  A resilient Claude/Apex orchestration system should be a small layered control
  plane, not a swarm. Use always-loaded guidance for stable norms, skills for
  repeatable procedures, workflows for multi-stage processes, subagents for
  context-isolated work, scripts/hooks for deterministic enforcement, and plugins
  or MCP only when distribution or external connectivity is justified.
used_when:
  - "Designing a reusable Claude Code / Apex operating model."
  - "Choosing the smallest mechanism that can carry a task safely."
  - "Preventing one all-purpose agent or CLAUDE.md file from becoming the whole system."
not_used_when:
  - "A runtime hook, plugin, workflow, MCP server, scheduler, or production agent file must be written."
  - "The next step is deterministic postflight or retrieval indexing."
reads:
  - "Phase 1 batch analyses"
  - "operator Phase 1 decisions"
  - "specialized-index compile plan"
writes:
  - "compiled summary and concept pages only"
  - "no runtime configuration"
token_efficiency:
  - "Use index-first navigation and small compiled pages before raw sources."
  - "Keep activation surfaces thin; place deeper contracts in referenced pages."
drift_controls:
  - "Separate source-backed doctrine from deferred implementation questions."
  - "Use source_refs, confidence, claim_label, and status on every page."
open_questions:
  - "Exact persistent agent roster remains deferred."
  - "Plugin and MCP packaging remain deferred."
```

The central compiled pattern is a mechanism ladder. Plain Markdown/YAML artifacts come first. Skills, workflows, subagents, persistent agents, deterministic scripts/hooks, plugins, and MCP are added only when the previous mechanism cannot safely carry the work.
