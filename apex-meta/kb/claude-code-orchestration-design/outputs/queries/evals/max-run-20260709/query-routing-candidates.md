# Query Routing Candidates — Max Run 20260709

```yaml
kb_slug: claude-code-orchestration-design
run_id: max-run-20260709
status: new_parallel_compile
source_policy: source_preserving
legacy_output_policy: old_pages_for_comparison_only
```

## Routing Candidates

```yaml
query_routes:
  - query: "When should Claude Code use skills, hooks, plugins, subagents, or MCP?"
    primary_route: apex-meta/kb/claude-code-orchestration-design/wiki/summaries/max-run-20260709/claude-code-mechanism-decision-model.md
    supporting_routes:
      - apex-meta/kb/claude-code-orchestration-design/wiki/summaries/max-run-20260709/skill-hook-plugin-mcp-boundaries.md
      - apex-meta/kb/claude-code-orchestration-design/wiki/concepts/max-run-20260709/skill-boundary.md
      - apex-meta/kb/claude-code-orchestration-design/wiki/concepts/max-run-20260709/hook-vs-skill-instruction.md
      - apex-meta/kb/claude-code-orchestration-design/wiki/concepts/max-run-20260709/mcp-allowlist-and-injection-risk.md
      - apex-meta/kb/claude-code-orchestration-design/wiki/concepts/max-run-20260709/persistent-agent-vs-ephemeral-subagent.md

  - query: "What is the safest minimal Claude orchestration architecture?"
    primary_route: apex-meta/kb/claude-code-orchestration-design/wiki/summaries/max-run-20260709/minimal-claude-orchestration-architecture.md
    supporting_routes:
      - apex-meta/kb/claude-code-orchestration-design/wiki/summaries/max-run-20260709/deterministic-vs-llm-execution-model.md
      - apex-meta/kb/claude-code-orchestration-design/wiki/summaries/max-run-20260709/production-agent-readiness-and-risk-model.md

  - query: "When should Agent/Codex be used versus current assistant LLM?"
    primary_route: apex-meta/kb/claude-code-orchestration-design/wiki/summaries/max-run-20260709/deterministic-vs-llm-execution-model.md
    supporting_routes:
      - apex-meta/kb/claude-code-orchestration-design/wiki/concepts/max-run-20260709/deterministic-executor-only-boundary.md
      - apex-meta/kb/claude-code-orchestration-design/wiki/concepts/max-run-20260709/current-assistant-semantic-owner.md

  - query: "What are the risks of MCP and plugin surfaces?"
    primary_route: apex-meta/kb/claude-code-orchestration-design/wiki/concepts/max-run-20260709/mcp-allowlist-and-injection-risk.md
    supporting_routes:
      - apex-meta/kb/claude-code-orchestration-design/wiki/entities/max-run-20260709/mcp.md
      - apex-meta/kb/claude-code-orchestration-design/wiki/entities/max-run-20260709/claude-code-plugins.md

  - query: "How should source-preserving agent memory be structured?"
    primary_route: apex-meta/kb/claude-code-orchestration-design/wiki/summaries/max-run-20260709/apex-kb-as-source-preserving-agent-memory.md
    supporting_routes:
      - apex-meta/kb/claude-code-orchestration-design/wiki/concepts/max-run-20260709/source-preserving-kb-compile.md
      - apex-meta/kb/claude-code-orchestration-design/wiki/entities/max-run-20260709/apex-kb.md

  - query: "How should old wiki outputs be compared to new max-run outputs?"
    primary_route: apex-meta/kb/claude-code-orchestration-design/wiki/concepts/max-run-20260709/old-output-comparison-policy.md
    supporting_routes:
      - apex-meta/kb/claude-code-orchestration-design/wiki/summaries/max-run-20260709/failure-analysis-and-feedback-loop.md
```

## Raw Source Reopen Rules

```yaml
raw_source_needed_when:
  - runtime files will be written
  - current product availability or version-specific behavior is asked
  - source-payload-manifest freshness is being asserted
  - old output will be deleted, moved, or promoted
  - MCP, plugin, hook, or subagent config will be installed or executed
```
