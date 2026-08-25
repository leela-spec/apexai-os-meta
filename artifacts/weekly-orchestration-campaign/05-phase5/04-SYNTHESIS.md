# 04-SYNTHESIS.md — Independent evaluator synthesis after reviews

```yaml
evaluator_id: SYN-1
model_profile: "ox-alpha via Hermes Agent session"
inputs: [Phase1 findings, Q1-Q20 eval defs, Phase2 baselines, Phase3 baseline eval, R-C review, R-D review]
isolation_note: "fresh evaluation task after both reviews completed; evaluator did not participate in reviewer lens authoring"
```

## Agreements (both reviewers, independently)

| Theme | R-C | R-D | Convergence strength |
| :-- | :-- | :-- | :-- |
| F01 weekly sprint grid must go | remove S-cells (d) | wrong-layer impossible via schema without sprint fields (b/c) | STRONG — same fix, different mechanism |
| F03 delta needs an owned slot | delta block top of daily+weekly (e) | diff of declared emphasis vs actuals consumes handoff (c) | STRONG |
| F04 provenance must move to fact level | inline tags + ledger (b/e) | ledger as schema obligation (b) | STRONG |
| F09 routing owned once | one statement + exceptions escalate | (not directly addressed; implicit in typed refs) | MODERATE |
| Baseline passes came from generator discipline, not templates | implied throughout | stated explicitly as root cause 1 | STRONG |

## Meaningful disagreements (preserved, not averaged)

1. **Enforcement philosophy.**
   - R-C fixes presentation: right information, right depth, visual weight for exceptions. Trusts reading-order and rendering.
   - R-D fixes contracts: typed references, enums, digests, validation gates. Trusts structure making violations impossible.
   - These can conflict: contract strictness can degrade degraded-mode flexibility (R-D's own risk #2), while presentation-only fixes leave duplication mechanically possible (R-D's root cause 1). NOT resolved here by preference — resolved below by which candidate satisfies more Q-jobs with fewer regressions.
2. **Weekly brief day representation.**
   - R-C keeps the improvised Day-emphasis table as the pattern.
   - R-D embeds day_emphasis as tokens inside the structured handoff rather than a visible table.
   - Open question: does the operator need a VISIBLE table (Q4/Q5 readability) or machine-consumable tokens (Q10/Q12 enforcement)? Both may be satisfiable (tokens generate the table), but that is a design commitment neither reviewer made explicitly.

## Unsupported claims rejected

- Neither reviewer fabricated timings or percentages — nothing to reject on evidence grounds.
- R-C's claim that Depth-0 compression improves Q14 is plausible but unproven until a candidate artifact exists; carried as prediction only.
- R-D's digest/version mechanism improves DETECTION of stale consumption (their own admission); it is recorded as such, not as a Q11 improvement claim.

## Candidate architectures (maximally distinct, ≤3)

### CANDIDATE-1 "Presentation-led" (R-C core)
Delta blocks + fact-level source tags + exception-weighted layout + day-emphasis tables replacing grids. Templates change mostly by section surgery; generation stays flexible.
- Predicted improvements: Q1,Q4,Q5,Q9,Q10,Q11,Q13,Q14 (mechanisms cited in R-C f).
- Predicted risks: quiet-day noise; clutter; no mechanical dedup guarantee (F02 only softened).

### CANDIDATE-2 "Contract-led" (R-D core)
Typed reference fields, unified deformation enum, constrained status tokens, prompt input-binding requirements, schema_version coupling. Duplication becomes structurally impossible; provenance becomes ledger columns.
- Predicted improvements: Q8,Q9,Q12,Q15,Q20 plus mechanical F02 elimination (mechanisms in R-D f).
- Predicted risks: degraded-mode rigidity (D-type weeks); broken refs under sloppy generation; migration complexity.

### CANDIDATE-3 "Layered hybrid" (synthesis proposal — smallest change set satisfying both)
Take CANDIDATE-1's three user-visible moves (delta blocks first-position, fact-level source tags, day-emphasis table replacing sprint grid, single route statement with exception escalation) AND CANDIDATE-2's two cheapest structural moves (unified deformation/status enum across doctrine+templates; prompt files gain required inputs:/return:/done: fields). Explicitly DEFERS digests/typed-ref-everywhere (highest complexity, lowest near-term job coverage).
- Predicted improvements: union of the above minus detection-only items.
- Predicted risks: inherits noise risk (C1) and partial-rigidity (C2) at lower intensity each.

## Selection logic for Phase 5 (per campaign rules: evidence next, not prose preference)

All three candidates must be instantiated against the SAME scenario facts
(Case A + Case B constrained day are sufficient for first comparison; D/E added
for regression checks), then re-run Q1-Q20 with fresh evaluation. Advancement
rule from campaign spec applies verbatim: targeted failure improves, no material
regression elsewhere, ownership coherent, provenance intact, hops not increased,
improvement visible in outputs.

Prediction on record before instantiation: CANDIDATE-3 covers the most jobs,
but CANDIDATE-2 uniquely eliminates F02 mechanically — if hybrid instantiation
shows residual duplication, that is the signal to promote typed refs despite cost.
