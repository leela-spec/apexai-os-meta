---
type: ModuleDeepeningResult
title: A04 Complexity-Adaptive Workflow
description: Evidence-backed deepening result for the universal <workflow> module, using process tailoring and progressive elaboration to scale planning, decomposition, delegation, and review without creating universal ceremony.
status: DONE
updated: 2026-09-07
---

# A04 — Complexity-Adaptive Workflow

## 1. Final decision

- **Module:** A04
- **XML tag:** `<workflow>`
- **Semantic purpose:** Match execution method and control depth to the actual characteristics of the task so simple work stays direct while uncertain, coupled, consequential, or genuinely complex work receives enough planning, decomposition, delegation, and review to improve outcome quality and throughput.
- **Selected deeper owner:** **No deeper artifact**
- **Selected established principles:** process tailoring/customization; progressive elaboration/adaptive planning; risk-informed technical planning.
- **Replaced as primary anchor:** `complexity-adaptive-routing`. The intent was directionally right, but the phrase is not the strongest established vocabulary and complexity alone is too narrow a trigger.
- **Retained conceptually but renamed:** `progressive-refinement` becomes the established project-management concept **progressive elaboration**.

### Final root XML

```xml
<workflow principles="process-tailoring,progressive-elaboration,risk-informed-planning">
  Tailor execution depth to task complexity, uncertainty, coupling, and consequence. Execute clear low-risk work directly; when those factors warrant it, plan, decompose, delegate independent work, and review proportionately, adapting as new evidence changes the task.
</workflow>
```

### Equivalent compact Markdown control

```markdown
**Workflow — process tailoring / progressive elaboration / risk-informed planning:** Tailor execution depth to task complexity, uncertainty, coupling, and consequence. Execute clear low-risk work directly; when those factors warrant it, plan, decompose, delegate independent work, and review proportionately, adapting as new evidence changes the task.
```

## 2. Why this is the right method

### 2.1 Underlying discipline evidence

The strongest established analogue is **process tailoring/customization**: keep the intent and required rigor of a process while adapting how much process is applied to the actual task.

NASA's current systems-engineering requirements explicitly define **customizing** as adapting implementation of engineering processes according to the program/project's **size, complexity, and acceptable risk**. Its tailoring/customization considerations extend beyond size to scope, failure consequences, human involvement, security, impact on other systems, longevity, serviceability, cost/schedule constraints, quality, and technology maturity. This is a stronger model than a complexity-only trigger.

NASA's Systems Engineering Handbook states the positive purpose directly: tailoring and customization should preserve the desired benefits while **eliminating unnecessary overhead**. It also warns that acceptable risk and mission needs matter. Therefore the correct agent behavior is neither "always use the full process" nor "always use the shortest process"; it is to select enough process for the task's risk and coordination characteristics.

NASA Technical Planning similarly plans the technical effort needed to satisfy project objectives within cost, schedule, and risk constraints. Planning is therefore a control mechanism tied to the work and its consequences, not a ritual deliverable.

PMI's tailoring guidance likewise adapts methodologies to project size, complexity, duration, organizational context, and risk tolerance. PMI's agile examination content uses the established term **adaptive planning** and explicitly links rolling-wave planning / **progressive elaboration** to using the appropriate level of detail and adapting planning cadence to size, complexity, and criticality.

The resulting model is:

```text
workflow depth is a task-dependent control variable

clear + bounded + low consequence + low uncertainty
  -> direct execution

multi-step / coupled / uncertain / broad / consequential
  -> plan or preflight enough to expose dependencies and hazards

independent parallelizable streams
  -> delegation / parallel execution may improve throughput or context isolation

strongly coupled or same-state work
  -> keep coordination local/sequential unless isolation is available

high consequence / hard-to-reverse / security- or data-sensitive work
  -> stronger review / validation / approval as applicable

new evidence changes task shape
  -> adapt the workflow rather than obeying a stale plan
```

### 2.2 Proven agent implementations

Current mature agent products implement the same pattern as **conditional execution modes**, not universal ceremony.

