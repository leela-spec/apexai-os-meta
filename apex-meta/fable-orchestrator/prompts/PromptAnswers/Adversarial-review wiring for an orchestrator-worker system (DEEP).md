



## 1. Numbered wiring specification

**Decision-change result:** one isolated Claude “Detective” reviewing another Claude worker is **not sufficient independent validation for consequential outputs**. It provides context separation, but not model-family independence. Claude Code subagents receive isolated contexts and scoped tools, yet they remain Claude instances; isolation removes conversational contamination, not shared training priors, stylistic preferences, or correlated blind spots. citeturn220224search0turn220224search3turn220224search15

The failure path is concrete:

1. The worker selects evidence, frames assumptions, and writes an internally coherent packet.
2. A same-family reviewer recognizes familiar style and reasoning patterns.
3. The reviewer checks completeness and internal consistency more readily than it reconstructs the claim from primary evidence.
4. Unavailable evidence is treated as “no contradiction found.”
5. The packet receives a plausible PASS despite a shared omission.

Research has found self- and family-preference in judges, including models assigning higher scores to their own and same-family outputs. Familiar, lower-perplexity text can be preferred even when it was not literally self-generated. citeturn947815search0turn947815search18 Your own project after-action evidence also shows same-context subagents re-deriving conclusions already reached while adding substantial cost, rather than supplying genuinely independent information. fileciteturn0file0

### 1. Freeze the review subject

**Input:** consequential worker artifact and worker claim packet.

**Reads:**

```text
runs/<run_id>/work/worker-artifact.vNNN.<ext>
runs/<run_id>/work/worker-claim-packet.vNNN.yaml
```

**Writes:**

```text
runs/<run_id>/review/artifact-lock.vNNN.yaml
```

The lock records:

- SHA-256 of the exact artifact;
- source-packet hashes;
- version;
- declared scope;
- worker identity and model family, stored for audit but withheld from reviewers;
- changed-claim IDs;
- review-trigger reason.

No review begins against a mutable path. All verdicts bind to the artifact hash, not merely its filename.

---

### 2. Construct two blind, lens-specific packets

**Input:** artifact lock, source inventory, macro-goal records and review policy.

**Reads:**

```text
runs/<run_id>/review/artifact-lock.vNNN.yaml
runs/<run_id>/work/worker-claim-packet.vNNN.yaml
governance/review-policy.yaml
governance/validity-criteria.yaml
governance/alignment-criteria.yaml
governance/macro-goal.yaml
governance/decision-log.yaml
```

**Writes:**

```text
runs/<run_id>/review/validity-input.vNNN.yaml
runs/<run_id>/review/alignment-input.vNNN.yaml
```

Both packets omit:

- worker model and agent name;
- worker confidence;
- proposed verdict;
- persuasive rationale;
- descriptions of how hard the work was;
- prior reviewer conclusions;
- any “please confirm” or approval-oriented language.

The artifact itself, source locations, explicit assumptions, uncertainties and stop conditions remain available.

**Why:** withholding the author’s reasoning reduces anchoring and prevents the reviewer from merely checking whether the reasoning sounds coherent. It forces review of the artifact and evidence rather than the author’s correction or success claim.

---

### 3. Run deterministic packet preflight

**Input:** both review-input packets.

**Reads:**

```text
runs/<run_id>/review/validity-input.vNNN.yaml
runs/<run_id>/review/alignment-input.vNNN.yaml
```

**Writes:**

```text
runs/<run_id>/review/preflight.vNNN.yaml
```

The script verifies:

- YAML/schema validity;
- artifact hash;
- existence and readability of every mandatory source;
- uniqueness of criterion IDs;
- criterion-to-owner mapping;
- no forbidden fields in blind packets;
- validity packet contains no strategic verdict;
- alignment packet contains no validity verdict;
- every critical criterion declares an evidence requirement;
- source snapshots have hashes or immutable identifiers.

A failed preflight yields `hold`; neither reviewer is invoked.

---

### 4. Run the independent validity review

**Input:** validity packet and read-only access to the exact artifact and declared sources.

