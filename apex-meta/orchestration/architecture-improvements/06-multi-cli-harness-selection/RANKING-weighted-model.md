---
type: Analysis
id: RANKING-MULTICLI-WEIGHTED-20261109
title: "Weighted variable model and re-ranking of multi-CLI harnesses"
description: "Sixteen weighted variables scored 1-100 per candidate, with per-account integration answered yes or no from source, the measured WSL2 cost on this host, and the sensitivity that decides the outcome."
status: candidate
date: 2026-11-09
tags: [orchestration, ranking, mcda, cli-agents, multi-account]
---

# Weighted variable model and re-ranking

Supersedes the composite in `RANKING-per-workload.md`. The per-workload rankings there remain valid; this file adds the explicit variable set, the weights, and a single composite that includes the newly stated requirement for future agent-orchestration workflows.

## 1. Does each product hold multiple accounts per provider? Yes or no

Asked plainly, answered from source. "Account" means a distinct provider login with its own credential store, not a config profile.

| Product | Claude Code multi-account | Codex multi-account | Automatic switch on limit | Mechanism |
|---|---|---|---|---|
| **Paseo + ZeroSub** | **Yes** | **Yes** | **Yes**, same-provider | `server/homes.ts` builds "a real directory holding that account's own credentials and account state" per account, via `prepareClaudeHome` and `prepareCodexHome`, and points the native CLI at it with `CLAUDE_CONFIG_DIR` / `CODEX_HOME`. Per-account files are split from shared config (`.credentials.json`, `.session_ingress_token`), written atomically under a config lock |
| **Paseo + Paseo Accounts** | **Yes** | **Yes** | **Yes**, same-provider | Same mechanism; the licence carries Kapybara copyright, so this is the derived implementation |
| **OpenMausBot** | **Partly** | **Yes** | **Cross-provider only** | Per-engine isolated homes, confirmed on this host: `~/.openmausbot/providers/chatgpt-plan/` holds **two** distinct account directories and `providers/antigravity/` holds **four**. No `providers/claude*` directory exists here, so Claude accounts are not in that store. Same-provider rotation is an open request (issue 3092); cross-provider takeover already works (issue 3892) |
| **Orca** | **Yes** | **Yes** | **No** — manual | Per-account homes with documented hot-swap, applied to **new** sessions only; running processes keep their account. Automatic failover is an open feature request (issue 20512) |
| **CAO** | **No** | **No** | **No** | CAO has no account concept. Profiles carry `codexProfile`, which names a `$CODEX_HOME/<name>.config.toml` **config** file, and an `env` map — not an account. The Codex provider's own source says `--profile` "resolves names relative to `$CODEX_HOME`, which this provider has no reliable way to resolve **per-account** from here". `docs/claude-code.md` documents one auth path: `claude setup-token` or `ANTHROPIC_API_KEY`. `services/provider_error_classifier.py` does classify a `rate_limited` signature, but the recovery decision it feeds is "retry, never replay" — not a switch |

**Short answer:** Paseo plus either plugin is yes for both providers with automatic same-provider switching. Orca is yes for both but manual. OpenMausBot is yes for Codex, not for Claude here, and switches only across providers. **CAO is no.** You could bolt per-account homes onto CAO by setting `CLAUDE_CONFIG_DIR` / `CODEX_HOME` in a profile's `env` map, but that is an unsupported workaround, it gives you static per-agent pinning rather than rotation, and the provider's own comment says it cannot resolve accounts.

## 2. Is WSL2 the right call? Measured, not estimated

Your instinct was that WSL2 would cost a lot of RAM. The measurement says you are already paying that cost and it is small.

| Measurement | Value |
|---|---|
| Total physical RAM | 31.6 GB |
| Free at probe time | 6.0 GB |
| `~/.wslconfig` | already present: `memory=16GB`, `swap=4GB` |
| `vmmemWSL` working set, running now | **0.94 GB** |
| Distros registered | `Ubuntu` |

Three conclusions:

1. **The WSL2 VM itself is not the cost.** It is resident at under 1 GB, and `memory=16GB` is a ceiling, not a reservation — your own comment in `.wslconfig` says so. Adding CAO adds a Python process and tmux, both small. The expensive part of any harness is the **CLI agent processes**, and those cost the same whether they run on Windows or in WSL.
2. **Your real constraint is the 6 GB free, not WSL.** Five concurrent CLI agents is the pressure point on a 31.6 GB machine that is already 81% committed, and that applies to every candidate equally.
3. **Do not install CAO into the existing `Ubuntu` distro.** Your global operating note states the `ki-basis` Linux stack runs in a separate VM and that Windows workstation agents must not invoke or touch it, and your `.wslconfig` comment references that stack. A CAO trial belongs in its own distro (`wsl --install -d <name>`), which costs disk rather than RAM and keeps the boundary intact.

