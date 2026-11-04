---
type: Evidence
id: EVIDENCE-PROJECT-CLOSEOUT-ADHERENCE-v1.0
title: "Project closeout — adherence testing and deterministic enforcement, 2026-11-03"
description: Single entry point for a future AI session to load this project's full arc without re-deriving it — what was built, what was found, what is still open, and the one meta-lesson that recurred four times.
status: current_truth
tags: [evidence, closeout, adherence, deterministic-enforcement, index]
---

# Project closeout — 2026-11-03

**If you are an AI session picking this up cold: read this file top to bottom before opening
anything else it links to. It is written to be the only thing you need to read before deciding
what to open next.**

## 0. What this project answered

Two questions, pursued together because the second grew out of the first:

1. **Does an agent actually apply the instruction corpus (global carrier + a subject repo's
   `AGENTS.md`), or does it behave the same with or without it?** Tested two ways: real-OpenProject
   field evidence (one real Claude Code session, real bug-fix tickets) and a controlled, pre-
   registered synthetic test (Codex CLI, 4→10 arms).
2. **For every prose rule in that corpus, could it instead be a deterministic check — a gate, a
   test, a hook, a linter — so adherence does not depend on a model remembering a rule at turn 60
   the way it did at turn 1?** Answered rule-by-rule, then acted on the highest-value findings:
   built, broke, fixed, and proved three real checkers and three real hooks.

## 1. The arc, in order, with the artifact that proves each claim

