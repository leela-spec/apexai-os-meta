---
type: Handover
title: Leela & Mastery — OpenProject consolidation and multi-agent skill standardization
description: Full context for another chat to initiate, set up, and test OpenProject as the operator's single project-orchestration surface across Leela, Mastery of Arts, and 5 AI agent accounts. Alignment phase only — nothing created yet.
tags: [handover, openproject, leela, mastery-of-arts, multi-agent, project-management]
status: draft
generated: { by: "claude/sonnet-5", at: "2026-09-26" }
stale_after: "2026-10-31"
---

# Handover: Leela & Mastery OpenProject consolidation

> **⛔ SKILL LOCATION SUPERSEDED (2026-09-28).** References below to the skill at
> `C:\GitDev\Leela-Cloud-2026\.agents\skills\openproject\` are historical. The skill is now a single
> canonical source at `C:\GitDev\agent-skills\skills\openproject\`, linked into each agent's user-global
> dir (Claude `~/.claude/skills`, Codex `~/.agents/skills`, Antigravity `~/.gemini/config/skills`); token at
> `~/.config/openproject/op.env`. See `Leela-Cloud-2026/docs/ProjectMM/openproject/DECISION-2026-09-28-canonical-skill-architecture.md`.

## Mission

The operator runs multiple projects (Leela — a Flutter app; Mastery of Arts — an entrepreneurship
umbrella with ~20-30 verticals) across multiple AI-agent accounts (Codex ×2, Claude Code ×2,
Antigravity ×1). Right now these are fragmented: different tools/accounts can't see or orchestrate
each other's work. The operator wants **one root OpenProject project** ("Leela & Mastery") containing
everything as sub-projects, so any account, using a standardized skill, can see and act on the whole
picture — not just its own corner.

Concretely, four things need to happen, in roughly this order:
1. **Information architecture**: build the "Leela & Mastery" root project + sub-project hierarchy in
   the operator's private OpenProject instance.
2. **Skill standardization test**: prove all 5 agent accounts discover and use the *same* OpenProject
   skill identically (same reads, same write-confirmation gate, same safety fingerprint).
3. **Complex PM test**: build/import a real hierarchy with dependencies (parent/child work packages,
   relations, milestones) — proving OpenProject actually enforces dependency structure, not just flat
   lists.
4. **Real-data user story**: merge actual existing planning content (not synthetic test data) into
   OpenProject as the first genuine end-to-end proof this whole thing works.

**This is the alignment/setup handover, not the "go build it" handover.** Several design decisions are
explicitly still open and need the operator directly — see "Open decisions" below. Do not invent
answers to those; ask.

## Mandatory read order — three different repos, three different governance models

Read these **before touching anything**, in this order:

1. **This document, in full.**
2. `C:\GitDev\Leela-Cloud-2026\.agents\skills\openproject\SKILL.md` (+ `references/operations.md` and
   `references/write-policy.md` when you need exact payloads) — the **existing, working** OpenProject
   skill. Read it verbatim; do not assume you know what it does from this handover's summary below.
3. **`C:\GitDev\Leela-Cloud-2026`'s own governance — read this even if you think you already know it:**
   - `CLAUDE.md` and `AGENTS.md` at the repo root. This repo runs strict anti-drift rules
     (`docs/orchestration/LEARNINGS_anti_drift.md`), an SSOT/materialization system, and gated scripts
     (`scripts/gates.py`, `check_orchestration_contracts.py`).
   - **Critical constraint**: `AGENTS.md`'s "Where a new document goes" table states the
     `docs/orchestration/` allowlist is **frozen** — "never a new top-level `docs/orchestration/`
     handover." A handover you write about Leela-Cloud-2026 work goes **beside the work bundle it
     hands over, or in `docs/audits/handovers/`** — not as a new top-level orchestration doc. This
     bundle (under `apexai-os-meta`) exists specifically so this cross-repo initiative doesn't need to
     violate that rule.
   - Do not run `Leela-Cloud-2026`'s SSOT/decision machinery casually. If you need to record a real
     decision *inside* that repo (not just read from it), it has its own decision-record convention
     (`docs/ssot/decisions/`, `SSOT-D-###` IDs, `build_decision_registry.py`) — follow it exactly, don't
     improvise a new format.
