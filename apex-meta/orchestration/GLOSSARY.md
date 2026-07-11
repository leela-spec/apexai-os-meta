---
title: "Orchestration Glossary"
purpose: >
  The canonical meaning of every term that has drifted across the source KBs and skills.
  One meaning per term; the drifted meanings each entry replaces are named so old
  documents remain readable. Terminology authority for the whole orchestration system
  (Informatics Design lane applies it; new entries arrive as candidates).
created: 2026-07-11
source: "design-lock-answers.md Q7; ORCHESTRATION-SYSTEMS-INDEX.md §5.3"
---

# Orchestration Glossary

| Term | Canonical meaning | Replaces / disambiguates |
|---|---|---|
| **role / accountability** | The semantic answerability layer: WHO is answerable for a class of work (Alfred, Meta Strategy, Meta Ops, Meta Detective, the lanes). A role label grants **no** permission. | v2 "role" sometimes read as permission source — explicitly invalid ("no role label may be used as compliance theater for permissions the current state does not grant"). |
| **state** | The permission-bearing layer: `lifecycle_stage` of a packet, `authority.state` of an artifact, `operator_validation` of a mutation. What is *allowed* derives from state, never from role. | v2 BUILD/VERIFY/LOCK operational states (translated, not revived). |
| **agent** | In this system, always qualified: **accountability** (durable role definition in `.claude/agents/`, invoked ephemerally) vs. **subagent** (any ephemeral isolated Claude invocation) vs. **domain worker** (one-off subagent or human with one bounded deliverable). There are no always-on agents. | Unqualified "agent" across the KBs meaning any of the three. |
| **candidate** | `authority.state: candidate` — produced but not independently reviewed; may inform, may not justify canon-changing writes; never auto-promotes. | "Draft", "proposal-quality", LEARNING_QUEUE entries. |
| **canon / accepted / verified** | `authority.state: verified` — independently reviewed against this exact version (`basis_digest` matches, `verification_ref` resolves). | v2 "LOCK", "accepted", "canonical". |
| **packet** | A handoff record per `schemas/handoff-packet.schema.md` — the ONE shape. `apex_plan_packet`, sync reports, H6 artifacts, worker returns are instances, not separate schemas. | Per-skill invented packet shapes. |
| **workflow** | An ordered, file-recorded procedure with owners and gates (`workflows/*.md`) — resilient because its plan lives in files/scripts. | "Workflow" as loose synonym for "process" or for a skill. |
| **skill** | A `.claude/skills/` capability package invoked by an accountable role; supports the accountability, never erases ownership. | Skills as "agents" or authorization surfaces. |
| **validation** | Detective/deterministic verification that an artifact survives evidence (`verified`). **Validation ≠ approval.** | — |
| **approval / confirmation** | The operator's gate decision, recorded as `operator_validation: confirmed` on a specific mutation. Approves the *act*, not the artifact's truth. | "Approval" used for both artifact quality and mutation authorization. |
| **consequential** | Triggers durable mutation, public output, spend, safety-relevant instruction, or doctrine change ⇒ full loop (Detective review + operator gate). Everything else may collapse the middle phases, never the gate. | Undefined "important". |
| **mutation backbone** | The three-package boundary: `apex-plan` (propose) → `apex-sync` (compute) → `apex-session` (gated mutate) — the only path to durable state. | — |

Change rule: a new or amended entry enters as `candidate` (proposed by any role, usually Informatics Design), becomes canonical only after Detective review + operator confirmation — the glossary is itself a consequential artifact.
