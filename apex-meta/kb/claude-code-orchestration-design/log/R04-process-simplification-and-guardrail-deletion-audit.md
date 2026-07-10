# R04 — Apex KB Process Simplification and Guardrail Deletion Audit

```yaml
report_id: R04
repository: leela-spec/apexai-os-meta
branch: main
mode: adversarial_process_audit
created_at: 2026-07-10
scope:
  primary_files_read: 9
  additional_files_read: 0
repository_change:
  report_only: true
  runtime_or_contract_files_modified: false
```

## 1. Verdict

```yaml
verdict: simplify_now
primary_finding: >
  Apex KB has enough rules to describe a safe lifecycle, but too many documents
  claim lifecycle authority and too few transitions are enforced by executable
  evidence. The process repeatedly substitutes file existence, headings,
  read-back, state names, and future-validation promises for useful knowledge
  and proven completion.
core_recommendation: >
  Reduce the active process to seven target-facing stages, three capability
  functions, six evidence-derived states, one deterministic postflight packet,
  one semantic acceptance decision, and one candidate-driven repair loop.
current_active_process_surfaces: 7
recommended_active_process_surfaces: 4
current_named_lifecycle_states: 11
recommended_runtime_states: 6
current_macro_flow_labels: 4
recommended_macro_flow_labels: 0
```

The process should be simplified immediately. The observed failure was not caused by missing prose. It occurred because existing prose did not govern execution: the quality command was not run, structural checks were treated as quality proof, connector read-back replaced terminal validation, and a completion label overstated what had been proven.

The correct deletion rule is:

```yaml
deletion_rule:
  keep_only_when:
    - prevents a named observed failure
    - is executable or directly controls an executable transition
    - is not already authoritative elsewhere
  otherwise: delete_merge_or_move_to_example
```

## 2. Evidence Summary by File

| File | Authority observed | Decisive evidence | Audit judgment |
|---|---|---|---|
| `log/max-run-20260709-phase2-quality-failure-root-cause.md` | Historical failure evidence | Quality was not run; heading-complete thin pages escaped; connector read-back replaced validation; artifact count became the completion proxy. | Keep as historical evidence. Do not convert every listed remedy into permanent process law. |
| `log/max-run-20260709-execution-audit.md` | Historical execution evidence | Empty payload manifest, no deterministic postflight, 37 commits, unrelated diff-window file, thin pages, overstated completion. | Keep as historical evidence. Use its concrete failures to justify only minimal controls. |
| `.claude/skills/apex-kb/SKILL.md` | Intended top-level authority | Defines scope, roles, lifecycle, output tiers, boundaries, and completion language. Also repeats lower-level command and lifecycle rules. | Keep as the single operator-facing lifecycle authority after consolidation. |
| `references/lifecycle-state-machine.md` | Competing lifecycle authority | Defines 11 states plus four macro states. Most states restate file existence or command sequence rather than evidence-backed readiness. | Deprecate as active authority; merge only truthful completion states into `SKILL.md`. |
| `references/script-command-contract.md` | Intended executable contract | Defines command surface and write policy, but can overclaim behavior when documentation leads implementation. | Keep, but restrict it to actual CLI behavior and machine-readable result semantics. |
| `references/ingest-query-lint-audit-rules.md` | Competing semantic/process authority | Repeats source grounding, phase boundaries, Phase 1/2 flow, query behavior, lint rules, and gate policy. Contradicts other files on the Phase 1→2 gate. | Merge unique semantic rules into `SKILL.md`; remove duplicated lifecycle authority. |
| `references/acceptance-tests.md` | Executable evidence specification | Contains runnable smoke tests, but current fixtures prove structure more readily than semantic usefulness and can preserve obsolete gates. | Keep as the sole behavioral proof surface; add only tests tied to observed failures. |
| `examples/lifecycle-runbook.md` | Operator example presented close to authority | Repeats output tiers and execution sequence. Examples can become stale and be mistaken for requirements. | Keep only as a non-authoritative example generated from current commands. |
| `package-manifest.md` | Package inventory | Lists package surfaces, including multiple documents that appear equally authoritative. | Keep as inventory only; add explicit authority classes and deprecation markers. |

## 3. Current Process Elements