**Reviewer:** preferably a **different model family**, exposed to the Claude Code orchestrator through an MCP/API tool. A normal Claude subagent is not a different-family judge.

**Tool allowlist:**

```text
Read
Grep
Glob
approved source-retrieval tool
approved citation-verifier
```

No `Write`, `Edit`, mutation-capable `Bash`, git commit or patch tool.

**Reads:**

```text
runs/<run_id>/review/validity-input.vNNN.yaml
runs/<run_id>/work/worker-artifact.vNNN.<ext>
<declared evidence files>
```

**Writes:**

```text
runs/<run_id>/review/validity-verdict.vNNN.yaml
```

For every criterion, the reviewer must first construct the strongest plausible case that the artifact is wrong, then test that case against retrieved evidence. This is not a free-form “be critical” instruction. The output must record:

- falsification hypothesis;
- evidence searched;
- evidence found;
- counterevidence;
- criterion verdict;
- defect owner;
- unresolved uncertainty.

Checklist decomposition is empirically preferable to one holistic score: CheckEval’s decomposed binary questions improved agreement across 12 evaluator models and multiple datasets, while related hierarchical-criteria work reports better evaluator alignment across domains. These are benchmark findings, not proof of production reliability, but they support criterion-level review over a single PASS/FAIL impression. citeturn947815search2turn947815search11

---

### 5. Run strategic-alignment review independently and in parallel

**Input:** alignment packet, artifact, macro goal and binding decisions.

**Reviewer:** a separate fresh Claude subagent is acceptable here because this lens does not claim epistemic independence from Claude-generated factual reasoning. It checks whether the artifact still serves the operator’s intent.

**Reads:**

```text
runs/<run_id>/review/alignment-input.vNNN.yaml
runs/<run_id>/work/worker-artifact.vNNN.<ext>
governance/macro-goal.yaml
governance/decision-log.yaml
```

**Writes:**

```text
runs/<run_id>/review/alignment-verdict.vNNN.yaml
```

It may not see:

```text
validity-verdict.vNNN.yaml
worker rationale
worker confidence
```

The two lenses are therefore **two agents, run blind and in parallel**, not two sequential passes by one agent.

**Why:** one agent performing validity and alignment sequentially is likely to rationalize validity defects because the artifact is strategically attractive, or reject a valid artifact because it dislikes the strategic choice. Parallel isolation prevents the first verdict from becoming an anchor. Claude Code supports isolated parallel agents, but parallel agents multiply token usage; the wall-clock duration is approximately the slower call rather than the sum when the calls truly run concurrently. citeturn220224search2turn220224search5

---

### 6. Aggregate deterministically; do not ask an LLM to “resolve” the verdicts

**Input:** preflight, validity verdict and alignment verdict.

**Reads:**

```text
runs/<run_id>/review/preflight.vNNN.yaml
runs/<run_id>/review/validity-verdict.vNNN.yaml
runs/<run_id>/review/alignment-verdict.vNNN.yaml
governance/review-policy.yaml
```

**Writes:**

```text
runs/<run_id>/review/review-decision.vNNN.yaml
```

The deterministic precedence is:

```text
escalate
needs_input
hold
revise
pass
```

Promotion requires:

```text
preflight = pass
validity = pass
alignment = pass
all critical criteria = pass
all PASS criteria contain evidence references
all PASS criteria contain a completed falsification attempt
no unresolved critical uncertainty
artifact hashes match
```

A single critical non-pass blocks promotion. There is no majority override and no “two positive reviews defeat one dissenting review.”

This matters because majority voting assumes sufficiently independent errors. Controlled debate studies find that majority pressure can suppress a correct minority, while recent multi-judge work finds highly correlated errors and much less effective independence than the raw judge count suggests. citeturn947815search7turn947815search10turn947815search28

---

### 7. Route defects to named owners

**Input:** aggregated decision and criterion defects.

**Reads:**

```text
runs/<run_id>/review/review-decision.vNNN.yaml
runs/<run_id>/review/validity-verdict.vNNN.yaml
runs/<run_id>/review/alignment-verdict.vNNN.yaml
```