- **OpenAI Codex:** OpenAI's documented internal practice recommends starting with Ask Mode and an implementation plan for **large changes**, while Codex is also used directly for smaller well-scoped tasks. Current Codex supports multiple agents in parallel for substantial or independent work and review of their changes. This supports task-dependent planning and delegation rather than always-on orchestration.
- **Claude Code:** `/plan` is documented as a mode to use before a **large change**. `/batch` is for a large codebase change that can be decomposed into independent units. Claude's parallel-agent guidance says the right approach depends on coordination needs, whether workers must communicate, and whether they touch the same files; it also explicitly warns that parallel sessions multiply token usage. This is strong evidence against delegation theater.
- **GitHub Copilot:** Plan mode performs read-only task research and decomposition before implementation and is meant to produce an implementation plan for review. Copilot CLI describes custom/subagents as useful for complex multi-step work, research, code review, and isolated command execution rather than as a mandatory layer for every task.
- **Gemini CLI:** Plan Mode is a read-only environment for researching and planning **complex changes**. Its built-in planning workflow is adaptive, and Gemini can route planning and implementation phases differently. The current toolset also includes task dependency tracking and research subagents. Again, planning is a mode entered when useful, not the universal execution mode.

Across these systems the mature pattern is consistent:

1. direct work remains available;
2. planning is a distinct mode for changes that benefit from exploration/alignment;
3. decomposition and parallelism are conditional on separability and coordination cost;
4. review is an available control, not a proof that every task needs a formal review stage;
5. the workflow can change as the task becomes better understood.

### 2.3 Local inference / decision

The pilot sentence is directionally good but has two weaknesses:

1. **"observable task complexity" is too narrow.** A one-line credential, permission, destructive database, deployment, or security change can be structurally simple but highly consequential. Conversely a large routine transformation can be low-risk and mechanically direct.
2. **"only when ... requires it" can become artificial minimalism.** Planning, decomposition, or review often improve reliability before they become logically indispensable. The intended test is whether they materially improve reliability, coordination, or throughput given the task characteristics—not whether failure is otherwise certain.

The replacement therefore makes four factors explicit: **complexity, uncertainty, coupling, and consequence**. These capture most reasons to increase workflow depth without creating a numerical scoring system.

It also makes delegation specifically about **independent work**, preventing the common failure where agents spawn multiple workers for tightly coupled tasks and then spend more effort reconciling them than doing the work.

Finally, it requires adaptation when evidence changes. A plan is a current execution model, not a higher authority than the target or current state.

## 3. Semantic contract

### MUST

- Tailor workflow depth to the actual task rather than applying a fixed universal procedure.
- Consider at least these characteristics when they are material:
  - complexity / number of dependent moving parts;
  - uncertainty / unfamiliarity / unresolved facts;
  - coupling / shared state / cross-component dependencies;
  - consequence / risk / reversibility of failure.
- Execute clear, bounded, low-risk work directly without manufacturing a planning artifact.
- Use a planning/preflight step before substantial mutation when dependencies, uncertainty, breadth, or consequences make an explicit execution model materially useful.
- Decompose work when separate work units, dependencies, ownership boundaries, or validation points become useful to execution.
- Delegate or parallelize work only when tasks are sufficiently independent, isolatable, or context-heavy that delegation provides real value.
- Keep strongly coupled work coordinated rather than parallelizing it for appearance or agent count.
- Scale review/validation effort with consequence and change surface rather than line count alone.
- Adapt the workflow upward when hidden complexity/risk appears and downward when the task becomes simpler than expected.
- Treat plans, task graphs, subagents, checkpoints, and reviews as means for realizing the target, not as substitute deliverables unless the task explicitly asks for them.
- Honor an explicitly requested planning, review, or no-implementation mode even if execution could technically begin immediately.

### MUST NOT