4. **Prior work directly on this exact topic — read this before designing anything new, it may already
   contain decisions that supersede parts of this handover:**
   `C:\GitDev\Leela-Cloud-2026\docs\orchestration\wave-orchestration\project-management-consolidation\infrastructure-improvement-portfolio-2026-09-18\`
   — specifically `06-phase0-live-alignment-and-openproject-user-story-direction-2026-09-23.md`,
   `07-openproject-operator-agent-research-handover.md`,
   `08-handover-to-redesign-openproject-research-handover.md`, and
   `08-openproject-operator-agent-research-handover-v2.md` (the "v2" and the "redesign" filename
   suggest 07/08 were superseded once already — read all four and figure out which is current before
   trusting any one of them). **Neither the operator nor this session has read these in full yet** — an
   earlier attempt in this session to have a sub-agent read them was interrupted by the operator before
   completion, so this is genuinely unread territory, not something already reconciled into this
   handover. Treat anything in this handover that touches Leela's own OpenProject direction as
   provisional until you've read these four files and reconciled any conflict.
5. `C:\GitDev\apexai-os-meta\apex-meta\orchestration\architecture-improvements\03-wsl2-native-stack-consolidation\`
   (`log.md` + `02-decisions-log.md`, D-01 through D-18) — **the live OpenProject instance this whole
   initiative operates on is the same one migrated in that bundle.** `leela-op178-openproject` now runs
   against a shared PostgreSQL cluster (`priv_openproject` database), re-wired to private Hermes, with
   38 real work packages already in it. Two real incidents happened touching this exact instance during
   that migration (D-17) — read that section regardless of whether you touch infra, because it tells
   you how fragile naive assumptions about "which OpenProject" can be in this environment.

## What already exists (verified this session, not assumed)

- **The OpenProject skill is real and working**, not aspirational: `C:\GitDev\Leela-Cloud-2026\.agents\skills\openproject\`
  — a plain Node.js CLI (`client/opCall.js` + `client/opClient.js`), no framework lock-in, no
  AnythingLLM runtime dependency, no upstream `op` CLI. Discovered natively by Antigravity and Codex
  via `.agents/skills/`; Claude Code reaches the identical files through a `.claude/skills/openproject`
  junction (confirmed: `.claude/skills/openproject -> /c/GitDev/Leela-Cloud-2026/.agents/skills/openproject`).
- **Write policy already enforces exactly the discipline this whole migration session used manually**:
  every mutating op (`wp.create/update/delete`, `wp.comment`, `relation.create/delete`) is blocked by
  default, prints a preview, and requires an identical second call with `--confirmed` after explicit
  operator OK for *that specific action*. Every write must be re-read afterward and compared
  intended-vs-observed. This is not a policy to design — it's already built and matches the discipline
  this session's Docker migration used throughout (see `[[verify-before-destructive-infra-actions]]` if
  that memory persists into your session).
- **Built-in wrong-target protection**: before any write, the client re-checks `GET /api/v3` against
  `OPENPROJECT_EXPECT_VERSION_PREFIX`/`OPENPROJECT_EXPECT_HOST` env vars and refuses on mismatch. This
  is specifically designed to prevent hitting the community instance or the retired v14 duplicate —
  the exact class of mistake that caused D-17's incident 2 in the Docker migration (an agent resurrecting
  and writing to the wrong OpenProject instance). Confirm these env vars are actually set correctly for
  the *current* target before relying on this — don't just trust the SKILL.md example values.
- **Write autonomy beyond reads and explicitly authorized test-scope mutations is stated as "operator-open
  (not yet decided)"** directly in the skill's own `SKILL.md`. This is not resolved by this handover —
  do not self-authorize workflow/structural/high-impact/destructive writes just because the skill lets
  you preview them.
- **Naming, verified this session** (do not re-derive, and do not reintroduce the confusion this session
  cleared up):
  - **Leela** = the whole product (`C:\GitDev\Leela-Cloud-2026`, a Flutter app with its own SSOT
    engineering process). `leela-op178` is just its PM instance's nickname.
  - **"Lila"** (as the operator initially wrote it) = **Leela** — confirmed by the operator this session.
    Not a separate product. Don't go looking for a "Lila" app.
  - **Mastery of Arts** = a separate real repo, `C:\GitDev\MasterOfArts`, sibling of `apexai-os-meta`.
  - **Lika** ("Temple of Lika," a real nonprofit *e.V.*, `lika-community` docker stack,
    `MasterOfArts\Lika\`) exists and is real, but the **operator explicitly excluded it from this round**
    — do not add a Lika sub-project without the operator re-opening that scope.
  - **`acim-secular`** is yet another separate repo (an Astro site) — distinct from the raw ACIM content
    sitting inside `MasterOfArts\ACIM\`. Don't conflate them if ACIM-related sub-projects come up.

## Mastery of Arts — real top-level folder listing (orientation basis, not a finalized taxonomy)

The operator explicitly wants the sub-project taxonomy for Mastery of Arts **designed together with
them** in a live session, not decided unilaterally by an agent — but they also said to use the actual
`C:\GitDev\MasterOfArts` folder structure as the *orientation* for that conversation, not to invent
something disconnected from what already exists on disk. Verified listing (2026-09-26), infra/meta
entries excluded:

```
ACIM              Art               AIHowTo (meta — likely excluded)
Awakening         Business          Cacao Cocoa
Coaching          Content Creation  Dance Fusion
Geopolitcs        Health            IPOS
KIdsCamp26        Legal             LHTL
Lika (EXCLUDED this round)          Meditation
Misc              Neijia New        OpenClaw / OpenClaw_Setup
Podcast           Science           Sexism
Sham              SuperHeroKids     WEbsite
workshops         Orchestration (meta — likely excluded)
```

Do not assign these to sub-projects yourself. Bring this list to the operator and run the actual
collaborative taxonomy session — likely questions to raise with them: which of these are truly active
verticals vs. dormant/archival (`Misc`, `Sham`, `Sexism` in particular look like they may not be
"projects" in the PM sense); whether some should merge (e.g. is `OpenClaw`/`OpenClaw_Setup` one
sub-project or two); whether `AIHowTo` and `Orchestration` belong in the PM hierarchy at all or are
purely meta/tooling directories that don't need OpenProject sub-projects.

## Multi-agent / multi-account dimension

Stated fleet (from the operator directly, treat as ground truth — nothing else in the repo documents
this as a fact, only as exploratory research):
- **Codex** — 2 accounts
- **Claude Code** — 2 accounts
- **Antigravity** — 1 account

What exists to support this:
- Claude Code: `CLAUDE_CONFIG_DIR` (Anthropic's own documented mechanism) — research already done at
  `apex-meta\kb\claude-code-orchestration-design\OperatorResearch\Subscription+Terminal\` (two files,
  `Claude_OneMachineSeveralSeats.md` and `ClaudeCodeSessions.md`). Concludes it works cleanly on Windows.
- Codex: `codex auth login --profile <name>` + `%APPDATA%\OpenAI\Codex\auth-profiles.json` +
  git-worktree isolation for concurrent same-repo work by two accounts — research at
  `MasterOfArts\AIHowTo\Codex\2ndaccoint\Untitled.md`.
- **Antigravity: nothing documented.** No research, no setup guide, no confirmation multi-account is
  even supported. This is a genuine gap — the next session needs to investigate this live (check
  Antigravity's own docs/settings for account-switching support) rather than assume it works like
  Claude Code or Codex's mechanisms.
- **Nothing anywhere states the actual current, live assignment** — which account does what, whether
  all 5 are actually configured and working right now, or whether this is aspirational. Verify live
  state before designing a test protocol around it.

### The actual test protocol (what "test if skills are understood and standardized/usable by all agents" means concretely)

For each of the 5 accounts, in turn:
1. Confirm it can discover the skill at all (`.agents/skills/openproject` directly, or via Claude
   Code's `.claude/skills/openproject` junction).
2. Run `node client/opCall.js root` and `whoami` — confirm identical instance identity across all 5.
3. Run one read op (`project.list` or `wp.list --project <id>`) — confirm identical, correct output.
4. Attempt one **authorized test-scope** write (e.g. a comment on a designated test work package, not
   production data) — confirm the preview-then-`--confirmed` gate behaves identically, and confirm the
   post-write reread step is actually performed, not skipped.
5. Record any account where behavior diverges — a divergence here is a real finding, not a test
   failure to hide; report it plainly.

Do **not** design a new test-scope work package under real production data (the 38 real work packages
already in `priv_openproject`) — create a clearly-labeled test project or test work package for step 4,
and clean it up (or leave it clearly labeled) afterward.

## Real-data user story — candidates found this session (not yet read in full)

Three existing epic folders under
`C:\GitDev\apexai-os-meta\apex-meta\epics\` — each has an `epic.md` plus several numbered story files:
- `leela-core-interaction-development\` (`001.md`…`008.md`)
- `leela-product-decisions\` (`001.md`…`009.md`)
- `leela-project-management-cleanup\` (`001.md`…`006.md`) — **note the name**: this one is literally
  about PM cleanup, which makes it a thematically fitting first import candidate, but confirm its
  actual content matches before committing to it (paths were confirmed to exist; content was not read
  this session).

Also: `Leela-Cloud-2026` runs its own live internal PM system independent of OpenProject — a generated
`docs/ssot/_generated/status/STATUS.md` (17 complete / 12 blocked / 1 active packet across several
waves, as of this session). Do not treat this as raw import material without understanding it first —
it's Leela's own SSOT status view, generated by that repo's own tooling, and importing it naively into
OpenProject risks creating a second, divergent source of truth for the same facts. Read
`Leela-Cloud-2026\CLAUDE.md`'s "Product/work authority" section (auto-loaded context in this session,
quoted in full in that repo's own root docs) before deciding how — or whether — SSOT status data should
flow into OpenProject at all. This is exactly the kind of design question the operator should be in the
loop on, not something to resolve unilaterally.

## Decision log — what the operator already decided this session

| # | Question | Operator's answer |
|---|---|---|
| 1 | Does "Lila, the app" mean Leela? | **Yes.** Not a separate product. |
| 2 | Where does Lika fit in the big project structure? | **Excluded from this round entirely.** Do not add it without the operator reopening this. |
| 3 | Mastery of Arts sub-project taxonomy — mirror existing folders, or design fresh? | **Design fresh, together with the operator** — but use the real folder structure (above) as the orientation basis for that conversation, not a from-scratch invention disconnected from what exists. |
| 4 | Should prior Leela-Cloud-2026 OpenProject research be read first? | **Yes, read it first** — see "Mandatory read order" item 4. Not yet done as of this handover. |

## Safety boundaries

- **The target OpenProject instance holds real, live data** (38 real work packages, actively used by
  the operator). Everything the skill's write-policy already enforces (preview → explicit confirm →
  reread) is not optional ceremony — follow it exactly, the same way this session's Docker migration
  treated every destructive infra step.
- **Never target the community OpenProject instance or the stopped/deleted v14 duplicate** — the skill's
  own fingerprint check guards against this, but verify the guard is actually configured correctly for
  whatever you're doing, don't assume it silently.
- **Bulk creates for the information-architecture step (root project + sub-projects) are structural,
  not test-scope** — get explicit operator confirmation before creating the actual project hierarchy in
  OpenProject, even though the skill's per-write gate will also individually block each call. A batch of
  20-30 individually-confirmed sub-project creates is still a structural decision the operator should
  see as a whole plan first, not discover one confirm-prompt at a time.
- **Respect `Leela-Cloud-2026`'s own governance** (frozen orchestration allowlist, SSOT decision
  conventions, `scripts/gates.py`) for anything you do inside that repo — this handover's existence
  under `apexai-os-meta` is specifically so this initiative doesn't need to violate those rules.
- Reread after every write, exactly as the skill already mandates and as this whole session's Docker
  migration practiced — a clean-looking API response is not proof of correct state.

## Immediate next action

1. Read the four unread Leela-Cloud-2026 OpenProject research docs (item 4 above) and report back what
   they already decided — do not proceed past this until that's done, since it may change or already
   answer parts of what's below.
2. Confirm current live status of the target OpenProject instance (mirrors item 4 of the Docker
   migration's own follow-up handover — `docker ps` for `leela-op178-openproject`, confirm it's healthy).
3. Run the skill's identity-check ops (`root`, `whoami`) from whichever single account you're running
   as right now, to confirm baseline connectivity before planning the 5-account test protocol.
4. Present the operator a synthesized picture — reconciling this handover with whatever the four prior
   docs actually say — and get their go before creating anything in OpenProject or running the
   multi-account test protocol.
