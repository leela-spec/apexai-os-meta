# APEX Local Executor — OpenClaw/ClawHub Skill Selection Decision Report

Status: research complete. Reuse-first order applied throughout: native → bundled → ClawHub → adapt/fork → custom.

---

## Section A — Executive Recommendation

Smallest viable stack. Almost everything required already exists as **native OpenClaw tools**. No browser-automation library, git wrapper, scheduler, or evidence subsystem needs to be built.

```
OpenClaw native:
- browser tool (profiles: openclaw / user / chrome-extension) — Workflows A, B, C
- exec tool (host=gateway, security=allowlist/ask/auto) — Workflow D
- git (via exec, plain CLI) — Workflow E (local ops)
- automations/cron (openclaw automations / openclaw cron) — Workflow F
- background tasks ledger (openclaw tasks) — Workflows G, H, J
- audit ledger (openclaw audit) — Workflow J
- skills precedence (workspace > project > personal > managed > bundled > extra) — Workflow I
- sandbox/workspace roots (per-agent workspace, Docker/SSH sandbox binds) — Workflow I

Bundled (ships with OpenClaw, enable only):
- browser-automation skill (snapshot/stale-ref/recovery loop, auto-loaded with browser plugin) — Workflow C
- github skill (gh CLI wrapper for issues/PRs/CI, alongside plain git for commit/push) — Workflow E

Community (ClawHub), install only if native+bundled is judged insufficient:
- none required for A/B/C/D/E/F/G/H/J at the "make it work" bar.
- Optional convenience only: a repo-scanning/knowledge skill (e.g. read-github) if deep code review across many repos becomes a bottleneck — not required for the vertical slice.

APEX-specific skill required (SKILL.md instruction packs, not new tools/code):
- "subscription-ai-web" skill: three short provider playbooks (ChatGPT, Gemini, Perplexity) that tell the agent, using only the native browser tool, which tab/profile to use, how to locate the composer, how to insert and verify a long prompt before Send, and when to stop and escalate (CAPTCHA/2FA/lost auth). This is markdown guidance, not code.
- "apex-evidence-receipt" skill: a short convention (file naming + hash/size/status fields) telling the agent what to write to disk and what compact receipt to hand back to the reasoning layer, reusing exec (sha256sum/Get-FileHash) and the browser tool's existing download/upload metadata. No new tool.
```

No custom submit_prompt_from_ref, capture_response_to_ref, browser wrapper, git helper, or scheduler is justified. See Section F for the evidence trail on each near-miss.

---

## Section B — Workflow-to-Skill Matrix

