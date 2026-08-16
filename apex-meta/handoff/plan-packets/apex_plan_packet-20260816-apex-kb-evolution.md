---
title: "Apex Plan Packet — ApexKB Alternatives or Upgrade"
document_role: apex_plan_operator_review_packet
created: 2026-08-16
status: operator_review_needed
planning_status: evidence_checked_candidate
package: apex-plan
candidate_epic_slug: apex-kb-evolution
target_week: 2026-W34
canonical_mutation_performed: false
---

# ApexKB Alternatives or Upgrade

## project_capture_record

```yaml
project_capture_record:
  goal: >
    Decide and validate the highest-value forward path for ApexKB without
    assuming that further custom development is justified: continue upgrading,
    freeze, replace with an existing system, or preserve ApexKB's strongest
    deterministic/source-integrity components around another wiki/retrieval engine.

  source:
    - operator portfolio input 2026-08-16
    - installed apex-kb operating contract
    - apex-meta/kb current roots
    - apex-meta/kb/therapy-narm-personal-development/audit/handoffs/2026-07-23-apex-kb-value-audit-handover.md
    - apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/

  current_strengths:
    - durable source custody and manifests
    - deterministic lifecycle/state checks
    - source-pointer/citation validation
    - structured Phase 1/Phase 2 knowledge compilation
    - deterministic source atlases
    - local retrieval/indexing
    - drift/staleness and audit concepts

  known_residual_risks:
    - lexical FTS5-only retrieval
    - semantic acceptance disabled by default in latest CLI flow
    - query_ready may overstate semantic quality
    - no operator-intent benchmark or golden query set
    - no measured token-savings benchmark versus raw corpus
    - no embedding/hybrid reranker/query decomposition/graph layer
    - retrieval returns chunks rather than a bounded evidence/answer packet
    - update/drift behavior not sufficiently proven after the new architecture
    - CLI skill and repository instructions diverge across generations
    - clean installation/packaging remains brittle
    - future agents are not automatically integrated with KB query/retrieval policy
    - operator interface still exposes excessive lifecycle mechanics
    - small-corpus success may not generalize

  constraints:
    - sunk development effort is not a reason to continue
    - external competitors must be verified against current primary sources before scoring
    - private KB data must not be exposed to hosted evaluation/retrieval services without explicit governance approval
    - no replacement migration before comparative evidence and operator decision
```

## epic_record

```yaml
epic_record:
  slug: apex-kb-evolution
  title: ApexKB Alternatives or Upgrade
  status: open
  priority: medium
  due_date: null
```

## proposed_task_records

### Task 1 — Re-baseline current ApexKB implementation and contract

```yaml
id: 1
title: Re-baseline current ApexKB implementation and contract
status: open
priority: high
due_date: null
depends_on: []
blocked_by: []
acceptance_criteria:
  - current CLI command surface and installed apex-kb skill are compared
  - current lifecycle states/gates are documented from current main
  - current retrieval architecture is documented
  - current semantic-acceptance behavior is verified
  - previously listed residual risks are marked still-present fixed or superseded
  - current KB roots and representative completed KBs are inventoried
definition_of_done:
  - one current-state baseline exists that does not rely on July handovers as current truth
source:
  - apex-meta/apex-kb-cli/
  - .claude/skills/apex-kb/
  - apex-meta/scripts/apex_kb.py and retrieval tooling where current
  - current audit handovers
```

### Task 2 — Build operator-value benchmark for ApexKB

```yaml
id: 2
title: Build operator-value and retrieval benchmark for ApexKB
status: open
priority: high
due_date: null
depends_on: [1]
blocked_by: []
acceptance_criteria:
  - predefined high-value query set is created from real intended use cases
  - answer-quality rubric covers correctness completeness reasoning provenance uncertainty and practical usefulness
  - retrieval precision/recall or equivalent relevance measures are defined
  - raw-source reopen behavior is tested
  - token/context cost is measured against reading raw corpus directly
  - update/drift cases include changed added deleted and superseded sources
  - benchmark separates deterministic completion from semantic usefulness
definition_of_done:
  - current ApexKB has a measured value baseline rather than only structural test counts
```

### Task 3 — Evaluate cheapest credible ApexKB upgrade path

