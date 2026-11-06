---
type: Evidence
id: EVIDENCE-READ-TRACE-PILOT-BASE-REF-FRAGILITY-v1.0
title: Read-trace pilot results — JIT pointer gates are task-structure-dependent, not gate-wording-dependent, and base_ref resolution is non-deterministic across environments
description: An 8-cell pilot (not the full 04-empirical-test-protocol.md matrix) instrumenting real subagent tool-call transcripts to test whether ref= pointer gates actually get opened. Two of three gated modules were never opened; the third was opened via two different, inconsistent path-resolution strategies. Traces this to a documented design contradiction in Rule 22 and an incomplete multi-environment deployment.
status: current_truth
tags: [evidence, read-trace, DEC-16, DEC-M2, base_ref, pointers, falsification, pre-registered, deterministic-enforcement]
---

# Read-trace pilot results — 2026-11-04

> **Scope note.** This is a deliberately scoped-down pilot (1 arm × 4 task types × 2 reps = 8 runs),
> not the full `candidates/04-empirical-test-protocol.md` design (which remains unrun — its own
> structural defects, logged in `operations/16` §2, are untouched by this file). The pilot exists to
> answer the single question blocking the 5-environment rollout cheaply: does a `ref=` pointer
> actually get opened? It also surfaced two findings the protocol's design never anticipated, which
> matter more than the original question.

> **Continuation handover:** [`handovers/HANDOVER-08-DETERMINISTIC-ENFORCEMENT-FOR-JIT-GATES.md`](handovers/HANDOVER-08-DETERMINISTIC-ENFORCEMENT-FOR-JIT-GATES.md)
> is the runnable next-session brief for closing `DEC-O7`–`DEC-O10` below.

## 0. Executive verdict

**The gates are not uniformly honoured, and the one that was honoured was not honoured for the
reason the architecture assumes.** `<handover>` and `<trade_off>` were never followed (0/2 each) —
a fresh agent writes from training knowledge and never opens the pointed-to file, regardless of the
`when=` condition matching exactly. `<schemas>` was followed (2/2) — but by two different path
resolutions across two runs of the identical task, one of which is a documented, explicitly
forbidden failure mode. The apparent reliability of `<schemas>` is confounded by task structure
(you cannot emit a conformant JSON object without real field names), not evidence that `ref=` gating
works as a mechanism. `DEC-16`'s premise — that gated files get read when their condition fires — is
**falsified for judgment-type gates and only accidentally true for structurally-forcing ones.**

## 1. What this answers and what it doesn't