So WSL2 is not the reason to rule CAO out. The reasons are that it holds no accounts (section 1) and that it writes into your root instruction files by default (section 3, V04).

## 3. The variables, and why each carries the weight it does

Scores are 1-100 per variable. Weights sum to 100 and are set by your situation: five accounts, a Windows 11 host, two existing Apex orchestration systems, four workloads of which one is business development, and a stated intention to run agent-orchestration workflows in future.

| ID | Variable | Weight | Why this weight for you |
|---|---|---:|---|
| V01 | Same-provider account rotation, Claude | 11 | Two Claude accounts. This is the original purpose of the exercise |
| V02 | Same-provider account rotation, Codex | 11 | Two Codex accounts, and the seam with the least evidence anywhere in the field |
| V04 | Non-interference with `CLAUDE.md`, `AGENTS.md` and gates | 10 | Apex invariants 1 and 5, plus the no-full-file-rewrite rule. A breach is a correctness failure, not a nuisance |
| V06 | **Future agent-orchestration workflow capability** | 10 | Newly stated. Weighted equal to non-interference because you want it to be possible later, not now — high enough to matter, not high enough to outrank what you need today |
| V03 | Windows 11 host operation | 9 | Hard constraint, but WSL2 exists and is already resident, so a POSIX-only product is penalised rather than excluded |
| V05 | Permission fidelity — never widens the original's permissions | 6 | Two candidates ship permission bypass as a default |
| V07 | Durable run recovery and resumability | 6 | Both Apex systems already persist state to files. A harness adds margin here, not foundation |
| V08 | Scheduling and unattended triggering | 6 | PrecapNextDay runs on a daily cadence |
| V09 | Long-session continuation fidelity after a switch | 6 | MoA content work crosses rotations mid-piece |
| V10 | Business automation and app connectors | 6 | One of your four workloads (mindful-bar) is company development, not coding |
| V13 | Credential and security boundary | 5 | Paseo plugins run unsandboxed with the daemon user's credential access |
| V11 | Maintenance and project health | 4 | Your contract asks for an *established* harness |
| V14 | Provider-terms compliance posture | 4 | P0 gates; lower than it looks because it is binary per deployment rather than graded |
| V12 | Licence and cost | 2 | Every candidate is open source and free. Almost no discriminating power |
| V15 | Resource footprint on this host | 2 | Measured as small for all candidates; the agents dominate |
| V16 | Adoption cost from today's state | 2 | Real but minor: one candidate is already installed here |
| | **Total** | **100** | |

## 4. Scores, 1-100

| Variable | W | Paseo+ZeroSub | Paseo+Accounts | OpenMausBot | Orca | CAO (WSL2) |
|---|---:|---:|---:|---:|---:|---:|
| V01 Claude rotation | 11 | 60 | 60 | 30 | 35 | **10** |
| V02 Codex rotation | 11 | 55 | 40 | 45 | 35 | **8** |
| V04 Non-interference | 10 | 85 | 85 | 50 | 85 | 50 |
| V06 Future orchestration | 10 | 70 | 70 | 85 | 55 | **95** |
| V03 Windows 11 | 9 | 70 | 70 | **95** | 85 | 35 |
| V05 Permission fidelity | 6 | 80 | 80 | 70 | 80 | 25 |
| V07 Durable recovery | 6 | 30 | 30 | 65 | 40 | **85** |
| V08 Scheduling | 6 | 75 | 75 | **90** | 45 | 55 |
| V09 Continuation fidelity | 6 | 60 | 45 | 50 | 30 | 15 |
| V10 Business connectors | 6 | 20 | 20 | **95** | 20 | 45 |
| V13 Credential boundary | 5 | 45 | 40 | 65 | 70 | 80 |
| V11 Maintenance health | 4 | 70 | **25** | 85 | 90 | 80 |
| V14 Terms posture | 4 | 75 | 75 | 40 | 70 | 85 |
| V12 Licence and cost | 2 | 90 | 90 | 90 | 95 | 95 |
| V15 Resource footprint | 2 | 60 | 60 | 50 | 60 | 65 |
| V16 Adoption cost | 2 | 50 | 50 | **95** | 50 | 30 |
| **Weighted total** | **100** | **62.4** | **57.8** | **65.5** | **56.3** | **47.5** |

