---
type: Handover
title: 5-account OpenProject skill standardization test
description: Prove all five AI agent accounts (Codex ×2, Claude Code ×2, Antigravity ×1) discover and use the SAME OpenProject skill identically — same reads, same write-confirmation gate, same instance fingerprint.
tags: [handover, openproject, skill, multi-agent, standardization-test]
status: ready
generated: { by: "claude/opus-4.8", at: "2026-09-27" }
implementation_authority: operator-gated
---

# Handover: 5-account skill standardization test

## Goal
Demonstrate that each of the five agent accounts uses the **identical** OpenProject skill with identical
behavior: same instance identity, same read output, same preview→confirm write gate, same post-write
reread. Record any divergence plainly — a divergence is a real finding, not a failure to hide.

## What already exists (verified 2026-09-27 — do not re-derive)
- Skill canonical source (since 2026-09-28): `C:\GitDev\agent-skills\skills\openproject\` (router `SKILL.md`
  + Node client `client/opCall.js` + `opClient.js`), linked into each agent's **user-global** dir — Claude
  `~/.claude/skills/openproject`, Codex `~/.agents/skills/openproject`, Antigravity `~/.gemini/config/skills/openproject`
  (no per-repo copy; token at `~/.config/openproject/op.env`). **This 5-account test now verifies THIS layout.**
  See `Leela-Cloud-2026/docs/ProjectMM/openproject/DECISION-2026-09-28-canonical-skill-architecture.md`.
- **The skill now runs and is behaviorally verified** (this session): `doctor` passes; `type.list --project`,
  `wp.create --type "<name>"` name-resolution, and the preview→`--confirmed`→reread write-gate all work.
- **Transport is solved both ways:** the instance answers on `127.0.0.1:8083` from **inside WSL** (Node
  installed at `/home/gehma/nodejs/bin/node`) **and** from the **Windows host** (container republished on
  `0.0.0.0:8083`). So an agent can run the skill either as a Windows process (Windows has Node at
  `…\ApexNode\…`) or inside WSL.
- Config: **auto-loaded by the skill** from `~/.config/openproject/op.env` (base `http://127.0.0.1:8083`,
  admin token, expect-version `17.`, expect-host `127.0.0.1:8083`) — no per-session env setup needed. The
  old `C:\GitDev\leela-op178\op.env` is retained only as the migration source.
- **Idle-sleep caveat:** cold access takes ~80s; wrap the test in a boot-wait or hold the instance warm
  (see `05-handover-browser-keepalive.md`).

## Fleet (operator ground truth) and prerequisites to verify FIRST
- **Codex ×2** — `codex auth login --profile <name>` + `%APPDATA%\OpenAI\Codex\auth-profiles.json` +
  git-worktree isolation. Research: `MasterOfArts\AIHowTo\Codex\2ndaccoint\Untitled.md`.
- **Claude Code ×2** — `CLAUDE_CONFIG_DIR` (Anthropic-documented). Research:
  `apex-meta\kb\claude-code-orchestration-design\OperatorResearch\Subscription+Terminal\`
  (`Claude_OneMachineSeveralSeats.md`, `ClaudeCodeSessions.md`).
- **Antigravity ×1** — **UNDOCUMENTED gap.** No setup/multi-account confirmation exists. Investigate live
  (check Antigravity's own docs/settings for account switching) before assuming it works.
- **Nothing states the actual current live assignment** — verify each of the 5 accounts is genuinely
  configured and working before designing the protocol around them.

## Test protocol (per account, in turn)
1. **Discover** the skill (`.agents/skills/openproject` directly, or Claude's `.claude/skills/openproject`
   junction).
2. **Identity:** run `root`, `whoami`, and `doctor --project 3` → confirm identical instance identity
   (`OpenProject 17.8.0`, host `127.0.0.1:8083`, admin) and a `pass` verdict across all 5.
3. **Read:** one read op (`project.list` or `wp.list --project 3`) → identical, correct output.
4. **Gated write:** one **authorized test-scope** write (a comment on a clearly-labeled TEST work package,
   or a create in a TEST project) — confirm the preview→`--confirmed` gate behaves identically and the
   post-write reread is actually performed, not skipped.
5. **Record** any account where behavior diverges (discovery, identity, output, gate, or reread).

## Safety — do NOT test-write on production data
- The Leela project (id 3) now holds **83 real work packages** and the "Leela & Mastery" hierarchy. Do
  **not** use them as the step-4 write target.
- Create a clearly-labeled **test project** (e.g. `zz-skill-test`) or a single test WP for step 4, and
  delete/clean it (or leave it clearly labeled) afterward. `project.create`/`wp.delete` exist in the skill.
- Never target the community instance (`:9082` / `comm_openproject`) or the retired v14 duplicate (deleted,
  but the fingerprint guard must still be configured). Confirm `OPENPROJECT_EXPECT_*` are set for the run.

## Open decisions for the operator
- Which transport per account: run the skill as a **Windows process** (uniform on Windows, needs the
  instance reachable — it now is) or **inside WSL** via `wsl … node opCall.js`? Pick one convention so all
  5 are truly identical (this is the option-C-vs-A question from `02-preflight-and-transport-diagnosis.md`,
  now that both work).
- Write autonomy beyond reads + authorized test-scope is still **operator-open** in the skill's own
  `write-policy.md` — the test does not change that; keep it read + one authorized test write.

## Definition of done
A results table: for each of the 5 accounts — discovery ✓/✗, identity (root/whoami/doctor) identical ✓/✗,
read output identical ✓/✗, gated write + reread behaved identically ✓/✗ — with any divergence described.
Antigravity multi-account feasibility explicitly confirmed or flagged as unsupported.