```yaml
id: 3
title: Evaluate cheapest credible ApexKB upgrade path
status: open
priority: medium
due_date: null
depends_on: [1, 2]
blocked_by: []
acceptance_criteria:
  - improvements are ranked by measured benchmark impact and implementation cost
  - retrieval options consider lexical improvements hybrid/vector retrieval reranking query planning and evidence-packet generation only where justified
  - semantic acceptance and future-agent integration are evaluated
  - lifecycle/operator UX simplification is evaluated
  - update/drift reliability is included
  - proposals preserve local/private operation options
  - no architecture is added solely because it is fashionable
definition_of_done:
  - bounded upgrade candidate and expected benchmark gains are explicit
```

### Task 4 — Evaluate current external/local alternatives and hybrid options

```yaml
id: 4
title: Evaluate current ApexKB alternatives and hybrid options
status: open
priority: medium
due_date: null
depends_on: [1, 2]
blocked_by: []
acceptance_criteria:
  - current primary documentation/code is used for every candidate
  - local indexed llm-wiki projects are evaluated individually rather than from old summary alone
  - named prior competitors are re-verified for current capability status
  - additional maintained alternatives may be added only when they match operator goals
  - candidates are scored on source preservation retrieval/answer quality updates privacy local operation integration simplicity maintenance cost and migration cost
  - hybrid option explicitly evaluates retaining Apex deterministic custody/audit around another retrieval/wiki engine
  - marketing claims are not treated as verified capabilities
definition_of_done:
  - decision matrix compares keep/upgrade replace and hybrid paths on current evidence
notes:
  - this task requires current external research at execution time
```

### Task 5 — Run controlled comparison on the same corpus and query set

```yaml
id: 5
title: Run controlled ApexKB versus alternative comparison
status: open
priority: high
due_date: null
depends_on: [3, 4]
blocked_by: []
acceptance_criteria:
  - same source corpus and golden query set are used where technically possible
  - privacy constraints are respected
  - setup/operator effort is measured
  - retrieval and answer quality use the same rubric
  - token/context cost and update behavior are measured
  - failures and manual interventions are recorded
  - results distinguish product fit from implementation polish
definition_of_done:
  - empirical comparison can support a continue freeze replace or hybrid decision
```

### Task 6 — Decide ApexKB direction

```yaml
id: 6
title: Decide ApexKB continue freeze replace or hybrid direction
status: open
priority: high
due_date: null
depends_on: [5]
blocked_by:
  - operator_decision_required
acceptance_criteria:
  - measured benchmark and comparison results are presented
  - sunk cost is excluded from decision rationale
  - transition cost and reversibility are explicit
  - operator chooses one direction
  - rejected options and reasons are recorded
definition_of_done:
  - one authoritative direction decision exists
```

### Task 7 — Pilot chosen ApexKB evolution path before migration

```yaml
id: 7
title: Pilot chosen ApexKB evolution path before broad migration
status: open
priority: medium
due_date: null
depends_on: [6]
blocked_by: []
acceptance_criteria:
  - one representative KB/use case is used
  - current sources and old KB remain recoverable
  - pilot validates the expected operator-value improvement
  - integration with future-agent query workflow is tested
  - rollback path exists
  - broad migration is not started unless pilot acceptance succeeds
definition_of_done:
  - chosen path has real pilot evidence and explicit migration/no-migration recommendation
```

## dependency_plan

```yaml
dependency_plan:
  chain:
    - 1 -> 2
    - 2 -> 3
    - 2 -> 4
    - 3 + 4 -> 5
    - 5 -> 6
    - 6 -> 7
  apex_sync_handoff_requests:
    - validate_dependencies
    - compute_next_action
    - compute_focus_candidates
```

## priority_urgency_focus_rationale

```yaml
priority_urgency_focus_rationale:
  epic_priority: medium
  due_date: null
  provisional_focus_recommendation:
    first: Re-baseline current ApexKB implementation and contract
    rationale: >
      The strongest prior audit is valuable but explicitly historical. A current
      baseline is necessary before comparing upgrades or alternatives.
```

## review_flags

```yaml
review_flags:
  - operator_review_needed
  - external_alternatives_require_current_primary_source_research
  - privacy_governance_required_for_hosted_candidates
  - do_not_assume_custom_upgrade_is_preferred
```

## handoff_requests

```yaml
handoff_requests:
  to_apex_session_after_operator_approval:
    - create canonical epic/task records
```

## operator_gate

```yaml
operator_gate:
  status: operator_review_needed
  recommended_decision: approved_for_handoff
  mutation_allowed_by_this_packet: false
```
