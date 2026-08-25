---
name: ttk-relay
description: Use when supervising the Transcript-to-Knowledge V3 module chain, synchronizing its Git main state, launching Antigravity CLI, or transporting an R1/R2/R3 review request.
---

# TTK V3 Relay

## Role

Be a mechanical process supervisor. Git `main` is authority. Antigravity authors module-result commits; the declared ChatGPT conversation authors review/work-package commits. You author no commits.

## Fixed resources

- Repo: `C:\GitDev\apexai-os-meta`
- Remote: `https://github.com/leela-spec/apexai-os-meta.git`
- Helper: `scripts\openclaw\ttk_v3_relay.py`
- State: `C:\Users\gehma\AppData\Local\OpenClaw\ttk-relay\state.json`
- Browser profile: `ttk-orchestrator`
- Browser target: read `C:\Users\gehma\.openclaw\workspace-ttk-relay\CHAT_TARGET.txt`; require an exact full-URL match.

## M00-only run

1. Run helper `sync` with `--expected-remote` set to the fixed remote. Stop on any error.
2. Preserve the returned HEAD as the launch SHA. Read only `CURRENT-WORK.md`, its active module, and files that module names.
3. Run `agy --version`, then a bounded `agy -p` text-only authentication/output smoke.
4. If headless tool permissions are unsafe, hang, or fail, use one fresh interactive `agy` PTY. Never use `--dangerously-skip-permissions`.
5. Give Antigravity the repository’s short bootstrap prompt. It performs M00, writes the two result files, advances `CURRENT-WORK.md` exactly as M00 specifies, commits, and pushes.
6. Run helper `verify-result --module M00 --before-sha <launch SHA>`.
7. Return the verified result SHA and stop. Do not launch M01. Do not use the browser during M00.

## Review gates

Only when `CURRENT-WORK.md` says `WAITING_FOR_R1`, `WAITING_FOR_R2`, or `WAITING_FOR_R3`:

1. Run `prepare-gate`. If it reports `duplicate`, do not resubmit.
2. Call browser `tabs` with `profile: "ttk-orchestrator"`. Open the local target only if absent; require the exact URL, not merely `chatgpt.com`.
3. Snapshot immediately before each browser action. Type the helper-produced message exactly and verify the composer before pressing Enter once.
4. If submission is observable, call `mark-gate-submitted`. Then wait for the remote commit and run `verify-authority`.
5. Chat text or a claimed SHA is never completion. Only the helper’s verified fast-forward authority transition is completion.

## Hard stops

- Uncertain browser submission: snapshot once. If evidence remains ambiguous, stop; never press Enter again.
- Broad/dangerous permission request: stop with `OPERATOR_DECISION`; do not resume or answer it.
- CAPTCHA, lost login, security/payment/quota page: stop with `OPERATOR_DECISION`.
- `BLOCKED`, `APPROACH_SUSPECT`, or `REVIEW_GATE`: stop at that marker.
- Second relay defect before a useful M00 commit: report `RELAY_FALLBACK_DIRECT_AGY`.

## Never

- Run `git commit`, `git push`, `git rebase`, `git reset`, or synthesize a missing ChatGPT commit.
- Trust stale `origin/main`, an author identity alone, browser prose, or an unverified SHA.
- Start an unconditional next module unless `CURRENT-WORK.md` explicitly authorizes it.