**Writes:**

```text
runs/<run_id>/review/revision-order.vNNN.yaml
```

Each defect names exactly one primary owner:

```text
worker
orchestrator
source_owner
strategy_owner
operator
review_configuration
```

The order specifies:

- defect ID;
- responsible owner;
- affected artifact location;
- failed criterion;
- evidence supporting the defect;
- required outcome;
- prohibited adjacent changes;
- whether the artifact must be fully re-reviewed.

Neither reviewer may fix the artifact. This preserves reviewer independence and prevents the reviewer from later validating its own replacement text.

---

### 8. Correct by creating a new immutable artifact version

**Input:** revision order and prior artifact.

**Reads:**

```text
runs/<run_id>/review/revision-order.vNNN.yaml
runs/<run_id>/work/worker-artifact.vNNN.<ext>
```

**Writes:**

```text
runs/<run_id>/work/worker-artifact.vNNN+1.<ext>
runs/<run_id>/work/worker-claim-packet.vNNN+1.yaml
runs/<run_id>/review/artifact-lock.vNNN+1.yaml
```

The worker reports changed claim IDs and source changes, but “we fixed issue X” is not review evidence.

The old artifact and verdicts remain immutable.

---

### 9. Re-review the corrected artifact, not the correction claim

**Input:** new artifact lock and prior defect IDs.

**Reads:**

```text
runs/<run_id>/review/artifact-lock.vNNN+1.yaml
runs/<run_id>/work/worker-artifact.vNNN+1.<ext>
runs/<run_id>/review/revision-order.vNNN.yaml
```

**Writes:**

```text
runs/<run_id>/review/validity-verdict.vNNN+1.yaml
runs/<run_id>/review/alignment-verdict.vNNN+1.yaml
runs/<run_id>/review/review-decision.vNNN+1.yaml
```

Use fresh reviewer contexts. Supply prior defect IDs and failed criteria, but not the worker’s explanation of why the correction should now pass.

A narrow change may permit criterion-scoped re-review only when a deterministic diff proves that no other reviewed content changed. Any change to evidence, central claims, conclusions, safety assumptions or macro direction triggers complete review by the affected lens.

---

### 10. Promote only through a deterministic gate and append the audit record

**Input:** final review decision.

**Reads:**

```text
runs/<run_id>/review/review-decision.vNNN.yaml
runs/<run_id>/review/validity-verdict.vNNN.yaml
runs/<run_id>/review/alignment-verdict.vNNN.yaml
```

**Writes:**

```text
runs/<run_id>/promotion/promotion-gate.vNNN.yaml
runs/<run_id>/review/review-history.jsonl
```

The gate records:

- artifact hash;
- reviewer model families;
- lens separation;
- criterion verdicts;
- evidence-free-PASS gate result;
- unresolved uncertainties;
- number of revision cycles;
- operator escalation, where applicable.

A reviewer timeout, malformed output, incomplete source retrieval or token-budget truncation becomes `hold`, never implicit PASS.

---

## 2. YAML schemas

### Reviewer input-packet schema

