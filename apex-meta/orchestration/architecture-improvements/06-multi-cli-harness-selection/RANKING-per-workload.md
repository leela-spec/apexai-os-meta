---
type: Analysis
id: RANKING-MULTICLI-WORKLOAD-20261109
title: "Multi-CLI harness ranking per operator workload"
description: "Four separate rankings for weekly orchestration, multi-agent orchestration, MoA content creation and mindful-bar development, each with weights derived from the workload's own measured demands."
status: candidate
date: 2026-11-09
tags: [orchestration, ranking, cli-agents, workload-fit]
---

# Harness ranking per workload

Replaces section 2 of RESEARCH-MULTICLI-HARNESS-20261109, whose single ranking is invalidated in `AUDIT-ranking-validity.md`. One ranking per workload, because the four workloads make different demands and the single table hid that.

## The finding that reshapes every ranking

Three of the four workloads are **not parallel coding-agent work**, which is what the entire candidate field is built for.

| Workload | Repository | Measured composition | Orchestration already in repo |
|---|---|---|---|
| Weekly orchestration | `apexai-os-meta` | Claude Code skills and subagents | **Yes** — `.claude/skills/weekly-orchestrator/SKILL.md`, stages G1-G5, `execution: context_fork` |
| Multi-agent orchestration | `apexai-os-meta` | Claude Code skills and subagents | **Yes** — `apex-meta/orchestration/00-START-HERE.md`, five invariants, Alfred / Meta Ops / Meta Detective |
| Content creation | `MasterOfArts` | 8,005 tracked files: 5,083 `.md`, 1,076 `.py`, 222 `.html` | No `.claude/skills`, no `.claude/agents` |
| Product and company development | `mindful-bar` | 424 tracked files: 310 `.md`, 46 `.py` | No `.claude/skills`, no `.claude/agents` |

Consequences:

1. **For the two Apex workloads the harness must supply accounts and process supervision, not orchestration.** Both systems already decompose work, isolate reviewer context, hold gates and persist state to files. A harness that brings its own journal, task database or memory injection competes with them. CAO's memory feature writes delimited content into `AGENTS.md` and `CLAUDE.md` (source document line 117) — a direct breach of invariant 1 and invariant 5, and of the repository's own no-full-file-rewrite rule.
2. **For MoA and mindful-bar the binding constraint is quota, not parallelism.** Neither needs git worktrees, PR review or CI surfaces, which is most of what the candidate field optimises.
3. **Antigravity is not required by any of the four.** The P0 Antigravity block therefore costs nothing here, and every ranking below assumes Antigravity support is switched off. This is the cheapest way to clear the hardest gate in the source document.

Shared facts applying to all four rankings, verified 2026-11-09:

- **Paseo** runs natively on Windows (`Paseo-Setup-0.15.3-x64.exe`, release v0.15.3), Apache-2.0, free.
- **Orca** states support for macOS, Windows and Linux, MIT, free.
- **OpenMausBot** ships Mac, Windows, Linux and phone apps, Apache-2.0, free for the desktop app. It is **already installed and populated on this host**: `~/.openmausbot/` holds `bots/`, `decisions/`, `events/`, `memory-journal/`, `meetings/` and `codex-instructions/`. It is an incumbent, not a trial candidate, and the source document never notes this. Adoption cost is near zero; the corresponding obligation is to audit what the existing install can already reach (`TEST-PLAN.md`, T03).
- **CAO** raises `ImportError` on `sys.platform == "win32"` and requires tmux 3.3+. On this host it exists only inside WSL2.
- **Between the two Paseo account plugins, ZeroSub is the better-evidenced choice** (D-05): five contributors against one, pushed today against eight days stale, 22 forks against one, and `paseo-accounts` incorporates Kapybara-copyright portions, meaning it derives from ZeroSub rather than validating it. Every "Paseo + plugin" entry below means **Paseo + ZeroSub**.
- **Neither plugin has real-account Codex or Windows evidence.** This is the single open risk common to all four rankings and the reason `TEST-PLAN.md` exists.

## 1. Weekly orchestration — `apexai-os-meta`

The loop is a sequential gated pipeline: PrecapWeek (G1), PrecapNextDay (G2), operator execution (G3), flow-recap (G4), status-merge (G5), with durable mutation routed through `apex-session` and deterministic computation through `scripts/apex_sync.py`. Runs are short, interactive and gate-bound. Daily cadence is the real requirement.

**Weights.** Non-interference with gates, permissions and root instruction files 35%; reliable scheduled triggering 20%; native Windows operation 20%; quota continuity 15%; own orchestration features 5%; own durable journal 5%. The last two are low because the loop already owns both and a second owner violates the "one owner per canonical workflow state" rule (source line 128).

| Rank | Choice | Why | Against it |
|---|---|---|---|
| **1** | **Paseo + ZeroSub** | Native Windows; thin process supervisor that launches the unmodified CLI; scheduling built in; the plugin states a fork "never gets more permissions than the original agent", which preserves G1-G5 gating | Plugins run unsandboxed with the daemon's credential access (source line 113); Codex and Windows failover unproven |
| **2** | **Orca** | Native Windows, MIT, best-evidenced of the field (E80 R53), and manual account selection is *sufficient* for a loop whose stages are short | Account switching applies to new sessions only; no automatic rotation (issue 20512 open) |
| **3** | **OpenMausBot** | Native Windows, Apache-2.0, strong scheduling, and its bots can hold long-lived roles | Its Chief-and-team model duplicates Alfred and Meta Ops; heaviest surface for the lightest workload |
| **4** | **CAO** | Strongest durable journal in the field | Disqualified twice: no Windows support, and its memory feature writes into `AGENTS.md` and `CLAUDE.md`, breaching invariants 1 and 5 |

