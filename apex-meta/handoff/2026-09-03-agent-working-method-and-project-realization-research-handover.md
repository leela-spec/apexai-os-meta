---
type: Handover
title: Agent Working Method and Project Realization — Research Continuation Handover
description: Research launcher for selecting an established, AI-legible, complexity-adaptive working method that combines intake/understanding, hierarchical specification and realization, iterative verification/validation, project-management integration, and progressive-disclosure agent instructions without inventing a new Apex methodology.
status: research_handover_no_implementation_authorized
created: 2026-09-03
repository: leela-spec/apexai-os-meta
branch: main
basis_commit_at_handover_start: b9d7a77c1b84aaed99093e42cea32a7d51c56f26
---

# Agent Working Method and Project Realization — Research Continuation Handover

## 0. Start here

This handover launches a **research and architecture-selection task**, not an implementation task.

The operator wants one consistent way for Apex agents to understand, decompose, execute, verify, iterate, and manage work. The critical constraint is that this method should use **existing, widely recognized vocabulary and established systems wherever possible**. Do not create a novel Apex vocabulary when a mature systems-engineering, project-management, software-development, or agentic-workflow term already exists.

The reason is practical: every locally invented concept creates another inference burden for an LLM. The preferred architecture should let an agent recognize most of the method from established terminology, with Apex-specific adaptation kept as thin as possible.

Do **not** implement or patch live agent files from this handover. Research first, produce a decision-ready design, simulate it, and identify exact patch targets. The current post-W2 patch packs remain proposed/not-applied unless separately authorized.

---

# 1. Operator intent — preserve exactly

The operator wants a general working method with these properties:

1. **Known vocabulary first.** Use established methods, standards, and agent frameworks so the model does not have to infer a bespoke mental model.
2. **Very small always-on instruction surface.** The general agent instruction should be extremely short and token-efficient.
3. **Progressive disclosure.** The short instruction should route to a small method file/Skill only when the task needs it; deeper details should be further referenced rather than always loaded.
4. **Complexity-adaptive execution.** The method must scale without forcing ceremony onto trivial work:
   - simple/bounded task → execute directly in one session;
   - moderately complex task → structured top-down definition followed by bottom-up verification;
   - very complex/long-horizon task → multiple bounded iterations, durable artifacts/checkpoints, and possibly recursive decomposition/sub-specs, patch cycles, or scoped worker contexts.
5. **Understanding before execution.** For nontrivial requests, the agent should establish and expose what it understood before it starts changing things. The operator's desired pre-execution view includes at least:
   - input / evidence supplied;
   - actual task / intended outcome;
   - scope and boundaries;
   - sub-tasks or decomposition;
   - iterative realization process;
   - expected deliverable/output format;
   - rough output structure/content map;
   - dependencies/interdependencies;
   - sources the agent intends to use;
   - material ambiguity or missing information.
6. **Top-down then bottom-up.** The operator's existing mental model is Macro → Meso → Micro on the way down, then Micro → Meso → Macro on the way back up.
7. **Project-management integration.** The method must not be a prompt trick detached from project state. It must map cleanly into project/epic/module/task artifacts, dependencies, status, evidence, and the current Plan-Sync-Session backbone.
8. **Agent-management integration.** Agent files should reference the shared method rather than duplicate it. Specialist agents add domain-specific behavior; they should not each invent their own planning/execution lifecycle.
9. **Informatics compatibility.** The design must conform to the current Apex informatics architecture: small current-truth entrypoints, one owner per concept, refs rather than copies, context-budget discipline, and on-demand loading.
10. **No framework cosplay.** If an external method only partially fits, say exactly which part fits. Do not claim that a local composition is a formal standard.

---

# 2. The operator's Macro / Meso / Micro semantics

Do not confuse this with the repository's existing Weekly files that happen to use the same labels.

The operator means a **general hierarchical realization method** for any sufficiently complex target: project, feature, content system, research program, event, architecture, process, or other goal.

| Layer | Operator meaning | Primary question | Expected content |
|---|---|---|---|
| **Macro** | Strategic / system layer | Why? What is the target as a whole? | purpose, intended value, success, environment, system boundary, stakeholders, external relationships, major modules/capabilities, cross-cutting constraints, interdependencies, strategic rationale |
| **Meso** | Tactical / architecture layer | How is the target organized and realized? | modules/sub-targets, responsibilities, interfaces, dependencies, sequence, coordination, shared constraints, how modules jointly satisfy Macro intent |
| **Micro** | Operational / realization layer | What exactly must be defined/built/done? | detailed design/specification, exact tasks, code/content/configuration, tests, acceptance conditions, implementation evidence |

The critical behavior is not merely three document sizes. It is a **closed hierarchical loop**:

```text
Macro definition / system intent
        ↓ decompose / allocate / derive
Meso architecture / modules
        ↓ check against Macro before descending
Micro specification / implementation
        ↓ execute + verify
Micro evidence
        ↑ integrate / verify module realization
Meso correction + integration validation
        ↑ validate realized target against system intent
Macro correction / validation
        ↺ iterate when evidence invalidates assumptions
```

For complex targets, a Meso module may itself become a recursively decomposed target.