- Require a formal plan, checklist, decomposition, subagent, or review ceremony for every task.
- Equate "small change" with "low risk" or "many files" with "high complexity" without considering consequences and coupling.
- Use "simple workflow" as an excuse for shallow content, weak validation, or insufficient rigor; A01 owns substantive adequacy.
- Split a coherent task into artificial subtasks only to demonstrate orchestration.
- Delegate tightly coupled work to multiple agents when shared state or coordination cost would make the result worse.
- Continue following an obsolete plan after evidence invalidates its assumptions.
- Turn planning into a delay tactic when the user requested execution and no real planning/authorization gate is needed.
- Use A04 to decide whether adjacent work belongs (A02), whether to reuse/build (A03), what the target means (A05), or what evidence standard proves a claim (A08).
- Treat process artifacts as completion proxies; the realized outcome remains authoritative under A01.

### Activation condition

Always active as a workflow-selection invariant. Its observable effect can be near-zero on trivial tasks.

### Deepen condition

None at the universal layer. When a task genuinely needs a specialized multi-step procedure, the relevant domain Skill/reference or neighboring conditional module should supply it. A04's job is to decide **how much workflow control is useful**, not to invent a universal project-management methodology.

## 4. Workflow tailoring model

This matrix is explanatory evidence for the module result, not a required runtime checklist.

| Task signal | Typical workflow response | Why |
|---|---|---|
| Clear, bounded, reversible, low-risk | Execute directly; verify result | Planning overhead is unlikely to improve the outcome |
| Multiple dependent steps / broad change | Short plan or preflight; sequence dependencies; checkpoints as useful | Makes hidden ordering and integration risk visible |
| High uncertainty / unfamiliar system | Read/research/explore before mutation; progressively refine plan | Reduces premature commitment |
| Independent research or implementation streams | Delegate/parallelize when context isolation or throughput benefits exceed coordination cost | Exploits parallelism without coupling damage |
| Same files / shared mutable state / high interdependence | Prefer one coordinated execution stream or isolated worktrees with explicit integration | Avoids conflict and reconciliation overhead |
| High consequence / difficult rollback / security / data integrity | Stronger preflight, review, validation, rollback/approval controls as applicable | Consequence justifies additional control even if implementation is short |
| Discovery changes assumptions | Revise or discard the plan; change execution mode | Progressive elaboration keeps the process aligned with current truth |

No row is a mandatory ceremony. The target, governing constraints, and task evidence decide the actual response.

## 5. Neighboring-module boundaries

### A01 `<target>` — substantive adequacy and proportional rigor

A01 decides what outcome quality, depth, rigor, and validation the target needs. A04 decides **how to organize execution** to achieve it. A04 must not interpret "direct execution" as permission to under-deliver.

### A02 `<scope>` — work boundary

A02 decides whether a work item belongs inside the authorized task. A04 only decides how in-scope work is organized. A planning step cannot authorize adjacent implementation.

### A03 `<reuse>` — reuse vs custom capability

A03 chooses between existing capability, adaptation, and custom construction. A04 can plan or delegate the chosen path but must not replace the reuse trade-off.

### A05 `<intent>` — ambiguity

A05 owns material intent ambiguity and operator check-back. A04 may detect that uncertainty increases workflow depth, but it must not invent a clarification protocol.

### A06 `<context>` — active information loading

A06 decides what context to load and when. A04 may use isolated subagents because context separation helps, but context policy remains A06's job.

### A07 `<realization>` — hierarchical decomposition and bottom-up verification/validation

A04 decides whether decomposition is warranted and how much execution structure is useful. When work genuinely has dependent system/module/implementation levels, A07 owns the Macro→Meso→Micro realization method and bottom-up verification/validation.

### A08 `<evidence>` — evidence discipline

A04 can decide that a consequential task deserves stronger review or validation stages. A08 determines what counts as sufficiently authoritative evidence and how uncertainty is represented.

### A10 `<recovery>` — failures during execution

A04 allows workflow adaptation when the task changes. A10 owns the actual response to errors, blockers, and escalation conditions.

### C01 `<decision>` and C02 `<research>`

A04 can route a task into decision analysis or research when complexity/uncertainty warrants those activities, but the specialized methods belong to the conditional modules.

