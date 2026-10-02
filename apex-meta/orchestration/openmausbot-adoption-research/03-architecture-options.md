---
type: Research
title: "Architecture options and recommended pilot"
description: "Architecture options and recommended pilot for the APEX OpenMausBot adoption research."
status: candidate
date: 2026-09-27
---

# Architecture options and recommended pilot

## Decision to make

Choose where APEX's control logic runs before creating a team of named bots.
A one-to-one mapping from seven role files to seven persistent peers is not automatically faithful to the supplied architecture.

All options below are proposals, not accepted architecture.

| Option | Shape | Main benefit | Main unresolved cost |
|---|---|---|---|
| A — Native APEX inside one OpenMausBot conversation | One Claude-backed run controller; existing project subagents and skills | Smallest change to Alfred/Meta Ops and fresh worker semantics | Prove project discovery, child-tool constraints, and review context through the app |
| B — OpenMausBot-native team | Controller plus persistent specialist bots; native coordination | Visible team, peer status, app-based role management | Standing peer history, memory, Chief instructions, and role enforcement need adaptation |
| C — Existing APEX controller with external OpenMausBot MCP | Existing control session directs selected OpenMausBot tasks | Retains established gate owner; adds execution UI incrementally | New MCP trust boundary, paired credential custody, distributed continuity |

Evidence basis: [A02](../ARCHITECTURE.md), [S07](14-source-register.md#s07), [S19–S25](14-source-register.md#s19).

## Recommended first experiment

**Proposal D04: test Option A first in an isolated pilot workspace.**
Use one product bot as the container for the existing main-conversation contracts.
Alfred handles intake and presentation phases; Meta Ops handles sequencing and integration phases.
These remain distinct accountabilities within one conversation.

Do not designate this bot as a product Chief initially.
The inspected Chief prompt tells its holder how to coordinate named product teammates.
That can compete with native APEX subagent routing.
The pilot should first establish faithful engine behavior without adding that competing route.

Use the existing project role definitions as the authority.
Prove discovery rather than copying every definition into a giant standing prompt.
If Option A cannot preserve the required native execution semantics, record the failure and evaluate C.
Option B is a later choice when visible peer collaboration justifies its extra adaptation work.

### Why this is a conditional recommendation

The supplied APEX architecture explicitly keeps Alfred and Meta Ops in one thread.
It also requires fresh read-only Detective invocations.
Option A changes fewer of those assumptions.

Anthropic's official documentation supports the underlying subagent mechanism.
OpenMausBot's documentation supports project settings and provider execution.
Neither establishes a passed end-to-end APEX integration.
The pilot is the missing evidence, not an optional demonstration.

## Intended control flow

~~~text
Operator
   |
OpenMausBot APEX pilot conversation
   |-- Alfred: intake and bounded choices
   |-- Meta Ops: packet state and sequencing
   |
   +--> native Strategy / specialist worker --> candidate files
   |
   +--> fresh validity reviewer -----------+
   +--> fresh alignment reviewer ---------+--> deterministic aggregation
   |
Alfred presents exact G-items
   |
Operator decision captured in file
   |
Existing Session / approved registry path
   |
Fetch-back receipt + H6 continuation
~~~

This diagram describes a proposed pilot, not an installed topology.

## Authority placement

The product owns execution identity and visible status.
APEX owns domain authority, gate interpretation, and canonical file state.
An adapter may carry file references, digests, run IDs, and thread IDs between those planes.
It must not translate “settled” directly into “verified” or “confirmed.”

The app may remember preferences. It may not become the sole repository of accepted strategy.
The user can continue an interrupted run from files, even if the conversation is unavailable.

## Conditions for Option B

Before using a native team for consequential work, prove:

- Reviewers cannot receive producer persuasion or the other lens's findings through memory, groups, or peer history.
- Strategy and Detective have enforced read-only tools, beyond a prompt instruction.
- Only the intended controller can apply the approved mutation path.
- The Chief's conversation cannot elevate delegate permissions unexpectedly.
- Bounded work returns full artifacts, not only short product receipts.
- Queue/retry behavior cannot duplicate a consequential effect.
- Team setup changes do not silently alter the approved runtime contract.

If any condition is only procedural, label it procedural.
Do not describe the whole system as mechanically enforced.

## Conditions for Option C

External MCP can dispatch and observe; it cannot approve on behalf of the operator.
Keep token material outside repository files and pin the target host/port.
Record both controller run ID and product conversation ID.
Treat needs-user, failed, stalled, and timed-out as explicit branch states.
Persist the exact returned artifact before closing its task.
Do not assume the external server can import team packages or administer computers.

## Deployment choice is independent

Any option still needs one execution host decision.
Windows desktop fits the already installed app.
A WSL/Linux server aligns more directly with recorded ext4 workspaces.
A separate always-on host solves laptop sleep, but adds account and repository custody work.

Choose based on the first workflow's actual files and uptime needs.
Do not combine architecture selection, multi-account rollout, infrastructure migration, and financial automation into one pilot.
