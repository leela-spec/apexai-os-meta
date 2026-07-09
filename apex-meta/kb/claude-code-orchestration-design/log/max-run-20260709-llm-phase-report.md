# Max Run 20260709 LLM Phase Report

## Run Summary

```yaml
kb_slug: claude-code-orchestration-design
run_id: max-run-20260709
mode: apex_kb_llm_phase_only
status: completed_with_terminal_postflight_required
repo: leela-spec/apexai-os-meta
branch: main
old_outputs_overwritten: false
baseline_warning: source-payload-manifest exists but connector-read content is empty
```

The LLM-owned Phase 1 analysis, Phase 2 focused wiki compile, and query-routing seed artifacts were written as new parallel outputs under `max-run-20260709` folders. Legacy root-level wiki pages and old ingest-analysis files were not overwritten.

## Files Created

```yaml
phase1:
  - ingest-analysis/max-run-20260709/01-skill-package-and-apex-kb-contracts.md
  - ingest-analysis/max-run-20260709/02-claude-code-mechanisms-and-surfaces.md
  - ingest-analysis/max-run-20260709/03-orchestration-workflows-and-agent-boundaries.md
  - ingest-analysis/max-run-20260709/04-subscription-seat-terminal-and-machine-models.md
  - ingest-analysis/max-run-20260709/05-failure-analysis-and-operator-feedback.md
  - ingest-analysis/max-run-20260709/06-deterministic-vs-llm-execution-model.md
  - ingest-analysis/max-run-20260709/phase1-completion-report.md
phase2_summaries:
  - wiki/summaries/max-run-20260709/minimal-claude-orchestration-architecture.md
  - wiki/summaries/max-run-20260709/claude-code-mechanism-decision-model.md
  - wiki/summaries/max-run-20260709/skill-hook-plugin-mcp-boundaries.md
  - wiki/summaries/max-run-20260709/deterministic-vs-llm-execution-model.md
  - wiki/summaries/max-run-20260709/subscription-seat-terminal-machine-model.md
  - wiki/summaries/max-run-20260709/failure-analysis-and-feedback-loop.md
  - wiki/summaries/max-run-20260709/apex-kb-as-source-preserving-agent-memory.md
  - wiki/summaries/max-run-20260709/production-agent-readiness-and-risk-model.md
phase2_concepts:
  - wiki/concepts/max-run-20260709/deterministic-executor-only-boundary.md
  - wiki/concepts/max-run-20260709/current-assistant-semantic-owner.md
  - wiki/concepts/max-run-20260709/skill-boundary.md
  - wiki/concepts/max-run-20260709/hook-vs-skill-instruction.md
  - wiki/concepts/max-run-20260709/mcp-allowlist-and-injection-risk.md
  - wiki/concepts/max-run-20260709/persistent-agent-vs-ephemeral-subagent.md
  - wiki/concepts/max-run-20260709/low-token-handoff-design.md
  - wiki/concepts/max-run-20260709/source-preserving-kb-compile.md
  - wiki/concepts/max-run-20260709/old-output-comparison-policy.md
  - wiki/concepts/max-run-20260709/phase2-value-contract.md
phase2_entities:
  - wiki/entities/max-run-20260709/claude-code.md
  - wiki/entities/max-run-20260709/claude-code-skills.md
  - wiki/entities/max-run-20260709/claude-code-hooks.md
  - wiki/entities/max-run-20260709/claude-code-plugins.md
  - wiki/entities/max-run-20260709/claude-code-subagents.md
  - wiki/entities/max-run-20260709/mcp.md
  - wiki/entities/max-run-20260709/apex-kb.md
query_eval:
  - outputs/queries/evals/max-run-20260709/query-routing-candidates.md
  - outputs/queries/evals/max-run-20260709/query-eval-seed.json
log:
  - log/max-run-20260709-write-probe.md
  - log/max-run-20260709-llm-phase-report.md
```

## Sources Read

```yaml
sources_read:
  - .claude/skills/apex-kb/SKILL.md
  - .claude/skills/apex-kb/references/kb-contract.md
  - .claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md
  - .claude/skills/apex-kb/references/retrieval-contract.md
  - .claude/skills/apex-kb/templates/ingest-analysis-template.md
  - .claude/skills/apex-kb/templates/wiki-page-templates.md
  - .claude/skills/apex-kb/examples/lifecycle-runbook.md
  - manifests/source-manifest.json
  - manifests/source-payload-manifest.json
  - manifests/phase0/phase0-navigation-report.md
  - manifests/phase0/corpus-profile.md
  - manifests/phase0/topic-file-map.json
  - manifests/phase0/source-priority-candidates.md
  - manifests/phase0/process-flow-graph-summary.md
  - outputs/queries/evals/query-eval-pack.json
  - ingest-analysis/phase1-completion-report.md
  - wiki/index.md
  - selected raw Claude Code skill, hook, plugin, MCP, subagent, .claude directory, and operator-research files
```

## Claims / Concepts / Entities Produced

```yaml
core_claims:
  - current_assistant_chat_llm_is_default_semantic_execution_surface
  - external_agent_or_codex_is_deterministic_executor_only_by_default
  - phase2_pages_require_improved_value_contract_sections
  - old_outputs_are_comparison_material_only
  - source_payload_manifest_is_empty_in_connector_read_and_requires_postflight
concepts:
  - deterministic-executor-only-boundary
  - current-assistant-semantic-owner
  - skill-boundary
  - hook-vs-skill-instruction
  - mcp-allowlist-and-injection-risk
  - persistent-agent-vs-ephemeral-subagent
  - low-token-handoff-design
  - source-preserving-kb-compile
  - old-output-comparison-policy
  - phase2-value-contract
entities:
  - claude-code
  - claude-code-skills
  - claude-code-hooks
  - claude-code-plugins
  - claude-code-subagents
  - mcp
  - apex-kb
```

## Old Output Comparison Notes

```yaml
old_outputs:
  overwritten: false
  treatment: comparison_only
  notes:
    - "Legacy wiki/index.md lists 73 compiled pages and remains untouched."
    - "New pages live under max-run-20260709 subfolders."
    - "Old pages may be compared and promoted later only by explicit operator decision."
```

## Remaining Deterministic Postflight Needed

```yaml
needs_terminal_postflight: true
postflight_reasons:
  - source-payload-manifest content was empty in connector read
  - wiki index has not been rebuilt after max-run page creation
  - retrieval index has not been rebuilt after max-run page creation
  - status and lint have not been rerun after max-run page creation
```

## Operator Follow-Up Questions

```yaml
operator_follow_up_questions:
  - "Should the empty source-payload-manifest be regenerated and committed before comparing old and new wiki outputs?"
  - "After deterministic postflight, which max-run pages should be promoted into the non-versioned wiki folders?"
  - "Should max-run query-eval seed replace or extend the root query-eval-pack.json after validation?"
```
