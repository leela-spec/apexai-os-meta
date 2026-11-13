---
title: "Multi-Agent Orchestration — Architecture"
purpose: >
  The live Multi-Agent Orchestration architecture inside APEX OS: activation and scope,
  topology, runtime mapping, component wiring, permission model, and the explicit record
  of what was deliberately not built. Design history remains in
  apex-meta/fable-orchestrator/design-lock-answers.md and its research-integration note.
created: 2026-07-11
status: "live architecture; per-story adoption remains governed by simulations/ records"
---

# Multi-Agent Orchestration Architecture

## Scope and activation

This architecture governs Multi-Agent Orchestration only. Start it only after an explicit operator request for a Multi-Agent Orchestration run or an explicit operator route of a bounded problem into this system. It is not the default APEX OS mode.

The Weekly Orchestrator is a separate APEX OS orchestration system and is not included in this topology. A shared `.claude/agents/` location does not create shared orchestration. Cross-system transfer requires explicit operator instruction, an explicit handoff packet, or a confirmed durable-artifact reference.

## 1. Topology (Q1, Q2)

File-backed workflow + tool-scoped subagents. Four durable **accountabilities** — Alfred (operator interface), Meta Strategy (macro direction), Meta Ops (meso workflow + shared-backbone integration), Meta Detective (independent review) — plus three **specialist lanes** (Knowledge Bank, Informatics Design, Prompts & Workflows) and unbounded one-off **domain workers**. The definitions are durable; role adoption and spawned workers are run-scoped. None holds authoritative state between runs — state is in files.

The Plan-Sync-Session Backbone is shared APEX OS infrastructure, not a third orchestration system and not owned by Multi-Agent Orchestration. Inside an active run, Meta Ops uses it as follows: `apex-plan` proposes and decomposes, `apex-sync` computes deterministically, and `apex-session` applies confirmed mutation and closure. The old Apex v2 swarm is translated (its invariants survive as fields, workflows, and law), not revived (no 9 always-on agents, no BUILD/VERIFY/LOCK engine).

```
OPERATOR ⇄ Alfred
             │
  Meta Strategy (options; operator selects)
             │
  Meta Ops ──── apex-plan → apex-sync → [lanes/workers] → integrate
     │                                                        │
     ├────────── detective-review (validity ∥ alignment) ◄────┘
     │                    │ verdicts → named owners
     └── operator gate → apex-session (confirmed mutation) → state delta / next session
```

## 2. Runtime mapping (mechanism ladder — smallest sufficient rung)

**Invocation modes (load-bearing):** **Alfred and Meta Ops are main-conversation contracts** adopted only inside an explicitly started Multi-Agent Orchestration run. Alfred remains in the main conversation for live operator dialogue and exact decision capture. Meta Ops remains there to hold the complete run sequence, gate records, integration state, and closure across phases. **Meta Strategy, Meta Detective, the three lanes, and domain workers are spawned only when the active workflow routes a bounded packet to them.** Custom subagent skills and delegation capabilities are explicit runtime configuration, not an activation signal; the presence of a file under `.claude/agents/` never makes a role global or always active.

| Component | Mechanism | Rung |
|---|---|---|
| Accountabilities/lanes | `.claude/agents/*.md` (name, description, narrow tools, contract) | subagent definition |
| Run loop | `workflows/orchestrator-run.md` followed by the main conversation (or a Workflow script for large fan-outs) | markdown contract / workflow |
| Packets, verdicts, state | Markdown + YAML frontmatter on disk | plain artifact |
| Deterministic compute | `scripts/apex_sync.py` (stdlib, dry-run-first, `--json`) | script |
| Review | two parallel fresh `meta-detective` invocations with blind packets | subagent |
| Gate | `operator_validation` field + literal confirmation phrase | field + conversation |
| NOT used | hooks, plugins, MCP, external models, LLM aggregators | — deliberately below the escalation bar |

## 3. Permission model (Q6, Q7, Q8 + research P1)