This semantic definition is a requirement for the research. The next agent may recommend **different external terms** for implementation if they are better known to LLMs, but it must preserve the behavior above.

---

# 3. Important correction to earlier Apex work

The previous post-W2 verification mostly treated Macro/Meso/Micro as a **terminology-collision problem**. That work did not formalize the operator's general realization method.

Current proposed patch:

`apex-meta/SmallSkills/OKF_Format/adoption-project/post-w2-verification/PATCH-04-terminology-and-ambiguity.md`

contains logic that namespaces Macro/Meso/Micro to Weekly and removes Macro/Meso shorthand from some live role descriptions. **Do not apply those Macro/Meso/Micro blocks until this research resolves whether Apex should adopt a general hierarchical realization vocabulary or aliases.**

The current Weekly artifacts are also not implementations of the operator's intended method:

- `apex-meta/kb/Weekly-Orchestrator/architecture/01-macro-architecture-decision.md` is mainly an orchestration-topology decision record.
- `apex-meta/kb/Weekly-Orchestrator/architecture/02-meso-file-map.md` is mainly an execution/file/write-surface map.
- `apex-meta/kb/Weekly-Orchestrator/architecture/03-execution-trace-verification.md` is explicitly historical verification evidence, not a live Micro implementation layer.

Do not retrofit those files merely to preserve labels. First choose the method; then decide whether those historical Weekly labels should be renamed/reclassified.

---

# 4. Current Apex substrate already available

The next session does not need to rebuild the whole agent architecture.

## 4.1 Compact routing already exists

`AGENTS.md` currently establishes directness, scope discipline, current-truth discipline, Informatics routing, Apex KB routing, and patch safety. It explicitly says simple operations should take the shortest correct path rather than accumulate workflow ceremony.

`.claude/CLAUDE.md` is already a compact project activation/router. It states that detailed instructions should be loaded only from the entrypoint selected by operator intent and that agents should read only the active entrypoint plus the state/packets/references needed for the request.

This is compatible with the operator's desired **short global rule → on-demand method detail** pattern.

## 4.2 Informatics already provides the information architecture

Canonical entrypoint:

`apex-meta/informatics/index.md`

Current package already defines progressive disclosure, one-owner/refs-not-copies principles, and scoped knowledge/instruction surfaces. Do not create a second documentation architecture for the new working method.

## 4.3 Prior agent/skill research already reached useful conclusions

Read before duplicating research:

- `apex-meta/handoff/agent-skill-system-research/best-practice-report.md`
- `apex-meta/handoff/agent-skill-system-research/design-lock-qa.md`

That research already found, from current Anthropic/MCP guidance and Apex evidence:

- default to fixed workflows for repeatable known procedures;
- use open-ended agents only where the path genuinely requires model-directed branching;
- keep a small stable role set;
- use Skills for reusable procedures;
- use progressive disclosure (metadata → Skill body → referenced resources);
- keep subagents ephemeral/task-scoped and context-isolated;
- use just-in-time retrieval and the smallest sufficient context;
- persist structured handoffs/state rather than relying on conversational memory;
- preserve deterministic computation vs semantic judgment boundaries;
- gate consequential durable mutations.

The new work should extend this, not restart the agents-vs-skills debate from zero.

## 4.4 Current project-management backbone

`.claude/CLAUDE.md` defines the shared Plan-Sync-Session backbone:

- `apex-plan` — proposal and decomposition;
- `apex-sync` — deterministic computation/read-side reports;
- `apex-session` — confirmed mutation, handoff, closure.

The new method must determine how established specification/decomposition/verification artifacts map into this backbone **without silently creating a competing state system**.

---

# 5. Preliminary external research — strongest findings so far

These are starting findings, not final architectural decisions. Verify current versions and primary sources in the continuation session.

## 5.1 GitHub Spec Kit / Agentic Spec-Driven Development — strongest existing agentic match so far

Primary project:

- https://github.com/github/spec-kit
- https://github.github.com/spec-kit/

As of August 2026, Spec Kit is a mature, actively maintained GitHub project for **Spec-Driven Development (SDD)** and broader agentic processes. Its documentation explicitly says it can guide an agent through an SDLC **or another business process**, and it supports many coding-agent integrations.

Core lifecycle:

```text
constitution
  → specify
  → clarify
  → plan
  → checklist
  → tasks
  → analyze
  → implement
  → converge
```

Relevant behavior:

- `constitution` defines governing principles/constraints.
- `specify` defines what/why, requirements, user scenarios, and success criteria.
- `clarify` resolves underspecified areas before planning.
- `plan` translates requirements into architecture/technical approach.
- `tasks` creates dependency-ordered actionable work.
- `analyze` checks cross-artifact consistency/coverage before implementation.
- `implement` executes dependency-ordered tasks.
- `converge` checks implementation against spec/plan/tasks, appends missing work, and supports repeated implement → converge cycles until no gaps remain.

Important current sources:

