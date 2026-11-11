---
type: Report
id: RESULTS-MULTICLI-PHASE2-20261109
title: "Phase 2 results — Paseo and ZeroSub installed and measured on Windows 11"
description: "Install, integrity, plugin load and live quota detection measured on the operator host, with the two rotation tests still blocked on second-account sign-in."
status: candidate
date: 2026-11-09
tags: [orchestration, test-results, paseo, zerosub, windows]
---

# Phase 2 results — measured on this host

Executed 2026-11-09 on Windows 11 Pro 26200, against an isolated daemon home so nothing touched `~/.paseo` or any live repository.

## What is now installed

| Item | Value |
|---|---|
| Installer | `Paseo-Setup-0.15.3-x64.exe`, 145,569,446 bytes (138.8 MB) |
| Source | `github.com/getpaseo/paseo` release v0.15.3, published 2026-11-06 |
| SHA-512 | matches the publisher's `latest.yml` manifest exactly — **VERIFIED** |
| Authenticode | **NotSigned** — no publisher code signature |
| Install path | `%LOCALAPPDATA%\Programs\Paseo` (per-user, no elevation, exit 0) |
| CLI | `%LOCALAPPDATA%\Programs\Paseo\resources\bin\paseo.cmd`, reports 0.15.3. Not added to PATH |
| Plugin | `@kapybara/zerosub` 1.5.1, installed from npm |
| Trial daemon home | the session scratchpad, **not** `~/.paseo` |
| Daemon | PID on `127.0.0.1:6767`, loopback only, relay disabled, CORS limited to `app.paseo.sh` |

## Test results

| Test | Result | Measured evidence |
|---|---|---|
| **T08 limit detection on Windows** | **PASS** | `paseo usage` returned live figures for both providers from their existing CLI logins: **Claude** session 0% used / 100% remaining, weekly 5% used / 95% remaining; **Codex** 5-hour 26% used / 74% remaining, weekly 48% used / 52% remaining. Fetched 2026-11-09T17:21:25Z. Issue 3589's macOS-keychain fallback concern does **not** bite on this host |
| **ZeroSub runs on Windows** | **PASS** | Plugin status `running`. The catalog page states "Windows is untested" — it now has one data point, and it works |
| **Account control surface exists** | **PASS** | ZeroSub registered 15 RPC methods: `zerosub.accounts.available / default / enabled / redeem / remove / rename`, `zerosub.agents.account`, `zerosub.agents.fork`, `zerosub.login.start / code / cancel`, `zerosub.state`, plus three settings methods. **`zerosub.accounts.enabled` is the lever the zero-cost rotation test needs** — disable an account to force the switch instead of exhausting a limit |
| Provider detection | **PASS** | Eight providers detected: claude, codex, copilot, opencode, pi, antigravity, muse (enabled), omp (unavailable) |
| Plugin reads Claude reset state | **PASS, informational** | `[ZeroSub] Claude limit resets for CLI login: not eligible (surface), 0 grant(s), 0 reset(s) left` — it queries the real login and reports honestly rather than guessing |
| **T06 Claude rotation** | **BLOCKED** | Only one Claude account is registered (the existing CLI login). Needs the second account signed in |
| **T07 Codex rotation** | **BLOCKED** | Only one Codex account is registered. Needs the second account signed in |

## Two findings worth recording

**A security default in Paseo's favour.** Third-party plugins do not load until `"pluginsEnabled": true` is set at the top level of `config.json`. It is **off by default**: installing a plugin succeeds, but the daemon refuses to start it (`Plugins are globally disabled`, raised at `@getpaseo/server/dist/server/server/plugins/index.js`). Enabling it is a deliberate, separate act. The installer also warns in plain words that "server code and preparation commands run unsandboxed on the daemon host" — which is T02's risk, stated by the vendor at the moment of consent.

**A correction to an earlier finding.** I reported that `codex` was "not on PATH" and flagged it as a Phase 2 blocker. Paseo detects the Codex provider and reads its quota regardless, so this was a scope issue in my own shell, not a harness problem. No PATH fix is needed.

## Comparison with the incumbent, on like-for-like data

Both products now have measured telemetry on this host, and they measure different things:

| | **Paseo + ZeroSub** | **OpenMausBot** |
|---|---|---|
| Accounts registered **today** | 1 Claude, 1 Codex (existing CLI logins) | **2 ChatGPT/Codex**, 4 Antigravity, 0 Claude |
| What it reports | **Remaining quota** — session, weekly and 5-hour windows, per account, as percentages | **Per-turn cost ledger** — `costUsd`, input/output/cached tokens, context window, model, outcome, tools, tool errors; 85 turns recorded in November |
| Purpose of that data | Decide *when to switch accounts* | Account for *what was spent and how a turn went* |
| Rotation | Automatic, same-provider — mechanism present, not yet proven | Cross-provider only; same-provider is an open request |

Neither telemetry substitutes for the other. Paseo answers "how much is left on this login"; OpenMausBot answers "what did that turn cost and did it succeed". For quota continuity the first is the one that matters.

## What only the operator can do next

T06 and T07 are the tests that decide the ranking, and both need a second account per provider. **Signing in is yours to do** — add the second Claude account and the second Codex account through the Paseo app or `zerosub.login.start` against the trial home. Once two of each are present, both tests run without spending any quota, by disabling an account with `zerosub.accounts.enabled` rather than exhausting it.

## How to undo everything

```
& "$env:LOCALAPPDATA\Programs\Paseo\resources\bin\paseo.cmd" --home <trial-home> daemon stop
```
The CLI is **not on PATH** — the bare name `paseo` fails with `CommandNotFoundException`. Then delete the scratchpad folder, and uninstall through `%LOCALAPPDATA%\Programs\Paseo\Uninstall Paseo.exe` if you want the app gone. Nothing was written to `~/.paseo`, no repository was touched, and no quota was consumed.
