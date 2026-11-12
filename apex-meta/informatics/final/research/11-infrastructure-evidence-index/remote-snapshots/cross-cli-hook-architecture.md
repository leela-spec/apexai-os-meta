---
okf_version: "0.2"
type: Architecture
id: SPEC-CROSS-CLI-HOOK-ARCHITECTURE
title: Cross-CLI Hook Architecture and Multi-Repository Organization
description: Evidence-grounded lifecycle compatibility, shared Python policy, vendor distribution, operational invariants, and staged rollout for Antigravity, Claude Code, and Codex.
status: proposed
tags: [informatics, hooks, cross-cli, antigravity, claude-code, codex, governance]
---

# Cross-CLI Hook Architecture and Multi-Repository Organization

> **Decision (design only, 2026-11-12):** One portable Python **policy core**, distributed byte-identically to each repository, with CLI-specific input/output adapters and per-repository policy data. Native pre-tool hooks are the immediate feedback layer; Git hooks and CI are independent defenses. Do not modify the ratified 23-rule XML contract.
>
> **Execution boundary:** This file specifies a future rollout. It does **not** install hooks, change agent settings, update vendor carriers, or prove the local Windows 11 runtime meets the latency target. No actual CLI hook activation or workstation smoke was performed in this documentation pass.

## 1. Authority, evidence, and explicit corrections

**Authoritative repository inputs (GitHub, 2026-11-12):**

- Handover: apex-meta/informatics/final/operations/handovers/HANDOVER-13-CROSS-CLI-HOOK-ARCHITECTURE-AND-REPOSITORY-ORGANIZATION.md (commit 58e50fad).
- Empirical benchmark: apex-meta/informatics/final/research/10-ultra-upgrade-validation/01-results-and-verdict.md.
- Antigravity reference fixture: apex-meta/informatics/final/research/10-ultra-upgrade-validation/fixtures/armB_hook_agy.py.
- Ratified constitution: apex-meta/informatics/final/specs/apex_contract_v1.0_ultra.xml (read-only, unchanged).
- Carrier architecture: apex-meta/informatics/final/tools/apex_carrier_sync.py and operations/18-APEX-CARRIER-MAP.md.
- Existing Leela hooks: Leela-Cloud-2026/.claude/settings.json, .claude/hooks/, scripts/check_jit_gate_compliance.py, scripts/gates.py.

**Vendor specifications (current online documentation, not locally installed-version proof):**

- Antigravity: https://antigravity.google/docs/hooks
- Claude Code: https://code.claude.com/docs/en/hooks
- Claude Code settings scopes: https://code.claude.com/docs/en/settings
- Codex: https://learn.chatgpt.com/docs/hooks
- Git hooks: https://git-scm.com/docs/githooks
- Git config hooksPath: https://git-scm.com/docs/git-config

**Evidence boundaries:**

1. Round 2 compared 33 task cells per arm: 18/33 under XML/footer alone versus 31/33 under **hooks plus concise workspace reminders**; the combination is proven only on the tested Antigravity harness. The 5/5 T1 interventions were PreToolUse denials; T6/T7 close-out gains came from concise reminders, not Stop denials. No independent claim that hooks alone caused all 13 net additional passes.
2. The handover's statement that Codex lacks native hooks is **outdated as an architectural generalization**: current Codex documentation specifies native project and user hooks, including PreToolUse, PostToolUse, and Stop. A particular installed CLI version may differ; check locally before enabling.
3. GitHub confirms that no committed .agents/hooks.json exists in any of the three target repositories. Leela already has Claude PreToolUse, SessionStart, and Stop hooks. Meta has .claude/settings.json with only defaultMode; Mindful Bar has no committed .claude/settings.json. Local untracked configs, installed CLI versions, Git hook directories, and session permissions are **not observable through GitHub**.
4. Leela-Cloud-2026's current default branch is **master**; apexai-os-meta and mindful-bar default to **main**. Do not silently rename, create a branch, or push Leela under a fictitious main. Rollout to Leela requires an explicit branch-policy resolution.

## 2. Native lifecycle compatibility