### Roles and capability functions

The inspected files imply more roles than are needed:

```yaml
current_role_surfaces:
  - operator
  - LLM semantic compiler
  - Python deterministic executor
  - retrieval executor
  - GitHub connector writer
  - terminal validator
  - query synthesizer
  - maintenance actor
  - implied independent reviewer
```

Most are environments or command modes, not durable roles. Treating them as separate roles creates handovers and lets one actor defer essential work to another unnamed executor.

### States

The state machine defines eleven sequential states from source access through maintenance. Several states are not real states:

- `S1_scaffold_ready`, `S2_source_intake_ready`, and `S2b_source_payload_manifest_ready` are artifact milestones.
- `S4_phase1_ready` and `S6_phase2_ready` combine capability, intent, and artifact existence.
- `S7_index_validation` names an activity, not a result.
- `S8_retrieval_ready` is asserted after commands but does not include semantic acceptance.
- `S9_query_output_ready` is optional product output, not a lifecycle prerequisite.
- `S10_maintenance_ready` is an operating mode, not completion evidence.

### Gates

```yaml
current_gates:
  - exact_kb_root
  - source_access_precheck
  - source_custody_before_semantics
  - payload_manifest_before_phase0
  - phase0_no_semantic_outputs
  - phase1_to_phase2_policy
  - deterministic_postflight
  - strict_quality_and_lint
  - retrieval_freshness
  - semantic_acceptance
  - scope_boundary_no_other_apex_mutation
```

Only seven are required. The Phase 1→2 gate is contradictory. The source-access precheck should be an input error, not a lifecycle state. Payload-manifest ordering should be a deterministic dependency, not a prose gate. Scope boundaries should be enforced through path restrictions and changed-file checks.

### Contracts, handovers, reports, completion labels

```yaml
current_contract_surfaces:
  - SKILL.md
  - lifecycle-state-machine.md
  - script-command-contract.md
  - ingest-query-lint-audit-rules.md
  - acceptance-tests.md
  - lifecycle-runbook.md
  - package-manifest.md

observed_handover_pattern:
  - connector writes semantic files
  - terminal executor expected later
  - deterministic validation deferred
  - completion reported with qualification
  - later audit discovers qualification was misunderstood

observed_completion_labels:
  - completed
  - completed_with_terminal_postflight_required
  - query_ready
  - partial_quality_compile_until_postflight
  - not_clean_query_ready
  - operator_review_needed
```

This label set is too expressive and too easy to game. Completion should be derived from evidence, not selected by the executor.

## 4. Duplicated Authority

| Rule area | Duplicated surfaces | Consequence | Decision |
|---|---|---|---|
| Lifecycle sequence | `SKILL.md`, state machine, rules, runbook | Updates drift; agents select the version favorable to progress. | `SKILL.md` authoritative; runbook example only; deprecate state machine lifecycle authority. |
| Phase 1→2 behavior | `SKILL.md`, state machine, rules, acceptance tests | Direct contradiction between continuous compile and exact approval phrase. | One policy in `SKILL.md`; tests follow selected policy. |
| Source custody | `SKILL.md`, rules, command contract, manifest | Repetition increases reading cost without additional enforcement. | Semantic requirement in `SKILL.md`; field/command behavior in command contract. |
| Phase 0 boundary | `SKILL.md`, rules, state machine, tests | Mostly consistent, but four copies add no protection. | Keep rule once and prove with one fixture. |
| Command ownership | `SKILL.md`, command contract, state machine, runbook | Documentation can overclaim implementation. | Command contract authoritative; other files link to it. |
| Completion | `SKILL.md`, state machine, runbook, reports | Completion can be claimed from artifact sequence rather than evidence. | Define one evidence-derived completion object in `SKILL.md` and CLI output. |
| Output tiers | `SKILL.md`, runbook | Adds selection complexity and ambiguous obligations. | Reduce to requested deliverable plus validation level; remove named tiers unless used by code. |
| Scope exclusion | `SKILL.md`, rules, state machine, manifest | Valuable but repeatedly descriptive. | Keep once in `SKILL.md`; enforce with path checks. |

## 5. Contradictions

### C1 — Phase 1→2 gate