Role names grant nothing. Permission derives from state, on three axes:

1. **`lifecycle_stage`** (packet): `proposal` → `computed` → `confirmed`. Only apex-session writes `confirmed`.
2. **`authority.state`** (artifact): `candidate` → `verified` → (`invalidated`). Only a passing independent review (per `schemas/authority-state.schema.md` transitions) yields `verified`; any substantive edit resets to `candidate`.
3. **`operator_validation`** (mutation): `confirmed | rejected | needs_revision | not_requested`.

Canon-changing write ⇔ `operator_validation: confirmed` ∧ every authoritative input `verified` with matching `basis_digest`. Tool scoping enforces the coarse boundary (Detective and Strategy are read-only; only Meta Ops carries Write/Edit/Bash into the backbone).

## 4. Review model (Q8 + research P2)

Two blind parallel lenses (validity, strategic alignment) as fresh `meta-detective` invocations; criterion-level falsification mandatory; deterministic aggregation (`escalate > needs_input > hold > revise > pass`, single critical non-pass blocks, no majority vote, no LLM aggregator); reviewer never fixes; correction = new immutable version = re-review. Full wiring: `workflows/detective-review.md`.

**Recorded limitation:** both lenses are Claude-family. Compensating controls: blindness contract, falsification-before-evaluation, evidence-bearing PASS gate, deterministic aggregation. Escalation path if simulations show plausible-but-wrong artifacts passing: different-family judge — an operator trust-boundary decision, currently out of scope (no external calls, operator direction 2026-07-11).

## 5. Context economy (Q3, Q5 dimension D5)

Compact anchors (this package's files are each ≤ ~6 KB), detail behind explicit references, templates on demand, exact computation pushed into the script, verbose work isolated in ephemeral subagents returning packet summaries. No token accounting was added (neither source system had it; no observed failure justifies the ceremony).

## 6. Deliberately not built (with the reason)

| Not built | Why |
|---|---|
| Always-on named agents / cross-session agent memory | No durable-identity need demonstrated; user stories route to run-scoped accountabilities without it (Q1) |
| Weekly Orchestrator absorption or automatic cross-activation | Weekly Orchestrator is a separate APEX OS system with its own entrypoint and loop; transfer occurs only through explicit instruction or durable handoff artifacts. |
| BUILD/VERIFY/LOCK state engine | The three state axes above cover the demonstrated failure classes; a full machine is disproportionate (Q8, research P1) |
| Different-family validity judge (MCP/API) | Operator direction: no external calls; breaks the offline/stdlib trust boundary (research P2 adaptation) |
| Hard SKILL.md line caps, periodic drift-detection skill, token budgets | Defensive ceremony without an observed failure (decisions.md D2; Q3, Q7) |
| Relocation of `.claude/skills/` or `scripts/` | Canonical runtime locations of working machinery; moving = breakage for aesthetics |
| Enforced path-scoped writes for lanes | Lane rules like "write only inside KB roots" are **guidance, not enforcement** — the `Write` tool grant is repo-wide. Permission settings are the designated enforcement rung IF a simulation ever records a violation (mechanism-ladder rule: don't escalate without an observed failure) |

## 7. Current build status and open items

1. **Registry materialized.** `apex-meta/registry/index.md` exists and is maintained through the `apex-sync` registry path. Its presence does not authorize an unreviewed write.
2. **Authority-digest enforcement code remains open** in the apex-session write flow (`schemas/authority-state.schema.md` §enforcement) — Codex execution item per `apex-meta/CODEX_EXECUTION_STANDARD.md`; until then enforced procedurally by Meta Ops.
3. **Per-story adoption remains evidence-gated.** Each user story records pass/partial/fail in `simulations/` before its workflow counts as adopted; do not infer current adoption from this architecture file.
4. **Script-held run loop remains an escalation trigger, not a default build item.** The run loop is main-conversation-held with file state as the resumability control. Escalate to a Workflow script only if a simulation records lost in-flight phase work that durable file state did not capture.
