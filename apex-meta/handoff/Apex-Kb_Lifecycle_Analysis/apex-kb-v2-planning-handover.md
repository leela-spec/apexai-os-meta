# Apex KB v2 Planning Handover

```yaml
handover_metadata:
  artifact_name: apex_kb_v2_planning_handover
  status: planning_handover_for_next_chat
  branch_context: test/apex-kb-skill-package-execution
  latest_known_commit_from_operator: a47eeb9
  commit_message_from_operator: Repair apex-kb package contracts
  created_for: next_chat_planning
  mode: audit_and_planning_only
  repo_write_required_next: false
  primary_question: >
    What should the next version of Apex KB optimize after the package passed
    its first real Codex execution test and the package-contract repair script
    was run?
```

## 0. Current state

```yaml
current_state:
  package_path: .claude/skills/apex-kb/
  deterministic_script: apex-meta/scripts/apex_kb.py
  tested_kb_root: apex-meta/kb/apex-kb-skill-test/
  test_verdict: skill_package_passed_with_warnings
  post_repair_state:
    operator_reported_commit: a47eeb9
    pushed: true
    excluded_untracked:
      - .repair-backups/
      - FutureDevelopments&Research/...
```

The current package is no longer a theoretical design only. It has produced a real isolated KB, run deterministic script commands, and then had its package contracts repaired for source modes, phase gates, claim labeling, and collapsed YAML/template formatting.

## 1. Evidence base to load in the next chat

```yaml
must_load_first:
  repaired_branch_files:
    - .claude/skills/apex-kb/SKILL.md
    - .claude/skills/apex-kb/references/kb-contract.md
    - .claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md
    - .claude/skills/apex-kb/references/script-command-contract.md
    - .claude/skills/apex-kb/templates/ingest-analysis-template.md
    - .claude/skills/apex-kb/templates/wiki-page-templates.md
    - .claude/skills/apex-kb/package-manifest.md
    - apex-meta/scripts/apex_kb.py

  execution_test_artifacts:
    - apex-meta/kb/apex-kb-skill-test/test-run-report.md
    - apex-meta/kb/apex-kb-skill-test/manifests/source-manifest.json
    - apex-meta/kb/apex-kb-skill-test/wiki/index.md
    - apex-meta/kb/apex-kb-skill-test/ingest-analysis/et-heller-narm.analysis.md
    - apex-meta/kb/apex-kb-skill-test/ingest-analysis/shadow-insight-v1.analysis.md
    - apex-meta/kb/apex-kb-skill-test/ingest-analysis/narm-acim-handover.analysis.md

  saved_project_sources:
    - APEX KB — LLM-Wiki Blueprint Capability Map.md
    - APEX KB — Validated Decision Addendum
    - Apex KB Test Run.txt
    - prior comparison/improvement analysis saved as project source
    - Claude_Skill_Package_BestPractice_Handover.md
    - Claude_Skill_PromptFlow_Design_Guidance_v1.md
```

Do not re-open public GitHub research unless the operator explicitly asks. The current task is package-evolution planning from saved project sources and repo-local outputs.

## 2. What is already solved

```yaml
solved:
  execution_proof:
    - Codex could run the skill package from installed files.
    - apex_kb.py exposed scaffold/hash/preflight/manifest/index/lint/audit.
    - Deterministic postflight succeeded on the isolated KB.

  repaired_contract_defects:
    - source_storage_modes added.
    - same-prompt phase gate ambiguity documented.
    - confidence and claim_label separated.
    - wiki template frontmatter uncollapsed.
    - script-command contract aligned closer to actual apex_kb.py.
    - SKILL.md supporting/failure/completion YAML uncollapsed.

  stable architectural decisions:
    - Python owns deterministic structure and validation.
    - LLM owns semantic extraction, synthesis, page drafting, and query synthesis.
    - kb-schema.md is used instead of CLAUDE.md inside KB roots.
    - ingest-analysis/ is mandatory for Phase 1.
    - wiki/index.md is the query entry point.
```

## 3. Remaining strategic problem

```yaml
remaining_problem:
  name: apex_kb_v2_efficiency_and_quality_upgrade
  description: >
    V1 proves the package can execute. V2 should improve the value-to-overhead
    ratio: fewer files/pages where possible, less prompt burden, stronger
    deterministic checks, better ingestion quality, and clearer output tiers.
  anti_goal: >
    Do not create more package files just because the architecture can support
    them. Reduce friction unless an extension materially improves future AI
    retrieval, source traceability, or rebuild reliability.
```

## 4. Priority metric system

Use this scoring model for all proposed V2 changes.

```yaml
priority_metric:
  scale: 0_to_5_per_dimension
  dimensions:
    impact:
      weight: 0.30
      meaning: "Improves real KB usefulness, future AI work quality, or source-grounded synthesis."
    reliability:
      weight: 0.20
      meaning: "Reduces hallucination, drift, schema mismatch, broken links, or operator ambiguity."
    token_efficiency:
      weight: 0.20
      meaning: "Reduces repeated reading, file count, context burden, or output bloat."
    implementation_ease:
      weight: 0.15
      meaning: "Can be implemented with small repo-local changes and little architecture risk."
    reuse_leverage:
      weight: 0.10
      meaning: "Useful for many future KBs, not just the therapy/NARM test."
    testability:
      weight: 0.05
      meaning: "Can be validated by script or repeatable Codex test."
  score_formula: >
    round(20 * (0.30*impact + 0.20*reliability + 0.20*token_efficiency +
    0.15*implementation_ease + 0.10*reuse_leverage + 0.05*testability))
```

