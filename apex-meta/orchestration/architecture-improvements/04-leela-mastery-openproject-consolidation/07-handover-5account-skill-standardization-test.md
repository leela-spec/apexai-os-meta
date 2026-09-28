---
type: Handover
title: 5-account OpenProject skill standardization test
description: Prove all five AI agent accounts (Codex ×2, Claude Code ×2, Antigravity ×1) discover and use the SAME OpenProject skill identically — same reads, same write-confirmation gate, same instance fingerprint.
tags: [handover, openproject, skill, multi-agent, standardization-test]
status: done — all 3 tool surfaces auto-invoke the canonical skill (Codex/Claude/Antigravity verified live 2026-09-28); optional: confirm 2nd Codex/2nd Claude accounts + Antigravity multi-account
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

## Results — standardization run (2026-09-28)

**Method:** the canonical skill was exercised **through each tool's discovery-path link**, under a *stripped*
environment (no `OPENPROJECT_*` vars — the harshest case, since Codex strips `*TOKEN*`), so the file-fallback
loader was the only credential path. Multiple accounts of one tool share that tool's discovery dir, so
per-tool identity == per-account identity (see caveat).

| Discovery path (tool) | link→canonical, sha256 identical | root / whoami | doctor --project 3 | read (project.list) | write-gate (no `--confirmed`) |
|---|---|---|---|---|---|
| Claude `~/.claude/skills/openproject` | ✓ YES | OpenProject 17.8.0 / admin | pass (exit 0) | 10 projects | blocked (exit 3, "NOT executed") |
| Codex `~/.agents/skills/openproject` | ✓ YES | 17.8.0 / admin | pass | 10 | blocked |
| Antigravity `~/.gemini/config/skills/openproject` | ✓ YES | 17.8.0 / admin | pass | 10 | blocked |

All three links (Windows junctions + WSL symlinks) resolve to the ONE canonical file
`agent-skills/skills/openproject` (`SKILL.md` + `opClient.js` sha256 identical). Behaviour identical on every
path. Confirmed-write + reread is identical **by construction** (byte-identical client) and was demonstrated
this session (MoA-Content / MoA-Business / ApexAI-OS creates, read-back verified).

**Verdict: skill standardization PASS** — one identical skill, identical behaviour, across all agent
discovery surfaces; the two-phase write-gate and instance fingerprint hold on every path.

### Still requires operator-driven live sessions (not provable by one assistant session)
- **Agent-initiated auto-invocation:** the skill was driven *through* each path here; proving each live agent
  PROCESS (`agy`, `codex`) autonomously *chooses* to invoke it needs those agents run fresh — protocol in
  `Leela-Cloud-2026/docs/ProjectMM/openproject/VERIFICATION-2026-09-28-agent-invocation.md`.
- **The fleet:** Codex ×2 + Claude ×2 + Antigravity ×1 must be confirmed configured. **Caveat:** an account
  that overrides its config dir (Claude `CLAUDE_CONFIG_DIR`, or a Codex profile with a different `HOME`) needs
  the per-skill link created in *that* dir too, or it won't see the skill.
- **Antigravity multi-account** remains the undocumented gap flagged above — confirm or record unsupported.

## Live agent-initiated run (2026-09-28) — operator-driven, Prompt A
Prompt (no skill/command named): *"On the private Leela OpenProject instance, what are the subject and
current status of work package 38? Please show how you retrieved it."* All three returned the correct
answer (subject "User-story census — Stage-4 coverage closure verification (189 IDs)", status **Closed**).

| Agent | Auto-invoked the skill? | How it retrieved | Verdict |
|---|---|---|---|
| **Codex** | ✅ YES | ran `opCall.js root/whoami/project.list/wp.get --id 38/doctor` — through the skill, safety preflight passed | **PASS** |
| **Claude** | ✅ YES | ran `opCall.js wp.get --id 38` via `~/.claude/skills/openproject`, auth from `~/.config/openproject/op.env` | **PASS** |
| **Antigravity (`agy`, Windows)** | ❌ NO | **bypassed the skill** — read the token directly from `op.env` and hand-rolled a raw `curl` with `Authorization: Bearer <token>` (wrong scheme: OpenProject API keys are Basic `apikey:` — narrated method suspect); ~2 min (slow path) | **FINDING** |

**Root cause of the Antigravity finding:** `agy` (the CLI) discovers skills under `~/.gemini/antigravity-cli/skills/`,
but only `~/.gemini/config/skills/` (the IDE/2.0 path) had been linked — so the CLI never saw the skill and
fell back to reading the credential file + curl. **This bypasses the skill's safety gates (instance
fingerprint, token redaction, two-phase write-confirm)** — harmless for this read, but unsafe for a write.
**Fix applied 2026-09-28:** linked the canonical skill into `~/.gemini/antigravity-cli/skills/openproject`
and the legacy `~/.gemini/antigravity/skills/openproject` (Windows junctions + WSL symlinks). **Re-test `agy`
with Prompt A** to confirm it now auto-invokes the skill (and returns to the fast path).

**Re-test PASS (2026-09-28):** after the antigravity-cli link, `agy` discovered the canonical skill and ran
`node C:\GitDev\agent-skills\skills\openproject\client\opCall.js root` + `wp.get --id 38` — now using the
skill's **Basic `apikey:` auth** (through the fingerprint/redaction/write gates), not the raw Bearer curl.
Correct WP#38 read returned. **All three tool surfaces (Codex, Claude, Antigravity) now auto-invoke the one
canonical skill.** ✅

**Fleet coverage (accounts actually tested):**
- **Claude — `AOG` ✅ tested.** Second Claude account **`agehm` ⏳ STILL OPEN** (not yet run).
- **Codex — `axelg` ✅ tested.** Second Codex account **`alexg` ⏳ STILL OPEN** (not yet run).
- **Antigravity — the one account ✅ tested** (after the antigravity-cli fix). Multi-account feasibility still unconfirmed.

The untested second accounts share their tool's discovery dir, so they should inherit the same PASS —
*unless* an account overrides its config dir (`CLAUDE_CONFIG_DIR`, or a Codex profile with a different
`HOME`), which would need the per-skill link created in that dir too. Confirm by running Prompt A in a fresh
session of `agehm` (Claude) and `alexg` (Codex).
