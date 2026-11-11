---
type: Research
id: RESEARCH-MULTICLI-HARNESS-20261109
title: "Five-account native CLI orchestration harness — evidence-gated selection"
description: "Comparative research on local Claude Code, Codex and Antigravity orchestration, quota continuity, durable execution, skills, learning, security and applicable provider terms."
status: candidate
date: 2026-11-09
tags: [orchestration, cli-agents, account-failover, comparison, mcda]
---

# Native CLI orchestration harness — 9 November 2026

**Decision status: RESEARCH / CANDIDATE. No product adopted; no five-account test executed; no installation or change of live Apex contracts authorized.**

## Target and outcome contract

The operator has **2 Codex accounts, 2 Claude Code accounts, and 1 Antigravity account**. Desired outcome: an established, inexpensive, open-source, locally operable harness that runs and supervises these accounts; executes role-based autonomous workflows; continues *authorized* work through supported account/provider failures; persists evidence and task status; enables verified lessons to improve future procedures; and optionally permits metered APIs only when explicitly authorized. Critical distinction: launching another account, handing off a task, and resuming an exact conversation without duplicated side effects are NOT the same capability.

**Existing Apex constraints:** Use the live [Multi-Agent Orchestration entrypoint](../../00-START-HERE.md), [current system manifest](../../CURRENT-SYSTEM-MANIFEST.yaml), and [Informatics standard](../../../informatics/index.md). Multi-Agent Orchestration and Weekly Orchestrator remain distinct; Plan-Sync-Session governs approved durable mutations. A harness is a proposed execution substrate, not new file/project/knowledge authority. Do not reimplement an agent runtime, create a competing canonical task database, promote agent memories into approved policy, or rewrite files.

**Research contract:** first party documentation and source > documented issue/reproduction > third-party evaluator with disclosed method > marketing claims. Prefer evidence dated in 2026 and distinguish observed behavior, implementation/documentation, open request, and inference. Source and limitation references appear in Section 7.

## P0 hard-gate findings

