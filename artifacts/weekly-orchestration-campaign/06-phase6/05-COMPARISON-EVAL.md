# 05-COMPARISON-EVAL.md — Baseline vs CANDIDATE-3 (same scenario facts)

```yaml
evaluator_id: EVAL-CMP-1
model_profile: "ox-alpha via Hermes Agent session"
method: same Q1-Q20 jobs applied to baseline artifacts vs candidate-3 instantiations; deterministic checks where possible
blind_note: "artifacts compared side-by-side on identical facts; candidate provenance not hidden from evaluator file layout but content-level comparison performed before consulting synthesis predictions"
```

## Weekly-brief jobs (Case A facts)

| Job | Baseline | Candidate-3 | Evidence |
| :-- | :-- | :-- | :-- |
| Q1 changed vs last week | PARTIAL (no owned section) | **PASS** — "Changed since last week" block names the one delta with source tag | section exists; grep-verifiable |
| Q2 top outcomes | PASS | PASS (unchanged content) | both list ≤2 outcomes up top |
| Q3 why now | PASS | PASS | retained |
| Q4 Monday intent | PARTIAL | **PASS** — day_emphasis column in priorities table; no sprint cells anywhere | zero S-tokens in candidate weekly: `grep -c 'S[123]:' candidate = 0` vs baseline-generation's removal being unenforced |
| Q5 capacity constrained | PASS* | PASS — capacity_class token STANDARD/REDUCED/CRITICAL at header | B-type check below |
| Q6 blocked/deferred | PASS | PASS — Parked + open_decisions with bite_day | equal or better precision |
| Q7 operator decision | PASS | PASS — Decisions open in header line | first-line reachable |
| Q8 confirmed vs assumed | PARTIAL | **PARTIAL→improving** — every claim tagged to ledger with freshness class; per-fact confirmed/assumed status still implicit in freshness | tags verifiable; full status column deferred |
| Q9 fact provenance | PARTIAL | **PASS for structure** — no untagged claims; single-hop ledger resolution by design | mechanical tag-presence check passes |
| Q10 wrong-layer | PARTIAL | **PASS** — schema has no sprint field; emphasis is directional tokens only | structurally enforced |

## Daily-brief jobs

| Job | Baseline | Candidate-3 | Evidence |
| :-- | :-- | :-- | :-- |
| Q11 day delta | PARTIAL (template lacks it; generation added it) | **PASS** — Changes-since-yesterday table is now the artifact's second element with per-row source tags | position + presence deterministic |
| Q12 order + why | PASS | PASS — Today table order + status reasons inline | comparable |
| Q13 compressed/blocked/omitted | PASS | PASS — unified enum FULL/COMPRESSED/MINIMAL/OMITTED/BLOCKED used; omissions carry reasons and tags | Case-B instantiation confirms |
| Q14 next action | PASS | PASS — header NEXT ACTION line, earlier than baseline's blockquote form | comparable-or-better |
| Q15 detail location | PASS | PASS — card links present | path check |

## Prompt jobs (F1-S2 exemplar)

| Job | Baseline prompt | Candidate prompt | Evidence |
| :-- | :-- | :-- | :-- |
| Q17 task-specific inputs | PASS | PASS — inputs: as required front-matter fields now | schema-enforced |
| Q18 concrete output | PASS | PASS — return: named block | enforced |
| Q19 done/stop | PASS | PASS — done:/stop: fields | enforced |
| Q20 S-difference | PASS (by discipline) | PASS (by schema — label-swap prompts fail missing-field validation) | structural |
| Q16 self-sufficiency | PASS | PASS — inputs+return+done present | unchanged |
| F09 routing noise | triple statement across card/index/prompt | **reduced** — routing-note declares single authoritative statement; others reference | count of route statements: 3→1 |

## Regression sweep

| Check | Result |
| :-- | :-- |
| D-type staleness week still expressible? | YES — case-D instantiation uses null+reason pattern (Investment UNPLANNED with source); no fabrication forced by schema |
| B-type constrained week visible? | YES — CRITICAL capacity class + OMITTED rows with reasons |
| Ownership coherence weekly↔daily | MAINTAINED — daily consumes weekly handoff; no restated weekly targets in daily flows |
| Source hops increased? | NO — ledger adds one resolution step at most (tag→ledger row), replacing scroll-to-appendix |
| Provenance intact | YES — strengthened (tags + freshness class) |
| Quiet-day noise risk | PRESENT but bounded — "no changes" state defined; needs live-week sampling to fully clear (not testable offline) → carried as open verification item |

## Verdict

CANDIDATE-3 advances per campaign advancement criteria:
- targeted failures improve (Q1,Q4,Q10,Q11 template-level; Q9 structurally),
- no material regression found in A/B/D sweeps,
- ownership coherent, provenance intact, hops not increased,
- improvements are visible in artifact outputs, not scores.

NOT claimed: any elapsed-time improvement (not_measured — no instrument);
not claimed against production templates yet (this validated a candidate
DESIGN, not a patch).

## Honest limitations

1. Same model family authored baselines and candidates — convergence between my
   own generations cannot be fully excluded; mitigated partially by reviewer
   divergence (R-C vs R-D mechanisms differ) and by deterministic checks.
2. E-type degraded-routing presentation was designed but only partially
   instantiated (prompt-index DEGRADED flag exists in baseline; candidate
   inherits mechanism via exception escalation rule).
3. Human/operator adjudication of consequential tradeoffs (§6 Phase-6 rules)
   has NOT occurred — final UX-value judgment belongs to the operator.
