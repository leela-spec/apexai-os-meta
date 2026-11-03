---
type: Evidence
id: EVIDENCE-ADHERENCE-TEST-RESULTS-v1.0
title: Adherence test results — 2026-11-03 (controlled Codex test and Claude field evidence)
description: Answers whether the v1.0-ultra contract and its referenced modules change agent behavior in a controlled four-arm test, alongside the originating real-repo field evidence.
status: current_truth
tags: [evidence, adherence, codex, claude-code, hooks, empirical]
---

# Adherence test results — 2026-11-03

> Named output slot per
> [`handovers/HANDOVER-07-PRE-ROLLOUT-ADHERENCE-TEST.md`](handovers/HANDOVER-07-PRE-ROLLOUT-ADHERENCE-TEST.md)
> §5. This file now contains that pre-registered 6-task × 4-arm controlled test and the earlier
> real-world observation from one Claude Code session in `Leela-Cloud-2026`. The controlled test
> answers whether the instruction payload changes behavior. The field evidence records what failed
> during a long session. Neither substitutes for the separate read-trace protocol.

## Controlled test pre-registration — 2026-11-03

The runner recorded these predictions before spawning any test agent:

- Arm B will exceed Arm A by at least 3 of 6 tasks.
- Arm C will exceed Arm D because agents will honour inlined modules more often than `ref=` pointers.
- Arm D will approximately equal Arm B because a pointer will add no effect beyond the contract text.

The runner will score only the saved artifact for each cell. A task earns `yes` only when its binary
observable is present in that artifact. Marker checks verify arm delivery separately and never count
toward the adherence score.

## Controlled test results

The contract changed behavior. Arm B exceeded Arm A by exactly the pre-registered threshold. Inlined
modules and pointer-only modules tied, while the single-owner reuse task failed in every arm.

| Task | Principle | A control | B contract | C +modules | D +pointer |
|---|---|:---:|:---:|:---:|:---:|
| 1 | `FA-13` inline lists | [no](adherence-test-artifacts/2026-11-03/task-1-arm-A.txt) | [yes](adherence-test-artifacts/2026-11-03/task-1-arm-B.txt) | [yes](adherence-test-artifacts/2026-11-03/task-1-arm-C.txt) | [yes](adherence-test-artifacts/2026-11-03/task-1-arm-D.txt) |
| 2 | `FA-01` history separation | [no](adherence-test-artifacts/2026-11-03/task-2-arm-A.txt) | [yes](adherence-test-artifacts/2026-11-03/task-2-arm-B.txt) | [yes](adherence-test-artifacts/2026-11-03/task-2-arm-C.txt) | [yes](adherence-test-artifacts/2026-11-03/task-2-arm-D.txt) |
| 3 | `WP-23` reference the owner | [no](adherence-test-artifacts/2026-11-03/task-3-arm-A.txt) | [no](adherence-test-artifacts/2026-11-03/task-3-arm-B.txt) | [no](adherence-test-artifacts/2026-11-03/task-3-arm-C.txt) | [no](adherence-test-artifacts/2026-11-03/task-3-arm-D.txt) |
| 4 | `FA-10` Information Mapping | [yes](adherence-test-artifacts/2026-11-03/task-4-arm-A.txt) | [yes](adherence-test-artifacts/2026-11-03/task-4-arm-B.txt) | [yes](adherence-test-artifacts/2026-11-03/task-4-arm-C.txt) | [yes](adherence-test-artifacts/2026-11-03/task-4-arm-D.txt) |
| 5 | `<ground>` command-carrying claims | [no](adherence-test-artifacts/2026-11-03/task-5-arm-A.txt) | [yes](adherence-test-artifacts/2026-11-03/task-5-arm-B.txt) | [yes](adherence-test-artifacts/2026-11-03/task-5-arm-C.txt) | [yes](adherence-test-artifacts/2026-11-03/task-5-arm-D.txt) |
| 6 | `<product_first>` / `<new_machinery>` | [no](adherence-test-artifacts/2026-11-03/task-6-arm-A.txt) | [no](adherence-test-artifacts/2026-11-03/task-6-arm-B.txt) | [yes](adherence-test-artifacts/2026-11-03/task-6-arm-C.txt) | [yes](adherence-test-artifacts/2026-11-03/task-6-arm-D.txt) |

**Totals:** A 1/6 · B 4/6 · C 5/6 · D 5/6.

### Prediction verdicts

- **B > A by at least 3 of 6 — HELD.** The observed difference was exactly 3.
- **C > D — FAILED.** Both arms scored 5/6.
- **D approximately equals B — HELD.** D exceeded B by one task.

### Decision

Apply HANDOVER-07's pre-registered `C ≈ D` branch: proceed with the rollout architecture. This
behavioral tie does not prove that agents opened the pointed-to modules. Run the separate read-trace
protocol before claiming that `ref=` reliably causes retrieval. Treat `WP-23` as the unresolved
behavioral failure: every arm restated the rule instead of returning a reference-only module.

### Run integrity

- All 24 cells used fresh, non-conversational Codex CLI sessions with model `gpt-5.6-sol`.
- Arm A received the task and runner marker only. A temporary `CODEX_HOME` omitted the global
  `AGENTS.md`; `Test-Path $env:CODEX_HOME\AGENTS.md` returned `False` before scoring.
