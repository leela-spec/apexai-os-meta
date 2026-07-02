# Phase 1 Batch 02 — Claude Code Orchestration Surface

```yaml
title: "Claude Code Orchestration Surface"
source_batch_id: "phase1-batch02-claude-code-orchestration-surface"
kb_slug: "claude-code-orchestration-design"
phase: "ingest_phase_1"
status: "operator_review_needed"
created_at: "2026-07-02T00:00:00Z"
claim_labels_allowed:
  - fact
  - interpretation
  - recommendation
  - open_question
  - contradiction
confidence_labels_allowed:
  - high
  - medium
  - low
operator_gate:
  phase_2_allowed: false
  required_confirmation_phrase: "approve ingest"
```

## 1. Source Scope

This batch analyzes Claude Code's native orchestration surface: skills, custom commands, hooks, subagents, plugins, MCP, settings, memory/rules, and `.claude/` layout. The purpose is to separate what each surface is for and how Apex should compose them without collapsing all orchestration behavior into one skill or one `CLAUDE.md`.

This is Phase 1 semantic ingest only. Phase 2 wiki synthesis is blocked pending operator approval with the exact phrase `approve ingest`.

## 2. Source Files Read

```yaml
source_files_read:
  - source_id: "claude-code-skills-docs"
    path: "raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-skills.md.md"
    source_type: "primary_docs"
    authority: "primary"
    pointers:
      - "lines 7-22: skills extend Claude Code and commands have merged into skills"
      - "lines 101-128: skill locations, precedence, nested skills, plugin conversion"
      - "lines 130-168: live change detection and parent/nested discovery"
      - "lines 170-210: content types and concision"
      - "continuation lines 3-36: frontmatter fields and runtime controls"
      - "continuation lines 37-68: command-name derivation and substitutions"
      - "continuation lines 87-154: supporting files, invocation control, lifecycle after activation"
  - source_id: "claude-code-hooks-reference"
    path: "raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-hooks.md.md"
    source_type: "primary_docs"
    authority: "primary"
    pointers:
      - "lines 7-19: hooks definition and lifecycle"
      - "lines 29-60: hook event table"
      - "lines 62-150: PreToolUse blocking example"
      - "lines 152-180: hook configuration and hook locations"
      - "lines 181-205: matcher semantics"
  - source_id: "claude-code-subagents-docs"
    path: "raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-sub-agents.md.md"
    source_type: "primary_docs"
    authority: "primary"
    pointers:
      - "lines 7-14: subagents definition and isolated context"
      - "lines 19-29: benefits and delegation descriptions"
      - "lines 31-86: built-in subagent types and restrictions"
      - "lines 88-148: custom subagent quickstart"
      - "lines 150-190: scope, discovery, uniqueness, plugin/CLI definitions"
      - "lines 230-234: file-based frontmatter and plugin subagent caveat"
  - source_id: "claude-directory-docs"
    path: "raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-claude-directory.md.md"
    source_type: "primary_docs"
    authority: "primary"
    pointers:
      - "lines 7-10: .claude directory contents"
      - "lines 30-39: CLAUDE.md session loading and line-count guidance"
      - "lines 58-80: .mcp.json project-scoped MCP servers"
      - "lines 101-141: settings.json, permissions, and hooks"
      - "lines 163-214: rules folder and path-scoped guidance"
      - "lines 216-223: skills folder role"
  - source_id: "claude-code-plugins-reference"
    path: "raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-plugins-reference.md.md"
    source_type: "primary_docs"
    authority: "primary"
    pointers:
      - "lines 15-18: plugin definition and component list"
      - "lines 19-49: plugin skills"
      - "lines 51-83: plugin agents"
      - "lines 85-155: plugin hooks and hook types"
      - "lines 156-190: plugin MCP servers"
      - "lines 192-222: plugin LSP integration"
  - source_id: "claude-code-mcp-docs"
    path: "raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/secondary-code-claude-com-docs-en-mcp.md.md"
    source_type: "primary_docs_snapshot"
    authority: "primary"
    pointers:
      - "lines 7-15: MCP purpose"
      - "lines 17-27: MCP use cases"
      - "lines 32-36: trust and prompt injection warning"
      - "lines 60-146: server transports"
      - "lines 147-190: management, trust approval, reconnection"
      - "lines 196-218: channels, timeout limits, output limits"
  - source_id: "source-priority-candidates"
    path: "manifests/phase0/source-priority-candidates.md"
    source_type: "phase0_navigation"
    authority: "primary_navigation"
    pointers:
      - "lines 9-23: Phase 0 ranks hooks, skills, settings, plugins, MCP, and subagents among the highest-priority source candidates"
  - source_id: "phase0-navigation-report"
    path: "manifests/phase0/phase0-navigation-report.md"
    source_type: "phase0_navigation"
    authority: "primary_navigation"
    pointers:
      - "lines 20-24: deterministic boundary; no Phase 1/wiki/vector/Plan/Sync/Session writes"
```

