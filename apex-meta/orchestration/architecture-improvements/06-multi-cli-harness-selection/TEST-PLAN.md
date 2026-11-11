---
type: Procedure
id: TESTPLAN-MULTICLI-HARNESS-20261109
title: "Multi-CLI harness test plan, zero-cost first"
description: "Prepared, unexecuted test runs for Paseo plus ZeroSub, OpenMausBot, Orca and CAO, ordered so that the decisive unknown is settled before any install, any quota spend and any exposure of a live repository."
status: candidate
date: 2026-11-09
tags: [orchestration, test-plan, cli-agents, windows]
---

# Test plan — multi-CLI harness

Scope: settle the one claim every ranking in `RANKING-per-workload.md` depends on — **same-provider account rotation on Windows, with Codex** — before adopting anything. Phases run in order; each phase is a stop point.

**Standing constraints.** No live Apex, MasterOfArts or mindful-bar repository is exposed before Phase 3 passes. No provider quota is deliberately exhausted at any point. No credential value appears in any artifact. Antigravity support stays switched off throughout, which keeps the P0 legal block out of scope at no cost (no workload here requires it).

## Phase 0 — host capability probe — EXECUTED 2026-11-09

Read-only, no install, no network, no quota. Script: `probe-host.ps1` in this bundle.

| Check | Result | Consequence |
|---|---|---|
| `node` | v24.18.0 | Paseo plugins (npm packages) installable |
| `npm` | 11.16.0 | ready |
| `git` | 2.55.0.windows.3 | ready |
| `claude` | **2.1.310** | matches the Claude Code 2.1 line the plugin was tested against |
| `codex` | **not on PATH** | `~/.codex` exists with session history, so Codex has run here; the binary is not resolvable from this shell. A harness that launches `codex` by name will fail until PATH is fixed. **Resolve before Phase 2.** |
| `tmux` | ABSENT | expected; confirms CAO cannot run natively |
| `uv` | 0.12.0 (x86_64-pc-windows-msvc) | CAO's installer prerequisite is met, but the package still refuses to import on `win32` |
| `paseo` | ABSENT | not installed |
| `CLAUDE_CONFIG_DIR` / `CLAUDE_HOME` / `CODEX_HOME` | all unset | clean baseline: nothing currently forces a shared config directory, so per-account homes can be introduced without unpicking an existing override |
| `~/.claude`, `~/.codex` | present | live provider homes |
| `~/.openmausbot` | **present and populated** (`bots/`, `decisions/`, `events/`, `memory-journal/`, `meetings/`, `codex-instructions/`) | **OpenMausBot is already deployed on this host.** It is an incumbent, not a trial candidate. Its adoption cost for mindful-bar is near zero; its Phase 1 is an audit of the existing install, not a fresh one |

WSL2 footprint, measured separately: total RAM 31.6 GB, free 6.0 GB, `~/.wslconfig` already set to `memory=16GB` and `swap=4GB`, `vmmemWSL` resident at **0.94 GB**, one distro registered (`Ubuntu`). WSL2 is therefore not a material RAM cost — the CLI agent processes are, and they cost the same on either side. Still unmeasured inside the distro: `python3`, `tmux` and `uv` versions; required only if CAO reaches Phase 4, via `probe-host.ps1 -IncludeWsl`.

**A CAO trial must not go into the existing `Ubuntu` distro.** The global operating note keeps the `ki-basis` stack in a separate VM and off-limits to Windows workstation agents, and `.wslconfig` references that stack. Install into a dedicated distro instead.

## Phase 1 — static audit, still no install — EXECUTED 2026-11-09

| Test | Question | Result | Evidence |
|---|---|---|---|
| T01 | Does ZeroSub launch the unmodified `claude` / `codex` binary, or intermediate the OAuth flow? | **PASS** | `server/homes.ts`: "A managed account home is a real directory holding that account's own credentials and account state." `prepareClaudeHome` and `prepareCodexHome` build per-account homes, split per-account files (`.credentials.json`, `.session_ingress_token`) from shared config, write atomically under a config lock, and point the native CLI at the home through `CLAUDE_CONFIG_DIR` / `CODEX_HOME`. No token minting or proxying. This is the architecturally correct mechanism and the strongest available answer on provider-terms grounds |
| T02 | What filesystem and credential reach does a Paseo plugin have? | **Risk accepted, not a pass** | `paseo-accounts/SECURITY.md`: plugins run unsandboxed with the daemon user's file, process, credential and network access. ZeroSub additionally copies credential files into its managed homes (`syncOverlay`). Concrete consequence: the plugin holds your subscription credentials on disk and could read anything the daemon user can |
| T03 | Does OpenMausBot's existing install already hold bots, accounts or memory that would act on a repository? | **PASS, with findings** | `~/.openmausbot/` is live and active through today. Two bots (`bb2f252e…` last written 2026-11-04, `c68d0dad…` 2026-09-26). `providers/chatgpt-plan/` holds **2** account homes, `providers/antigravity/` holds **4**; no `providers/claude*` exists. `routines.json` (4,943 B) and `routine-checks.json` are registered, so schedules are already running. `memory-journal/` 475 KB, `events/` 2.9 MB, `codex-instructions/`, `decisions/`, `runtime.db`. **Not a trial candidate — an incumbent.** Scope what the two bots can reach before Phase 3 |
| T04 | Does CAO's memory feature write into `AGENTS.md` or `CLAUDE.md`, and can it be switched off? | **PASS** | `docs/memory.md`: the `claude_code` handler writes `<cwd>/.claude/CLAUDE.md` and the `codex` handler writes `<cwd>/AGENTS.md`, automatically "when a terminal of that provider is created in that cwd". Mitigations confirmed: each replaces **only its own delimited block**, not the whole file, and `cao config set memory.enabled false` / `CAO_MEMORY_ENABLED=false` is a global off switch that "always wins". Unsafe by default, correctable by configuration — so CAO is not excluded outright |

