# PATCH_BACKLOG

Phase: `Phase 4 - Staging Mirror Creation`

Repo: `leela-spec/MasterOfArts`

Branch: `main`

Status: `initialized`

## Purpose

This file tracks the future one-file-at-a-time patch backlog for the Meta Heads KB update.

It is not approval to patch final target files.

## Rules

- Final target files remain untouched until staged mirror synthesis and red-team validation pass.
- Patch exactly one final target file at a time.
- Patch only from the staged mirror source file to the matching final target file.
- Do not patch `openclaw.json`.
- Do not patch Apex AI.
- Do not patch unrelated agents.
- Do not treat candidate material as accepted doctrine.

## Backlog status

| Order | Agent | Target file | Mirror source | Current operation class | Status | Notes |
|---:|---|---|---|---|---|---|
| 1 | `meta_strategy` | `OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_strategy/ESSENCE.md` | `OpenClaw/07_finalopenclawsystem/NewFinals/MetaHeadsKBUpdateState/mirror/OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_strategy/ESSENCE.md` | light patch | staged_baseline_created | Needs synthesis and validation before final patch. |
| 2 | `meta_strategy` | `OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_strategy/BEST_PRACTICES.md` | `OpenClaw/07_finalopenclawsystem/NewFinals/MetaHeadsKBUpdateState/mirror/OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_strategy/BEST_PRACTICES.md` | full rewrite | staged_baseline_created | Empty scaffold; needs synthesis and validation. |
| 3 | `meta_strategy` | `OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_strategy/MISTAKES.md` | `OpenClaw/07_finalopenclawsystem/NewFinals/MetaHeadsKBUpdateState/mirror/OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_strategy/MISTAKES.md` | full rewrite | staged_baseline_created | Empty scaffold; needs synthesis and validation. |
| 4 | `meta_strategy` | `OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_strategy/TEMPLATES.md` | `OpenClaw/07_finalopenclawsystem/NewFinals/MetaHeadsKBUpdateState/mirror/OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_strategy/TEMPLATES.md` | full rewrite | staged_baseline_created | Empty scaffold; needs synthesis and validation. |
| 5 | `meta_strategy` | `OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_strategy/LEARNING_QUEUE.md` | `OpenClaw/07_finalopenclawsystem/NewFinals/MetaHeadsKBUpdateState/mirror/OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_strategy/LEARNING_QUEUE.md` | light patch | staged_baseline_created | Candidate-only; add only unvalidated entries if needed. |
| 6 | `meta_strategy` | `OpenClaw/07_finalopenclawsystem/managed/agents/meta_strategy.md` | `OpenClaw/07_finalopenclawsystem/NewFinals/MetaHeadsKBUpdateState/mirror/OpenClaw/07_finalopenclawsystem/managed/agents/meta_strategy.md` | full rewrite | staged_baseline_created | Current final seed has wrapper artifact; staged synthesis should strip wrapper. |
| 7 | `meta_detective` | `OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/ESSENCE.md` | `OpenClaw/07_finalopenclawsystem/NewFinals/MetaHeadsKBUpdateState/mirror/OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/ESSENCE.md` | light patch | staged_baseline_created | Needs synthesis and validation before final patch. |
| 8 | `meta_detective` | `OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/BEST_PRACTICES.md` | `OpenClaw/07_finalopenclawsystem/NewFinals/MetaHeadsKBUpdateState/mirror/OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/BEST_PRACTICES.md` | full rewrite | staged_baseline_created | Empty scaffold; needs synthesis and validation. |
| 9 | `meta_detective` | `OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/MISTAKES.md` | `OpenClaw/07_finalopenclawsystem/NewFinals/MetaHeadsKBUpdateState/mirror/OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/MISTAKES.md` | full rewrite | staged_baseline_created | Empty scaffold; needs synthesis and validation. |
| 10 | `meta_detective` | `OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/TEMPLATES.md` | `OpenClaw/07_finalopenclawsystem/NewFinals/MetaHeadsKBUpdateState/mirror/OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/TEMPLATES.md` | full rewrite | staged_baseline_created | Empty scaffold; needs synthesis and validation. |
| 11 | `meta_detective` | `OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/LEARNING_QUEUE.md` | `OpenClaw/07_finalopenclawsystem/NewFinals/MetaHeadsKBUpdateState/mirror/OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/LEARNING_QUEUE.md` | light patch | staged_baseline_created | Candidate-only; add only unvalidated entries if needed. |
| 12 | `meta_detective` | `OpenClaw/07_finalopenclawsystem/managed/agents/meta_detective.md` | `OpenClaw/07_finalopenclawsystem/NewFinals/MetaHeadsKBUpdateState/mirror/OpenClaw/07_finalopenclawsystem/managed/agents/meta_detective.md` | keep as-is or light patch | staged_baseline_created | Current seed already clean; later normalization only if needed. |

## Next action

Proceed to single-agent synthesis for `meta_strategy` first, writing only to staged mirror files.