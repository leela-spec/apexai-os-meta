# Apex KB Phase 2 Target-Oriented Codex Handover

## 0. Purpose

This handover defines how Codex must repair and simplify Apex KB Phase 2 so the system executes the operator's intended workflow rather than stopping after one bounded semantic packet or optimizing for structural compliance.

The target is not a larger control system. The target is a smaller, clearer, end-to-end execution path that reliably produces useful compiled knowledge.

```yaml
repository: leela-spec/apexai-os-meta
branch: main
execution_mode: inspect_live_repo_then_modify_directly
primary_package: apex-meta/apex-kb-cli
current_run_root: apex-meta/kb/therapy-narm-personal-development
current_run_id: run-20260722T183018661588Z-03d9cf49be
first_phase2_commit: 05b5568f63db709df4c4d07843f57d05368910c8
first_phase2_result: apex-meta/kb/therapy-narm-personal-development/runs/run-20260722T183018661588Z-03d9cf49be/incoming/phase2-narm-model-and-core-needs-a01.json
required_operating_principle: target_oriented_execution_over_control_theater
```

This document is both:

1. a current-state diagnosis;
2. a concrete implementation and execution brief for Codex.

Do not create a branch or pull request. Work on `main`, commit, and push `origin main`.

---

## 1. Operator-defined process

The operator's intended process is:

```yaml
operator_process:
  run_scope: complete_the_whole_configured_apex_kb_run
  interaction:
    ask_for_approval: false
    stop_after_each_file: false
    ask_questions_between_topics: false
    wait_for_operator_to_reprompt: false
  semantic_unit:
    phase1: one_result_per_topic
    phase2: one_result_per_topic
  phase2_topic_count_for_current_run: 5
  phase2_result_commits:
    rule: one_incoming_phase2_json_per_commit_and_push
    continue_after_push: immediately
  outer_loop:
    - inspect_current_cli_status
    - execute_or_import_current_packet
    - advance_cli
    - execute_next_packet
    - repeat_until_terminal
  reports:
    allowed: brief_progress_output
    must_not_interrupt_execution: true
```

The critical distinction is:

> A bounded semantic task packet limits what the semantic worker may write. It does not authorize the outer executor to stop the full run.

The outer executor must keep invoking the lifecycle, generating the next packet, executing it, importing it, and advancing until the run reaches its configured terminal state.

For this run, the configured output is `query_ready`. The run is not complete after one Phase 2 JSON, one topic, one rendered dossier, or one commit.

---

## 2. Current run inventory

The current configuration defines five topics:

```yaml
topics:
  - narm-model-and-core-needs
  - personal-pattern-map
  - narm-personal-match-map
  - framework-integration
  - methods-and-development-operating-system
```

Therefore, the current run requires five Phase 2 semantic result JSON files:

```text
phase2-narm-model-and-core-needs-a01.json
phase2-personal-pattern-map-a01.json
phase2-narm-personal-match-map-a01.json
phase2-framework-integration-a01.json
phase2-methods-and-development-operating-system-a01.json
```

Each Phase 2 JSON is an input to the application. Each import deterministically renders two Markdown pages:

```text
wiki/concepts/<topic>.md
wiki/summaries/<topic>-source-atlas.md
```

The semantic worker directly writes one JSON file. The application owns the two Markdown projections and lifecycle state updates.

For the complete current run, the expected Phase 2 knowledge outputs are:

```yaml
semantic_input_results: 5
rendered_concept_dossiers: 5
rendered_source_atlases: 5
rendered_markdown_total: 10
```

The first semantic result exists in commit `05b5568f63db709df4c4d07843f57d05368910c8`. The current run state still identifies the first Phase 2 packet as active because the result has not yet been successfully imported through the CLI lifecycle.

---

## 3. What Apex KB currently does

### 3.1 CLI authority model

The live package currently defines the CLI as lifecycle authority. `apex-kb continue` performs exactly one legal action per invocation.

The lifecycle sequence is currently:

