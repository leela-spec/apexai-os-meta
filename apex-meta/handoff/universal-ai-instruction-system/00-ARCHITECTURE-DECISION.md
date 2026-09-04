---
type: ArchitectureDecision
title: Universal AI Instruction System — Architecture Decision
description: Evidence-backed decision to reuse established scoped-instruction and Agent Skill patterns through a canonical portable behavior layer and thin runtime adapters.
status: decision_ready_not_propagated
created: 2026-09-04
---

# Universal AI Instruction System — Architecture Decision

## Decision

Adopt **canonical portable behavior modules with thin runtime adapters**.

Reuse the existing Apex Informatics hierarchy and established agent instruction mechanisms. Do not create a new Apex instruction framework.

```text
CANONICAL PORTABLE BEHAVIOR MODULE
  core rule + trigger + focused method
          |
          +--> tiny self-sufficient snippet export
          |       |
          |       +--> AGENTS.md / custom instructions / system prompt
          |       +--> CLAUDE.md / GEMINI.md / Copilot adapter where required
          |
          +--> Agent Skill or focused method entrypoint when procedural depth is useful
                  |
                  +--> references / examples / evals / evidence, loaded JIT
```

**Candidate C wins.** Candidate A remains the universal fallback. Candidate B is the preferred implementation when the runtime supports Agent Skills.

## Why this is integration, not invention

| Existing mechanism | Proven role | Apex use |
|---|---|---|
| Apex Informatics | Five-plane scoping and progressive disclosure | Keep as information/instruction architecture owner |
| `AGENTS.md` | Cross-agent repository guidance with hierarchical scoping | Primary repository adapter where supported |
| Agent Skills | Metadata -> `SKILL.md` -> optional resources | Preferred deeper procedure packaging |
| Claude scoped rules / `CLAUDE.md` | Runtime-specific hierarchical and path-scoped instructions | Thin adapter only |
| Gemini `GEMINI.md` / context imports | Hierarchical and just-in-time context | Thin adapter only |
| Copilot instructions / `AGENTS.md` | Repository and path-specific instructions | Thin adapter only |
| Codex `AGENTS.md` discovery | Root-to-working-directory instruction aggregation | Thin adapter only |

Primary external references:

- https://agents.md/
- https://agentskills.io/specification
- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- https://www.anthropic.com/engineering/building-effective-agents
- https://github.com/github/spec-kit

## XML decision

### Reject XML as the canonical format

Do **not** make semantic XML tags the storage, routing, or portability standard.

Reasons:

1. The established cross-agent surfaces above use Markdown, frontmatter, hierarchical files, descriptions, and references.
2. XML tags are a useful prompting notation for some models, not a universal agent-instruction standard.
3. Exact formatting matters less than clear structure and high-signal context on modern models.
4. Requiring structured text around tool calls can conflict with native tool/function calling in some runtimes.
5. The uploaded `adaptive_informatics` XML already restates rules canonically owned by `apex-meta/informatics/standard.md`.
6. A second XML authority would create duplication and adapter drift.

### Allow XML as an optional adapter

A runtime-specific adapter MAY render a canonical short rule as XML when measured evaluation shows a benefit.

The XML remains derived output. It never becomes an independent policy owner.

## Canonical ownership

| Concern | Canonical owner |
|---|---|
| Information architecture, serialization, scoped instruction placement | `apex-meta/informatics/` |
| Hierarchical realization / V-model orientation | `apex-meta/informatics/MMM/` |
| Durable project/task state and handoffs | Existing Plan-Sync-Session owners |
| Action authorization / irreversible mutation gates | Existing authorization and mutation contracts |
| Universal interaction behaviors selected by this run | One canonical module each; child handovers research final authoring |
| Task-specific deterministic patching | Task-specific procedure/Skill, not universal behavior |
| Runtime delivery | Derived adapter only |

## Layer contract

### L0 — always-on adapter

Keep only enough information to change behavior correctly.

Requirements:

- self-sufficient core rule;
- explicit trigger for deeper guidance when needed;
- no encyclopedia content;
- no hidden dependency on a file the runtime cannot read;
- no mandatory ceremony for simple work.

### L1 — focused method

Load only when the task matches the trigger or the short rule is insufficient.

A focused method may be:

- a concise Markdown method file;
- an Agent Skill when the behavior is procedural and the runtime supports Skills;
- an inlined focused reference when filesystem retrieval is unavailable.

### L2 — deeper resources

Load examples, edge cases, evidence, evaluations, or scripts only when required.

Keep references shallow. Avoid chains of references that force agents to explore the repository.

## Runtime adapter rules

1. Adapters MUST NOT become policy owners.
2. Adapters SHOULD point to canonical modules instead of copying deep guidance.
3. If text must be copied, treat it as a generated/mirrored export with one canonical source.
4. Runtime-specific syntax MAY optimize delivery without changing semantics.
5. Path-specific rules belong in scoped runtime mechanisms, not root universal instructions.
6. If a runtime cannot read linked files, the short rule still applies. Inline only the focused method needed for the active task.

## Architecture candidate comparison

| Candidate | Portability | Progressive disclosure | Established reuse | Drift risk | Verdict |
|---|---:|---:|---:|---:|---|
| A — short text + Markdown references | Very high | Medium | High | Low | Universal fallback |
| B — runtime root + Agent Skills | Medium-high | Very high | Very high | Low | Preferred where supported |
| C — canonical modules + thin adapters | **Very high** | **Very high** | **Very high** | Medium unless ownership is strict | **Selected architecture** |

Candidate C uses A and B rather than replacing them.

## Existing Apex findings reused

The 2026-09-03 `Agent_Setup` research already supports this decision:

- use established machine-facing vocabulary before local shorthand;
- execute simple work directly;
- use compact preflight for nontrivial work;
- scale to full or recursive specification only when observable complexity requires it;
- use top-down decomposition and bottom-up verification/validation;
- keep the shared method separate from Plan-Sync-Session and authorization.

This run does not create a competing method.

## Non-decisions

This run does not decide:

- the final wording of global instructions;
- which runtime receives which adapter;
- whether a final module is a Skill or plain method file;
- whether every candidate module survives independent research;
- any Plan-Sync-Session changes.

Those decisions require module evaluation and later cross-module synthesis.

## Acceptance

The architecture is acceptable only if evaluation confirms:

- simple requests remain direct;
- complex requests can discover deeper guidance;
- linked files improve behavior without being required for basic compliance;
- adapters preserve semantics across supported runtimes;
- combined snippets do not cause ceremony, conflict, or context bloat;
- no concept has multiple canonical owners.
