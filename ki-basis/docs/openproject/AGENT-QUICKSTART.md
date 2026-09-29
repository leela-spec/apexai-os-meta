---
okf_version: "0.2"
type: quickstart
title: Agent quickstart — operate OpenProject via the skill + API (not the browser)
description: Paste-ready instructions for any agent (Codex, Antigravity, Claude) to operate the private Leela OpenProject through the portable skill and API v3 — no web login required.
tags: [openproject, agent, codex, antigravity, skill, api, quickstart]
status: current
updated: 2026-09-28
---

# Agent quickstart — operate OpenProject via the skill + API

**Do NOT use the OpenProject website / browser login.** The web password is a separate credential and is
irrelevant to agents. Agents talk to OpenProject through its **API v3** via the **`openproject` skill**,
authenticated by an **API token** (not a username/password).

## Where the skill is
**Canonical source (edit only here):** `C:\GitDev\agent-skills\skills\openproject\`. It is **linked** into
every agent's discovery dir, so it's available in every repo with no copies:
- Claude Code → `~/.claude/skills/openproject` · Codex → `~/.agents/skills/openproject` ·
  Antigravity → `~/.gemini/config/skills/openproject` (Windows junctions + WSL symlinks to the canonical source).
- `SKILL.md` (read first) · `client/opCall.js` (the CLI) · `references/operations.md` (payloads) ·
  `references/write-policy.md` (write gate).

The API token lives in the user-level file `~/.config/openproject/op.env`
(= `C:\Users\gehma\.config\openproject\op.env`), outside every repo. **The skill auto-loads it** (env
first, then that file) — so you normally don't set anything. Never print or commit the token.

## Target instance — never guess
The **private** Leela OpenProject only: `http://127.0.0.1:8083`. Never the community instance or the
stopped duplicate.

## Setup (token auto-loaded — usually nothing to do)
```bash
# WSL/bash — just move into the linked skill folder; the client reads ~/.config/openproject/op.env itself:
cd ~/.agents/skills/openproject          # (Codex/Antigravity)   or ~/.claude/skills/openproject (Claude)
```
PowerShell: `cd $HOME\.agents\skills\openproject`. No env-var setup needed; the client loads the token from
`~/.config/openproject/op.env` automatically (this is why it works under Codex, which strips `*TOKEN*` env vars).
Only if you want to override: set `OPENPROJECT_ENV_FILE` to a different file path.

## Always start read-only (prove identity + reachability)
```bash
node client/opCall.js root                  # instanceName + coreVersion (expect 17.x @ 127.0.0.1:8083)
node client/opCall.js whoami                # authenticated identity
node client/opCall.js project.list          # resolve project ids/identifiers
node client/opCall.js doctor --project <id> # one-shot read-only preflight before real work
```

## Common reads
```bash
node client/opCall.js wp.get --id 38
node client/opCall.js wp.list --project <id> --pageSize 20
node client/opCall.js status.list
node client/opCall.js type.list --project <id>   # types are enabled per-project
```

## Writes — two-phase and gated
1. Run the mutating command **without** `--confirmed` → prints a preview, does **not** write.
2. Only after the operator OKs that specific action, re-run the identical command **with** `--confirmed`.
3. After any write, **reread** (`wp.get`) and compare intended vs. actual. `wp.update` needs the current
   `lockVersion` from a prior `wp.get`.

Do not self-authorize workflow/structural/destructive writes — that autonomy policy is still operator-open
(see `references/write-policy.md`).

## Efficiency & verification
- Run `doctor` once at the start; use `project.list` to resolve ids rather than guessing.
- Prove every result: for a read, echo the returned id + a stable field; for a write, show the post-write reread.
- If a skill call fails, repeat the same call directly against the API to tell a skill bug from an API problem.

## Boundaries
- Never target the community/stopped instances; never write PostgreSQL directly (API only).
- The large `docs/ProjectMM/openproject/openproject/` package is reference-only, not a runtime dependency.

## Live project hierarchy (context)
See [`README.md`](README.md). Master project **Leela & Mastery** contains **Leela** and **PM Infrastructure**.
