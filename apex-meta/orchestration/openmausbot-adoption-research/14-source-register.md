---
type: Research
title: "Official and local source register"
description: "Official and local source register for the APEX OpenMausBot adoption research."
status: candidate
date: 2026-09-27
---

# Official and local source register

## Scope and evidence rules

Research date: 2026-09-27. “OpenMaoz/Openauz Bot” is interpreted as OpenMausBot, the product identified earlier in this task.

This bundle uses official OpenMausBot documentation, its official source repository, official release metadata, and official Anthropic documentation. APEX files are first-party requirements and local evidence, not vendor claims. Search results from forums, mirrors, and third-party tutorials were excluded.

Evidence classes:

| Label | Meaning | Does not establish |
|---|---|---|
| DOC | Retrieved official product documentation | Behavior in the installed version |
| SRC | Inspected code at a pinned upstream commit | That code shipped in the installer |
| LOCAL | Observed local file, binary metadata, or command result | A successful live agent workflow |
| APEX | Existing local contract or recorded decision | Independent verification of historical execution |
| PROPOSAL | Integration recommendation derived from the cited constraints | Operator acceptance or proven product capability |
| UNKNOWN | Evidence missing or contradictory | A negative capability claim |

The inspected upstream commit is **1d8808b62fb38ead913e1bc4210858509b141ee0**, dated 2026-09-27.
The installed executable reports **0.1.88.0**. The official latest release is **v0.1.88**, published 2026-09-26.
The source package also says 0.1.88; that matching label does **not** prove identical source and installed binary behavior.
Every pilot must record the actual build and engine version.

## Official source register

### S01