- Core overview: https://github.com/github/spec-kit/blob/main/docs/index.md
- Agentic SDD lifecycle: https://github.com/github/spec-kit/blob/main/docs/reference/agentic-sdd.md
- Lean workflow: https://github.com/github/spec-kit/blob/main/presets/lean/README.md
- Handling complex features: https://github.com/github/spec-kit/blob/main/docs/concepts/complex-features.md
- Spec of Specs: https://github.com/github/spec-kit/blob/main/docs/concepts/spec-of-specs.md
- Convergence semantics: https://github.com/github/spec-kit/blob/main/templates/commands/converge.md

### Why it is unusually relevant to the operator's complexity requirement

Spec Kit already documents a graduated response to context/task size:

1. **Normal/smaller feature:** one standard specify → plan → tasks → implement cycle.
2. **Large feature:** scope each implementation run to a phase or bounded task range and verify before continuing.
3. **Subagent-capable runtime:** delegate bounded tasks so each worker receives focused context rather than the whole feature.
4. **Very large feature:** use **spec-of-specs** — one roadmap pass decomposes the epic into independently specifiable slices; each slice gets its own spec/plan/tasks/implement cycle.
5. **Recursive case:** if one slice is still too large, give it its own roadmap and decompose again.

This is extremely close to the operator's desired "simple → one cycle; complex → hierarchical cycle; very complex → several bounded recursive cycles" requirement and should be studied before inventing an Apex-specific complexity taxonomy.

### Spec-of-specs details especially worth reusing or comparing

Spec Kit's current roadmap artifact records:

- stable ID;
- sub-feature name;
- intent;
- explicit scope boundary;
- dependencies;
- status;
- link to sub-spec.

It requires bidirectional linkage between roadmap entry and sub-spec, and explicitly frames this as traceability plus context control.

That maps closely to the operator's desired Macro/Meso relationship, but do not force a 1:1 mapping until the full semantics are compared.

## 5.2 Spec Kit `assess` extension — candidate upstream intake/discovery pattern

Current primary source:

https://github.com/github/spec-kit/blob/main/extensions/assess/README.md

In July 2026 Spec Kit added a bundled **Idea Assessment Pipeline** ahead of SDD:

```text
intake → research → define → shape → decide
                              ↓
                   go / clarify / kill
```

It writes separate durable Markdown artifacts for intake, evidence, problem definition, concept shaping, and decision. A `go` result hands the idea to `specify`.

This is relevant to high-uncertainty/high-impact work, but probably **too heavy to run before every ordinary task**. Evaluate it as an optional discovery/assessment mode, not as the universal preflight by default.

## 5.3 Kiro Specs / Quick Spec — strong vendor implementation of adaptive planning

Primary docs:

- https://kiro.dev/docs/cli/v3/specs/
- https://kiro.dev/docs/specs/quick-spec/
- https://kiro.dev/docs/steering/

Current Kiro Spec flow:

```text
Requirements → Design → Tasks → Execution
```

Kiro documents verification between execution steps. It also has distinct modes:

- **Quick Spec:** asks clarifying questions up front, then generates requirements/design/tasks in one pass without gates.
- **Full Spec:** structured requirements/design/tasks with review/approval gates between phases.
- **Bug Fix:** investigation/root cause → fix design → implementation tasks.

Kiro steering is also relevant to token-efficient rule architecture:

- always-on project steering for foundational context;
- conditional/auto-included steering for context-heavy guidance;
- AGENTS.md support;
- custom agents can explicitly list steering resources.

Kiro's implementation is useful corroboration that **complexity-adaptive structured planning plus conditional instruction loading is already a productized agent pattern**.

## 5.4 Systems Engineering Vee / requirements flowdown / V&V — strongest formal basis for Macro→Meso→Micro→Meso→Macro

Primary NASA sources:

- NASA Systems Engineering Handbook: https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf
- NASA software requirements decomposition/flowdown guidance: https://swehb.nasa.gov/spaces/7150/pages/16449651/SWE-050%2B-%2BSoftware%2BRequirements
- NASA Systems Modeling Handbook (NASA-HDBK-1009A, 2025): https://standards.nasa.gov/standard/NASA/NASA-HDBK-1009

Key established concepts:

- hierarchical decomposition and allocation of higher-level requirements to elements/subsystems/components;
- derived requirements at each level should be validated against parent/stakeholder expectations before further decomposition;
- traceability continues to the lowest design level;
- the Vee descends through decomposition/definition and ascends through integration/verification;
- **verification** asks whether the realized product complies with specification;
- **validation** asks whether the system actually accomplishes its intended purpose.

This is the closest formal external model to the operator's top-down/bottom-up loop. The continuation session should determine whether Apex should describe its general method using **systems-engineering vocabulary directly** rather than asking agents to learn Macro/Meso/Micro as primary terms.

## 5.5 Work Breakdown Structure (WBS) — established hierarchical project decomposition

Primary PMI references:

- https://www.pmi.org/standards/work-breakdown-structures-third-edition
- https://www.pmi.org/learning/library/practice-standard-work-breakdown-structures-8063

Useful established concepts:

- deliverable-oriented hierarchical decomposition;
- each descending level increases detail;
- lowest manageable units are work packages;
- the **100% rule**: child scope accounts for all and only the parent scope;
- WBS supports project planning, scheduling, risk, performance, and control.