```yaml
review_input_packet:
  schema_version: "apex.independent_review.input.v1"

  required_fields:
    - run_id
    - review_id
    - review_lens
    - artifact
    - independence
    - criteria
    - sources
    - assumptions
    - uncertainties
    - changed_claims
    - stop_conditions
    - evidence_free_pass_gate
    - forbidden_context

  run_id:
    type: string

  review_id:
    type: string

  review_lens:
    type: string
    allowed:
      - validity
      - strategic_alignment

  artifact:
    type: object
    required:
      - path
      - version
      - sha256
      - artifact_type
      - declared_scope
    properties:
      path:
        type: string
      version:
        type: integer
        min: 1
      sha256:
        type: string
        pattern: "^[a-f0-9]{64}$"
      artifact_type:
        type: string
      declared_scope:
        type: array
        items:
          type: string

  independence:
    type: object
    required:
      - author_model_family_withheld
      - author_identity_withheld
      - author_reasoning_withheld
      - prior_verdicts_withheld
      - reviewer_context_is_fresh
      - reviewer_model_family
    properties:
      author_model_family_withheld:
        type: boolean
        required_value: true
      author_identity_withheld:
        type: boolean
        required_value: true
      author_reasoning_withheld:
        type: boolean
        required_value: true
      prior_verdicts_withheld:
        type: boolean
        required_value: true
      reviewer_context_is_fresh:
        type: boolean
        required_value: true
      reviewer_model_family:
        type: string
      author_model_family_for_aggregator_only:
        type:
          - string
          - "null"

  criteria:
    type: array
    min_items: 1
    items:
      type: object
      required:
        - criterion_id
        - question
        - severity
        - evidence_requirement
        - owner_on_failure
        - pass_condition
      properties:
        criterion_id:
          type: string
        question:
          type: string
        severity:
          type: string
          allowed:
            - critical
            - major
            - minor
        evidence_requirement:
          type: string
        owner_on_failure:
          type: string
          allowed:
            - worker
            - orchestrator
            - source_owner
            - strategy_owner
            - operator
            - review_configuration
        pass_condition:
          type: string

  sources:
    type: array
    items:
      type: object
      required:
        - source_id
        - path_or_locator
        - source_type
        - required
        - integrity
      properties:
        source_id:
          type: string
        path_or_locator:
          type: string
        source_type:
          type: string
          allowed:
            - primary
            - secondary
            - project_record
            - deterministic_output
            - governing_decision
        required:
          type: boolean
        integrity:
          type: object
          required:
            - verification_method
          properties:
            sha256:
              type:
                - string
                - "null"
            immutable_revision:
              type:
                - string
                - "null"
            verification_method:
              type: string

  assumptions:
    type: array
    items:
      type: object
      required:
        - assumption_id
        - statement
        - materiality
      properties:
        assumption_id:
          type: string
        statement:
          type: string
        materiality:
          type: string
          allowed:
            - critical
            - material
            - non_material

  uncertainties:
    type: array
    items:
      type: object
      required:
        - uncertainty_id
        - statement
        - blocks_pass
      properties:
        uncertainty_id:
          type: string
        statement:
          type: string
        blocks_pass:
          type: boolean

  changed_claims:
    type: array
    items:
      type: object
      required:
        - claim_id
        - artifact_location
        - statement
      properties:
        claim_id:
          type: string
        artifact_location:
          type: string
        statement:
          type: string

  strategic_context:
    type: object
    required_when:
      review_lens: strategic_alignment
    forbidden_when:
      review_lens: validity
    properties:
      macro_goal_path:
        type: string
      decision_log_path:
        type: string
      explicit_non_goals:
        type: array
        items:
          type: string

  stop_conditions:
    type: array
    min_items: 1
    items:
      type: string

  evidence_free_pass_gate:
    type: object
    purpose: >
      Prevent a reviewer from issuing PASS merely because no obvious defect
      was noticed.
    required:
      - pass_requires_evidence_refs_per_criterion
      - pass_requires_falsification_attempt_per_criterion
      - pass_forbidden_when_required_source_unavailable
      - pass_forbidden_when_critical_uncertainty_unresolved
      - pass_forbidden_when_artifact_hash_mismatch
      - abstain_instead_of_guess
    properties:
      pass_requires_evidence_refs_per_criterion:
        type: boolean
        required_value: true
      pass_requires_falsification_attempt_per_criterion:
        type: boolean
        required_value: true
      pass_forbidden_when_required_source_unavailable:
        type: boolean
        required_value: true
      pass_forbidden_when_critical_uncertainty_unresolved:
        type: boolean
        required_value: true
      pass_forbidden_when_artifact_hash_mismatch:
        type: boolean
        required_value: true
      abstain_instead_of_guess:
        type: boolean
        required_value: true

  forbidden_context:
    type: array
    required_values:
      - worker_model_identity
      - worker_confidence
      - worker_success_claim
      - worker_persuasive_rationale
      - other_lens_verdict
      - prior_overall_verdict
```

### Verdict-output schema