| Lifecycle / control | Antigravity (workspace .agents/hooks.json) | Claude Code (workspace .claude/settings.json) | Codex CLI (workspace .codex/hooks.json) |
|---|---|---|---|
| SessionStart | Native | Native | Native |
| UserPromptSubmit | No documented native event in current Antigravity hook reference | Native | Native |
| PreInvocation / per-model | Native PreInvocation | No equivalent named PreInvocation; other model/switch events differ | Native PreModelRequest (not schema equivalent) |
| PreToolUse | Native; toolCall.name / toolCall.args | Native; tool_name / tool_input | Native; tool_name / tool_input; covers Bash, apply_patch, MCP and most local functions |
| PostToolUse | Native; toolCall plus error, not guaranteed tool output | Native; tool result available | Native; some special tool paths excluded |
| PostInvocation / per-model | Native PostInvocation | No equivalent named PostInvocation | Native PostModelRequest (not schema equivalent) |
| Stop | Native; decision=continue to keep loop alive | Native; event-specific block output or exit code 2 | Native; supported, but event-specific decision schema must be verified |
| Git pre-commit | Git process, not an AI lifecycle event | Same | Same |
| Enforcement fallback | Explicit run command + Git pre-commit + CI if native hook absent/disabled | Same | Same; do not assume git-only |

**Naming and payload differences:** Antigravity uses camelCase fields (conversationId, workspacePaths, toolCall); Claude/Codex use snake_case (session_id, cwd, tool_name, tool_input). Normalize these into one internal event, **never** copy one harness's decision JSON into another unmodified.

**Response adapters:**