## 3. Source-Grounded Claims

```yaml
claims:
  - id: "B02-C001"
    label: fact
    confidence: high
    claim: >
      Claude Code now treats custom commands and skills as the same underlying mechanism for new workflows; skills add supporting files, frontmatter controls, and automatic loading when relevant.
    source_pointers:
      - "primary-code-claude-com-docs-en-skills.md.md lines 11-22"
      - "primary-code-claude-com-docs-en-claude-directory.md.md lines 25-26"

  - id: "B02-C002"
    label: fact
    confidence: high
    claim: >
      Skills can live at enterprise, personal, project, nested project, or plugin levels; conflict resolution and command naming depend on location, not solely frontmatter.
    source_pointers:
      - "primary-code-claude-com-docs-en-skills.md.md lines 101-128"
      - "primary-code-claude-com-docs-en-skills.md.md continuation lines 37-51"

  - id: "B02-C003"
    label: fact
    confidence: high
    claim: >
      Skill content is optimized for progressive loading: descriptions are always visible, full content loads when invoked, and supporting files should remain separate and only load when needed.
    source_pointers:
      - "primary-code-claude-com-docs-en-skills.md.md lines 130-154"
      - "primary-code-claude-com-docs-en-skills.md.md continuation lines 87-109"
      - "primary-code-claude-com-docs-en-skills.md.md continuation lines 148-154"

  - id: "B02-C004"
    label: fact
    confidence: high
    claim: >
      Claude Code supports runtime frontmatter controls such as `disable-model-invocation`, `user-invocable`, `allowed-tools`, `disallowed-tools`, `model`, `effort`, `context: fork`, `agent`, `hooks`, `paths`, and `shell`.
    source_pointers:
      - "primary-code-claude-com-docs-en-skills.md.md continuation lines 18-36"

  - id: "B02-C005"
    label: fact
    confidence: high
    claim: >
      Hooks are lifecycle-bound event handlers that can run shell commands, HTTP endpoints, MCP tools, prompts, or agents at session, turn, tool-call, subagent, compaction, and file-change events.
    source_pointers:
      - "primary-code-claude-com-docs-en-hooks.md.md lines 7-19"
      - "primary-code-claude-com-docs-en-hooks.md.md lines 29-60"
      - "primary-code-claude-com-docs-en-plugins-reference.md.md lines 148-155"

  - id: "B02-C006"
    label: fact
    confidence: high
    claim: >
      A `PreToolUse` hook can enforce hard safety or policy decisions before a tool call executes; the example blocks destructive `rm -rf` commands through a deny decision.
    source_pointers:
      - "primary-code-claude-com-docs-en-hooks.md.md lines 62-150"

  - id: "B02-C007"
    label: fact
    confidence: high
    claim: >
      Hook scope can be user, project, local project override, managed policy, plugin, or active skill/agent frontmatter; this makes hooks a cross-cutting enforcement layer distinct from normal prompt guidance.
    source_pointers:
      - "primary-code-claude-com-docs-en-hooks.md.md lines 166-180"

  - id: "B02-C008"
    label: fact
    confidence: high
    claim: >
      Subagents isolate exploratory or specialized work in separate context windows and return summaries to the main conversation, preserving main-thread context and enabling tool/model specialization.
    source_pointers:
      - "primary-code-claude-com-docs-en-sub-agents.md.md lines 7-14"
      - "primary-code-claude-com-docs-en-sub-agents.md.md lines 19-29"

  - id: "B02-C009"
    label: fact
    confidence: high
    claim: >
      Built-in Explore and Plan subagents are read-only/research-oriented and keep exploration results out of the main context, while general-purpose subagents can perform complex multi-step operations with broader tools.
    source_pointers:
      - "primary-code-claude-com-docs-en-sub-agents.md.md lines 31-86"

  - id: "B02-C010"
    label: fact
    confidence: high
    claim: >
      `.claude/` is the project-level surface for settings, hooks, rules, skills, agents, workflows, output styles, and other project-specific extensions; `CLAUDE.md` is loaded as session guidance rather than an enforcement surface.
    source_pointers:
      - "primary-code-claude-com-docs-en-claude-directory.md.md lines 7-10"
      - "primary-code-claude-com-docs-en-claude-directory.md.md lines 30-39"
      - "primary-code-claude-com-docs-en-claude-directory.md.md lines 101-141"

  - id: "B02-C011"
    label: fact
    confidence: high
    claim: >
      Rules in `.claude/rules/` provide topic-scoped or path-scoped guidance; like `CLAUDE.md`, rules are guidance Claude reads, not enforced configuration.
    source_pointers:
      - "primary-code-claude-com-docs-en-claude-directory.md.md lines 163-214"

  - id: "B02-C012"
    label: fact
    confidence: high
    claim: >
      Plugins bundle multiple Claude Code components, including skills, agents, hooks, MCP servers, LSP servers, and monitors, into distributable directories.
    source_pointers:
      - "primary-code-claude-com-docs-en-plugins-reference.md.md lines 15-18"
      - "primary-code-claude-com-docs-en-plugins-reference.md.md lines 19-49"
      - "primary-code-claude-com-docs-en-plugins-reference.md.md lines 51-190"

  - id: "B02-C013"
    label: fact
    confidence: high
    claim: >
      MCP connects Claude Code to external tools, databases, APIs, and event channels, but requires explicit trust evaluation because external content can expose prompt-injection risk.
    source_pointers:
      - "secondary-code-claude-com-docs-en-mcp.md.md lines 7-15"
      - "secondary-code-claude-com-docs-en-mcp.md.md lines 17-36"
      - "secondary-code-claude-com-docs-en-mcp.md.md lines 196-218"

  - id: "B02-C014"
    label: interpretation
    confidence: high
    claim: >
      Claude Code orchestration should be modeled as a layered control plane: `CLAUDE.md` and rules for always-on/path-scoped guidance; skills for repeatable procedures; hooks/settings for enforcement; subagents for context isolation; MCP for external tool surfaces; plugins for distributable bundles.
    source_pointers:
      - "primary-code-claude-com-docs-en-claude-directory.md.md lines 30-39 and 101-141"
      - "primary-code-claude-com-docs-en-skills.md.md lines 11-22"
      - "primary-code-claude-com-docs-en-hooks.md.md lines 7-19"
      - "primary-code-claude-com-docs-en-sub-agents.md.md lines 7-14"
      - "primary-code-claude-com-docs-en-plugins-reference.md.md lines 15-18"
      - "secondary-code-claude-com-docs-en-mcp.md.md lines 7-15"

  - id: "B02-C015"
    label: recommendation
    confidence: high
    claim: >
      Apex should reserve hooks and permissions for hard gates, and avoid relying on `CLAUDE.md`, rules, or skill prose to enforce destructive-operation, Phase 2, or source-custody boundaries.
    source_pointers:
      - "primary-code-claude-com-docs-en-hooks.md.md lines 62-150"
      - "primary-code-claude-com-docs-en-claude-directory.md.md lines 116-118"
      - "manifests/phase0/phase0-navigation-report.md lines 20-24"

  - id: "B02-C016"
    label: contradiction
    confidence: medium
    claim: >
      Claude Code's integrated command/skill mechanism creates a tension for Apex naming: `commands/` files still work, but skills are recommended for new workflows because they can bundle files and frontmatter; legacy command patterns should not be treated as first-class long-term architecture unless there is a migration reason.
    source_pointers:
      - "primary-code-claude-com-docs-en-skills.md.md lines 15-22"
      - "primary-code-claude-com-docs-en-skills.md.md lines 156-158"
      - "primary-code-claude-com-docs-en-claude-directory.md.md lines 25-26"
```

