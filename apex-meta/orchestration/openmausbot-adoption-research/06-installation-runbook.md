---
type: Research
title: "Installation and environment runbook"
description: "Installation and environment runbook for the APEX OpenMausBot adoption research."
status: candidate
date: 2026-09-27
---

# Installation and environment runbook

## Observed machine state

Read-only inspection on 2026-09-27 found:

| Item | Observation |
|---|---|
| Installed app | C:\Users\gehma\AppData\Local\Programs\OpenMausBot\OpenMausBot.exe |
| Executable product version | 0.1.88.0 |
| Downloaded installer | C:\Users\gehma\Downloads\OpenMausBot-setup.exe |
| Installer product version | 0.1.88 |
| Installer size | 235204516 bytes |
| SHA-256 | 08d737c86ddc40a6d4bc003f238aada0a32c872c1bda9e8bd1b3f57d32d49d6b |
| Official release match | Exact size and SHA-256 match to v0.1.88 |
| Claude executable | C:\Users\gehma\.local\bin\claude.exe |
| Codex executable | Discovered inside the locally installed Codex application |
| Python | python --version returned Python 3.12.10 |
| Git | Executable discovered |

No reinstall is needed to begin the readiness check.
The research did not launch the app, change its configuration, authenticate engines, or inspect personal chats.
Executable presence does not prove first-run setup or successful provider access.
Evidence: [S01–S02](14-source-register.md#s01), local command receipts in [validation](16-validation-report.md).

## Proposed installation principle

Use the official released desktop package for the first Windows pilot.
Keep source checkouts for evidence and controlled engineering, not as an accidental second production server.
Pin the chosen release in the pilot record.
Recheck the installed build before relying on features inspected on main.

The package embeds its harness.
Source-build requirements such as Node and pnpm are not automatically desktop-user prerequisites.
Agent engines remain separately installed and authenticated.

## Readiness sequence

| Step | Action | Evidence to capture | Stop condition |
|---|---|---|---|
| I01 | Open installed app and inspect version | App version and selected host | Version or host identity unclear |
| I02 | Inspect Settings → Engines | Detected CLI path/version and account alias | Missing CLI or authentication |
| I03 | Select one supported Claude model | Exact live model identifier | Model unavailable |
| I04 | Confirm pilot conversation is Ask | Conversation-level mode | Full/Custom or inherited elevation |
| I05 | Select an isolated pilot working folder | Resolved absolute host path | Unclear Windows/WSL path ownership |
| I06 | Inventory available tools without exercising services | Names and provider origin | Unexpected write-capable connectors |
| I07 | Confirm canonical project agents and skills load | Discovery receipt | Missing procedure dependencies |
| I08 | Run one harmless source-reading task | Exact file citation and output | Fabricated source access |
| I09 | Run a bounded native worker test | Actual worker identity and tools | No reliable subagent route |
| I10 | Stop before canonical mutation | Pilot run packet | Missing reviewed and confirmed basis |

This is a future runbook. None of I01–I10 is claimed executed during this research.

## Choose the execution host explicitly

### Windows desktop

Best initial fit when the first pilot reads this Windows checkout.
Use Windows paths for the provider actually launched on Windows.
Do not assume a shell tool automatically runs inside WSL because the repository also has Linux copies.

Advantages: installed app, existing discovered CLIs, direct operator interaction.
Open question: which filesystem contains the accepted current project state?

### WSL/Linux host with desktop client

Consider when execution must operate on native ext4 workspaces and the existing service network.
The official self-hosting and companion docs support a server/client split.
Engine authentication belongs on the execution host.
The Windows client does not transfer its local CLI accounts, repositories, or installed skills to that server.

This is an environment migration, not a mere working-folder edit.
Prove host identity, repository revision, file permissions, and service reachability first.
Use the repository's current WSL migration records; do not reinstall Docker Desktop from old workflow instructions.

### Always-on host

Consider only if unattended operation while the laptop sleeps is a real requirement.
Local routines require the harness to stay running.
A cloud computer assigned to a bot does not by itself make a sleeping local scheduler available.
Sources: [S10](14-source-register.md#s10), [S14–S15](14-source-register.md#s14).

## Optional external MCP setup

Only Option C needs this control interface initially.
The official Windows pattern uses the installed executable with its adjacent resources/server/mcp-server.js and ELECTRON_RUN_AS_NODE=1.
The external server can discover local app ports; a configured token requires a pinned port or URL.
Packaged mutating calls require a paired session.

Before connecting:

1. Verify the executable and bundled script actually exist.
2. Review the external client's exact requested tool scope.
3. Pair through the documented local app flow.
4. Store the token in private client configuration.
5. Pin the actual harness port.
6. Verify one read-only health call.
7. Exercise one explicitly scoped test task.
8. Verify revocation.

Do not place a bearer token in this project, a shared template, or an issue.
This runbook deliberately includes no fabricated executable paths beyond the observed install and documented relative script location.
Source: [S07](14-source-register.md#s07).

## Team package rollout

Create a package only after the pilot configuration is accepted.
The official sharing format is useful for distributing profiles, instructions, skills, groups, and paused routines.
It excludes credentials, selected models, and computers.
Imported skills and connections need their own review and activation.

A package is therefore a deployment input, not a complete installed orchestration system.
A valid import cannot prove role isolation or valid APEX mutation gates.
Source: [S09](14-source-register.md#s09).

## Update and rollback

Record the old app version, chosen installer digest, provider versions, and external project revision.
Create an appropriate app-state backup before a production upgrade.
Back up external project files separately.
Repeat the role, permission, context-isolation, and resume smoke tests after updates.

Do not assume an older binary can read a newer state database.
Rollback requires a compatible application version and a verified recovery copy.
No automatic downgrade procedure is asserted here.

## Windows symlink prerequisite

If a future skill setup reports missing symlink support, check Windows Developer Mode first.
The user's Windows defaults permit non-elevated symbolic-link creation in that mode.
Do not demand an elevated terminal merely because a skill-discovery link failed.
No Developer Mode setting was changed by this research.