- Antigravity PreToolUse: stdout JSON {"decision":"deny","reason":"..."} or {"decision":"allow"}; exit 0. PostToolUse: {}. Antigravity Stop: {"decision":"continue","reason":"..."} only for an exceptional, bounded retry.
- Claude Code PreToolUse: stdout JSON {"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"..."}}; ordinary allow may emit no decision. Exit 2/stderr blocks as a fallback. PostToolUse observes successful reads. Avoid obsolete top-level PreToolUse decision format.
- Codex PreToolUse: the same hookSpecificOutput.permissionDecision="deny" shape (or exit 2/stderr) is documented. Do **not** use unsupported permissionDecision="ask" as a policy decision. Validate installed version, loaded hook list, and covered tools before treating this as active.
- Invalid JSON, hook crashes, timeouts, untrusted hooks and unhooked/special tool paths can bypass enforcement. Native hooks are **guardrails, not a security boundary**. Use independent Git/CI checks for repository integrity.

**Required local capabilities before rollout:** agy --version and /hooks; claude --version and /hooks; codex --version and /hooks; python --version; git --version. GitHub evidence and official schemas are not substitutes for those local probes.

## 3. Shared implementation and deployment organization

**Canonical tracked source:** apexai-os-meta/.agents/hooks/apex_hook.py. This is the only file to edit when changing common logic. The same bytes are **vendored** to mindful-bar/.agents/hooks/apex_hook.py and Leela-Cloud-2026/.agents/hooks/apex_hook.py; no symlinks (Windows portability). Do not create a second independently edited policy in .claude/hooks/.

**Target repository layout (proposed):**

~~~text
apexai-os-meta/
  .agents/hooks.json                 # Antigravity dispatch; opt-in
  .agents/hooks/apex_hook.py         # canonical policy + adapters
  .agents/hook-policy.json           # repository-specific rules
  .claude/settings.json              # additive hook entries, retain existing settings
  .codex/hooks.json                  # Codex native dispatch, if local smoke passes
  .agents/git-hooks/pre-commit       # optional tracked Git fallback
  apex-meta/informatics/final/tools/apex_carrier_sync.py
  apex-meta/informatics/final/tools/check_vendor_drift.py
  apex-meta/informatics/final/tools/tests/test_apex_hook.py

mindful-bar/                     Leela-Cloud-2026/
  .agents/hooks.json              .agents/hooks.json
  .agents/hooks/apex_hook.py      .agents/hooks/apex_hook.py
  .agents/hook-policy.json        .agents/hook-policy.json
  .claude/settings.json           .claude/settings.json  # preserve existing hooks
  .codex/hooks.json               .codex/hooks.json
  .agents/git-hooks/pre-commit    .agents/git-hooks/pre-commit
~~~

**One program, three adapters:** apex_hook.py exposes host={antigravity,claude,codex}, event={pre,post,stop}. The host adapter maps stdin to a common internal event and maps its ALLOW/DENY decision back to the documented host JSON. A small policy function evaluates only canonicalized paths, exact command tokens, and successful read receipts. No HTTP, model calls, Docker, elevation, registry, background daemon, or recursive repository scan.

**Common event:** {host, event, session_id, repo_root, tool_name, command, target_paths, success}. Treat source paths as canonical repo-relative names after resolving relative paths, case and separators correctly for the actual filesystem. Unparseable or ambiguous governed write paths must not be silently classified as outside scope.

**State:** Session-local read ledger in a process-safe temp path keyed by repo-root identity + host + session ID. Only mark a required file read after a successful PostToolUse (not on an attempted PreToolUse read or a mere Grep match). Reset on a supported new-task boundary; where Antigravity has no UserPromptSubmit event, require a fresh session for strict JIT tasks or an explicit reset entry point. Persist no transcript bodies or private prompt data. Concurrent hooks need atomic state updates; if that cannot be provided within the latency budget, restrict state to a single session-specific file and reject unproven concurrency semantics.

**Sources versus policy:** Hardcode only generic mechanics in Python. Put governed path prefixes, exact required ref paths, and exceptions in .agents/hook-policy.json. Do not invent product semantics for other repositories. Keep XML and existing Leela gates authoritative.

## 4. Reference configurations (proposed, not activated)

The following JSON shapes are derived from the current vendor documentation. They require the named script, a working Python launcher, trusted hooks, and a smoke test from the repository root **and from subdirectories**. Commands intentionally make no permission bypass request.

### 4.1 Antigravity — .agents/hooks.json

~~~json
{
  "apex-invariants": {
    "enabled": true,
    "PreToolUse": [
      {
        "matcher": "run_command|write_to_file|replace_file_content|multi_replace_file_content",
        "hooks": [
          {
            "type": "command",
            "command": "python -S .agents/hooks/apex_hook.py --host antigravity --event pre",
            "timeout": 2
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "view_file",
        "hooks": [
          {
            "type": "command",
            "command": "python -S .agents/hooks/apex_hook.py --host antigravity --event post",
            "timeout": 2
          }
        ]
      }
    ]
  }
}
~~~

Relative path assumes execution from repo root; if the installed host runs from another cwd, replace with a **verified** absolute/root-resolving launcher rather than assuming success.

### 4.2 Claude Code — additive entries in .claude/settings.json

~~~json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash|Write|Edit|MultiEdit",
        "hooks": [
          {
            "type": "command",
            "command": "python -S \"${CLAUDE_PROJECT_DIR}/.agents/hooks/apex_hook.py\" --host claude --event pre",
            "timeout": 2
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Read",
        "hooks": [
          {
            "type": "command",
            "command": "python -S \"${CLAUDE_PROJECT_DIR}/.agents/hooks/apex_hook.py\" --host claude --event post",
            "timeout": 2
          }
        ]
      }
    ]
  }
}
~~~

**Merge, never replace:** In Leela append these handlers to the already present PreToolUse Bash rule, SessionStart git-status hook, and Stop checks; preserve enabledPlugins and skillOverrides. Claude's existing Leela check-jit-gate-compliance.py stays until equivalence is proven. Validate the actual shell environment and availability of CLAUDE_PROJECT_DIR on Windows.

### 4.3 Codex — .codex/hooks.json (native primary path where supported)

~~~json
{
  "description": "Repository-scoped Apex invariants.",
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash|apply_patch|Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "python -S .agents/hooks/apex_hook.py --host codex --event pre",
            "timeout": 2
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python -S .agents/hooks/apex_hook.py --host codex --event post",
            "timeout": 2
          }
        ]
      }
    ]
  }
}
~~~

Codex may launch in a subdirectory. Use a verified repo-root launcher before production activation. Codex additionally requires review/trust of repository hooks through /hooks; project trust and feature toggles can disable them. The PostToolUse Bash adapter may credit a read only when the completed command demonstrably opened the **exact** required path successfully. Hosted or excluded tools are not covered. On an older installed Codex without native hooks, omit this config rather than falsely marking it active.

## 5. Minimal deterministic invariant set