```yaml
current_lifecycle:
  - deterministic_corpus_intelligence
  - phase1_packet_per_topic
  - phase1_import_per_topic
  - phase2_packet_per_topic
  - phase2_import_per_topic
  - independent_acceptance_packet_per_topic
  - acceptance_import_per_topic
  - deterministic_postflight
  - retrieval_build_for_query_ready
  - completion_certificate
```

The relevant implementation is primarily in:

```text
apex-meta/apex-kb-cli/src/apex_kb/cli.py
apex-meta/apex-kb-cli/src/apex_kb/lifecycle.py
apex-meta/apex-kb-cli/src/apex_kb/semantic/engine.py
apex-meta/apex-kb-cli/src/apex_kb/schemas/
apex-meta/apex-kb-cli/src/apex_kb/templates/
```

### 3.2 Current Phase 2 packet contract

The current Phase 2 packet tells the worker to:

- produce one structured JSON result;
- populate one dossier and one source atlas inside that JSON;
- preserve all target questions;
- preserve every candidate exactly once in the atlas;
- cite only Phase 1-reviewed candidates and allowed pointers;
- write only to the declared incoming path;
- avoid changing lifecycle-owned files.

The application then validates and renders:

```text
wiki/concepts/<topic>.md
wiki/summaries/<topic>-source-atlas.md
```

This write boundary is correct for the semantic worker.

The execution failure is that the surrounding process did not continue after the worker result was committed.

### 3.3 Current one-action continuation model

`apex-kb continue` currently executes one action and returns. This is mechanically safe but operationally too granular for an autonomous executor.

The current operator guide says to repeat `continue`. In practice, this created ambiguity:

```yaml
ambiguity:
  packet_rule: do_not_select_the_next_lifecycle_stage
  worker_interpretation: stop_the_entire_run
  intended_meaning: do_not_mutate_or_guess_lifecycle_state_inside_the_worker_result
```

The CLI needs an explicit outer-driving surface so an executor can continue automatically without interpreting packet wording as a global stop condition.

---

## 4. First Phase 2 test: what worked

The first result demonstrated that the basic data route is viable.

```yaml
first_test_strengths:
  - correct_phase2_schema_identifier
  - correct_run_and_task_identity
  - correct_topic_identity
  - locked_target_questions_present
  - macro_meso_micro_fields_present
  - key_claims_present
  - source_atlas_contains_nine_candidates
  - dossier_and_atlas_routes_present
  - output_written_to_the_declared_incoming_path
  - one_semantic_result_file_committed_alone
```

The first result also showed that a semantic worker can derive a compact dossier from accepted Phase 1 material.

However, these are shell and routing successes. They do not prove that the result is importable or that the rendered page meets the intended knowledge value.

---

## 5. First Phase 2 test: concrete defects

### 5.1 The result is likely not importable under the live citation validator

The Phase 2 importer validates every citation pointer against the pointer list preserved in the corresponding Phase 1 `source_review`.

The first Phase 2 result cites pointers including:

```text
src-c2fb4d779264e00e:line:335
src-c2fb4d779264e00e:line:431
src-c2fb4d779264e00e:line:287
src-c2fb4d779264e00e:line:5583
src-c2fb4d779264e00e:line:5587
```

The Phase 1 topic analysis itself used several of these citations in `topic_analysis.target_answers`, but the same source's `source_review.pointers` does not preserve all of them.

This means:

```yaml
first_result_validation_reality:
  json_schema_validation: may_pass
  identity_validation: may_pass
  atlas_count_validation: may_pass
  full_cli_import_validation: expected_to_fail_on_citation_pointer_invalid
```

The earlier statement that the first file had fully passed validation was therefore too strong. It appears to have passed structural inspection, not the live `import_phase2_result` path.

This is not merely a bad Phase 2 draft. It exposes a Phase 1 contract defect:

> Phase 1 can emit target-answer citations that are not included in the canonical source-review pointer ledger later enforced by Phase 2.

The pipeline must reject that inconsistency during Phase 1 import rather than allowing it to become a downstream Phase 2 failure.

### 5.2 The atlas is LLM-generated duplication of deterministic Phase 1 data

The Phase 2 importer requires atlas fields to exactly match the Phase 1 source review:

```yaml
exact_match_fields:
  - repository_path
  - disposition
  - read_status
  - individual_value
  - authority
  - freshness
  - duplicate_or_supersession
  - pointers
  - questions_supported
  - content_snapshot_equals_phase1_summary
```

Because these fields are exact copies, asking the LLM to reproduce the atlas is unnecessary.

It creates:

- token waste;
- copying risk;
- ordering noise;
- avoidable schema failures;
- no new semantic value.

The source atlas should be generated deterministically from Phase 1 by the application. The LLM should only provide genuinely semantic additions, such as source priority, why a source matters for a specific claim, or when to reopen it.

### 5.3 Macro, Meso, and Micro are structurally present but semantically compressed

The first result uses a single short paragraph for each abstraction level. It is coherent but too thin for the configured `deep` semantic depth and the broad topic.

The result should have created distinct value:

```yaml
macro:
  should_answer:
    - why_the_topic_matters
    - what_larger_decision_or_understanding_it_supports
    - what_the_model_is_and_is_not

meso:
  should_answer:
    - concept_relationships
    - mechanisms
    - distinctions
    - model_structure
    - crosslinks

micro:
  should_answer:
    - precise_terms
    - methods
    - edge_cases
    - operational_implications
    - exact_evidence
```

The current schema only enforces non-empty strings. It does not encode the intended page value.

### 5.4 The current schema omits important Phase 2 value fields

Earlier Apex KB design work defined a stronger page-value contract, including:

- adaptive ranked source set;
- route by question;
- raw-source reopen triggers;
- related pages / next reads;
- explicit source relevance;
- uncertainty and contradiction handling.

The live `phase2-result.schema.json` does not require these fields.

The renderer therefore cannot produce them consistently.

The system currently says it wants query-useful durable pages, while the schema primarily asks for:

```yaml
current_dossier_shell:
  - executive_summary
  - macro
  - meso
  - micro
  - target_answers
  - key_claims
  - evolution
  - contradictions
  - uncertainties
```

This is insufficient for routing and durable reuse.

### 5.5 Evidence-state language encourages fabricated category coverage

The task says:

> Preserve present, proposed, historical, open, and contradicted states.

The first result appears to have supplied at least one claim in every state, including weak or artificial uses such as:

- using `contradicted` for a framework-boundary statement;
- using `historical` for versioned personal notes even when that state adds little value to the topic.

The correct rule is:

```yaml
evidence_state_rule:
  preserve_states_that_are_present_in_phase1: true
  fabricate_one_claim_per_enum_value: false
  require_all_enum_values_on_every_page: false
```

The enum should remain available, but the task must explicitly prohibit manufacturing claims to satisfy category coverage.

### 5.6 Contradictions are conflated with boundaries and non-equivalence

The first result says other frameworks are not interchangeable with NARM and labels this as a contradiction.

That is mainly a source boundary, not necessarily a contradiction.

Phase 2 needs separate concepts:

```yaml
semantic_distinctions:
  contradiction: two_supported_claims_that_cannot_both_hold_as_stated
  tension: frameworks_or_sources_emphasize_different_assumptions
  boundary: a_source_cannot_support_a_specific_kind_of_claim
  uncertainty: evidence_is_incomplete_or_ambiguous
  open_question: unresolved_question_for_future_work
```

The schema should not force all of these into `contradictions`.

### 5.7 Some wording overstates evidence

The first result uses language such as `Validated principles` even though the primary evidence is a configured NARM theory source and personal/contextual material.

Use source-accurate wording:

```yaml
preferred_wording:
  - the_source_describes
  - within_the_narm_model
  - the_phase1_review_supports
  - the_personal_source_reports

avoid_without_evidence:
  - validated
  - proven
  - clinically_established
  - confirmed_for_the_operator
```

### 5.8 Generic safety language should not replace topic value

The current run has legitimate medical and psychological boundaries. Those boundaries should remain where the topic contract explicitly requires them.

They should not expand into generic safety boilerplate on every page or become a reason to avoid useful synthesis.

```yaml
safety_boundary_policy:
  include_when:
    - target_query_requires_it
    - source_contains_specific_boundary
    - output_could_reasonably_be_used_as_action_guidance
  do_not_use_as:
    - semantic_filler
    - substitute_for_answering_the_question
    - separate_control_layer
```

