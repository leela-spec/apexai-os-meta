---
title: "APEX Orchestration System — Architecture"
purpose: >
  The milestone-5 target architecture, assembled: topology, runtime mapping, component
  wiring, permission model, and the explicit record of what was deliberately not built.
  Every decision here traces to apex-meta/fable-orchestrator/design-lock-answers.md
  (Q1–Q8) and its research-integration note.
created: 2026-07-11
status: "built this session; per-story adoption gated on simulations/ records"
---

# Architecture

## 1. Topology (Q1, Q2)

Workflow backbone + ephemeral tool-scoped subagents. Four durable **accountabilities** — Alfred (operator interface), Meta Strategy (macro direction), Meta Ops (meso workflow + mutation backbone), Meta Detective (independent review) — plus three **specialist lanes** (Knowledge Bank, Informatics Design, Prompts & Workflows) and unbounded one-off **domain workers**. All are ephemeral invocations of named definitions; none holds state between runs — state is in files.

The three-package system is the mutation backbone, layered under Meta Ops: `apex-plan` proposes, `apex-sync` computes deterministically, `apex-session` mutates behind the operator gate. The old Apex v2 swarm is translated (its invariants survive as fields, workflows, and law), not revived (no 9 always-on agents, no BUILD/VERIFY/LOCK engine).

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
| Always-on named agents / cross-session agent memory | No durable-identity need demonstrated; user stories route to accountabilities without it (Q1) |
| BUILD/VERIFY/LOCK state engine | The three state axes above cover the demonstrated failure classes; a full machine is disproportionate (Q8, research P1) |
| Different-family validity judge (MCP/API) | Operator direction: no external calls; breaks the offline/stdlib trust boundary (research P2 adaptation) |
| Hard SKILL.md line caps, periodic drift-detection skill, token budgets | Defensive ceremony without an observed failure (decisions.md D2; Q3, Q7) |
| Relocation of `.claude/skills/` or `scripts/` | Canonical runtime locations of working machinery; moving = breakage for aesthetics |

## 7. Open build items

1. **Authority-digest enforcement code** in the apex-session write flow (`schemas/authority-state.schema.md` §enforcement) — Codex execution item per `apex-meta/CODEX_EXECUTION_STANDARD.md`; until then enforced procedurally by Meta Ops.
2. **Registry materialization** — `apex-meta/registry/index.md` does not exist yet; first `apex_sync.py` rebuild against `apex-meta/epics/narm-support-knowledgebase/` creates it (part of the first simulation).
3. **Per-story adoption** — each of the seven user stories runs for real and records pass/partial/fail in `simulations/` before its workflow counts as adopted. First candidate: US-IDEA-01 (smallest durable set).