## 6. Failure modes this module exists to prevent

1. **Planning theater:** producing plans/checklists because agents are expected to look methodical, even when direct execution is clearer and safer.
2. **Delegation theater:** spawning subagents without independent work, increasing token/context/coordination cost while lowering coherence.
3. **Complexity-only routing:** failing to plan/review a short but high-consequence or hard-to-reverse action.
4. **Size proxy error:** assuming file count, line count, or prompt length equals real task difficulty.
5. **Under-planning:** beginning mutation before understanding critical dependencies, risks, or integration points.
6. **Over-planning:** spending more effort specifying execution than the task can justify.
7. **Stale-plan obedience:** continuing to execute a plan after new evidence invalidates it.
8. **Premature parallelism:** splitting strongly coupled tasks across workers and paying reconciliation cost.
9. **Workflow as deliverable:** treating a task graph, plan, or review report as success instead of realizing the requested outcome.
10. **Process-induced minimalism:** using "lightweight" workflow language to reduce substantive quality rather than merely reduce unnecessary process.

## 7. Wording decision

### Candidate A — current complexity-only pilot

```xml
<workflow principles="complexity-adaptive-routing,progressive-refinement">
  Execute clear bounded work directly. Add planning, decomposition, delegation, or review only when observable task complexity requires it.
</workflow>
```

**Strength:** compact; strongly resists ceremony.

**Why it loses:** `complexity-adaptive-routing` is weak established vocabulary; risk, uncertainty, coupling, reversibility, and consequence are omitted; `requires` is too strict and may cause under-planning.

### Candidate B — always-plan / always-review

```xml
<workflow principles="planning,review">
  Plan before execution, decompose the work, and review the result before completion.
</workflow>
```

**Strength:** predictable and easy to enforce.

**Why it loses:** creates ceremony on trivial tasks, increases latency/context cost, and encourages mechanical plans and reviews as proxies for good execution.

### Candidate C — tailored adaptive workflow — SELECTED

```xml
<workflow principles="process-tailoring,progressive-elaboration,risk-informed-planning">
  Tailor execution depth to task complexity, uncertainty, coupling, and consequence. Execute clear low-risk work directly; when those factors warrant it, plan, decompose, delegate independent work, and review proportionately, adapting as new evidence changes the task.
</workflow>
```

**Strength:** grounded in established tailoring/adaptive-planning practice; includes risk and coupling; supports both direct execution and substantial orchestration; explicitly prevents stale plans and indiscriminate delegation.

**Trade-off:** slightly longer than the pilot, but the added factors remove important failure modes and reduce ambiguity.

### Candidate D — numeric routing score

```text
Score complexity, uncertainty, coupling, consequence, and reversibility; choose workflow tier 0-3 from the total.
```

**Strength:** deterministic-looking routing.

**Why it loses:** false precision, scoring overhead, brittle thresholds, and a new custom methodology with no evidence that a universal numeric score improves agent outcomes.

## 8. Deeper-owner decision

### Selected: no deeper artifact

A separate generic workflow Skill or reference is not justified at this stage.

Reasons:

1. Mature runtimes already provide planning modes, subagents, task graphs, worktrees, and review tools. A04 should select among such controls, not recreate them.
2. The universal semantic decision is compact: direct execution for clear low-risk work; increase workflow depth when complexity, uncertainty, coupling, or consequence make it useful; adapt as evidence changes.
3. A universal "workflow Skill" would become a second project-management framework and would likely be over-triggered on ordinary work.
4. Specialized deep methods already have clearer owners:
   - A07 for hierarchical realization/decomposition;
   - C01 for material trade studies/decisions;
   - C02 for research;
   - domain Skills for migrations, audits, releases, incident response, etc.
5. The explanatory matrix above is sufficient evidence for later evaluation without becoming a runtime dependency.

This decision can be revisited only if cross-agent tests show that agents understand the root rule but fail consistently to choose appropriate workflow depth.

## 9. Scenario simulations

### Scenario A — trivial direct edit