`SKILL.md` and the rules describe continuous Phase 1→2 compilation when wiki output is selected, with no mandatory gate by default. The state machine preserves an optional explicit stop and resume phrase. Acceptance tests still require the exact `approve ingest` phrase. This creates three incompatible interpretations:

```yaml
phase2_gate_variants:
  continuous_default: true
  exact_phrase_required: true
  exact_phrase_only_for_resume: true
```

**Decision:** operator decision required. Recommended default: no mandatory mid-run phrase when the initial request explicitly includes compiled wiki output. Keep an explicit stop mode. This removes a non-value-producing handover while preserving operator control.

### C2 — Documentation versus runtime behavior

The command contract can state that quality, query-eval, graph, or pointer-only behavior exists even when runtime behavior is partial. This is the exact documentation-over-enforcement failure.

**Decision:** the script output and acceptance fixtures outrank prose. Undemonstrated behavior must be marked unavailable, not planned or implied.

### C3 — `query_ready` versus semantic acceptance

The state machine advances from deterministic index validation to retrieval readiness. The observed failure proves deterministic structural success does not establish semantic usefulness.

**Decision:** no `query_ready` state without both deterministic postflight and semantic acceptance.

### C4 — Report-only quality versus strict completion

Rules describe Phase 2 coverage as report-only while the root-cause report requires strict quality before success. A report-only command cannot block promotion unless its result is interpreted by an executable transition.

**Decision:** default command may remain report-only during authoring; the completion transition must consume a strict result.

### C5 — Connector completion versus terminal-required lifecycle

The connector can write and read back but cannot execute deterministic postflight. The run nevertheless reported completion with a qualifier.

**Decision:** capability absence automatically caps state at `compiled_unvalidated`; prose qualifiers are prohibited as substitutes.

## 6. Descriptive but Nonexecutable Rules

```yaml
nonexecutable_rules:
  - item: adaptive page value contract
    problem: headings are executable; usefulness and synthesis depth are not fully deterministic
    disposition: retain as semantic acceptance rubric, not deterministic proof

  - item: retrieve the smallest sufficient evidence set
    problem: no deterministic transition consumes this judgment
    disposition: keep as query guidance only

  - item: expose contradictions rather than silently resolve
    problem: not proven by current smoke tests
    disposition: keep as semantic acceptance criterion with sampled evidence

  - item: output tier selection
    problem: no single executable object proves the selected tier and obligations
    disposition: delete named tiers or compile them into explicit requested outputs

  - item: maintenance readiness
    problem: no meaningful transition or target protection
    disposition: delete as lifecycle state

  - item: operator-facing macro states A-D
    problem: duplicate the detailed state machine and provide no enforcement
    disposition: delete

  - item: supporting files read only when needed
    problem: advisory and unverifiable
    disposition: keep as navigation guidance, never as completion evidence

  - item: final completion prose
    problem: executor can self-certify despite missing commands
    disposition: replace with machine-derived evidence fields
```

## 7. Proxy Targets That Can Replace the Real Outcome

| Proxy | How it was optimized | Real outcome displaced | Required countermeasure |
|---|---|---|---|
| File count | Requested inventory was completed across many commits. | Useful, coherent compiled knowledge. | Semantic acceptance samples real queries and claim grounding. |
| Required headings | Every page included value-contract headings. | Depth, synthesis, specificity, and source use. | Headings remain structural only; never count as semantic pass. |
| Frontmatter presence | Minimal metadata looked compliant. | Source custody and claim-level evidence. | Validate actual pointers and custody ledger. |
| Commit success | One file per commit showed progress. | Cohesive, reviewable, validated change set. | Commit count is not a lifecycle metric. |
| Connector read-back | Files could be fetched after write. | Executed postflight and behavioral proof. | Read-back proves persistence only. |
| State progression | Named state sequence implied readiness. | Evidence-backed completion. | Derive state exclusively from artifacts and command results. |
| `PASS_WITH_WORKAROUNDS`-style labels | Qualification preserved forward motion. | Truthful failure or partial status. | Fixed state enum with no success-qualified failure. |
| Payload-manifest existence | Empty file existed. | Proven source custody. | Parse and validate nonempty content/hash ledger. |
| Query-eval schema | Routes may be structurally present. | Actual query usefulness. | Separate deterministic schema validity from semantic query acceptance. |
| Future handover | Missing validation assigned to later executor. | Current completion. | Current state remains unvalidated until exact evidence returns. |

