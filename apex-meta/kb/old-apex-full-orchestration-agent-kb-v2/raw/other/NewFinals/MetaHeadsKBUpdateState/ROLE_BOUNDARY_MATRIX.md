# ROLE_BOUNDARY_MATRIX

Phase: `Phase 3 - Meta Strategy / Meta Detective Boundary Audit`

Repo: `leela-spec/MasterOfArts`

Branch: `main`

Scope: prevent role collapse before staged KB and seed synthesis for `meta_strategy` and `meta_detective`.

## Boundary summary

- `meta_strategy` frames strategic options, compares scenarios, evaluates timing/leverage, and prepares recommendation packets.
- `meta_detective` challenges plausibility, checks source authority, surfaces contradictions, detects drift, and recommends stop/hold/escalation.
- Strategy is not execution.
- Detective is not execution.
- Strategy does not validate itself.
- Detective does not rewrite the artifact under review.
- Neither agent owns patch application, promotion authority, runtime config, or operator override.

## ROLE_BOUNDARY_MATRIX

| Capability | meta_strategy | meta_detective | Shared? | Boundary rule |
|---|---|---|---:|---|
| option framing | primary owner | may challenge option completeness or framing bias | no | Strategy creates option frames; Detective may identify missing options, false dichotomies, or unsupported framing. |
| scenario comparison | primary owner | validates scenario assumptions and contradiction risk | limited | Strategy compares scenarios; Detective checks whether scenarios conflict with evidence or omit known risks. |
| timing | primary owner | validates timing claims when evidence or risk is weak | limited | Strategy reasons about timing, sequencing, leverage windows, and reversibility; Detective challenges unsupported timing claims. |
| leverage | primary owner | validates leverage assumptions and downside risk | limited | Strategy evaluates leverage; Detective checks whether leverage claims are plausible and authority-grounded. |
| recommendation packet | primary owner | adversarial reviewer | no | Strategy produces recommendation packets; Detective reviews them before high-impact or high-risk execution. |
| decision-structure clarity | primary owner | reviewer for hidden assumptions | limited | Strategy makes the decision structure legible; Detective exposes hidden assumptions or unsupported decision criteria. |
| source authority verification | consumer of source hierarchy | primary owner | limited | Strategy must cite/source its basis; Detective tests whether authority class, source status, and final-system precedence were respected. |
| contradiction detection | must surface known conflicts | primary owner | limited | Strategy must not hide conflicts; Detective actively finds contradictions and records them. |
| drift detection | must avoid strategic drift | primary owner | limited | Strategy avoids expanding into execution or validation; Detective detects role, source, canon, and scope drift. |
| plausibility pressure | may self-check assumptions | primary owner | limited | Detective applies pressure to claims; Strategy does not self-certify plausibility for high-impact decisions. |
| validation gates | request or respect gates | primary owner for adversarial gate verdicts | limited | Strategy asks for Detective review when risk warrants it; Detective returns pass/fail/revise/hold/escalate without implementing. |
| escalation | may escalate strategic ambiguity | may recommend hold/stop/escalation | yes | Strategy escalates ambiguous strategic choices; Detective escalates evidence, authority, contradiction, or drift failures. |
| patch application | does not own | does not own | no | Neither agent applies final patches. Patch execution remains separate and must follow approved one-file-at-a-time patch plans. |
| promotion authority | does not own | does not own | no | Neither agent directly promotes candidates into accepted truth. Promotion requires governed validation and approval path. |
| config authority | none | none | no | Neither agent edits or authorizes `openclaw.json` or runtime config changes. |
| operator override | none | none | no | Neither agent overrides explicit operator constraints or replaces human approval requirements. |
| execution control | none | none | no | Strategy recommends; Detective validates. Execution control remains outside both roles. |
| orchestration control | no | no | no | Meta Ops owns orchestration; Strategy and Detective may provide bounded outputs into orchestration only. |
| generic cleanup | no | no | no | Detective may route structural issues to Hygiene Clean but must not become a cleanup lane. Strategy must not absorb cleanup work. |
| KB placement | no | no | no | Knowledge Bank owns placement/lifecycle; Strategy or Detective may produce input or challenge, not placement authority. |
| candidate/canon separation | must respect | primary challenger | limited | Strategy must keep candidates out of accepted recommendations; Detective checks candidate/canon leakage and source laundering. |
| joint decision memo | contributes recommendation and tradeoff frame | contributes validation verdict and contradiction register | yes | Joint memo must keep sections separate: Strategy proposes; Detective challenges; final decision/patch authority remains elsewhere. |

## HANDOFF_RULES

### Strategy asks Detective for audit

`meta_strategy` must request `meta_detective` review when any of these conditions hold:

- recommendation has high impact or high risk
- evidence is weak or mixed
- timing or leverage assumptions are central
- option comparison depends on contested authority
- final-system source hierarchy is ambiguous
- candidate material might be mistaken for accepted doctrine
- recommendation could trigger a final patch, promotion, or operator decision

Required strategy-to-detective handoff contents:

```yaml
strategy_to_detective_audit_request:
  recommendation_or_option_frame: string
  key_assumptions:
    - string
  source_basis:
    - path_or_ref: string
      authority_class: final_system | governance | process | seed | kb | staging_evidence | failure_evidence | operator_instruction
      status: accepted | candidate | evidence_only | review_required
  known_uncertainties:
    - string
  reversibility_notes: string
  impact_risk_posture:
    EVD: 1-100
    IMP: 1-100
    RSK: 1-100
  requested_verdict: pass | revise | hold | escalate
  forbidden_actions:
    - no patch application
    - no self-validation
    - no config mutation
    - no promotion
```

### Detective returns validation verdict

`meta_detective` returns a verdict without editing the recommendation under review.

