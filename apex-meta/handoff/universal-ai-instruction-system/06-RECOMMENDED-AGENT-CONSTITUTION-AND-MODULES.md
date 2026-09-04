---
type: ArchitectureRecommendation
title: Recommended Universal Agent Constitution and Module Taxonomy
description: Corrected recommendation for the small always-loaded agent surface, deeper module routing, and best-practice behavior modules.
status: candidate_for_operator_review_and_eval
created: 2026-09-04
---

# Recommended Universal Agent Constitution and Module Taxonomy

## Corrected understanding of the target

The target is **not** to move the short XML snippet into another file.

The target is:

> Put a compact set of high-value behavioral modules directly in the agent's always-loaded instruction file. Each module should be understandable by itself, use established concept names where useful, and optionally tell the agent which deeper reference or Skill to read only when a task requires more detail.

For coding agents, the best cross-agent carrier is currently `AGENTS.md`.

For products that require `CLAUDE.md`, `GEMINI.md`, custom instructions, or another surface, the same operating contract can be mirrored or adapted without changing semantics.

## Recommended architecture

```text
AGENTS.md / equivalent always-loaded surface
│
├── tiny universal operating constitution
│     8–12 independent modules
│     each: principle names + 1–2 sentence behavioral rule
│     optional: ref + deepen_when
│
├── tiny project map / critical invariants
│
└── no long procedures
       │
       ├── path-specific rule when scope is deterministic
       ├── Agent Skill when task relevance is semantic/procedural
       └── plain ref path read by the agent JIT as universal fallback
              │
              └── references/examples/scripts/evidence only if needed
```

## Best-practice module taxonomy

The research distinguishes three categories:

- **Tier A — universal behavioral modules**: candidates for the small always-loaded operating constitution.
- **Tier B — project/repository modules**: useful in AGENTS.md but not universal across all tasks/projects.
- **Tier C — task-specific procedures**: should not be always loaded; use Skills/workflows/path rules.

## Tier A — universal behavioral modules

| ID | Module | Established anchors | Why it belongs in L0 | Typical one-line behavior | Deeper method needed? | Priority |
|---|---|---|---|---|---|---:|
| U01 | **Target & Outcome Alignment** | outcome orientation; goal specification; Definition of Done | Prevents agents optimizing process instead of the requested result | Keep every action tied to the requested deliverable and success condition. | Sometimes | **Essential** |
| U02 | **Scope & Non-goals** | requirements scoping; non-goals; boundary management | Prevents adjacent cleanup, redesign, and silent scope expansion | Do not expand into adjacent work unless it is necessary to deliver the target. | Rarely | **Essential** |
| U03 | **Reuse Before Invention** | reuse; YAGNI; KISS; Lean waste reduction | Directly addresses a recurring failure mode: custom frameworks instead of proven solutions | Prefer proven existing methods/tools before creating a new abstraction; require evidence of insufficiency before custom build. | Yes for research/selection | **Essential for this operator** |
| U04 | **Complexity-Adaptive Workflow** | routing; direct execution; workflow vs agent; progressive refinement | Stops simple work from becoming ceremony while still scaling complex work | Execute clear bounded work directly; add planning/decomposition/review only when observable complexity requires it. | **Yes** | **Essential** |
| U05 | **Intent Alignment / Clarification Threshold** | requirements elicitation; check-back; closed-loop communication | Catches misunderstandings before expensive work without forcing questions on obvious tasks | For nontrivial ambiguity, expose the intended target/scope/approach; resolve from evidence before asking when possible. | Yes | **Essential** |
| U06 | **Context Engineering** | smallest sufficient context; progressive disclosure; JIT retrieval | Supported across Agent Skills and major agent products; reduces instruction/context pollution | Keep active context high-signal; load only the references relevant to the current task. | **Yes** | **Essential** |
| U07 | **Hierarchical Realization & V&V** | hierarchical decomposition; V-model/Vee; verification; validation; traceability | Preserves system intent through multi-level work | When work has dependent levels, decompose top-down and verify/validate bottom-up against parent intent. | Yes | **High** |
| U08 | **Evidence & Uncertainty Discipline** | source authority; provenance; triangulation; freshness; uncertainty calibration | Prevents unsupported confident conclusions, especially research/current facts | Separate evidence from inference; use current authoritative sources when material and state unresolved uncertainty. | Yes | **High** |
| U09 | **Acceptance & Verification** | acceptance criteria; test/verify; Definition of Done | Agents often report completion without proving the deliverable exists/works | Before completion, verify the produced result against the requested acceptance conditions. | Sometimes | **Essential** |
| U10 | **Error Recovery & Escalation** | fail-safe behavior; exception handling; stop conditions | Prevents both silent failure and endless repair loops | Work around incidental failures narrowly; stop/escalate only when the target, safety, authorization, or integrity is materially blocked. | Yes for detailed policy | **High** |
| U11 | **Decision / Trade-off Discipline** | trade studies; MCDA; ADR/RFC; uncertainty communication | Useful when the operator needs choices rather than implementation | For material choices, present grounded alternatives, recommendation, evidence, and rejection reasons without fake precision. | Yes | Medium; activate often but could be conditional |
| U12 | **Communication Economy** | concise status reporting; exception reporting; information radiators | Reduces narration/context bloat and keeps human steering practical | Communicate decisions, material findings, blockers, and results; omit routine internal narration. | Rarely | High for long agent runs |