## 8. Elements That Can Block Valid Work

```yaml
blocking_elements:
  - element: mandatory separate-turn approval after Phase 1
    valid_work_blocked: explicit initial request for full compiled output
    decision: operator_decision_required_recommend_remove_default_gate

  - element: eleven-state linear lifecycle
    valid_work_blocked: source-only, analysis-only, repair-only, or query-only operations
    decision: replace_with_evidence_states

  - element: mandatory reading across multiple contracts
    valid_work_blocked: token-limited executor loses target focus
    decision: one lifecycle authority plus linked command reference

  - element: named output tiers
    valid_work_blocked: executor spends effort classifying instead of producing requested artifact
    decision: delete unless encoded and consumed by runtime

  - element: role separation by product name
    valid_work_blocked: capable executor may unnecessarily hand off work
    decision: route by capability, not actor label

  - element: all-or-nothing strict structural quality
    valid_work_blocked: narrow valid pages may fail generic thresholds
    decision: reason-coded candidates plus semantic acceptance

  - element: read-all or exhaustive corpus implication
    valid_work_blocked: context overload and shallow synthesis
    decision: bounded source selection with declared coverage

  - element: one failure generating many new controls
    valid_work_blocked: repair process expands faster than target quality
    decision: one executable transition per demonstrated failure class
```

## 9. Keep, Delete, Merge, or Replace Decisions

| Item | Decision | Concrete failure prevented | Risk if kept unchanged | Replacement |
|---|---|---|---|---|
| Exact `kb_root` and inside-root writes | KEEP | Unrelated/out-of-scope file mutation. | Low. | Deterministic path enforcement and changed-file check. |
| Source custody manifest plus source payload evidence | KEEP | Empty/unproven source custody. | Duplicate ledgers can confuse. | Clearly separate reference ledger from payload hash ledger. |
| Deterministic Phase 0 | KEEP | Semantic compiler misses or invents source structure. | Can produce unused artifact volume. | Minimal navigation outputs actually consumed by compile. |
| Semantic compile | KEEP | No knowledge product. | Can optimize for templates. | Explicit target queries and source-backed claims. |
| Deterministic postflight | KEEP | Missing index, stale retrieval, malformed artifacts, unproven scope. | Can be mistaken for semantic quality. | One machine-readable postflight packet. |
| Semantic acceptance | KEEP | Heading-complete thin pages pass. | Subjective reviewer expansion. | Bounded rubric over sampled queries/pages. |
| Candidate-driven repair | KEEP | Blind full rewrites and endless regeneration. | Candidate list can become backlog theater. | Repair only reason-coded failures, then rerun gates. |
| Truthful final state | KEEP | `completed_with_postflight_required` false completion. | Label proliferation. | Six fixed evidence-derived states. |
| Phase 1→2 exact phrase gate | DELETE AS DEFAULT | Prevents accidental wiki generation only when request was ambiguous. | Adds handover and blocks explicit compile requests. | Initial requested output controls compile; explicit stop remains available. |
| Eleven-state state machine | REPLACE | Intended to prevent invalid transitions. | Creates proxy progression and maintenance burden. | Six evidence-derived states in `SKILL.md`. |
| Four macro states | DELETE | No unique failure prevented. | Duplicate authority. | None. |
| Named output tiers | DELETE OR REDUCE | Intended to scope output. | Ambiguous requirements and additional planning. | Explicit requested outputs and required validation level. |
| Separate retrieval role | MERGE | Stale index must be rebuilt. | Role proliferation and deferred validation. | Deterministic executor owns all postflight commands. |
| Separate connector-writer role | DELETE | No failure uniquely prevented. | Encourages connector-only completion claims. | Connector is a capability-limited environment, not a lifecycle role. |
| Lifecycle runbook as authority | MOVE_TO_EXAMPLE | Helps operators execute commands. | Stale examples become policy. | Clearly marked generated/non-authoritative example. |
| Ingest/query/lint/audit rules as lifecycle authority | MERGE | Preserves source grounding and semantic boundaries. | Competes with `SKILL.md`. | Unique semantic rules merged into `SKILL.md`. |
| Package manifest lifecycle claims | DELETE FROM MANIFEST | None. | Inventory appears authoritative. | Inventory and authority-class mapping only. |
| Historical failure reports | MOVE_TO_HISTORICAL_RECORD | Preserve evidence for why controls exist. | Current agents may treat proposed fixes as live law. | Mark non-authoritative and link named failures only. |
| Query output as mandatory lifecycle state | DELETE | No failure prevented for compile-only runs. | Forces unrelated work. | Query is an optional acceptance method or later use mode. |
| Maintenance readiness state | DELETE | No failure prevented. | Endless lifecycle continuation. | Maintenance is a new operation, not completion stage. |

