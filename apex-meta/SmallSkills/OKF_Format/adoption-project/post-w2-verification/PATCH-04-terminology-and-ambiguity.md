---
type: Plan
title: PATCH-04 — Terminology Authority and Ambiguity
description: Exact-match patch pack to consolidate APEX orchestration terminology, separate verified from accepted state, namespace Weekly Macro/Meso/Micro, and remove ambiguous macro/meso labels from live agent routing descriptions.
tags: [patch, terminology, glossary, macro, meso, micro, agents]
status: proposed_not_applied
---

# Intent

Resolve terminology defects without creating another principles document or taxonomy.

Current problems:

1. `apex-meta/GLOSSARY.md` and `apex-meta/orchestration/GLOSSARY.md` both present themselves as canonical.
2. the root glossary carries stale pre-direct-fork definitions.
3. the canonical orchestration glossary currently collapses `verified` and `canon / accepted`, which weakens the review-versus-operator-confirmation boundary.
4. `macro`, `meso`, and `micro` are used for Weekly architecture levels, Multi-Agent role descriptions, and a document-analysis summary.
5. the phrase `project principles` has no canonical repository artifact and should not silently create one.

The repository-wide orchestration index already names `apex-meta/orchestration/GLOSSARY.md` as the terminology authority. This patch follows that existing decision.

**Do not apply this file as a whole-file rewrite. Apply each exact-match block independently.**

# A. Retire the duplicate root glossary as an authority

## Block 1 — make root glossary a compatibility route

<file>apex-meta/GLOSSARY.md</file>
<old>Rule: when any repo file uses these terms in a conflicting sense, this file wins for interpretation; the owning skill contract still wins for schema fields. Referenced from `ORCHESTRATION-SYSTEMS-INDEX.md` and `.claude/skills/weekly-orchestrator/SKILL.md`.</old>
<new>Rule: this file is a compatibility route only. Canonical live APEX OS orchestration terminology is owned by `apex-meta/orchestration/GLOSSARY.md`; the owning Skill or schema contract still wins for its own fields.</new>

## Block 2 — remove the duplicated stale definitions

<file>apex-meta/GLOSSARY.md</file>
<old>| term | canonical meaning | not |
|---|---|---|
| role | a named accountability with scoped tools and a precise description; says who may act | a unit of permission over artifacts — permission over an artifact comes from `authority.state`, never from role identity |
| state (of an artifact) | the artifact's `authority.state` (candidate / verified / invalidated) plus its `lifecycle_stage` (proposal / computed / confirmed) | the runtime memory of any agent |
| agent | an ephemeral, context-isolated subagent invocation from a durable definition file under `.claude/agents/` | an always-on process holding independent state; a skill |
| accountability | one of the four durable ownership surfaces — alfred, meta_strategy, meta_ops, meta_detective — carried as a field on packets and as subagent definitions | a persistent named agent with memory |
| skill | a reusable procedure/contract package under `.claude/skills/` that runs inside the invoking context (main thread or preloaded into a subagent) | an agent; a mechanism that grants isolation |
| workflow | the fixed stage sequence of the weekly loop, held in files (CLAUDE.md core_loop + weekly-orchestrator SKILL.md), not in any agent's memory | whatever sequence a session improvised |
| packet | any stage output carrying the shared handoff envelope (`.claude/skills/weekly-orchestrator/references/handoff-schema.md`) — the one shape for all handoffs | a free-form chat summary |
| candidate | produced but not independently reviewed; may not justify a canon-changing write | wrong, rejected, or low-quality |
| verified | independently reviewed at the current basis_digest with a pass verdict | operator-approved for write (that is `operator_validation: confirmed`) |
| canon / accepted | durable state under `state/` or `.claude/kb/` after a gated write | anything under `artifacts/` |
| validation | checking a packet against its contract/evidence (can be done by a reviewer agent) | approval — only the operator approves |
| approval | the operator setting `operator_validation: confirmed` on a specific packet | a reviewer pass verdict; silence; a prior approval of a different packet |</old>
<new>## Canonical terminology

Read `apex-meta/orchestration/GLOSSARY.md` for APEX OS, Weekly Orchestrator, Multi-Agent Orchestration, Plan-Sync-Session, role/state, agent/Skill, review, handoff, and Macro/Meso/Micro terminology.

Do not add a second definition here. Propose terminology changes at the canonical glossary owner.</new>

# B. Correct and extend the canonical orchestration glossary

## Block 3 — qualify agent semantics for both agent definitions and forked Skills

<file>apex-meta/orchestration/GLOSSARY.md</file>
<old>| **agent** | A role definition or runtime worker only when qualified by system and invocation mode. Presence under `.claude/agents/` does not activate it or assign it to Weekly Orchestrator. | Unqualified "agent" used as an always-active identity. |</old>
<new>| **agent / worker** | A runtime worker only when qualified by system and invocation mode. It may be spawned from a `.claude/agents/` definition or created by a Skill with `context: fork`; neither mechanism implies global activation or ownership. | Unqualified "agent" used as an always-active identity, or the assumption that every isolated worker must have a `.claude/agents/` wrapper. |</new>