## 5. Ranked high-impact realizations

| Rank | Realization | Score | Why it matters | Recommended V2 action |
|---:|---|---:|---|---|
| 1 | Make `apex-kb` explicitly tiered: raw source ledger → Phase 1 analysis → compiled wiki → applied cards/query outputs | 94 | V1 already has all layers, but the operator needs clearer control over which layers are required for which job. | Add an `output_tier_policy` and default tier presets: `source_only`, `analysis_only`, `compiled_minimal`, `compiled_full`, `query_only`. |
| 2 | Add a deterministic `quality` or `eval` command to `apex_kb.py` | 92 | Current lint validates structure; it does not measure semantic coverage, page redundancy, claim-label consistency, applied-card presence, or source-to-page coverage. | Implement a Python `quality` command with non-semantic checks and a required LLM-authored `quality-notes` section. |
| 3 | Compact `SKILL.md` into a routing kernel and move most policy detail to references | 88 | The repaired `SKILL.md` is now readable, but it still carries many contract details. Skills should trigger quickly and progressively load references. | Target 120-170 lines for `SKILL.md`; keep mode, boundaries, procedure, and support-file map only. Move deep source/phase/label policy to references. |
| 4 | Add source-set planning before ingestion | 87 | V1 ingested three sources and left two optional sources unread as present-but-not-ingested. This was correct for a test but not ideal for real KB growth. | Add a Phase 0 `source-set-plan.md` or generated section listing candidate sources, inclusion decision, expected pages, and token budget. |
| 5 | Create a real manual-vs-skill KB comparison protocol | 86 | The test report says the skill-test KB is smaller and valid enough for comparison, but semantic comparison was not done. | Add a comparison prompt/template that scores manual baseline vs skill KB on coverage, fidelity, retrieval, traceability, and applied usefulness. |
| 6 | Introduce page-class budgets to avoid wiki sprawl | 84 | Future KBs can explode into too many concept pages. V1 created a small coherent page set; keep that discipline. | Define defaults: `source_summary_per_source`, `concept_page_only_if_reused`, `fusion_page_only_if_multi_source`, `entity_page_only_if durable named actor/tool`. |
| 7 | Promote `source_storage_mode` into script outputs | 82 | The repair added source modes to docs, but preflight/report output should make source mode explicit. | Add `--source-storage-mode` to preflight and manifest commands, with defaults and validation. |
| 8 | Add claim-density and redundancy checks | 80 | V2 should reduce pages that are verbose but low-signal. | Script can count headings, YAML blocks, source refs, claim IDs, backlinks, and applied cards; LLM can rate redundancy separately. |
| 9 | Add query-performance smoke tests | 78 | The whole value of the KB is fast future retrieval. Current tests validate files, not answer quality. | Create 5 canned query prompts per KB and require answers from index + minimal page set. |
| 10 | Add cross-KB source pointer policy | 76 | The first test used therapy raw notes as sources for a separate test KB. This pattern is useful, but needs lifecycle rules. | Define `same_repo_pointer` vs `copied_snapshot` and stale-source behavior. |
| 11 | Add `apex-kb` rebuild/update workflow | 74 | V1 scaffolded and ingested, but repeat ingestion when source changes needs clearer workflow. | Add update rules: changed source hash → re-run Phase 1, mark stale pages, preserve old notes until accepted. |
| 12 | Add a compact operator review surface | 72 | Current Phase 1 files are useful but long. Operator review should be faster. | Require a top `operator_review_card` with approve/reject/partial decisions, page plan, and risks. |
| 13 | Add manifest-derived coverage dashboard | 70 | Manifest already maps sources to pages; V2 can expose coverage without reading every file. | Generate `coverage_report` from manifest: sources without pages, pages without sources, review flags by source. |
| 14 | Formalize “applied card” as optional not universal | 68 | Applied cards are high-value for therapeutic/process KBs, but not every concept needs them. | Add `applied_card_required_when: operator_actionable_concept | self_work | process_rule`; otherwise optional. |
| 15 | Separate canonical KB package from test KB artifacts | 66 | The branch contains package fixes plus test output; next chat should avoid confusing test artifacts with package design. | Decide merge strategy: package repair branch vs test artifact branch, or archive test KB under `apex-meta/kb/_tests/`. |

## 6. Compacting recommendations

