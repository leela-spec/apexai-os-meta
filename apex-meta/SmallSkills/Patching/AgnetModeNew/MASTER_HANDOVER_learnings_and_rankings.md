# MASTER HANDOVER — Full Learnings, File Index, Failure Patterns, Ranked Instructions
Prepared: 2026-07-07 18:21 CEST

====================================================================
PART 1 — COMPLETE FILE INDEX (what exists, and its actual value)
====================================================================

--- ROOT CAUSE & CORRECTED UNDERSTANDING ---

file:70 "Create a learning for the failure modes. research.md"
  VALUE: Identifies the true root cause via external research — silent
  connector-level truncation on large file fetches is a documented,
  known failure class (not a one-off bug). Cites specific mechanisms:
  "silent tool truncation" (~8KB default caps), "context debt"/"memory
  wall" in long-running agents, and confirms via Reddit/community sources
  that GitHub connector fetches routinely truncate large files without
  signaling it.

file:69 "agent-mode-prompt-failure-pattern-analysis-correction-2026-07-07.md"
  VALUE: Corrects an earlier WRONG diagnosis. Establishes that checking
  for a live git worktree every run is unnecessary — this container
  never has one, confirmed repeatedly. Saves wasted turns.

file:1 "agent-mode-prompt-failure-pattern-analysis-2026-07-07.md"
  VALUE: First pattern analysis across the earliest ~9 failures. Grouped
  failures into: repo-discovery loops, fabricated content, lost ZIP
  artifacts, ambiguous "clean copy" instructions, undefined patch naming.

--- RAW FAILURE EVIDENCE (do not re-read fully; reference only) ---

file:35 "ChatHistoryClaudeConstantFailures.md"
  VALUE: Full transcript of failure #14 — the run that exposed the root
  cause. Agent built a baseline mirror TWICE (duplicate build), never
  successfully read Section 7 of the plan on any attempt, and self-
  reported an honest FAIL with zero patches produced.

file:34 paste.txt (190314 chars)
  VALUE: Raw reasoning trace for the same failure #14. Shows the exact
  fetch attempts that failed — line ranges 670-900 and 1040-1100 of the
  plan file returned truncated/empty content every time.

file:31 paste.txt (74618 chars)
  VALUE: Earlier failure — large-file fetch thrashing. Agent tried THREE
  different strategies on one file in sequence (line-range fetch, base64
  decode, 100-line chunking) and separately discovered it had written
  two files to the wrong directory depth, requiring a redo.

file:32 "the-process-failed-again-btw-the-last-owrking-pro.md"
  VALUE: Batch-A run report — zero patches produced because "required
  per-file changes from the plan couldn't be recalled." Same root cause
  as file:34/35, different session, confirming it's systemic not a
  one-off.

file:9 "ThinkinProcessWorkingAgentMode.md" (251038 chars)
  VALUE: A WORKING run's full trace. Positive reference for correct
  step-by-step behavior, but its scale/success does NOT mean large
  single-shot sessions are safe — this was a smaller/simpler task shape.

file:10 "FailReport_Claude.md", file:11 "ThinPRocessFailPrompt_claude.md"
  VALUE: Earlier-generation failure reports. Superseded by file:1/69/70
  analyses; historical detail only.

file:2 "ChatHistory_ConstantFailurePrompts.md"
  VALUE: General background chat log. Low standalone value; context only.

--- PROMPT VERSION HISTORY (all superseded — do not execute any of these) ---

file:6 "PromptClaude.md"
  WHAT IT WAS: The ORIGINAL 22-file, single-shot prompt.
  FAILURE IT CAUSED: Unnecessary git-worktree re-checks every run; no
  ZIP verification step, leading to empty-ZIP-reported-as-success.

file:29 "create-a-new-version-of-the-prompt...md"
  WHAT IT WAS: First rebuild. Added ACCESS_DECLARATION block and
  explicit honest-partial-completion mechanics (files_failed lists).
  GAP REMAINING: Still no large-file handling; still single 22-file batch.

file:28 "verify-this-is-a-legit-prompt-and-does-not-overeng.md"
  WHAT IT WAS: A gap-analysis pass on file:29. Flagged: undefined "clean
  copy" instruction, missing explicit mkdir step, undefined patch
  filename convention.
  CORRECTED IN: file:30/33.

file:30 / file:33 "create-a-solid-version-with-all-the-best-pracitce(-2).md"
  WHAT IT WAS: Incorporated all file:28 gap fixes — explicit mkdir,
  deterministic naming rule, defined "clean copy" meaning.
  GAP REMAINING: Still no large-file fetch rule (this caused the next
  failure), still 22 files in one batch.

file:27 "is-that-puprompt-really-using-git-to-create-the-ac-3.md"
  WHAT IT WAS: A quick verification that git commands were genuinely
  present in the prompt (not just described). Confirmed yes, flagged
  two steps needing more literal phrasing.

file:3 "AgentModePatchGuide_v4.md", file:4 "WorkingPromptExample.md"
  WHAT IT WAS: Earlier drafts/reference guides. Superseded by all of the
  above.

file:68 "agent-mode-working-prompt-reproduction-handoff-2026-07-07.md"
  WHAT IT WAS: An EARLIER handover attempt, written BEFORE the plan-split
  fix existed. SUPERSEDED — do not use, it still assumes a single large
  plan file and doesn't know about the root-cause fix.