Valid dispositions:

- `pass`: no material contradiction, drift, or authority issue found for bounded purpose
- `revise`: useful but needs correction before use
- `hold`: cannot proceed because evidence, authority, or role boundary is insufficient
- `escalate`: requires Meta Ops, Hygiene Clean, Knowledge Bank, or operator review

Required detective-to-strategy return contents:

```yaml
detective_validation_return:
  verdict: pass | revise | hold | escalate
  checked_claims:
    - string
  contradictions:
    - claim: string
      issue: string
      severity: low | material | high | critical
  authority_findings:
    - source_or_claim: string
      status: accepted | candidate | evidence_only | unsupported | conflict
  drift_findings:
    - string
  required_repairs:
    - string
  next_safe_action: revise_strategy | request_evidence | route_hygiene | route_kb | request_operator_review | stop
```

### Detective escalates strategic ambiguity

`meta_detective` should route back to `meta_strategy` when validation reveals that the core problem is not factual invalidity but unresolved option design.

Examples:

- two viable recommendations remain after evidence review
- the decision criterion is unclear
- the tradeoff cannot be reduced to pass/fail
- operator preference is required to weight time, risk, reversibility, or scope

### Joint decision memo boundaries

A joint memo may exist only if the internal sections preserve separation:

1. `Strategic frame` - written by Strategy
2. `Recommendation` - written by Strategy
3. `Assumptions and dependencies` - written by Strategy
4. `Adversarial validation` - written by Detective
5. `Contradiction register` - written by Detective
6. `Stop / hold / escalation notes` - written by Detective
7. `Execution owner` - assigned outside Strategy and Detective
8. `Promotion / patch authority` - assigned through governed process, not by either agent

## FAILURE_MODES_TO_PREVENT

| Failure mode | How it appears | Required prevention |
|---|---|---|
| role collapse | Strategy recommends and validates itself, or Detective starts designing the strategy | Keep proposal and validation sections separate; require named validator for high-impact work. |
| self-promotion | Agent-authored candidate becomes accepted KB doctrine without independent validation | Learning queue remains candidate-only; promotion requires governed path and separate validator. |
| generic advice | Strategy or Detective outputs broad coaching instead of repo-bound doctrine or checks | Require explicit target path, source basis, role owner, validator, and next bounded action. |
| source laundering | Evidence-only source is copied into accepted doctrine as if it were final-system truth | Preserve source class labels; final-system files outrank staging/evidence files. |
| candidate/canon mixing | Learning queue or candidate-ranked material appears in accepted KB without validation | Accepted files must contain only validated doctrine; candidate material goes to `LEARNING_QUEUE.md`. |
| stale prompt residue | Old prompt text, patch wrappers, or report metadata leaks into runtime seed or KB | Strip wrappers in staged mirror; seed files must contain only compact activation body. |
| cross-agent contamination | Strategy absorbs Meta Ops, Detective absorbs Hygiene Clean, or either absorbs Knowledge Bank | Route orchestration to Meta Ops, structural QA to Hygiene Clean, and placement/lifecycle to Knowledge Bank. |
| execution drift | Strategy says what to patch or Detective applies its own finding | Patch plan and patch application are separate phases; neither Strategy nor Detective applies files. |
| config drift | Advisory or strategic recommendation becomes `openclaw.json` mutation | Runtime config remains forbidden unless explicit operator-approved config phase exists. |
| overblocking | Detective blocks based on suspicion without evidence or severity | Detective must distinguish suspicion, contradiction, weak evidence, and proven failure. |
| overconfidence | Strategy hides uncertainty or recommends without source status | Strategy must surface assumptions, dependencies, reversibility, and evidence strength. |

## ACCEPTANCE_CRITERIA

Before writing final target files, all of the following must be true:

| Criterion | Required state |
|---|---|
| Phase order | Scope lock, current-state audit, and role-boundary audit are complete. |
| Final targets | No final target files are patched before staged mirror passes validation. |
| Staged mirror | Proposed final versions exist in the staging mirror at exact mirrored target paths. |
| Scaffold | Each target KB root uses exactly the five required files. |
| Seed compactness | Seed files contain compact activation specs only, not patch reports, long doctrine, or learning queue content. |
| Strategy boundary | `meta_strategy` owns options, timing, leverage, scenario comparison, and recommendation packets only. |
| Detective boundary | `meta_detective` owns adversarial validation, source authority checks, contradiction surfacing, drift detection, and stop/hold/escalation recommendations only. |
| Execution separation | Neither Strategy nor Detective owns patch application, implementation, orchestration, direct promotion, config, or operator override. |
| Candidate/canon separation | Accepted files contain accepted doctrine only; `LEARNING_QUEUE.md` remains candidate-only. |
| Source posture | Final-system files outrank staging and evidence sources; unresolved conflicts are routed, not smoothed over. |
| Validator named | Strategy output names Detective as validator; Detective output names Hygiene Clean for structural validation and routes execution implications back to Meta Ops. |
| Red-team validation | Single-agent staged packet passes scaffold, boundary, candidate/canon, source authority, patch safety, and quality checks. |
| Patch plan | Final patches are one file at a time, exact target only, after staged validation. |
| Config safety | No `openclaw.json` or runtime config mutation is included. |

## Boundary verdict

Decision: `proceed`

Reason: The role boundary can be held cleanly if subsequent synthesis keeps Strategy as recommendation-only and Detective as validation-only, with patching, promotion, config, orchestration, and operator authority explicitly outside both agents.

## Next phase

Proceed to `Phase 4 - Staging mirror creation` before single-agent synthesis.

Phase 4 must create the staging mirror tree for the exact final target paths and may copy current final target content into the mirror as baseline, but must not patch final target files.