## Block 4 — include Skill-fork workers in spawned-subagent semantics

<file>apex-meta/orchestration/GLOSSARY.md</file>
<old>| **spawned subagent** | A context-isolated, run-scoped worker invoked only when an active workflow routes a bounded packet to its description and tools; it returns its result and stops. | Persistent or globally active role behavior. |</old>
<new>| **spawned / forked worker** | A context-isolated, run-scoped worker created either from a custom agent definition or by `context: fork` on a Skill. It receives bounded task context, returns its result, and stops. | Persistent or globally active role behavior; proof that a separate wrapper-agent file is required. |</new>

## Block 5 — split verified from canon / accepted

<file>apex-meta/orchestration/GLOSSARY.md</file>
<old>| **canon / accepted / verified** | `authority.state: verified` — independently reviewed against this exact version (`basis_digest` matches, `verification_ref` resolves). | v2 "LOCK", "accepted", "canonical". |</old>
<new>| **verified** | `authority.state: verified` — independently reviewed against this exact version (`basis_digest` matches, `verification_ref` resolves). Verification establishes evidentiary status; it does not itself authorize a durable mutation. | Operator approval, durable acceptance, or v2 "LOCK". |
| **canon / accepted** | Durable current state after the owning write path has satisfied its required authority checks and operator gate. For project/task mutation, this means the applicable `apex-session` path with `operator_validation: confirmed`. | Merely `candidate`; merely `verified`; anything under an artifact/output folder that has not passed the owning write contract. |</new>

## Block 6 — make workflow definition work for both orchestration systems

<file>apex-meta/orchestration/GLOSSARY.md</file>
<old>| **workflow** | An ordered, file-recorded procedure with owners and gates (`workflows/*.md`) — resilient because its plan and outcomes live in durable artifacts. | "Workflow" as a loose synonym for a skill or system. |</old>
<new>| **workflow** | An ordered procedure owned by a named system or capability and recorded in its live entrypoint/contracts plus durable packets or state. A workflow may be represented by `workflows/*.md` or by a Skill-led control plane such as Weekly Orchestrator. | A loose synonym for a Skill, agent, or orchestration system; a sequence improvised only in chat. |</new>

## Block 7 — make Skill execution semantics current

<file>apex-meta/orchestration/GLOSSARY.md</file>
<old>| **skill** | A `.claude/skills/` capability package invoked for a repeatable procedure; it supports an accountability or orchestration system and does not erase ownership. | Skills as agents, systems, or authorization surfaces. |</old>
<new>| **skill** | A `.claude/skills/` capability package for a repeatable procedure. It can execute in the invoking context or, when its runtime frontmatter declares `context: fork`, as an isolated worker; either way it does not become an orchestration system or grant mutation authority. | The assumption that a Skill is always inline, always an agent, or an authorization surface. |</new>

## Block 8 — namespace the Weekly architecture levels and define ambiguity handling

<file>apex-meta/orchestration/GLOSSARY.md</file>
<old>| **Weekly Orchestrator** | The independent weekly operational system entered at `.claude/skills/weekly-orchestrator/SKILL.md`; owns PrecapWeek, PrecapNextDay, operator execution/evidence intake, FlowRecap, StatusMerge, ProjectStatus, and the next cycle. | The weekly loop treated as a stage of the live agent system. |</old>
<new>| **Weekly Orchestrator** | The independent weekly operational system entered at `.claude/skills/weekly-orchestrator/SKILL.md`; owns PrecapWeek, PrecapNextDay, operator execution/evidence intake, FlowRecap, StatusMerge, ProjectStatus, and the next cycle. | The weekly loop treated as a stage of the live agent system. |
| **Weekly Macro** | `apex-meta/kb/Weekly-Orchestrator/architecture/01-macro-architecture-decision.md` — the Weekly system-level topology and mechanism decisions. | A global APEX architecture tier; Meta Strategy's role label. |
| **Weekly Meso** | `apex-meta/kb/Weekly-Orchestrator/architecture/02-meso-file-map.md` — the Weekly execution-surface and write-boundary map. | A global APEX workflow tier; Meta Ops' role label. |
| **Weekly Micro evidence** | `apex-meta/kb/Weekly-Orchestrator/architecture/03-execution-trace-verification.md` — historical execution-trace evidence for the configuration it explicitly dates; not current runtime law. | A third live controller layer or a universal meaning of "micro". |</new>

## Block 9 — add explicit ambiguity rules without creating a principles artifact

<file>apex-meta/orchestration/GLOSSARY.md</file>
<old>Change rule: a new or amended entry enters as `candidate` (proposed by any role, usually Informatics Design), becomes canonical only after Detective review + operator confirmation — the glossary is itself a consequential artifact.</old>
<new>## Ambiguous shorthand

