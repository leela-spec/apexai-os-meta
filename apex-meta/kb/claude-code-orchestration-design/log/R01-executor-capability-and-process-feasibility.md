# R01 — Executor Capability and Process Feasibility

```okf
research_report:
  id: R01
  title: executor_capability_and_process_feasibility
  repository: leela-spec/apexai-os-meta
  branch: main
  research_mode: bounded_repository_research
  verdict: adopt_with_changes
  primary_failure: >
    Apex KB currently describes a complete lifecycle but does not bind lifecycle
    states to executor capabilities and evidence. The max-run therefore allowed
    GitHub connector writes and read-back to stand in for terminal execution,
    deterministic postflight, and semantic acceptance. This produced a semantic
    compile that existed in Git but was neither deterministically validated nor
    proven useful enough for query-ready promotion.
  smallest_viable_process: >
    Use one capability check, one semantic compile stage, one deterministic
    postflight stage, and one independent semantic acceptance stage. Preserve
    source custody as a prerequisite. Permit bounded handover when the active
    executor cannot perform the next stage. Do not represent a stronger state
    than the evidence bundle supports.
```

## 1. Verdict

The smallest executable lifecycle has **five stages and six truthful completion states**:

1. **Prepare and preserve sources** — terminal-capable deterministic executor or operator.
2. **Semantic compile** — current assistant/chat LLM by default.
3. **Repository persistence** — any executor with bounded repository write capability.
4. **Deterministic postflight** — terminal-backed Agent Mode, Codex with terminal access, or operator.
5. **Independent semantic acceptance** — second-pass LLM or operator that did not draft the evaluated pages.

The lifecycle must separate three claims:

- **compiled**: semantic artifacts were written and read back;
- **validated**: required deterministic commands executed successfully against the committed artifact set;
- **query_ready**: deterministic validation passed, retrieval is fresh, and independent semantic review passed.

A connector-only run may truthfully claim `compiled_unvalidated`; it may not claim `validated`, `postflight_complete`, `lint_clean`, `quality_validated`, or `query_ready`.

## 2. Evidence summary by file

```okf
source_index:
  - id: S01
    path: apex-meta/kb/claude-code-orchestration-design/log/max-run-20260709-phase2-quality-failure-root-cause.md
    authority: failure_evidence
    decisive_findings:
      - quality command was not executed after semantic writes
      - GitHub read-back replaced terminal validation
      - heading-complete thin pages escaped the structural heuristic
      - connector limitations biased execution toward compressed pages and many commits
      - connector-only status should be partial_unvalidated_compile

  - id: S02
    path: apex-meta/kb/claude-code-orchestration-design/log/max-run-20260709-execution-audit.md
    authority: failure_evidence
    decisive_findings:
      - run was not clean query-ready
      - source payload custody was not proven
      - no deterministic postflight ran after writes
      - 37 direct commits increased interruption and rollback risk
      - final report overstated completion unless read narrowly

  - id: S03
    path: .claude/skills/apex-kb/SKILL.md
    authority: contract
    decisive_findings:
      - semantic work belongs to current assistant by default
      - Agent Mode and Codex are deterministic executors by default
      - query_ready requires postflight, retrieval, and quality checks
      - current completion gate does not define evidence per state
      - Phase 1 and Phase 2 are continuous for compiled output tiers

  - id: S04
    path: .claude/skills/apex-kb/references/lifecycle-state-machine.md
    authority: contract
    decisive_findings:
      - current model has eleven detailed states plus four macro states
      - transitions name commands but do not verify executor capability
      - S6 can advance directly to deterministic validation without a bounded handover state
      - semantic acceptance is absent
      - query-ready evidence is not represented as a state bundle

  - id: S05
    path: .claude/skills/apex-kb/references/script-command-contract.md
    authority: contract
    decisive_findings:
      - scripts are local, no-network, dry-run by default
      - deterministic commands require Python execution and sometimes writes
      - lifecycle and retrieval commands have explicit exit policies
      - quality is structural and deterministic, not semantic certification
      - documentation can describe capabilities that still require live execution proof

  - id: S06
    path: .claude/skills/apex-kb/references/acceptance-tests.md
    authority: acceptance_test
    decisive_findings:
      - tests require repository-root terminal execution
      - fixtures cover source custody, Phase 0, indexes, lint, quality, graph, and stale status
      - tests do not independently accept semantic usefulness
      - fixture pages can satisfy headings while containing placeholders
      - documented acceptance is not evidence unless commands actually run

  - id: S07
    path: .claude/skills/apex-kb/examples/lifecycle-runbook.md
    authority: runbook
    decisive_findings:
      - runbook has four macro phases
      - postflight is described as required but not capability-routed
      - no explicit status is defined for an interrupted semantic compile
      - no semantic reviewer is required before query-ready

  - id: S08
    path: apex-meta/scripts/apex_kb.py
    authority: runtime
    inspected_symbols:
      - cmd_quality
      - cmd_lint
      - cmd_status
      - build_parser
      - main
    decisive_findings:
      - lint distinguishes report-only findings from blocking findings
      - quality strict fails only on repair or shell candidates
      - status reports freshness but does not certify lifecycle completion
      - main maps fail, blocked, or error to nonzero exit
      - parser exposes commands but does not enforce lifecycle order or capability routing

  - id: S09
    path: apex-meta/scripts/apex_kb_retrieval.py
    authority: runtime
    inspected_surfaces:
      - index building
      - stale detection
      - command dispatch
    decisive_findings:
      - build-index writes JSON, NDJSON, metadata, and optional SQLite artifacts
      - stale detection compares current wiki hashes with index metadata
      - missing or unreadable metadata is not fresh
      - command dispatch returns nonzero only for blocked or error states
      - query can fall back to live page chunking, so retrieval availability is not query-ready certification
```