```yaml
review_verdict:
  schema_version: "apex.independent_review.verdict.v1"

  required_fields:
    - verdict_id
    - run_id
    - review_id
    - artifact
    - review_lens
    - reviewer
    - overall_verdict
    - criterion_verdicts
    - unresolved_uncertainties
    - evidence_free_pass_gate
    - prohibited_actions_confirmation

  verdict_id:
    type: string

  run_id:
    type: string

  review_id:
    type: string

  artifact:
    type: object
    required:
      - path
      - version
      - expected_sha256
      - observed_sha256
      - hash_verified
    properties:
      path:
        type: string
      version:
        type: integer
      expected_sha256:
        type: string
      observed_sha256:
        type: string
      hash_verified:
        type: boolean

  review_lens:
    type: string
    allowed:
      - validity
      - strategic_alignment

  reviewer:
    type: object
    required:
      - model_family
      - model_identifier
      - context_was_fresh
      - tools_used
    properties:
      model_family:
        type: string
      model_identifier:
        type: string
      context_was_fresh:
        type: boolean
      tools_used:
        type: array
        items:
          type: string

  overall_verdict:
    type: string
    allowed:
      - pass
      - revise
      - hold
      - needs_input
      - escalate

  verdict_semantics:
    pass: "All applicable criteria pass and every PASS gate is satisfied."
    revise: "The artifact has correctable defects assigned to named owners."
    hold: "Review cannot safely complete because a gate or required check failed."
    needs_input: "Specific missing evidence or operator information is required."
    escalate: "The issue exceeds reviewer authority or presents unresolved critical risk."

  criterion_verdicts:
    type: array
    min_items: 1
    items:
      type: object
      required:
        - criterion_id
        - verdict
        - falsification_attempt
        - evidence_refs
        - reasoning_summary
        - confidence_band
      properties:
        criterion_id:
          type: string

        verdict:
          type: string
          allowed:
            - pass
            - revise
            - hold
            - needs_input
            - escalate
            - not_applicable

        falsification_attempt:
          type: object
          required:
            - strongest_wrong_case
            - evidence_sought
            - search_completed
            - result
          properties:
            strongest_wrong_case:
              type: string
            evidence_sought:
              type: array
              min_items: 1
              items:
                type: string
            search_completed:
              type: boolean
            result:
              type: string
              allowed:
                - falsified_artifact
                - did_not_falsify_artifact
                - inconclusive

        evidence_refs:
          type: array
          items:
            type: object
            required:
              - source_id
              - locator
              - supports
            properties:
              source_id:
                type: string
              locator:
                type: string
              supports:
                type: string

        counterevidence_refs:
          type: array
          items:
            type: object
            required:
              - source_id
              - locator
              - implication
            properties:
              source_id:
                type: string
              locator:
                type: string
              implication:
                type: string

        reasoning_summary:
          type: string

        confidence_band:
          type: string
          allowed:
            - low
            - medium
            - high

        defect:
          type:
            - object
            - "null"
          required_when:
            verdict:
              - revise
              - hold
              - needs_input
              - escalate
          properties:
            defect_id:
              type: string
            severity:
              type: string
              allowed:
                - critical
                - major
                - minor
            owner:
              type: string
              allowed:
                - worker
                - orchestrator
                - source_owner
                - strategy_owner
                - operator
                - review_configuration
            artifact_location:
              type: string
            defective_claim:
              type: string
            required_outcome:
              type: string
            prohibited_adjacent_changes:
              type: array
              items:
                type: string

  unresolved_uncertainties:
    type: array
    items:
      type: object
      required:
        - uncertainty_id
        - statement
        - materiality
        - blocks_pass
      properties:
        uncertainty_id:
          type: string
        statement:
          type: string
        materiality:
          type: string
          allowed:
            - critical
            - material
            - non_material
        blocks_pass:
          type: boolean

  evidence_free_pass_gate:
    type: object
    required:
      - artifact_hash_verified
      - required_sources_retrieved
      - every_pass_has_evidence
      - every_pass_has_falsification_attempt
      - no_unresolved_critical_uncertainty
      - no_incomplete_critical_criterion
      - pass_authorized
      - gate_failure_reasons
    properties:
      artifact_hash_verified:
        type: boolean
      required_sources_retrieved:
        type: boolean
      every_pass_has_evidence:
        type: boolean
      every_pass_has_falsification_attempt:
        type: boolean
      no_unresolved_critical_uncertainty:
        type: boolean
      no_incomplete_critical_criterion:
        type: boolean
      pass_authorized:
        type: boolean
        rule: >
          May be true only when all preceding gate fields are true and the
          overall_verdict is pass.
      gate_failure_reasons:
        type: array
        items:
          type: string

  escalation:
    type:
      - object
      - "null"
    properties:
      target:
        type: string
        allowed:
          - operator
          - strategy_owner
          - domain_expert
          - source_owner
          - review_system_owner
      question:
        type: string
      evidence_needed:
        type: array
        items:
          type: string

  prohibited_actions_confirmation:
    type: object
    required:
      - reviewer_did_not_modify_artifact
      - reviewer_did_not_write_correction
      - reviewer_did_not_consult_other_lens_verdict
    properties:
      reviewer_did_not_modify_artifact:
        type: boolean
        required_value: true
      reviewer_did_not_write_correction:
        type: boolean
        required_value: true
      reviewer_did_not_consult_other_lens_verdict:
        type: boolean
        required_value: true
```