Also established in Phase 1, answering the account question directly (see `RANKING-weighted-model.md` §1): **CAO holds no accounts.** Profiles carry a `codexProfile` naming a `$CODEX_HOME/<name>.config.toml` config file and an `env` map, not an account; `providers/codex.py` states the provider "has no reliable way to resolve per-account from here"; `docs/claude-code.md` documents a single auth path; and `services/provider_error_classifier.py` classifies `rate_limited` for a retry decision, not a switch.

## Phase 2 — rotation proof in a disposable workspace

Install Paseo and **one** plugin (ZeroSub) against a scratch workspace. Never both plugins against the same account homes.

The method that avoids spending quota: both plugins expose a manual account control — disabling an account for a period, and a **Mark as available again** control. Disabling an account forces the rotation path without consuming a limit. Authentic limit-triggered tests run only against an account that is already legitimately exhausted.

| Test | Actual outcome required | Evidence |
|---|---|---|
| T05 | Two Claude accounts and two Codex accounts register with separate homes and no credential cross-contamination | Per-account config paths, distinct child PIDs, redacted identity labels |
| T06 | **Claude rotation on Windows.** Disable account 1 mid-task; the agent continues on account 2 | Rotation log, task id, pre- and post-state, no duplicated side effect |
| T07 | **Codex rotation on Windows — the decisive test.** Disable Codex 1 mid-task; record exactly what the successor receives | Account attribution plus a verbatim record of what crossed. The plugin's own `OVERVIEW.md` says Codex conversations cannot move because Codex encrypts them per account, so the expected result is a *new* agent with a transcript, not a resumed thread. The test measures how much task fidelity that costs, not whether the thread survives |
| T08 | Limit *detection* works on Windows without a macOS keychain | Usage and limit state read per account. `getpaseo/paseo` issue 3589 shows usage lookup resolving tokens from a hardcoded home with a macOS keychain fallback, in the custom-provider path. Confirm the plugin path does not inherit this |
| T09 | Daemon restart | Record what survives and what resets. Line 28 of the source document reports the transcript starting fresh after a daemon restart; confirm or refute on this host |
| T10 | No unexpected spend | Zero API calls, zero paid credits, zero resets consumed; provider usage page before and after |

**Gate.** T07 and T08 decide the programme. If Codex rotation does not work on Windows, or limit detection is unreliable, Paseo drops behind Orca for every workload and the recommendation becomes manual account selection.

## Phase 3 — non-interference against a repository copy

Run against a **copy** of `apexai-os-meta`, never the live checkout.

| Test | Required outcome | Evidence |
|---|---|---|
| T11 | No harness writes to `CLAUDE.md`, `AGENTS.md`, `.claude/skills/` or `.claude/agents/` | `git status` and full diff of the copy, before and after |
| T12 | Permission mode is never widened. A rotated or forked agent holds at most the original's permissions | Side-by-side mode comparison. The plugin claims "never gives a fork more freedom than you gave the original"; verify it |
| T13 | A weekly gate still blocks. Attempt a durable mutation outside the `apex-session` path and confirm refusal | Negative test, mutation-gate event |
| T14 | No full-file rewrite of any existing governed file | Diff shows exact-match patches only |

**Gate.** Any failure here excludes that product from both Apex workloads permanently, whatever Phase 2 showed.

## Phase 4 — one real vertical slice per workload

One task per repository, on a copy, scored on output quality and operator actions required — not on a green exit code.

| Workload | Slice | Harness under test |
|---|---|---|
| Weekly orchestration | One PrecapNextDay run, scheduled, triggered once, producing a real brief and flow cards | Paseo + ZeroSub; Orca as comparator |
| Multi-agent orchestration | One bounded run: Alfred intake, two specialist lanes, one Detective lens, one gate — with an account disabled mid-run | Paseo + ZeroSub |
| MoA content creation | One long-form content piece from `Content Creation/`, long enough to cross a rotation | Paseo + ZeroSub; OpenMausBot as comparator |
| mindful-bar | One company-development task using the existing OpenMausBot install and its connectors, with no new connector grants | OpenMausBot (incumbent audit) |

CAO enters Phase 4 only as a WSL2-side experiment, only if T04 found a memory off switch, and only against a repository copy inside WSL.

## Acceptance

A product is adopted only when the human-facing artifact is correct, no duplicate side effects occurred, no governed file was rewritten, no unexpected spend appeared, and the operator actions required are fewer than today. Anything untested is marked UNVERIFIED and anything refused is marked BLOCKED. Neither is ever recorded as PASS.

## Authorization still required

Phases 0 and 1 are done — both are read-only and cost nothing. **Phase 2 is the first step that installs anything**, and it installs third-party code that runs unsandboxed with the daemon user's credential access (T02). Phases 3 and 4 touch repository copies. Nothing beyond Phase 1 has been performed.

Next action when Phase 2 is authorized, in order: put `codex` on PATH; install Paseo 0.15.3 and **ZeroSub only**; register the four accounts against a scratch workspace; then run T06 and T07, which decide the ranking.
