---
type: Research
title: "Role and context mapping"
description: "Role and context mapping for the APEX OpenMausBot adoption research."
status: candidate
date: 2026-09-27
---

# Role and context mapping

## Mapping principle

A product bot is a persistent profile. An APEX role is an accountability activated for a bounded run.
Preserve the role contracts before choosing the number of sidebar entries.
Sources: [A02](../ARCHITECTURE.md), [A10](14-source-register.md#apex-source-register), [S05](14-source-register.md#s05).

## Proposed pilot mapping

| APEX role | Option A runtime | Required input | Permitted return | Forbidden shortcut |
|---|---|---|---|---|
| Alfred | Controller conversation during intake/gate | Exact operator objective and constraints | Intake and gate presentation | Inventing approval or choosing a strategy |
| Meta Ops | Same controller during execution/closure | Accepted intent and file-backed phase state | Packets, integration, gated mutation receipts | Treating its own synthesis as independent review |
| Meta Strategy | Native read-only worker | Evidence slice, options question, stop condition | 2–3 distinct directions with uncertainties | Performing the implementation |
| Detective — validity | Fresh native read-only worker | Frozen artifact, evidence, validity criteria | Full evidence-bearing verdict | Reading alignment verdict or fixing artifact |
| Detective — alignment | Separate fresh native read-only worker | Frozen artifact, goal, decision log | Full alignment verdict | Reading validity verdict |
| Knowledge Bank | Bounded native lane | Sources, intended placement, lifecycle status | Candidate custody/placement output | Promoting its own content |
| Informatics Design | Bounded native lane | Exact files and consistency objective | Candidate structure findings/artifact | Broad renames outside packet |
| Prompts & Workflows | Bounded native lane | Reusable procedure requirement and canonical schemas | Candidate template with use case and stop condition | Replacing canonical packet shape |
| Domain worker | Temporary native worker | One deliverable and acceptance criteria | Candidate artifact and evidence | Unbounded delegation or shared-file ownership |

There are two Detective invocations, not necessarily two permanently installed role definitions.

## Product-native team variant

If Option B is chosen, a proposed visible roster is:

- APEX Run Controller, carrying Alfred/Meta Ops phase contracts.
- Meta Strategy.
- Knowledge Bank.
- Informatics Design.
- Prompts & Workflows.
- Separate validity and alignment reviewer profiles only after isolation is proven.
- Temporary domain workers only when packets justify them.

Do not create a separate Alfred bot that delegates to a separate Meta Ops bot by default.
That would split the supplied main-conversation contract and require a deliberate redesign.

Persistent specialist bots can be useful for ordinary production continuity.
The same continuity is a liability for fresh independent review.
New threads alone do not remove shared memory or recent-work context.
Evidence: [S04](14-source-register.md#s04), [S20–S21](14-source-register.md#s20).

## Tool and access contract

| Role | Existing native tool scope | Required migration test |
|---|---|---|
| Strategy | Read, Grep, Glob | Write, shell, outbound connectors absent or denied |
| Detective | Read, Grep, Glob | No mutation; identity verification method explicitly recorded |
| Informatics | Read, Grep, Glob, Write | Writes stay on named candidate surface |
| Prompts & Workflows | Read, Grep, Glob, Write | No self-installation of resulting doctrine |
| Knowledge Bank | Read, Grep, Glob, Write | Correct KB roots and source preservation |
| Meta Ops | Read, Grep, Glob, Write, Edit, Bash | Backbone boundary and exact approved change retained |

Native Write access is not an enforced path allowlist.
The existing architecture already acknowledges that limitation.
OpenMausBot's working-folder setting does not automatically close it.

The Detective's current read-only tool list lacks a hash command.
Prior APEX simulations recorded this limitation.
Use the established attestation plus controller recomputation honestly until a dedicated read-only hashing mechanism is accepted.
Do not report independent hash recomputation when the reviewer only read a supplied hash.

## Standing instructions versus job context

Standing role material should name purpose, boundaries, canonical entry point, and activation condition.
It should not contain a mutable current plan, pending approval, or previous verdict.
Those belong in the run packet.

A job brief should carry:

1. Run and packet identity.
2. Exact input artifact paths.
3. Desired output and acceptance criteria.
4. Allowed tools and write surface.
5. Source restrictions and unresolved uncertainties.
6. Stop condition and return destination.

These specialize the existing handoff schema; they do not replace it.

## Model and account mapping

Keep the current Claude-family Detective constraint until the operator changes it.
A second provider is not automatically a better or authorized review policy.
The product's engine list is capability evidence, not an account assignment plan.

For each chosen engine, record its executable, version, account alias, model identifier, and approval mode.
Record account aliases only, never credentials.
The local presence of claude.exe and codex.exe proves executables exist, not that either is authenticated.

## Acceptance condition

A role mapping passes only when an actual invocation receives the intended context and produces a valid bounded return.
A correctly named bot and an attractive team map do not satisfy this condition.