### 5.9 One-line JSON is poor for repository review

The first file is a single very long JSON line. It is valid but produces an unusable Git diff.

Phase result files should be written as stable, indented UTF-8 JSON with deterministic key ordering where practical.

---

## 6. Root causes

```yaml
root_causes:
  target_contract_gap:
    description: phase2_schema_checks_presence_but_not_the_intended_knowledge_value

  duplicated_responsibility:
    description: llm_is_asked_to_copy_an_atlas_the_application_can_build_exactly

  phase1_phase2_evidence_mismatch:
    description: phase1_target_answers_can_cite_pointers_missing_from_source_review_pointer_ledgers

  continuation_granularity:
    description: one_action_per_continue_requires_an_outer_loop_but_no_first_class_outer_driver_exists

  packet_scope_ambiguity:
    description: worker_write_boundary_was_misread_as_end_to_end_stop_instruction

  acceptance_overengineering:
    description: separate_evaluator_and_repair_state_add_complexity_without_first_fixing_the_page_target

  proxy_success:
    description: schema_fields_file_count_and_commit_success_were_treated_as_semantic_completion
```

---

## 7. Required design principles

### 7.1 Target before controls

The first question is:

> What durable answer should this page make possible that would otherwise require reopening and rereading the source set?

Only after that target is explicit should the schema and deterministic checks be designed.

### 7.2 Deterministic code owns mechanics

Python should own:

- run identity;
- paths;
- topic enumeration;
- candidate enumeration;
- exact source metadata;
- atlas projection;
- schema validation;
- citation membership;
- route identity;
- state transitions;
- readable JSON formatting;
- retrieval construction.

### 7.3 The LLM owns meaning

The semantic worker should own:

- synthesis;
- claim formulation;
- answer construction;
- conceptual relationships;
- practical implications;
- source relevance explanation;
- uncertainty articulation;
- route-by-question guidance;
- raw-source reopen conditions.

### 7.4 Do not add an evaluator to compensate for an undefined target

A separate semantic verifier is not the current priority.

The default path should not require:

- a second LLM context;
- independent acceptance packets;
- creator/evaluator identity comparison;
- repeated repair cycles based on subjective scoring.

First make the task contract and output shape generate the desired artifact directly.

### 7.5 Keep validation narrow and mechanical

Useful deterministic checks include:

- exact query coverage;
- valid source IDs;
- valid preserved pointers;
- no duplicate claims when claim IDs are used;
- required routes;
- non-empty substantive fields;
- deterministic atlas completeness;
- no source or lifecycle mutation by the worker.

Do not implement semantic quality scoring in Python.

### 7.6 One autonomous run surface

The user should be able to instruct Codex once and have it run through the full lifecycle without repeated manual prompts.

---

## 8. Recommended target lifecycle

The default lifecycle should become:

```yaml
target_lifecycle:
  - phase0_corpus_intelligence
  - phase1_semantic_analysis_per_topic
  - phase2_semantic_compile_per_topic
  - deterministic_postflight
  - retrieval_build_if_query_ready
  - completion
```

The separate acceptance stage should be removed from the default path.

For compatibility, it may remain as an optional mode:

```yaml
optional_acceptance:
  config_key: run_options.semantic_acceptance
  allowed_values:
    - disabled
    - optional
    - required
  default: disabled
```

Do not make this configuration more elaborate than necessary. If maintaining the old state schema is cheaper, treat existing acceptance slots as `not_required` when disabled.

---

## 9. Recommended Phase 1 changes

### 9.1 Establish one canonical evidence ledger

Each source review should contain the complete pointer set allowed for later citation.

Any pointer used by:

- source capsule claims;
- topic analysis claims;
- target answers;
- contradictions;
- uncertainties;

must be present in that source review's canonical pointer ledger.

### 9.2 Validate Phase 1 citations at Phase 1 import

Add Phase 1 import validation so every target-answer citation:

1. references a candidate in the topic;
2. references a non-blocked source;
3. uses a pointer preserved in that source review.

This prevents a valid-looking but unusable Phase 1 artifact from generating an impossible Phase 2 task.