WBS is useful for project/task decomposition and completeness, but it does **not by itself** provide the operator's strategic/system layer or bottom-up V&V loop. Treat it as a possible Meso→Micro decomposition primitive, not the whole methodology.

## 5.6 Hierarchical Task Network (HTN) planning — established AI planning vocabulary

Foundational reference:

Erol, Hendler, Nau — *UMCP: A Sound and Complete Procedure for Hierarchical Task-Network Planning*:
https://www.cs.umd.edu/~nau/papers/erol1994umcp.pdf

HTN planning formalizes decomposition of compound tasks into progressively more concrete subtasks until executable/primitive tasks are reached.

This is useful because it is native **AI planning vocabulary**, but it is task-centric. It does not supply strategic intent, architecture, or V&V by itself. Evaluate whether HTN terminology improves agent comprehension of decomposition or merely adds another framework the system does not need.

## 5.7 Agent Skills specification — direct fit for progressive disclosure

Primary specification:

https://agentskills.io/specification

The Agent Skills specification explicitly defines progressive disclosure:

1. skill metadata (`name`, `description`) loaded broadly;
2. `SKILL.md` body loaded only when activated;
3. referenced resources/scripts/assets loaded only when required.

The spec recommends keeping detailed references focused and on demand. This directly supports the operator's desired architecture:

```text
very short always-on rule
  → method Skill / short procedure
    → detailed references only for the active phase
```

Do not duplicate method details across every agent file if this mechanism can centralize them.

## 5.8 SIPOC+CM / IDEF0 — possible vocabulary for the pre-execution understanding frame

These are **candidates to evaluate**, not recommendations yet.

ASQ SIPOC+CM:
https://asq.org/quality-resources/sipoc

SIPOC+CM captures Suppliers, Inputs, Process, Outputs, Customers, Constraints, and Measures as a concise high-level process frame before detailed flow design.

IDEF0 / ICOM:
- NIST FIPS 183 historical publication: https://www.govinfo.gov/app/details/GOVPUB-C13-ba43579ec72306f00c01305771ffdf3b
- Current NIST example/navigation material: https://pages.nist.gov/circular-economy-manufacturing-models/instructions.html

IDEF0 frames an activity through Inputs, Controls, Outputs, and Mechanisms and supports hierarchical decomposition.

These may help name parts of the operator's desired "what did you receive / what controls apply / what will you produce / how will you do it" preflight. They do not obviously cover sources, acceptance criteria, task breakdown, or agent-context strategy. Do not add either unless it genuinely reduces local invention.

## 5.9 Self-Refine / Reflexion — evidence for iterative feedback, not a governance standard

Research:

- Self-Refine: https://papers.nips.cc/paper/2023/hash/91edff07232fb1b55a505a9e9f6c0ff3-Abstract-Conference.html
- Reflexion: https://papers.nips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html

These demonstrate that language-model outputs can improve through explicit feedback/refinement cycles and that feedback from prior trials can guide subsequent agent behavior.

Use them only as supporting evidence for iterative review/refinement. They are research frameworks, not the primary project-management or specification standard Apex should adopt.

## 5.10 Current OpenAI model guidance supports lean global prompts

Current OpenAI model guidance states that leaner prompts can improve performance and reduce token use, recommends stating each instruction once, exposing only relevant tools, and defining success criteria/stopping rules for complex workflows.

Source:
https://developers.openai.com/api/docs/guides/latest-model

This reinforces the operator's architecture objective: **small global contract + task-conditioned detail**, not a monolithic master agent prompt.

---

# 6. Strongest synthesis hypothesis to test — not yet a decision

The emerging evidence suggests Apex may not need a new "Macro/Meso/Micro framework" as its primary machine vocabulary at all.

A likely solution is a **thin composition of established concepts**, for example:

```text
Agent instruction / progressive disclosure
  Agent Skills + AGENTS.md / scoped rules

Task intake / readiness
  requirements elicitation / clarify / acceptance criteria
  optional assessment for high-uncertainty ideas

Delivery lifecycle
  Spec-Driven Development:
  Specify → Plan → Tasks → Implement → Converge

Hierarchy / large-target handling
  systems decomposition + WBS / roadmap / spec-of-specs

Top-down / bottom-up integrity
  Systems Engineering Vee
  requirements flowdown + bidirectional traceability
  verification + validation

Iteration
  bounded implement → verify/converge cycles
  recurse into sub-specs only when task/context size requires it
```

Under that model, the operator's Macro/Meso/Micro terms could remain a **human-friendly alias** rather than a new set of instructions the model must learn:

```text
Macro ≈ system/problem/specification intent and parent requirements
Meso  ≈ architecture/plan/module decomposition and interfaces
Micro ≈ tasks/implementation/verification evidence
```

But this mapping is imperfect and must be tested. In particular:

- Spec Kit `specify` often describes what/why, while the operator's Macro also includes environment, major module relationships, and system constraints.
- Spec Kit `plan` combines architecture and implementation planning; the operator's Meso is specifically module architecture/how.
- WBS defines the "what" of project scope rather than the operator's why/how/what mnemonic.
- Systems engineering uses multiple hierarchy levels rather than exactly three.