## 4. Concepts Extracted

```yaml
concepts_extracted:
  - concept_slug: claude-code-control-plane
    label: "Claude Code control plane"
    definition: "The combined system of project memory, settings, hooks, skills, subagents, plugins, workflows, MCP servers, and rules."
    confidence: high
    source_pointers:
      - "primary-code-claude-com-docs-en-claude-directory.md.md lines 7-10"

  - concept_slug: soft-guidance-vs-hard-enforcement
    label: "Soft guidance vs hard enforcement"
    definition: "Guidance files (`CLAUDE.md`, rules, skills) influence model behavior; settings, permissions, and hooks can enforce policy before or after tool calls."
    confidence: high
    source_pointers:
      - "primary-code-claude-com-docs-en-claude-directory.md.md lines 30-39 and 116-118"
      - "primary-code-claude-com-docs-en-hooks.md.md lines 62-150"

  - concept_slug: skill-command-convergence
    label: "Skill/command convergence"
    definition: "Claude Code has merged custom commands into skills; commands remain supported but skills are preferred for new workflows with supporting files."
    confidence: high
    source_pointers:
      - "primary-code-claude-com-docs-en-skills.md.md lines 15-22"

  - concept_slug: subagent-context-isolation
    label: "Subagent context isolation"
    definition: "A delegation mechanism where specialized work occurs in a separate context and returns compact results to the main session."
    confidence: high
    source_pointers:
      - "primary-code-claude-com-docs-en-sub-agents.md.md lines 7-14"

  - concept_slug: hook-enforcement-gate
    label: "Hook enforcement gate"
    definition: "A lifecycle event handler that can block, transform, verify, log, or trigger actions around model turns and tool calls."
    confidence: high
    source_pointers:
      - "primary-code-claude-com-docs-en-hooks.md.md lines 17-60"

  - concept_slug: plugin-bundled-orchestration
    label: "Plugin-bundled orchestration"
    definition: "Packaging skills, agents, hooks, MCP servers, and related components into one installable/distributable extension."
    confidence: high
    source_pointers:
      - "primary-code-claude-com-docs-en-plugins-reference.md.md lines 15-18"

  - concept_slug: mcp-tool-connectivity-layer
    label: "MCP tool connectivity layer"
    definition: "A tool/data access layer that lets Claude Code interact with external systems while requiring trust and injection-risk controls."
    confidence: high
    source_pointers:
      - "secondary-code-claude-com-docs-en-mcp.md.md lines 7-36"
```