| Workflow | Recommended existing capability/skill | Alternative | Missing gap | Custom work required? |
|---|---|---|---|---|
| A. Prompt submission to subscription AIs | Native `browser` tool with `openclaw` (isolated persistent Chrome profile) or `chrome` (Browser Relay extension, works with nobody at the desk) profile, using `snapshot`→`act(type)`→`snapshot`(verify)→`act(click Send)` [web:72][web:45] | `user` profile (Chrome DevTools MCP attach to real signed-in Chrome) for cases needing the operator's own logged-in tabs [web:72] | No bundled/ClawHub skill encodes "insert exact long prompt, verify full text landed, then Send" per-provider UI steps | Yes — thin SKILL.md (provider playbook), no new tool |
| B. Wait/capture subscription-AI output | Native `browser` `wait` (URL/text/selector/JS predicate/networkidle) + `snapshot`/`act:evaluate` to pull only the response text, plus `download`/`waitfordownload` for file-based capture, all returning managed local paths, not full payload to Qwen [web:45][web:72] | none better found | No bundled skill defines "Deep Research completion" heuristics per provider | Yes — same provider playbook adds a "detect completion, don't false-truncate" checklist; capture writes to file via exec, receipt only returned |
| C. Browser recovery | Native `browser` tool: stable `tabId`/`suggestedTargetId` handles that survive tab replacement, `--efficient`/`--interactive`/`--compact`/`--selector`/`--depth` compact snapshots, stale-ref re-snapshot, dialog hooks, `doctor` health checks — plus the **bundled `browser-automation` skill** which already teaches this exact recovery loop [web:72][web:45] | ClawHub `agent-browser`/`browser-use`/`browser-automation` (Stagehand) community CLIs [web:55][web:81][web:82] | None found — native tool + bundled skill cover snapshot efficiency, stale-ref recovery, and modal handling directly | No |
| D. Deterministic scripts (Python/PowerShell) | Native `exec` tool: `host=gateway|node`, `security=deny|allowlist|ask|auto`, per-request approval, timeout, stdout/stderr capture, exit status, shell-snapshot aliasing [web:44][web:46][web:52] | none needed | None | No |
| E. Git/repository operations | Plain `git` CLI via `exec` for status/diff/add/commit/push (local ops); **bundled `github` skill** using `gh` CLI for PR/issue/CI [web:60][web:69] | ClawHub `git-notes-memory`, `github-kb` (convenience only) [web:64] | No native/bundled "policy layer" that hard-blocks `push --force`/`reset --hard` by itself | Yes — minimal: an exec allowlist/deny-pattern config (`security: allowlist`, deny `git push --force`, `git reset --hard`) is configuration, not code |
| F. Cron/scheduled orchestration | Native `openclaw automations`/`openclaw cron`: cron/interval/webhook triggers, `--agent` targeting, `--due`, run history, deterministic vs model-backed jobs distinguished by whether the job invokes exec directly or wakes an agent turn [web:47][web:48][web:51] | none needed | None | No |
| G. Immediate dispatch from orchestration | Native `openclaw message send`/`openclaw agent exec` to wake a session immediately (no polling), plus `openclaw tasks` for durable background-task tracking with push-driven completion notify [web:91][web:89] | Cron `--due`/one-shot job as fallback trigger | None | No |
| H. Long-running jobs and resume | Native background **tasks** ledger: `queued→running→terminal` lifecycle, survives Gateway restart via shared SQLite state, `lost` reconciliation after 5-minute grace, `tasks retry`/`tasks dismiss` for idempotent re-delivery after ambiguous failures, tab/process cleanup on completion [web:89] | none needed | Duplicate-submission prevention for a *browser* prompt-send action specifically (as opposed to task delivery) is not automatic | Yes — small: the provider playbook must include a pre-send idempotency check ("did I already submit this exact prompt in this tab?") using the browser snapshot, not a new subsystem |
| I. Multi-repository execution | Native skills-precedence model (workspace > project-agent > personal-agent > managed > bundled > extra-dirs) plus per-agent workspace + sandbox `workspaceRoot`/binds for scoping filesystem roots across repos [web:102][web:104][web:103] | Separate OpenClaw agent per repo, or one agent with multiple declared workspace roots | No single "multi-repo queue" primitive — but the task explicitly says not to build one | No — use existing per-agent workspace scoping; do not add a queue |
| J. Evidence and receipts | Native `openclaw audit` (identity/provenance/status ledger) + `openclaw tasks show` (timing, delivery state, terminal summary) already record what ran, when, and outcome [web:76][web:89] | none needed | Audit/tasks do not capture *project-level* artifact metadata (file hash/size/path of a research report) | Yes — minimal: the evidence-receipt convention (Section A) adds hash+size+path fields written by exec, referenced by task/audit ids already provided natively |

---

## Section C — Detailed Candidate Comparison

### Workflow A/B — Subscription-AI web automation

| Candidate | Mechanics | Auth model | Payload behavior | Score (0-100) | Verdict |
|---|---|---|---|---|---|
| **Native `browser` tool, profile=`openclaw`** [web:72] | Playwright+CDP, isolated dedicated Chrome profile, managed downloads dir | Manual one-time login in the `openclaw` profile, persists across restarts [web:73][web:77] | Snapshot/act returns bounded text; downloads/uploads return `{url, suggestedFilename, path}` handles, not raw bytes [web:72][web:45] | 91 | **Winner** |
| **Native `browser` tool, profile=`chrome` (Browser Relay extension)** [web:72][web:86] | Chrome extension relay, drives the user's real signed-in Chrome | Real Chrome login/session, no remote-debugging prompt, works headless-remote | Same bounded snapshot/act contract as above | 84 | **Runner-up** — use when the reasoning layer needs the operator's actual logged-in ChatGPT Plus/Gemini/Perplexity Pro session and Munich machine may be unattended |
| `gemini-browser` (ClawHub, @eccstartup) [web:94] | Browser Relay automation of gemini.google.com | Relies on Relay session | Unknown internals; **ClawHub flagged this skill as suspicious** | 15 | **Reject** — hard gate: unvetted, security-flagged |
| `chatgpt-image-generation` (@amian) [web:84] | Playwright automation of ChatGPT web UI, session-saved | Manual login, session persisted | Saves images to disk directly (good pattern) but scoped to image generation only, not general prompt/response text capture | 40 | Reference pattern only, not a fit for text prompt/response workflow |
| `agent-browser` / `browser-use` / Stagehand-based skills (ClawHub) [web:55][web:81][web:82] | Standalone CLI daemons duplicating Playwright/CDP snapshot+ref control OpenClaw's native browser tool already provides | Own session/profile handling, separate from OpenClaw's `openclaw`/`chrome` profiles | Generally compact (ref-based), but this is a second, competing browser stack | 35 | **Reject as primary** — redundant with native tool; would fragment session/profile state |