Therefore do **not** simply rename Spec Kit artifacts Macro/Meso/Micro. Determine whether aliases help the operator without degrading AI comprehension.

---

# 7. Critical research question: can an existing method cover the whole system?

The next agent must explicitly test three alternatives:

## Option family A — adopt one existing agentic framework almost directly

Primary candidate: GitHub Spec Kit, possibly with selected core/Lean/assess patterns.

Question: Can Spec Kit's current lifecycle, complexity handling, roadmap recursion, and convergence already satisfy most requirements with only a thin Apex integration layer?

Pros to test:
- established agent-facing commands/files;
- multi-agent integration ecosystem;
- explicit artifact chain;
- current handling of context exhaustion/complex features;
- explicit convergence loop;
- existing lightweight vs full modes.

Risks to test:
- coding/feature bias despite broader stated positioning;
- documentation proliferation;
- overlap/conflict with Apex Plan-Sync-Session;
- constitution might duplicate AGENTS/informatics authority;
- current Spec Kit multi-feature/project coordination may still be weaker than Apex project management.

## Option family B — use standards vocabulary but keep an Apex-native thin workflow

Example basis:
- requirements elicitation;
- Spec/Plan/Tasks;
- Systems Engineering Vee;
- WBS/traceability;
- Agent Skills progressive disclosure.

Question: Is a very small local adapter more resilient than importing Spec Kit's file/runtime conventions?

Constraint: this is acceptable only if the local layer is genuinely thin and mostly established vocabulary, not a renamed bespoke framework.

## Option family C — hybrid

Use Spec Kit/SDD artifact semantics for bounded delivery, Systems Engineering Vee for hierarchical V&V, Agent Skills for instruction loading, and Apex Plan-Sync-Session for durable project state/mutation.

This is currently the strongest hypothesis, but it must be tested for concept duplication and cognitive load.

---

# 8. The pre-execution understanding step must be researched separately

The operator wants a deliberate iteration **before execution** for nontrivial prompts.

Do not immediately invent `TASK-BRIEF.md` or another schema. First determine whether a recognized artifact/process already fits.

Research at least:

- Spec Kit `clarify` and the `assess` intake/define stages;
- Kiro Quick Spec's up-front clarifying questions;
- requirements elicitation / requirements analysis;
- acceptance criteria and readiness concepts;
- project charter / statement-of-work / execution-plan patterns where useful;
- SIPOC+CM / IDEF0 only if they improve the field vocabulary.

The desired visible preflight should probably communicate some compact subset of:

```text
Intent / outcome
Inputs / evidence
Scope / non-goals
Deliverables + output structure
Acceptance criteria
Dependencies / constraints
Sources / authority plan
Execution phases / decomposition
Unknowns / assumptions
```

But the research should determine the smallest established vocabulary that gives the operator the correction opportunity he wants.

### Complexity interaction to solve

A universal visible preflight would conflict with current Apex **Directness** for trivial tasks. The target design should likely have a complexity/readiness threshold such as:

- trivial, bounded, reversible → execute directly;
- nontrivial but familiar → compact preflight + one structured cycle;
- complex/high-impact/ambiguous → explicit preflight/specification before mutation;
- very large → roadmap/sub-spec cycles.

Do not hard-code arbitrary numeric complexity scores unless an established framework or empirical evaluation justifies them.

---

# 9. Project-management integration questions

This is not complete until it maps into durable project state.

The next session must inspect, minimally and only as needed:

- `.claude/skills/apex-plan/SKILL.md`
- `.claude/skills/apex-sync/SKILL.md`
- `.claude/skills/apex-session/SKILL.md`
- relevant shared schemas referenced by those Skills
- `apex-meta/orchestration/00-START-HERE.md`
- `apex-meta/orchestration/ARCHITECTURE.md`
- `apex-meta/orchestration/GLOSSARY.md`
- current project/task record formats only where needed for mapping.

Answer at least:

1. Does `apex-plan` become the owner of specification/decomposition artifacts, or only consume them?
2. Where should roadmap/spec/module/task parent-child relations live?
3. Can `apex-sync` compute readiness, dependency availability, drift, and next-action reports from those relations?
4. Does `apex-session` remain the sole confirmed durable project/task mutation path?
5. How are specification/plan/tasks linked to project/epic/task records without duplicating source of truth?
6. What is the smallest traceability relation set needed? Candidate established relations include `derives from`, `depends on`, `satisfies`, `implements`, `verifies`, and `validated by`.
7. Can large projects use recursive roadmaps/sub-specs without forcing every small task into an epic hierarchy?
8. How does evidence from Micro/implementation propagate back to module/plan and system/spec without rewriting history or losing current truth?

Do not add another state machine if Plan-Sync-Session already provides the necessary proposal/computation/confirmed-mutation boundaries.

---

# 10. Agent architecture questions

The operator plans further agent reorganization. The working method must be separable from role/domain identity.

Research/design target:

```text
AGENTS / compact client router
  └─ one tiny general working-method rule
       └─ shared method Skill / short reference
            ├─ intake/readiness detail when needed
            ├─ specification/decomposition detail when needed
            ├─ implementation/V&V detail when needed
            └─ complex/recursive-work detail when needed

specialist agent
  ├─ role/domain responsibility
  ├─ allowed tools / mutation bounds
  └─ references shared working method rather than copying it
```

