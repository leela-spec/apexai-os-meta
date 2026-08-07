---
title: "Local Orchestration Engine — APEX OS meta project"
purpose: "Design-lock workspace for a laptop-resident, non-reasoning orchestrator that sequences workflow steps and delegates the actual reasoning to browser-driven AI subscription sessions and worker repos (candidates: Hermes, Odysseus, OpenClaw)."
created: 2026-07-28
status: "pre-design — architecture questions being resolved via DESIGN-LOCK-QA.md"
maintenance: "Update this file's status line whenever the initiative moves from Q&A to build, and whenever ORCHESTRATION-SYSTEMS-INDEX.md classification changes (see DESIGN-LOCK-QA.md Q5)."
---

# Local Orchestration Engine

> **Latest handover:** `apex-meta/local-orchestration-engine/HANDOVER-2026-08-07.md` — read this
> before the sections below if you are picking this work up fresh (local or online agent). It
> records what was corrected, approved, and applied most recently, and what is explicitly still
> pending a fresh operator decision.

## What this is

A project folder for designing a small local model that acts purely as an **operator**, not a
reasoner: it sequences a workflow of prompts, manages state/handoffs, and calls tools — while the
actual heavy reasoning (research, prompt extraction, analysis) is delegated to browser-driven
sessions against paid AI chat subscriptions (Claude, ChatGPT, Gemini, etc.) and to one or more
worker codebases running in a sandbox on this machine. Candidate worker codebases under
consideration: **Hermes** (Nous Research's agent framework, `hermes-agent.nousresearch.com`),
**Odysseus** (identity not yet confirmed), and **OpenClaw** (this operator's own terminal/repo
system, already present in this KB under `MasterOfArts/OpenClaw/`).

## System name

The live name for this system is the **Flow Execution Engine (FEE)**. It is deliberately *not*
called an orchestrator: `apex-meta/orchestration/GLOSSARY.md` pins "orchestration system" to the
two that exist, and FEE is an **execution substrate for one stage of one of them**, not a third
system. `local-orchestration-engine/` is therefore a **former working name, not the live system
name** — handled exactly as `apex-meta/fable-orchestrator/` was for Multi-Agent Orchestration.
Folder rename is optional and deferred.

## Where to start

```yaml
read_order:
  1: architecture/01-macro-architecture-decision.md   # what combines, AI tier allocation, trust boundary
  2: architecture/02-meso-module-design.md            # the nine modules and their contracts
  3: architecture/03-micro-implementation-map.md      # paths, CLI, frozen-plan schema, verification plan
  4: architecture/04-decision-ledger.md               # every decision ranked, with reversal triggers
  5: DESIGN-LOCK-QA.md                                # Q&A provenance; Q1 is the only substantive open item
```

`DESIGN-LOCK-QA.md` remains the reasoning record. Q1–Q16 are resolved except **Q1** (what Hermes /
Odysseus AI / OpenClaw concretely are, and which to adopt), which gates only the executor bridge
(M7) — every other module can be built without it.

## Relationship to the rest of APEX OS

**Resolved:** FEE attaches to the **Weekly Orchestrator at step 4 only** — the one stage of the
locked dispatch trace whose actor is `operator (human)`. It replaces the actor at that step and
nothing else. Gate G3 stays a human gate.

It is **not** a third orchestration system and must not be added to
`apex-meta/ORCHESTRATION-SYSTEMS-INDEX.md` as a peer. It never activates Multi-Agent Orchestration —
it may only emit a handoff packet the operator chooses to route, per the repo's cross-system
transfer law.

Exactly three files outside this folder need additive changes, each requiring its own operator gate;
they are enumerated in `architecture/03-micro-implementation-map.md` §5.

## Status

`authority.state: candidate`. Nothing is built, nothing is operator-confirmed, and no live contract
has been edited. `03-micro-implementation-map.md` §6 defines the nine tests (V1–V9) that must
actually pass before any part of this counts as adopted — the injection-containment test (V3) must
pass before any browser adapter is written.

## Known risk carried into every downstream decision

Driving a subscription chat web UI programmatically (rather than through the metered API) sits
outside most providers' consumer terms of service and carries real account-suspension risk. The
operator has accepted this risk and wants detection-avoidance engineering (see DESIGN-LOCK-QA.md
Q4). Any implementation work on the browser-automation layer must carry this forward explicitly —
it is a standing design constraint, not a one-time disclaimer.