| Step | What happened | Artifact |
|---|---|---|
| 1 | Four blind, real-OpenProject-issue handovers written in `Leela-Cloud-2026`, deliberately carrying no meta-commentary about what they test (an earlier draft that named the rules under test was rejected and rewritten) | `Leela-Cloud-2026/docs/audits/handovers/2026-11-03-{skill-tree-bundle-fusion-reconciliation,skill-tree-structural-vocabulary,path-rhythm-tp-priority-ui,inter-feature-runtime-reliability-fixes}-handover.md` |
| 2 | Handover D (5 real runtime-reliability bug-fix tickets, #206-#210) was actually executed by a real Claude Code agent | Session transcript `~/.claude/projects/C--GitDev-Leela-Cloud-2026/3daefdf7-....jsonl`; outcome commit `Leela-Cloud-2026@b01edf61` |
| 3 | Ground-truth audit of that execution — harness transcript + independent `git diff` + independent gate re-run, never the agent's self-report — found an explicit repo rule bypassed 11 times (`flutter test`/`analyze` run directly instead of through `scripts/gates.py`) | `Leela-Cloud-2026/docs/audits/2026-11-03-agent-adherence-inter-feature-runtime-reliability/README.md` |
| 4 | Built real deterministic enforcement for that one rule: Claude Code `PreToolUse` hook, proven live; Gemini CLI and Codex CLI equivalents, pipe-tested only | `Leela-Cloud-2026/scripts/check_gate_runner_bypass.py` + `.claude/`, `.gemini/`, `.codex/` hook configs |
| 5 | Broadened the question to the whole corpus: swept the global carrier, its nested execution-mode specs, `AGENTS.md`, and nested `agents/*.md`, classifying every rule A (already deterministic)/B (feasible, unbuilt)/C (judgment, not worth forcing) | `operations/15-PROSE-TO-DETERMINISTIC-TRANSLATION-FINDINGS.md` |
| 6 | In parallel, a pre-registered controlled test ran independently via fresh Codex CLI sessions (not this session) — confirmed the contract changes behavior (B > A), found `WP-23` ("reference the owner, don't copy") fails in **every** arm including the one with the full contract, found the `C ≈ D` (inline-module vs. `ref=`-pointer) tie is behaviorally real but not proof of retrieval | `operations/14-ADHERENCE-TEST-RESULTS.md` |
| 7 | Built the highest-value `B` finding from step 5 (`GS-12`/`GS-13` bake-off/decision-matrix shape, declared in `governance-schemas.md` but never enforced) — **synthetic fixtures alone passed on the first try and would have shipped a broken checker**; rejected as insufficient evidence, rebuilt against two real decisions instead, which found and fixed 3 real bugs across two rounds | `tools/check_decision_bakeoff_shape.py`, wired into `tools/okf_validator.py` (scoped to apex-meta deliberately — confirmed this corpus's validator is never run against any downstream repo) |
| 8 | Built a detector for the one rule proven to fail in every arm (`WP-23`, step 6) | `tools/check_governed_markdown_duplicates.py` — found 4 real violations (`patch-discipline.md` copying blocks owned by `execution-modes.md`, byte-identical, manually confirmed), a clean control, and a CLI-misuse guard added after independent verification hit the exact misuse live |
| 9 | A real Codex CLI run found the Codex hook from step 4 **failing open** — `flutter analyze` executed instead of being blocked, because `$CODEX_PROJECT_DIR` env-var substitution doesn't work in a Codex hook command string | Fixed, pushed `Leela-Cloud-2026@6786adc1`; the identical unverified assumption in the Gemini hook was found and fixed pre-emptively, still not proven live (`Leela-Cloud-2026@1359d42f`) |
| 10 | Added `SessionEnd` (Gemini)/`Stop` (Codex) advisory nudges mirroring the Claude `Stop` nudge — never auto-commit, since "is this verified" is a judgment call | `Leela-Cloud-2026@0fb79a73` |
| 11 | Scoped (did not run) the existing but under-specified read-trace protocol for whether `ref=` pointers are actually followed, not just behaviorally tied | `candidates/04-empirical-test-protocol.md` — found it claims "4 arms / 12 tasks" but actually defines 10 arms / 16 tasks, Arm D circularly depends on an unresolved B1/B2 winner, Arm F needs two undefined tasks; not run |
| 12 | Independent re-verification of steps 7-10 by re-running every claimed command against real files — caught and corrected the duplicate-file-copy misuse (step 8) and confirmed the Codex/Gemini fix (step 9) actually works | This closeout session |

## 2. Current state of every artifact — what's live, what's open

| Artifact | Repo | State |
|---|---|---|
| `scripts/check_gate_runner_bypass.py` + Claude Code hook | `Leela-Cloud-2026` | **Live, proven**, blocks real sessions today |
| Gemini CLI hook (same rule) | `Leela-Cloud-2026` | Fixed, pipe-tested, **not proven on a real Gemini CLI install** |
| Codex CLI hook (same rule) | `Leela-Cloud-2026` | **Live, proven** — found broken by a real run, fixed, re-proven |
| `scripts/session_preflight_git_status.py` + 3 harness adapters | `Leela-Cloud-2026` | Claude proven live; Gemini/Codex pipe-tested only |
| `Stop`/`SessionEnd` commit nudges, all 3 harnesses | `Leela-Cloud-2026` | Claude pipe-tested; Gemini/Codex pipe-tested only; none auto-commit by design |
| `check_vendor_drift.py` wired into `gates.py` | `Leela-Cloud-2026` | **Live** — was unwired since before 2026-10-28, now a real fast-tier gate, full canary run 16/16 GREEN |
| `tools/check_decision_bakeoff_shape.py` | `apexai-os-meta` | **Live** — wired into `okf_validator.py`'s `validate_bundle()`, runs on every `--target` invocation, scoped to apex-meta only |
| `tools/check_governed_markdown_duplicates.py` | `apexai-os-meta` | Standalone, committed, **not** wired into `okf_validator.py` or CI — needs an explicit ownership manifest first, a separate decision |
| `candidates/04-empirical-test-protocol.md` | `apexai-os-meta` | Needs repair (freeze the real arm/task count, define Arm F's missing tasks, fix Arm D's circular dependency) before it can run |
| `AGENTS.md` §7 commit/push authorization | `Leela-Cloud-2026` | Was already correct and pre-authorized the whole time — the real finding was that it sits past `GS-03`'s own top-loading horizon and got missed on a first read, not that it was ambiguous |

## 3. The one meta-lesson that recurred four times — read this even if nothing else

**Every verification layer this project added still needed a human or a second independent check to
catch its own bugs, and every time one did, it found something real:**

1. `check_decision_bakeoff_shape.py` passed its own synthetic fixtures on the first try. The operator
   rejected that as insufficient ("find an open project with a real bake-off... real life decisions")
   and was right to — real-data testing found 2 real detection bugs the fixtures could never have
   caught.
2. This session's own `echo '...' | python hook.py` pipe-tests (used repeatedly for the Claude/Codex
   hooks) silently mangled backslash-escaped JSON on this shell; the hook's fail-open-on-parse-error
   behavior masked it, producing a false "it works" result that a later, more careful test caught.
3. A real Codex CLI run found the Codex hook failing open in production — the schema assumption
   (`$CODEX_PROJECT_DIR` substitution) had only ever been checked against documentation, never a real
   install.
4. This closeout's own first run of `check_governed_markdown_duplicates.py` produced nonsense
   self-matching output — not a bug in the tool, but the owner file passed twice (once via `--owner`,
   once in the candidate list), a misuse the tool now rejects with a clear error specifically because
   someone hit it for real and reported it back.

**The pattern in all four**: self-test and documentation-grounded assumptions are necessary but not
sufficient. Nothing in this project was trusted as "done" until it had been run against something
real — a real decision, a real harness, a real repo file, a real misuse — and three of the four times
that real-world check found a genuine bug self-test had missed. If you are extending this work:
run the thing against real data before reporting it as working, and expect to find something.

## 4. Full file index

**`Leela-Cloud-2026`**:
- `docs/audits/handovers/2026-11-03-*.md` — the 4 blind test handovers (3 unused as designed, 1 executed)
- `docs/audits/2026-11-03-agent-adherence-inter-feature-runtime-reliability/README.md` — the field-evidence audit, including the live Codex-failure correction in §5
- `scripts/check_gate_runner_bypass.py`, `scripts/session_preflight_git_status.py` — harness-neutral logic
- `.claude/hooks/*.py`, `.gemini/hooks/*.py`, `.codex/hooks/*.py` + their harness config files — thin per-harness adapters
- `scripts/gates.py` — `check_vendor_drift` entry added
- `AGENTS.md` §1 `commit_granularity` (pointer only, not restated) and §7 (the actual rule)
- `agents/gates.md` — inventory table entry for the new checker

**`apexai-os-meta`** (`apex-meta/informatics/final/`):
- `operations/13-INSTRUCTION-ADHERENCE-FIELD-EVIDENCE-HANDOVER.md` — the original n=1 this project's evidence supersedes
- `operations/14-ADHERENCE-TEST-RESULTS.md` — controlled Codex test + field evidence
- `operations/15-PROSE-TO-DETERMINISTIC-TRANSLATION-FINDINGS.md` — the full rule-by-rule sweep
- `operations/16-...` — this file
- `tools/check_decision_bakeoff_shape.py`, `tools/check_governed_markdown_duplicates.py` — the two new checkers
- `tools/okf_validator.py` — wiring point for the first
- `candidates/04-empirical-test-protocol.md` — the unrun, needs-repair read-trace protocol