## 5. Entities Extracted

```yaml
entities_extracted:
  - entity_slug: claude-code-skills
    entity_label: "Claude Code skills"
    entity_type: "runtime_component"
    role: "Repeatable procedure and reference packages invoked directly or automatically."
    confidence: high

  - entity_slug: claude-code-hooks
    entity_label: "Claude Code hooks"
    entity_type: "runtime_component"
    role: "Lifecycle event enforcement and automation mechanism."
    confidence: high

  - entity_slug: claude-code-subagents
    entity_label: "Claude Code subagents"
    entity_type: "runtime_component"
    role: "Context-isolated worker sessions with custom prompts, tools, models, and permissions."
    confidence: high

  - entity_slug: claude-code-plugins
    entity_label: "Claude Code plugins"
    entity_type: "distribution_component"
    role: "Bundle skills, agents, hooks, MCP servers, and LSP integrations."
    confidence: high

  - entity_slug: model-context-protocol
    entity_label: "Model Context Protocol"
    entity_type: "protocol"
    role: "External tool/data connectivity standard used by Claude Code."
    confidence: high

  - entity_slug: claude-md
    entity_label: "CLAUDE.md"
    entity_type: "guidance_file"
    role: "Always-loaded project instruction file for session-level behavior."
    confidence: high

  - entity_slug: claude-settings-json
    entity_label: ".claude/settings.json"
    entity_type: "configuration_file"
    role: "Project-level configuration and enforcement surface for permissions, hooks, model, environment, and output style."
    confidence: high
```

## 6. Contradictions or Tensions