### 9.3 Normalize citation representation

Phase 1 currently uses citation strings such as:

```text
src-c2fb4d779264e00e:line:181
```

Phase 2 uses objects:

```json
{"source_id": "src-c2fb4d779264e00e", "pointer": "line:181"}
```

Use one structured citation model in both phases.

Recommended form:

```json
{
  "source_id": "src-c2fb4d779264e00e",
  "pointer": "line:181"
}
```

### 9.4 Give claims stable IDs where useful

For broad deep runs, Phase 1 may optionally produce a claim ledger:

```yaml
claim:
  claim_id: narm-core-needs-001
  text: NARM identifies five biologically grounded core needs.
  state: present
  citations:
    - source_id: src-c2fb4d779264e00e
      pointer: line:181
  supports_queries:
    - narm-q01
```

Do not require IDs for trivial capsule statements. Use them for material topic-level evidence that Phase 2 should reuse.

---

## 10. Recommended Phase 2 packet and schema

### 10.1 Stop asking the LLM to reproduce the full source atlas

The packet should contain a deterministic atlas seed or no atlas field at all.

Preferred implementation:

```yaml
phase2_worker_output:
  required:
    - identity
    - dossier
  not_llm_owned:
    - atlas

phase2_import:
  - validate_dossier
  - generate_atlas_from_phase1_source_reviews
  - render_dossier
  - render_atlas
```

If the result schema must remain backward compatible, allow an omitted atlas and generate it. Remove the requirement in the next schema version.

### 10.2 Make the semantic target explicit in the packet

Add a compact `page_contract` to the Phase 2 task:

```yaml
page_contract:
  page_purpose: exact_one_sentence_target
  target_queries: locked
  required_value:
    - answer_queries_directly
    - synthesize_across_relevant_sources
    - distinguish_source_fact_inference_and_hypothesis
    - explain_source_relevance
    - provide_routing_and_raw_source_triggers
  non_goals:
    - restate_phase1_generic_summary
    - copy_atlas_metadata
    - fabricate_evidence_states
    - add_generic_safety_boilerplate
```

### 10.3 Replace single-string Macro/Meso/Micro with useful structured content

Keep the three abstraction levels, but allow sections or paragraphs rather than one compressed string.

Recommended schema shape:

```yaml
dossier:
  route: string
  title: string
  page_purpose: string
  executive_summary: string
  macro:
    significance: string
    scope_and_boundaries: string
  meso:
    mechanisms: array[string]
    relationships: array[string]
    distinctions: array[string]
  micro:
    operational_points: array[string]
    edge_cases: array[string]
    implementation_or_practice_implications: array[string]
  target_answers: array
  key_claims: array
  ranked_sources: array
  route_by_question: array
  source_boundaries: array[string]
  contradictions: array[string]
  tensions: array[string]
  uncertainties: array[string]
  raw_source_triggers: array
  evolution: array[string]
```

Do not make every array mandatory when the topic does not need it. The schema should support the value contract without forcing filler.

### 10.4 Add an adaptive ranked source set

The ranked source set is semantic because it explains why a source matters.

```yaml
ranked_source:
  source_id: required
  priority: primary | supporting | contextual | incidental
  why_relevant: required
  supports:
    - query_id_or_claim_id
  reopen_raw_source_when: string_or_null
```

Do not use a fixed source count. Include every source that materially changes the answer; exclude incidental sources from the ranked set while preserving them in the deterministic atlas.

### 10.5 Add route-by-question

Each locked query should have a durable route entry:

```yaml
route_entry:
  query_id: exact_locked_id
  start_here: dossier_section_or_heading
  next_reads: array[route]
  raw_source_needed: no | conditional | yes
  reopen_when: string_or_null
```

This makes the compiled KB useful for retrieval and future AI synthesis.

### 10.6 Separate contradiction, tension, boundary, uncertainty, and open question

Do not force every topic to contain every category.

### 10.7 Preserve evidence states without fabricating coverage

Task wording must say:

```text
Preserve evidence states present in accepted Phase 1 material. Do not create claims merely to populate every allowed state.
```

### 10.8 Include an explicit allowed citation map

The Phase 2 packet should expose:

