---
type: Runbook
id: RUNBOOK-HANDOVER-DETERMINISTIC-ENFORCEMENT-FOR-JIT-GATES-v1.0
title: Handover — close DEC-O7 through DEC-O10 from the read-trace pilot
description: Runnable handover for a fresh session to act on operations/17's findings — fix base_ref, build and live-prove a Stop-hook for the two JIT gates measured as never-honoured, and surface the DEC-O3 governance gap to the operator.
status: current_truth
tags: [handover, runbook, deterministic-enforcement, base_ref, jit-gates, DEC-O7, DEC-O8, DEC-O9, DEC-O10]
---

# Handover: Deterministic enforcement for the two JIT gates that never fire

> Written per `EM-09`'s 4-Dimensional Contract and 5-Component Report
> ([specs/execution-modes/handover.md](../../specs/execution-modes/handover.md)). This handover is
> for continuing work in a **new session** — everything the prior session found is saved to disk
> and indexed in QMD; nothing here depends on that session's chat history.

## 5-Component Forensic & Completion Report (what the prior session found)

### 1. Observation

- Built a real (not simulated) read-trace collector using Claude Code `general-purpose` subagents
  and their raw tool-call JSONL transcripts — not the tool's documented `output_file` (confirmed
  empty, 0 bytes) but the actual populated location:
  `~/.claude/projects/<project>/<parent-session-id>/subagents/agent-<id>.jsonl`.
- 8 cells run (1 arm — the live production contract — × 4 task types × 2 reps), every tool-use event
  parsed from the raw file, not trusted from the subagent's own prose report. Full table with exact
  transcript paths: `operations/17-READ-TRACE-PILOT-AND-BASE-REF-FRAGILITY-FINDINGS.md` §3.
- `<handover>` gate (`ref=specs/execution-modes/handover.md`): **0/2** opened.
- `<trade_off>` gate (`ref=specs/execution-modes/bake-off.md`): **0/2** opened.
- `<schemas>` gate (`ref=specs/governance-schemas.md`): **2/2** opened — but via two *different*
  resolutions: one run found `C:\GitDev\Leela-Cloud-2026\docs\apex\specs\governance-schemas.md`
  (a byte-identical local mirror, confirmed by `diff`, found by local search, not by resolving
  `base_ref`); the other opened the literal `base_ref`-anchored absolute path.
- `research/06-layered-rule-kb/rule-22-pointers.md:41` documents `base_ref` as intended to be
  **relative**; the live contract in `~/.claude/CLAUDE.md` ships it as an **absolute** path into one
  specific repo on one specific machine. The same file's §5 (line ~101) explicitly names "resolve
  against arbitrary parent directories" as a forbidden failure mode — which is exactly what the
  local-mirror resolution did.