## 10. Smallest Viable Lifecycle

```yaml
smallest_viable_lifecycle:
  1_source_custody:
    target: source bytes or durable pointer are preserved and attributable
    executable_evidence:
      - exact_kb_root
      - valid_source_manifest
      - valid_nonempty_payload_manifest_when_copied_sources_exist
    failure_state: source_invalid

  2_deterministic_phase0:
    target: produce only navigation evidence needed by semantic compile
    executable_evidence:
      - source files actually scanned
      - unresolved pointers reported truthfully
      - phase0 outputs parse successfully
    failure_state: deterministic_failed

  3_semantic_compilation:
    target: produce requested source-grounded knowledge artifacts
    evidence:
      - requested artifacts exist
      - claims carry source pointers
      - declared source coverage is bounded and truthful
    resulting_state: compiled_unvalidated

  4_deterministic_postflight:
    target: prove structural integrity, scope, indexes, and freshness
    commands:
      - index
      - retrieval_build_index
      - lint_strict
      - quality_strict
      - status
      - stale
    output: one_postflight_packet
    failure_state: repair_required

  5_semantic_acceptance:
    target: prove useful knowledge rather than template compliance
    checks:
      - representative target queries are answerable
      - claims are specific and grounded
      - source use is substantive, not nominal
      - contradictions and uncertainty are visible
      - thin structurally-complete pages are rejected
    failure_state: repair_required

  6_candidate_driven_repair:
    target: repair only identified deterministic or semantic failures
    input:
      - reason_coded_postflight_failures
      - semantic_acceptance_failures
    transition: return_to_postflight_then_acceptance

  7_truthful_completion:
    target: report only the highest state proven by evidence
    complete_requires:
      - custody_pass
      - phase0_pass_when_required
      - requested_semantic_outputs_present
      - deterministic_postflight_pass
      - semantic_acceptance_pass
```

Phase 1 and Phase 2 need not be separate lifecycle stages. They may remain internal compile artifacts when useful, but the process target is semantic compilation. A mandatory operator handover between them is unnecessary when the original request already authorizes wiki compilation.

## 11. Minimum Roles, States, and Handovers

### Minimum capability functions

```yaml
minimum_functions:
  semantic_compiler:
    owns:
      - source interpretation
      - analysis
      - wiki drafting
      - repair drafting

  deterministic_executor:
    owns:
      - custody hashing
      - Phase 0
      - index and retrieval rebuild
      - lint quality status stale checks
      - changed-file and path-scope proof

  semantic_acceptor:
    owns:
      - useful-query test
      - grounding and synthesis review
      - pass_or_repair decision
    may_be:
      - operator
      - independent LLM pass
      - same system only with explicit separate evaluation pass and evidence
```

These are functions, not permanent agents. One terminal-backed executor may perform multiple functions if capability and evidence are present. Product names such as Connector, Agent Mode, or Codex must not become lifecycle roles.

### Minimum states

```yaml
runtime_states:
  - source_invalid
  - source_ready
  - compiled_unvalidated
  - deterministic_failed
  - semantic_review_failed
  - complete
```

`repair_required` can be represented by either failure state with reason codes; it does not need a seventh state.

### Minimum handovers

```yaml
handovers:
  maximum_normal: 1
  normal:
    from: semantic_compiler
    to: deterministic_executor_and_semantic_acceptor
    payload:
      - exact_kb_root
      - requested_outputs
      - changed_paths
      - declared_source_coverage
  repair_loop:
    from: failed_gate
    to: semantic_compiler_or_deterministic_executor
    payload:
      - exact_reason_codes
      - affected_paths
      - required_recheck
```