| Rule | Trigger and decision | Non-goals / boundary |
|---|---|---|
| H-GIT-01 — scoped staging | Native PreToolUse denies direct blanket staging such as git add -A, git add --all, git add ., git add -- ., git commit -a and relevant equivalents; advise git add -- exact/path. Recognize git -C / git -c wrappers and shell chains when tested. | A Git pre-commit hook cannot know which git add command produced the index. Shell wrappers and unobserved tools require Git/CI defense. Do not block explicit git add -- named paths. |
| H-READ-01 — governed pre-read | On an explicit write to governed paths, require successful reads of configured source files in the **current task/session scope** before allowing. Meta's final/** rule requires final/index.md; handover files also require specs/execution-modes/handover.md. | The fact a tool opened a file is not proof the model understood its content. Do not demand unrelated spec reads on ordinary edits. |
| H-SCOPE-01 — staged protection | Git pre-commit may inspect staged filenames against **existing, explicitly configured** forbidden/generated path rules; if a task-scope manifest is present, compare the staged set against that declared scope. | Without an authorized scope receipt or baseline, pre-commit cannot distinguish unrelated staged files from intentional edits. Do not fail merely because unrelated unstaged dirty files exist. |

**Meta policy example** (illustrative config, requires exact path validation):

~~~json
{
  "schema": "apex.hook-policy.v1",
  "repo": "apexai-os-meta",
  "governed": [
    {
      "path_prefix": "apex-meta/informatics/final/",
      "required_reads": ["apex-meta/informatics/final/index.md"]
    },
    {
      "path_prefix": "apex-meta/informatics/final/operations/handovers/",
      "required_reads": [
        "apex-meta/informatics/final/index.md",
        "apex-meta/informatics/final/specs/execution-modes/handover.md"
      ]
    }
  ],
  "ban_blanket_staging": true
}
~~~

For mindful-bar and Leela, derive rules from their *own* tracked contracts before enabling. For Leela, preserve scripts/gates.py and docs/apex/check_vendor_drift.py; they are not per-tool 50 ms work. The project JIT check currently covers handover, trade-off and authoring triggers, with a transcript-based Stop adapter; do not turn this into a universal rule for all Flutter files.

**Denial output:** one sentence, concrete and reversible; e.g. "Read apex-meta/informatics/final/index.md before editing governed files." or "Stage only requested files with git add -- <paths>; blanket staging is blocked." Never add a multi-step lecture to hook stdout. Do not repeat denials on Stop for the same already-declined tool call. Do not introduce an unbounded force-continue loop.

**Failure and bypass policy:** A policy violation with valid input returns DENY using the host's schema. A malformed event, missing policy, unavailable Python, or hook startup error is **NOT VERIFIED**, not ALLOW-by-design; the engine may fail open regardless. CI/Git owns independent safety checks. Do not claim adversarial command-parsing coverage without negative tests. The design is for cooperative agents, not hostile-code isolation.

## 6. Git hook fallback and limits

Git hooks work regardless of agent CLI only when installed and not bypassed. A tracked source at .agents/git-hooks/pre-commit can be activated **per local clone**, after explicit rollout, with:

~~~bash
git config --local core.hooksPath .agents/git-hooks
~~~

Or install the same tracked script into .git/hooks/pre-commit; note that the latter directory is not committed. Keep pre-commit fast and focused on **staged content**. Use git diff --cached --name-only -z to inspect exact staged paths and invoke only required checks; no fetching, no whole-tree scans. A pre-commit hook can reject forbidden staged paths, explicit manifest scope violations and known invalid content, but **cannot prove git add -A was not used** and **cannot verify what the agent read**. Use native PreToolUse for those two questions.

Hooks may be skipped by --no-verify or replaced via core.hooksPath; they do not protect raw filesystem writes or GitHub API commits. Keep required invariant coverage in existing repository gates and CI where those checks exist. Sandboxes restrict filesystem/process access but do not prove spec pre-reads. MCP middleware only intercepts tools routed through that middleware; it is optional, not a universal solution.

## 7. Vendor management and ownership

**Owner:** apexai-os-meta main; canonical script .agents/hooks/apex_hook.py; architecture/policy specification here. No edits to apex_contract_v1.0_ultra.xml.

**Proposed narrow sync extension to apex_carrier_sync.py:** add a separate opt-in hook audit/sync mode, not implicit default behavior. Audit compares SHA-256 of canonical apex_hook.py with each vendored copy and verifies configuration references exist. Sync copies only the common script and known reference fixture updates, creating backup or requiring clean target content; never rewrite repo-specific hook-policy.json, Leela's existing .claude/settings.json, Git local configuration, or global user settings automatically. Keep the existing XML carrier sync unchanged.