---

## 3. Failure-mode table

| Failure mode | Why it happens in same-family LLM review | Specific mechanism in the wiring that mitigates it | Residual risk that remains | Citation |
|---|---|---|---|---|
| **Sycophancy / approval seeking** | Reviewer instructions, worker confidence and polished rationale implicitly frame agreement as the cooperative response. In SycEval, the three tested frontier models showed sycophantic behavior in 58.19% of benchmark interactions; persistence after the first sycophantic response was reported at 78.5%. These are controlled math/medical benchmark results, not a direct production-review failure rate. | Hide worker confidence and success claims; require falsification before evaluation; make missing evidence produce `hold`, not PASS; require criterion-level evidence; deterministic gate rejects unsupported PASS. | A reviewer can manufacture a superficial falsification attempt and then agree anyway. Periodic human-labelled calibration sets are still required. | citeturn958739view5 |
| **Self-preference and family-preference** | Models prefer familiar generation styles and policies. One study reported a self-preference bias score of 0.749 for GPT-4 under its metric and found preference for lower-perplexity, familiar text even when it was not self-generated. A later study found both GPT-4o and Claude 3.5 Sonnet could favor their own and same-family outputs. | Different-family model for validity; redact author/model identity; withhold author reasoning; use fixed criterion structure rather than “which answer feels better?”; judge evidence support rather than prose quality. | Cross-family models share internet corpora, instruction-tuning conventions and evaluator datasets. Different family reduces, but does not eliminate, familiarity bias. | citeturn947815search0turn947815search18turn947815search21 |
| **Correlated blind spot** | Same-family author and judge can omit the same premise, misread the same source or share the same learned misconception. More judges do not imply proportionally more independent evidence when their errors are correlated. Recent work explicitly describes “confabulation consensus,” where repeated faulty reasoning becomes a misleading vote count. | Cross-family validity judge; source-grounded reconstruction; deterministic source-integrity preflight; critical-defect veto; unresolved uncertainty escalates instead of being voted away. | Both families may share the same training-data error or all available sources may repeat the same false claim. High-impact claims still require authoritative or human-domain review. | citeturn947815search10turn947815search28 |
| **Evidence-free rubber stamp under time/token pressure** | Holistic review encourages the model to inspect visible structure, completeness and plausibility first. In code-validation experiments, LLM validators accepted valid outputs at roughly 96% true-positive rate but rejected invalid outputs at under 25% true-negative rate, demonstrating severe positive/agreeableness bias in that setting. | Explicit `evidence_free_pass_gate`; one verdict per criterion; every PASS requires evidence and a falsification attempt; timeout or truncation becomes `hold`; reviewers cannot omit critical criteria. | Evidence citations may be irrelevant or only indirectly supportive. Citation entailment needs deterministic checks where possible and sampled human audits. | citeturn346517view2turn346517view3 |
| **Position and presentation bias** | Pairwise judges may favor whichever item appears first or second, and can confuse length or polish with quality. A study covering 12 judges, 22 tasks and more than 100,000 evaluations found systematic position-bias variation by judge and task, strongly affected by the quality gap. Another study observed decision reversals after answer-order swaps at approximately 25% for GPT-4, 58% for GPT-3.5 and 89% for Llama in its tested settings. | Use pointwise criterion review, not worker-output-versus-alternative pairwise selection; fixed packet ordering; separate evidence from artifact prose; no score bonus for verbosity; source locators required. | Section order and salience can still influence attention inside one artifact. Periodic order perturbation tests should be part of evaluator calibration. | citeturn947815search6turn958739view2 |
| **Strategic desirability contaminates factual validity** | A strategically attractive artifact makes the reviewer more inclined to rationalize unsupported claims; a technically valid artifact can likewise be rejected because the reviewer dislikes the chosen direction. | Separate validity and alignment into blind parallel agents. Validity receives no macro-goal advocacy; alignment receives no validity verdict. Both must pass. | Some criteria genuinely span both lenses, such as whether evidence is sufficient for a strategic risk. Such criteria need an explicit primary owner and may require operator escalation. | This separation is a design inference supported by the documented effects of anchoring, role diversity and correlated judgement, not a directly measured benchmark result. citeturn947815search5turn947815search7 |
| **Sequential conformity and debate drift** | Once a reviewer sees another verdict, it may defend or converge on that position rather than independently reassess. Controlled debate research found majority pressure can suppress independent correction. Broader evaluations have also found multi-agent debate frequently fails to outperform simpler chain-of-thought or self-consistency despite greater compute. | Independent parallel first pass; no cross-lens verdict visibility; deterministic aggregation; no free-form debate by default; disagreement results in `hold` or escalation. | Parallel reviewers can independently reach the same wrong conclusion. The design prevents social convergence but not shared factual error. | citeturn947815search7turn445831view0 |
| **Adversarial-review theater** | Merely naming an agent “Detective” or telling it to be skeptical does not change its incentives. A generic critic can produce rhetorical objections and then approve without testing any claim. | Criterion contract, mandatory strongest-wrong-case field, mandatory evidence search record, hard PASS gate and prohibited implementation actions. | The falsification text can become boilerplate. Detect this through minimum evidence diversity, duplicate-text checks and human review of sampled verdicts. | Devil’s-advocate prompting has improved two NLG meta-evaluation benchmarks, but the successful design used a strong explicit critic role and structured interaction; it does not prove that generic adversarial language is sufficient for arbitrary production artifacts. citeturn947815search5turn947815search8 |
| **False confidence / poor calibration** | A fluent judge can produce stable confidence language even when its criterion classification is systematically biased. High aggregate F1 can also hide asymmetric false-pass and false-fail rates. | Use categorical confidence bands only as metadata; never allow confidence to override verdict gates; record abstentions and `needs_input`; maintain a human-labelled calibration set and report per-label confusion matrices. | Calibration drifts by domain, prompt version and model version. It must be measured continuously rather than assumed from a benchmark. | Recent judge-methodology work emphasizes that scalar agreement can conceal label-specific failure and that judge assessment should include confusion, abstention and coverage, not one correlation score. citeturn740649academia46 |
| **Reviewer repairs its own finding** | Once the reviewer authors the correction, its next review becomes self-evaluation and inherits self-preference plus commitment bias. | Read-only tools; output schema explicitly confirms no artifact modification; defects return to named owner; fresh reviewer checks a newly hashed artifact. | The worker may copy reviewer wording verbatim, leaving the corrected artifact stylistically similar to the reviewer. Different-family re-review and evidence reconstruction still reduce this risk. | Self- and family-preference evidence applies directly to this ownership conflict. citeturn947815search0turn947815search18 |