[Official installation guide](https://docs.openmausbot.com/docs/getting-started/installation).
DOC. Windows package, agent CLI prerequisite, app-data location. Read 2026-09-27.

### S02

[Official v0.1.88 release](https://github.com/milind-soni/openmausbot-releases/releases/tag/v0.1.88).
[Release metadata API](https://api.github.com/repos/milind-soni/openmausbot-releases/releases/latest).
LOCAL plus official metadata. API retrieved with PowerShell after the web reader could not open it.
Installer size: 235204516 bytes.
Official asset digest: sha256:08d737c86ddc40a6d4bc003f238aada0a32c872c1bda9e8bd1b3f57d32d49d6b.
The downloaded local installer matches this digest. This establishes asset integrity, not vendor code-signing.

### S03

[Approval levels, pinned source](https://github.com/milind-soni/OpenMausBot/blob/1d8808b62fb38ead913e1bc4210858509b141ee0/docs/approval-levels.md).
DOC/SRC. Provider permission mappings, conversation-specific levels, Chief Full Access delegation, unattended turns.
Read the opening table and “Provider mappings.”
Also read the section about Full Access delegation by a Chief.
The nine-read-tool count in this document is not exhaustive for this commit; agent-tool-policy.ts contains a larger set.

### S04

[Bot memory, pinned source](https://github.com/milind-soni/OpenMausBot/blob/1d8808b62fb38ead913e1bc4210858509b141ee0/docs/memory.md).
DOC/SRC. MEMORY.md loading budget; shared notes; recent-work briefs; recall; journal limitations.
Sections: “What loads,” “What a bot knows about its other conversations,” “The journal.”

### S05

[Bots, folders, and threads](https://docs.openmausbot.com/docs/features/bots-and-tasks).
DOC. Persistent profiles, separate thread state, shared memory, folders versus sandbox, bounded delegation.

### S06

[Threads, groups, and collaboration](https://docs.openmausbot.com/docs/features/chat-and-teams).
DOC. Group context, costs, specialist model selection, thread branching, teams.

### S07

[External MCP server, pinned source](https://github.com/milind-soni/OpenMausBot/blob/1d8808b62fb38ead913e1bc4210858509b141ee0/docs/mcp-server.md).
DOC/SRC. Windows executable/script paths; paired mutation access; port discovery; bounded transcript reads; explicit excluded operations.

### S08

[Custom MCP servers, pinned source](https://github.com/milind-soni/OpenMausBot/blob/1d8808b62fb38ead913e1bc4210858509b141ee0/docs/custom-mcp-servers.md).
DOC/SRC. Per-bot server selection; project-config exceptions; provider transports; Claude config inheritance; Codex config inheritance; secret storage.

### S09

[Team sharing, pinned source](https://github.com/milind-soni/OpenMausBot/blob/1d8808b62fb38ead913e1bc4210858509b141ee0/docs/team-sharing.md).
DOC/SRC. Package version 2; additive import; Ask defaults; disabled skills; paused routines; excluded credentials/models/computers.

### S10

[Routine schedules, pinned source](https://github.com/milind-soni/OpenMausBot/blob/1d8808b62fb38ead913e1bc4210858509b141ee0/docs/routine-schedules.md).
DOC/SRC. Timezones, cron, sleep/downtime, catch-up, paused imports, execution target.

### S11

[Routines and webhooks](https://docs.openmausbot.com/docs/features/automation).
DOC. Receipt states; independent execution and report destinations; separate webhook receiver.

### S12

[Data and backups](https://docs.openmausbot.com/docs/self-hosting/data-and-backups).
DOC. Encrypted Settings export, replacement restore, excluded external repositories and credentials, filesystem snapshots.
This is the authority for the distinction between template export and recovery backup.

### S13

[Security model](https://docs.openmausbot.com/docs/security).
DOC. Process boundary, scoped access, credentials, dedicated environments.
Detailed permission behavior in S03 qualifies broad approval language here.

### S14

[Self-hosting, pinned source](https://github.com/milind-soni/OpenMausBot/blob/1d8808b62fb38ead913e1bc4210858509b141ee0/docs/self-hosting.md).
DOC/SRC. Local-owner loopback trust, service deployment, server-side engine authentication, deployment alternatives.
Read “Loopback trust: owner or service” before selecting a shared server.

### S15

[Desktop companion, pinned source](https://github.com/milind-soni/OpenMausBot/blob/1d8808b62fb38ead913e1bc4210858509b141ee0/docs/desktop-companion.md).
DOC/SRC. Remote desktop client boundaries, host-side execution, paired relay, host awake requirement.

### S16

[Agent engines](https://docs.openmausbot.com/docs/providers).
DOC. Supported engines including Hermes ACP; executable override; live model list; named Claude accounts.
Account entitlement and actual Hermes compatibility remain local acceptance tests.

### S17

[Configuration](https://docs.openmausbot.com/docs/getting-started/configuration).
DOC. UI configuration and source/headless Claude tool subsets.
Do not assume a source/headless example is exposed as a packaged desktop per-bot control.

### S18

[Team incidents, pinned source](https://github.com/milind-soni/OpenMausBot/blob/1d8808b62fb38ead913e1bc4210858509b141ee0/docs/team-incidents.md).
DOC/SRC. Chief notifications, retry scope and limits, unchanged receiving-thread approval mode.

### S19

[Claude Code custom subagents](https://code.claude.com/docs/en/sub-agents).
Official Anthropic DOC. Project agent discovery, isolated contexts, tool restrictions, and startup context.
This proves Claude capabilities, not their availability through every OpenMausBot configuration.

### S20

[Chief prompt implementation](https://github.com/milind-soni/OpenMausBot/blob/1d8808b62fb38ead913e1bc4210858509b141ee0/server/chief-of-staff.ts#L40).
SRC. Both bounded-coordination and older delegation prompt branches.
The bounded branch explicitly continues a standing peer conversation.

### S21

[Internal agent tool catalog](https://github.com/milind-soni/OpenMausBot/blob/1d8808b62fb38ead913e1bc4210858509b141ee0/server/drivers/agents-catalog.ts#L244).
SRC. coordinate_bots schema: 1–4 recipients, 4,000-character message, request_key and rework.
Tool profiles replace older tools; inspect the active catalog instead of hard-coding assumed availability.

### S22

[Delegation implementation](https://github.com/milind-soni/OpenMausBot/blob/1d8808b62fb38ead913e1bc4210858509b141ee0/server/delegations.ts#L114).
SRC. Older delegation queue and bounded receipts: 100 records, 48-hour pruning, 4,000-character results.
These limits do not automatically describe the separate coordinate_bots implementation.

### S23

[Skill storage implementation](https://github.com/milind-soni/OpenMausBot/blob/1d8808b62fb38ead913e1bc4210858509b141ee0/server/skills.ts).
SRC. Import behavior, per-bot storage, native discovery links, indexed prompt loading.
The file's opening v1 comment is narrower than the v2 team-sharing document; verify import routes independently.

### S24

[Claude driver implementation](https://github.com/milind-soni/OpenMausBot/blob/1d8808b62fb38ead913e1bc4210858509b141ee0/server/drivers/claude.ts#L1145).
SRC. tools/disallowedTools settings; project setting sources; strict MCP config; integrations.
An implementation option is not evidence of a reviewed desktop UI workflow.

### S25

[Harness implementation](https://github.com/milind-soni/OpenMausBot/blob/1d8808b62fb38ead913e1bc4210858509b141ee0/server/index.ts#L7606).
SRC. Runtime selection between bounded coordination and other execution paths.
Only targeted relevant sections were inspected; this is not a complete security audit.

### S26

[Official source repository](https://github.com/milind-soni/OpenMausBot).
Official project identity, README, Apache-2.0 license, application architecture.
Acquired using a shallow sparse clone. No dependency installation or project execution occurred.

### S27

[Connected apps](https://docs.openmausbot.com/docs/connected-apps).
DOC. Managed versus self-hosted connection setup, account aliases, per-bot tool grants, disconnect behavior.
The page's “signed desktop” wording does not override S01's explicit unsigned Windows installer status.

## APEX source register

All links below are relative to this bundle. The inspected checkout HEAD is bf5eee796c709b513fcfd726a9f47e0742af5c4c.
Existing working-tree changes mean HEAD alone is not an exact snapshot of every file. See the source fingerprint manifest.

| ID | Local first-party source | Research use |
|---|---|---|
| A01 | [Start here](../00-START-HERE.md) | Scope, activation, five invariants |
| A02 | [Architecture](../ARCHITECTURE.md) | Main-conversation roles; bounded workers; explicit non-goals |
| A03 | [Glossary](../GLOSSARY.md) | Validation versus approval; roles versus state |
| A04 | [Run workflow](../workflows/orchestrator-run.md) | Ten-phase loop |
| A05 | [Detective workflow](../workflows/detective-review.md) | Blind review and aggregation |
| A06 | [Operator gate](../workflows/operator-gate.md) | Confirmation records and fetch-back |
| A07 | [Packet schema](../schemas/handoff-packet.schema.md) | Cross-role envelope |
| A08 | [Authority schema](../schemas/authority-state.schema.md) | Evidence closure and verified state |
| A09 | [Review schema](../schemas/review-verdict.schema.md) | Criterion-level verdict requirements |
| A10 | [Role directory](../../../.claude/agents/) | Seven actual role definitions |
| A11 | [Backbone integration](../agents/meta-ops/INTEGRATION-apex-plan-sync-session.md) | Plan / Sync / Session boundaries |
| A12 | [User stories](../user-stories/user-stories.md) | Seven real workflow patterns |
| A13 | [Idea simulation](../simulations/US-IDEA-01-20260711.md) | Full-pass record plus residual findings |
| A14 | [Strategy simulation](../simulations/US-SEQ-01-20260712.md) | Partial pass, gate still required |
| A15 | [Contract checker](../../../scripts/orchestration_check.py) | Implemented checks and limitations |
| A16 | [Negative fixtures](../tests/negative/RESULTS.md) | Recorded tests, rerun during research |
| A17 | [Weekly skill](../../../.claude/skills/weekly-orchestrator/SKILL.md) | Separate weekly stages and G1–G5 |
| A18 | [WF program](../new_final_v4/workflow_plans/00_META_PROGRAM_PLAN.md) | Ten domain workflow plans, not execution proof |
| A19 | [WSL migration index](../architecture-improvements/03-wsl2-native-stack-consolidation/index.md) | Later reported infrastructure state |
| A20 | [OpenProject handover](../architecture-improvements/04-leela-mastery-openproject-consolidation/00-handover.md) | PM scope, account fleet, unresolved taxonomy |
| A21 | [Informatics standard](../../informatics/standard.md) | Bundle structure and source discipline |
| A22 | [System manifest](../CURRENT-SYSTEM-MANIFEST.yaml) | Live versus historical classification |

## Reproduction and custody

The temporary upstream checkout was acquired at:
C:\Users\gehma\AppData\Local\Temp\openmausbot-research-1261ed9d439340db8da6b21d31b47f2a.

This bundle does not depend on that temporary directory. Permanent pinned URLs and fingerprints identify its sources.
No secret-containing configuration or chat history was copied into this research.
A credential-like literal was encountered in WF07; its value is deliberately excluded.
Local product inspection covered executable metadata and CLI presence, not account credentials, live bot profiles, or existing conversations.

Do not treat this bundle's self-check as independent Detective review. Its authority remains candidate.