- `operations/12-MULTI-ENVIRONMENT-INTEGRATION-HANDOVERS.md` §2 Environment 5 specifies
  `.claude/rules/informatics.md` (Claude Code's native, harness-enforced path-scoped rule) as the
  intended deterministic mechanism. It exists in `apexai-os-meta` but is scoped to *editing* the
  corpus, not *consuming* it — doesn't cover the measured failure. It does not exist at all in
  `Leela-Cloud-2026` (confirmed by `ls`/`find` and independently by `qmd`'s own `leela-agent-rules`
  collection reporting 0 indexed files).
- `Leela-Cloud-2026/.claude/hooks/stop-uncommitted-nudge.py`, wired via `.claude/settings.json`'s
  `Stop` hook, is a **live, proven** deterministic mechanism already running in this exact repo for
  an unrelated check — the pattern to clone, not invent.
- `DEC-O3` ("split `execution-modes.md` only if the test passes") was never satisfied — the test's
  own frontmatter still reads `status: design_not_run` — yet the split happened
  (`git log a6792617`).

### 2. Logic Chain

`operations/14` found Arm C/D tied and flagged it as non-evidence for retrieval → this session built
a real collector and found gate-honouring correlates with task structure (schemas: forces real
content) not gate wording (handover/trade-off: pure prose, never checked) → traced the one
"honoured" gate's inconsistency to a documented, already-known base_ref design contradiction →
traced the fix to an already-proven-live hook pattern in the same repo, so the fix is cloning, not
inventing → one piece of this (whether the ungated split was ever authorized) is a governance
question, not a technical one, and is not this session's or the next session's to decide alone.

### 3. Caveats

- n=2 per cell: unanimous within every cell, so qualitatively solid, but not a statistically powered
  rate. A third rep could sharpen confidence without changing the direction.
- Tested on Claude Code only. Codex CLI (the originally intended harness, matching `operations/14`)
  was unreachable in that session's environment — confirmed by three independent lookup methods.
  Gemini/ChatGPT/Antigravity untested entirely.
- The vendored `docs/apex/` mirror in `Leela-Cloud-2026` may be a perfectly good deployment pattern
  on its own terms. The problem is narrower: the contract gives an agent no deterministic way to
  know *which* copy it opened, and it is not enforced by any rule in that repo at all.
- `DEC-O7`'s fix (making `base_ref` relative) needs the exact target form verified against the
  live `ref="specs/...` path strings before editing — do not copy Rule 22's example string
  (`"apex-meta/informatics/"`) literally; it predates the current `final/` directory layer.

### 4. Conclusion

`DEC-16`'s premise (splitting + JIT-gating preserves reliability while saving tokens) is **falsified
for judgment-type modules and only accidentally true for structurally-forcing ones**. A fix exists
and is not speculative — it is the same deterministic-hook pattern this repo already runs
successfully elsewhere. Four decisions are open (`DEC-O7`–`DEC-O10`, full table in `operations/17`
§9); this handover's job is to close the first three and escalate the fourth.

### 5. Verification Method

- Re-parse any of the 8 cited transcripts with the `python3` one-liner in `operations/17` §3.
  **Check first that the transcript files still exist** — they live under the *prior* session's
  path (`~/.claude/projects/C--GitDev-Leela-Cloud-2026/5cfc414d-5e07-4c16-9902-bf1ec7b0efdb/subagents/`)
  and Claude Code may prune old subagent transcripts; if gone, that's a caveat to note, not a reason
  to doubt the findings (the prose in `operations/17` already captures what each one showed).
- `diff` the two `governance-schemas.md` copies again before assuming `DEC-O7` is still low-risk —
  confirm they haven't silently diverged since this was written.
- `qmd search "DEC-O7 DEC-O8 DEC-O9 DEC-O10 base_ref Stop hook"` against the `apex-informatics-final`
  collection to pull every cited source back up without needing any file path memorized.

---

## 4-Dimensional Handover Contract (what to do next)

### Input & Priority Ledger

Read in this order; stop escalating once a question is answered:

1. **`operations/17-READ-TRACE-PILOT-AND-BASE-REF-FRAGILITY-FINDINGS.md`** — primary evidence base,
   read in full first.
2. `research/06-layered-rule-kb/rule-22-pointers.md` — the contradicted design spec.
3. `operations/12-MULTI-ENVIRONMENT-INTEGRATION-HANDOVERS.md` §2 Environment 5 — intended Claude
   Code mechanism.
4. `apexai-os-meta/.claude/rules/informatics.md` — the existing, mis-scoped path-gated rule.
5. `Leela-Cloud-2026/.claude/hooks/stop-uncommitted-nudge.py` +
   `Leela-Cloud-2026/.claude/settings.json` (`Stop` hook block) — the pattern to clone.
6. `operations/14-ADHERENCE-TEST-RESULTS.md` §"General" findings 3–4 — the prior, independent
   statement of the same "deterministic beats prose" principle, and the "one neutral script, thin
   adapters" cross-harness pattern.
7. `candidates/01-decision-register.md` Part E — existing decision table format; `DEC-O7`–`DEC-O10`
   belong here once resolved (not yet appended — this is an open gap, see Output below).
8. Secondary/optional: the 8 raw subagent deliverable files under the prior session's scratchpad
   (paths listed in `operations/17` §3's table, same directory as each transcript) — only if you
   need to see exactly what a subagent wrote, not just what it opened.

**Ignore**: the full `candidates/04-empirical-test-protocol.md` 10-arm/16-task matrix (18-30 hour
estimate) — out of scope unless the operator explicitly authorizes it (`operations/17` §8 row 4).
Do not attempt to install or re-locate Codex CLI to "complete" the original harness — the pivot to
Claude Code was deliberate and is not a gap to close.

### Process

- Do not re-litigate whether the finding is real. Spot-checking one transcript (per Verification
  Method above) is fine and encouraged; re-running the full pilot from scratch is not the ask.
- Work `DEC-O7` first (cheapest, one line, already contradicts the project's own spec) — but verify
  the exact relative form against live `ref=` strings before editing (Caveat above).
- Work `DEC-O8` next. Follow this corpus's own repeated meta-lesson
  (`operations/16` §3): a hook is not "done" on a pipe test — "this session's own
  `echo '...' | python hook.py` pipe-tests... silently mangled... producing a false 'it works'
  result" is the exact failure this project has hit twice already (Claude and Codex hooks both).
  Pipe-test first, then **prove it live** in a real Claude Code session attempting a real
  handover-triggering task.
- Keep the check logic harness-neutral where practical (`operations/14`'s "one neutral script, thin
  per-harness adapters" pattern) — Gemini CLI and Codex CLI hook support is confirmed to exist
  (`operations/14` §general-3), even though building those adapters now is explicitly out of scope
  (see DoD below) — don't paint yourself into a Claude-only design if a shared core is nearly free.
- `DEC-O9` (fold the two modules back to always-on) is a **fallback only** — don't reach for it
  until `DEC-O8`'s live-proof step has failed **twice** (`<stop_repairing>`).
- `DEC-O10` is **not yours to resolve**. Surface it to the operator plainly (it was already
  surfaced once in `operations/17` §9 and not yet answered) — don't silently pick ratify or revert.
- Anti-drift boundary: scope stays to the two measured-failing modules
  (`handover.md`, `bake-off.md`). Do not generalize the hook to all nine `execution-modes/*.md`
  adapters without the operator asking — the other seven were not measured in this pilot.

### Output (Predefined Meta-Layer & Examples)

- **`DEC-O7`**: one-line edit to `~/.claude/CLAUDE.md`'s `<apex_contract base_ref="...">` attribute.
  Example target shape (verify against live file before committing to this exact string):
  `base_ref="apex-meta/informatics/final/"` — relative, matching Rule 22's documented intent, scoped
  correctly for the current directory layer (not copied verbatim from the Rule 22 doc's older
  example).
- **`DEC-O8`**: new script, naming convention matching the existing three
  (`block-direct-flutter.py`, `session-start-git-status.py`, `stop-uncommitted-nudge.py`) — e.g.
  `Leela-Cloud-2026/.claude/hooks/check-jit-gate-compliance.py`, wired into
  `.claude/settings.json`'s `Stop` hook block alongside the existing three. Consider a harness-neutral
  core script under `scripts/` (mirroring `scripts/check_gate_runner_bypass.py`) with a thin
  `.claude/hooks/` adapter, per the cross-harness pattern already proven in this repo.
- **`DEC-O9`** (fallback only, if reached): edit `~/.claude/CLAUDE.md` to remove the `when=`/`ref=`
  gating on `<handover>` and `<trade_off>`, inlining their adapter content as always-on text instead.
- **`DEC-O10`**: no file edit from you — ask the operator directly (ratify the split retroactively /
  revert pending a real protocol run / run the full `04` protocol first), then log whatever they
  decide.
- **Housekeeping gap to close**: append `DEC-O7`–`DEC-O10` (with final resolutions) into
  `candidates/01-decision-register.md` Part E, matching its existing table format — this was
  intentionally left undone by the prior session (logged only in `operations/17` §9) to avoid
  registering decisions before they were actually made.

### Definition of Done (DoD & Independent Verification)

- **`DEC-O7` done** only when: (a) `grep -o 'base_ref="[^"]*"' ~/.claude/CLAUDE.md` shows the new
  value, **and** (b) a fresh subagent run on the exact schema-r1/r2 prompt
  (`operations/17` §3) is repeated at least twice more, its transcript parsed with the same
  collector method, and resolves to **one consistent path** both times — not just "the attribute
  changed." Re-running the actual read-trace cell is the DoD; a grep alone is not.
- **`DEC-O8` done** only when: (a) a standalone pipe-test of the new hook with synthetic
  `Stop`-event JSON passes, **and** (b) a real, live Claude Code session (not a subagent, an actual
  interactive or scripted session) attempts a genuine handover-triggering task and the hook is
  observed to actually fire and act (block or nudge). Do not declare this done on (a) alone — that
  exact shortcut already produced a false "it works" twice in this corpus's own history
  (`operations/16` §3, items 2 and 3).
- **`DEC-O9` done** only if invoked: confirm via a fresh read-trace cell that the previously-0/2
  content is now present in every run's context (trivially true once inlined, but verify the edit
  didn't break the XML block — run whatever `okf_validator.py`/contract lint already exists).
- **`DEC-O10` done** only when the operator has given an explicit, logged answer — not resolvable by
  any file edit.
- **Forbidden as completion evidence** (`EM-09`'s explicit anti-pattern): a self-verifying script
  that only checks superficial string presence. Completion requires the independent read-trace
  re-run or the live-session proof described above, not a grep confirming a file changed.