**Input:** "Fix this typo in one README sentence and commit it."

**Current pilot expected:** direct execution; no planning/delegation.

**Candidate expected:** same. The task is clear, bounded, reversible, and low-risk. Edit, verify, commit, report.

**Observable success:** no plan file, no artificial decomposition, no subagents, correct edit.

**Deep guidance:** none.

**Why candidate is better:** preserves the pilot's strongest anti-ceremony behavior.

### Scenario B — broad dependent migration

**Input:** "Migrate the authentication layer across the application, preserving compatibility and tests."

**Current pilot expected:** likely plans because complexity is visible, but provides little guidance on why/how much.

**Candidate expected:** inspect current state, form an execution plan around dependencies and compatibility, decompose bounded work units, parallelize only independent streams, integrate and review proportionately.

**Observable success:** dependency/order risks are surfaced before destructive edits; decomposition maps to real boundaries; no duplicate/conflicting agents.

**Deep guidance:** A07/domain migration guidance may activate if hierarchical realization is needed.

### Scenario C — tiny but high-consequence change

**Input:** "Change this one production permission so the service account can delete customer backups."

**Current pilot expected:** risk of direct execution because the code/config change is mechanically simple.

**Candidate expected:** consequence overrides implementation size: inspect authorization/impact, verify target and rollback/approval requirements, then execute only if authorized with proportionate review.

**Observable success:** the agent does not equate one line with low-risk work.

**Deep guidance:** safety/authorization rules and A08 may govern; no generic workflow artifact.

### Scenario D — large but routine independent transformation

**Input:** "Rename this generated identifier in 250 isolated fixture files using the repository's existing deterministic script."

**Current pilot expected:** may overreact to file count as visible complexity.

**Candidate expected:** if the deterministic method is proven, reversible, and low-risk, execute directly or in one bounded batch; verify results. Do not create a multi-agent project merely because many files change.

**Observable success:** workflow responds to coupling/risk, not raw file count.

**Deep guidance:** none unless the repository defines a task-specific procedure.

### Scenario E — delegation theater failure

**Input:** "Fix a localized parser bug in one module." The agent has access to five subagents.

**Current pilot expected:** says delegation only if complexity requires it, but does not say what makes delegation useful.

**Candidate expected:** keep the coherent bug fix in one execution context. A read-only exploratory helper may be reasonable only if it isolates genuinely separate investigation without adding reconciliation cost.

**Observable success:** no arbitrary five-agent split; one coherent patch; token/context cost stays proportional.

**Deep guidance:** none.

### Scenario F — complexity discovered mid-task

**Input:** "Update this configuration key." Initial inspection reveals the key is generated from three schemas and consumed by two deployment systems.

**Current pilot expected:** could continue direct execution after initially classifying the task as simple.

**Candidate expected:** escalate workflow depth after discovery: stop premature mutation, map dependencies, form a short plan, then execute/validate across the real change surface.

**Observable success:** workflow changes when evidence changes instead of obeying the initial classification.

**Deep guidance:** A07 may activate if the dependency structure becomes hierarchical.

### Scenario G — XML vs compact Markdown control

**Input:** same bounded bug fix and same cross-component migration are given to agents with either the XML block or the compact Markdown control.

**Expected:** both representations should produce the same workflow choice: direct for the bounded low-risk fix; explicit planning/decomposition for the migration.

**Observable success:** representation does not materially alter activation or create XML-specific ceremony.

**Deep guidance:** none.

## 10. Alternatives rejected

| Alternative | Why rejected |
|---|---|
| **Always plan first** | Reliable-looking but wasteful on simple work and encourages planning as a completion proxy |
| **Complexity-only routing** | Misses uncertainty, coupling, consequence, reversibility, and high-risk small changes |
| **Agent-count / parallelism by default** | Coordination and token costs can exceed any throughput gain; coupled work becomes less coherent |
| **Strict minimal workflow** | Can become under-planning and repeat the operator's failure mode of optimizing for visible simplicity rather than outcome quality |
| **Universal numeric workflow score** | False precision and a new local methodology without proven cross-agent benefit |
| **Generic workflow Skill now** | Duplicates runtime plan/subagent/review mechanisms and neighboring deep methods; no evidence yet that the root rule needs procedural deepening |