Questions:

1. Should the general method be an Agent Skill, a canonical method document, or both (small Skill front door + canonical references)?
2. Which parts must be cross-client in `AGENTS.md`, and which can remain runtime-specific?
3. Can the same method be exposed to Claude, Codex, Kiro, Cursor, Copilot, etc. through Agent Skills or client adapters without duplicating semantics?
4. What exact content must always be loaded vs auto/conditional vs manual?
5. Should a complexity classifier be a deterministic rule, LLM judgment with examples, or simply route based on obvious task properties?
6. When should a subagent be used because of context pollution, and when should the same session continue?
7. How do specialists receive only the relevant parent requirements/module slice rather than the whole project?

Prior research strongly supports workflow-first + ephemeral scoped workers + Skills/progressive disclosure. Do not revert to a large permanent agent roster without new evidence.

---

# 11. Informatics integration

The selected working method must conform to `apex-meta/informatics/` rather than creating another parallel information-design doctrine.

Check:

- one owner per concept;
- refs not copies;
- short index/entrypoint;
- current truth separate from history/evidence;
- concept/task/reference separation where useful;
- explicit source authority;
- no duplicated glossary authority;
- smallest sufficient context;
- detail loaded only when required.

The working method is a **process/realization contract**, not a replacement for Informatics. Informatics governs how durable knowledge/instruction artifacts are structured and retrieved; the working method governs how work moves from intent to realization and verification.

---

# 12. Evaluation rubric for candidate methods

Score each serious candidate/composition 1–5 and explain evidence. Do not score unsupported cells from intuition alone.

| Dimension | Weight | What good looks like |
|---|---:|---|
| Existing AI-legible vocabulary / adoption | 15% | LLMs and agent tools are likely to recognize the terms without a long local explanation |
| Covers operator's top-down + bottom-up semantics | 15% | Intent → architecture/decomposition → implementation → verification/integration → validation |
| Complexity adaptivity | 12% | Lightweight for simple work, scalable/recursive for long-horizon work |
| Progressive disclosure / token efficiency | 12% | Tiny always-on rule, task-conditioned deeper context |
| Durable artifacts + traceability | 10% | Parent-child/dependency/requirement/evidence relationships survive sessions |
| Project-management compatibility | 10% | Integrates with project/epic/task state, dependencies, status, ownership |
| Cross-agent/client portability | 8% | Not locked to one proprietary UI/runtime; adapters are thin |
| Verification/validation rigor | 8% | Explicit acceptance, consistency checks, convergence, system-level validation |
| Non-code/general-target applicability | 5% | Works beyond software features without distorting the method |
| Implementation cost / conceptual duplication | 5% | Reuses Apex substrate, avoids another governance stack |

Hard failure conditions:

- requires a long bespoke explanation in every agent prompt;
- duplicates Plan-Sync-Session mutation authority;
- forces heavyweight artifacts for trivial tasks;
- loses parent intent during lower-level execution;
- no bottom-up evidence/validation path;
- loads whole-project context by default;
- requires invented relations where established ones suffice;
- conflates verification, validation, approval, and durable mutation.

---

# 13. Required web-research method

Use current web research. Do not rely on model memory for agent-framework capabilities or current file formats.

Priority:

1. formal/primary standards and original documentation;
2. official maintained vendor/project documentation;
3. original academic papers for agent/reasoning methods;
4. secondary comparisons only to corroborate operational experience.

Research at minimum:

- GitHub Spec Kit current core, Lean, assess, complex-features, spec-of-specs, converge, and integrations;
- Kiro current Specs, Quick Spec, Steering, and custom-agent resource inclusion;
- NASA/INCOSE/SEBoK or equivalent primary systems-engineering sources for decomposition, Vee, V&V, traceability;
- PMI WBS current standard/official guidance;
- Agent Skills specification and current client implementations;
- current OpenAI/Anthropic guidance on lean instructions, planning, context engineering, scoped workers, evaluation loops;
- HTN only to test whether it adds material value;
- intake/readiness vocabulary (requirements elicitation, readiness, SIPOC/IDEF0 if relevant).

Explicitly distinguish:

- formal standard;
- established engineering method;
- vendor workflow/product implementation;
- academic agent technique;
- local Apex adaptation.

---

# 14. Research process — context discipline

Do not load the whole repository.

Use this iterative sequence:

```text
1. External landscape + vocabulary map
2. Candidate shortlist
3. Minimal repo read for integration point A
4. Map candidate to live Apex contracts
5. Identify conflicts/duplication
6. Simulate representative requests
7. Refine architecture
8. Produce decision artifacts + patch plan
```

For each step:

- load only files required for that question;
- preserve source/provenance;
- write concise evidence notes rather than keeping large source bodies in context;
- prefer direct links to source documents over copied prose;
- do not turn the primary continuation chat into a historical archive.

---

# 15. Required request simulations

Before recommending implementation, simulate at least these cases against the candidate method.

## S1 — trivial/direct

