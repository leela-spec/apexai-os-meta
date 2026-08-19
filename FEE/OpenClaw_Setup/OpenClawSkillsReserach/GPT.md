# Decision report — OpenClaw stack for the APEX Local Executor

**Research date:** August 11, 2026  
**Decision rule applied:** native OpenClaw → bundled skill/plugin → vetted community skill → adapt → custom only with a demonstrated gap.

## Bottom line

The broad ecosystem search does **not** support building a new APEX browser layer, scheduler, Git wrapper, execution framework, session system, evidence database, or general payload-transfer framework.

The smallest coherent stack is:

### OpenClaw native / bundled

- **Native Browser + bundled `browser-automation` skill**
    
- **Core `read` / `write` / `edit` / `apply_patch`**
    
- **Native `exec` + Exec Approvals**
    
- **Built-in Automations/Cron**
    
- **Native agent/session dispatch**
    
- **Background Tasks + restart recovery + audit history**
    
- **Per-agent workspaces and skill scoping**
    
- **Bundled `github` skill**
    
- **Bundled `oracle` skill**
    

### Additional install

- **`@steipete/oracle@0.17.2` CLI** — strongly recommended for ChatGPT web workflows.
    
- **`@etherstrings/openclaw-gemini-web@0.1.5`** — recommended, but use **manual-login/session-reuse mode only**.
    

### Perplexity

- **Do not install a Perplexity community automation package yet.**
    
- Start with OpenClaw's native Browser + bundled browser-automation workflow.
    
- The strongest community Perplexity implementations I found either rewrite the prompt, are explicitly unsuitable for unattended automation, use their own Playwright stack/credentials, or use anti-bot/Cloudflare-bypass techniques.
    

### APEX-specific custom skill

**None required for the first vertical slice.**

There is one _possible_ small integration gap for Gemini/Perplexity: moving a very large text file into a web composer **as literal root prompt text**, rather than as an uploaded attachment, without passing it through Qwen. That should be tested before anything is built.

This conclusion is consistent with OpenClaw's own current guidance: use ClawHub before building a skill from scratch. ([OpenClaw](https://docs.openclaw.ai/tools/creating-skills "https://docs.openclaw.ai/tools/creating-skills"))

Your uploaded benchmark captures also confirm the machine assumed in the research: Core Ultra 7 258V, ~31.6 GB RAM and Arc 140V on Windows 11, across Geekbench 6/7 CPU and GPU runs.

---

# A — Executive recommendation

## Recommended stack

```text
OpenClaw Gateway
|
+-- Qwen3-8B Local Executor
|
+-- Native Browser
|     |
|     +-- bundled browser-automation
|     |
|     +-- ChatGPT
|     |     +-- bundled oracle skill
|     |     +-- @steipete/oracle CLI 0.17.2
|     |
|     +-- Gemini
|     |     +-- OpenClaw Gemini Web 0.1.5
|     |     +-- native browser underneath
|     |
|     +-- Perplexity
|           +-- native browser/browser-automation
|           +-- no community runtime initially
|
+-- Native filesystem
|     +-- read / edit / write / apply_patch
|
+-- Native exec
|     +-- PowerShell / Python / git / tests
|     +-- per-agent allowlist
|     +-- argv restrictions
|     +-- strictInlineEval
|
+-- bundled GitHub skill
|     +-- git for repository operations
|     +-- gh for GitHub operations
|
+-- Automations
|     +-- model-backed scheduled jobs
|     +-- exact deterministic command jobs
|
+-- Agent/session dispatch
|
+-- Background Tasks
+-- Restart recovery
+-- Audit history
|
+-- APEX artifact files
      +-- result
      +-- hash
      +-- byte count
      +-- compact receipt
```