```yaml
allowed_citations:
  src-c2fb4d779264e00e:
    - line:3
    - line:181
    - line:187
```

This should be generated from validated Phase 1 reviews and used by both worker and importer.

### 10.9 Write readable JSON

All semantic result files should use:

- UTF-8;
- two-space indentation;
- stable key ordering where practical;
- final newline.

---

## 11. Recommended renderer changes

The concept dossier renderer should create stable headings:

```text
# <Title>
## Purpose
## Executive summary
## Macro — Why this matters
## Meso — Model, mechanisms, and relationships
## Micro — Operational detail
## Direct answers
## Key claims
## Ranked sources
## Route by question
## Source boundaries
## Contradictions and tensions
## Uncertainty and open questions
## Raw-source reopen triggers
## Evolution and versions
## Routes
```

The source atlas renderer should remain deterministic and preserve every candidate exactly once.

The atlas should not pretend every source is equally important. It is an inventory and evidence map, not the semantic priority list. Priority belongs in the dossier's ranked source section.

---

## 12. Recommended autonomous CLI surface

### 12.1 Keep `continue` for one-step debugging

Do not break the existing command:

```powershell
apex-kb continue --run-root <path>
```

### 12.2 Add an outer driver command

Add a command such as:

```powershell
apex-kb drive --run-root <path>
```

Its behavior:

```yaml
drive_behavior:
  loop:
    - derive_next_action
    - execute_deterministic_actions_automatically
    - import_present_semantic_results_automatically
    - stop_only_when_semantic_worker_input_is_required_or_run_is_terminal_or_blocked
  output:
    - compact_machine_readable_next_action
    - exact_packet_dir
    - exact_expected_output_path
    - terminal_state_when_complete
```

This command does not call an external LLM. Codex remains the semantic worker. The command removes repeated manual `continue` invocations and makes the outer loop explicit.

Alternative acceptable name:

```text
apex-kb advance --until semantic_wait|terminal
```

Choose one simple public interface, not both.

### 12.3 Provide a compact JSON contract for Codex

When semantic work is required, return:

```json
{
  "status": "semantic_task_required",
  "task_kind": "phase2",
  "topic_id": "personal-pattern-map",
  "packet_dir": "...",
  "expected_output_path": "...",
  "next_command_after_write": "apex-kb drive --run-root ..."
}
```

Do not make Codex infer the next command from prose.

### 12.4 Clarify packet wording

Replace:

```text
Do not select the next lifecycle stage.
```

with:

```text
This result file must not mutate or choose lifecycle state. After writing the result, the outer executor must immediately return control to the Apex KB CLI and continue the run.
```

This preserves the write boundary while removing the stop ambiguity.

---

## 13. Git execution policy for the current run

The operator requires one semantic result file per commit and push.

Use this exact policy:

```yaml
git_policy:
  branch: main
  semantic_result_commit:
    stage: only_the_new_incoming_json
    commit: one_file_only
    push: origin_main_immediately
  unrelated_or_cli_generated_changes:
    block_execution: false
    stage_during_semantic_result_commit: false
  final_lifecycle_commit:
    after_terminal_or_before_final_push: true
    includes:
      - imported_semantic_results
      - rendered_wiki_pages
      - run_state
      - stage_results
      - generated_task_packets
      - postflight
      - retrieval
      - completion_certificate
```

This preserves one file per semantic push while allowing the local CLI to maintain uncommitted application-owned state between semantic iterations.

Do not stop because unrelated or generated files are dirty. Stage only the intended semantic result file for each semantic commit.

Suggested semantic commit messages:

```text
Add NARM Phase 2 model dossier result
Add personal pattern Phase 2 result
Add NARM personal match Phase 2 result
Add framework integration Phase 2 result
Add development operating system Phase 2 result
```

Suggested final deterministic commit:

```text
Finalize NARM personal development KB run
```

---

## 14. Current-run repair and continuation plan

### Step 1 — Reproduce the first import failure

Run the installed CLI against:

```text
C:\GitDev\apexai-os-meta\apex-meta\kb\therapy-narm-personal-development
```

Use the public command only.

Expected result under current code: the first Phase 2 result should fail citation-pointer validation.