`operations/14-ADHERENCE-TEST-RESULTS.md` found Arm C (inlined) and Arm D (pointer-only) tied 5/6 on
artifact score, and explicitly flagged that as **non-evidence** for retrieval: "This behavioral tie
does not prove that agents opened the pointed-to modules. Run the separate read-trace protocol
before claiming that `ref=` reliably causes retrieval." (`operations/14` §Decision). That protocol
(`candidates/04-empirical-test-protocol.md`) is a 10-arm/16-task design costing an estimated
18-30 execution-hours once its own defects (frozen arm/task count never set; Arm D defined
circularly as "winning contract B1 or B2"; Arm F's two edit-heavy tasks undefined) are fixed. This
pilot answers the narrower, load-bearing question — *does the pointer mechanism get followed at
all, on the live production contract* — at 8 runs instead of 144+, using the actual harness this
operator runs day-to-day (Claude Code) instead of Codex CLI (unreachable in this environment — see
§2).

This file does **not** supersede or replace the full protocol. It does not give statistically
confident per-gate rates (n=2 is a pilot, not a trial). It gives a **go/no-go signal with concrete,
traceable evidence**, per the task's own instruction to pilot before committing to the expensive run.

## 2. Method — deviation from the original design, stated honestly

The task that requested this pilot specified Codex CLI (matching `operations/14`'s harness). Codex
was not reachable in this environment: absent from `bash` `PATH`, absent from PowerShell
`Get-Command`/`where.exe`, and direct invocation of `codex --version` / `codex auth whoami` both
failed with `CommandNotFoundException`, despite `~/.codex/` holding real prior session data from
2026-07-31 through today — meaning it ran here before, in a context this session does not have
access to. Two independent lookup paths failed; per `<stop_repairing>`, pivoted rather than hunting
a third.

**Pivot: Claude Code subagents** (`general-purpose` type, dispatched via the `Agent` tool), each a
genuinely fresh, non-conversational session that still receives the live global
`~/.claude/CLAUDE.md` contract (confirmed harness fact, not assumed). This is arguably *more*
relevant than Codex for this operator's actual risk surface, since Claude Code is the harness this
whole corpus is deployed to run under (Environment 5 of
`operations/12-MULTI-ENVIRONMENT-INTEGRATION-HANDOVERS.md`).

**Collector.** The tool's own documentation names an `output_file` as "the full subagent JSONL
transcript" per completed Agent call — this file was **confirmed empty (0 bytes)** for the first
pilot cell. That is itself the "pipe test is not evidence" trap the task warned about: the
documented access path doesn't deliver. The real, populated transcript was found by directory
search at a different, undocumented location:
`~/.claude/projects/<project>/<parent-session-id>/subagents/agent-<id>.jsonl`. Every tool_use event
in that file carries a `name` (`Read`/`Grep`/`Glob`/`Write`/`Bash`/...) and an `input` object with a
real `file_path`/`path`/`pattern` — a native, directly parseable event stream, not a simulation,
confirmed by direct `python3 -c "..."` parses shown per-cell below.

## 3. Evidence table — all 8 cells, verified against raw transcripts

| Cell | Task (no hint given) | Gate / `ref=` target | Tool-use count | Opened the gated file? | Transcript |
|---|---|---|---:|:---:|---|
| handover-r1 | Write a session handover note | `<handover>` → `specs/execution-modes/handover.md` | 2 (Write, Handback) | **No** | `subagents/agent-a41e3d0715f0e0692.jsonl` |
| handover-r2 | Write a session handover note (different bugfix) | `<handover>` → same | 2 (Write, Handback) | **No** | `subagents/agent-ac8b1b1f910465472.jsonl` |
| trade-r1 | Pick a Python test runner (pytest/unittest/nose2) | `<trade_off>` → `specs/execution-modes/bake-off.md` | 2 (Write, Handback) | **No** | `subagents/agent-a7fe87d49fc0f2ac7.jsonl` |
| trade-r2 | Same task, independent run | `<trade_off>` → same | 2 (Write, Handback) | **No** | `subagents/agent-a2cd2f30427a1b0ff.jsonl` |
| schema-r1 | Emit a `patch_intent.v1` JSON object | `<schemas>` → `specs/governance-schemas.md` | 10 | **Yes — via `C:\GitDev\Leela-Cloud-2026\docs\apex\specs\governance-schemas.md`** (local vendored mirror, found by repo-local `Grep`, not by resolving the contract's literal `base_ref`) | `subagents/agent-a2a76190fa5e0433d.jsonl` |
| schema-r2 | Same task, independent run | `<schemas>` → same | 10 | **Yes — via `c:/GitDev/apexai-os-meta/apex-meta/informatics/final/specs/governance-schemas.md`** (the literal `base_ref`-anchored path) | `subagents/agent-ae692412b3449369c.jsonl` |
| nogate-r1 | Fix an unrelated one-word typo | none (bloat control) | 2 (Write, Handback) | **Correctly opened nothing** | `subagents/agent-adb2bdaadf26e4c32.jsonl` |
| nogate-r2 | Same control, independent run | none | 2 (Write, Handback) | **Correctly opened nothing** | `subagents/agent-a45a575fe6d2aa468.jsonl` |

Every row was parsed from the raw JSONL, not taken from the subagent's own prose report (which, per
this project's own repeated meta-lesson in `operations/16` §3, is necessary but not sufficient to
trust). Reproduction command, run per cell:

```bash
python3 -c "
import json
path = r'<transcript path above>'
with open(path, encoding='utf-8') as f:
    for line in f:
        obj = json.loads(line.strip() or '{}')
        for c in (obj.get('message', {}) or {}).get('content', []) or []:
            if isinstance(c, dict) and c.get('type') == 'tool_use':
                inp = c.get('input', {})
                print(c.get('name'), inp.get('file_path') or inp.get('path') or inp.get('command'))
"
```

## 4. Root cause 1 — gate honouring correlates with task structure, not gate wording

All three gates (`<handover>`, `<trade_off>`, `<schemas>`) use the identical prose mechanism: a
`when="<condition>"` attribute plus a `ref="<path>"` attribute, governed by the same terminal
`<pointers>` rule. The condition matched exactly in all three task designs (there was no ambiguity
about whether "write a handover" triggers `<handover>`, or whether "emit a patch_intent" triggers
`<schemas>`). Only the **schemas** tasks pulled real file content — because a `patch_intent.v1`
object has validatable field names and a concrete envelope shape that cannot be plausibly
hallucinated the way handover prose or a trade-off paragraph can. The mechanism did not cause
compliance; the task's own structural demand did. This means **`DEC-M2`'s assumed benefit (gates
buy precision because they're honoured) does not transfer evenly across modules** — it holds for
schema/structural content and fails for narrative/judgment content, and the failure is invisible to
any test that scores only the final artifact (exactly `operations/14`'s own caveat, now confirmed
with read-trace evidence rather than inferred from a tie).

## 5. Root cause 2 — `base_ref` is implemented as an absolute, single-repo path, contradicting the project's own design

`research/06-layered-rule-kb/rule-22-pointers.md` §2.1 (line 41) documents the intended semantics:
*"any `ref="..."` attribute inside `<apex_contract>` resolves relative to `base_ref="apex-meta/informatics/"`
declared on the root tag"* — a **relative**, portable anchor. The live, shipped contract in
`~/.claude/CLAUDE.md` instead declares `base_ref="c:/GitDev/apexai-os-meta/apex-meta/informatics/final/"`
— an **absolute path into one specific repository on one specific machine**. That contradiction is
not cosmetic: it is the direct cause of the inconsistent resolution observed in schema-r1 vs.
schema-r2 above. Worse, the same Rule 22 document's own §5 "Failure Modes & Not-To-Dos" states,
verbatim: *"Never resolve relative `ref="..."` paths against arbitrary parent directories: Always
anchor resolution to `base_ref`."* Schema-r1 did exactly the forbidden thing — it found a
same-content file via repo-local search, not via `base_ref` resolution — meaning **this project
already predicted and named this exact failure mode, and it happened anyway**, in the second live
trial of the mechanism this file documents.

Confirmed by direct diff, not assumption:

```bash
diff "C:/GitDev/Leela-Cloud-2026/docs/apex/specs/governance-schemas.md" \
     "C:/GitDev/apexai-os-meta/apex-meta/informatics/final/specs/governance-schemas.md"
# 0 lines of output — byte-identical. The two files agree today; nothing guarantees they
# stay in sync, and the contract gives an agent no way to know which one it opened.
```

## 6. Root cause 3 — the intended deterministic mechanism for Claude Code was only half-deployed

`operations/12-MULTI-ENVIRONMENT-INTEGRATION-HANDOVERS.md` §2, Environment 5, names the intended
Claude Code mechanism explicitly: **"Modular path-scoped rules integration via
`.claude/rules/informatics.md`"** — Claude Code's own harness-native, deterministic `paths:`
frontmatter gating (independently confirmed elsewhere in this operator's own prior sessions to fire
6/6, unlike prose). Checked directly:

- `apexai-os-meta/.claude/rules/informatics.md` **exists**, with
  `paths: ["apex-meta/informatics/**", "apex-meta/SmallSkills/OKF_Format/**"]` — but that scope
  triggers only when an agent **edits the informatics corpus itself**. It does not and cannot cover
  the failure mode measured here: an agent doing an unrelated task (writing a handover, choosing a
  test runner) that should *consult* the corpus, not edit it. The one deterministic mechanism this
  project built for Claude Code does not gate the thing that just failed.
- `Leela-Cloud-2026/.claude/rules/` **does not exist at all** — confirmed by `ls`/`find`, both
  reporting "No such file or directory." Leela-Cloud-2026 is a live, actively-worked member of the
  5-environment matrix with its own vendored `docs/apex/` mirror (§5), but the per-repo path-scoped
  rule the runbook's own design calls for was never deployed to it. The content was copied; the
  enforcement was not.

## 7. A deterministic mechanism already proven in this exact repo — the model to copy, not invent

`Leela-Cloud-2026/.claude/hooks/stop-uncommitted-nudge.py`, wired via `.claude/settings.json`'s
`Stop` hook, is a **live, proven** deterministic check that fires on session end regardless of model
attention (`operations/16` §2, row 4). `operations/14`'s own general field finding states it plainly:
*"Deterministic enforcement, not better prose, is what closes a bypass... these hooks fail open on a
crash, timeout, or script error [but are] not a replacement for sandboxing."* This pilot is a second,
independent confirmation of the identical principle on a different failure mode — judgment-gated JIT
pointers, not gate-runner bypass — and the fix category is the same one already proven to work in
this repo: a hook, not refined wording.

## 8. Recommendations — ranked, each a material trade-off per `<trade_off>`

| # | Option | Mechanism | Grounding | Rough cost (I/E/R, 1-100) | Recommendation |
|---|---|---|---|---|---|
| 1 | Make `base_ref` relative/portable | Change the one attribute in the live contract to match Rule 22's own documented design (§5) | Fixes the confirmed cross-environment fragility (§5); zero behavior change where a repo already vendors its own copy | I95/E90/R10 — one-line change, trivially reversible | **Do it** — it already contradicts the project's own spec, costs nothing |
| 2 | Add a `Stop`-hook deterministic check for judgment-gated modules, Claude Code first | Clone the proven pattern in §7: on session end, if the transcript looks like a handover/trade-off output but shows no `Read` of the matching `ref=` file, nudge or block | Directly closes the measured 0/2, 0/2 gap; pattern already live elsewhere in this repo, not speculative | I85/E60/R30 — new script + wiring, needs its own pipe test then a real-session proof (this project's own recurring lesson, `operations/16` §3) | **Do it**, scoped to Claude Code only until proven; Gemini/Codex CLI hook support exists per `operations/14` but is unproven live for this specific check |
| 3 | Fold `handover.md` and `bake-off.md` back to always-on, reversing that slice of `DEC-16` | If #2 isn't built or doesn't hold, accept the token cost for guaranteed delivery | These two modules are small (`DEC-M4`'s token table puts the whole `execution-modes.md` family in the ~2-4k token band); the measured failure rate for these two is 100%, not marginal | I98/E95/R05 — no engineering, pure token-cost trade | **Fallback only** if #2 stalls — don't do both; #2 obsoletes #3 for Claude Code |
| 4 | Fix and run the full `04-empirical-test-protocol.md` matrix | Freeze arm/task count, fix Arm D's circularity, write Arm F's two tasks, run at full n | Needed for publication-grade, cross-model generalizable numbers; this pilot's n=2 is a go/no-go signal, not a confidence interval | 18-30 execution-hours per the task's own prior estimate — now sharper: schema cells (real reads) ran 52-67s each, no-gate/narrative cells ran 6-17s, so a full-matrix estimate must weight by expected gate-hit rate per cell, not assume uniform time | **Leave open as an explicit operator decision** — not a default next action; this pilot already answers the question that was blocking the rollout |

## 9. New operator decisions to register (format matches `candidates/01-decision-register.md` Part E)

| ID | Question | Options | My lean | Blocked by |
|---|---|---|---|---|
| **DEC-O7** | Make `base_ref` relative instead of absolute, per Rule 22's own design? | Yes / No / Defer | **Yes** — already contradicts the project's own spec (§5) | — |
| **DEC-O8** | Build a `Stop`-hook deterministic check for `<handover>`/`<trade_off>` in Claude Code? | Yes / No / Defer | **Yes**, Claude Code first | `DEC-O7` not required first but should land together |
| **DEC-O9** | If `DEC-O8` stalls or fails its own live-proof, fold those two modules back to always-on? | Yes / No | **Yes, as fallback only** | `DEC-O8` outcome |
| **DEC-O10** | `DEC-O3` ("split `execution-modes.md` only if the test passes") was never satisfied — the test (`04-empirical-test-protocol.md`) has `status: design_not_run` in its own frontmatter, confirmed twice in this session — yet the split (git `a6792617`) happened anyway. Ratify retroactively, or revert pending a real test? | Ratify / Revert / Run `04` first | **Not mine to decide** — this is a governance gap, not a technical one; surfacing it, not resolving it | Operator judgment |

## 10. What this file does not claim

- Not a statistically confident per-gate failure rate — n=2 per cell. Every cell was internally
  unanimous (no split verdicts within a cell), which is why a larger n is a confidence exercise, not
  a question-resolving one, per the reasoning given to the operator before this pilot ran.
- Not evidence about Gemini, ChatGPT, Antigravity, or Codex CLI — all untested here; Codex was the
  originally intended harness and was unreachable (§2).
- Not a claim that `docs/apex/` vendoring is wrong — it may be the right per-repo deployment
  pattern. The problem is that the contract gives an agent no deterministic way to know which copy
  it opened, and one repo in the 5-environment matrix has no enforcement rule for its own copy at
  all (§6).
