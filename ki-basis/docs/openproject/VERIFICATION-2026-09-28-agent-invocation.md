---
okf_version: "0.2"
type: verification
title: OpenProject skill — agent invocation verification status (Antigravity, Codex, Claude)
description: What is verified about skill discovery/wiring across agent surfaces, and the exact ready-to-run protocol for the agent-initiated read proof that still requires a live operator-driven session.
tags: [openproject, antigravity, codex, claude, skill, verification]
status: partial
date: 2026-09-28
program_ref: apexai-os-meta/apex-meta/orchestration/architecture-improvements/05-program-closeout/PLAN.md (T15)
---

# Agent invocation verification — 2026-09-28

## Verified (discovery wiring is present and well-formed)
> **Update 2026-09-28:** the skill is now a single canonical source at `C:\GitDev\agent-skills\skills\openproject\`,
> linked into each agent's **user-global** dir (no per-repo copy). The wiring below is re-expressed for that layout.
- **Skill definition** `agent-skills/skills/openproject/SKILL.md` has `name: openproject` and a
  trigger-shaped `description` ("Use when a task involves OpenProject work packages, PM status,
  hierarchy, dependencies, or writing evidence back to OpenProject") — the shape auto-invocation relies on.
- **Claude Code**: `~/.claude/skills/openproject` → canonical source (link present, both Windows + WSL). Discovers the skill.
- **Codex**: `~/.agents/skills/openproject` → canonical source. **Antigravity**: `~/.gemini/config/skills/openproject` → canonical source.
  All three point at the one canonical directory (verified via smoke tests).
- Portability by construction: plain Node CLI + one shared API-v3 client, no AnythingLLM runtime, no
  upstream `op` CLI dependency (per `SKILL.md`).

## NOT yet proven (needs a live, operator-driven agent session)
Per anti-drift rule 1a, "documented as discoverable" is **not** proof of **agent-initiated** invocation.
The acceptance for program T15 is *evidence of an agent-initiated (not hand-run) read via the skill* on
**Antigravity** and **Codex**. That cannot be produced by Claude running the skill on their behalf, and no
prior agent-initiated evidence is logged. It requires driving `agy` and `codex` in a real session and
capturing that each **chose** to invoke the skill.

### Ready-to-run protocol (per surface)
1. No token setup needed — the skill auto-loads it from `~/.config/openproject/op.env`. Just confirm the
   17.8 instance is up (see `RUNBOOK-openproject-17.8-operations.md` §3).
2. Start a **fresh** session of the agent (no prior skill mention in context).
3. Give a natural-language task that does NOT name the skill or a command, e.g.
   *"What's the status and subject of OpenProject work package 38 on the private Leela instance?"*
4. **Pass** = the agent, unprompted, invokes the `openproject` skill (`op wp.get --id 38` or equivalent)
   and returns the verified WP #38 attributes. Capture the transcript showing the agent chose the skill.
5. Record per surface: agent + version, the task prompt, the invocation it selected, and the returned
   attributes (redact anything sensitive). Save evidence beside this file.

### Status per surface
| Surface | Discovery wired | Agent-initiated read proven |
|---|---|---|
| Claude Code | ✅ (junction live) | n/a for T15 (T15 targets agy + Codex) |
| Antigravity (`agy`) | ✅ (native `.agents/skills/`) | ⏳ operator-run session required |
| Codex | ✅ (native `.agents/skills/`) | ⏳ operator-run session required |

## Disposition
T15 is **partial**: discovery/wiring verified on all surfaces; the agent-initiated read proof on
Antigravity and Codex is **open** and gated on a live operator-driven run using the protocol above.
