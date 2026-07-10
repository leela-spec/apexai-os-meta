---
title: "Claude Mechanism Decision Model"
page_type: summary
kb_slug: "claude-code-orchestration-design"
summary_slug: "claude-mechanism-decision-model"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 112-123; claude_mechanism_mapping_index questions"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch02-claude-code-orchestration-surface.md"
    source_hash: "505c6297d2c7198cbf0e77800577ab8e18a25d73"
    source_pointer: "claims B02-C001 through B02-C016; concepts extracted"
    source_storage_mode: "pointer_only"
  - source_id: "operator-phase1-review-decisions-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md"
    source_hash: "34d9c16967d2f7f49b716d75c8bb1a2a10eb96a7"
    source_pointer: "lines 46-122; operator decisions"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "claude-code-orchestration-design/concepts/deterministic-script-boundary.md"
related_entities:
  - "claude-code-orchestration-design/entities/claude-code-skills.md"
  - "claude-code-orchestration-design/entities/claude-code-subagents.md"
review_flags: []
---

# Claude Mechanism Decision Model

## Core Summary

The compile plan's `claude_mechanism_mapping_index` asks when Claude Code should use plain artifacts, skills, workflows, ephemeral subagents, persistent agents, scripts/hooks, or plugins/MCP, and which rules are soft guidance versus hard enforcement (compile plan lines 112-123). Phase 1 batch 02 answers most of this directly: Claude Code's control plane is layered — `CLAUDE.md` and rules for always-on/path-scoped guidance, skills for repeatable procedures, hooks/settings for enforcement, subagents for context isolation, MCP for external tool surfaces, and plugins for distributable bundles (B02-C014). Guidance and enforcement are explicitly distinct: `CLAUDE.md` and rules are guidance the model reads, while settings, permissions, and hooks are the enforced layer (B02-C010, B02-C011, B02-T001). The operator's Phase 1 review converted several of these mapping questions into concrete policy: hard-enforce only a short list of high-risk gates via hooks/scripts (Q002), use project skills now and defer plugins (Q003), keep persistent subagents small and validated while ephemeral subagents handle one-off exploration (Q004), and defer MCP policy entirely (Q005).

## What This Adds

```yaml
adds:
  - "A single ordered mechanism ladder (artifact -> skill -> workflow -> ephemeral subagent -> persistent agent -> deterministic script/hook -> plugin/MCP) derived from B02-C014 and the compile plan's mapping index."
  - "An explicit soft-guidance-vs-hard-enforcement boundary (B02-T001) that disqualifies CLAUDE.md/rules/skill-prose as a substitute for hooks on high-risk gates."
  - "Operator-approved scope for what is currently hard-enforced (Q002 hard_enforce list) versus what remains soft-enforced style/terminology guidance."
clarifies:
  - "Plugins and MCP are not earlier-stage defaults; both are explicitly deferred by operator decision (Q003, Q005), which the mechanism ladder places at the outer edge for the same reason."
  - "Persistent subagents are not banned, but are reserved for repeated domain roles, stable validation/audit roles, or security-sensitive repo executors with explicit constraints (Q004); ephemeral subagents remain the default for one-off exploration."
limits:
  - "This model does not itself decide the final Apex agent roster, plugin packaging, or MCP allowlist — those remain explicit Phase 2 non-goals (compile plan section 7)."
  - "The mapping is a decision doctrine, not a runtime implementation; no hooks, workflows, MCP config, plugins, or agent files exist because of this page."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    rationale: "Primary source for the layered control-plane claim (B02-C014) and the soft-guidance-vs-hard-enforcement distinction (B02-T001) that anchor the mechanism ladder."
    coverage: "B02-C001 through B02-C016; concepts_extracted claude-code-control-plane, soft-guidance-vs-hard-enforcement, skill-command-convergence, subagent-context-isolation, hook-enforcement-gate, plugin-bundled-orchestration, mcp-tool-connectivity-layer."
  - source_id: "operator-phase1-review-decisions-20260702"
    rationale: "Converts the abstract mapping index into concrete Phase 2 policy: which gates are hard-enforced, which packaging surface is current, and which mechanisms are deferred."
    coverage: "Q002 hook/script enforcement scope; Q003 packaging surface; Q004 subagent persistence; Q005 MCP policy deferral."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Defines the question set (claude_mechanism_mapping_index) that this page exists to answer, and the page-shape rule requiring what/when/when-not/reads/writes/token-cost/drift-prevention/source for every Phase 2 page."
    coverage: "lines 51-135 needed_specialized_indexes; lines 182-197 page_shape_rule."
```