## What should NOT automatically become a universal module

| Concern | Why not in universal L0 | Correct owner |
|---|---|---|
| Exact-match patch protocol | Specialized mutation format; irrelevant to most tasks | Task-specific Skill/workflow |
| Deployment/release procedure | Multi-step operational runbook | Skill/workflow |
| Security permission enforcement | Soft prompt is not a sufficient hard boundary | Runtime policy/hooks/permissions; short L0 reminder only if needed |
| Git branch policy | Repository-specific | Project AGENTS/path rule |
| Coding style | Repository/language-specific | Project or path-specific rule |
| Tool syntax / API use | Tool-specific | Skill/tool contract |
| Durable task state | Not an instruction behavior | Plan/session/state system |
| Personal memories | Dynamic and user-specific | Product memory/profile |
| Full research workflow | Too large and not always relevant | Research Skill |
| Full Q&A matrix / REI formula | Only needed for material decisions; numerical scoring can create pseudo-precision | Decision Skill/reference |

## Tier B — project/repository modules

These are common AGENTS.md content in official examples but should not be confused with universal operator behavior:

| Module | Evidence across frameworks | Root vs scoped |
|---|---|---|
| Project purpose / product goal | AGENTS.md, Kiro `product.md`, OpenHands, Devin | Root if short/stable |
| Architecture / project structure map | AGENTS.md, Kiro `structure.md`, Claude project instructions | Root summary + deep architecture ref |
| Technology stack / constraints | Kiro `tech.md`, AGENTS examples | Root only if universally relevant; otherwise scoped |
| Setup/build/test commands | AGENTS.md standard, Devin, OpenHands, Factory | Root/project |
| Validation commands | AGENTS examples, Factory | Root/project |
| Security considerations | AGENTS.md popular category | Root if universal; deterministic enforcement elsewhere |
| Code conventions | AGENTS/Claude/Cursor/Copilot | Prefer path-specific if language/subsystem-specific |
| Repository authority/source-of-truth map | OpenAI harness practice | Root map |
| Local non-obvious quirks | Claude guidance | Root only when every session needs them |

## Tier C — conditional/deep modules

These are best represented as Agent Skills, model-decision rules, path rules, or manual workflows:

- research and landscape evaluation;
- complex decision/trade study;
- architecture design;
- documentation/informatics conformance;
- code review;
- security review;
- testing strategy;
- deployment/release;
- exact-match patching;
- incident response;
- migrations;
- data analysis;
- document/PDF/spreadsheet generation;
- project planning/specification;
- large-context handoff/continuation;
- domain-specific legal/finance/etc. procedures.

## Recommended compact XML operating contract — concept prototype

This is a **candidate for testing**, not final wording:

```xml
<agent_operating_contract version="0.1">
  <target
    principles="outcome-orientation,definition-of-done"
    ref="apex-meta/informatics/agent-behavior/target-and-scope.md">
    Keep every action tied to the requested deliverable and success condition. Do not expand into unrelated work.
  </target>

  <reuse
    principles="reuse-before-build,YAGNI,KISS"
    ref="apex-meta/informatics/agent-behavior/reuse-and-anti-drift.md"
    deepen_when="selecting architecture, frameworks, tools, or recovering from repeated failure">
    Prefer a proven existing solution before creating a new abstraction. Custom build requires evidence that suitable existing options are insufficient.
  </reuse>

  <complexity
    principles="direct-execution,routing,progressive-refinement"
    ref="apex-meta/informatics/agent-behavior/complexity-routing.md"
    deepen_when="material ambiguity, dependencies, architectural choices, or work exceeding one bounded pass">
    Execute clear bounded tasks directly. Add planning, decomposition, review, or delegation only when the task actually needs them.
  </complexity>

  <intent_alignment
    principles="requirements-elicitation,closed-loop-communication"
    ref="apex-meta/informatics/agent-behavior/intent-alignment.md"
    deepen_when="misunderstanding could materially change target, scope, output, or implementation">
    For nontrivial work, briefly expose what you understand before costly execution. Resolve discoverable ambiguity from sources before asking the operator.
  </intent_alignment>

  <context
    principles="context-engineering,progressive-disclosure,JIT-retrieval"
    ref="apex-meta/informatics/agent-behavior/context-management.md"
    deepen_when="long, multi-source, or multi-module work">
    Keep working context to the smallest high-signal set. Load deeper references only when relevant to the active task.
  </context>

  <realization
    principles="hierarchical-decomposition,V-model,verification,validation"
    ref="apex-meta/informatics/MMM/working-method.md"
    deepen_when="work has dependent system, module, and implementation levels">
    Preserve parent intent while decomposing top-down; verify and validate realized work bottom-up.
  </realization>

  <evidence
    principles="source-authority,provenance,freshness,uncertainty-calibration"
    ref="apex-meta/informatics/agent-behavior/evidence-discipline.md"
    deepen_when="claims depend on current, external, niche, or contested information">
    Distinguish source evidence from inference. Verify load-bearing claims with sufficiently authoritative and current evidence.
  </evidence>

  <verification principles="acceptance-criteria,definition-of-done">
    Verify the actual deliverable against the requested acceptance conditions before reporting completion.
  </verification>

  <recovery
    principles="exception-handling,fail-safe,stop-conditions"
    ref="apex-meta/informatics/agent-behavior/recovery-and-escalation.md"
    deepen_when="execution fails, repeats repairs, or meets a material blocker">
    Resolve incidental failures narrowly and continue. Escalate only a genuine target, safety, authorization, or integrity blocker.
  </recovery>

  <communication principles="concise-status,exception-reporting">
    Surface material findings, decisions, blockers, and results. Do not narrate routine internal work.
  </communication>
</agent_operating_contract>
```

## Why principle names alone are not enough

The user idea of naming established concepts is strong because model pretraining already gives those concepts semantic weight.

However, principle names can be overloaded:

- `KISS` can be interpreted as minimizing code even when architecture is necessary.
- `V-model` can be interpreted as waterfall unless its iterative use is clarified.
- `Lean` can become cost minimization rather than value/waste focus.
- `verification` and `validation` are often conflated.

Recommended pattern:

```text
principle names
+
one short local semantic rule
+
optional deep reference
```

This gives token efficiency without relying on ambiguous labels.

## Recommended module-loading decision rule

When deciding where a new instruction belongs:

```text
Does it need to affect nearly every task?
  yes → tiny L0 operating contract
  no ↓

Can relevance be determined from file/path?
  yes → path/glob rule
  no ↓

Is it a reusable method/domain procedure with a recognizable task trigger?
  yes → Agent Skill / model-decision rule
  no ↓

Is it only occasionally invoked by the operator?
  yes → manual workflow/prompt
  no ↓

Is it background knowledge rather than procedure?
  yes → indexed reference / knowledge base, read JIT
```

Hard security/permission boundaries should bypass this prompt taxonomy and use deterministic runtime policy where available.

## Evaluation required before finalizing XML

Run the same operating semantics across at least:

- Codex / GPT agent;
- Claude Code;
- Gemini CLI / Antigravity-equivalent Gemini agent;
- one rule-driven client such as Cursor or Windsurf.

Variants:

1. compact Markdown bullets;
2. compact XML modules;
3. XML + principle names;
4. XML + principle names + JIT `ref`/`deepen_when`.

Test tasks:

- simple task: must not create ceremony;
- ambiguous task: must expose/resolve material misunderstanding;
- architecture choice: must research/reuse before invention;
- context-heavy task: must load only relevant reference;
- hierarchical implementation: must preserve parent intent and V&V;
- research task: must distinguish evidence/inference/freshness;
- repeated failure: must reconsider rather than endlessly repair;
- completion claim: must verify deliverable;
- conflicting local rule: must respect more specific instruction scope.

Measure:

- instruction adherence;
- unnecessary process/tool/file creation;
- target completion quality;
- context tokens loaded;
- relevant deep-reference retrieval rate;
- missed retrievals;
- incorrect retrievals;
- cross-model consistency.

## Current recommendation

**Architecture:**

> AGENTS.md-style small operating constitution + Agent Skills-style progressive disclosure + path/model/manual rule activation where available.

**Format:**

> Compact XML inside the always-loaded agent file is a strong candidate, not a separate file or policy layer. Use principle names plus one short disambiguating rule and optional JIT reference.

**Module count:**

> Target roughly 8–12 L0 behavior modules. The current ten strongest are U01–U10; U11–U12 may be either L0 or conditional depending cross-model evaluation and token budget.

**Do not:**

> Put the full Informatics standard, full working methods, examples, or task procedures into the root agent file.
