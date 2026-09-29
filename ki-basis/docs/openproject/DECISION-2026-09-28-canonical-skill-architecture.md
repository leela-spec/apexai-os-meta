---
okf_version: "0.2"
type: decision-record
title: Canonical agent-skill architecture — one source, linked into every agent (why & how)
description: Records why the OpenProject (and all future) agent skills were consolidated into a single canonical repo linked into each agent's discovery path, with the token moved to a user-level file — so future agents understand the reasoning and don't re-introduce drift.
tags: [openproject, agent-skills, architecture, decision, secrets, windows, wsl2]
status: accepted
date: 2026-09-28
canonical_source: "C:\\GitDev\\agent-skills\\  (README + research/FINDINGS.md + research/ENVIRONMENT-CONSTRAINTS.okf.md)"
program_ref: apexai-os-meta/apex-meta/orchestration/architecture-improvements/05-program-closeout/PLAN.md
---

# Decision — canonical agent-skill architecture (2026-09-28)

## Problem
The OpenProject skill was **copied** into product repos (`Leela-Cloud-2026/.agents/skills/openproject`
and `Investment/.agents/skills/openproject`) and the copies had **already drifted** (SKILL.md 92 vs 123
lines). Copies in N repos → N update points → drift, confusion, stale docs. Two further smells: a
credential shouldn't dictate a repo (`leela-op178/op.env`), and a cross-cutting capability shouldn't live
inside one product repo (Leela-Cloud-2026) when it's used everywhere.

## Decision
**One canonical source of truth for all custom agent skills, linked into each agent's discovery path — zero
copies.** Backed by two cited research passes (see `agent-skills/research/FINDINGS.md`), constrained by a
machine-readable environment file (`agent-skills/research/ENVIRONMENT-CONSTRAINTS.okf.md`).

## What was built
- **Canonical repo:** `C:\GitDev\agent-skills\` (git, `.gitattributes eol=lf`). Holds `skills/openproject/`
  (reconciled — the two copies differed only in `SKILL.md`; the better content was merged) and scales to
  future skills.
- **Discovery links** (per-skill, not whole-dir, so existing skills are untouched):
  - Windows **junctions** (no admin): `~/.claude/skills/openproject`, `~/.agents/skills/openproject`,
    `~/.gemini/config/skills/openproject`.
  - WSL **symlinks**: the same three under `/home/gehma`.
- **Secret moved** to `~/.config/openproject/op.env` (CRLF→LF), outside every repo. The skill's client now
  loads config **env-first, then this file** (CRLF-tolerant) — required because **Codex strips `*TOKEN*`
  env vars** from subprocesses, so env-only would silently have no token.
- **Security hardening** (after a Codex review caught a flaw in the first loader): config now loads
  **atomically from one source** (an env base URL can't redirect a file-loaded token), and the client
  **refuses to send the token to any host != `OPENPROJECT_EXPECT_HOST`** on every request; the WSL path no
  longer hard-codes the username. Wrong-then-fixed trail: `agent-skills/research/LEARNINGS.md`.
- **Verified:** with a stripped environment (no `OPENPROJECT_*` vars, like Codex), `root`/`whoami` succeed
  via the file fallback through the `~/.agents/skills` symlink (200, admin); an "evil" env base URL is
  ignored/refused (the token never leaves the expected host).

## Correct discovery paths (per official docs — the machine's old folders were legacy)
- Claude Code → `~/.claude/skills/` · Codex → `~/.agents/skills/` (not `~/.codex/skills`) ·
  Antigravity → `~/.gemini/config/skills/` (not `~/.gemini/skills`).

## Consequences / rules for future agents
- **Never copy a skill into a product repo.** Edit only in `C:\GitDev\agent-skills\`. A product-repo
  override is a deliberate exception, not the default.
- The old per-repo copies (`Leela-Cloud-2026`, `Investment`) are being removed; `Investment` is handled by
  its own agent session (coordination).
- Adding a skill: create it in the canonical repo, then link it into each agent dir (both OSes) — see the
  repo README.

## Links
- Canonical repo + usage: `C:\GitDev\agent-skills\README.md`
- Reasoning + cited research: `C:\GitDev\agent-skills\research\FINDINGS.md`
- Environment constraints (OKF 0.2): `C:\GitDev\agent-skills\research\ENVIRONMENT-CONSTRAINTS.okf.md`
- Agent usage quickstart: [`AGENT-QUICKSTART.md`](AGENT-QUICKSTART.md)