## Macro / Meso / Micro

### Macro

Apex should select the least-powerful Claude Code mechanism that still preserves source custody, safety, auditability, and token economy for a given task (compile-plan-derived pattern). The mechanism ladder runs: plain markdown/YAML artifact, skill, workflow, ephemeral subagent, persistent agent, deterministic script, hook, then plugin or MCP. Each step up the ladder trades token efficiency and simplicity for more isolation, enforcement power, or distribution reach — and each step is only justified when the previous step demonstrably cannot carry the work safely.

### Meso

The ladder is grounded in two separate findings. First, Claude Code's own documentation frames its control plane as layered by design: guidance files versus enforcement mechanisms versus isolation mechanisms versus distribution mechanisms (B02-C014). Second, the operator's Phase 1 review turned each rung's threshold into policy rather than leaving it abstract: hooks are reserved for a named short list of high-risk gates (phase2_without_approve_ingest, write_outside_kb_root, raw_source_delete_or_mutation, kb_schema_overwrite_without_explicit_flag, destructive_archive_delete — Q002), while style/terminology/ordering conventions remain soft-enforced. Packaging (plugins) and external connectivity (MCP) are both explicitly deferred (Q003, Q005) rather than adopted early, which keeps the ladder's outer rungs unused until the inner rungs prove insufficient.

### Micro

Source pointers: compile plan lines 110-123 (claude_mechanism_mapping_index core questions); B02-C014 (layered control-plane interpretation); B02-T001 (guidance vs enforcement contradiction); operator-phase1-review-decisions-20260702.md lines 52-65 (Q002 hard/soft enforcement lists), lines 67-72 (Q003), lines 74-84 (Q004), lines 86-89 (Q005).

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Claude Code orchestration should be modeled as a layered control plane: CLAUDE.md and rules for always-on/path-scoped guidance; skills for repeatable procedures; hooks/settings for enforcement; subagents for context isolation; MCP for external tool surfaces; plugins for distributable bundles."
    source_pointer: "B02-C014"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages:
      - "claude-code-orchestration-design/summaries/minimal-claude-orchestration-architecture.md"
  - claim_id: C002
    claim: "Guidance and enforcement are distinct surfaces; any Apex design that encodes hard gates only in skill prose or CLAUDE.md is weaker than one backed by hooks or deterministic scripts."
    source_pointer: "B02-T001"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages:
      - "claude-code-orchestration-design/concepts/deterministic-script-boundary.md"
  - claim_id: C003
    claim: "The operator's Phase 1 review approved hard-enforcing only a named short list of high-risk gates via hooks/scripts, leaving style/terminology/ordering conventions as soft-enforced."
    source_pointer: "operator-phase1-review-decisions-20260702.md lines 52-65 (Q002)"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages: []
```

## Routes Here

```yaml
routes:
  - question: "Should this capability be a skill, a subagent, a hook, or a plugin?"
    leads_to: "claude-code-orchestration-design/entities/claude-code-skills.md"
    rationale: "The mechanism ladder starts with skills as the default repeatable-procedure mechanism."
  - related_page: "claude-code-orchestration-design/summaries/minimal-claude-orchestration-architecture.md"
    relation: "That summary applies this same mechanism ladder to the question of an overall minimal orchestration architecture."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Which Apex gates require hook-level enforcement rather than skill-prose instruction only, beyond the named Q002 list? (B02-Q001)"
    source_pointer: "B02-Q001"
    proposed_handling: "planning_task_candidate"
  - id: U002
    description: "Should Apex package reusable orchestration surfaces as plain repo skills, plugins, or both? (B02-Q002)"
    source_pointer: "B02-Q002"
    proposed_handling: "planning_task_candidate"
  - id: U003
    description: "Which Apex subagent definitions should be persistent project files, and which should remain ephemeral CLI/session definitions? (B02-Q003)"
    source_pointer: "B02-Q003"
    proposed_handling: "planning_task_candidate"
  - id: U004
    description: "Plugin packaging timing and full subagent roster remain explicit boundary/open items per operator Phase 2 implications, not settled doctrine."
    source_pointer: "operator-phase1-review-decisions-20260702.md lines 132-137"
    proposed_handling: "leave_as_gap"
```

The decision model is a boundary map. It does not create hooks, workflows, MCP configuration, plugins, or agent files in this KB compile step.