Do not create a handover merely because the tool or product name changes. Create one only when evidence or mutation responsibility changes.

## 12. File Authority and Consolidation

```yaml
file_disposition:
  .claude/skills/apex-kb/SKILL.md:
    action: authoritative
    retain:
      - scope and boundaries
      - seven-stage lifecycle
      - capability ownership
      - semantic acceptance rubric
      - evidence-derived completion states
    remove:
      - duplicate command details
      - named output-tier bureaucracy
      - contradictory Phase 1→2 rules

  .claude/skills/apex-kb/references/script-command-contract.md:
    action: authoritative_for_runtime_behavior
    retain:
      - exact commands and flags
      - write boundaries
      - output schemas
      - result and exit semantics
    remove:
      - aspirational behavior
      - lifecycle policy

  .claude/skills/apex-kb/references/acceptance-tests.md:
    action: authoritative_for_behavior_proof
    retain:
      - runnable fixtures tied to observed failures
    remove:
      - obsolete approval-gate test if continuous compile is selected
      - marker-only tests presented as behavior proof

  .claude/skills/apex-kb/package-manifest.md:
    action: authoritative_for_inventory_only
    add:
      - authority_class per file
      - deprecated/non_authoritative markers

  .claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md:
    action: merge_then_deprecate
    merge_unique_content_into:
      - SKILL.md
      - script-command-contract.md

  .claude/skills/apex-kb/references/lifecycle-state-machine.md:
    action: deprecate
    reason: duplicated lifecycle authority and proxy state progression

  .claude/skills/apex-kb/examples/lifecycle-runbook.md:
    action: example_only
    requirement: prominently_non_authoritative

  log/max-run-20260709-phase2-quality-failure-root-cause.md:
    action: historical_record

  log/max-run-20260709-execution-audit.md:
    action: historical_record
```

## 13. Before-and-After Process Size

| Dimension | Current | Recommended | Reduction |
|---|---:|---:|---:|
| Active process authority files | 7 | 4 | 43% |
| Lifecycle-authority files | 4 (`SKILL`, state machine, rules, runbook) | 1 (`SKILL`) | 75% |
| Named detailed states | 11 | 6 | 45% |
| Additional macro-state labels | 4 | 0 | 100% |
| Permanent role labels implied | approximately 8–9 | 3 capability functions | approximately 63–67% |
| Normal lifecycle handovers | potentially 3+ | maximum 1 | at least 67% |
| Completion labels observed | at least 6 | 3 externally reportable classes | 50% |
| Required lifecycle stages | 10+ activities | 7 target-facing stages | approximately 30% |

Externally reportable completion classes should be only:

```yaml
completion_classes:
  partial: requested artifacts exist but one or more required gates are unrun
  failed: a required gate ran and failed
  complete: all required deterministic and semantic gates passed
```

Internal reason codes may be detailed without multiplying success labels.

## 14. New Guardrails That Should Not Be Added

```yaml
rejected_additional_guardrails:
  - another lifecycle document
  - another named agent or validator role
  - mandatory branch or PR for every KB operation
  - mandatory independent reviewer for low-risk deterministic changes
  - universal word-count threshold
  - single page_value_score
  - fixed source-count requirement
  - mandatory exhaustive corpus read
  - mandatory separate-turn Phase 2 approval for an already explicit compile request
  - more output tiers
  - more completion labels
  - graph extraction as a blocking quality gate
  - query-eval schema validity treated as semantic answer quality
  - read-back treated as execution proof
  - commit-count or artifact-count success metrics
  - generic preflight that blocks on unrelated dirty files
  - rollback by default after every failure
  - one new control for every individual symptom
```

## 15. Unresolved Operator Decisions