- Arms B, C, and D received the exact contract. Arm C received both complete modules inline. Arm D
  received only their absolute paths and filesystem read access.
- The live JSONL stream showed the correct arm marker as the first agent message in all 24 cells.
  The command below independently verifies 24 saved artifacts and zero missing final markers.

```powershell
$files = Get-ChildItem operations/adherence-test-artifacts/2026-11-03 -Filter 'task-*-arm-*.txt'
$bad = @($files | Where-Object { (Get-Content $_ -TotalCount 1) -notmatch '^ARM_[ABCD]_MARKER$' })
"files=$($files.Count) bad_markers=$($bad.Count)"
# files=24 bad_markers=0
```

## Field evidence — what was run

A repo-local `AGENTS.md` layered on top of the global `apex_contract`, executing a bundle of five
real bug-fix tickets (#206-#210) under a parent Epic. Full method, ground-truth sourcing (harness
transcript, independent `git diff`, independent re-run of the repo's own gate script — never the
agent's self-report), and the complete finding set live at
`docs/audits/2026-11-03-agent-adherence-inter-feature-runtime-reliability/README.md` in the subject
repo (not duplicated here — that file is the originating artifact; this file states the portable
conclusion only, per `<ground>`: find the owner, don't restate it).

## Field evidence findings, split by what generalizes and what doesn't

### General — applies to any LLM coding agent, any harness (Claude, Gemini, Codex), evidenced by multiple independent sources, not just this one run

1. **Rules drift is real and session-length-dependent.** A rule loaded once at session start
   measurably loses salience as tool-output volume accumulates; multiple independent sources place
   the onset around message 20-30. In this run, the first violation of an explicit, unambiguous
   repo rule occurred well past that window, after 10 clean turns, and recurred 10 more times
   without self-correction. **Implication for the rollout this corpus exists to inform**: a
   long-session agent cannot be assumed to still be weighting a system-prompt rule the same way at
   turn 60 as at turn 1. Prose alone does not survive session length.
2. **The cheaper path wins by default under no adversarial pressure.** The agent did not need
   "pressure" or an adversarial framing to bypass a stated rule — ordinary iterative implementation
   was sufficient, because the forbidden path (a direct, fast, immediate-feedback tool call) stayed
   exactly as reachable as the correct one (a slower, batched gate-runner call) the entire time nothing
   structurally favored the correct path.
3. **Deterministic enforcement, not better prose, is what closes a bypass.** A `PreToolUse`-class
   hook — present in some form in Claude Code, Gemini CLI, and Codex CLI as of this writing, each
   with its own native config format and location — is the only mechanism in this corpus proven to
   close a bypass outright rather than reduce its likelihood. It does so by not depending on model
   attention at all.
   - Shared limitation, also confirmed across harnesses: these hooks **fail open** on a crash,
     timeout, or script error. A hook is a guardrail layered on top of sandboxing/approval policy,
     not a replacement for it.
4. **The right split for a cross-harness guard is: one neutral script, thin per-harness adapters.**
   Writing the actual check logic once, in a plain CLI script with no vendor-specific I/O, and
   giving each harness only a small adapter that translates its own hook JSON shape to that script's
   plain contract, avoids triplicating policy logic across Claude/Gemini/Codex config formats. This
   matches the pattern independently adopted by several open guard-rail projects for the same
   problem, not a convention invented for this corpus.
5. **A correct rule placed past the attention horizon gets silently skipped.** The subject repo's
   commit trigger already stated when to commit, but it sat near the end of a 230-line carrier.
   Two sessions failed to act on it. The evidence supports top-loading the trigger, not restating
   it in a second owner.

### Repo-specific — true only of `Leela-Cloud-2026`, do not generalize

- The specific bypassed rule (`flutter analyze`/`flutter test` must route through
  `python scripts/gates.py`) is that repo's own gate-runner architecture; no other repo in this
  corpus has an equivalent.
- The specific hook files (`.claude/hooks/block-direct-flutter.py`,
  `.claude/hooks/session-start-git-status.py`) and their harness-neutral backing scripts
  (`scripts/check_gate_runner_bypass.py`, `scripts/session_preflight_git_status.py`) are that repo's
  artifacts, proven live in that repo only.
- The existing `AGENTS.md` commit trigger and its placement are that repo's own carrier text.

## Open, not yet done

The Gemini CLI and Codex CLI adapters exist and pass standalone pipe tests, but neither has been
proven live in its native harness. The 16-task, 9-arm read-trace protocol also remains unrun. That
protocol must determine whether `ref=` causes a module read; this behavioral test measures only the
artifact outcome.

## Sources

- `docs/audits/2026-11-03-agent-adherence-inter-feature-runtime-reliability/README.md` (Leela-Cloud-2026) — full method, transcript citation, and finding set.
- `docs/audits/handovers/2026-11-03-{a,b,c}*.md`, `2026-11-03-inter-feature-runtime-reliability-fixes-handover.md` (Leela-Cloud-2026) — the four blind real-task handovers this corpus's adherence-test design produced, one of which (D, the runtime-reliability bundle) is the subject of this evidence file.