## 2. Multi-agent orchestration — `apexai-os-meta`

Alfred intake, Meta Strategy framing, Meta Ops routing, bounded specialist lanes, two blind Meta Detective lenses, operator gates. Runs are long and token-heavy, with parallel specialist lanes. This is the workload most likely to exhaust an account mid-run.

**Weights.** Quota continuity 30%; non-interference 25%; parallel process supervision 20%; native Windows 15%; scheduling 10%.

| Rank | Choice | Why | Against it |
|---|---|---|---|
| **1** | **Paseo + ZeroSub** | The only candidate that is both native-Windows and designed for same-provider rotation; supervises parallel agents without owning their state | Rotation unproven for Codex on Windows — the decisive unknown for this workload specifically, since it holds two Codex accounts |
| **2** | **CAO** | Genuinely the best fan-out and resumable journal, and its reviewer isolation matches the Detective lanes | WSL2-only on this host, and adopting its journal recreates the competing task database line 19 forbids. Viable only as a WSL2-side experiment on a copy of the repository |
| **3** | **Orca** | Reliable fleet view and account homes; safest thing to run against a live repository | Manual rotation does not survive a long unattended run; cross-provider handoff defect open (issue 35806) |
| **4** | **OpenMausBot** | Cross-provider takeover already works in the field (issue 3892) | Same-provider rotation still an open request (issue 3092), and an external child CLI finishing does not notify the originating bot (issue 5030) — fatal for an unattended multi-lane run |

## 3. Content creation — `MasterOfArts`

5,083 markdown files across roughly thirty domains, an Obsidian vault, heavy qmd indexing (`moa-root`, `moa-website`, `moa-business`, `moa-acim`, `moa-sequencing`, `content-creation` and more). Long generative sessions, high token volume, no worktrees, no CI. Publishing to channels is part of the output.

**Weights.** Quota continuity 40%; fidelity of long-session continuation after a switch 20%; connectors and publishing surfaces 15%; native Windows 15%; own orchestration 10%.

| Rank | Choice | Why | Against it |
|---|---|---|---|
| **1** | **Paseo + ZeroSub** | Quota continuity is 40% here and this is the only candidate built primarily for it; ZeroSub's account-specific Codex continuation tabs address the exact seam this workload hits | Codex conversations cannot move between accounts — the plugin's own `OVERVIEW.md` says Codex "encrypts them per account", so a switch starts a new agent with a transcript, not the original thread. For long-form content this is a real quality risk, not a formality |
| **2** | **OpenMausBot** | Closest fit after accounts: schedules, app connectors via Composio, a chat surface suited to non-coding production, and long-lived role bots per content domain | Same-provider rotation open (issue 3092), so the 40% criterion is only partly met |
| **3** | **Orca** | Manual account selection plus good session management | Manual switching is worst-matched to precisely the workload that exhausts accounts |
| **4** | **CAO** | — | Built for tmux-hosted coding fan-out; no Windows; nothing it adds serves markdown content production |

## 4. Product and company development — `mindful-bar`

A cacao-bar company in planning: 310 markdown files across `company/`, `products/cacao-bar/`, `customers/`, `brand-and-sales/`, `finance/`, `systems/`, plus 46 helper scripts and a vendored OpenProject skill copy. This is business automation with a documentation substrate, not software development.

**Weights.** Business automation and app connectors 30%; long-lived role agents 20%; quota continuity 20%; native Windows 15%; scheduling 15%.

| Rank | Choice | Why | Against it |
|---|---|---|---|
| **1** | **OpenMausBot** | The one workload where its model is the right shape: persistent bots per function (brand, finance, customer research), a Chief coordinating them, app connectors, schedules, and phone access for a founder-facing workflow. Apache-2.0, Windows app, free for self-hosted desktop use — and **already installed on this host**, so there is nothing to adopt, only to scope | Rotation gaps (issues 3092, 5030); a Chief's new bots inherit the Chief's connected apps and access level, so connector scope must be set deliberately before any bot is created |
| **2** | **Paseo + ZeroSub** | Accounts and supervision with the least surface; keeps the repository's authoring blueprint and OpenProject custody rules intact | No business connectors; nothing addresses the 30% criterion |
| **3** | **Orca** | Safe, well-evidenced, Windows-native | Coding-fleet product aimed at a repository that is 73% markdown |
| **4** | **CAO** | — | No Windows; worktree and tmux model irrelevant to company planning |

## 5. Summary

| Workload | 1st | 2nd | Decisive criterion |
|---|---|---|---|
| Weekly orchestration | Paseo + ZeroSub | Orca | Non-interference with G1-G5 and root instruction files |
| Multi-agent orchestration | Paseo + ZeroSub | CAO (WSL2 only) | Quota continuity across long parallel runs |
| MoA content creation | Paseo + ZeroSub | OpenMausBot | Quota continuity and continuation fidelity |
| mindful-bar | OpenMausBot | Paseo + ZeroSub | Business connectors and long-lived role bots |

**Operative reading.** Paseo + ZeroSub is the single harness that serves three of four workloads, and mindful-bar is the one case for a second product. CAO wins nothing here: the capability that earned it rank 2 in the source document is orchestration the operator already owns, and it cannot run on this host outside WSL2. Orca remains the correct fallback if automatic rotation proves unreliable on Windows, since manual selection is enough for the weekly loop.

Every first place above rests on one unproven claim — same-provider rotation on Windows with Codex. `TEST-PLAN.md` is scoped to settle exactly that, at zero cost, before anything is adopted.