## 3. Current lifecycle as actually executable

```okf
actual_current_lifecycle:
  - stage: prepare
    intended_actions:
      - scaffold
      - source intake
      - payload manifest
      - phase0
    actual_requirement: terminal or manual Python execution for deterministic proof
    failure_mode: connector can write approximations but cannot prove commands ran

  - stage: semantic_compile
    intended_actions:
      - Phase 1 analysis
      - Phase 2 wiki drafting when selected tier includes wiki
    actual_requirement: source-reading LLM plus repository write surface
    failure_mode: artifact count and headings can replace useful synthesis

  - stage: persistence
    intended_actions:
      - save compiled pages
      - preserve scope
    actual_requirement: GitHub connector, terminal Git, Codex, or operator
    failure_mode: many one-file commits, partial interruption, unrelated commits in audit window

  - stage: deterministic_postflight
    intended_actions:
      - index
      - retrieval build-index
      - stale
      - lint strict
      - quality strict
      - status
    actual_requirement: terminal-backed executor
    failure_mode: described in docs but skipped when active executor lacks terminal

  - stage: query_or_maintain
    intended_actions:
      - retrieve
      - query
      - audit
      - repair
    actual_requirement: fresh evidence bundle and query synthesis
    failure_mode: retrieval fallback can return results even when derived index is stale, allowing availability to be mistaken for readiness
```

The current process is executable only when a terminal-backed executor participates. It is not executable end-to-end in normal ChatGPT chat with only a GitHub connector.

## 4. Executor capability matrix

Legend: `supported` means the executor can perform and evidence the capability in the described environment; `partial` means it can contribute but cannot certify completion; `unsupported` means it cannot perform the required operation.

| Lifecycle capability | ChatGPT + GitHub connector | Terminal-backed Agent Mode | Codex + repo/terminal | Operator/manual |
|---|---|---|---|---|
| Read repository files | supported | supported | supported | supported |
| Read supplied sources semantically | supported | supported | partial by default role | supported |
| Draft Phase 1/Phase 2 semantics | supported | partial; only when delegated | partial; not default owner | supported |
| Write repository files | supported | supported | supported | supported |
| Group changes into controlled Git commit | partial | supported | supported | supported |
| Run `apex_kb.py` commands | unsupported | supported | supported | supported |
| Run retrieval build/stale | unsupported | supported | supported | supported |
| Prove exit codes and command outputs | unsupported | supported | supported | supported |
| Detect dirty worktree or concurrent changes | unsupported | supported | supported | supported |
| Deterministic postflight certification | unsupported | supported | supported | supported |
| Independent semantic review | supported only as a separate review pass | supported if not drafter | supported if explicitly tasked and supplied sources | supported |
| Commit and push | supported through connector but weakly grouped | supported | supported | supported |
| Certify `query_ready` alone | unsupported | partial; lacks independent semantic review if same drafter | partial; lacks independent semantic review if same drafter | supported when review separation is maintained |

### Capability conclusions

- **ChatGPT with GitHub connector** is a semantic drafter and repository writer, not a terminal validator.
- **Terminal-backed Agent Mode** can own deterministic preparation, persistence, postflight, and handover evidence. It should not become the default semantic author merely because it has terminal access.
- **Codex with terminal access** is suitable for deterministic application, tests, validation, commit, and push. Semantic ownership remains optional and explicit.
- **Operator/manual execution** is the universal fallback and final authority for ambiguous semantic acceptance.

