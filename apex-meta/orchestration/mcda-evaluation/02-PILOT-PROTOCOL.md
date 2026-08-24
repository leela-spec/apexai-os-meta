# 02 — Pilot Protocol

## Purpose

The MCDA desk score may reduce the field, but it cannot select the production orchestration system. Finalists must demonstrate useful Master of Arts work under the same controlled pilot.

The pilot evaluates the **system**, not the intelligence of one particular model. Use the same source packet, acceptance criteria, CEO decisions, and output expectations for all finalists.

## General rules

1. **No custom replacement subsystems.** Use candidate-native installation/configuration/extensions only.
2. **One canonical truth per concept.** No parallel hidden task board for a specific AI client.
3. **Persist before handoff.** Any agent switch must be recoverable from durable state alone.
4. **Output-first.** Every execution cycle produces a tangible artifact or state transition, not only discussion.
5. **Maker ≠ reviewer.** A distinct review pass must evaluate the work.
6. **Human owns consequential decisions.** The system may prepare options/recommendations but must stop at defined CEO gates.
7. **Deterministic where mechanical.** Validation, schema checks, status transitions, recurring schedules, file/path checks and similar bounded operations should not require a reasoning-model judgment where ordinary code can own the rule.
8. **Record actual friction.** Count repeated context loading, manual glue, broken handoffs, duplicate state, and recovery effort.

---

# Pilot A — Workshop from concept to approved skeleton

## Goal

Create the first decision-ready skeleton for a Master of Arts workshop from an ambiguous concept, using prior project knowledge and clear review roles.

## Required behavior

```text
CEO need
  -> project/spec framing
  -> relevant knowledge/context selection
  -> creative/subject expert draft
  -> operations/format review
  -> risk/safety/adherence review
  -> consolidated skeleton
  -> CEO decision gate
  -> durable next actions
```

## Pass conditions

- project goal and acceptance criteria are explicit;
- relevant prior workshop/method knowledge is referenced rather than rediscovered blindly;
- work can fan out to specialized roles without losing one canonical task state;
- reviewer can reject/request revision;
- CEO receives options/tradeoffs rather than silent autonomous scope decisions;
- approved skeleton and rejected alternatives remain traceable;
- next session can resume from repo state without chat transcript.

---

# Pilot B — Research-to-knowledge-to-content chain

## Goal

Take one bounded research question relevant to a coaching/method/offer topic and produce:

1. research synthesis;
2. method/knowledge update candidate;
3. one derived public-content concept;
4. provenance linking the derived output to evidence and decision state.

## Pass conditions

- research work and content creation are related but not conflated;
- evidence/provenance survives handoffs;
- reviewer can identify unsupported claims;
- knowledge promotion is explicit, not automatic just because a draft exists;
- content agent receives only the needed context rather than the entire repository;
- deterministic checks validate required metadata/references/state.

---

# Pilot C — Portfolio operating cycle

## Goal

Run a weekly review across several heterogeneous Master of Arts workstreams, e.g. website, workshop, method/coaching, content, research/operations.

## Required behavior

- list durable open work and dependencies;
- identify blocked/stale work;
- identify decisions requiring CEO input;
- propose next priorities with rationale;
- preserve previous priority/decision history;
- schedule or emit deterministic recurring follow-up where the candidate supports it;
- do not let an agent silently reprioritize a CEO-locked item.

## Pass conditions

A fresh agent/client can answer from durable state:

- What matters now?
- Why?
- What is blocked?
- Who/what is supposed to act next?
- What needs CEO decision?
- What changed since last review?

---

# Pilot D — Cross-agent handoff and independent verification

## Goal

Demonstrate that one AI client can start work, another can continue it, and a third or separate review role can verify it without relying on private chat memory.

Suggested sequence:

```text
Agent/client A: define + begin
Agent/client B: resume + execute
Reviewer C: inspect + challenge
CEO: approve/reject
Agent/client A or D: resume after decision
```

At least one switch should be between different agent ecosystems if available (for example Claude Code -> Codex or local CLI -> ChatGPT with GitHub access).

## Pass conditions

- no manual prose handover is needed beyond pointing the next agent to the project;
- status/dependencies/acceptance criteria remain intact;
- reviewer sees the evidence/decision history;
- rejected review findings become durable work items or state;
- final agent can continue after CEO approval without reconstructing intent.

---

# Pilot E — Failure and recovery

## Goal

Interrupt a multi-step workflow deliberately after durable work has been created.

Examples:

- agent session ends;
- command/process fails;
- one worker never finishes;
- review rejects the output;
- source/project file changes during execution.

## Pass conditions

- completed work is not repeated unnecessarily;
- remaining work is discoverable deterministically;
- stale/invalidated work is distinguishable from completed valid work;
- a new agent can resume;
- no chat transcript archaeology is required;
- the system does not mark the parent project complete while required child/review tasks remain open.

---

# Measurement sheet

For every candidate/pilot record:

| Metric | Measurement |
|---|---|
| Product usefulness | 1–5 human rating against acceptance criteria |
| Durable-state completeness | missing/partial/complete |
| Cross-agent resume | fail/partial/pass |
| Independent review | fail/partial/pass |
| CEO gate quality | fail/partial/pass |
| Provenance/decision trace | fail/partial/pass |
| Deterministic automation use | low/medium/high |
| Context reload burden | approximate files/tokens/steps needed after handoff |
| Manual glue | count and description of operator interventions not intrinsic to the work |
| Duplicate state | none / minor / significant |
| Recovery effort | steps needed after forced interruption |
| Framework-specific custom code | lines/files + why upstream extension was insufficient |
| Operational complexity | 1–5 |
| Failure notes | concrete evidence |

## Selection rule

The winner is **not** the system with the most features. Select the candidate/composition that:

1. passes all hard gates;
2. remains top-tier across MCDA sensitivity profiles;
3. passes A–E with useful artifacts;
4. requires the least custom infrastructure and duplicate truth;
5. gives the strongest durable collaboration between human CEO, local agents, web agents and deterministic automation.

If the specialized finalists do not materially outperform the GitHub-native control, choose the control and avoid unnecessary orchestration infrastructure.