Scoring notes that carry the result:

- **V01/V02** reflect that rotation is implemented and proven on macOS but has **no real-account evidence on Windows or for Codex**. That is why no candidate scores above 60 on the two heaviest variables. Paseo Accounts scores lower on V02 because its own `TESTING.md` puts Codex under "Only covered by automated tests"; ZeroSub documents account-specific Codex continuation tabs.
- **V04 for CAO is 50, not 25.** Phase 1 settled this: the `claude_code` handler writes `<cwd>/.claude/CLAUDE.md` and the `codex` handler writes `<cwd>/AGENTS.md`, automatically when a terminal of that provider is created in that directory — but it replaces only its own delimited block, and `cao config set memory.enabled false` (or `CAO_MEMORY_ENABLED=false`) is a documented global off switch that "always wins". Unsafe by default, correctable by configuration.
- **V04 for OpenMausBot is 50** because it maintains its own `codex-instructions/` and `memory-journal/` on this host, so instruction authorship is shared rather than left wholly to Apex.
- **V06 for CAO is 95** — it genuinely is the strongest orchestration substrate in the field: supervisor and worker roles, fan-out, a resumable step journal, five-scope memory, a retrospector, and twelve provider CLIs. That strength is real and is why the variable exists.
- **V14 for OpenMausBot is 40** because four Antigravity account homes already exist in its provider store on this machine, which makes the Google Additional Terms §6 question live here rather than hypothetical. Worth checking against your own accepted terms; this model does not assume the answer.
- **V11 for Paseo Accounts is 25**: 20 days old, 9 commits, one author, 8 days stale, 1 fork, 0 watchers.

## 5. Ranking

| Rank | Product | Score | Shape of the result |
|---:|---|---:|---|
| **1** | **OpenMausBot** | **65.5** | Wins on breadth and on already being here: native Windows, best scheduling, by far the best connectors, strong future-orchestration primitives, near-zero adoption cost. Weakest exactly where your original purpose lies — it does not rotate Claude accounts and rotates Codex only across providers |
| **2** | **Paseo + ZeroSub** | **62.4** | The only candidate that does the actual job — automatic same-provider rotation for both Claude and Codex — with a verified-correct mechanism. Held back by an unsandboxed plugin credential boundary and no business connectors |
| **3** | Paseo + Paseo Accounts | 57.8 | Same mechanism, thinner evidence, weaker maintenance, worse Codex coverage. Dominated by rank 2 on every variable where they differ |
| **4** | Orca | 56.3 | Healthiest project in the field and the safest thing to point at a live repository. Manual switching is what keeps it here |
| **5** | CAO (WSL2) | 47.5 | Best orchestration substrate, no accounts, POSIX-only, unsafe defaults. The 21 points on V06 and V07 cannot offset 22 points of V01 and V02 scored near zero |

## 6. The sensitivity that decides this

The gap between rank 1 and rank 2 is 3.1 points, and both heaviest variables are unproven. Phase 2 of `TEST-PLAN.md` resolves them:

| Outcome of T06 and T07 | Paseo + ZeroSub | New rank |
|---|---:|---|
| Rotation confirmed on Windows for both providers (V01, V02 → 90) | **69.6** | **1st**, ahead of OpenMausBot |
| As scored today (unproven) | 62.4 | 2nd |
| Rotation fails on Windows or for Codex (V01, V02 → 20) | 54.2 | 4th, behind Orca |

So the ranking is not really a ranking yet; it is a bet on one measurement. Run T06 and T07 and the order stops moving.

## 7. What this means in practice

**Both, not one.** They are not competing for the same slot:

- **OpenMausBot is already running here** with two bots and two ChatGPT accounts. It is your business-automation and scheduling layer, and it is the right answer for mindful-bar today. The work there is scoping what the existing install can reach, not installing anything.
- **Paseo + ZeroSub is the account layer** for the two Apex workloads and for MoA content, which is where quota actually binds. It is the only product that performs same-provider rotation automatically, and Phase 1 confirmed the mechanism is the architecturally correct one — per-account credential homes plus the unmodified native CLI.
- **CAO is a future-orchestration bet, not a current harness.** If you want its workflow substrate later, it runs in its own WSL2 distro with `memory.enabled false`, against repository copies. Not on the critical path now.
- **Orca is the fallback** if T06 or T07 fails.