**Vendor-drift boundary:** check_vendor_drift.py presently checks Markdown modules under vendored docs/apex and systems/apex; it does **not** cover .agents/hooks scripts. Extend a purpose-specific hook manifest/check, not its unrelated Markdown rules. If the meta source repository is unavailable, report SKIPPED/UNVERIFIED, never IN SYNC. Record canonical source commit and vendor content hash.

**Update workflow:** change canonical script + tests on meta main; audit; approve targeted distribution; commit target-repository copies individually on their authorized branch; report per-repo hashes; smoke in each installed CLI. Do not turn sync into an unattended cross-repo mutation.

## 8. Rollout and measurable acceptance

| Step | Repository / owner | Action | Evidence and gate |
|---|---|---|---|
| R0 | apexai-os-meta | Implement pure-stdlib shared core + host adapters + synthetic event fixtures and negative tests, without enabling hooks. | Explicit tests for allow, deny, target path normalization, successful-read-only receipts, malformed input, quoted commands, command chains, and interrupted sessions. |
| R1 | apexai-os-meta | Add proposed .agents/hooks.json, additive .claude/settings.json, conditional .codex/hooks.json; run each installed CLI locally. | /hooks lists the trusted hook; a harmless write allows; premature governed write denies; an actual successful required read unblocks; blanket git add denies. |
| R2 | mindful-bar | Vendor identical script and configure only verified governed paths. No global configuration edits. | SHA matches master, product edits not covered by policy remain unrestricted, governed edits reliably gate. |
| R3 | Leela-Cloud-2026 | Resolve existing master-versus-main policy before any write; vendor script; merge with preexisting Claude hooks and check-JIT behavior. | Existing Leela tests/gates still pass, no double-stop or performance regression, all three CLIs smoke. |
| R4 | all three | Optional Git pre-commit for staged-path checks and CI follow-up. | Git hooks installed per clone, protected staged paths tested, --no-verify limitation documented, drift audit passes. |

**Latency gate (not yet measured):** Handover 13 requires every hot-path hook to run in under 50 ms with no network. Use python -S with only stdlib JSON/path/regex work and bounded session-state I/O; do not run git status, validators, or parse full transcripts in PreToolUse/PostToolUse. Measure **end-to-end subprocess startup plus execution**, not only Python function time, on the actual Windows 11 host for 200 allow and 200 deny events per CLI. Record median, p95, maximum, Python version, filesystem, and cold-start cases; reject activation if the stated <50 ms bound is not proven. Vendor timeout values in the JSON examples are coarse *fail-safes in seconds*, not evidence of 50 ms execution.

**Acceptance:** Zero unauthorized writes; positive/negative hook events and Git fallback pass; no vendor drift; all policy denials single-sentence and actionable; no Stop retry loop; XML SHA unchanged; documentation validator reports zero OKF_ERROR and APEX_PROFILE_ERROR findings; Leela's existing gates retain their authoritative role.

## 9. Verification status and explicit open items

- **Confirmed from GitHub:** Handover 13 exists; Round 2 fixture and evidence exist; Leela has existing Claude hooks; no committed Antigravity hooks configs in the three repos; Leela branch is master, other two main.
- **Confirmed from vendor documentation:** Three CLIs currently document native lifecycle hook events, but their schemas, event coverage and trust rules differ. Codex native hooks supersede the handover's git-only fallback assumption.
- **Specified, NOT EXECUTED:** Shared Python implementation, configs shown above, local Windows compatibility, shell cwd resolution, native event smoke, 50 ms latency, per-repo policy deployment, Git hooks installation, carrier-sync extension and cross-repo rollout.
- **Important correction before deployment:** Existing benchmark fixture does whole-transcript scans, Git subprocess calls, and Stop-time validation. Its proven behavioral efficacy must not be mistaken for a proven <50 ms production hot path.
- **Decision boundary:** This architecture specification does not authorize changing the constitution, enabling global hooks, or writing to mindful-bar and Leela. Approve rollout independently after native probes and scope verification.

**Completion of this document** means the three investigation tasks and deployment design are specified. Operational adoption remains unverified until the measured R0–R4 evidence exists.