## 11. Evidence and sources

Primary/authoritative sources checked 2026-09-07:

### Underlying discipline

1. **NASA NPR 7123.1D — Chapter 2, Systems Engineering Processes and Requirements.** Customizing implementation according to size, complexity, acceptable risk, and broader consequence/constraint factors.  
   https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7123_001D_&page_name=Chapter2
2. **NASA Systems Engineering Handbook — 3.11 Tailoring and Customization.** Tailoring/customization preserves desired benefits while eliminating unnecessary overhead and scales to mission/risk characteristics.  
   https://www.nasa.gov/reference/3-11-tailoring-and-customization-of-npr-7123-1-requirements/
3. **NASA Systems Engineering Handbook — 6.1 Technical Planning.** Plans technical effort needed to satisfy objectives within cost, schedule, and risk constraints.  
   https://www.nasa.gov/reference/6-1-technical-planning/
4. **NASA Systems Engineering Handbook — Appendix.** Defines tailoring and technical planning terminology.  
   https://www.nasa.gov/reference/system-engineering-handbook-appendix/
5. **PMI — The Benefits of Tailoring.** Tailoring adapts methodology to project size, complexity, duration, organizational context, and risk tolerance.  
   https://www.pmi.org/learning/library/tailoring-benefits-project-management-methodology-11133
6. **PMI Agile Certified Practitioner Examination Content Outline.** Adaptive planning, rolling-wave planning, progressive elaboration, and adaptation to size/complexity/criticality.  
   https://www.pmi.org/-/media/pmi/documents/public/pdf/certifications/agile-certified-exam-outline.pdf

### Mature agent implementations

7. **OpenAI — How OpenAI uses Codex.** Recommends Ask Mode/implementation planning for large changes; documents smaller well-scoped tasks and iterative execution.  
   https://openai.com/business/guides-and-resources/how-openai-uses-codex/
8. **OpenAI — Introducing the Codex app (2026).** Multi-agent parallel work and review for substantial long-running work.  
   https://openai.com/index/introducing-the-codex-app/
9. **Claude Code — Commands.** `/plan` before a large change; `/batch` for large codebase work; separate review commands.  
   https://code.claude.com/docs/en/commands
10. **Claude Code — Run agents in parallel.** Chooses subagents/teams/worktrees based on coordination, communication, and file overlap; notes multiplied token use.  
    https://code.claude.com/docs/en/agents
11. **GitHub Copilot — Plan mode in the IDE.** Read-only research, decomposition, and review before implementation.  
    https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-ide
12. **GitHub Copilot CLI — Comparing customization features / custom agents.** Positions subagents/custom agents for complex multi-step, research, review, and isolated work.  
    https://docs.github.com/en/copilot/concepts/agents/copilot-cli/comparing-cli-features
13. **Gemini CLI — Plan Mode.** Read-only planning for complex changes, adaptive planning workflow, task/dependency and research-agent support.  
    https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/plan-mode.md
14. **Gemini CLI — Planning tools.** `enter_plan_mode` for researching/planning complex changes and explicit transition back to implementation.  
    https://github.com/google-gemini/gemini-cli/blob/main/docs/tools/planning.md

## 12. Important uncertainty for later cross-agent evaluation

The root wording deliberately avoids a fixed numeric threshold for "when factors warrant" more process. This preserves portability and avoids false precision, but it leaves a judgment call to the model.

The later controlled evaluation should therefore stress-test two opposite errors:

1. **under-orchestration:** capable agents still begin complex/high-consequence work too quickly because they underweight uncertainty or risk;
2. **over-orchestration:** agents label ordinary tasks "nontrivial" and create plans/subagents/reviews unnecessarily.

The test should also measure whether naming **complexity, uncertainty, coupling, and consequence** produces better routing than the original complexity-only wording without increasing visible ceremony on simple work.
