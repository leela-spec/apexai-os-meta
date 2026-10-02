---
type: Research
title: "OpenMausBot capabilities and evidence"
description: "OpenMausBot capabilities and evidence for the APEX OpenMausBot adoption research."
status: candidate
date: 2026-09-27
---

# OpenMausBot capabilities and evidence

## What OpenMausBot provides

OpenMausBot is a local agent harness and collaboration UI.
The inspected sources support using it for profiles, conversations, tool access, execution visibility, and scheduled dispatch.
They do not establish a native implementation of APEX's packet authority model.

| Capability | Verified source finding | Fit for APEX | Qualification |
|---|---|---|---|
| Agent engines | Supported CLI engines; explicit executable overrides | Reuse engines and accounts | Authentication and model entitlement need local tests |
| Bot profiles | Durable identity, instructions, memory, skills | Stable role presentation | APEX execution remains run-scoped |
| Threads | Separate running/conversation state | One run or bounded task | Bot memory remains shared |
| Groups | Shared conversation | Collaborative production | Unsuitable as default blind-review channel |
| Chief of Staff | Coordinates team and setup | Possible Meta Ops presentation | Generated coordination instructions need conflict tests |
| Peer work | Bounded assignments and returned status | Specialist execution | Some paths retain standing peer history |
| External MCP | Bounded inspect/create/send/wait controls | Optional external APEX controller | Excludes approval grants and several admin actions |
| Custom MCP | Provider-dependent tool connections | Existing service adapters | Per-bot selection is not shell isolation |
| Skills | Imported/indexed procedures | Portable role procedures | Supporting assets and engine semantics require route-specific testing |
| Team packages | Additive reviewed import | Repeatable rollout | Not complete execution configuration |
| Routines | Scheduled agent executions | Authorized recurring work | App/server must remain running |
| Backups | App-state recovery | Recovery alongside repository backup | Does not include external project directories |

Sources: [S05–S17](14-source-register.md#s05), [S20–S25](14-source-register.md#s20).

## Three separate orchestration interfaces

### Native engine workers

An OpenMausBot conversation can use a provider whose own runtime supports subagents.
Anthropic documents project-scoped agents and tool-restricted contexts.
Whether this exact APEX project configuration loads inside the installed OpenMausBot process remains a pilot test.
Do not substitute an OpenMausBot profile for a Claude subagent definition and assume equivalence.

### OpenMausBot internal peer coordination

The pinned tool catalog exposes coordinate_bots for active profiles that use bounded coordination.
It accepts actual teammate IDs, an explicit request_key, a bounded brief, and optional rework.
Normal direct assignments continue a standing conversation with that peer.
Other source paths expose delegate_bot, ask_bot, and delegation status tools.

These are different execution paths. Limits or freshness guarantees from one path cannot be generalized to all paths.
The active runtime tool catalog and returned receipts are the authority for what can actually be called.
Sources: [S20](14-source-register.md#s20), [S21](14-source-register.md#s21), [S25](14-source-register.md#s25).

### External MCP coordination

The separately documented external stdio server supports inspecting bots/channels, creating task conversations, sending work, waiting, and interrupting.
It intentionally omits approval grants, credential modification, team import, deletion, and computer lifecycle.
It is not the same catalog as the internal agents integration.

This is promising for a controller that keeps APEX governance outside the app.
It still adds an MCP integration absent from the supplied architecture's current mechanism baseline.
Adoption needs an explicit architecture decision. Source: [S07](14-source-register.md#s07).

## Important non-equivalences

| Product expression | What it means here | What it must not be treated as |
|---|---|---|
| Ask | Provider-specific permission mode | Read-only access or guaranteed approval for every write |
| Full Access | Broad standing execution approval | APEX operator confirmation for a particular mutation |
| New thread | New conversation state | Empty bot memory or no recent-work brief |
| Chief | Product team coordinator | Human strategic authority |
| Peer review/approval | Product communication or tool flow | Two independent APEX Detective verdicts |
| Routine complete | Execution receipt | Verified artifact, accepted plan, or financial approval |
| Skill imported | Stored procedure material | All references resolved or native fork semantics preserved |
| Team exported | Portable package | Full backup, account transfer, or active permission rollout |

## Contradictions and version uncertainty

The official security overview uses broad approval-card language.
The detailed approval guide says provider modes govern native tool decisions; Codex Ask includes workspace-write.
Use the detailed guide to avoid claiming universal write prompts.

The skill implementation header describes a narrow SKILL.md-only import.
The team-sharing guide describes richer packaged skills. These can reflect different routes and evolution.
Do not flatten them into either “all files import” or “all files are discarded.”

The release asset is verified locally, but source inspection is of a later main commit.
Features described in that source remain release-unverified until exercised against the installed build.

## Best-practice statement supported by the evidence

Use OpenMausBot as the execution and visibility surface for explicitly scoped work.
Keep APEX authority in files and in its existing contracts.
Treat memory, shared groups, automatic permissions, and peer-history reuse as separate design choices.
This recommendation is a PROPOSAL derived from verified facts; no official vendor source prescribes the APEX-specific design.
