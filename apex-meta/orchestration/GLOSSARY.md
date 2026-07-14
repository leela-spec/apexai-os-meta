---
title: "APEX OS Orchestration Glossary"
purpose: >
  Canonical live terminology for APEX OS, Weekly Orchestrator, Multi-Agent Orchestration,
  and the shared Plan-Sync-Session Backbone. One meaning per term; historical names remain
  readable but do not compete with current runtime names.
created: 2026-07-11
source: "design-lock-answers.md Q7; ORCHESTRATION-SYSTEMS-INDEX.md"
---

# APEX OS Orchestration Glossary

| Term | Canonical meaning | Replaces / disambiguates |
|---|---|---|
| **APEX OS** | The repository-level operating system containing two separate orchestration systems — Weekly Orchestrator and Multi-Agent Orchestration — plus the shared Plan-Sync-Session Backbone. | "Apex" or "APEX orchestration system" when used as though only one orchestration system exists. |
| **Weekly Orchestrator** | The independent weekly operational system entered at `.claude/skills/weekly-orchestrator/SKILL.md`; owns PrecapWeek, PrecapNextDay, operator execution/evidence intake, FlowRecap, StatusMerge, ProjectStatus, and the next cycle. | The weekly loop treated as a stage of the live agent system. |
| **Multi-Agent Orchestration** | The operator-triggered orchestration system entered at `apex-meta/orchestration/00-START-HERE.md`; uses Alfred, Meta Strategy, Meta Ops, Meta Detective, specialist lanes, and bounded workers. | The live system's former working name "Fable Orchestrator" and ambiguous bare "Orchestration" labels. |
| **Plan-Sync-Session Backbone** | Shared APEX OS capability backbone: `apex-plan` proposes/decomposes, `apex-sync` computes deterministic reports, and `apex-session` applies confirmed mutation and closure. It is not a third orchestration system. | "Mutation backbone" when that phrase implies ownership by Multi-Agent Orchestration or a separate orchestration system. |
| **orchestration run** | One explicitly started, bounded execution of a named orchestration system, with a declared entry condition, file-backed state, stop/completion boundary, and operator-visible outcome. | An always-on agent mode or an implicit continuation from another system. |
| **role / accountability** | The semantic answerability layer: WHO is answerable for a class of work (Alfred, Meta Strategy, Meta Ops, Meta Detective, the lanes). A role label grants **no** permission. | v2 "role" sometimes read as permission source. |
| **state** | The permission-bearing layer: `lifecycle_stage` of a packet, `authority.state` of an artifact, and `operator_validation` of a mutation. What is allowed derives from state, never from role. | v2 BUILD/VERIFY/LOCK operational states (translated, not revived). |
| **agent** | A role definition or runtime worker only when qualified by system and invocation mode. Presence under `.claude/agents/` does not activate it or assign it to Weekly Orchestrator. | Unqualified "agent" used as an always-active identity. |
| **main-conversation contract** | A role contract adopted by the current main conversation for an active Multi-Agent Orchestration phase; Alfred and Meta Ops use this mode so dialogue, gates, integration state, and run continuity remain in one thread. | Treating every `.claude/agents/` file as a spawned subagent. |
| **spawned subagent** | A context-isolated, run-scoped worker invoked only when an active workflow routes a bounded packet to its description and tools; it returns its result and stops. | Persistent or globally active role behavior. |
| **candidate** | `authority.state: candidate` — produced but not independently reviewed; may inform, may not justify canon-changing writes; never auto-promotes. | "Draft", "proposal-quality", LEARNING_QUEUE entries. |
| **canon / accepted / verified** | `authority.state: verified` — independently reviewed against this exact version (`basis_digest` matches, `verification_ref` resolves). | v2 "LOCK", "accepted", "canonical". |
| **packet** | A record conforming to `schemas/handoff-packet.schema.md`; plan packets, Sync reports, H6 artifacts, and worker returns are instances, not competing schemas. | Per-skill invented packet shapes. |
| **handoff** | An explicit packet or confirmed durable-artifact reference that names sender, receiver, expected action, stop condition, and source basis. It transfers information, not automatic activation. | Chat-only implication, shared-folder inference, or silent reinterpretation. |
| **cross-system transfer** | Transfer between Weekly Orchestrator and Multi-Agent Orchestration authorized by explicit operator instruction, an explicit handoff packet, or a confirmed durable-artifact reference. The receiving system still requires its own activation condition. | Automatic cross-activation or absorption. |
| **workflow** | An ordered, file-recorded procedure with owners and gates (`workflows/*.md`) — resilient because its plan and outcomes live in durable artifacts. | "Workflow" as a loose synonym for a skill or system. |
| **skill** | A `.claude/skills/` capability package invoked for a repeatable procedure; it supports an accountability or orchestration system and does not erase ownership. | Skills as agents, systems, or authorization surfaces. |
| **validation** | Detective or deterministic verification that an artifact survives evidence (`verified`). **Validation ≠ approval.** | — |
| **approval / confirmation** | The operator's gate decision, recorded as `operator_validation: confirmed` on a specific mutation. It approves the act, not the artifact's truth. | "Approval" used for both artifact quality and mutation authorization. |
| **consequential** | Triggers durable mutation, public output, spend, safety-relevant instruction, or doctrine change, and therefore requires the applicable review and operator gate. | Undefined "important". |

Change rule: a new or amended entry enters as `candidate` (proposed by any role, usually Informatics Design), becomes canonical only after Detective review + operator confirmation — the glossary is itself a consequential artifact.
