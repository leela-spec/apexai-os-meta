# REVIEW PACKET — Weekly Orchestration Campaign Phase 4
You are an isolated reviewer. You did not generate the material under review.
You cannot see sibling reviewers or any generator conversation. Your output is
graded on evidence quality, not agreement with anyone.

## What this packet contains (your ONLY authorized inputs)
1. This file (task + rules).
2. Phase 0 authority map: `artifacts/weekly-orchestration-campaign/00-phase0/00-AUTHORITY-MAP.md`
3. Phase 0 contradiction register: `artifacts/weekly-orchestration-campaign/00-phase0/00-CONTRADICTION-REGISTER.md`
4. Phase 1 findings: `artifacts/weekly-orchestration-campaign/01-phase1/01-FINDINGS.okf.md`
5. Phase 1 eval cases: `artifacts/weekly-orchestration-campaign/01-phase1/01-EVAL-CASES.yaml`
6. Phase 2 input corpus: `artifacts/weekly-orchestration-campaign/02-phase2/02-INPUT-CORPUS.md`
7. Baseline artifacts (read-only): everything under
   `artifacts/weekly-orchestration-campaign/02-phase2/02-BASELINE/` — five case
   directories, each with weekly brief, daily brief, flow card(s), prompt index,
   prompts, receipt.
8. Production templates (read-only):
   - `.claude/skills/PrecapWeek/weekly-command-brief-template.md`
   - `.claude/skills/PrecapNextDay/templates/precap-next-day-brief-template.md`
   - `.claude/skills/PrecapNextDay/templates/flow-execution-card-template.md`
   - `.claude/skills/PrecapNextDay/templates/prompt-files-and-index-template.md`

## FORBIDDEN
- Reading anything else in `04-phase4/reviewers/` except your own directory.
- Reading campaign chat/session history (you have none).
- Modifying ANY file outside your own reviewer directory.
- Fabricating measurements, approvals, elapsed times.
- Self-certifying improvement claims.

## Output contract — write exactly these files:
1. `review.md` containing ALL SEVEN sections:
   a. Diagnosed root causes tied to finding IDs (F01–F10); own diagnoses use your namespace `<YOUR-ID>-N*`.
   b. Proposed information architecture (which layer owns which block).
   c. ONE full-fidelity redesigned artifact example — pick one baseline artifact,
      keep its underlying facts, show the redesign completely (not a sketch).
   d. What should be removed (each removal tied to a finding).
   e. What moves between layers (source layer -> target layer -> why).
   f. Which Q1–Q20 outcomes improve and the causal mechanism — mechanism-based
      predictions only; no invented percentages/timings; write not_measured where
      you cannot measure.
   g. Risks/regressions + how to detect them.
2. `receipt.yaml`: reviewer id, lens, model/profile you actually ran as,
   execution primitive, isolation status (you ARE isolated — state it), files
   read (paths), tools used, measurements performed (or none).

## Blocker protocol
Do NOT stop for missing optional context. If something blocks review, return a
structured note at top of review.md:
status: BLOCKED_FOR_REVIEW / missing / classification (source_missing |
capability_missing | authority_conflict | genuine_operator_decision) /
recommended_parent_action. Missing optional specialist capability is
capability_missing — apply your documented methodology fallback and label it.

## Evaluation stance
Judge against operator jobs Q1–Q20 (listed in eval cases file). "Can the
operator do the job from the artifact?" — not aesthetics. Anchor every claim
in quoted file evidence (path + quote). Mechanical compliance alone is NOT
quality evidence.
## YOUR LENS: Systems / Contract Architecture (R-D)
Focus: authority, provenance, duplication, state ownership, handoffs,
weekly-vs-daily boundary integrity. You care about whether each block of each
artifact has exactly one owning layer, whether references resolve instead of
restating, whether gate/provenance semantics stay unambiguous, and whether the
handoff chain (weekly brief -> daily brief -> flow card -> prompt) enforces or
merely suggests its ownership rules. The contradiction register's C-05 tension
is directly in scope.