## 5. Proxy completion and false validation points

```okf
proxy_substitution_failures:
  - proxy: file_exists
    mistaken_for: semantic_compile_complete
    correction: require expected artifact inventory plus read-back and interruption marker absence

  - proxy: headings_present
    mistaken_for: useful_phase2_page
    correction: keep deterministic structural metrics separate from semantic acceptance

  - proxy: connector_readback
    mistaken_for: terminal_command_execution
    correction: read-back proves persistence only

  - proxy: command_documented
    mistaken_for: command_executed
    correction: require captured command, exit code, commit SHA, and artifact hashes

  - proxy: status_command_output
    mistaken_for: lifecycle_certification
    correction: status is an observation surface, not a promotion authority

  - proxy: retrieval_returns_results
    mistaken_for: fresh_query_ready_retrieval
    correction: require stale status fresh or explicitly bounded raw fallback

  - proxy: same_llm_second_pass
    mistaken_for: independent_semantic_review
    correction: require separate review context or operator review

  - proxy: all_requested_files_created
    mistaken_for: complete_run
    correction: completion state derives from the strongest completed evidence bundle

  - proxy: postflight_required_later
    mistaken_for: completed_with_minor_followup
    correction: classify as compiled_unvalidated, not completed
```

## 6. Smallest viable lifecycle

### 6.1 Stages

```okf
minimum_lifecycle:
  stages:
    - id: P0
      name: capability_and_scope_precheck
      owner: active_executor
      required_evidence:
        - resolved repository and branch
        - resolved KB root and output tier
        - capability declaration for semantic read, repo write, terminal execution, independent review
      success_state: ready
      failure_state: bounded_handover_required

    - id: P1
      name: source_custody_and_navigation
      owner: terminal_executor_or_operator
      required_evidence:
        - source manifest or durable pointer records
        - payload manifest status
        - Phase 0 result when corpus navigation is required
      success_state: source_ready

    - id: P2
      name: semantic_compile_and_persist
      owner: semantic_executor
      required_evidence:
        - expected artifact inventory
        - source pointers in outputs
        - repository read-back at one immutable commit or tree
        - compile completion record
      success_state: compiled_unvalidated

    - id: P3
      name: deterministic_postflight
      owner: terminal_executor_or_operator
      required_evidence:
        - index command pass
        - retrieval build-index pass
        - retrieval stale status fresh
        - lint strict pass
        - quality strict pass
        - status output
        - exact commit SHA validated
      success_state: deterministically_validated

    - id: P4
      name: independent_semantic_acceptance
      owner: independent_llm_or_operator
      required_evidence:
        - bounded page sample or targeted repair-candidate review
        - source-faithfulness verdict
        - query-usefulness verdict
        - no unresolved semantic fail
      success_state: query_ready
```

### 6.2 Completion states

```okf
completion_states:
  - state: ready
    meaning: scope and required executor capabilities are resolved

  - state: source_ready
    meaning: source custody and required deterministic navigation are proven

  - state: compile_in_progress
    meaning: semantic outputs may be partial; no completion claim allowed

  - state: compiled_unvalidated
    meaning: expected semantic artifacts were persisted and read back, but terminal postflight has not passed

  - state: deterministically_validated
    meaning: required commands passed against the identified commit; semantic usefulness is not yet certified

  - state: query_ready
    meaning: deterministic validation passed, retrieval is fresh, and independent semantic acceptance passed

  - state: repair_required
    meaning: deterministic or semantic review failed; only targeted repair may resume
```

### 6.3 Transition contract

```okf
transition_requirements:
  - from: ready
    to: source_ready
    requires: deterministic source-custody evidence

  - from: source_ready
    to: compile_in_progress
    requires: semantic executor with source access and repo-write or handover target

  - from: compile_in_progress
    to: compiled_unvalidated
    requires:
      - complete expected artifact inventory
      - immutable commit or tree identifier
      - no known interrupted write

  - from: compiled_unvalidated
    to: deterministically_validated
    requires:
      - terminal execution against same or descendant commit containing only bounded repairs
      - all mandatory postflight commands pass

  - from: deterministically_validated
    to: query_ready
    requires:
      - independent semantic acceptance pass
      - retrieval status fresh

  - from: any_nonterminal_state
    to: repair_required
    requires: failed deterministic command, failed semantic review, stale retrieval after rebuild attempt, or scope contamination
```

No transition may be inferred from file presence, headings, connector read-back, or a promise to validate later.

## 7. Behavior when required capability is unavailable