```yaml
contradictions_or_tensions:
  - id: "B02-T001"
    label: contradiction
    confidence: high
    summary: >
      Guidance and enforcement are distinct surfaces. The `.claude` docs state that CLAUDE.md and rules are guidance, while settings/hooks/permissions are enforced. Any Apex design that encodes hard gates only in skill prose or CLAUDE.md is weaker than one backed by hooks or deterministic scripts.
    source_pointers:
      - "primary-code-claude-com-docs-en-claude-directory.md.md lines 30-39 and 116-118"
      - "primary-code-claude-com-docs-en-hooks.md.md lines 62-150"

  - id: "B02-T002"
    label: contradiction
    confidence: medium
    summary: >
      Project-level skills, hooks, and MCP configuration are shareable and useful, but they are also trust-sensitive. Apex wants repo-native orchestration, while Claude Code warns that untrusted projects should not silently inject instructions or tool surfaces.
    source_pointers:
      - "adding-skills-support.mdx lines 91-100"
      - "secondary-code-claude-com-docs-en-mcp.md.md lines 32-36"
      - "primary-code-claude-com-docs-en-skills.md.md continuation lines 156-160"

  - id: "B02-T003"
    label: contradiction
    confidence: medium
    summary: >
      Plugins support distribution of full orchestration bundles, but plugin-shipped agents have security restrictions and do not support every frontmatter field available to project/user subagents.
    source_pointers:
      - "primary-code-claude-com-docs-en-plugins-reference.md.md lines 51-83"
      - "primary-code-claude-com-docs-en-sub-agents.md.md lines 230-237"
```

## 7. Open Questions

```yaml
open_questions:
  - id: "B02-Q001"
    label: open_question
    confidence: high
    question: "Which Apex gates require hook-level enforcement rather than skill-prose instruction only?"
    source_pointers:
      - "primary-code-claude-com-docs-en-hooks.md.md lines 62-150"
      - "manifests/phase0/phase0-navigation-report.md lines 20-24"

  - id: "B02-Q002"
    label: open_question
    confidence: medium
    question: "Should Apex package reusable orchestration surfaces as plain repo skills, plugins, or both?"
    source_pointers:
      - "primary-code-claude-com-docs-en-skills.md.md lines 101-128"
      - "primary-code-claude-com-docs-en-plugins-reference.md.md lines 15-18"

  - id: "B02-Q003"
    label: open_question
    confidence: medium
    question: "Which Apex subagent definitions should be persistent project files, and which should remain ephemeral CLI/session definitions?"
    source_pointers:
      - "primary-code-claude-com-docs-en-sub-agents.md.md lines 150-190"

  - id: "B02-Q004"
    label: open_question
    confidence: medium
    question: "How should Apex distinguish MCP servers that are safe to commit in `.mcp.json` from user-local or operator-private MCP servers?"
    source_pointers:
      - "secondary-code-claude-com-docs-en-mcp.md.md lines 60-180"
```

## 8. Proposed Phase 2 Wiki Targets

```yaml
proposed_phase_2_wiki_targets:
  summaries:
    - "wiki/summaries/claude-code-orchestration-surface.md"
  concepts:
    - "wiki/concepts/claude-code-control-plane.md"
    - "wiki/concepts/soft-guidance-vs-hard-enforcement.md"
    - "wiki/concepts/skill-command-convergence.md"
    - "wiki/concepts/subagent-context-isolation.md"
    - "wiki/concepts/hook-enforcement-gate.md"
    - "wiki/concepts/plugin-bundled-orchestration.md"
    - "wiki/concepts/mcp-tool-connectivity-layer.md"
  entities:
    - "wiki/entities/claude-code-skills.md"
    - "wiki/entities/claude-code-hooks.md"
    - "wiki/entities/claude-code-subagents.md"
    - "wiki/entities/claude-code-plugins.md"
    - "wiki/entities/model-context-protocol.md"
    - "wiki/entities/claude-md.md"
    - "wiki/entities/claude-settings-json.md"
  contradiction_pages:
    - "wiki/concepts/soft-guidance-vs-enforced-gate-boundary.md"
    - "wiki/concepts/repo-native-orchestration-vs-trust-safety.md"
```

## 9. Phase 2 Gate Statement

Phase 2 is blocked. Do not write `wiki/concepts/`, `wiki/entities/`, `wiki/summaries/`, semantic index sections, or final compiled KB pages until the operator gives the exact approval phrase in a later turn:

```text
approve ingest
```