Record the exact failure. Do not manually advance state.

### Step 2 — Implement the minimal pipeline corrections

At minimum:

1. validate Phase 1 target-answer citations during Phase 1 import;
2. expose a canonical allowed citation map in Phase 2 packets;
3. deterministically generate the source atlas from Phase 1;
4. clarify Phase 2 task wording;
5. remove or disable acceptance in the default lifecycle;
6. add the autonomous outer driver command;
7. update schema and renderer to encode route-by-question, ranked sources, and raw-source triggers;
8. write semantic JSON in readable format.

### Step 3 — Repair the first result

Repair the first Phase 2 result against the corrected contract.

The repaired dossier must:

- answer all three NARM questions directly;
- use only allowed pointers;
- distinguish NARM theory from personal application;
- define the five needs and corresponding capacities with adequate detail;
- explain adaptive survival structures, shame/counter-identification, regulation, contact, and trauma distinctions;
- include ranked source relevance;
- include route-by-question;
- include raw-source reopen triggers;
- avoid fabricated evidence-state coverage;
- avoid claiming validation not established by the source set.

Update the existing file only if the corrected schema remains compatible. Otherwise create a new attempt file through the lifecycle, such as `phase2-narm-model-and-core-needs-a02.json`.

Do not overwrite history outside supported lifecycle behavior.

### Step 4 — Run all remaining Phase 2 topics

Execute the remaining topics automatically:

```text
personal-pattern-map
narm-personal-match-map
framework-integration
methods-and-development-operating-system
```

For each topic:

1. obtain the packet from the CLI;
2. read all packet files;
3. produce the semantic result;
4. stage only that result file;
5. commit;
6. push `origin main`;
7. return to the CLI immediately;
8. continue without asking the operator.

### Step 5 — Complete deterministic lifecycle work

After all Phase 2 results are imported:

- run deterministic postflight;
- build retrieval;
- verify retrieval health;
- write completion evidence;
- commit all generated lifecycle artifacts;
- push `origin main`.

---

## 15. Targeted implementation files

Inspect and modify only files materially required for the target.

Likely files:

```text
apex-meta/apex-kb-cli/src/apex_kb/cli.py
apex-meta/apex-kb-cli/src/apex_kb/lifecycle.py
apex-meta/apex-kb-cli/src/apex_kb/semantic/engine.py
apex-meta/apex-kb-cli/src/apex_kb/schemas/phase1-result.schema.json
apex-meta/apex-kb-cli/src/apex_kb/schemas/phase2-result.schema.json
apex-meta/apex-kb-cli/src/apex_kb/schemas/run-config.schema.json
apex-meta/apex-kb-cli/src/apex_kb/schemas/run-state.schema.json
apex-meta/apex-kb-cli/src/apex_kb/templates/phase2-task.md
apex-meta/apex-kb-cli/README.md
apex-meta/apex-kb-cli/docs/OPERATOR-GUIDE.md
apex-meta/apex-kb-cli/tests/
```

Do not revive or patch legacy command surfaces unless a live import requires it:

```text
scripts/apex_kb.py
apex-meta/scripts/apex_kb_control.py
legacy skill-era orchestration files
```

The installed package under `apex-meta/apex-kb-cli` is authoritative.

---

## 16. Tests

Use targeted tests. Do not build a broad validation bureaucracy.

Required tests:

```yaml
tests:
  phase1_pointer_integrity:
    - target_answer_pointer_missing_from_review_is_rejected
    - valid_structured_citation_is_accepted

  phase2_atlas_generation:
    - atlas_is_generated_from_phase1_without_llm_copy
    - every_candidate_is_preserved_exactly_once

  phase2_state_preservation:
    - absent_evidence_states_are_not_required
    - existing_states_are_preserved

  phase2_value_contract:
    - locked_queries_are_present_once
    - ranked_sources_validate_against_candidate_ids
    - route_by_question_covers_locked_queries
    - raw_source_triggers_accept_conditional_entries

  lifecycle_drive:
    - deterministic_actions_loop_until_semantic_wait
    - present_semantic_result_is_imported_then_loop_continues
    - terminal_run_returns_terminal_status
    - disabled_acceptance_does_not_create_acceptance_packets

  readable_json:
    - semantic_result_writer_or_fixture_uses_indented_json
```