```yaml
compacting_recommendations:
  skill_entrypoint:
    current_issue: "Readable after repair, but still contains deep policy that can live in references."
    v2_target: "Routing kernel with minimal contract and procedure."
    keep_in_skill_md:
      - trigger description
      - modes
      - hard boundaries
      - support-file map
      - 6_to_8_step procedure
      - completion gate summary
    move_to_references:
      - source storage policy details
      - epistemic labels
      - phase rules
      - query rules
      - lint/audit details

  templates:
    current_issue: "Good explicitness but templates are long."
    v2_target: "Small canonical frontmatter plus modular body blocks."
    proposal:
      - one shared frontmatter template
      - one summary body block
      - one concept body block
      - one entity body block
      - one optional applied-card block
      - one optional contradiction block

  phase_1_analysis:
    current_issue: "High-value but potentially long for every source."
    v2_target: "Two-level Phase 1: review card first, full extraction below."
    required_top_card:
      - source_id
      - include_decision
      - proposed_pages
      - top_claims
      - risks
      - operator_decision_needed

  wiki_pages:
    current_issue: "V1 page quality is good, but future KBs risk uncontrolled page proliferation."
    v2_target: "Page budgets and creation thresholds."
    thresholds:
      concept_page: "Only if concept appears in at least one source and will be reused."
      fusion_page: "Only if synthesis spans two or more sources and requires explicit uncertainty handling."
      entity_page: "Only if durable actor/tool/project/file/artifact appears repeatedly."
```

## 7. High-impact extensions to consider

```yaml
extensions:
  E1_quality_command:
    type: deterministic_plus_llm
    impact: very_high
    owner: python_for_structure_llm_for_semantics
    output: apex-meta/kb/<kb-slug>/log/quality-report-YYYYMMDD.md

  E2_source_set_plan:
    type: llm_planning_artifact
    impact: high
    owner: llm
    output: apex-meta/kb/<kb-slug>/ingest-analysis/source-set-plan.md

  E3_coverage_report:
    type: deterministic
    impact: high
    owner: python
    output: command_output_or_log_file

  E4_query_eval_pack:
    type: test_artifact
    impact: high
    owner: llm_generates_questions_python_checks_file_presence
    output: apex-meta/kb/<kb-slug>/outputs/queries/evals/

  E5_update_reingest_policy:
    type: workflow_rule
    impact: medium_high
    owner: package_reference_plus_python_hash_check
    output: new section in ingest rules and script contract
```

## 8. Proposed next-chat mission

```markdown
# Apex KB v2 Planning Chat — Prompt

You are planning the next version of the Apex KB skill package. Do not rewrite package files yet.

Load the repaired branch files and the first skill-test KB artifacts. Treat the latest repaired package as the current baseline. Treat previous pre-repair drafts as historical context only.

Your task:
1. Verify what V1 now solves after the repair commit.
2. Identify what should be compacted, moved, removed, or promoted to script validation.
3. Rank proposed V2 changes using the metric system in `apex-meta/handoff/apex-kb-v2-planning-handover.md`.
4. Produce a V2 package-change plan with three tiers:
   - must_patch_before_second_full_test
   - should_patch_after_second_test
   - defer_until_real_multi_kb_use
5. Do not generate final replacement files unless explicitly requested.

Primary files to read:
- `.claude/skills/apex-kb/SKILL.md`
- `.claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md`
- `.claude/skills/apex-kb/templates/wiki-page-templates.md`
- `apex-meta/kb/apex-kb-skill-test/test-run-report.md`
- `apex-meta/kb/apex-kb-skill-test/manifests/source-manifest.json`
- `apex-meta/kb/apex-kb-skill-test/wiki/index.md`

Output:
- one ranked table
- one compact V2 architecture proposal
- one test plan for `apex-kb-skill-test-v2`
- one explicit list of files to patch and files not to touch
```

## 9. Recommended second full test

```yaml
second_test:
  branch: test/apex-kb-skill-package-v2
  kb_slug: apex-kb-skill-test-v2
  source_set:
    required:
      - apex-meta/kb/therapy/raw/notes/ET-Heller-NARM.md
      - apex-meta/kb/therapy/raw/notes/shadow_insight_v1.md
      - apex-meta/kb/therapy/raw/notes/PsychologicalHandover_ChatTherapeuticFramework_inACIM.md
    expanded:
      - apex-meta/kb/therapy/raw/notes/Psychological_Handover_Medical_Grade_v1.md
      - apex-meta/kb/therapy/raw/notes/MyTherapy.md
  compare_against:
    - apex-meta/kb/apex-kb-skill-test/
    - apex-meta/kb/therapy/wiki/
  success_metrics:
    - fewer_or_no_contract_warnings
    - source_storage_mode_explicit_in_manifest
    - confidence_and_claim_label_valid_everywhere
    - Phase_1_review_cards_present
    - machine_index_valid
    - lint_passes
    - audit_passes
    - query_eval_answers_use_index_first
    - page_count_justified_by_page_budget
```

## 10. Do-not-do list for next chat

```yaml
do_not_do:
  - Do not create a new KB architecture from scratch.
  - Do not re-open public blueprint research unless explicitly requested.
  - Do not treat the first manual therapy KB as canonical package behavior.
  - Do not expand files just to make the package feel complete.
  - Do not merge applied-card requirements into every concept by default.
  - Do not add scripts for semantic synthesis.
  - Do not patch files before producing the ranked V2 plan.
```