1. **Google Antigravity legal restriction:** Google's current [Additional Terms §6](https://antigravity.google/terms) explicitly identify accessing the Service through third-party software/tools (example: OpenClaw via Antigravity OAuth) as a breach potentially causing suspension. Google Enterprise is under potentially different accepted terms. An advertised official/ACP/agy adapter is evidence of technical feasibility, NOT permission. **Third-party Antigravity unattended execution is blocked pending terms-specific authorization/clarification**, including use by Paseo, Orca, CAO or OpenMausBot. This does not prevent independent use of the official Antigravity product according to its own terms.
2. **Anthropic authentication distinction:** [Claude Code legal/compliance](https://code.claude.com/docs/en/legal-and-compliance) permits an end user to authenticate the unmodified Claude Code binary using their own subscription, including where hosted in a platform, while restricting third-party developers who offer Claude.ai login or intermediate subscription OAuth. Their [account authentication guidance](https://support.claude.com/en/articles/13189465-log-in-to-your-claude-account) warns against routing third-party traffic against subscription quotas. Each plugin must be assessed for whether it launches the untouched CLI or intermediates/duplicates/refreshes credentials in a disallowed way. Never assume a plugin is approved because it works.
3. **OpenAI quota policy:** [OpenAI Terms](https://openai.com/policies/terms-of-use/) prohibit circumventing rate limits/restrictions. Having multiple legitimately owned accounts does not itself prove permission to pool/reset quotas. OpenAI also documents [multiple-account/device restrictions](https://help.openai.com/en/articles/20001559-understanding-card-and-device-limits-in-chatgpt). The new [Sign in with ChatGPT for open-source apps](https://developers.openai.com/siwc/token-sharing-open-source) is an expressly authorized alternative for *eligible* clients with consent and app limits; it is not synonymous with native Codex CLI process control or guaranteed additional quota. Use only authorized account identities and provider-approved flows.
4. **Paseo Antigravity safety:** [Paseo supported providers](https://paseo.sh/docs/supported-providers) says Antigravity is launched with --dangerously-skip-permissions, with **only Full Access** supported; native prompts cannot gate calls in this integration. Its transcript also starts fresh after daemon restart although agy retains conversation. Unsafe for an unrestricted live Apex repository; isolate in a disposable workspace if later permissible.
5. **CAO permission bypass:** The [CAO Claude provider](https://github.com/awslabs/cli-agent-orchestrator/blob/main/docs/claude-code.md) defaults to dangerous permission bypass; [Codex provider](https://github.com/awslabs/cli-agent-orchestrator/blob/main/docs/codex-cli.md) defaults to --yolo, disabling Codex's native sandbox unless stricter profile settings are applied. Do not accept a permissive default as a safe policy implementation.
6. **Evidence gap:** No reviewed, independently reproduced Windows/WSL pilot demonstrates all five accounts, quota-driven handoff, durable continuation, crash recovery, and Apex-compliant approvals in one supported setup. No product currently passes all gates on documentation alone.

## 1. Candidate discovery & hard screening

| Candidate                                             | Native provider fit                                                                                | Quota failover reality                                                                                                              | Durable workflow / learning                                                                                                          | Primary failure mode                                                                                                | Status                                                 |
| ----------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| **Paseo + Paseo Accounts** (jgreys)                   | Built-in Claude, Codex, agy                                                                        | Plugin implements same-provider rotation; real Claude failover **reported macOS-only**; Codex + Windows covered by tests/mocks only | SDK/MCP/CLI delegation, scheduling, skills; provider transcript/handoff, not a proven cross-run transaction journal                  | Third-party plugin full daemon access, unverified Windows/Codex failover, agy bypass, Antigravity terms             | Trial 1 if permitted                                   |
| **Paseo + ZeroSub**                                   | Same core                                                                                          | Separate maintained plugin claims Claude/Codex rotation and continuation, with Codex tab-aware handoff; macOS tested, Windows not   | Same Paseo controls                                                                                                                  | Limited external deployment evidence, plugin credential access, agy constraint                                      | Comparator to first row, do not install simultaneously |
| **AWS Labs CLI Agent Orchestrator (CAO)**             | First-party Claude, Codex, Antigravity CLI provider docs                                           | Provider account rotation not established as native feature                                                                         | **Strong**: resumable durable workflow journal, fan-out, five-scope memory, outcome capture, retrospector, explicit lesson promotion | Dangerous permissions by default; adapter/CLI status parsing; quota-specific handoff unproven                       | Trial 2, durable workflow benchmark                    |
| **OpenMausBot**                                       | Claude/Codex native; newer Google Antigravity ACP provider with isolated accounts                  | Cross-provider auto takeover exists; **same-provider account failover request OPEN**                                                | Bots, team/Chief, schedules, app connectors; claimed deeper harness functionality needs outcome-level tests                          | Auto notification to originating bot after external child CLI completes is open issue; authority/reviewer isolation | Trial 3, broad business automation                     |
| **Orca**                                              | Mature Claude/Codex account home isolation and manual hot-swap; agy Windows structural limitations | **Manual** same-provider hot-swap, open auto-rotation issue                                                                         | Fleet UI, session restart, handoff, worktrees, dashboard                                                                             | Restart/new session not lossless; open cross-provider handoff bug; Windows Antigravity chat issue                   | Trial 4, account fleet baseline                        |
| **Omnigent**                                          | Heterogeneous meta-harness incl. Claude/Codex/agy                                                  | Native five-account failover not established                                                                                        | YAML orchestration, policies, scheduling, agents and sandboxes                                                                       | Native Windows degraded; account transition and recovery tests missing                                              | Conditional challenger                                 |
| **Herdr**                                             | CLI process manager, mixed providers                                                               | Same-provider fallbacks advertised                                                                                                  | Persistent agent processes and terminal sessions                                                                                     | Antigravity five-account coverage and Windows real failover unverified                                              | Secondary                                              |
| **OpenClaw**                                          | Integrated models/auth profiles; external native CLI process workers not same primitive            | Auth-profile rotation for some model clients                                                                                        | Strong scheduling/integration platform                                                                                               | Confuses model auth failover with native CLI agent process supervision; provider legal constraints                  | Different layer / incumbent                            |
| **Hermes Agent**                                      | Native own agent/provider adapters                                                                 | Native external Claude/Codex CLI Kanban worker lanes not paved                                                                      | Strong Kanban, skills, curator learning                                                                                              | Existing native internal-agent path does not prove native five CLI worker orchestrator                              | Incumbent comparator, not discarded                    |
| **Multica**                                           | Claude/Codex/Antigravity listed                                                                    | Account handoff unknown                                                                                                             | Issues, retries, review, roles                                                                                                       | Additional Multica License conditions; no verified five-account continuity                                          | Conditional                                            |
| **ccswap / agentswap / Claudexor**                    | Focused multi-account Claude/Codex tools                                                           | Account rotation / session teleport proposed or implemented                                                                         | Incomplete complete orchestration, limited public evidence or single-purpose account layer                                           | Operational integration and credential security; cannot assume seamless in-flight state                             | Specialized donors only                                |
| **Emdash / T3 Code / Cloudroom / Agent Orchestrator** | Several native CLIs, may include agy                                                               | No verified target five-account rotation                                                                                            | Strong coding-agent UX, isolated worktrees, PR review/CI and remote surfaces depending on vendor                                     | Primarily code/worktree workflows, not verified cross-account recovery                                              | Landscape comparators                                  |
| **Anchor**                                            | Claude-focused not orchestration                                                                   | None                                                                                                                                | Local warnings, compaction/task handoff discipline                                                                                   | Maintainer explicitly says WARN-ONLY; cannot enforce a gate                                                         | Exclude as primary harness                             |

The candidate list is deliberately wider than the final pilot shortlist. The whole product must be assessed against the *operator's* outcome, not mere stars, tool presence, a schema PASS, or a checkmark.

## 2. Conditional multicriteria desk ranking

**Screening weights, 100%:** quota-aware continuation 25%, native CLI/account isolation 20%, durable task recovery 20%, orchestration/workflows/skills 15%, permissions and authority compatibility 10%, Windows/local/open-source feasibility 10%. Each raw criterion score is 1–5. Composite is a **transparent analyst assessment of documented feature-fit**, *not* an external benchmark, measured reliability, or evidence that legal gates pass. Gaps cannot be compensated for by a numeric score.

| Candidate | Quota 25% | CLI 20% | Durable 20% | Flow 15% | Gates 10% | Local 10% | Weighted /100 | Primary failure mode |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| **Paseo + one account plugin** | 4.0 | 5.0 | 3.0 | 4.0 | 2.0 | 4.0 | **78.0** | Plugin cannot prove Codex+Windows real failover; dangerous agy access |
| **CAO** | 1.5 | 5.0 | 5.0 | 5.0 | 2.0 | 4.0 | **74.5** | Account rotation gap, unsafe defaults |
| **OpenMausBot** | 2.0 | 4.5 | 3.5 | 4.5 | 3.0 | 4.0 | **69.5** | Same-provider failover and external child CLI completion gaps |
| **Orca** | 2.0 | 4.5 | 3.0 | 3.0 | 3.0 | 4.5 | **64.0** | Rotation remains manual; handoff bug |
| **Omnigent** | 1.5 | 4.5 | 3.0 | 4.0 | 3.0 | 3.0 | **61.5** | Windows degraded and quota failover gap |

**Apex significance scores:** independent raw operator value (I), evidence specifically for user configuration (E), and risk/downside (R), 1–100; do not combine these into a formula.

| Candidate | Significance estimate | Interpretation |
|---|---|---|
| Paseo + plugin | [P0 / I98 E48 R78] | Most targeted existing solution, but substantial real-device/test/legal risk |
| CAO | [P0 / I95 E73 R78] | Strongest documented durable orchestration/learning; unsafe defaults and no native rotation |
| OpenMausBot | [P0 / I93 E67 R67] | Broadest non-code automation fit, growing features not all shipped |
| Orca | [P1 / I88 E80 R53] | Strong account fleet/product evidence but not autonomous limit failover |
| Omnigent | [P1 / I84 E60 R70] | Promising meta-harness, limited fit proof |

**Evidence grading:** E scores do not imply independent production certification; credible first-party source code and documented issue reproductions still do not substitute for actual local user acceptance. Independent reviews by [Cloudroom](https://www.cloudroom.dev/blog/open-source-agent-orchestrators) disclose that the author works at a competing product and personally tested only some entries; [faun.dev comparator](https://faun.dev/toolbox/compare-coding-agent-orchestration-platforms/) provides an editorial multi-axis ranking, not quota-specific validation; [Repolode overview](https://repolode.com/en/collections/parallel-coding-agents) compares code-worktree tools, not cross-account recovery. Their relative editorial popularity cannot settle this decision.

### Decision triggers

- **Choose Paseo + one audited plugin** only if Claude/Codex subscription use and account controls are permitted for the actual setup, Windows real-CLI failover works, no billing escape path is enabled, approval/credential boundaries hold, and an interrupted multi-step task resumes without duplicate effects.
- **Choose CAO** if its durable workflow journal/recovery and gated learning materially beat Paseo on identical tasks, **and** the security profiles can be constrained **without** uncontrolled --yolo/permission bypass, while account exhaustion has a supported or separately authorized route.
- **Choose OpenMausBot** if non-code business automation, channels, schedules, and long-lived teams outweigh rotation shortcomings, after external job completion, app version, review isolation, and approval-chain proofs pass.
- **Choose Orca** if reliable manual multi-account selection is sufficient while automation is deferred; avoid describing its account switcher as automatic quota failover.
- **Do not select any system on green unit tests, GitHub stars, or a documented login picker alone.**

## 3. Required real-world pilot (one controlled, intent-preserving test suite)

**Do not spend usage just to manufacture a quota exhaustion.** Where permissible, first use built-in fake-provider/test fixtures for error classification; perform bounded authentic quota-trigger tests only against legitimately exhausted accounts and with explicit authorization. No credential contents in the report, commits or screenshots.

| Test | Actual outcome required | Evidence |
|---|---|---|
| T01 Five identity profiles | 2 Codex, 2 Claude, 1 independent Antigravity (or explicit legal BLOCK) visibly attributable | CLI version, authenticated identity labels redacted, process PID/host, login type, settings |
| T02 Parallel independent execution | Two authorized CLI tasks with no credential/session cross-contamination | Separate local homes, child processes, final SHA/output |
| T03 Claude quota handoff | After a genuinely reported limit on Claude1, legal and safe handoff to Claude2 without redoing completed effects | Provider error, rotation log, task/run ID, pre/post snapshot |
| T04 Codex quota handoff | Codex1->Codex2 *new continuation* with sufficient source instructions/diff; does not pretend private context transferred | Account attribution, handoff record, persisted evidence, duplicate-effect check |
| T05 Ordered cross-provider fallback | Explicit opt-in only; no silent API/paid-credit route; keep model/tool changes visible | Provider routing events, spend configuration, source/target identifiers |
| T06 Crash/resume | Crash after saved sub-step; completed verified sub-step never reexecuted | Durable journal, step hashes, restart action and output |
| T07 External job completion | A delegated background CLI job terminates and **automatically notifies/resumes the initiating coordinator** | PID/status/exit receipt and originating-run event |
| T08 Independent review | Reviewer has fresh isolated context and does not inherit builder's authority/memory | Separate reviewer transcript, proof, author/scope |
| T09 Unauthorized mutation | Attempt to change existing Apex file without authorized exact patch is blocked; no full-file rewrite | Negative test, diff and mutation-gate event |
| T10 Learning candidate | Real failure feedback becomes advisory lesson, not auto-modified policy | Outcome record, candidate lesson, no live AGENTS/CLAUDE edits |
| T11 Cost and resource | 0 unexpected API calls / resets / paid credits; bounded RAM/CPU, prompt/context overhead | Provider account usage, billing settings, logs |
| T12 Windows/WSL | Same provider versions and workspace paths actually work on user's Windows 11/WSL host | Full environment manifest and smoke result |
| T13 Schedule | Trigger a repeatable workflow exactly once; detect missed/duplicate triggers | Scheduler owner, run id, execution result |
| T14 Fail-closed interruption | Unknown outcome, cancellation, revoked authorization or broken handoff does not silently retry write | Durable stop record; safe human recovery path |

**Acceptance standard:** the human-facing artifact and repaired final task—not merely a successful shell exit, file presence or receipt—must be correct. For a real business workflow, include input/source priority, expected output and concrete review criteria. Current rejected/untested features are marked BLOCKED or UNVERIFIED, never PASS.

### Example vertical slice

Operator starts an Apex research task: collect three current primary sources, produce a comparative research note, have a different agent review citations, and save only an approved candidate artifact. The orchestrator records a stable task ID; launches a Claude worker on the approved official CLI; saves source URLs, findings and step receipt; uses a Codex reviewer in read-only context; on permitted account interruption selects an eligible account; passes concise immutable source/step manifest rather than secret chat state; validates output against the user's research intent; writes the approved file via scoped patch/file creation; logs the completed task; proposes a lesson from observed failure *without* silently changing Apex doctrine. A crash after evidence collection must resume from review rather than re-searching or overwriting already-approved outputs.

## 4. Real integration caveats

- **Paseo Accounts:** [overview](https://github.com/jgreys/paseo-accounts/blob/main/OVERVIEW.md) claims rotation; [TESTING](https://github.com/jgreys/paseo-accounts/blob/main/TESTING.md) explicitly reports real Claude account failover on **macOS 26, Paseo 0.12, Claude Code 2.1** and only automated tests for Codex switching beyond sign-in/usage, plus Windows. The [SECURITY](https://github.com/jgreys/paseo-accounts/blob/main/SECURITY.md) note says Paseo plugins run **unsandboxed** with daemon user's file/process/credential/network access. Its Codex transition starts a new session with previous transcript because private context is account-bound. This is precisely the critical unexplored seam for the user's 2 Codex logins.
- **ZeroSub:** [README](https://github.com/kapybara-org/zerosub/blob/main/README.md) documents account-specific Codex continuation tabs, guarded switches and own-provider fallback; current [catalog](https://paseo.cafe/plugins/zerosub/) notes Windows **untested**. Competes as alternative plugin, not an independent backup orchestrator. Do not install both plugins simultaneously against the same account homes.
- **Orca:** [account hot-swap](https://www.onorca.dev/docs/agents/codex-hot-swap) changes accounts for **new** sessions; existing processes retain their account. [Issue 20512](https://github.com/stablyai/orca/issues/20512) requests automatic quota failover; [issue 35806](https://github.com/stablyai/orca/issues/35806) reports Claude->Codex continuation prompt delivery failure; [issue 40321](https://github.com/stablyai/orca/issues/40321) asks to enable host agy ACP on Windows. Treat issues as reported reproducible concerns, not universally reproduced defects.
- **OpenMausBot:** [Antigravity provider](https://github.com/milind-soni/OpenMausBot/blob/main/apps/docs/content/docs/providers/antigravity.mdx) uses Google's separately installed ACP runtime and per-engine private Google homes. [Issue 3092](https://github.com/milind-soni/OpenMausBot/issues/3092) requests automatic **same-provider** account rotation. [Issue 3892](https://github.com/milind-soni/OpenMausBot/issues/3892) reports existing cross-provider takeover from exhausted Codex to Claude (even when another gateway was configured), confirming recovery is real but policy can be surprising. [Issue 5030](https://github.com/milind-soni/OpenMausBot/issues/5030) documents a bot not being automatically notified when an external CLI child process finishes; user must trigger later inspection. Product bot-as-engine support is distinct from spawning another CLI tool as a detached child.
- **CAO:** [workflows](https://github.com/awslabs/cli-agent-orchestrator/blob/main/docs/workflows.md) use deterministic step journals and re-execute workflow control scripts from the start, with recorded completed step values replayed. Unsettled steps halt pending a specific decision; do not confuse this with arbitrary exactly-once side-effect safety. [Self-learning](https://github.com/awslabs/cli-agent-orchestrator/blob/main/docs/self-learning.md) is opt-in: outcomes -> retrospector -> lessons, with manual instruction promotion. [Memory](https://github.com/awslabs/cli-agent-orchestrator/blob/main/docs/memory.md) may inject delimited content into AGENTS.md / CLAUDE.md: disable this on existing Apex root files until verified surgical-mutation policy is met. The [Antigravity provider](https://github.com/awslabs/cli-agent-orchestrator/blob/main/docs/antigravity-cli.md) also uses dangerous permission bypass in normal unattended execution.
- **Omnigent:** [official README](https://github.com/omnigent-ai/omnigent) describes SDK/native CLI integration and Windows degraded mode; full quota automation not established.
- **Multica:** [LICENSE](https://github.com/multica-ai/multica/blob/main/LICENSE) includes additional Part I commercial/branding restrictions; repository being public does not mean plain Apache-2.0.
- **OpenClaw/Hermes:** evaluate as **incumbent control planes**, but do not change their canonical role because a specialized account-switcher demos better.

## 5. Existing Apex architecture decisions preserved

- File-backed state, explicit activation, separate weekly system, action-scoped authorization and independent review are non-negotiable. Product-native learning remains **candidate** pending operator approval.
- Avoid an always-on giant context prompt. Source ranking and progressive disclosure remain necessary independent of the chosen UI.
- No uncontrolled whole-file rewrites. Existing files can change only through the repository's exact-match patch/AST discipline. This report was created as a **new research document**, not a modification to canonical spec, skills or procedures.
- Favor native features and documented extensions; a new custom adapter is authorized only if the incumbent's established interface is insufficient **and** its value is verified. No speculative multi-stack rewrite.
- Keep one owner for each canonical workflow/task state; distinguish service-side run logs, knowledge/evidence, and accepted project status.

## 6. Practical decision sequence

1. Verify provider terms and account authorization; distinguish provider-owned native CLI logins from plugin-managed login intermediaries. If unclear, leave that provider outside the automated test rather than treating a working login as permission.
2. Choose between *automatic quota continuity* and *maximum general-purpose workflow/learning* as the criterion that would reverse the choice. Both matter; first test the existing target-specific solution (Paseo + one audited plugin), then CAO journal/review path on the **same fixture**.
3. Use Orca as the manual multi-account baseline and OpenMausBot as the business-automation challenger; evaluate whether any provides materially better operator outcomes, not just more buttons.
4. Record actual Windows/WSL versions and reproduce T01-T14 in disposable workspaces with real CLI process logs. Score output quality, duplicate side effects and operator actions, not merely checkboxes.
5. Accept **one** harness only after the result has equivalent or better product quality, safe approvals and a credible authorized account policy. Keep already-functioning Apex/Hermes responsibilities until then.

## 7. Source register and evidence quality

**Official product / direct implementation:**
- https://github.com/getpaseo/paseo and https://paseo.sh/docs/supported-providers (core CLI adapters, agy Full Access caveat)
- https://github.com/jgreys/paseo-accounts/blob/main/TESTING.md and SECURITY.md (actual vs mocked plugin tests, credential boundary)
- https://github.com/kapybara-org/zerosub and https://paseo.cafe/plugins/zerosub/ (alternate account plugin and platform tests)
- https://www.onorca.dev/docs/agents/codex-hot-swap and https://www.onorca.dev/docs/agents/claude-code (account homes; manual hot-swapping)
- https://github.com/awslabs/cli-agent-orchestrator/blob/main/docs/workflows.md and docs/self-learning.md (durable workflows and learning)
- https://github.com/milind-soni/OpenMausBot/blob/main/apps/docs/content/docs/providers/antigravity.mdx (official ACP-backed agy accounts)
- https://github.com/omnigent-ai/omnigent (cross-harness support)
- https://github.com/nousresearch/hermes-agent and https://github.com/openclaw/openclaw (incumbents)

**Primary user reports / negative evidence:**
- https://github.com/stablyai/orca/issues/20512 and /issues/40321 and /issues/35806 (auto-rotation, Windows agy, cross-provider handoff)
- https://github.com/milind-soni/OpenMausBot/issues/3092 and /issues/3892 and /issues/5030 (auto account rotation, provider takeover, child-CLI completion)
- https://github.com/getpaseo/paseo/issues/3589 (per-profile auth config causing quota display gap)

**Provider agreements (must outrank product marketing):**
- https://antigravity.google/terms
- https://code.claude.com/docs/en/legal-and-compliance
- https://support.claude.com/en/articles/13189465-log-in-to-your-claude-account
- https://openai.com/policies/terms-of-use/
- https://developers.openai.com/siwc/token-sharing-open-source

**Secondary landscapes, not outcome-level validation:**
- https://www.cloudroom.dev/blog/open-source-agent-orchestrators (author discloses vendor affiliation; tested selected competitors)
- https://faun.dev/toolbox/compare-coding-agent-orchestration-platforms/ (multi-criterion editorial ranking, not cross-account benchmark)
- https://repolode.com/en/collections/parallel-coding-agents (open-source parallel coding tools; worktree emphasis)

**Research limitations:** This was GitHub API/official web documentation and issue-level verification, NOT a running Windows harness, paid-account integration, security audit or independent empirical reliability trial. No API usage, third-party plugin installation, paid account consumption, repo skill mutation, or native CLI execution was performed. Benchmarks requiring user-owned subscriptions and host access remain explicitly unverified.

**Operative conclusion:** The first promising feature-complete combination is **Paseo + one account plugin**, but it is not yet safe or proven for the target environment. **CAO** is the strongest durable-workflow and governed-learning benchmark; **OpenMausBot** is the business-automation candidate; **Orca** is the best documented manual multi-account control. A winner must pass real authorized quota/restart/reviewer/permission tests; do not convert a high desk score into false production authority.
