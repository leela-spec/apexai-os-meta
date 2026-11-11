---
type: Procedure
id: INSTALL-MULTICLI-HARNESS-20261109
title: "Installation sequence — the infrastructure to stand up, in order"
description: "Ordered install steps for the selected harness stack, with the ZeroSub risk audit that gates step 3 and the account sign-ins only the operator can perform."
status: candidate
date: 2026-11-09
tags: [orchestration, installation, paseo, zerosub, windows]
---

# Installation sequence

What to stand up, in order, with who performs each step. Steps marked **OPERATOR** need credentials or a decision and cannot be delegated.

## Before you start — the CLI is not on PATH

`paseo` alone fails with `CommandNotFoundException`. The installer does not add its `bin` directory to PATH. Every command below therefore uses the full path:

```
C:\Users\gehma\AppData\Local\Programs\Paseo\resources\bin\paseo.cmd
```

To use the short name instead, add it once to the user PATH, then open a new shell:

```
[Environment]::SetEnvironmentVariable('Path', [Environment]::GetEnvironmentVariable('Path','User') + ';' + "$env:LOCALAPPDATA\Programs\Paseo\resources\bin", 'User')
```

The commands below are written with the full path so they work either way.

## What is already true on this host

| Component | State |
|---|---|
| OpenMausBot | **Installed and active.** 2 ChatGPT/Codex account homes, 4 Antigravity homes, live routines. No install work needed |
| Claude Code CLI | 2.1.310, one account signed in |
| Codex CLI | present (`~/.codex`), one account signed in |
| Paseo 0.15.3 | **Installed** at `%LOCALAPPDATA%\Programs\Paseo` |
| Trial daemon | **Stopped** 2026-11-09. Port 6767 released. Scratchpad folder still on disk, pending step 9 |
| `~/.paseo` (the permanent home) | **Created and running.** PID 39528 on `127.0.0.1:6767`, daemon 0.15.3, relay disabled, MCP endpoint disabled, voice disabled, CORS limited to `app.paseo.sh` |
| Plugin gate | **Open.** `pluginsEnabled: true` set by the operator 2026-11-09 and reloaded into the daemon. CORS, relay and MCP settings verified intact after the rewrite |
| ZeroSub in the permanent home | **Not installed.** `plugin ls` returns empty. Only `plugin install` remains |

Steps 2 and 3 are complete. Step 4 is the remaining install work, and it must be run by the operator: both the `pluginsEnabled` edit and `plugin install` were refused to the agent as unsandboxed-code-execution actions. That refusal is the gate working as designed — the one act that grants third-party code credential access stays a human decision.

## Step 1 — Decide on ZeroSub — **OPERATOR**

This gates everything after it. The audit is in §"ZeroSub risk audit" below. One decision: accept the plugin or stop at bare Paseo.

Consequence of stopping: bare Paseo gives agent orchestration across 8 providers and quota display for **one** account per provider. Its `provider` command offers only `ls`, `models` and `diagnostic` — there is no account management in Paseo itself. The second Claude account and the second Codex account stay unused.

## Step 2 — Stop the trial daemon first

**The trial daemon holds `127.0.0.1:6767`, which is also `onboard`'s default port.** Onboarding while it runs collides. Stop it before step 3, not at the end:

```
& "$env:LOCALAPPDATA\Programs\Paseo\resources\bin\paseo.cmd" --home "C:\Users\gehma\AppData\Local\Temp\claude\818acbd8bb9842e1\e37b89b3-e81d-497d-a0bd-08832ee21fdb\scratchpad\paseo-trial-home" daemon stop
```

Trial daemon PID 32804, running since 2026-11-09T17:18:30Z.

## Step 3 — Create the permanent Paseo home

```
& "$env:LOCALAPPDATA\Programs\Paseo\resources\bin\paseo.cmd" onboard --no-relay --no-mcp --voice disable
```

Creates `~/.paseo`, starts the daemon from persistent configuration, and prints pairing instructions.

The flags are deliberate rather than defaults: `--no-relay` keeps the daemon off Paseo's relay network, `--no-mcp` closes the Agent MCP HTTP endpoint, and `--voice disable` skips the local speech model download. Each is a surface no workload here needs. Drop a flag only when a workload actually requires it.

## Step 4 — Enable plugins and pin ZeroSub — **OPERATOR**

There is no CLI command for the global gate. `paseo plugin` offers `enable` and `disable` per plugin, but the top-level flag is config-file-only, so this edit is unavoidable and manual.

Plugins are refused until this is set at the **top level** of `~/.paseo/config.json`:

```json
{ "pluginsEnabled": true }
```

Paseo's own help calls this surface "Manage trusted, unsandboxed plugins" — the vendor states the T02 risk in the command description itself.

Then install the audited version explicitly, never a floating range:

```
& "$env:LOCALAPPDATA\Programs\Paseo\resources\bin\paseo.cmd" plugin install npm:@kapybara/zerosub@1.5.1
```

Pinning matters: the audit below covers 1.5.1 only. Re-audit before accepting any upgrade.

## Step 5 — Sign in the four accounts — **OPERATOR**

Two Claude accounts and two Codex accounts, through the Paseo app's ZeroSub panel or `zerosub.login.start`. Each lands in its own managed home with its own credential file.

Record which account is which label, because rotation logs refer to them by label.

## Step 6 — Prove rotation (T06, T07)

The decisive tests. Neither spends quota:

1. Start an agent on Claude account 1.
2. Disable account 1 with `zerosub.accounts.enabled`.
3. Confirm the agent continues on account 2 — rotation log, task id, no duplicated side effect.
4. Repeat for Codex. Expect a **new** agent with a transcript rather than a resumed thread: Codex encrypts conversations per account, so the thread cannot move. Measure how much task fidelity that costs.

**Gate.** If Codex rotation fails, the recommendation reverts to manual account selection and Paseo's value drops to orchestration only.

## Step 7 — Non-interference against a repository copy (T11–T14)

Against a **copy** of `apexai-os-meta`, never the live checkout. Confirm no harness writes to `CLAUDE.md`, `AGENTS.md`, `.claude/skills/` or `.claude/agents/`, and that a rotated agent never holds wider permissions than the original.

**Gate.** Any failure here excludes Paseo from both Apex workloads regardless of step 5.

## Step 8 — Wire one workload

One vertical slice, on a copy, per `TEST-PLAN.md` Phase 4. Start with MasterOfArts content creation — it is the workload with the least governance surface and the longest tasks, so it exercises rotation hardest with the least risk.

Leave the Apex weekly and multi-agent workloads until a slice has run clean, since both have gate contracts that a harness could plausibly disturb.

## Step 9 — Delete the trial folder

The trial daemon was already stopped at step 2. All that remains is deleting the scratchpad folder, once the permanent home is proven working.

## ZeroSub risk audit — version 1.5.1, measured on this host

Four properties were measured directly from the installed package, not from documentation.

| Property | Finding | Why it matters |
|---|---|---|
| **Runtime dependencies** | **Zero.** `node_modules` contains only `@kapybara`. Every dependency in `package.json` is a `devDependency` | No transitive npm supply chain. The trust boundary is Kapybara's own code and nothing else — this removes the most common compromise path for a small npm package |
| **Distribution form** | **Readable TypeScript source**, not minified bundles. 8,818 lines shipped; 6,294 in `server/` and `shared/` | Auditable by a person. `service.ts` is 1,998 lines, `continuations.ts` 640, `codex.ts` 548, `claude.ts` 488 — a real afternoon's reading, not an impossible one |
| **Outbound network surface** | **One host, three calls, all to `api.anthropic.com`**: `/api/oauth/usage?cedar_ember=1&skip_spend=1` twice, and `/api/organizations/{org}/reset_rate_limits` once. No other `fetch` or HTTP call exists in the server code | It does not phone home. There is no telemetry endpoint, no Kapybara host, no analytics. The usage call carries `skip_spend=1`, explicitly asking Anthropic not to bill the lookup |
| **Load gate** | `pluginsEnabled` is **off by default** at the top level of `config.json`. Installing succeeds; the daemon refuses to start the plugin until the flag is set | Enabling third-party code is a deliberate separate act, not a side effect of installing |

**The risk that remains, stated plainly.** Paseo plugins run unsandboxed with the daemon user's file, process, credential and network access, and ZeroSub copies provider credential files into its managed homes — that is how per-account homes work and there is no way to do it without touching credentials. The code in 1.5.1 does what it claims and reaches nowhere it should not. The exposure is not this version; it is that a 47-day-old project with 6 contributors and an MIT no-warranty licence holds credential-level access, and **a future version could differ**.

Two mitigations follow directly: pin the version, and treat every upgrade as a fresh decision rather than routine maintenance.

**What ZeroSub adds, precisely.** The second Claude account and the second Codex account, selectable per agent, switched automatically when one hits its limit. Nothing else in the stack provides this: bare Paseo manages providers but not accounts, CAO holds no accounts at all, and OpenMausBot switches only across providers. If the plugin is refused, the four subscriptions stay four separate manual logins, which is the situation today.