```okf
missing_capability_behavior:
  rule: never downgrade the required evidence silently

  before_stage_start:
    action: do_not_start_stage
    output:
      - current_state
      - missing_capability
      - required_executor_class
      - exact next commands or semantic review task
      - immutable commit or artifact paths

  during_semantic_compile:
    action: persist_completed_subset_and_mark_compile_in_progress
    forbidden_claims:
      - compiled
      - validated
      - query_ready

  after_repository_write_without_terminal:
    action: set_compiled_unvalidated_and_handover
    handover_minimum:
      - repository
      - branch
      - commit_sha
      - kb_root
      - expected postflight commands
      - expected pass conditions

  during_deterministic_postflight:
    action: stop_at_first_blocking_failure
    next_state: repair_required
    preserve:
      - command output
      - exit code
      - tested commit
      - dirty-state report

  during_semantic_review:
    action: produce_reason_coded_repair_set
    next_state: repair_required
    forbidden: self-certify by adding headings or generic claims
```

A bounded handover is not an extra lifecycle stage. It is the required output of any stage that cannot continue under the active executor.

## 8. Keep, delete, or merge

| Existing item | Decision | Reason |
|---|---|---|
| Current four macro phases A–D | **merge/replace** | Replace with five executable stages tied to evidence; current phases hide executor boundaries. |
| Eleven detailed lifecycle states | **merge** | Reduce to six completion states plus `repair_required`; several current states are implementation steps, not externally meaningful states. |
| Phase 1 and Phase 2 separate approval state | **merge by default** | Keep a stop option for analysis-only, but compiled tiers should use one semantic compile stage as current SKILL already specifies. |
| `approve ingest` legacy phrase | **keep only as optional resume mechanism** | It is not a capability or quality gate. |
| Source custody prerequisite | **keep** | Prevents inferred or untraceable source use. |
| Deterministic versus semantic ownership split | **keep** | Directly prevents connector read-back from replacing terminal validation. |
| Output tiers | **keep but redefine evidence** | Useful operator interface if `compiled`, `validated`, and `query_ready` are evidence-bound. |
| `status` as completion gate | **delete** | Runtime status reports facts but cannot certify semantic or aggregate completion. |
| Report-only page-value lint | **keep** | Useful structural signal; must not stand in for semantic acceptance. |
| Mandatory postflight handover for connector runs | **keep and simplify** | One bounded handover packet is sufficient; no multi-agent architecture required. |
| Dedicated Agent Mode patch-builder role for normal KB runs | **delete from lifecycle** | It is a repair workflow specialization, not a necessary KB lifecycle role. |
| Separate validator, executor, and final approver for every stage | **delete** | Excessive. Independence is required only for semantic acceptance and high-risk repository changes. |
| Query-eval schema validation | **keep as deterministic evidence** | It validates expected routes but does not prove answer quality. |
| Independent semantic review | **add** | This is the missing gate for heading-complete but low-value pages. |

## 9. Failure-case tests

```okf
failure_simulations:
  - scenario: connector_only_work
    setup: ChatGPT drafts and writes pages through GitHub connector
    expected_behavior: state becomes compiled_unvalidated
    prevented_false_claim: connector read-back cannot produce validated or query_ready

  - scenario: interrupted_writes
    setup: expected artifact inventory is incomplete or writes span partial commits
    expected_behavior: remain compile_in_progress; handover lists completed and missing files
    prevented_false_claim: partial file set cannot become compiled

  - scenario: failed_postflight
    setup: lint strict or quality strict returns nonzero
    expected_behavior: state becomes repair_required; query_ready transition blocked
    prevented_false_claim: existence and headings cannot override failed commands

  - scenario: stale_retrieval
    setup: wiki pages change after index metadata generation
    expected_behavior: rebuild retrieval; require stale status fresh before query_ready
    prevented_false_claim: successful fallback query cannot certify freshness

  - scenario: failed_semantic_review
    setup: pages are structurally valid but shallow, weakly grounded, or query-useless
    expected_behavior: deterministically_validated remains true, query_ready blocked, reason-coded repair set produced
    prevented_false_claim: deterministic validation cannot self-promote semantic quality

  - scenario: dirty_or_changed_main
    setup: main advances or unrelated files appear between compile and postflight
    expected_behavior: terminal validator identifies exact tested commit and scope; unrelated changes are excluded or run is blocked
    prevented_false_claim: broad base-to-head comparison cannot contaminate run accounting
```

## 10. Exact repository files likely to require later changes

