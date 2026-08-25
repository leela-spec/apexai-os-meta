---
name: evidence-driven-workflow-improvement
description: Use when asked to improve a workflow, artifact system, or process based on evidence - enforce real baselines and honest comparison before claiming any improvement.
version: 0.1.0-candidate
metadata:
  hermes:
    tags: [methodology, evaluation, workflow-improvement]
  staged: true
  provenance: "learned from Weekly Orchestration eval-driven improvement pilot (2026-08); project-local, not promoted"
---

# Evidence-Driven Workflow Improvement

A reusable method for improving an operational workflow WITHOUT fooling
yourself. Each step is a gate; skipping one voids the improvement claim.

## The procedure

1. **Real target** - identify the actual job a human/operator performs with the
   workflow. Not file quality, not rubric scores. If you cannot name the job,
   stop.
2. **Real authority** - map which files/skills own which semantics. Record
   paths + hashes. Resolve contradictory authorities BEFORE evaluating anything;
   ambiguous vocabulary invalidates later comparisons.
3. **Faithful baseline** - produce what production actually produces, from
   realistic inputs (never invented ones), using exact current templates.
   Record inputs, provenance, generator identity, constraints in a receipt.
4. **Identify failure** - evaluate the baseline against the real jobs. Verdicts
   PASS/PARTIAL/FAIL per job, each tied to quoted evidence. Note which failures
   are template-rooted vs generation-rooted.
5. **Identify proxy shortcuts** - list every way the improvement could be faked:
   unique hashes, expected strings, self-scores, invented timings, reviewer
   personas. These become forbidden evidence for the rest of the run.
6. **Smallest candidate change** - design the minimal change that targets the
   confirmed failures. Derive candidate designs from independent reviews when
   feasible; preserve material disagreement between reviewers instead of
   averaging it.
7. **Execute real task** - instantiate the candidate against the SAME scenario
   facts as the baseline. Same jobs, same grader stance.
8. **Close evidence** - deterministic checks where possible (section presence,
   tag presence, reference resolution); semantic judgment labeled as such;
   measurements only if a real instrument exists (else `not_measured`).
9. **Compare baseline** - job-by-job delta on identical facts. An improvement
   claim requires the target jobs to improve in the OUTPUTS, visibly.
10. **Regression** - sweep adjacent scenarios (degraded/stale/constrained cases)
    for material regressions. Ownership boundaries and provenance must remain
    coherent; context hops must not increase materially.
11. **Only then claim improvement** - state scope honestly: design-level vs
    production-level; what remains unverified; which decisions belong to the
    operator.

## Hard rules

- Never fabricate approvals, timings, or measurements.
- A reviewer is independent only with fresh context, no sibling visibility, and
  bounded inputs - record identity and isolation status truthfully.
- Mechanical compliance alone is not quality evidence.
- Do not mutate production artifacts during evaluation; patches come only after
  evidence closes AND the operator authorizes.

## Failure signals to watch for

- Evaluations that pass everything (the eval is probably weak).
- Candidates that differ by styling rather than information architecture or
  behavior.
- Reviews that agree too easily - check whether reviewers shared context.
- Improvements measurable only by the author's own scoring.
