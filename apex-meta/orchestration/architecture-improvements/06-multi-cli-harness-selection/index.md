---
type: Index
id: INDEX-MULTICLI-HARNESS-20261109
title: "Multi-CLI harness selection"
description: "Audit of the 9 November 2026 harness desk ranking, replacement rankings per operator workload, and the prepared test plan with its executed host probe."
status: candidate
date: 2026-11-09
tags: [orchestration, cli-agents, selection]
---

# Multi-CLI harness selection

Reviews `C:\Users\gehma\Downloads\2026-11-09-multi-cli-harness-operator-bakeoff.md` (RESEARCH-MULTICLI-HARNESS-20261109) and replaces its single desk ranking with per-workload rankings. Candidate status: nothing is adopted, nothing is installed beyond what the host already carried, and no provider quota was spent.

| File | Contains | Read when |
|---|---|---|
| `AUDIT-ranking-validity.md` | Fourteen numbered defects in the source ranking, the arithmetic recheck, the corrected ordering, and verified licence and cost facts for all seven products | Deciding whether the source ranking can be acted on |
| `RANKING-per-workload.md` | Four rankings — weekly orchestration, multi-agent orchestration, MasterOfArts content creation, mindful-bar development — each with weights derived from that workload's measured composition | Choosing a harness for a specific workload |
| `RANKING-weighted-model.md` | Sixteen weighted variables scored 1-100 per candidate, the yes/no answer on per-provider multi-account support, the measured WSL2 cost, and the sensitivity that decides the order | Comparing products across all criteria at once, or checking why a product sits where it does |
| `TRACTION-comparison.md` | Measured stars, age, contributor counts, commit activity, release cadence and download volume for all five products | Judging project health, or answering "how established is it?" |
| `TEST-PLAN.md` | Phase 0 (executed) through Phase 4 (prepared), ordered so the decisive unknown is settled before any install or quota spend | Before authorizing any installation |
| `PHASE2-RESULTS.md` | What was actually installed and measured on this host: integrity, plugin load, live quota detection, and the two tests still blocked | Checking real measured behaviour rather than documentation claims |
| `INSTALL-STEPS.md` | The ordered install sequence, which steps need the operator, and the measured ZeroSub 1.5.1 risk audit | Standing the infrastructure up, or deciding whether to accept the plugin |
| `probe-host.ps1` | The read-only Phase 0 probe | Re-measuring the host, or adding the WSL2 pass with `-IncludeWsl` |

## Conclusions

1. **The source ranking does not survive.** Its rank-1 score is arithmetically wrong (76.0, not 78.0), and the 25%-weighted quota criterion is scored 4.0 for a capability its own primary source reports as untested on Windows and untested for Codex — the operator's exact configuration. Corrected, CAO takes rank 1; CAO is then disqualified because it raises `ImportError` on Windows.
2. **The criteria were the wrong criteria.** Thirty-five percent of the weight rewarded durable journals and orchestration features, which the same document's constraints forbid adopting and which the operator already owns twice over in `.claude/skills/weekly-orchestrator/` and `apex-meta/orchestration/`.
3. **All four named candidates are open source and free to self-host.** Paseo Apache-2.0, ZeroSub MIT, Paseo Accounts MIT, CAO Apache-2.0, OpenMausBot Apache-2.0. The only cost is the provider subscriptions already held.
4. **Within the Paseo option, ZeroSub replaces Paseo Accounts.** Paseo Accounts is 20 days old with 9 commits from one author, 8 days stale, and its licence carries Kapybara copyright — it derives from ZeroSub rather than serving as its independent comparator.
5. **Paseo plus ZeroSub serves three of four workloads; OpenMausBot serves mindful-bar and is already installed here.** CAO wins nothing on this host.
6. **One unknown decides everything above:** same-provider rotation on Windows with Codex. `TEST-PLAN.md` Phase 2 settles it without spending quota, by disabling an account rather than exhausting one.

## Added 2026-11-09, after Phase 1

7. **CAO holds no accounts at all** — not for Claude Code, not for Codex. Paseo with either plugin is the only candidate with automatic same-provider rotation; Orca has the accounts but switches manually; OpenMausBot switches only across providers. Full answer in `RANKING-weighted-model.md` §1.
8. **WSL2 is not a RAM problem on this host.** `vmmemWSL` is resident at 0.94 GB against 31.6 GB total, under a `memory=16GB` ceiling that is not a reservation. CAO's exclusion rests on accounts and defaults, not on WSL.
9. **The weighted model with future orchestration included ranks OpenMausBot first (65.5) and Paseo + ZeroSub second (62.4)** — but the gap is 3.1 points and both heaviest variables are unproven. Confirming rotation on Windows moves Paseo + ZeroSub to 69.6 and first place; failing it drops it to 54.2 and fourth.
10. **The answer is both products, not one.** OpenMausBot is the incumbent business-automation and scheduling layer and already runs here; Paseo + ZeroSub is the account layer for the Apex workloads and MoA content. CAO is a future-orchestration option to revisit in its own WSL2 distro with `memory.enabled false`.

## Added 2026-11-09, after the ZeroSub source audit

11. **ZeroSub 1.5.1 audits clean on the three properties that matter for a credential-handling plugin:** zero runtime dependencies, readable TypeScript source rather than minified bundles, and exactly one outbound host — `api.anthropic.com`, for quota reads and limit resets. No telemetry, no vendor endpoint. The residual exposure is the project's age and the possibility that a future version differs, which pinning to 1.5.1 contains. Full audit in `INSTALL-STEPS.md`.
12. **Paseo itself has no account management.** `paseo provider` exposes only `ls`, `models` and `diagnostic`. Multi-account support is entirely the plugin's contribution, so refusing the plugin reduces Paseo to orchestration plus single-account quota display.
