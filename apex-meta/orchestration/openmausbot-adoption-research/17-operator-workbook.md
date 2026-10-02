---
type: Research
title: Operator workbook for an APEX OpenMausBot pilot
description: Concrete candidate briefs and decision surfaces that preserve existing APEX contracts.
status: candidate
date: 2026-09-27
---

# Operator workbook

## Purpose

Use these examples after selecting the architecture and pilot scope.
They illustrate operation; they are not imported bot instructions or approved new skills.
Replace example paths and IDs with actual pilot records.
No example below grants a production mutation.

## First operator brief

> Start a bounded APEX Multi-Agent Orchestration pilot for this idea.
> Preserve my original text.
> Produce one candidate knowledge entry and placement recommendation.
> Keep Alfred and Meta Ops in the main conversation.
> Use the existing project role definitions and packet schemas.
> Review the consequential candidate through separate validity and alignment lenses.
> Present the proposed durable placement as an explicit decision.
> Stop before applying that decision.

This brief explicitly activates the intended system.
It also leaves project creation distinct from knowledge preservation.
Source: [canonical run](../workflows/orchestrator-run.md), [idea story](../user-stories/user-stories.md).

## Bounded worker return example

This is an illustrative top-level frontmatter shape matching current checker fixtures.
The schema document also presents a nested handoff_packet shape.
Resolve that parser/schema difference before implementing an adapter.

```yaml
packet_id: omb-pilot-idea-001
role_accountability: knowledge_bank
lifecycle_stage: proposal
status: operator_review_needed
target_surface: pilot-runs/idea-001/01-candidate.v1.md
next_state: candidate entry and placement advice returned to Meta Ops
prerequisites:
  - Original operator text preserved in 00-intake.md
expected_action: Recommend one source-preserving placement for the candidate entry
sources_evidence:
  - pilot-runs/idea-001/00-intake.md
uncertainties:
  - Operator has not selected durable placement
unresolved_risk:
  - Candidate could be mistaken for accepted project direction
stop_condition: Return the complete candidate packet without promoting it
operator_validation: not_requested
authority:
  state: candidate
  basis_digest: null
  verification_ref: null
```

The actual receiver must have access to the named source files.
A path in a message is not proof of access.
If the worker is read-only, the controller persists its full return verbatim.

## Product peer brief variant

If Option B is accepted and the active runtime exposes coordinate_bots:

> Read the packet at the exact host path provided below.
> Perform only its expected_action.
> Respect its allowed source and target scope.
> Return the candidate artifact reference and complete packet.
> Stop at its stop_condition.

Use the actual bot ID returned by the product.
Use a unique stable request_key for the assignment.
Use separate briefs for different responsibilities.
Do not use this persistent-peer route for blind review until T16 passes.
Source: [internal tool catalog](14-source-register.md#s21).

## Review packet construction

Instantiate the existing [review schema](../schemas/review-verdict.schema.md).
Do not replace it with a short “review this” chat message.

| Validity packet | Alignment packet |
|---|---|
| Frozen artifact identity | Same frozen artifact identity |
| Declared sources | Macro goal and decision log |
| Evidence and fidelity criteria | Scope and strategic-fit criteria |
| No producer advocacy | No validity verdict |
| No prior overall verdict | No producer confidence |

Ask each reviewer to identify the strongest wrong case per criterion.
Require retrieved evidence and an explicit result for that attempt.
Persist the whole verdict before integration.
Keep any missing evidence as hold or needs_input.

## Operator decision surface

```text
G1: Accept this exact candidate as a durable knowledge entry?
Target:
Artifact version and digest:
Independent review references:
Proposed before/after:
Options: accept this placement / revise / reject / defer
Unresolved uncertainties:
Action held until answer:

G2: Create any project action from this idea?
Options: no project / request a plan / provide a narrower next action
Consequences:
Action held until answer:
```

Capture the answer verbatim.
Do not merge G1 and G2 merely because the operator likes the idea.
Use the existing gate protocol and Session records for a later confirmed application.

## Daily operator view

The run controller should be able to answer:

| Question | Required evidence |
|---|---|
| What is the actual objective? | Intake packet |
| What has finished? | Full worker output and execution receipt |
| What is independently verified? | Version-bound review references |
| What needs my decision? | Named G-items |
| What changed durably? | Mutation record and fetch-back |
| What is blocked? | Concrete missing input or failed criterion |
| What happens next? | Next-session file |

Keep the answer compact while linking the full evidence.
Do not infer completion from a quiet bot or an empty queue.

## Resume brief

> Resume the named run from its saved files.
> Read next-session.md and the referenced packet, review, and mutation records.
> Report the current phase and unresolved gate.
> Recheck any input changed since review.
> Continue only the already authorized scope.

This tests the central file-backed continuity rule.
Do not ask the agent to reconstruct an approval from memory.

## Final adoption meeting

Review D04, D13, D17, and the actual pilot receipts.
Resolve only decisions supported by the evidence collected.
Record the accepted runtime scope and its limits.
Name the next workflow explicitly.
Leave untested domains unadopted.