The literature does not support a blanket statement that multi-agent review always fails. ReConcile reported gains of up to 11.4% across seven reasoning benchmarks, and diverse panels have sometimes outperformed one large judge while costing less. Conversely, controlled studies find that debate often adds compute without beating simpler baselines, and that diversity and underlying model competence matter more than debate order or confidence displays. The defensible synthesis is therefore: **heterogeneous independent evidence can help; additional same-family conversation is not itself evidence.** citeturn888825search0turn346517view0turn445831view0turn947815search7

---

## 4. Model recommendation

### Recommendation: different-model-family validity judge, not same-model role-play or majority vote

Use this configuration:

```yaml
review_model_policy:
  validity_review:
    model_requirement: "different family from the authoring model"
    execution: "independent, blind, read-only"
    authority: "critical-defect veto"

  strategic_alignment_review:
    model_requirement: "fresh isolated Claude subagent is acceptable"
    execution: "parallel with validity review"
    authority: "alignment veto"

  aggregation:
    mechanism: "deterministic rule engine"
    majority_vote: false
    debate_by_default: false
    disagreement_result: "hold_or_escalate"

  highest_risk_outputs:
    additional_gate: "human or qualified domain-expert review"
```

### Why not same model, different role?

A fresh Claude subagent gives you:

- context isolation;
- reduced contamination from the worker conversation;
- separate instructions;
- scoped tools.

