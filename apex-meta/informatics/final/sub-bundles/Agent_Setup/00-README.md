---
type: research-package-index
status: decision_ready_not_applied
created: 2026-09-03
basis_handover: apex-meta/handoff/2026-09-03-agent-working-method-and-project-realization-research-handover.md
repository: leela-spec/apexai-os-meta
branch: main
---

# Agent Setup — Working Method Research Package

## Purpose

Select a general Apex agent working method that is recognizable to modern AI agents, adapts to task complexity, preserves top-down decomposition plus bottom-up verification/validation, and fits the existing Plan-Sync-Session and Informatics architecture without creating a competing state system.

This package is **research and patch planning only**. It does not modify `AGENTS.md`, `.claude/CLAUDE.md`, any live `SKILL.md`, Plan-Sync-Session contracts, Weekly Orchestrator, or Multi-Agent Orchestration.

## Decision summary

**Recommended architecture: thin established-method hybrid.**

Do not invent an Apex-native Macro/Meso/Micro methodology as the primary agent vocabulary, and do not install/copy GitHub Spec Kit wholesale into Apex.

Use four established ideas for four different jobs:

1. **Spec-Driven Development vocabulary and artifact flow** for intent-to-realization: specification/requirements -> plan/design -> tasks/work packages -> implementation -> convergence.
2. **Systems Engineering requirements flowdown + V&V** for the hierarchical loop: decompose/allocate downward; integrate, verify and validate upward.
3. **WBS decomposition** for deliverable-oriented completeness and parent/child scope accounting.
4. **Agent Skills progressive disclosure** for instruction loading: tiny trigger metadata -> small method instructions -> detailed references/evals only when needed.

Apex-specific adaptation should be limited to routing these concepts through the existing Plan-Sync-Session backbone and current Informatics surfaces.

## Why this is the leading option

- GitHub Spec Kit explicitly supports a normal SDD cycle, bounded implementation runs for larger work, subagent delegation, and recursive "spec of specs" only when lighter scoping fails.
- Kiro independently productizes adaptive rigor: Quick Spec for well-understood bounded work; full Requirements -> Design -> Tasks with review gates for higher ambiguity/risk.
- NASA systems-engineering guidance formalizes hierarchical requirements decomposition/flowdown and requires validation against parent/stakeholder expectations before further decomposition; verification and validation then operate on the upward/integration side.
- PMI WBS supplies established deliverable-oriented decomposition and the 100% rule, but is intentionally not treated as the whole lifecycle.
- Anthropic Agent Skills explicitly uses progressive disclosure and recommends keeping `SKILL.md` compact with deeper references/scripts/evals loaded only when necessary.
- Current Apex already has a compact router and explicit Plan-Sync-Session proposal/computation/mutation separation, so replacing that substrate would create duplication rather than value.

## Package contents

| File | Owns |
|---|---|
| `01-method-and-vocabulary-decision.md` | Method comparison, canonical vocabulary, complexity routing, Macro/Meso/Micro mapping |
| `02-preflight-and-progressive-disclosure-design.md` | Pre-execution understanding contract, progressive-disclosure file architecture, ultra-short global instruction candidates |
| `03-plan-sync-session-integration-and-patch-plan.md` | Integration map, ownership boundaries, exact patch targets, implementation order |
| `04-simulation-evaluation-suite.yaml` | Machine-readable scenario/evaluation suite for validating the method before live adoption |

## Operator decision gate

Recommended approval set:

- **D1 = HYBRID:** thin Spec Kit/SDD + Systems Engineering V&V vocabulary; no wholesale framework transplant.
- **D2 = ADAPTIVE:** direct path for trivial work, compact preflight for bounded nontrivial work, full spec flow only when ambiguity/risk/size warrants it, recursive decomposition only when bounded execution still exceeds context/manageability.
- **D3 = PREVIEW_NOT_APPROVAL:** for nontrivial work the agent exposes a compact understanding/execution preflight before mutation; this is not automatically a new human approval gate unless existing risk/authorization policy requires one.
- **D4 = ONE_SHARED_METHOD_SURFACE:** specialist agents reference one shared method surface; they do not duplicate lifecycle instructions.
- **D5 = PLAN_SYNC_SESSION_REMAINS_STATE_OWNER:** no new registry, canonical task database, workflow state machine, or permission system is introduced by this method.

If these five decisions are accepted, the next phase is a bounded implementation patch against the targets listed in `03-plan-sync-session-integration-and-patch-plan.md`, followed by the simulation suite before any broad rollout.

## Primary external evidence

- GitHub Spec Kit overview: https://github.github.com/spec-kit/
- Agentic SDD: https://github.github.com/spec-kit/reference/agentic-sdd.html
- Handling complex features: https://github.github.com/spec-kit/concepts/complex-features.html
- Spec of Specs: https://github.github.com/spec-kit/concepts/spec-of-specs.html
- Kiro Quick Spec: https://kiro.dev/docs/specs/quick-spec/
- NASA software requirements flowdown: https://swehb.nasa.gov/spaces/7150/pages/16449651/SWE-050%2B-%2BSoftware%2BRequirements
- NASA Systems Modeling Handbook: https://standards.nasa.gov/standard/NASA/NASA-HDBK-1009
- PMI WBS guidance: https://www.pmi.org/learning/library/practice-standard-work-breakdown-structures-8063
- Anthropic Agent Skills overview: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- Anthropic Skill authoring best practices: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices

## Apex evidence inspected

- `AGENTS.md`
- `.claude/CLAUDE.md`
- `.claude/skills/apex-plan/SKILL.md`
- `.claude/skills/apex-session/SKILL.md`
- `apex-meta/informatics/index.md`
- `apex-meta/handoff/agent-skill-system-research/best-practice-report.md`
- `apex-meta/handoff/2026-09-03-agent-working-method-and-project-realization-research-handover.md`