- **Macro / Meso / Micro**: when used without the `Weekly` qualifier or an explicit document context, these words are not global APEX tiers. Ask one clarification if multiple namespaces remain plausible.
- **Project principles**: there is no canonical repository artifact with this name. Route repository-wide invariants to `AGENTS.md`, APEX system boundaries to `.claude/CLAUDE.md` plus the selected system entrypoint, informatics rules to `apex-meta/informatics/standard.md`, and role doctrine to the selected role domain. If the intended scope is still ambiguous, ask one clarification rather than inventing a new principle set.

Change rule: a new or amended entry enters as `candidate` (proposed by any role, usually Informatics Design), becomes canonical only after Detective review + operator confirmation — the glossary is itself a consequential artifact.</new>

# C. Remove Macro/Meso collision from live agent routing descriptions

Agent descriptions are routing surfaces. Keep the concepts in the role accountabilities, but use unambiguous operational language in the discovery text.

## Block 10 — Meta Strategy frontmatter

<file>.claude/agents/meta-strategy.md</file>
<old>  Multi-Agent Orchestration macro-direction accountability. Spawn only when an active,</old>
<new>  Multi-Agent Orchestration strategic-direction accountability. Spawn only when an active,</new>

## Block 11 — Meta Strategy body

<file>.claude/agents/meta-strategy.md</file>
<old>You are **Meta Strategy**, the spawned macro-direction accountability for one bounded packet inside an active **Multi-Agent Orchestration** run (`apex-meta/orchestration/00-START-HERE.md`).</old>
<new>You are **Meta Strategy**, the spawned strategic-direction accountability for one bounded packet inside an active **Multi-Agent Orchestration** run (`apex-meta/orchestration/00-START-HERE.md`).</new>

## Block 12 — Meta Ops frontmatter

<file>.claude/agents/meta-ops.md</file>
<old>  Multi-Agent Orchestration meso-workflow accountability. Adopt this main-conversation</old>
<new>  Multi-Agent Orchestration workflow-integration accountability. Adopt this main-conversation</new>

## Block 13 — Meta Ops body

<file>.claude/agents/meta-ops.md</file>
<old>You are **Meta Ops**, the main-conversation meso-workflow accountability inside an active **Multi-Agent Orchestration** run (`apex-meta/orchestration/00-START-HERE.md`). This contract does not activate the system and is separate from Weekly Orchestrator.</old>
<new>You are **Meta Ops**, the main-conversation workflow-integration accountability inside an active **Multi-Agent Orchestration** run (`apex-meta/orchestration/00-START-HERE.md`). This contract does not activate the system and is separate from Weekly Orchestrator.</new>

# D. Clarify the document-analysis use of Macro/Meso/Micro

## Block 14 — scope the informatics summary headings

<file>apex-meta/kb/claude-code-orchestration-design/wiki/summaries/informatics-design-formats-practice-guide.md</file>
<old>## Macro / Meso / Micro

### Macro</old>
<new>## Macro / Meso / Micro

Scope note: these headings describe package-level, grouped-rule, and individual-rule analysis inside this research summary only. They are not the Weekly Macro/Meso/Micro architecture files and do not define a global APEX tier taxonomy.

### Macro</new>

# E. Route Weekly informatics doctrine to the canonical glossary

## Block 15 — terminology owner

<file>.claude/skills/weekly-orchestrator/references/roles/informatics-design-doctrine.md</file>
<old>- Rule: one concept keeps one name across a file pack; when vocabulary is unsettled, label the term provisional instead of alternating synonyms. `apex-meta/GLOSSARY.md` is the term authority. (BEST_PRACTICES.md; MISTAKES.md MIS-INF-003)</old>
<new>- Rule: one concept keeps one name across a file pack; when vocabulary is unsettled, label the term provisional instead of alternating synonyms. `apex-meta/orchestration/GLOSSARY.md` is the APEX orchestration terminology authority. (BEST_PRACTICES.md; MISTAKES.md MIS-INF-003)</new>

# Correction to the verification report

`00-verification-report.md` §4.2 previously stated that no canonical Weekly Micro file was found. That statement is superseded by this patch pack and the completion index: `apex-meta/kb/Weekly-Orchestrator/00-START-HERE.md` explicitly maps Weekly Micro to `architecture/03-execution-trace-verification.md`. The Micro file is real but explicitly historical/evidence-only.

# Verification after application

```text
1. Search live current-truth files for claims that `apex-meta/GLOSSARY.md` is canonical; none should remain.
2. Query “what does verified mean?”: answer must not imply operator approval or completed durable write.
3. Query “what is Weekly Meso?”: resolve directly to architecture/02-meso-file-map.md.
4. Query “check the Meso file” outside Weekly context: ask one clarification when more than one namespace is plausible.
5. Query “apply the project principles”: resolve a named scope or ask one clarification; do not invent PROJECT-PRINCIPLES.md.
6. Agent discovery for Meta Strategy / Meta Ops should use strategic-direction / workflow-integration language, not Macro/Meso shorthand.
```