It does **not** give you an independently trained evaluator. Claude’s documentation describes subagents as separate, fresh-context Claude instances; this is a context-management mechanism, not a claim of epistemic independence. citeturn220224search0turn220224search3turn220224search15

For low-consequence screening, same-family review is useful. For the system’s claimed **independent validity gate**, it is not enough.

### Why not majority vote across N?

Majority vote is attractive only when errors are sufficiently independent. That assumption is weak for LLM panels sharing training corpora, post-training methods and benchmark conventions.

The evidence is mixed:

- Diverse-panel research has found cases where panels beat a single large judge and reduced intramodel bias. citeturn346517view0turn346517view1
- More recent analyses find that nominally large panels may behave like only a few effective independent voters, that the best single judge can equal or beat the panel on some tasks, and that alternative aggregation only partly repairs correlated errors. citeturn445831view2
- Controlled debate work finds group diversity and base reasoning strength dominate structural debate choices, while majority pressure can suppress correction. citeturn947815search7

Therefore, buying three or five votes is less defensible than buying **one genuinely different evidentiary perspective** and giving critical dissent blocking authority.

### Accepted token and latency cost

Relative to the current one-Detective sketch:

| Dimension | Current sketch | Recommended wiring |
|---|---:|---:|
| Review model calls per consequential artifact | 1 | 2 |
| Model families represented | 1 | 2 for validity-sensitive work |
| Default debate rounds | 0 or unspecified | 0 |
| Aggregator call | Often another LLM | None; deterministic |
| Re-review | Unspecified | Only after a new artifact version |
| Wall-clock path | One call | Approximately the slower of two parallel calls plus deterministic merge |
| Token consumption | One packet | Sum of two narrower lens packets |

Claude Code documentation explicitly warns that concurrent agents multiply token usage, even where parallelism reduces elapsed time. citeturn220224search2turn220224search5

The accepted cost is therefore:

- **one additional review call per consequential artifact;**
- an external-model integration surface for the validity judge;
- separate compact validity and alignment packets;
- re-review only after real artifact changes;
- no open-ended debate and no N-agent voting panel.

Because native Claude Code subagents remain Claude sessions, a genuinely different-family validity judge must be exposed as an external tool or service—for example through MCP or a narrow API wrapper—then invoked by the orchestrator with a read-only packet. Claude’s platform supports MCP connections to external tools and services, but the external judge wrapper and its credentials become part of the trusted computing boundary. citeturn220224search1turn220224search8

**Final decision:** retain a Claude Detective only as the **strategic-alignment reviewer or low-risk screening reviewer**. For consequential independent validity review, wire a blind, different-family judge with criterion-level falsification, evidence-bearing PASS requirements and deterministic veto aggregation. Without those changes, the single-Detective design is too close to adversarial-review theater.