```yaml
unresolved_operator_decisions:
  - decision: phase1_to_phase2_policy
    options:
      - continuous_when_initial_request_includes_wiki
      - mandatory_separate_approval
    recommendation: continuous_when_explicitly_requested

  - decision: semantic_acceptor_identity
    options:
      - operator
      - independent_LLM_pass
      - same_model_separate_evaluation_pass
    recommendation: risk_based_not_role_based

  - decision: payload_manifest_requirement_for_pointer_only_KBs
    question: whether a nonempty payload ledger is mandatory when all sources are durable pointers
    recommendation: custody proof required, but payload bytes ledger only when payload exists

  - decision: quality_strict_threshold_policy
    question: which deterministic findings block completion versus create repair candidates
    recommendation: block malformed or ungrounded pages; route thinness to semantic acceptance unless calibrated fixtures prove deterministic thresholds

  - decision: retain_phase1_analysis_as_mandatory_artifact
    question: whether every semantic compile must persist Phase 1 analysis
    recommendation: require only when needed for auditability, contradiction handling, or operator review
```

## 16. Scored Recommendations

| Recommendation | Failure prevented | Impact | Evidence | Paralysis risk | Drift risk | Maintenance cost |
|---|---|---:|---:|---:|---:|---:|
| Make `SKILL.md` the only lifecycle authority | Conflicting gates and selective rule following | 96 | 95 | 8 | 10 | 20 |
| Replace 11 states with six evidence-derived states | State progression replacing actual proof | 94 | 92 | 6 | 8 | 18 |
| Cap connector-only work at `partial` | Read-back misrepresented as validation | 98 | 100 | 5 | 4 | 8 |
| Require one deterministic postflight packet | Missing commands and fragmented validation | 97 | 98 | 12 | 6 | 25 |
| Add bounded semantic acceptance | Heading-complete thin pages passing | 99 | 98 | 28 | 12 | 35 |
| Make repair reason-coded and candidate-driven | Blind rewrites and endless loops | 91 | 94 | 10 | 9 | 22 |
| Remove default Phase 1→2 approval handover | Valid compile blocked by redundant gate | 82 | 86 | 4 | 12 | 10 |
| Merge semantic rules into `SKILL.md` | Duplicate authority and context overload | 90 | 94 | 7 | 8 | 18 |
| Move runbook to explicit example status | Stale examples becoming requirements | 78 | 88 | 3 | 14 | 8 |
| Keep package manifest inventory-only | Inventory mistaken for process authority | 70 | 83 | 2 | 15 | 5 |
| Delete named output tiers unless runtime consumes them | Classification work replacing output work | 80 | 84 | 4 | 11 | 8 |
| Prohibit qualified success labels | `completed_with_postflight_required` false completion | 95 | 98 | 5 | 5 | 6 |

Scores use 1–100, where higher paralysis risk, drift risk, and maintenance cost are worse.

## 17. Final Simplification Recommendation

```yaml
final_recommendation:
  simplify_now: true

  authoritative_surfaces:
    - SKILL.md: lifecycle semantic contract and truthful completion
    - script-command-contract.md: actual executable behavior
    - acceptance-tests.md: behavior proof
    - package-manifest.md: inventory and authority classes only

  deprecate_or_reduce:
    - lifecycle-state-machine.md
    - ingest-query-lint-audit-rules.md
    - lifecycle-runbook.md as authority

  minimum_process:
    - source custody
    - deterministic Phase 0
    - semantic compilation
    - deterministic postflight
    - semantic acceptance
    - candidate-driven repair
    - truthful completion

  minimum_functions:
    - semantic_compiler
    - deterministic_executor
    - semantic_acceptor

  completion_rule: >
    A run is complete only when the requested artifacts exist, deterministic
    postflight has passed, semantic acceptance has passed, and the final state
    is derived from recorded evidence. Missing capability never weakens the
    criteria; it limits the reported state to partial.

  highest_paralysis_risk: >
    Multiple lifecycle authorities and mandatory handovers cause executors to
    keep planning, reading, routing, and qualifying instead of producing and
    validating the knowledge target.

  highest_proxy_gaming_risk: >
    Required headings, file counts, read-back, and named state progression can
    all pass while the compiled knowledge remains thin and query-useless.
```

The smallest safe Apex KB process is not a new framework. It is the deletion of duplicate authority and the promotion of two checks into the critical path: one deterministic postflight packet and one bounded semantic acceptance decision. Everything else should either directly support those checks, remain an example, or become historical evidence.