Decision: use the native `browser` tool exclusively (profile `openclaw` for background/scheduled sends, profile `chrome` when the operator's actual subscription session must be reused unattended, profile `user` only when someone is at the Munich machine to approve the CDP attach prompt). Write one **APEX SKILL.md** per provider (ChatGPT, Gemini, Perplexity) containing only the UI-specific selectors/verification steps — this is the smallest gap-filling artifact, and it is markdown, not code.

### Workflow C — Browser recovery / compact snapshots

| Candidate | Snapshot styles | Verdict |
|---|---|---|
| **Native browser tool + bundled `browser-automation` skill** [web:72][web:45] | AI (numeric ref), role (`--interactive/--compact/--depth/--efficient`, scoped by `--selector`/`--frame`), ARIA — all with `[new]` delta markers between snapshots to avoid re-sending unchanged trees | **Winner** — this already is the "compact/efficient/interactive-only/selector-scoped" mechanism the task asked us to find |
| ClawHub `a11y-debugging` (Chrome DevTools MCP) [web:56] | Full accessibility tree via `take_snapshot`, aimed at web-dev QA, not agent action refs | Not a fit — wrong purpose (accessibility auditing, not action-taking) |

Decision: no community skill needed; configure `browser.snapshotDefaults.mode: "efficient"` as the default extraction mode to keep Qwen's 32K context bounded [web:72].

### Workflow D — Deterministic scripts

| Candidate | Mechanics | Verdict |
|---|---|---|
| **Native `exec` tool** [web:44][web:46][web:52] | `host: sandbox|gateway|node`, `security: deny|allowlist|ask|auto`, per-command approval file (`~/.openclaw/exec-approvals.json`), timeout, stdout/stderr capture, exit status, PATH-resolved binary-path allowlist matching (pipeline segments individually checked) | **Winner**, no alternative needed |

Decision: set `tools.exec.security: "allowlist"` on the gateway/node host for Windows, populate the allowlist with `python.exe`, `powershell.exe`/`pwsh.exe`, `git.exe`, and specific project script paths. No wrapper skill required.

### Workflow E — Git/GitHub

| Candidate | Mechanics | Verdict |
|---|---|---|
| **Plain `git` via exec** | status/diff/add/commit/push through the allowlisted exec tool | **Winner** for local repo ops |
| **Bundled `github` skill** (`gh` CLI) [web:60][web:69] | PR/issue/CI/review/release operations | **Winner** for GitHub-hosted metadata, complements git |
| `git-notes-memory`, `github-kb` (ClawHub) [web:64] | Memory/knowledge-base layers on top of git | Not required for the vertical slice; optional later |

Decision: no git-specific "safety wrapper" skill exists on ClawHub that blocks `--force`/`reset --hard` by name — but this is fully solved by the native exec allowlist/deny mechanism (deny-list specific subcommands), which is configuration, not a new skill or tool.

### Workflow F — Cron

| Candidate | Mechanics | Verdict |
|---|---|---|
| **Native `openclaw automations` / `openclaw cron`** [web:47][web:48][web:51] | cron/interval/webhook triggers, `--agent` targeting, `--due`, run history via `openclaw cron runs`, deterministic (direct command) vs model-backed (wake agent) jobs both natively supported | **Winner**, no alternative needed |

### Workflows G/H — Dispatch, resume, idempotency

| Candidate | Mechanics | Verdict |
|---|---|---|
| **Native `message`/`agent exec` + `tasks` ledger** [web:91][web:89] | Push-driven completion (no polling loop needed), `queued→running→terminal` lifecycle persisted in shared SQLite, survives Gateway restart, `tasks retry`/`tasks dismiss` explicitly designed for **recovering blocked/ambiguous completions without duplicating the visible result** | **Winner** — this directly answers the "avoid duplicate side effects after ambiguous browser failure" research question for *task delivery*. It does **not** by itself prevent double-submitting a prompt inside a browser tab — that check belongs in the provider SKILL.md (Section A) |

### Workflow I — Multi-repo

| Candidate | Mechanics | Verdict |
|---|---|---|
| **Native skill precedence + per-agent workspace + sandbox `workspaceRoot`/binds** [web:102][web:104][web:103] | Workspace-scoped skills override shared ones; sandbox config exposes explicit `workspaceRoot`, Docker `binds` (`:ro`/`:rw`), SSH remote workspace roots | **Winner** — sufficient to run one agent against `apexai-os-meta` and per-project workspaces without inventing a queue |

### Workflow J — Evidence

| Candidate | Mechanics | Verdict |
|---|---|---|
| **Native `openclaw audit` + `openclaw tasks show`** [web:76][web:89] | Identity/provenance/status ledger; per-task timing, delivery status, terminal summary, retained result for 7 days | **Winner** for run-level evidence. Artifact-level metadata (hash/size/path of a generated report) is outside audit's scope by design ("audit never stores content") — this is the one legitimate small gap |

---

## Section D — Recommended Installation Set

| Name | Install command | Version/pin | Why | Permissions | Dependencies | Security status |
|---|---|---|---|---|---|---|
| Browser plugin (native, likely already default-on) | n/a — enable via config: `browser.enabled: true`, `plugins.entries.browser.enabled: true` | pinned to installed OpenClaw release | Core of Workflows A/B/C | Loopback control API, Playwright/CDP, no external network required beyond target sites | Playwright (bundled) [web:72] | First-party, native |
| `browser-automation` bundled skill | auto-available once browser plugin enabled; no separate install | n/a | Recovery loop for Workflow C | none beyond browser tool | none | First-party, bundled [web:72] |
| `github` bundled skill | `openclaw skills install github` (bundled slug; confirm via `openclaw skills info github`) | pin to bundled release version | Workflow E, GitHub metadata ops | `gh` CLI OAuth token (scoped, user-approved) | GitHub CLI (`gh`) [web:60] | First-party, bundled |
| Exec allowlist policy | config only: `tools.exec.security: "allowlist"`, populate `tools.exec.allowlist` | n/a | Workflow D, and Workflow E git safety | Whatever binaries you allowlist | none | Native, least-authority |
| Cron/automations | native, no install | n/a | Workflow F | Same as agent's normal tool grants | none | Native |
| APEX `subscription-ai-web` SKILL.md (custom, minimal) | `openclaw skills install ./path/to/subscription-ai-web --as subscription-ai-web` (local directory install) | v0.1 internal | Workflow A/B provider playbooks | none beyond browser tool | none | Internal, review before install |
| APEX `apex-evidence-receipt` SKILL.md (custom, minimal) | `openclaw skills install ./path/to/apex-evidence-receipt --as apex-evidence-receipt` | v0.1 internal | Workflow J artifact metadata convention | exec (hash/size), file paths only | none | Internal, review before install |

Do not install: any of the redundant browser-automation CLIs, the flagged Gemini skill, or any Perplexity/ChatGPT *API*-based research skill for this workflow (see Section E).

---

## Section E — What NOT to Install

- **`gemini-browser` (@eccstartup)** — ClawHub itself flags this as suspicious. Hard-gate reject regardless of description match [web:94].
- **Perplexity Agent/Search *API* skills** (`perplexity-research`, "Search the web with AI-powered answers via Perplexity API") — these use the provider API, not the subscription web UI, which the task explicitly excludes for Workflow A/B [web:95][web:97].
- **`agent-browser`, `browser-use`, Stagehand-based `browser-automation` (ClawHub)** — each is a full second browser-automation stack (own session/profile model, own snapshot format) duplicating the native `browser` tool. Installing any of these alongside the native tool creates two competing sources of truth for tab/session state — exactly the "ten competing browser frameworks" outcome the task told us to avoid [web:55][web:81][web:82][web:83].
- **`chatgpt-image-generation`** — legitimate skill, but out of scope (image generation, not prompt/response text capture); do not install for this executor.
- **Fastio / third-party cloud file-storage skills** (`fast-io`, `file-upload`/PDFAPIHub) — introduce an external cloud dependency for something the native browser tool's managed downloads directory and the local filesystem already solve; unnecessary cloud coupling for a local-first executor [web:92][web:93].
- **`git-notes-memory`, `github-kb`** — plausible future conveniences, not needed for the first vertical slice; adding them now is scope creep against "reuse before invention," not against invention itself, but against over-installing.

---

## Section F — Custom-Gap Report

### Gap 1 — Provider-specific prompt-insertion/verification playbook (Workflow A/B)
- Requirement: exact prompt insertion into ChatGPT/Gemini/Perplexity composer, verified in full before Send, provider-specific completion detection (including Deep Research), CAPTCHA/2FA/auth-loss escalation.
- Existing native capability checked: `browser` tool `snapshot`/`act`/`wait` primitives — fully sufficient as the *mechanism* [web:72][web:45].
- Bundled skills checked: `browser-automation` — teaches the generic snapshot/recovery loop but has no provider-specific selectors or "what counts as done" heuristics [web:72].
- ClawHub candidates checked: `gemini-browser` (security-flagged, reject), `chatgpt-image-generation` (wrong scope), Perplexity skills (API-based, wrong surface), generic browser CLIs (redundant stack) [web:94][web:84][web:97][web:55][web:81][web:82].
- Closest implementation: bundled `browser-automation` skill's operating loop (check status → label tabs → snapshot → act → resnapshot → recover stale refs → report manual blockers).
- Exact missing capability: knowledge of each provider's DOM/composer conventions and a completion/verification checklist — this is domain knowledge, not a tool capability.
- Why configuration/adaptation cannot solve it: no ClawHub skill encodes this without either being security-flagged or targeting the wrong surface (API vs. web UI, image vs. text).
- Minimum custom addition: one SKILL.md per provider (three total), each under ~1 page, listing composer selectors/snapshot cues, the "verify full text landed" step, and the completion/timeout heuristic. No new tool, no new code — purely instructional.

### Gap 2 — Duplicate-submission guard inside a browser tab (Workflow H)
- Requirement: avoid re-submitting the same prompt after an ambiguous browser failure.
- Existing native capability checked: `tasks retry`/`tasks dismiss` solve duplicate *delivery* of results, not duplicate *submission* of a browser action [web:89].
- Bundled/ClawHub candidates checked: none address in-page idempotency for chat-composer submission specifically.
- Closest implementation: `browser-automation` skill's stale-ref/resnapshot recovery loop, which already re-checks page state before re-acting.
- Exact missing capability: a specific "check the conversation for my last message before re-sending" step.
- Why configuration/adaptation cannot solve it: this is a one-line addition to the provider playbook (Gap 1), not a separate capability.
- Minimum custom addition: fold into the same SKILL.md as Gap 1 — no separate artifact.

### Gap 3 — Project-level evidence metadata (Workflow J)
- Requirement: hash, size, path, timestamp, status for generated artifacts, returned as a compact receipt.
- Existing native capability checked: `openclaw audit` (run/tool/message provenance, explicitly never stores content) and `openclaw tasks show` (timing/status/terminal summary) [web:76][web:89].
- Bundled skills checked: none provide artifact-level hashing/receipts.
- ClawHub candidates checked: none found purpose-built for this; cloud file-storage skills (Fastio, PDFAPIHub) solve a different problem (hosting/sharing) and add unwanted cloud dependency [web:92][web:93].
- Closest implementation: exec tool can already run `sha256sum`/`Get-FileHash`/`Get-Item` to produce the receipt fields natively.
- Exact missing capability: a standard receipt *format/convention* so every workflow returns the same compact fields.
- Why configuration/adaptation cannot solve it: this is a naming/format convention, not a capability gap — but writing it down as a skill avoids ad hoc formats per workflow.
- Minimum custom addition: one short SKILL.md defining the receipt schema (path, sha256, bytes, created_at, status, source_task_id/audit_run_id) and instructing the agent to populate it via existing exec commands. No new tool.

### Gap 4 — Force-push/destructive-command policy for `apexai-os-meta` (Workflow E)
- Requirement: block `push --force`, `reset --hard`, unrequested branch/worktree operations.
- Existing native capability checked: `exec` allowlist mode already supports per-binary and pipeline-segment allow/deny matching [web:44][web:52].
- Bundled/ClawHub candidates checked: `github` skill (gh CLI) does not gate raw `git` subcommands; no ClawHub git-safety-policy skill found.
- Closest implementation: exec allowlist config.
- Exact missing capability: none — this is fully solvable by configuration (deny-pattern entries for `push --force`/`--force-with-lease` variants and `reset --hard`).
- Why configuration/adaptation cannot solve it: it can. No custom code needed.
- Minimum custom addition: none — configuration only.

---

## Section G — Integration Recommendation

```
OpenClaw Gateway (Windows 11, HP OmniBook X Flip 16)
|
+-- Qwen3-8B (Q4_K_M, llama.cpp/Vulkan, 32K context) — reasoning-lite executor loop only
|
+-- native browser tool
|     profile "openclaw"   -> scheduled/background subscription-AI sends
|     profile "chrome"     -> unattended sends needing the operator's real logged-in session
|     profile "user"       -> attended sessions needing CDP attach approval
|     + bundled browser-automation skill (recovery loop)
|     + APEX subscription-ai-web skill (ChatGPT/Gemini/Perplexity playbooks, incl. dedup + Gap 2)
|
+-- native exec tool (host=gateway, security=allowlist)
|     + allowlisted python.exe / pwsh.exe / git.exe / project scripts
|     + deny-patterns for git push --force / reset --hard
|     + bundled github skill (gh CLI) for PR/issue/CI metadata
|
+-- native automations/cron
|     deterministic jobs -> direct exec command, no Qwen
|     model-backed jobs  -> wake agent turn via cron --agent
|
+-- native tasks + audit
|     tasks: durable queued/running/terminal ledger, resume after Gateway restart, retry/dismiss for ambiguous delivery
|     audit: run/tool provenance ledger
|     + APEX apex-evidence-receipt skill (artifact hash/size/path convention on top of exec + tasks/audit ids)
|
+-- per-agent workspace / skill precedence
      apexai-os-meta workspace and each project-repo workspace declared separately;
      workspace-scoped skills override shared ones automatically
```

No additional architecture layer is introduced. Everything above is either a native tool, a bundled skill, or a short markdown SKILL.md.

---

## Section H — Open Questions

**DECISION REQUIRED**
- Which browser profile is the default for scheduled/unattended subscription-AI sends: `openclaw` (fully isolated, requires one-time manual login per provider) or `chrome` (Browser Relay extension riding the operator's real logged-in session)? This affects whether ChatGPT/Gemini/Perplexity need separate logins inside the `openclaw` profile.
- Should `tools.exec.security` be `allowlist` (silent allow/deny) or `ask` (allowlist + human approval on miss) for the first vertical slice on `apexai-os-meta`? This is a risk-tolerance call, not a research gap.
- Exact deny-pattern list for git (only `push --force[-with-lease]` and `reset --hard`, or also `push --force` to `main` specifically vs. any branch)?

**LIVE TEST REQUIRED**
- Whether Chrome DevTools MCP (`user` profile) reliably attaches on this specific Intel Arc 140V / Windows 11 machine without repeated "Allow remote debugging?" prompts blocking unattended runs.
- Whether the Browser Relay Chrome extension (`chrome` profile) survives Windows sleep/hibernate cycles on this laptop without needing manual re-pinning.
- Actual Deep Research completion timing on Gemini/ChatGPT/Perplexity in practice, to calibrate the wait/timeout heuristic in the provider SKILL.md (cannot be determined from documentation alone).
- Confirm that `openclaw skills install github` resolves to the bundled slug documented above on the currently installed OpenClaw version (bundled skill naming can shift between releases).