--- THE ROOT-CAUSE FIX ITSELF ---

code_file:66 "split_patch_plan.py"
  VALUE: The actual fix. Deterministically splits a large plan file into
  per-section and per-target files ONE TIME, outside agent reasoning,
  with a JSON manifest recording line_count + sha256 per file — making
  every subsequent read independently verifiable instead of trusted
  blindly.

code_file:67 "patch_plan_authoring_guidance.md"
  VALUE: Generalizes the fix into 8 authoring rules for any future patch
  plan, so this failure class can't recur in a different task.

code_file:71 / code_file:73 / code_file:74 — prior handover attempts
  VALUE: Iterative handover drafts. code_file:73 and 74 are the most
  current but were execution-focused, not full-learnings-focused — this
  document (the one you're reading) supersedes them as the comprehensive
  reference.

====================================================================
PART 2 — FAILURE PATTERNS AND WHAT CORRECTED EACH ONE
====================================================================

| # | Failure Pattern | Root Mechanism | What Corrected It |
|---|---|---|---|
| 1 | Repo-discovery loops | Prompt didn't declare environment facts upfront | ACCESS_DECLARATION block added (file:29) |
| 2 | Unnecessary git-worktree checks every run | Agent re-verified a fact that's always false in this container | Hardcoded mode_selected=api_mirror (file:69) |
| 3 | Fabricated file content | Agent felt pressure to appear complete | Explicit files_failed/files_not_fetched honest-reporting rule (file:29) |
| 4 | Lost/empty ZIP reported as success | No verification step before claiming success | Mandatory `unzip -l` listing check before success report (file:30/33) |
| 5 | Ambiguous "clean copy" instruction | Undefined term in prompt | Explicit definition added (file:30/33) |
| 6 | Undefined patch naming/directory | No deterministic rule given | Fixed naming convention + fixed output dir (file:30/33) |
| 7 | Large-file fetch thrashing (3 strategies on 1 file) | No single-attempt rule for oversized fetches | Single raw-fetch-once rule added; forbade strategy-switching mid-file (this chat, post file:32) |
| 8 | Wrong-directory writes / duplicate nested mirrors | No pwd verification before writes | Mandatory pwd check before every write (this chat) |
| 9 | 22-file single-shot session collapse | Task scope exceeded reliable single-session complexity | Split into Batch A (001-011) / Batch B (012-022) |
| 10 | Section 7 never successfully read (root cause) | Silent connector truncation on ~190KB single fetch, undetectable by agent | split_patch_plan.py — deterministic one-time pre-split with verifiable manifest (code_file:66) |
| 11 | Zero patches produced despite "source_plan_readable: true" | Self-reported read success was never actually verified against real content | Line-count/sha256 cross-check required before trusting any read (this chat) |
| 12 | Live chunking mid-session causing duplicate mirror builds | Agent invented its own splitting strategy under pressure | Rule: all chunking must happen BEFORE the run, never live (code_file:67, Rule 6) |

====================================================================
PART 3 — RANKED LEARNINGS FOR BUILDING THE NEXT PROMPT
====================================================================
Ranked by how much each one would have prevented, if applied from the start.

RANK 1 — Never trust a "read complete" without independent verification.
  This is the single most important learning. Every other failure either
  stems from this or is made worse by it. Any load-bearing file read must
  be checked against a known line_count and/or sha256 BEFORE the agent
  acts on its content. If verification isn't possible, treat the read as
  failed, not successful.

RANK 2 — Never let the agent split, chunk, or reorganize large content
  live, under its own judgment, mid-session. All structural splitting
  must happen once, deterministically, by a script, before the agent
  session starts. Live improvisation under context pressure is what
  caused the worst failures (duplicate mirrors, thrashing).

RANK 3 — Keep single-session scope small. ~10-12 files per run is a
  reliable ceiling; 22 in one shot reliably collapsed. When in doubt,
  split the task, not just the data.

RANK 4 — Declare fixed environment facts once, don't let the agent
  re-derive them every run (e.g., no live git worktree ever exists here).
  Re-checking a guaranteed-false condition wastes turns and adds no
  safety.

RANK 5 — Require a pwd/location check before every filesystem write.
  Cheap to add, prevented real duplicate-mirror damage.

RANK 6 — Make partial completion a normal, expected, honestly-reported
  outcome (never fabricate to appear complete). This preserves trust in
  the final report even when the run isn't perfect.

RANK 7 — Verify packaged artifacts (ZIPs) with an actual listing command
  before claiming success — a "created" file is not the same as a
  "verified non-empty and complete" file.

RANK 8 — Give deterministic naming/path rules explicitly; never leave
  naming conventions for the agent to invent per-file.

====================================================================
PART 4 — WHAT NOT TO DO (guard against over-engineering)
====================================================================
- Do not add a new rule for every hypothetical failure — only for ones
  with actual observed evidence in this task's history (all 12 patterns
  in Part 2 have evidence; nothing else should be added speculatively).
- Do not narrate this failure history inside the agent's actual working
  prompt — the agent should see clean, forward-only instructions. This
  document is the place for history, not the executable prompt.
- Do not build retry-with-backoff logic, rollback-to-git-tag systems, or
  multi-agent coordination — none of that has any evidence of being
  needed at this task's actual scale (~22 small files).
