# 03-BASELINE-EVAL.md — Baseline capability evaluation (Phase 3)
> Central question per case: "Can the operator perform the defined job from the
> produced artifact?" - not "does the expected field exist?"
> Scale: PASS / PARTIAL / FAIL / NOT_APPLICABLE.
> `objective` = deterministically observable; `judgment` = requires semantic
> evaluation. No numeric scores: no measurement instrument exists in this pilot.

## Scope note

Q1-Q20 were evaluated against Case A artifacts as primary evidence, with
Cases B/C/D/E consulted where their scenario stresses a specific job. The daily
briefs used here are the BASELINE generation (which already deviated from the
raw template by adding delta blocks and day-emphasis tables - see receipt
fidelity notes). Where baseline generation itself fixed a template gap, that is
recorded honestly: it means the TEMPLATE fails the job and the fix exists only
because the generator chose to deviate. Template-level verdicts drive Phase 4.

## Weekly Command Brief jobs

| Job | Verdict | Evidence | Notes | Type |
| :-- | :-- | :-- | :-- | :-- |
| Q1 what changed vs last week | PARTIAL | case-A weekly brief has no dedicated change section; carry-forward framing exists in "Why this week" lines but nothing names deltas vs prior week | template provides NO delta structure; only prose accident could answer this | judgment |
| Q2 top 2-4 outcomes | PASS | Success at week end lists 2 bullets (A); reduced to 1 in B | answerable from top third of artifact | objective+judgment |
| Q3 why now | PASS | per-project "Why this week" fields present in all cases | direct template section | objective |
| Q4 Monday intent | PARTIAL | Day-emphasis table gives directional answer (A/B/C/E); raw template would give sprint goals instead (wrong layer, F01) | verdict depends on which template variant - the shipped Matrix-2 grid FAILS this job by mixing layers | judgment |
| Q5 capacity constrained | PASS* | B states 55% capacity + per-day deformation table; A/C/D state standard capacity explicitly | *only because baseline generator added the table; raw template buries FreeT/Meets fragments in Matrix-2 cells with no validation | objective |
| Q6 blocked/deferred | PASS | Deliberately parked + deferred sections present in all cases with reasons | template section exists; generator complied | objective |
| Q7 decision needing input | PASS | Review needed line + review flags with Operator action, top-of-artifact | works in all five cases | objective |
| Q8 confirmed vs assumed | PARTIAL | Provenance section carries Confidence + Assumptions, but per-fact confirmed/assumed status absent - assumptions listed separately from facts they underpin (D shows the cost: staleness caveats live far from the priorities they qualify) | template has confidence block, not fact-level status | judgment |
| Q9 fact provenance | PARTIAL | provenance section present but terminal-positioned; individual facts inside priorities/work items carry no inline source markers; reader must trust wholesale or scroll | F04 placement problem persists even in improved generation | objective (marker presence) |
| Q10 wrong-layer content | PARTIAL | Baseline generation replaced sprint-grid with day-emphasis table (correct layering) - but this FIX IS NOT IN THE TEMPLATE; anyone generating from the shipped template gets 48 sprint cells | template-level FAIL; generation-level pass | objective |

## Daily Brief jobs

| Job | Verdict | Evidence | Notes | Type |
| :-- | :-- | :-- | :-- | :-- |
| Q11 changed since plan/yesterday | PARTIAL | baseline daily briefs lead with delta tables (A-E all have them) - BUT the shipped template contains no delta section at all (`Continuity from the week:` is the closest line) | template-level FAIL; generator deviation carried the job | objective (section presence checkable) |
| Q12 execution order + why | PASS | Cross-flow execution order numbered with reasons in every case | template section exists and works | objective |
| Q13 compressed/blocked/omitted | PASS | FULL/COMPRESSED/MINIMAL/OMITTED vocabulary used with capacity reasons (B TUE, E F1) | template supports statuses; constrained-day presentation required generator care, not template force | objective+judgment |
| Q14 exact next action | PASS | header Next action + card Start-or-resume exact step | consistent across cases | objective |
| Q15 where detail lives | PASS | Open Flow Execution Card refs resolve to files that exist in each case dir | checked paths exist on disk | objective |

## Flow/Prompt jobs

| Job | Verdict | Evidence | Notes | Type |
| :-- | :-- | :-- | :-- | :-- |
| Q16 worker self-sufficiency | PASS | each prompt binds concrete inputs + bounded return format; card carries execution context | contrast with corpus prompts (unbounded deliverables) | judgment |
| Q17 task-specific inputs | PASS | e.g., f1-s2-walk references index.yaml + subtree listing; f2-s2-map needs SOURCE_MAP + ID space | every prompt names its own inputs | objective |
| Q18 concrete output | PASS | every prompt defines a return block schema (SCHEMA_CHECK, WALK_REPORT, CLASSIFICATION_SUMMARY...) | unbounded phrases absent | objective |
| Q19 done/stop/evidence conditions | PASS | Done when + Stop conditions present per sprint and are verifiable (coverage counts, classification completeness) | cards carry same per sprint | objective+judgment |
| Q20 S1/S2/S3 semantic difference | PASS | sprints differ by role content (pre-flight vs walk vs classify), not label swap; bodies diverge substantively | again: generator discipline, not template force - template quality-check list does not measure this | judgment |

## Cross-case observations

1. **The decisive pattern:** most PASS verdicts above hold because the baseline
   GENERATOR deviated from or exceeded the shipped templates (delta blocks,
   day-emphasis vs sprint grid, bounded prompt schemas). The templates
   themselves fail or barely support Q1/Q4/Q10/Q11/Q17/Q18/Q20. This is
   precisely F01/F03/F06 manifesting at template level, and it defines where
   Phase 4 redesign must act: the templates, not one good generation.
2. **Provenance placement (Q9)** failed in ALL generations including careful
   ones - the template position (bottom section) survives any single-pass fix.
3. **Constrained/degraded days (Q13)** worked but required the generator to
   invent presentation (capacity budget table, DEGRADED flag prominence).
4. **No fabricated measurements** were needed for any verdict: every row is
   section-presence, path-existence, or content-inspection based.

## Baseline eval conclusion for Phase 4 intake

Template-rooted failures confirmed: F01 (weekly wrong-layer grid),
F03 (no delta section), F04 (provenance terminal + no inline markers),
F05 (no constrained-day presentation contract), F06 (prompt quality checks
don't test specificity), F09 (routing repetition across three surfaces -
visible in E's index/card/prompt triple statement). F02 partially addressed by
generation discipline but not enforced anywhere.

These six template-rooted failure classes are the review lenses' target list.