Run the smallest relevant test set first, then the package test suite once.

Recommended commands:

```powershell
python -m pip install -e ".\apex-meta\apex-kb-cli[test]"
pytest apex-meta/apex-kb-cli/tests -q
```

Do not repeatedly rerun unrelated suites.

---

## 17. Acceptance criteria

The implementation is complete only when all of the following are true:

```yaml
acceptance:
  process:
    - one_operator_instruction_can_drive_the_full_run
    - no_question_or_approval_is_required_between_topics
    - bounded_packet_scope_does_not_stop_the_outer_lifecycle
    - one_phase2_semantic_json_is_committed_and_pushed_per_topic

  current_run:
    - all_five_phase2_topic_results_exist
    - all_five_results_import_successfully
    - ten_markdown_pages_are_rendered
    - postflight_passes
    - retrieval_is_built_and_healthy
    - completion_json_exists
    - lifecycle_status_is_query_ready

  semantic_quality:
    - every_locked_query_is_directly_answered
    - no_invalid_citation_pointer_is_present
    - no_atlas_metadata_is_manually_copied_by_the_llm
    - macro_meso_micro_have_distinct_value
    - ranked_sources_explain_relevance
    - route_by_question_is_present
    - raw_source_reopen_triggers_are_present
    - theory_self_report_inference_and_hypothesis_are_distinguished
    - evidence_states_are_not_fabricated

  simplicity:
    - default_lifecycle_has_no_independent_acceptance_packet_stage
    - no_python_semantic_scoring_system_is_added
    - no_new_agent_or_role_architecture_is_added
    - no_security_or_verifier_layer_is_added_beyond_existing_mechanical_validation
```

---

## 18. Explicit non-goals

```yaml
non_goals:
  - build_a_multi_agent_review_system
  - add_an_llm_as_judge
  - add_security_boundary_theater
  - add_fixed_word_counts
  - add_page_value_scores
  - add_more_lifecycle_states_than_needed
  - create_a_new_skill_as_the_primary_runtime
  - require_operator_confirmation_between_topics
  - make_the_llm_copy_deterministic_metadata
  - treat_schema_success_as_semantic_success
  - redesign_retrieval_beyond_what_the_new_page_contract_needs
```

---

## 19. Codex execution instruction

```text
Repository: leela-spec/apexai-os-meta
Branch: main

Read this handover and inspect the live Apex KB CLI package, the current NARM run, commit 05b5568f63db709df4c4d07843f57d05368910c8, the first Phase 2 result, its Phase 1 analysis, task packet, schemas, renderer, lifecycle, tests, README, and operator guide.

Implement the smallest target-oriented repair described here.

Work directly on main. Do not create a branch or PR.

Run:
python -m pip install -e ".\apex-meta\apex-kb-cli[test]"
pytest apex-meta/apex-kb-cli/tests -q

Then resume the current NARM run. Produce and push one Phase 2 incoming JSON per semantic commit. Continue automatically through every remaining topic. Do not ask for approval. Do not stop after reports. Complete postflight, retrieval, and completion. Commit generated lifecycle artifacts in the final lifecycle commit.

Commit implementation changes with:
Simplify Apex KB Phase 2 execution

Push origin main.

Final report format:
- implementation commit SHA
- semantic result commit SHAs in order
- final lifecycle commit SHA
- changed files
- five Phase 2 result paths
- ten rendered Markdown paths
- test command and result
- final lifecycle status
- remaining blockers, or "none"
```

---

## 20. Final priority order

```yaml
priority_order:
  1: make_the_target_artifact_explicit
  2: repair_phase1_to_phase2_evidence_integrity
  3: remove_llm_copy_work
  4: make_the_outer_run_autonomous
  5: simplify_or_disable_acceptance
  6: complete_the_current_five_topic_run
  7: only_then_improve_secondary_docs_or_polish
```

The governing principle is:

> Make the shortest reliable path to a useful, source-grounded, query-ready knowledge base the default path. Do not substitute more control machinery for a better-defined target.
