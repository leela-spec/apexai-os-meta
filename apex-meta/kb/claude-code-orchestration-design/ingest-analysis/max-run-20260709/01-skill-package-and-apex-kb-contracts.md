# Phase 1 Analysis — Skill Package and Apex KB Contracts

## Run Metadata

```yaml
kb_slug: claude-code-orchestration-design
run_id: max-run-20260709
phase: ingest_phase_1_analysis
batch: 01-skill-package-and-apex-kb-contracts
status: new_parallel_compile
created_at: 2026-07-09T00:00:00Z
source_policy: source_preserving
legacy_output_policy: old_pages_for_comparison_only
```

## Source Scope

This batch covers the Apex KB skill package, its data/page contracts, ingest/query/lint/retrieval rules, and official Claude Code skill package mechanics. It does not treat legacy wiki pages as authority.

## Source Files Read

```yaml
sources_read:
  - .claude/skills/apex-kb/SKILL.md
  - .claude/skills/apex-kb/references/kb-contract.md
  - .claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md
  - .claude/skills/apex-kb/references/retrieval-contract.md
  - .claude/skills/apex-kb/templates/ingest-analysis-template.md
  - .claude/skills/apex-kb/templates/wiki-page-templates.md
  - .claude/skills/apex-kb/examples/lifecycle-runbook.md
  - apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-skills.md.md
  - apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/notes/SubskillsVsAgents_CC.md
  - apex-meta/kb/claude-code-orchestration-design/manifests/source-manifest.json
  - apex-meta/kb/claude-code-orchestration-design/manifests/phase0/corpus-profile.md
  - apex-meta/kb/claude-code-orchestration-design/manifests/phase0/source-priority-candidates.md
  - apex-meta/kb/claude-code-orchestration-design/log/max-update-run-gate-20260709.md
```

## Source-Grounded Claims

```yaml
claims:
  - id: P1-SKILL-001
    claim: "Apex KB owns semantic Phase 1 analysis and Phase 2 wiki drafting, while deterministic scripts own scaffold, hashing, Phase 0 maps, indexes, lint, status, and retrieval artifacts."
    source: .claude/skills/apex-kb/SKILL.md
    confidence: high
    claim_label: source_backed_summary
  - id: P1-SKILL-002
    claim: "The execution surface policy preserves current assistant/chat LLM as the default semantic owner and reserves Agent Mode or Codex for deterministic execution, validation, Git-native patching, and commit/push surfaces unless the operator overrides it."
    source: .claude/skills/apex-kb/SKILL.md
    confidence: high
    claim_label: source_backed_summary
  - id: P1-SKILL-003
    claim: "Compiled Phase 2 pages must include Adaptive Ranked Source Set, Macro / Meso / Micro, Key Claims, Routes Here, and Uncertainty / Raw Source Reopen Triggers."
    source: .claude/skills/apex-kb/references/kb-contract.md
    confidence: high
    claim_label: source_backed_summary
  - id: P1-SKILL-004
    claim: "Claude Code skills are directory-based SKILL.md packages whose description drives invocation; supporting files enable progressive disclosure rather than loading every reference by default."
    source: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-skills.md.md
    confidence: high
    claim_label: source_backed_summary
  - id: P1-SKILL-005
    claim: "The term subskill is not supported as an official skill architecture; sibling skills, companion files, references, scripts, assets, and templates are the safer vocabulary."
    source: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/notes/SubskillsVsAgents_CC.md
    confidence: medium
    claim_label: source_backed_summary
```

## Extracted Concepts

```yaml
concepts:
  - source-preserving-kb-compile
  - phase2-value-contract
  - current-assistant-semantic-owner
  - skill-boundary
  - old-output-comparison-policy
  - source-custody-before-semantics
  - progressive-disclosure-resource
```

## Extracted Entities

```yaml
entities:
  - apex-kb
  - claude-code-skills
  - agent-skills-standard
```

## Contradictions / Tensions

```yaml
tensions:
  - id: T-SKILL-001
    tension: "The user prompt states the improved deterministic baseline is complete, but committed main still lacks the required source-payload manifest, query-eval pack, and process graph artifacts in connector reads."
    sources:
      - apex-meta/kb/claude-code-orchestration-design/log/max-update-run-gate-20260709.md
      - apex-meta/kb/claude-code-orchestration-design/manifests/source-payload-manifest.json
    handling: "Expose as a source gap; do not infer missing artifact content."
  - id: T-SKILL-002
    tension: "Legacy Phase 1 used a separate operator gate while current v3 semantic compile policy allows continuous Phase 1 to Phase 2 when selected output tier includes wiki output."
    sources:
      - apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-completion-report.md
      - .claude/skills/apex-kb/SKILL.md
    handling: "Preserve current v3 policy for max-run outputs; treat old gate as historical."
```

## Open Questions

```yaml
open_questions:
  - id: O-SKILL-001
    question: "Was the deterministic baseline rerun committed after max-update-run-gate-20260709, or did it remain local/unpushed?"
    source: apex-meta/kb/claude-code-orchestration-design/log/max-update-run-gate-20260709.md
  - id: O-SKILL-002
    question: "Should strict Agent Skills open-standard requirements or Claude Code's pragmatic SKILL.md behavior be treated as primary when they diverge?"
    source: apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-completion-report.md
```

## Phase 2 Candidates

```yaml
phase2_candidates:
  summaries:
    - apex-kb-as-source-preserving-agent-memory.md
  concepts:
    - source-preserving-kb-compile.md
    - phase2-value-contract.md
    - current-assistant-semantic-owner.md
    - skill-boundary.md
    - old-output-comparison-policy.md
  entities:
    - apex-kb.md
    - claude-code-skills.md
```

## Source Gaps / Reopen Triggers

```yaml
source_gaps:
  - missing_committed_source_payload_manifest
  - missing_committed_query_eval_pack
  - missing_committed_process_flow_graph_summary
  - source-payload custody should be reopened before deterministic postflight claims are treated as fresh
```
