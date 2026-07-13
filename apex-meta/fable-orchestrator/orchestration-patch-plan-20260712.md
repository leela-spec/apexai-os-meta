---
title: "Patch plan — orchestration design gaps"
date: 2026-07-12
method: "Macro meta-analysis (confidence-rated) -> correction strategy per item -> patch files, most-load-bearing first. No agents spawned; inspection + direct schema/doctrine edits only. Local files only, no commit/push."
source: "apex-meta/fable-orchestrator/orchestration-design-benchmark-20260712.md"
---

# Patch plan

## 1. Macro meta-analysis — every field flagged, confidence-rated

| # | Field flagged | Evidence read | Confidence this needs correction | Verdict |
|---|---|---|---|---|
| G1 | System B's review-verdict shape (`apex-review-validity.md`, `apex-review-alignment.md`) has no structural falsification-gate field; System A's (`review-verdict.schema.md`) does — `falsification_attempt` object + `evidence_free_pass_gate` block. Both instruct falsification narratively; only A enforces it as a required, checkable field. | Diffed both files directly, line-for-line, above. | **High** — same KB practice (P11), same review purpose (blind meta_detective lens), one system structurally prevents a skipped falsification from silently passing and the other does not. Not documented anywhere as an intentional product difference. | Correct |
| G2 | System A's `run-record.schema.md` has no field to carry usage/token evidence from a real run. System B already has this via the `model-usage-log` skill's `model_usage_delta` (advisory, degrades to `unknown` when missing, never blocks). | Read `run-record.schema.md` in full; read `model-usage-log/SKILL.md` in full. | **Medium** — this is a genuine asymmetry (B has the mechanism, A doesn't), but it's additive, not a defect fix — no run has been broken by its absence. Worth closing because the mechanism already exists in B to copy the pattern from, not because A is unsafe without it. | Correct (additive) |
| G3 | Neither system sets a numeric packet-size ceiling (KB practice P9). | Read `packet-size-budget.md`'s cited status (`working_hypothesis`, no numeric ceiling, U001 open) via the earlier research pass. | **Low** — the KB itself has no evidence-backed number; inventing one now would be guessing dressed as a fix. | No patch — record the decision, do not invent a number |

## 2. Correction strategy + future vision, per item

**G1 — bring System B's review verdict to structural parity on falsification, keep its lighter vocabulary.**
Vision: System B stays a 4-value (`pass/needs_revision/fail/blocked`), lower-ceremony verdict — that
difference is justified by its recurring, lower-per-item-stakes cadence (weekly loop vs. arbitrary
consequential artifacts). What is NOT justified is a reviewer being able to write `pass` with no
falsification attempt recorded. Add the same two structural guarantees System A already has, scoped
to System B's existing shape: (a) a mandatory `falsification_attempt` object per criterion, (b) one
boolean gate (`every_pass_has_falsification_attempt`) that must be true for `overall: pass`. Do not
import System A's 5-value escalation vocabulary, its `evidence_refs` array, or its severity taxonomy
— that would be over-fitting B to A's shape rather than closing the specific gap found.

**G2 — give System A the same advisory, non-blocking usage-capture field System B already has.**
Vision: when the operator actually activates either system's real agents (not a build-time
inspection), the run record should be *able* to carry what the Agent tool's usage block reported,
the same way System B's `model_usage_delta` already can. Add one optional block to
`run-record.schema.md` mirroring B's degrade-to-unknown pattern exactly — advisory only, never
blocks a run, absence is not an error. This closes the asymmetry without inventing new
infrastructure or a metering system neither KB nor either system asked for.

**G3 — no correction. Record the decision.**
Leaving P9 unresolved matches the KB's own evidence state. Fabricating a ceiling would create a
false sense of settled design. The correct "fix" is documenting that this was evaluated and
deliberately left open, so a future session doesn't reopen it as an oversight.

## 3. Patch files, most load-bearing first

1. `.claude/agents/apex-review-validity.md` — add `falsification_attempt` per criterion + `evidence_free_pass_gate` block.
2. `.claude/agents/apex-review-alignment.md` — same, mirrored (both lenses must carry the same structural guarantee or the gap reopens asymmetrically between the two lenses of the *same* system).
3. `apex-meta/orchestration/schemas/run-record.schema.md` — add optional advisory `usage_evidence` block.
4. This file + the benchmark file — record the G3 no-patch decision (already done in the benchmark file's Recommendation section; superseded by this plan).

## 4. Outcome (operator-confirmed 2026-07-12)

- **G1 — applied, kept.** `.claude/agents/apex-review-validity.md` and `apex-review-alignment.md` now
  require a completed `falsification_attempt` and an `evidence_free_pass_gate` block before any
  criterion can pass. Structural parity with System A's review-verdict rigor on this specific point;
  System B keeps its own 4-value vocabulary.
- **G2 — applied.** `apex-meta/orchestration/schemas/run-record.schema.md` gained an optional,
  advisory `usage_evidence` block, mirroring `model-usage-log`'s `model_usage_delta` pattern. Never
  blocks a run; absence only degrades confidence.
- **G3 — no schema change, decision recorded.** No numeric packet-size ceiling was added to either
  system. This matches the KB's own unresolved (`working_hypothesis`) status on the question — a
  future session should not treat this absence as an oversight; it was evaluated on 2026-07-12 and
  deliberately left open pending real evidence.

All changes are local-file edits only; nothing was committed or pushed.