> "Rename this heading and fix the typo."

Expected property: no multi-file spec ceremony; direct execution after confirming exact target.

## S2 — bounded but nontrivial

> "Add a new validation rule to this existing script and tests."

Expected property: compact understanding/readiness step; spec/plan can be one bounded cycle; implementation and verification in same session if context permits.

## S3 — medium feature

> "Add a new project-status capability touching state schema, computation, and UI output."

Expected property: clear intent/spec → architecture/modules → dependency-ordered tasks → implementation → verification/convergence, with parent traceability.

## S4 — large cross-cutting program

> "Reorganize the Apex agent architecture and working method across runtimes."

Expected property: roadmap/spec-of-specs or equivalent; independent slices; stable IDs; dependencies; each slice gets bounded context; top-level intent remains traceable.

## S5 — ambiguous request

> "Improve the project principles and Meso design."

Expected property: identify ambiguous artifact/terminology before execution; expose understanding and ask only consequential clarification.

## S6 — research/content target, not software

> "Design a multi-stage event concept and execution plan."

Expected property: method still works without pretending everything is source code.

## S7 — implementation reveals wrong architecture

> A Micro/task implementation test shows a module assumption is false.

Expected property: evidence propagates upward; module/plan is corrected; system/spec is revalidated if impact crosses its constraints; no silent local workaround that violates parent intent.

## S8 — long context

> A sub-feature cannot fit safely into one implementation context.

Expected property: scoped phases/tasks, optional subagent isolation, or recursive sub-spec; durable progress makes continuation deterministic.

---

# 16. Required deliverables from the continuation session

Do not stop at a generic research essay.

Produce:

## A. Decision-ready method comparison

- evidence-backed candidate table;
- explicit winner or smallest composition;
- what is reused unchanged vs adapted;
- what should **not** be adopted.

## B. Canonical vocabulary map

A table similar to:

| Operator concept | Preferred established term | External source/method | Keep operator alias? | Notes |
|---|---|---|---|---|
| Macro | TBD | systems engineering / SDD | TBD | ... |
| Meso | TBD | architecture/plan/decomposition | TBD | ... |
| Micro | TBD | tasks/implementation/V&V | TBD | ... |
| top-down | requirements flowdown/decomposition | NASA SE | likely | ... |
| bottom-up | integration/verification/validation | Vee | likely | ... |

Do not force one-to-one terminology where it is misleading.

## C. Complexity-routing design

Define the minimum recognizable modes, ideally using existing framework terms rather than local labels.

For each mode specify:

- trigger;
- artifact depth;
- whether visible preflight is needed;
- whether operator gate is needed;
- whether execution can finish in one session;
- when to scope by phase/task;
- when to recurse into sub-specs/roadmaps;
- when to use a worker/subagent.

## D. Pre-execution understanding contract

Recommend the smallest established/portable form that gives the operator a chance to correct the agent's understanding before consequential execution.

Show:

- minimal fields;
- 1 compact example;
- which tasks skip it;
- which tasks require it;
- whether it is chat-only, durable artifact, or both.

## E. Progressive-disclosure file/Skill architecture

Show exact proposed responsibility boundaries, for example conceptually:

```text
always-on router
  → shared working-method Skill
       → intake/readiness reference
       → specification/planning reference
       → complex-feature/decomposition reference
       → verification/validation/convergence reference
```

Use actual recommended client mechanisms after research. Keep the always-on text demonstrably small.

## F. Candidate short global instruction

Draft 1–3 very short options for the always-on agent rule. Each must be grounded in the chosen external method(s), not free invention.

A research target, **not approved wording**, is something like:

> Use the lightest suitable delivery mode. Execute trivial bounded work directly. For nontrivial work, establish intent/acceptance, then follow specification → plan/decomposition → tasks → implementation → verification/convergence with traceability to parent intent. Scope large work into bounded or recursive sub-specs. Load process detail only when that mode is active.

The continuation agent must improve or reject this based on evidence.

## G. Apex integration map

Map the selected method to:

- `AGENTS.md` / cross-client compact rule;
- `.claude/CLAUDE.md` router;
- shared Skill(s)/references;
- Informatics standard;
- `apex-plan`;
- `apex-sync`;
- `apex-session`;
- Multi-Agent Orchestration roles;
- Weekly Orchestrator only where genuinely relevant;
- project/epic/task artifacts.

Identify one owner for each concept.

## H. Patch plan only

Identify exact files that would need change and why.

Do **not** apply production patches unless separately authorized.

If later patch authoring is requested, follow the repository's exact-match patch discipline and re-read live targets first.

## I. Verification/evaluation plan

Provide deterministic/static checks where possible plus representative agent simulations to test:

- trigger accuracy;
- context loaded;
- correct complexity mode;
- parent-child traceability;
- preflight usefulness;
- convergence behavior;
- false ceremony on trivial tasks;
- cross-client drift;
- token/context cost.

---

# 17. Important non-goals

Do not:

- invent a formal-sounding "Apex Macro-Meso-Micro Standard" before comparing existing systems;
- create a new `PROJECT-PRINCIPLES.md` merely because Spec Kit has a constitution;
- duplicate `AGENTS.md`, `.claude/CLAUDE.md`, Informatics, or Plan-Sync-Session authority;
- replace all current project-management artifacts with Spec Kit files without migration analysis;
- assume a software-only lifecycle is sufficient for research/content/business targets;
- add RAG/vector retrieval; this task is instruction/process architecture;
- normalize all cross-client Skill mirrors in the same change;
- delete root `CLAUDE.md` or other runtime compatibility surfaces without runtime evidence;
- treat academic LLM loops as production standards merely because they have a paper;
- force all work through multi-agent orchestration;
- require visible planning chatter for a trivial bounded action.

---

# 18. Known high-value tension to resolve

The final design must reconcile **two legitimate principles** already present in Apex:

### Directness

Simple, bounded work should take the shortest correct path. Process must not replace delivery.

### Deliberate understanding and traceability

Nontrivial work should not begin from a fuzzy prompt and allow the model to invent scope, architecture, dependencies, or output shape mid-execution.

The solution should therefore be **adaptive**, not universally heavy or universally direct.

A good final architecture will make the escalation path obvious to the model using familiar terms rather than an elaborate local scoring system.

---

# 19. Source manifest for the continuation agent

## Apex current truth / prior research

- `AGENTS.md`
- `.claude/CLAUDE.md`
- `apex-meta/informatics/index.md`
- `apex-meta/informatics/standard.md` — only sections needed for instruction/progressive-disclosure integration
- `apex-meta/handoff/agent-skill-system-research/best-practice-report.md`
- `apex-meta/handoff/agent-skill-system-research/design-lock-qa.md`
- `apex-meta/SmallSkills/OKF_Format/adoption-project/post-w2-verification/00-verification-report.md`
- `apex-meta/SmallSkills/OKF_Format/adoption-project/post-w2-verification/PATCH-04-terminology-and-ambiguity.md`
- `apex-meta/SmallSkills/OKF_Format/adoption-project/post-w2-verification/99-completion-index.md`
- `.claude/skills/apex-plan/SKILL.md`
- `.claude/skills/apex-sync/SKILL.md`
- `.claude/skills/apex-session/SKILL.md`
- `apex-meta/orchestration/00-START-HERE.md`
- `apex-meta/orchestration/ARCHITECTURE.md`
- `apex-meta/orchestration/GLOSSARY.md`

Load additional repository files only when a concrete integration question requires them.

## External starting sources

### GitHub Spec Kit
- https://github.com/github/spec-kit/blob/main/docs/index.md
- https://github.com/github/spec-kit/blob/main/docs/reference/agentic-sdd.md
- https://github.com/github/spec-kit/blob/main/presets/lean/README.md
- https://github.com/github/spec-kit/blob/main/docs/concepts/complex-features.md
- https://github.com/github/spec-kit/blob/main/docs/concepts/spec-of-specs.md
- https://github.com/github/spec-kit/blob/main/templates/commands/converge.md
- https://github.com/github/spec-kit/blob/main/extensions/assess/README.md

### Kiro
- https://kiro.dev/docs/cli/v3/specs/
- https://kiro.dev/docs/specs/quick-spec/
- https://kiro.dev/docs/steering/

### Systems engineering
- https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf
- https://swehb.nasa.gov/spaces/7150/pages/16449651/SWE-050%2B-%2BSoftware%2BRequirements
- https://standards.nasa.gov/standard/NASA/NASA-HDBK-1009

### Project decomposition
- https://www.pmi.org/standards/work-breakdown-structures-third-edition
- https://www.pmi.org/learning/library/practice-standard-work-breakdown-structures-8063
- https://www.cs.umd.edu/~nau/papers/erol1994umcp.pdf

### Agent instructions / context
- https://agentskills.io/specification
- https://developers.openai.com/api/docs/guides/latest-model

### Optional supporting methods
- https://asq.org/quality-resources/sipoc
- https://www.govinfo.gov/app/details/GOVPUB-C13-ba43579ec72306f00c01305771ffdf3b
- https://papers.nips.cc/paper/2023/hash/91edff07232fb1b55a505a9e9f6c0ff3-Abstract-Conference.html
- https://papers.nips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html

---

# 20. Expected final decision quality

The continuation is complete only when the operator can answer these questions without reading a large architecture essay:

1. **What established method(s) are we actually using?**
2. **Which parts are formal standards, vendor workflows, academic techniques, or Apex-specific adapters?**
3. **What does an agent do differently for trivial, normal, complex, and oversized work?**
4. **What exactly does it return before executing nontrivial work?**
5. **How are intent/specification, architecture/decomposition, implementation, and evidence linked?**
6. **How does lower-level evidence force higher-level reconsideration when necessary?**
7. **Where does each artifact live and who owns it?**
8. **How does Plan-Sync-Session consume/maintain it?**
9. **What 1–3 lines belong in the always-on agent instruction?**
10. **What file is loaded next, and under exactly which trigger?**
11. **How is the system verified not to over-plan simple work or lose coherence on large work?**
12. **Which current proposed patches need to be changed or withdrawn because of this decision?**

If those answers require the operator to learn another bespoke Apex conceptual framework, the research has probably failed its primary constraint.