```okf
exact_repo_files_likely_affected:
  mandatory:
    - .claude/skills/apex-kb/SKILL.md
    - .claude/skills/apex-kb/references/lifecycle-state-machine.md
    - .claude/skills/apex-kb/examples/lifecycle-runbook.md
    - .claude/skills/apex-kb/references/acceptance-tests.md
    - .claude/skills/apex-kb/references/script-command-contract.md

  likely_runtime_alignment:
    - apex-meta/scripts/apex_kb.py

  likely_no_change_required_for_process_model:
    - apex-meta/scripts/apex_kb_retrieval.py
```

Runtime changes in `apex_kb.py` should be limited to aggregate lifecycle evidence or explicit command-result fields if the process contract cannot be enforced solely in documentation and execution prompts. The parser should not become a general workflow engine.

## 11. Unresolved operator decisions

```okf
unresolved_operator_decisions:
  - decision: semantic_reviewer
    options:
      - separate ChatGPT review pass with isolated evaluator prompt
      - operator review
      - delegated independent model
    recommendation: separate review pass by default; operator decides failures

  - decision: compile_commit_policy
    options:
      - one grouped commit per semantic compile
      - bounded batch commits with final manifest
    recommendation: one grouped commit when terminal Git is available; bounded batches only when connector limitations require them

  - decision: strict_quality_failure_scope
    options:
      - fail any repair candidate
      - fail only target output set
    recommendation: evaluate only pages created or changed by the run plus directly affected indexes

  - decision: analysis_only_resume_gate
    options:
      - retain exact approve ingest phrase
      - use explicit resume command without fixed phrase
    recommendation: retain as compatibility alias, not core lifecycle state
```

## 12. Final recommendation

### Mandatory changes

```okf
mandatory_changes:
  - bind every completion state to explicit evidence
  - add capability precheck before starting each stage
  - classify connector-only semantic writes as compiled_unvalidated
  - require terminal postflight for deterministic validation
  - require independent semantic acceptance before query_ready
  - require immutable commit SHA in every handover and validation record
  - stop on blocking postflight failure and enter repair_required
  - require retrieval stale status fresh before query_ready
```

### Optional changes

```okf
optional_changes:
  - add one aggregate postflight command that invokes existing commands without replacing their outputs
  - add a machine-readable completion evidence packet under log/ or outputs/
  - group connector writes through Git trees when available
  - add targeted semantic review exemplars for strong and structurally complete but weak pages
```

### Rejected overengineering

```okf
rejected_overengineering:
  - permanent multi-agent hierarchy
  - separate agent for every lifecycle state
  - universal branch and pull-request requirement
  - making graph extraction blocking for query readiness
  - turning deterministic quality into an LLM score
  - requiring semantic review of every page in every run
  - embedding Git orchestration into apex_kb.py
  - blocking valid work merely because optional tools are unavailable
```

## 13. Scored recommendations

Scores use independent 1–100 scales. Higher implementation risk, paralysis risk, and complexity cost are worse. No composite score is calculated.

| Recommendation | Observed failure prevented | Impact | Evidence | Implementation risk | Process paralysis risk | Complexity cost |
|---|---|---:|---:|---:|---:|---:|
| Evidence-bound completion states | Final report overstated completion | 98 | 98 | 18 | 8 | 18 |
| Connector-only state `compiled_unvalidated` | Read-back represented as validation | 97 | 100 | 8 | 3 | 6 |
| Mandatory terminal postflight | Quality, lint, stale, index commands skipped | 99 | 100 | 20 | 18 | 22 |
| Independent semantic acceptance | Heading-complete thin pages escaped | 96 | 96 | 32 | 28 | 30 |
| Capability precheck and bounded handover | Executor limitations silently weakened criteria | 94 | 96 | 15 | 12 | 16 |
| Immutable commit SHA in validation | Concurrent/unrelated commits contaminated audit | 91 | 94 | 12 | 5 | 10 |
| Reduce lifecycle to six states | Descriptive states obscured executable boundaries | 82 | 88 | 25 | 10 | 14 |
| One grouped semantic compile commit | 37 commits increased interruption risk | 80 | 93 | 28 | 22 | 26 |
| Optional aggregate postflight command | Operators can omit one of several commands | 78 | 82 | 35 | 15 | 28 |
| Machine-readable completion packet | Completion evidence scattered across logs | 72 | 78 | 24 | 8 | 20 |

## 14. Final position

The lifecycle should not attempt to make every executor capable of every stage. It should make capability boundaries explicit and preserve truthful intermediate states.

The minimum reliable rule is:

> A run may claim only the strongest state supported by executed evidence against an identified artifact set.

Under that rule, semantic drafting can continue in ChatGPT, GitHub connector persistence remains useful, terminal-backed Agent Mode or Codex performs deterministic postflight, and a separate reviewer determines semantic usefulness. Missing capability produces a bounded handover rather than a weakened completion claim.