The native browser already supports stable tab identifiers/labels, snapshots, screenshots, input actions, file upload/download, dialogs, existing signed-in Chrome sessions, bounded observations and local browser-control scripting. The bundled browser-automation skill adds the correct recovery loop: snapshot → act → resnapshot after UI changes → recover stale refs → stop on login/CAPTCHA/2FA rather than improvising. ([OpenClaw](https://docs.openclaw.ai/tools/browser "https://docs.openclaw.ai/tools/browser"))

**Key architecture decision:** use Oracle as a specialized **ChatGPT-web execution engine**, not as another reasoning layer. OpenClaw already bundles its skill. Oracle 0.17.2 is current as of August 10, 2026, and its latest release specifically repaired ChatGPT's redesigned model picker and hardened session/artifact permissions. ([GitHub](https://github.com/openclaw/openclaw/blob/main/skills/oracle/SKILL.md "https://github.com/openclaw/openclaw/blob/main/skills/oracle/SKILL.md"))

---

# B — Workflow-to-skill matrix

|Workflow|Recommended existing capability|Runner-up|Remaining gap|Custom now?|
|---|---|---|---|---|
|**A. Prompt submission**|**ChatGPT:** bundled Oracle + Oracle CLI. **Gemini:** Etherstrings Gemini Web/native browser. **Perplexity:** native browser/browser-automation.|Native browser for all three|Generic huge-file → literal composer text remains unproven for Gemini/Perplexity|**No**|
|**B. Response capture**|**ChatGPT:** Oracle sessions + direct output/artifacts. **Gemini/Perplexity:** native browser DOM extraction/download to durable file|Native browser throughout|Need live proof of full long-response extraction on Gemini/Perplexity|**No**|
|**C. Browser recovery**|Native browser + bundled `browser-automation`|None needed|Provider UI drift is unavoidable but recovery mechanics exist|**No**|
|**D. Scripts**|Native `exec` + approvals/arg restrictions|Deterministic automation command jobs|None material|**No**|
|**E. Git**|Core file tools + native exec + bundled `github` + git/gh|ClawHub GitHub copy|Repository-specific policy configuration|**No skill**|
|**F. Cron**|Built-in Automations|OS scheduler only for exceptional external bootstrap|None|**No**|
|**G. Immediate dispatch**|`openclaw agent` / session key / agent targeting|session messaging|None|**No**|
|**H. Long run/resume**|Background Tasks + native restart recovery; Oracle sessions for ChatGPT|Task Flow for genuine multi-step OpenClaw flows|Provider-side ambiguity still needs idempotent workflow behavior|**No**|
|**I. Multi-repo**|Per-agent workspaces + explicit cwd + skill scoping/precedence|Separate agents for repo classes|Configuration only|**No**|
|**J. Evidence**|Tasks + automation history + audit + artifact receipt|Task Flow state when appropriate|Audit intentionally does not contain artifact/hash data|**Receipt only**|

OpenClaw's current restart recovery is substantially stronger than a simple “session survives” mechanism: conversation state, interrupted main-session turns, subagents, background tasks, scheduled jobs and delivery queues are persisted/reconciled through SQLite across Gateway restarts. ([OpenClaw](https://docs.openclaw.ai/es/gateway/restart-recovery "https://docs.openclaw.ai/es/gateway/restart-recovery"))

---

# C — Detailed candidate comparison

Scores below apply your 100-point weighting. They are **research-fit scores**, not measured reliability benchmarks on your laptop.

## A/B — ChatGPT web

|Candidate|Submission|Capture/resume|Decision|
|---|--:|--:|---|
|**Bundled Oracle skill + Oracle CLI 0.17.2**|**94**|**97**|**Winner**|
|Native Browser + browser-automation|84|79|Runner-up|
|`placidusaxalarak/chatgpt-skill`|58|60|Reject|
|independent GPT-Web/CDP skills|~50|~55|Reject|

### Winner: Oracle

This is the strongest reuse-first discovery in the research.

OpenClaw already ships an Oracle skill whose declared dependency is the `@steipete/oracle` package. ([GitHub](https://github.com/openclaw/openclaw/blob/main/skills/oracle/SKILL.md "https://github.com/openclaw/openclaw/blob/main/skills/oracle/SKILL.md"))

Oracle itself:

- automates a **signed-in ChatGPT browser session**;
    
- supports a dedicated/persistent browser profile;
    
- supports selected files, directories and globs;
    
- persists runs under its own session store;
    
- supports reattachment and follow-up;
    
- has specialized long-run ChatGPT behavior;
    
- has Deep Research support;
    
- has recently fixed false/early completion, model-picker drift, attachment verification and long-running Pro capture failure modes. ([GitHub](https://github.com/steipete/oracle "https://github.com/steipete/oracle"))
    

Most importantly for APEX, Oracle already implements much of the **handle-not-payload** pattern.

Its CLI can consume prompts via stdin, attach files directly, and save final output directly to a target file. The result therefore need not transit Qwen merely for copying. Oracle also maintains durable session artifacts, and its browser bridge has explicit byte-count/SHA-256 handling for generated-file transfer. ([GitHub](https://github.com/steipete/oracle/releases "https://github.com/steipete/oracle/releases"))

Conceptually:

```text
prompt.md
   |
   | local deterministic stdin
   v
Oracle CLI
   |
   v
signed-in ChatGPT web
   |
   v
result.md / Oracle session artifacts
   |
   v
hash + size + receipt
```

That's extremely close to the APEX target without creating `submit_prompt_from_ref`.

Oracle also directly addresses duplicate/recovery risk: it stores sessions and instructs operators to inspect/reattach rather than blindly starting another run. ([GitHub](https://github.com/steipete/oracle/blob/main/README.md "https://github.com/steipete/oracle/blob/main/README.md"))

### Why not generic ChatGPT skills?

`ChatGPT Web Skill` is genuinely relevant, but it introduces its own browser automation/session implementation rather than leveraging the OpenClaw-native browser stack as cleanly as Oracle, and its maturity/security profile is weaker. ([ClawHub](https://clawhub.ai/placidusaxalarak/skills/chatgpt-skill "https://clawhub.ai/placidusaxalarak/skills/chatgpt-skill"))

Given Oracle's active development—1,600+ commits in the current repo view and an Aug 10 release responding directly to ChatGPT UI changes—there is little justification for APEX to maintain a separate ChatGPT automation implementation. ([GitHub](https://github.com/steipete/oracle/releases "https://github.com/steipete/oracle/releases"))

### Caveat

Oracle is not magically immune to ChatGPT UI drift. Recent issue history shows exactly these kinds of failures; importantly, the corresponding fixes have been landing upstream quickly. For example, the recent Deep Research menu regression was fixed upstream, and 0.17.2 fixed another redesigned model-picker breakage. ([GitHub](https://github.com/steipete/oracle/issues/281 "https://github.com/steipete/oracle/issues/281"))

That supports **pin + test + update**, not building our own replacement.

---

## A/B — Gemini web

|Candidate|Score|Decision|
|---|--:|---|
|**Etherstrings OpenClaw Gemini Web 0.1.5**|**86**|**Winner, with credential restrictions**|
|Native Browser + browser-automation|**82**|Strong runner-up|
|ECC `gemini-browser` Browser Relay skill|73|Viable fallback|
|Oracle Gemini browser route|Hard-gate fail for strict UI requirement|Do not use for this requirement|
|independent Playwright/Gemini stacks|~55–60|Reject|

### Winner: Etherstrings OpenClaw Gemini Web

This skill is specifically written around **OpenClaw's own managed browser** rather than introducing another browser framework. Its source explicitly says it is for the Gemini **web interface**, not Gemini API or Gemini CLI. It covers session reuse, new/continued/forked threads, uploads, normal web conversation and downloaded results. ([GitHub](https://github.com/Etherstrings/openclaw-gemini-web-skill/blob/main/skills/openclaw-gemini-web/SKILL.md "https://github.com/Etherstrings/openclaw-gemini-web-skill/blob/main/skills/openclaw-gemini-web/SKILL.md"))

It also adopts exactly the blocker policy APEX wants: CAPTCHA, phone confirmation, suspicious-login checks, recovery challenges, account lockouts and terms gates must stop for human intervention. ([GitHub](https://github.com/Etherstrings/openclaw-gemini-web-skill/blob/main/skills/openclaw-gemini-web/SKILL.md "https://github.com/Etherstrings/openclaw-gemini-web-skill/blob/main/skills/openclaw-gemini-web/SKILL.md"))

### Security

ClawHub currently rates version **0.1.5 Pass**, with **66/66 VirusTotal vendors clean** and no suspicious static patterns. ([ClawHub](https://clawhub.ai/etherstrings/openclaw-gemini-web/security/static-analysis "https://clawhub.ai/etherstrings/openclaw-gemini-web/security/static-analysis"))

There are, however, two legitimate medium findings:

- its TOTP helper can ingest MFA secrets;
    
- it permits TOTP secrets via command-line arguments, which can expose them in history/process listings. ([ClawHub](https://clawhub.ai/etherstrings/openclaw-gemini-web/security/static-analysis "https://clawhub.ai/etherstrings/openclaw-gemini-web/security/static-analysis"))
    

Therefore:

> **Install the skill, but do not use its credential/TOTP automation.**

Use a dedicated OpenClaw-managed browser profile, log in manually once, and reuse the authenticated session.

That removes the main security concern while preserving the valuable Gemini-specific UI runbook.

### Maturity caveat

The source repo is small and young—only a few commits—and therefore doesn't deserve Oracle-level trust despite its clean audit. ([GitHub](https://github.com/Etherstrings/openclaw-gemini-web-skill "https://github.com/Etherstrings/openclaw-gemini-web-skill"))

For that reason, the underlying browser remains OpenClaw-native. If the Gemini skill goes stale, removing it does not require changing the browser stack.

### Why Oracle isn't the Gemini winner

Oracle's own documentation distinguishes its two browser paths: **ChatGPT uses browser automation**, whereas Gemini browser mode is a **cookie-based Gemini client**. That is not the literal subscription-web-UI workflow specified here. ([GitHub](https://github.com/steipete/oracle "https://github.com/steipete/oracle"))

---

## A/B — Perplexity web

|Candidate|Score|Decision|
|---|--:|---|
|**Native Browser + browser-automation**|**80**|**Winner**|
|`sligt83/perplexity-web-search-skill`|65|Reference / possible adaptation|
|Official Perplexity plugin|Hard-gate fail|API, wrong surface|
|Perplexity PRO headless stacks|Hard-gate fail|Avoid|
|`Hantok/perplexity-pro-to-openclaw`|Hard-gate fail|Avoid|

This is the one provider where I did **not** find a community package strong enough to displace OpenClaw's native browser.

### Best community reference

`sligt83/perplexity-web-search-skill`:

- uses the signed-in Perplexity website;
    
- explicitly avoids the API;
    
- uses an existing signed-in browser;
    
- has no separate cloud API credential requirement. ([GitHub](https://github.com/sligt83/perplexity-web-search-skill "https://github.com/sligt83/perplexity-web-search-skill"))
    

But it is optimized for a **research assistant** rather than an exact executor. Its documented behavior includes tightening/reworking the user's question and compactly summarizing results. It also says it is not a good fit for unattended/high-frequency workflows. ([GitHub](https://github.com/sligt83/perplexity-web-search-skill "https://github.com/sligt83/perplexity-web-search-skill"))

That violates APEX's authority separation: **the executor must not rewrite the reasoning agent's prompt.**

It is therefore useful as a UI-flow reference, not as the production runtime.

### Official Perplexity plugin

OpenClaw's official Perplexity plugin is a proper supported component, but it uses the **Perplexity API**, so it fails this workflow's web-subscription hard gate. ([ClawHub](https://clawhub.ai/openclaw/plugins/perplexity-plugin "https://clawhub.ai/openclaw/plugins/perplexity-plugin"))

### Avoid anti-bot/headless implementations

A community “Perplexity Pro” implementation explicitly advertises Cloudflare bypass/“undetectable” browser automation. That is exactly the wrong operational model for APEX: another browser stack, account risk, unnecessary stealth behavior and extra maintenance. ([ClawHub](https://clawhub.ai/hantok/perplexity-pro-to-openclaw/security/virustotal "https://clawhub.ai/hantok/perplexity-pro-to-openclaw/security/virustotal"))

**Decision:** native OpenClaw browser first.

---

# C — Browser recovery

### Winner: Native Browser + bundled browser-automation — **97/100**

OpenClaw currently gives us:

- stable `tabId`s and human labels;
    
- raw target replacement handling;
    
- snapshots and screenshots;
    
- ref-based interaction;
    
- `evaluate`;
    
- wait operations;
    
- upload/download primitives;
    
- modal/dialog state;
    
- network/error/console debugging;
    
- existing-session Chrome support. ([OpenClaw](https://docs.openclaw.ai/cli/browser "https://docs.openclaw.ai/cli/browser"))
    

Stable tab identity is particularly good: raw Chromium targets can change during navigation, while OpenClaw maintains the stable `tabId` or label where it can prove replacement correspondence. ([OpenClaw](https://docs.openclaw.ai/cli/browser "https://docs.openclaw.ai/cli/browser"))

### Context efficiency

This is another area where a custom APEX abstraction is unnecessary.

OpenClaw's browser documentation explicitly supports targeted/efficient observation instead of blindly dumping the whole page, including selector-scoped extraction/evaluation and efficient snapshots intended for actionable controls. ([OpenClaw](https://docs.openclaw.ai/tools/browser-control "https://docs.openclaw.ai/tools/browser-control"))

So Qwen does **not** inherently need to ingest giant accessibility trees.

### File handling

The native browser has explicit local upload/download helpers. Managed browser downloads return controlled local file metadata, and uploads are constrained to approved OpenClaw media/upload roots rather than arbitrary filesystem paths. ([OpenClaw](https://docs.openclaw.ai/cli/browser "https://docs.openclaw.ai/cli/browser"))

That's an important least-authority feature.

### What not to add

Do not add Browser-Use/Agent-Browser/Patchright as another general browser layer. The Browser-Use community package introduces two independent browser frameworks, while Patchright exists partly to evade browser-detection mechanisms. ([ClawHub](https://clawhub.ai/yinj0012/openclaw-skill-browser-use "https://clawhub.ai/yinj0012/openclaw-skill-browser-use"))

---

# D — Deterministic scripts

### Winner: native `exec` + Exec Approvals — **98/100**

No shell wrapper is needed.

OpenClaw already lets host execution be constrained by:

- tool policy;
    
- allowlists;
    
- optional explicit approval;
    
- execution-host enforcement;
    
- canonical cwd;
    
- exact argv;
    
- pinned executable;
    
- local-script binding so an approved script cannot silently change between approval and execution. ([OpenClaw](https://docs.openclaw.ai/tools/exec-approvals "https://docs.openclaw.ai/tools/exec-approvals"))
    

For interpreters, `strictInlineEval` forces things such as `python -c`, `node -e`, `sed`, `awk`, `find -exec`, `xargs`, etc. through stricter approval paths rather than treating interpreter approval as arbitrary-code authority. ([OpenClaw](https://docs.openclaw.ai/tools/exec "https://docs.openclaw.ai/tools/exec"))

This is exactly what APEX needs:

```text
allowed:
python .\approved\validator.py input.json
pwsh -File .\approved\maintenance.ps1
pytest tests\focused\
git status
git diff

not automatically allowed:
python -c "<arbitrary>"
pwsh -Command "<arbitrary>"
```

**Recommendation:** `tools.exec.mode = allowlist`, not `full`.

And keep `autoAllowSkills` off for this executor's high-trust operational profile.

---

# E — Git/repository operations

### Winner: native filesystem + `exec` + bundled GitHub skill — **97/100**

OpenClaw already includes a bundled `github` skill. Its division of responsibility is sensible:

- ordinary **Git** for local repository operations;
    
- `gh` for GitHub-specific operations. ([ClawHub](https://clawhub.ai/steipete/github/security-audit "https://clawhub.ai/steipete/github/security-audit"))
    

Core OpenClaw already supplies the file-editing surface, so another Git/repository abstraction buys very little.

## Crucial finding for the APEX `main` policy

Exec approvals can constrain **arguments**, not just executable names.

Therefore the executor does **not** need a custom “safe Git” wrapper just to prevent:

```text
git reset --hard
git push --force
git rebase ...
git worktree ...
git branch -D ...
```

Use a per-agent Git allowlist whose argument patterns permit only the required command shapes.

For example, conceptually:

```text
git status
git diff ...
git add <scoped paths>
git commit ...
git push origin main
```

while nonmatching argv requires approval or is denied.

OpenClaw pins exact argv/cwd for approved host execution, and host policy can only become stricter, not looser, through the approval layer. ([OpenClaw](https://docs.openclaw.ai/tools/exec-approvals "https://docs.openclaw.ai/tools/exec-approvals"))

That is substantially better than relying only on Qwen remembering “don't force push.”

### Do not use Coding Agent here

OpenClaw's bundled `coding-agent` is appropriate for delegated coding-agent work, but its isolation/worktree/branch-oriented workflows conflict with the operator's direct-`main` policy for `apexai-os-meta`.

Use the normal filesystem/exec/Git stack for this executor.

---

# F — Cron / scheduled orchestration

### Winner: built-in Automations — **99/100**

There is no justification for another APEX scheduler.

OpenClaw distinguishes the two exact classes required.

## Model-backed scheduled job

```text
OpenClaw Automation
        |
        v
Qwen executor turn
        |
        +-- browser
        +-- files
        +-- exec
```

## Deterministic scheduled job

```text
OpenClaw Automation
        |
        v
exact argv command
        |
        +-- stdout
        +-- stderr
        +-- exit/run history
```

The command form is first-class:

```text
--command-argv '["node","scripts/report.mjs"]'
```

Command jobs capture stdout/stderr and normal run history; agent-turn jobs can target explicit sessions. ([OpenClaw](https://docs.openclaw.ai/cli/cron "https://docs.openclaw.ai/cli/cron"))

For APEX that means:

- weekly orchestration requiring browser/tool execution → **agent turn**;
    
- “run this exact validator every night” → **command automation**;
    
- no Qwen at all for deterministic maintenance.
    

---

# G — Immediate execution from orchestration

### Winner: native `openclaw agent` / session dispatch — **97/100**

Cron does not need to be the dispatch bus.

Current OpenClaw supports:

```text
openclaw agent
  --agent <id>
  --session-key <key>
  --message <text>

openclaw agent
  --agent <id>
  --session-key <key>
  --message-file <path>
```

and explicit session ID reuse. ([OpenClaw](https://docs.openclaw.ai/cli/agent "https://docs.openclaw.ai/cli/agent"))

That directly implements:

```text
reasoning workflow approves action
        |
        v
compact execution instruction
        |
        v
openclaw agent --agent apex-executor
               --session-key ...
        |
        v
execute immediately
```

### Important payload distinction

`--message-file` is convenient, but it is **not claim-check storage**.

The file becomes the model's message body, and OpenClaw currently limits it to 4 MiB. ([OpenClaw](https://docs.openclaw.ai/cli/agent "https://docs.openclaw.ai/cli/agent"))

Therefore:

- compact instruction file → fine;
    
- 20,000-word source payload merely needing transfer → **do not use `--message-file`**.
    

Instead send something like:

```text
Execute approved research request.
Prompt artifact:
C:\...\prompt-2026-08-11.md
SHA256: ...
Expected provider: ChatGPT
Mode: Deep Research
```

and let the execution mechanism consume that path independently.

---

# H — Long-running jobs and resume

## Winner: native persistence + provider-specific recovery — **91/100**

OpenClaw already has three useful layers.

### 1. Session/restart recovery

Gateway restarts preserve or reconcile:

- session conversations;
    
- interrupted main-session turns;
    
- subagent work;
    
- background tasks;
    
- scheduled jobs;
    
- queued deliveries. ([OpenClaw](https://docs.openclaw.ai/gateway/restart-recovery "https://docs.openclaw.ai/gateway/restart-recovery"))
    

### 2. Background Tasks

`openclaw tasks` is a durable activity ledger for CLI, automation, subagent and ACP work, with statuses including running/succeeded/failed/timed_out/cancelled/lost. ([OpenClaw](https://docs.openclaw.ai/automation/tasks "https://docs.openclaw.ai/automation/tasks"))

### 3. Task Flow

Task Flow provides durable JSON state, revision counters and linked task records that survive Gateway restart. ([OpenClaw](https://docs.openclaw.ai/automation/taskflow "https://docs.openclaw.ai/automation/taskflow"))

**But I would not use Task Flow as an APEX global queue.**

Your orchestration system already owns workflow reasoning and approval. Add Task Flow only if a specific OpenClaw execution itself truly needs several restart-resilient child operations.

## ChatGPT long runs

Oracle gives an additional provider-level layer: sessions, reattachment, follow-up, long response handling and browser recovery. ([GitHub](https://github.com/steipete/oracle/blob/main/README.md "https://github.com/steipete/oracle/blob/main/README.md"))

That is the right place to solve ambiguous ChatGPT long-run completion rather than recreating it inside APEX.

### Duplicate-side-effect protection

OpenClaw itself has run deduplication around agent dispatch and warns that transport loss can be ambiguous—the Gateway may already have accepted the turn—so operators should inspect Gateway/session state before retrying. ([OpenClaw](https://docs.openclaw.ai/cli/agent "https://docs.openclaw.ai/cli/agent"))

Its Gateway protocol also requires idempotency keys on side-effecting RPC methods. ([OpenClaw](https://docs.openclaw.ai/gateway/protocol "https://docs.openclaw.ai/gateway/protocol"))

That does **not** automatically make provider webpage submissions idempotent, but it reduces duplication at the orchestration/dispatch boundary.

For ChatGPT, Oracle's stored-session/recheck behavior covers much of the provider-side ambiguity.

---

# I — Multi-repository execution

### Winner: existing workspace/cwd/agent mechanisms — **95/100**

Do not build a multi-repo global queue.

OpenClaw can scope different agents to different workspaces and control which skills are visible per agent. Skill loading/visibility is configurable at the agent level, and workspace skills can override broader defaults. ([OpenClaw](https://docs.openclaw.ai/tools/skills "https://docs.openclaw.ai/tools/skills"))

For APEX, I would configure something conceptually like:

```text
agent: apex-meta-executor
workspace:
  C:\...\apexai-os-meta

agent: leela-executor
workspace:
  C:\...\Leela
```

or keep one executor but use **explicit approved cwd/repository roots** per request.

For one-shot headless work, `openclaw agent exec --cwd <repo>` makes the chosen directory both workspace and tool working directory, while filesystem tools are scoped to that cwd. ([OpenClaw](https://docs.openclaw.ai/cli/agent "https://docs.openclaw.ai/cli/agent"))

That is already a good primitive for repository isolation.

---

# J — Evidence and receipts

### Winner: native run history + tiny APEX receipt convention — **91/100**

There is an important distinction here.

## OpenClaw already records

- run identity;
    
- agent identity;
    
- ordering/provenance;
    
- tool actions;
    
- outcome/status;
    
- task state;
    
- automation history;
    
- command stdout/stderr where applicable. ([OpenClaw](https://docs.openclaw.ai/automation/tasks "https://docs.openclaw.ai/automation/tasks"))
    

## OpenClaw deliberately does **not** put into its audit ledger

- prompts;
    
- bodies;
    
- tool arguments/results;
    
- attachments;
    
- filenames;
    
- URLs;
    
- command output;
    
- raw errors. ([OpenClaw](https://docs.openclaw.ai/gateway/audit.md "https://docs.openclaw.ai/gateway/audit.md"))
    

This is intentional privacy design; the audit ledger is a cross-run index, not another full evidence store. ([OpenClaw](https://docs.openclaw.ai/cli/audit.md "https://docs.openclaw.ai/cli/audit.md"))

Therefore APEX still needs a compact workflow output such as:

```json
{
  "status": "success",
  "provider": "chatgpt-web",
  "artifact": "C:\\...\\research-result.md",
  "sha256": "...",
  "bytes": 184221,
  "started_at": "...",
  "completed_at": "...",
  "conversation_id": "...",
  "openclaw_task_id": "...",
  "browser_status": "completed"
}
```

But this is **not an evidence subsystem**.

It is simply the workflow's return value.

Hashing and file size can be obtained deterministically using standard Windows/PowerShell tooling through native `exec`; no skill is necessary.

---

# D — Recommended installation set

## 1. Oracle CLI — **install**

**Skill:** already bundled with OpenClaw. Do **not** install another copy of the skill. ([GitHub](https://github.com/openclaw/openclaw/blob/main/skills/oracle/SKILL.md "https://github.com/openclaw/openclaw/blob/main/skills/oracle/SKILL.md"))

**Package:**

```powershell
npm install -g @steipete/oracle@0.17.2
```

Oracle requires Node 24+; current OpenClaw itself supports modern Node versions, so that dependency is reasonable on the target machine. ([GitHub](https://github.com/steipete/oracle "https://github.com/steipete/oracle"))

**Why:**

- ChatGPT signed-in browser workflow.
    
- Persistent/manual profile.
    
- long-running Pro/Deep Research.
    
- prompt + file handling.
    
- durable Oracle sessions.
    
- recovery/reattach.
    
- direct file outputs.
    
- active maintenance.
    

**Pin:** `0.17.2`.

The release was published August 10, 2026, and fixes ChatGPT's redesigned picker; it also hardened transcript/model/browser-artifact permissions and published registry integrity information. ([GitHub](https://github.com/steipete/oracle/releases "https://github.com/steipete/oracle/releases"))

**Security status:** OpenClaw bundles the skill; ClawHub's Oracle audit highlights normal external-package/browser risks and recommends dry-run/files-report, excluding secrets and not exposing the browser service publicly. ([ClawHub](https://clawhub.ai/steipete/oracle/security-audit "https://clawhub.ai/steipete/oracle/security-audit"))

**Permissions:** local files explicitly selected, Chrome/browser session, network access to provider, local Oracle session directory.

**Policy:** use `--engine browser` explicitly for the subscription-web workflow so an API key present elsewhere cannot accidentally change routing.

---

## 2. OpenClaw Gemini Web — **install after verify**

Before install:

```powershell
openclaw skills verify @etherstrings/openclaw-gemini-web
```

Install pinned version:

```powershell
openclaw skills install @etherstrings/openclaw-gemini-web --version 0.1.5
```

OpenClaw natively supports pinned ClawHub installs and verification; blocked malicious releases are refused and risky ones require explicit acknowledgement. ([OpenClaw](https://docs.openclaw.ai/es/cli/skills "https://docs.openclaw.ai/es/cli/skills"))

**Version:** `0.1.5`. ([GitHub](https://github.com/Etherstrings/openclaw-gemini-web-skill/blob/main/skills/openclaw-gemini-web/SKILL.md "https://github.com/Etherstrings/openclaw-gemini-web-skill/blob/main/skills/openclaw-gemini-web/SKILL.md"))

**Repository:** Etherstrings `openclaw-gemini-web-skill`.

**Security:** ClawHub Pass, 66/66 clean; two medium credential/TOTP concerns. ([ClawHub](https://clawhub.ai/etherstrings/openclaw-gemini-web/security/static-analysis "https://clawhub.ai/etherstrings/openclaw-gemini-web/security/static-analysis"))

**Required operating restriction:**

```text
DO:
- manually sign in
- dedicated OpenClaw browser profile
- reuse authenticated session

DO NOT:
- store Google password for the executor
- set GEMINI_WEB_TOTP_SECRET
- pass TOTP secrets on CLI
- allow automated account recovery/security challenges
```

That leaves us with almost entirely an **instruction/runbook skill over OpenClaw's own Browser**, which is the desired architecture.

---

## 3. GitHub CLI — **install only if missing**

This is a dependency for GitHub-specific operations, not another OpenClaw skill.

Official Windows installation:

```powershell
winget install --id GitHub.cli --source winget
```

GitHub documents WinGet as the recommended official Windows installation path. ([GitHub](https://github.com/cli/cli/blob/trunk/docs/install_windows.md "https://github.com/cli/cli/blob/trunk/docs/install_windows.md"))

Then authenticate interactively as appropriate:

```powershell
gh auth login
```

GitHub's own docs identify `gh` as supported on Windows. ([GitHub Docs](https://docs.github.com/en/github-cli/github-cli/quickstart "https://docs.github.com/en/github-cli/github-cli/quickstart"))

If all APEX vertical-slice operations are plain `git status/diff/add/commit/push`, **`gh` is not even required yet.**

---

## Nothing else

The following are already part of OpenClaw and need configuration/enabling rather than third-party installation:

```text
browser
browser-automation
exec
exec approvals
read/write/edit/apply_patch
Automations
agent/session dispatch
tasks
audit
github skill
oracle skill
workspaces
```

---

# E — What NOT to install

|Package/type|Decision|Reason|
|---|---|---|
|**ClawHub `@steipete/oracle` skill**|Don't install|Already bundled by OpenClaw. ([GitHub](https://github.com/openclaw/openclaw/blob/main/skills/oracle/SKILL.md "https://github.com/openclaw/openclaw/blob/main/skills/oracle/SKILL.md"))|
|**ClawHub GitHub helper duplicate**|Don't install|Bundled GitHub skill exists; duplicate instructions add little. ([ClawHub](https://clawhub.ai/steipete/github/security-audit "https://clawhub.ai/steipete/github/security-audit"))|
|**Official Perplexity plugin for A/B**|Don't install for this purpose|Uses API; violates subscription-web requirement. ([ClawHub](https://clawhub.ai/openclaw/plugins/perplexity-plugin "https://clawhub.ai/openclaw/plugins/perplexity-plugin"))|
|**Patchright ChatGPT skills**|Don't install|Parallel browser stack + bot-evasion behavior + less mature provider lifecycle. ([ClawHub](https://clawhub.ai/smallnest/skills/patchright-skill "https://clawhub.ai/smallnest/skills/patchright-skill"))|
|**Browser-Use / Agent-Browser bundle**|Don't install|Duplicates native browser and introduces another autonomous browser agent. ([ClawHub](https://clawhub.ai/yinj0012/openclaw-skill-browser-use "https://clawhub.ai/yinj0012/openclaw-skill-browser-use"))|
|**Hantok Perplexity Pro**|Don't install|Explicit Cloudflare/undetectable automation model. ([ClawHub](https://clawhub.ai/hantok/perplexity-pro-to-openclaw/security/virustotal "https://clawhub.ai/hantok/perplexity-pro-to-openclaw/security/virustotal"))|
|**Other headless Perplexity credential wrappers**|Don't install|Own browser/login storage, weak maturity, poor payload behavior|
|**`sligt83/perplexity-web-search-skill` initially**|Don't install|Useful reference, but rewrites questions and says unattended/high-frequency usage isn't its strength. ([GitHub](https://github.com/sligt83/perplexity-web-search-skill "https://github.com/sligt83/perplexity-web-search-skill"))|
|**OpenClaw Native Browser / WKWebView community package**|Don't install|Replaces native stack and is specifically a macOS WKWebView solution, wrong target OS. ([ClawHub](https://clawhub.ai/yungookim/skills/openclaw-browser-2 "https://clawhub.ai/yungookim/skills/openclaw-browser-2"))|
|**Coding Agent for routine Git**|Don't use|Too much delegation/isolation machinery for bounded direct-main execution|
|**Community schedulers/cron wrappers**|Don't install|Native Automations already provide both agent-turn and exact-command scheduling|
|**New queue/task manager**|Don't build/install|Tasks/Task Flow/restart recovery already exist|
|**New evidence database**|Don't build|Native tasks/audit/run histories exist; only artifact receipts are missing|

---

# F — Custom-gap report

This is the most important result of the reuse search.

## Gap 1 — Huge literal web-composer prompt from file

**Requirement:**  
Take, for example, a 20,000-word `prompt.md` and make that _literal text_ become the Gemini or Perplexity root prompt without Qwen receiving the contents.

**Existing native capability checked:**  
Native Browser `type`, `fill`, `evaluate`, batch operations, file upload, existing browser sessions and loopback Browser Control API. ([OpenClaw](https://docs.openclaw.ai/cli/browser "https://docs.openclaw.ai/cli/browser"))

**Bundled skills checked:**  
Browser automation; Oracle.

**ClawHub candidates checked:**  
Gemini Web, Gemini Browser Relay candidates, Perplexity native-browser workflows, headless Perplexity implementations.

**Closest implementation:**  
Oracle for ChatGPT.

Oracle can take large external context/files and route browser work without needing Qwen to reproduce all the content. Its CLI/session/file model is essentially the architecture APEX wants. ([GitHub](https://github.com/steipete/oracle "https://github.com/steipete/oracle"))

**Exact missing capability:**  
I found no documented generic native Browser primitive equivalent to:

```text
browser.typeFromFile(
  path="prompt.md",
  target=composer
)
```

Native `type` takes text, while native file upload uploads an actual file. ([OpenClaw](https://docs.openclaw.ai/cli/browser "https://docs.openclaw.ai/cli/browser"))

**Why configuration/adaptation may still solve it:**

Two routes remain to test first:

1. Provider accepts the prompt as an uploaded `.md/.txt` artifact plus a tiny control instruction.
    
2. Existing browser/OS/local Browser Control API primitives can insert the text deterministically without creating a new OpenClaw abstraction.
    

**Minimum custom addition if both fail:**  
A **tiny deterministic local helper**, not a Skill/browser framework:

```text
file path
  -> read bytes locally
  -> insert into already-selected composer
  -> compare character length/hash or end markers
  -> return success/failure
```

Bound it to:

- named browser profile;
    
- named tab;
    
- expected provider origin;
    
- expected composer;
    
- input path under approved APEX artifact root.
    

### Decision

**Do not build it now. Live-test first.**

---

## Gap 2 — Provider-independent raw response → file

**Requirement:**  
Capture a huge Gemini/Perplexity response without making Qwen ingest the response.

**Existing native capability checked:**

Browser supports:

- targeted `evaluate`;
    
- download;
    
- snapshots;
    
- response-body/debugging operations;
    
- local browser-control scripting. ([OpenClaw](https://docs.openclaw.ai/cli/browser "https://docs.openclaw.ai/cli/browser"))
    

**Bundled checked:**  
Browser automation; Oracle.

**Closest implementation:**  
Oracle `--write-output` / durable session outputs for ChatGPT. ([GitHub](https://github.com/steipete/oracle/blob/main/docs/quickstart.md "https://github.com/steipete/oracle/blob/main/docs/quickstart.md"))

**Exact missing capability:**  
No provider-independent documented one-liner whose semantic contract is “find the final assistant turn and atomically save only that turn to this file.”

**Why configuration may solve it:**  
Native `evaluate` can return targeted page text, and deterministic CLI output can be redirected to a file by the host shell. The executor does not have to feed that output back through Qwen.

Conceptually:

```text
browser evaluate final-response-selector
    |
    +--> stdout
            |
            +--> result.raw
```

Then:

```text
Get-FileHash result.raw
Get-Item result.raw
```

That may completely eliminate the gap.

### Decision

**No custom implementation yet.**

Test selector-scoped extraction + direct shell redirection first.

---

## Gap 3 — Evidence receipt

**Requirement:** path/hash/size/timestamps/provider status.

**Existing native capability checked:** audit, tasks, automation history.

**Exact gap:** audit deliberately does not retain artifact content, filenames or command output. ([OpenClaw](https://docs.openclaw.ai/gateway/audit.md "https://docs.openclaw.ai/gateway/audit.md"))

**Minimum addition:** a JSON or Markdown receipt generated by the workflow.

This is **not a new subsystem or Skill**.

Use existing OS commands/native exec.

---

# G — Integration recommendation

The selected components fit together without another architecture layer:

```text
APEX reasoning workflow
        |
        | compact approved execution instruction
        | artifact references
        v
OpenClaw Gateway
        |
        +-- Local Executor / Qwen3-8B
        |       |
        |       +-- reads control metadata
        |       +-- never needs huge payload itself
        |
        +-- Browser
        |       |
        |       +-- browser-automation
        |       |
        |       +-- ChatGPT
        |       |       |
        |       |       +-- Oracle 0.17.2
        |       |
        |       +-- Gemini
        |       |       |
        |       |       +-- Gemini Web skill
        |       |
        |       +-- Perplexity
        |               |
        |               +-- native browser workflow
        |
        +-- Files
        |       +-- input artifacts
        |       +-- output artifacts
        |
        +-- Exec + approvals
        |       +-- Python
        |       +-- PowerShell
        |       +-- validators
        |       +-- git
        |       +-- gh
        |
        +-- Automations
        |       +-- agent-turn jobs
        |       +-- exact-command jobs
        |
        +-- Agent/session dispatch
        |
        +-- Tasks / restart recovery / audit
        |
        v
compact result receipt
        |
        +-- status
        +-- path
        +-- SHA-256
        +-- size
        +-- timestamps
        +-- task/session/run identifiers
        +-- provider/browser status
        |
        v
owning APEX reasoning workflow
```

Notice what is **not** present:

```text
no APEX browser abstraction
no APEX scheduler
no APEX Git framework
no new global queue
no FEE subsystem
no second task database
no generic payload-transfer framework
no second browser runtime
```

That is the main decision from the research.

---

# H — Open questions

## DECISION REQUIRED

### 1. Gemini credential policy

My recommendation is:

> **Manual login only. Never give the local executor the Google password or TOTP seed.**

The installed Gemini skill can technically process them, but we gain essentially nothing important by enabling that part and materially increase credential authority. The browser profile can persist authentication instead. ([GitHub](https://github.com/Etherstrings/openclaw-gemini-web-skill/blob/main/skills/openclaw-gemini-web/SKILL.md "https://github.com/Etherstrings/openclaw-gemini-web-skill/blob/main/skills/openclaw-gemini-web/SKILL.md"))

I would lock this policy before implementation.

### 2. Dedicated provider profiles vs existing daily Chrome

For unattended reliability and account separation, I recommend **dedicated persistent automation profiles** for ChatGPT/Gemini/Perplexity, rather than operating in your general-purpose Chrome profile.

OpenClaw supports managed profiles and existing-session Chrome, so either approach is technically available. ([OpenClaw](https://docs.openclaw.ai/cli/browser "https://docs.openclaw.ai/cli/browser"))

---

## LIVE TEST REQUIRED

These are not research gaps; they depend on the actual provider accounts/UI and Windows machine.

### 3. Oracle 0.17.2 on the target Windows machine

Vertical test:

```text
manual login
→ tiny ChatGPT prompt
→ normal long prompt from file
→ result file
→ hash/size
→ resume session
→ Deep Research
→ restart/recheck
```

Oracle 0.17.x has CI evidence covering Windows/browser CDP paths, but signed-in ChatGPT browser behavior should still be proven on this actual profile. ([GitHub](https://github.com/steipete/oracle/releases "https://github.com/steipete/oracle/releases"))

### 4. Gemini exact large-prompt semantics

Test three sizes:

```text
1 KB
20 KB
100–150 KB+
```

Determine whether:

- native composer insertion remains exact;
    
- uploaded `.md` prompt artifacts are semantically acceptable;
    
- a deterministic file→composer operation is actually needed.
    

**Do not implement a helper before this result.**

### 5. Perplexity completion detection

Test:

```text
normal answer
long Pro answer
Deep Research if available on subscription
reload during generation
resume existing thread
fresh thread
```

Native browser is the winner because no community alternative cleared all hard gates, but Perplexity-specific completion selectors still need live qualification.

### 6. Native direct response-to-file

Test whether selector-scoped `evaluate` plus output redirection gives the complete raw Gemini/Perplexity answer without Qwen seeing it.

If yes, the second possible custom gap disappears entirely.

### 7. Git approval policy

On a disposable repository, prove that the configured Git argv rules:

```text
ALLOW:
status
diff
add
commit
push origin main

BLOCK:
reset --hard
push --force
rebase
worktree
branch -D
```

Exec approvals are capable of the required enforcement; only the exact APEX regex/allowlist configuration needs live validation. ([OpenClaw](https://docs.openclaw.ai/tools/exec-approvals "https://docs.openclaw.ai/tools/exec-approvals"))

---

# Final decision

**The ecosystem search changes the implementation plan materially.**

The first vertical slice should **not start by authoring APEX skills**.

It should start by configuring:

1. **OpenClaw native Browser + browser-automation**
    
2. **Oracle CLI 0.17.2 + the already-bundled Oracle skill**
    
3. **Gemini Web 0.1.5, manually authenticated**
    
4. **Native browser for Perplexity**
    
5. **Native exec with strict per-agent allowlists**
    
6. **Core Git + bundled GitHub skill**
    
7. **Native Automations**
    
8. **Native agent/session dispatch**
    
9. **Native Tasks/restart recovery/audit**
    
10. **A simple artifact receipt format**
    

The most important discovery is **Oracle**: for ChatGPT, the combination of file/context handling, signed-in browser automation, Deep Research, durable sessions, output files, recovery and duplicate-run avoidance already implements most of the “submit from reference / capture to reference” system you were considering. Rebuilding that inside APEX would currently be unjustified. ([GitHub](https://github.com/steipete/oracle/releases "https://github.com/steipete/oracle/releases"))

For Gemini and Perplexity, **there is not yet enough evidence for custom code**. The only defensible custom candidate is a tiny deterministic file↔composer/file↔response adapter, and even that remains behind the live-test gate.

So the current custom-gap count is:

> **New APEX skills/frameworks required now: 0.**  
> **Possible minimal deterministic adapters after live testing: 0–2.**