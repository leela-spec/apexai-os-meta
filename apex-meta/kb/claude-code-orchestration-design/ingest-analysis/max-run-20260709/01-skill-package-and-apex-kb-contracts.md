# Phase 1 Analysis — Skill Package and Apex KB Contracts

## Run Metadata

```yaml
kb_slug: claude-code-orchestration-design
run_id: max-run-20260709
phase: ingest_phase_1_analysis
batch: 01-skill-package-and-apex-kb-contracts
status: new_parallel_compile_updated
created_at: 2026-07-10T00:00:00Z
source_policy: source_preserving
legacy_output_policy: old_pages_for_comparison_only
baseline_warning: source-payload-manifest exists but is empty in GitHub main connector read
```

## Source Scope

This batch covers the Apex KB skill package, source/page contracts, ingest/query/lint/retrieval rules, wiki page templates, runbook policy, and official Claude Code skill mechanics. It treats raw sources and package contracts as authority, deterministic artifacts as routing evidence, and old Phase 1/wiki pages as comparison material only.

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
  - apex-meta/kb/claude-code-orchestration-design/manifests/source-manifest.json
  - apex-meta/kb/claude-code-orchestration-design/manifests/source-payload-manifest.json
  - apex-meta/kb/claude-code-orchestration-design/manifests/phase0/corpus-profile.md
  - apex-meta/kb/claude-code-orchestration-design/manifests/phase0/source-priority-candidates.md
  - apex-meta/kb/claude-code-orchestration-design/manifests/phase0/process-flow-graph-summary.md
  - apex-meta/kb/claude-code-orchestration-design/outputs/queries/evals/query-eval-pack.json
  - apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-skills.md.md
  - apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/notes/SubskillsVsAgents_CC.md
  - apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-completion-report.md
  - apex-meta/kb/claude-code-orchestration-design/wiki/index.md
```

## Source-Grounded Claims

```yaml
claims:
  - id: P1-SKILL-001
    claim: "Apex KB separates deterministic script ownership from LLM semantic ownership."
    source: .claude/skills/apex-kb/SKILL.md
    confidence: high
    claim_label: source_backed_summary
  - id: P1-SKILL-002
    claim: "The execution surface policy keeps the current assistant/chat LLM as default semantic owner and reserves Agent Mode or Codex for deterministic execution, validation, Git-native patching, and commit/push surfaces unless the operator explicitly overrides semantic delegation."
    source: .claude/skills/apex-kb/SKILL.md
    confidence: high
    claim_label: source_backed_summary
  - id: P1-SKILL-003
    claim: "Compiled Phase 2 pages must include Adaptive Ranked Source Set, Macro / Meso / Micro, Key Claims, Routes Here, and Uncertainty / Raw Source Reopen Triggers."
    source: .claude/skills/apex-kb/references/kb-contract.md
    confidence: high
    claim_label: source_backed_summary
  - id: P1-SKILL-004
    claim: "The source-payload manifest path exists but connector-read content is empty, so payload custody freshness is not proven for this run."
    source: apex-meta/kb/claude-code-orchestration-design/manifests/source-payload-manifest.json
    confidence: high
    claim_label: source_backed_summary
  - id: P1-SKILL-005
    claim: "Phase 0 scanned 1,732 files and supports clustered routing rather than all-file semantic reading."
    source: apex-meta/kb/claude-code-orchestration-design/manifests/phase0/corpus-profile.md
    confidence: high
    claim_label: source_backed_summary
  - id: P1-SKILL-006
    claim: "Claude Code skills are SKILL.md packages whose description drives invocation; supporting files provide progressive disclosure."
    source: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-skills.md.md
    confidence: high
    claim_label: source_backed_summary
  - id: P1-SKILL-007
    claim: "Subskill is not a safe canonical architecture term in the reviewed sources; sibling skills and companion files are safer."
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
  - old-output-comparison-policy
  - skill-boundary
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
    tension: "The operator reports the deterministic baseline as pushed; connector reads confirm graph summary and query-eval pack are present, but the source-payload manifest content is empty."
    sources:
      - apex-meta/kb/claude-code-orchestration-design/manifests/source-payload-manifest.json
      - apex-meta/kb/claude-code-orchestration-design/manifests/phase0/process-flow-graph-summary.md
      - apex-meta/kb/claude-code-orchestration-design/outputs/queries/evals/query-eval-pack.json
    handling: "Proceed with explicit warning; require terminal postflight to repair or verify payload custody."
  - id: T-SKILL-002
    tension: "Legacy Phase 1 used a separate operator gate while current v3 semantic compile policy allows continuous Phase 1 to Phase 2 when selected output tier includes wiki output."
    sources:
      - apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-completion-report.md
      - .claude/skills/apex-kb/SKILL.md
    handling: "Use current max-run compile policy; treat old gate as historical."
```

## Open Questions

```yaml
open_questions:
  - id: O-SKILL-001
    question: "Why did the committed source-payload-manifest path contain empty content after the deterministic rerun commit?"
    source: apex-meta/kb/claude-code-orchestration-design/manifests/source-payload-manifest.json
  - id: O-SKILL-002
    question: "Should strict Agent Skills open-standard requirements or Claude Code pragmatic SKILL.md behavior be primary when they diverge?"
    source: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/notes/SubskillsVsAgents_CC.md
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
  - id: G-SKILL-001
    trigger: "Reopen deterministic source custody if source-payload-manifest remains empty after terminal postflight."
    source: apex-meta/kb/claude-code-orchestration-design/manifests/source-payload-manifest.json
  - id: G-SKILL-002
    trigger: "Reopen old-output comparison after max-run pages are indexed and linted."
    source: apex-meta/kb/claude-code-orchestration-design/wiki/index.md
```
