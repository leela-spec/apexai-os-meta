# Pro Thinking Implementation Prompt — Complete the Final Operable Apex KB

## 0. Execution contract

```yaml
role:
  - senior Python application engineer
  - deterministic workflow and finite-state-machine architect
  - knowledge-system implementation lead
  - semantic-task contract designer
  - retrieval and test engineer

mode: one_continuous_implementation_run

primary_repository:
  full_name: leela-spec/apexai-os-meta
  target: continue_the_existing_Apex_KB_CLI_work
  current_candidate_pr: 10
  current_candidate_branch: agent/apex-kb-python-cli

canary_source_repository:
  full_name: leela-spec/leela
  source_root: LeelaAppDevelopment
  access: read_only

primary_result:
  - final_operable_Apex_KB_Python_application
  - completed_full_lifecycle
  - real_Leela_Skill_Tree_query_ready_canary
  - tested_ready_for_review_pull_request

repository_write:
  apexai_os_meta: allowed_on_the_selected_implementation_branch
  leela: prohibited

normal_public_interface:
  - apex-kb start
  - apex-kb continue
  - apex-kb status

additional_public_read_or_maintenance_surfaces:
  - apex-kb query
  - apex-kb update

specialist_commands:
  - allowed_when_needed
  - must_not_replace_the_simple_normal_flow
```

Use the highest available reasoning mode.

Think deeply, but report decisions, evidence, changes, and test results rather than exposing private reasoning.

Do not stop after research, feasibility analysis, architecture, planning, scaffolding, or unit tests. Inspect the existing implementation, complete the application, run product-level tests, and execute the real canary.

---

# 1. Mission

Complete the remaining functionality of the Apex KB Python CLI so it becomes a genuinely operable product rather than a limited vertical slice.

The final Apex KB must:

> Deterministically map the complete configured corpus, use bounded AI workers for meaning-based analysis and compilation, independently evaluate the resulting knowledge, build local retrieval over accepted pages, support incremental updates, and derive every lifecycle action from durable files.

The intended value is:

1. Every in-scope source is inventoried or explicitly excluded.
    
2. Every configured topic receives an exhaustive candidate map showing exactly why each source was surfaced.
    
3. AI reads the strongest evidence efficiently without losing complete source visibility.
    
4. Every candidate receives a durable semantic disposition.
    
5. Reusable source understanding is preserved by content hash.
    
6. Every topic produces an answer-bearing Macro/Meso/Micro dossier and a complete source atlas.
    
7. A fresh evaluator proves that routine questions can be answered from the compiled pages.
    
8. Accepted pages become locally searchable through deterministic retrieval.
    
9. Changed sources invalidate only affected knowledge.
    
10. A normal operator can run the lifecycle using a small command surface without understanding its internal stages.
    

This is the product target. Do not substitute a smaller target merely because it is easier to implement.

---

# 2. Current baseline

Start by resolving current repository truth.

## 2.1 Inspect the candidate implementation

Inspect PR #10 and its current head rather than relying on this prompt’s remembered commit.

Read completely:

```text
apex-meta/apex-kb-cli/pyproject.toml
apex-meta/apex-kb-cli/README.md
apex-meta/apex-kb-cli/src/apex_kb/cli.py
apex-meta/apex-kb-cli/src/apex_kb/core.py
apex-meta/apex-kb-cli/src/apex_kb/schemas/
apex-meta/apex-kb-cli/src/apex_kb/templates/
apex-meta/apex-kb-cli/tests/
.claude/skills/apex-kb/SKILL.md
```

Record:

```yaml
baseline:
  current_main_sha:
  current_pr_head_sha:
  branch_relation_to_main:
  existing_test_result:
  implemented_capabilities:
  incomplete_capabilities:
  defects_or_shortcuts_found:
```

Treat PR #10 as an implementation donor and candidate baseline, not unquestionable authority.

Preserve its sound foundation:

- installable `apex-kb` entrypoint;
    
- exact canonical Start template;
    
- independent source and destination roots;
    
- `run-config.yaml`;
    
- frozen `run-manifest.json`;
    
- canonical configuration hash;
    
- atomic `run-state.json`;
    
- file-only status and resume;
    
- deterministic inventory;
    
- semantic task packets;
    
- structural semantic-result import;
    
- thin optional Skill.
    

Correct or replace weak implementation where necessary.

## 2.2 Reconcile with current `main`

Compare the candidate branch with current `main`.

Do not automatically fetch, pull, reset, clean, stash, merge, rebase, or discard work.

If the branch is behind:

1. inspect the changed areas;
    
2. identify actual collisions;
    
3. incorporate required current-main changes deliberately;
    
4. preserve the CLI application as the one lifecycle authority.
    

Do not restart implementation from old scripts merely because they exist on `main`.

---

# 3. Source authority

## 3.1 Product and lifecycle authority

Read these Project Source files where available:

```text
Apex KB Python CLI.txt
NewPLanCodex.md
Apex KB Execution Model.txt
Apex-KB Redesign Guidance.txt
```

Read these repository sources selectively:

```text
FutureDevelopments&Research/
ProjectMM&Task&KB/KnowledgeBase/
ApexKBFinalDesignDeepResearch/
00-START-HERE.md

01-CURRENT-APEX-KB-FAILURE-ANALYSIS.md
02-LIFECYCLE-COMPONENT-VALUE-MAP.md
03-ARTIFACT-HANDOFF-TEMPLATES.md
04-Apex-KB-Current-Research-Index.md
05-Apex_KB_Current_Research_Index.machine-readable.yaml.md
06-LLM-WIKI-REPOSITORY-GUIDE.md
```

Use them for:

- final product value;
    
- whole-corpus intelligence;
    
- artifact interfaces;
    
- semantic source dispositions;
    
- concept dossiers;
    
- source atlases;
    
- acceptance;
    
- retrieval;
    
- maintenance.
    

Do not reproduce their old chat-orchestrator structures.

## 3.2 Existing runtime donors

Inspect only the functions that can materially reduce implementation effort:

```text
apex-meta/scripts/apex_kb.py
apex-meta/scripts/apex_kb_start.py
apex-meta/scripts/apex_kb_control.py
apex-meta/scripts/apex_kb_retrieval.py
```

Reuse good parsing, extraction, hashing, retrieval, validation, and fixture logic.

Do not preserve:

- competing command drivers;
    
- competing state owners;
    
- old public commands merely for compatibility;
    
- model-interpreted stage selection;
    
- old substring ranking;
    
- top-N truncation;
    
- duplicated schemas or templates.
    

Legacy scripts may become:

- internal donors;
    
- deprecated compatibility wrappers calling the package;
    
- or removable obsolete code.
    

They must not remain a parallel lifecycle authority.

---

# 4. Intent and feasibility lock

Before major edits, produce a concise internal decision table:

|Question|Required conclusion|
|---|---|
|Is the target a CLI application or Skill workflow?|CLI application; Skill optional and thin|
|Is complete deterministic corpus mapping feasible locally?|Verify, then implement|
|Can workflow state remain file-based?|Yes unless contradictory primary evidence appears|
|Is a workflow-state database required?|No|
|Is SQLite appropriate for derived retrieval?|Verify FTS5 availability; use it only as a rebuildable index|
|Is a GUI, MCP server, daemon, or workflow service required?|No|
|Can semantic work remain provider-neutral?|Yes, through task packets and validated imports|
|Can the complete lifecycle work without API credentials?|Yes, through manual packet mode|
|Are provider-specific adapters required for product completion?|No|
|Is a real Leela canary possible in the available runtime?|Resolve through connector access or temporary clones|
|What exact evidence proves operability?|Real lifecycle artifacts, semantic acceptance, retrieval results, resume proof, and source non-mutation|

This feasibility step must not become another research report.

If a detail is unresolved but nonblocking, choose the simplest reversible implementation and continue.

Ask the operator only when a contradiction would materially alter the product target or risk destructive writes.

---

# 5. Bounded web validation

Search the web before selecting dependencies or finalizing technical mechanisms.

## Rules

- Use no more than approximately twelve load-bearing sources.
    
- Prefer current official documentation and primary project documentation.
    
- Do not use web research to rediscover the Apex architecture.
    
- Research only implementation decisions that could have changed or affect portability.
    
- Record each adopted decision in the PR description or final report.
    
- Move directly from verification into implementation.
    

## Required validation topics

Use current official documentation for:

```yaml
web_validation:
  python_packaging:
    - pyproject project scripts
    - src layout
    - package data and importlib.resources

  click:
    - prompts and confirmations
    - command groups
    - exit codes
    - CliRunner transcript testing
    - Windows behavior

  schemas:
    - JSON Schema 2020-12
    - strict undeclared-property handling
    - schema versioning

  file_safety:
    - atomic replacement
    - pathlib and Windows path handling

  retrieval:
    - SQLite FTS5 runtime availability
    - MATCH queries
    - BM25 or rank ordering
    - snippet and highlight behavior
    - rebuild and integrity checks

  test_strategy:
    - pytest tmp_path
    - monkeypatch
    - isolated filesystem and subprocess tests

  source_extractors:
    - DOCX
    - PPTX
    - XLSX
    - text-based PDF
    - current license
    - Windows installability
    - stable pointer support

  semantic_adapter:
    - official provider documentation only if a provider-specific adapter is considered
```

Do not add a dependency merely because it is popular.

For every proposed dependency, assess:

```yaml
dependency_decision:
  purpose:
  standard_library_alternative:
  installability:
  Windows_support:
  license:
  maintenance_state:
  failure_behavior:
  accepted_or_rejected:
```

Prefer the smallest set that completes the required value.

---

# 6. Locked architecture

## 6.1 One lifecycle authority

The package under:

```text
apex-meta/apex-kb-cli/src/apex_kb/
```

is the only lifecycle authority.

It owns:

- configuration;
    
- templates;
    
- schemas;
    
- path derivation;
    
- manifests;
    
- state;
    
- legal transitions;
    
- deterministic stages;
    
- semantic packet creation;
    
- semantic imports;
    
- acceptance imports;
    
- retrieval;
    
- maintenance;
    
- completion.
    

The Skill does not own any of these.

## 6.2 State topology

Use:

```text
run-config.yaml
run-manifest.json
run-state.json
```

Rules:

- `run-config.yaml` is human editable before confirmation.
    
- `run-manifest.json` is frozen after confirmation.
    
- `run-state.json` is the only mutable lifecycle state.
    
- Every write is atomic.
    
- Every transition is schema validated.
    
- Every transition records a reason and artifact references.
    
- An interrupted run resumes from files in a fresh process.
    
- AI output never directly changes state.
    
- No workflow-state database.
    

## 6.3 Derived retrieval database

SQLite may be used only for rebuildable retrieval.

It is not canonical state.

Canonical knowledge remains:

- manifests;
    
- semantic analyses;
    
- accepted wiki pages;
    
- source atlases;
    
- acceptance records.
    

Delete the SQLite database and the application must be able to rebuild it completely.

## 6.4 Provider-neutral semantic execution

Mandatory execution mode:

```yaml
semantic_execution:
  manual_packet:
    required: true
    meaning: operator runs a packet with any capable AI and imports the declared result
```

Strongly preferred when safely implementable:

```yaml
semantic_execution:
  command_adapter:
    required: false
    meaning: invoke a configured local command with packet and output arguments
    safety:
      - argv_list_not_shell_string
      - shell_false
      - timeout
      - captured_exit_code_stdout_stderr
      - no_direct_state_access
```

Provider-specific APIs are optional convenience features and must not become product dependencies.

---

# 7. Final lifecycle

The application must support this complete sequence:

```text
START
  ↓
configuration and read-only preview
  ↓
operator confirmation
  ↓
manifest and initial state
  ↓
source custody and deterministic extraction
  ↓
whole-corpus intelligence
  ↓
Phase 1 source and topic semantic analysis
  ↓
Phase 2 concept dossier and source atlas
  ↓
independent semantic acceptance
  ↓
deterministic postflight
  ↓
retrieval rebuild
  ↓
query_ready
```

For an incremental run:

```text
UPDATE
  ↓
new source inventory
  ↓
source drift and impact map
  ↓
invalidate affected source capsules and topics only
  ↓
rerun affected semantic work
  ↓
reaccept affected pages
  ↓
rebuild affected retrieval
  ↓
query_ready
```

---

# 8. Required functionality

## 8.1 Complete deterministic corpus intelligence

Replace the simple inventory-only continuation with a real corpus-intelligence stage.

### Canonical inputs

The manifest must contain or deterministically derive:

```yaml
corpus_scope:
  source_roots:
  exclusions:
  output_root_exclusion:
  source_handling:
  non_text_policy:
  lifecycle_hint_rules:
  authority_hint_rules:

topic_registry:
  topics:
    - topic_id:
      name:
      primary_phrases:
      aliases:
      supporting_terms:
      negative_or_ambiguous_terms:
      target_queries:
      expected_dossier_path:
      expected_source_atlas_path:
```

Operator-defined path rules are hints only. They do not make semantic authority decisions.

### Required outputs

```text
manifests/source-inventory.ndjson
manifests/source-manifest.json
manifests/phase0/structure-map.ndjson
manifests/phase0/term-postings.ndjson
manifests/phase0/duplicate-map.json
manifests/phase0/topic-maps/<topic-id>.json
manifests/phase0/topic-maps/<topic-id>.md
manifests/phase0/phase0-navigation-report.md
```

### Inventory requirements

Every file beneath the source roots must have exactly one visible state:

```text
included
excluded_with_reason
unsupported_visible
unreadable_visible
```

Record at minimum:

- stable source ID;
    
- repository;
    
- source root;
    
- relative and resolved path;
    
- extension and media type;
    
- bytes;
    
- SHA-256;
    
- extraction status;
    
- extractor and version;
    
- filesystem timestamp where meaningful;
    
- Git last-change metadata where enabled;
    
- exclusion state and reason;
    
- source-handling state.
    

No file may disappear silently.

### Structure extraction

For supported text files, extract:

- title or H1;
    
- frontmatter;
    
- headings;
    
- section start and end lines;
    
- ordinary links;
    
- repository-relative file references;
    
- configured identifiers;
    
- parser warnings.
    

Use a simple deterministic parser first.

Add a heavier parser only when fixtures demonstrate a real failure.

### Term postings

For every configured phrase, alias, supporting term, and negative term, preserve separate signals for:

```text
path
filename
frontmatter_title
H1
heading
body
links
identifier_co_occurrence
```

Each posting must contain exact pointers.

Do not collapse all signals into one unexplained hit count.

### Topic maps

Each authoritative topic map must contain every deterministic candidate.

Never truncate the machine candidate set.

Bounded Markdown navigation views may show ranked groups, but the JSON map remains exhaustive.

Each row records:

- source ID;
    
- path;
    
- content hash;
    
- duplicate representative;
    
- source format;
    
- size;
    
- exact match signals;
    
- exact pointers;
    
- configured lifecycle or authority hints;
    
- deterministic candidate class;
    
- inspectable sort vector;
    
- no semantic relevance claim.
    

Candidate classes may include:

```text
direct
section_primary
dense_body
contextual
linked
duplicate
ambiguous
```

### Duplicate and version families

Implement:

- exact content-hash duplicates;
    
- normalized-text duplicate candidates;
    
- filename/version-family candidates;
    
- representative selection for reading efficiency.
    

Do not automatically declare a file superseded from path or filename alone.

That remains semantic work.

### Navigation report

`phase0-navigation-report.md` must be populated and useful.

Include:

- corpus coverage;
    
- extraction blockers;
    
- unsupported formats;
    
- duplicate families;
    
- topic coverage totals;
    
- direct and contextual groups;
    
- read-first source families;
    
- cross-topic reusable sources;
    
- recommended semantic batches;
    
- unresolved deterministic ambiguities.
    

An artifact list is not a navigation report.

---

## 8.2 Source formats

Required support:

|Format|Required behavior|
|---|---|
|Markdown, text, code|complete text and structural extraction|
|JSON, YAML, CSV|text plus appropriate structural keys/rows where practical|
|DOCX|paragraphs, tables where practical, stable paragraph/table pointers|
|PPTX|slide text, notes when supported, slide pointers|
|XLSX|sheet names, populated cells, cell coordinates|
|PDF|deterministic text extraction for text-based PDFs|
|Images/scans|inventory and metadata only by default|
|Unsupported|visible status and reason|

No OCR in the default lifecycle.

Extraction must be capability-gated and honest.

The configured policies must behave distinctly:

```text
inventory_and_report
extract_when_supported
block_on_unsupported
```

---

## 8.3 Source custody modes

Implement all configured modes.

### `pointer_only`

- leave source files in place;
    
- store repository identity, paths, commits where available, hashes, and extraction artifacts;
    
- never mutate source.
    

### `copy_into_kb`

- copy approved sources into the KB’s managed raw-source area;
    
- preserve original relative paths and provenance;
    
- verify copied hashes;
    
- never silently overwrite a differing file.
    

### `snapshot_copy`

- create an immutable run-specific source snapshot;
    
- record snapshot timestamp and manifest;
    
- verify every copied hash;
    
- preserve previous snapshots.
    

All modes feed the same later corpus-intelligence contract.

---

## 8.4 Multi-topic lifecycle scheduling

Support any number of configured topics.

The state must record topic-level progression without duplicating lifecycle authority.

Example:

```json
{
  "topics": {
    "skill-tree": {
      "phase1": "pending",
      "phase2": "pending",
      "acceptance": "pending"
    }
  }
}
```

The application must deterministically derive the one legal next action.

It may schedule work:

- one topic at a time;
    
- one bounded source batch at a time;
    
- or one reusable source-capsule task at a time.
    

The strategy must be deterministic and restartable.

It must support source reuse across topics.

---

## 8.5 Phase 1 semantic analysis

Implement two durable semantic layers.

### Reusable source capsule

```text
ingest-analysis/sources/<source-hash>.analysis.md
```

Create it for unique, materially relevant sources that were actually reviewed.

A source capsule records:

- source identity and hash;
    
- review mode;
    
- source limitations;
    
- one-sentence snapshot;
    
- material knowledge by section;
    
- authority and freshness assessment;
    
- current/proposed/historical/prototype state;
    
- contradictions and dependencies;
    
- topic contributions;
    
- exact evidence pointers.
    

Unchanged source hashes reuse valid capsules.

### Topic analysis

```text
ingest-analysis/topics/<topic-id>.analysis.md
```

It records:

- target-query coverage;
    
- every Phase 0 candidate exactly once;
    
- review mode;
    
- disposition;
    
- one-sentence content snapshot;
    
- individual value to the topic;
    
- authority/freshness judgment;
    
- contradiction and supersession relationships;
    
- exact pointers;
    
- proposed page topology;
    
- completion blockers.
    

Allowed dispositions include:

```text
core_current
supporting_current
implementation
prototype
historical
contextual
incidental
duplicate
superseded
irrelevant_after_review
blocked_unreadable
```

A filename, rank, or path is never evidence that the source contains a claim.

Unopened sources cannot be cited as evidence.

---

## 8.6 Phase 2 compilation

For a broad topic, compile:

```text
wiki/concepts/<topic-id>.md
wiki/summaries/<topic-id>-source-atlas.md
```

### Concept dossier

The concept dossier must provide:

1. direct current-state answer;
    
2. Macro explanation — why the concept exists and what value it creates;
    
3. Meso explanation — architecture, components, relationships, and workflows;
    
4. Micro explanation — concrete mechanics, fields, states, interfaces, and behavior;
    
5. current implementation versus target specification;
    
6. prototype and historical evolution;
    
7. contradictions and unresolved decisions;
    
8. related concept routes;
    
9. exact source pointers;
    
10. source-atlas route.
    

### Source atlas

The atlas must preserve every Phase 0 candidate.

For each candidate:

- source identity and path;
    
- date/version evidence;
    
- review mode;
    
- semantic disposition;
    
- one-sentence individual snapshot;
    
- individual value;
    
- authority and freshness;
    
- duplicate or supersession relationship;
    
- exact relevant sections;
    
- whether it was used as evidence;
    
- blocker status where applicable.
    

Every candidate appears exactly once.

For a genuinely small topic, the atlas may be embedded in the dossier only when that reduces duplication without losing source-level value.

---

## 8.7 Independent semantic acceptance

Generate a separate acceptance task for each topic.

The evaluator must be a fresh context that did not draft the pages.

Inputs:

- locked target questions;
    
- exact compiled pages;
    
- exact source passages selected for claim checks;
    
- acceptance schema;
    
- no drafting rationale or self-assessment.
    

Evaluate:

1. page-only answerability for every critical and routine question;
    
2. direct-answer completeness;
    
3. material-claim entailment;
    
4. contradiction and uncertainty treatment;
    
5. whether readable raw sources must still be reopened.
    

Allowed verdicts:

```text
semantic_pass
semantic_partial
semantic_fail
insufficient_evidence
```

Only `semantic_pass` may advance the topic toward final postflight.

The same worker that drafted the pages must not self-accept them.

---

## 8.8 Retrieval and query

Build retrieval only over semantically accepted compiled knowledge.

Default index scope:

```text
wiki/
```

Include source-atlas sections.

Do not index raw sources as the normal future-AI answer surface.

### Derived index

Use a rebuildable per-KB SQLite FTS5 database unless bounded web and runtime validation identifies a materially better simple option.

Suggested path:

```text
derived/search/search.sqlite
```

Index section-level chunks with:

- KB ID;
    
- page path;
    
- page type;
    
- topic ID;
    
- title;
    
- heading path;
    
- section body;
    
- source pointers;
    
- page hash;
    
- acceptance/run identity.
    

Required behavior:

- runtime FTS5 probe;
    
- deterministic rebuild;
    
- integrity check;
    
- stale-index detection;
    
- weighted field ranking;
    
- short answer-bearing snippets;
    
- JSON result envelope;
    
- auditable Markdown query artifact;
    
- exact page and heading pointers.
    

Add:

```powershell
apex-kb query --run-root <path> --query "<question>"
```

A query result should contain:

- direct retrieved sections;
    
- scores;
    
- page and heading routes;
    
- source-atlas routes;
    
- retrieval backend and freshness;
    
- raw-source reopen guidance only when needed.
    

### `query_ready`

A run reaches `query_ready` only when:

```yaml
query_ready_requires:
  - all_in_scope_topics_semantic_pass
  - deterministic_postflight_pass
  - retrieval_index_fresh
  - no_unresolved_critical_blocker
```

Do not reuse the temporary `v1_canary_complete` state as final completion.

---

## 8.9 Incremental update and maintenance

Add a clear update surface:

```powershell
apex-kb update --run-root <existing-kb>
```

It creates a new controlled run rather than rewriting history.

The update process must:

1. inventory the current sources;
    
2. compare hashes and paths to the prior accepted inventory;
    
3. identify added, changed, moved, deleted, or newly unreadable sources;
    
4. derive affected topics from prior maps and new deterministic matches;
    
5. reuse unchanged source capsules;
    
6. invalidate only affected topic analyses and pages;
    
7. preserve prior accepted artifacts;
    
8. regenerate acceptance for affected topics;
    
9. rebuild retrieval;
    
10. record an impact report.
    

Required artifact:

```text
runs/<run-id>/impact-report.json
```

No unchanged source should be semantically reread merely because an update run exists.

---

## 8.10 Compatibility and migration

Support existing Apex KB artifacts where practical.

Create explicit migration logic for supported earlier schema versions.

Rules:

- migrate through code, not model interpretation;
    
- preserve backups or prior run directories;
    
- record old and new schema versions;
    
- fail clearly on unsupported versions;
    
- legacy pages remain readable;
    
- legacy pages cannot newly become `query_ready` without satisfying current acceptance.
    

Do not indefinitely maintain two runtime engines.

---

## 8.11 Thin Skill

The Skill may only:

1. invoke the exact requested CLI command;
    
2. display the CLI’s returned operator message;
    
3. execute a specifically referenced semantic packet;
    
4. place its result at the declared incoming path.
    

It must not:

- choose a stage;
    
- choose a template;
    
- construct configuration;
    
- derive paths;
    
- edit manifest or state;
    
- decide completion;
    
- summarize away application output;
    
- become necessary for direct CLI use.
    

Deleting the Skill must not break the application.

---

# 9. Operator experience

## 9.1 Normal new-KB flow

```powershell
apex-kb start
apex-kb continue
apex-kb status
```

The operator should not select internal stages.

`continue` either:

- runs the next deterministic stage;
    
- generates the next semantic packet;
    
- imports an available result;
    
- generates an acceptance packet;
    
- runs postflight;
    
- rebuilds retrieval;
    
- or reports the exact blocker.
    

## 9.2 Query flow

```powershell
apex-kb query --run-root <path> --query "<question>"
```

## 9.3 Update flow

```powershell
apex-kb update --run-root <path>
apex-kb continue --run-root <path>
```

## 9.4 Status output

Status must show:

- run ID;
    
- run type;
    
- source and destination;
    
- output tier;
    
- current stage;
    
- topic progress;
    
- completed stages;
    
- current blocker;
    
- expected semantic result;
    
- retrieval freshness;
    
- exact next action;
    
- truthful completion state.
    

---

# 10. Application organization

Refactor the current large core module into bounded modules where useful.

Target shape:

```text
src/apex_kb/
├── cli.py
├── errors.py
├── envelopes.py
├── config.py
├── schemas.py
├── manifest.py
├── state.py
├── transitions.py
├── paths.py
├── atomic.py
├── custody.py
├── extractors/
│   ├── base.py
│   ├── text.py
│   ├── docx.py
│   ├── pptx.py
│   ├── xlsx.py
│   └── pdf.py
├── corpus/
│   ├── inventory.py
│   ├── structure.py
│   ├── postings.py
│   ├── duplicates.py
│   ├── topics.py
│   └── report.py
├── semantic/
│   ├── tasks.py
│   ├── import_results.py
│   ├── capsules.py
│   ├── compilation.py
│   └── acceptance.py
├── retrieval/
│   ├── sqlite_fts.py
│   ├── chunks.py
│   └── query.py
├── maintenance/
│   ├── drift.py
│   └── impact.py
├── postflight.py
├── schemas/
└── templates/
```

Adapt this to actual code rather than creating empty modules.

Keep functions cohesive and testable.

Do not create abstraction layers with only one trivial caller.

---

# 11. Implementation sequence

## Milestone 0 — Baseline and intent proof

- inspect current PR and current main;
    
- run current tests;
    
- identify incomplete and incorrect behavior;
    
- complete bounded web verification;
    
- lock dependency choices;
    
- record the exact starting commit.
    

Do not produce a standalone architecture report.

## Milestone 1 — Harden the kernel

- refactor state and transitions;
    
- finalize result/error envelopes;
    
- finalize schemas;
    
- remove competing authority;
    
- add migration/version handling;
    
- prove atomic writes and restart behavior.
    

## Milestone 2 — Corpus intelligence

- implement custody modes;
    
- implement extraction registry;
    
- implement all required source formats;
    
- implement structure maps;
    
- implement postings;
    
- implement duplicates/version families;
    
- implement exhaustive topic maps;
    
- implement populated navigation report;
    
- prove byte-identical reruns.
    

## Milestone 3 — Multi-topic semantic lifecycle

- implement deterministic topic scheduling;
    
- implement source-capsule reuse;
    
- generate Phase 1 tasks;
    
- import and validate Phase 1;
    
- generate Phase 2 tasks;
    
- import compiled pages;
    
- generate acceptance tasks;
    
- import acceptance;
    
- prove AI cannot alter state.
    

## Milestone 4 — Retrieval and query

- implement chunking;
    
- implement FTS5 probe;
    
- implement index rebuild;
    
- implement stale checks;
    
- implement query;
    
- implement query artifacts;
    
- enforce completion gates.
    

## Milestone 5 — Maintenance

- implement update run;
    
- source drift;
    
- impact mapping;
    
- selective invalidation;
    
- capsule reuse;
    
- selective recompilation;
    
- retrieval refresh.
    

## Milestone 6 — Full product proof

- run all product tests;
    
- build wheel;
    
- install wheel in a clean environment;
    
- run real Leela Skill Tree canary;
    
- run at least one multi-topic or cross-topic reuse proof;
    
- run crash/resume proof;
    
- run query proof;
    
- verify source non-mutation;
    
- make the PR ready for review only after all mandatory gates pass.
    

Do not mark the PR ready merely because unit tests pass.

---

# 12. Test requirements

Use product-level tests rather than implementation proxies.

## 12.1 Existing tests to retain

Retain and strengthen tests for:

- exact Start first output;
    
- approved template identity;
    
- value prefilling;
    
- prompting only for missing fields;
    
- Windows absolute paths;
    
- separate source/destination repositories;
    
- preview without writes;
    
- confirmation creating manifest/state;
    
- reproducible manifest hash;
    
- file-only status;
    
- one legal next action;
    
- fresh-process resume;
    
- invalid-state blocking;
    
- atomic writes;
    
- semantic question/allowlist identity;
    
- semantic schema validation;
    
- semantic worker state isolation;
    
- bounded repair instructions.
    

## 12.2 Deterministic corpus tests

Create fixtures proving:

```text
inventory covers every file
every exclusion has a reason
unsupported files remain visible
reruns are byte-identical
path and filename signals remain distinct
title and H1 signals remain distinct
heading and body signals remain distinct
primary phrases and broad supporting terms remain distinct
negative terms do not create strong matches alone
candidate number 31 remains in the authoritative map
current dedicated source outranks generic long source
exact duplicates are grouped
normalized duplicate candidates are visible
version families preserve evidence
topic maps contain exact pointers
navigation report contains populated guidance
```

## 12.3 Format extraction tests

Test:

- Markdown;
    
- JSON;
    
- YAML;
    
- CSV;
    
- source code;
    
- DOCX;
    
- PPTX;
    
- XLSX;
    
- text PDF;
    
- image inventory;
    
- corrupted file;
    
- missing optional extractor.
    

## 12.4 Semantic fixture

Create a multi-file fixture with:

- current specification;
    
- older conflicting specification;
    
- prototype;
    
- implementation artifact;
    
- duplicate;
    
- contextual source;
    
- irrelevant generic-keyword-heavy source.
    

Pass only when:

- every deterministic candidate is dispositioned;
    
- duplicates are not reread;
    
- current versus prototype versus historical is correct;
    
- locked questions are answered;
    
- source atlas covers every candidate;
    
- independent evaluator passes;
    
- AI output cannot select the next stage.
    

## 12.5 State and recovery tests

Inject failure after each consequential write boundary.

Prove:

- state is never half-written;
    
- rerun is idempotent;
    
- existing valid artifacts are reused;
    
- invalid artifacts do not advance;
    
- missing result produces one exact repair action;
    
- new process resumes correctly;
    
- manifest drift blocks safely;
    
- schema-version mismatch is reason-coded.
    

## 12.6 Retrieval tests

Prove:

- FTS5 capability is tested;
    
- accepted pages are indexed;
    
- unaccepted pages are excluded;
    
- heading sections become distinct chunks;
    
- title/heading weighting works;
    
- exact expected sections rank for fixture queries;
    
- snippets contain matching evidence;
    
- stale page hashes block `query_ready`;
    
- complete rebuild is deterministic;
    
- deleting the database does not lose canonical knowledge.
    

## 12.7 Maintenance tests

Prove:

- unchanged source reuses its capsule;
    
- changed source invalidates affected topics;
    
- unrelated topic remains accepted;
    
- moved identical file preserves content identity and records path change;
    
- deleted source remains visible in the impact record;
    
- retrieval refreshes only after reacceptance.
    

## 12.8 Packaging tests

Build both wheel and source distribution.

Install the wheel in a clean virtual environment.

Prove:

```powershell
apex-kb --help
apex-kb start --help
apex-kb status --help
apex-kb continue --help
apex-kb query --help
apex-kb update --help
```

Confirm all schemas and templates are included in the installed wheel.

---

# 13. Real Leela canary

## 13.1 Access

Use:

```yaml
source_repository: leela-spec/leela
source_root: LeelaAppDevelopment
source_access: read_only

destination_repository: leela-spec/apexai-os-meta
destination_folder: temporary_or_explicit_canary_KB_root
```

Resolve and record exact source and implementation commits.

Use temporary clones or isolated worktrees where terminal execution is available.

Do not modify or commit changes to `leela-spec/leela`.

Do not automatically clean or rewrite either repository.

## 13.2 Canary topic

Run the complete lifecycle for:

```text
Skill Tree
```

Target questions must include:

1. What is the current Skill Tree and what does it own?
    
2. What is the Epic/Block/Chunk hierarchy and data model?
    
3. How do UX, navigation, selection, and Path handoff work?
    
4. What is implemented now versus only specified or proposed?
    
5. Which prototypes and historical variants differ from the current direction?
    
6. What contradictions or unresolved decisions remain?
    
7. Which files cover Skill Tree, how current are they, and what does each contribute?
    

## 13.3 Required candidate coverage

The deterministic topic map must surface and classify at minimum:

```text
Upgrades/IndexOfUptoDateFolders/Index1.md
Upgrades/Night4/Updates new/Skill Tree Update N4 v1.md
Spatial Skill Tree and Path prompt/flow sources
dedicated Skill Tree specifications
build packs
MVP and user-story coverage
cross-feature contract sources
older 01_Features material
Prototyp Spark variants
archive and duplicate variants
contextual interconnection sources
```

Do not hardcode these as the entire candidate set.

They are sentinel evidence that the corpus-intelligence stage is working.

## 13.4 Canary completion

The canary passes only when:

- every source is inventoried or explicitly excluded;
    
- the candidate map is exhaustive;
    
- every candidate has one semantic disposition;
    
- reusable capsules are created for reviewed unique sources;
    
- the dossier answers every target question;
    
- the atlas describes every candidate individually;
    
- current architecture is not inferred from prototypes;
    
- a fresh acceptance worker returns `semantic_pass`;
    
- retrieval returns answer-bearing sections;
    
- status reports `query_ready`;
    
- source hashes remain unchanged;
    
- interruption/resume has been demonstrated;
    
- exact commands and artifacts are recorded.
    

If independent evaluator access is unavailable, do not fake acceptance.

The application may still be implemented, but the canary must remain truthfully capped below `query_ready`.

## 13.5 Multi-topic proof

In addition to Skill Tree, prove the scheduler and source-capsule reuse with:

- one second real Leela topic; or
    
- a purpose-built multi-topic fixture when another full semantic topic would be disproportionate.
    

This proof must show that one unchanged source capsule can contribute to multiple topics without repeated source review.

## 13.6 Canary artifacts

Write concise evidence only:

```text
audit/canary/<run-id>/commands.txt
audit/canary/<run-id>/start-transcript.txt
audit/canary/<run-id>/source-mutation-check.json
audit/canary/<run-id>/stage-summary.json
audit/canary/<run-id>/query-tests.json
audit/canary/<run-id>/CANARY-REPORT.md
```

Do not commit the full generated Leela KB to the implementation branch unless explicitly required.

---

# 14. Git and branch rules

- Continue the existing implementation branch or a direct descendant.
    
- Do not create a parallel implementation from old `main`.
    
- Inspect dirty state before writes.
    
- Never stage unrelated changes.
    
- Use focused commits grouped by working capability.
    
- Do not commit generated virtual environments, caches, build directories, temporary clones, retrieval databases, or canary corpora.
    
- Update PR #10 or open one direct successor if branch conditions make that necessary.
    
- Keep the PR draft while mandatory product gates fail.
    
- Mark ready for review only after the real required canary boundary passes.
    
- Do not merge without explicit operator authorization.
    

Recommended commit grouping:

```text
1. Harden CLI kernel and contracts
2. Implement whole-corpus intelligence and extractors
3. Implement multi-topic semantic lifecycle
4. Implement acceptance, retrieval, and query
5. Implement update and migration
6. Add real canary evidence and final documentation
```

Use fewer commits when changes are inseparable. Do not create dozens of one-file commits.

---

# 15. Simplicity constraints

The following are prohibited unless a demonstrated product failure requires them:

- GUI;
    
- TUI;
    
- MCP server;
    
- web service;
    
- daemon;
    
- workflow engine;
    
- autonomous multi-agent framework;
    
- vector database;
    
- embeddings;
    
- cloud retrieval;
    
- workflow-state database;
    
- plugin framework;
    
- event bus;
    
- hidden background process;
    
- new orchestration ledger;
    
- another handover chain;
    
- another architecture pack;
    
- multiple lifecycle drivers;
    
- multiple canonical configurations;
    
- provider-specific semantic lock-in;
    
- silent source omission;
    
- silent file overwrite;
    
- model-selected lifecycle transitions.
    

Use:

- normal Python package;
    
- Click;
    
- pathlib;
    
- JSON Schema;
    
- YAML configuration;
    
- ordinary files;
    
- SQLite FTS5 as derived retrieval;
    
- small optional extractor dependencies;
    
- pytest;
    
- Git for implementation history.
    

Every abstraction and artifact must have a real producer, consumer, and value.

---

# 16. Failure modes to prevent

## Target substitution

Do not treat any of these as product completion:

- help output;
    
- schemas existing;
    
- files existing;
    
- headings existing;
    
- unit tests alone;
    
- a synthetic canary alone;
    
- semantic result import alone;
    
- an FTS database existing;
    
- a Skill describing the flow;
    
- a PR being open;
    
- a stage called “complete.”
    

## Research drift

Do not reopen settled architecture debates unless live evidence makes the selected architecture infeasible.

## Partial implementation presented as final

Do not label unsupported features as planned options inside a “final” CLI.

Either implement them, remove them from the exposed configuration, or return an explicit truthful blocker.

## Parallel authority

Do not leave old scripts or Skill prose capable of choosing lifecycle stages beside the new package.

## Quality proxies

Do not use:

- word counts;
    
- fixed page counts;
    
- fixed source counts;
    
- headings;
    
- file counts;
    
- self-reported rereads
    

as proof of semantic value.

## Semantic contamination

Do not let:

- ranks become semantic truth;
    
- paths become authority;
    
- unopened sources become evidence;
    
- the compiler accept its own work;
    
- AI select output paths;
    
- AI mutate state.
    

---

# 17. Completion gates

The implementation is complete only when all applicable gates pass.

```yaml
application:
  installable_wheel: pass
  clean_environment_smoke_test: pass
  one_lifecycle_authority: pass
  start_status_continue: pass
  query: pass
  update: pass

deterministic:
  whole_corpus_inventory: pass
  all_candidate_topic_maps: pass
  no_top_n_truncation: pass
  duplicate_and_version_families: pass
  supported_format_extraction: pass
  populated_navigation_report: pass
  byte_identical_rerun: pass

semantic:
  source_capsule_reuse: pass
  multi_topic_scheduling: pass
  every_candidate_disposition: pass
  phase2_dossier: pass
  complete_source_atlas: pass
  ai_cannot_advance_state: pass

acceptance:
  fresh_context_evaluator: pass
  page_only_answerability: pass
  claim_entailment: pass

retrieval:
  FTS5_probe: pass
  accepted_page_indexing: pass
  stale_detection: pass
  answer_bearing_query_results: pass

maintenance:
  source_drift: pass
  selective_invalidation: pass
  unchanged_capsule_reuse: pass
  retrieval_refresh: pass

canary:
  real_Leela_source: pass
  source_non_mutation: pass
  Skill_Tree_semantic_pass: pass
  Skill_Tree_query_ready: pass
  fresh_process_resume: pass
```

A gate may be marked `blocked` only with concrete external evidence.

Do not convert `blocked` into `pass`.

---

# 18. Deliverables

Deliver implementation, not another process package.

Required:

1. completed Python package;
    
2. canonical runtime templates;
    
3. complete schemas;
    
4. deterministic corpus-intelligence engine;
    
5. extraction adapters;
    
6. source custody modes;
    
7. multi-topic scheduler;
    
8. Phase 1 packet/import lifecycle;
    
9. Phase 2 packet/import lifecycle;
    
10. independent acceptance packet/import lifecycle;
    
11. SQLite retrieval and query;
    
12. update/maintenance lifecycle;
    
13. compatibility or migration handling;
    
14. thin optional Skill;
    
15. product-level tests;
    
16. concise README;
    
17. updated draft PR;
    
18. concise final implementation report.
    

The README must explain only:

- installation;
    
- new KB;
    
- continue;
    
- status;
    
- query;
    
- update;
    
- semantic packet execution;
    
- output tiers;
    
- troubleshooting.
    

The final implementation report must contain:

```yaml
baseline:
  main_sha:
  starting_branch_sha:
  final_branch_sha:

implementation:
  files_added:
  files_modified:
  obsolete_authorities_removed_or_wrapped:
  dependency_decisions:

validation:
  commands_run:
  tests_passed:
  package_build:
  clean_install:
  real_canary:
  query_tests:
  source_mutation_check:

truth:
  completed_capabilities:
  blocked_capabilities:
  remaining_missing_functionality:
  final_completion_state:
```

If functionality is still missing, say so directly.

---

# 19. Final response

Return a concise result containing:

1. **Intent and feasibility verdict**
    
2. **Implemented capabilities**
    
3. **Architecture simplifications made**
    
4. **Files and commands**
    
5. **Tests**
    
6. **Real Leela canary**
    
7. **PR and branch**
    
8. **Remaining limitations**
    

Do not return another implementation plan as the primary result.

The priority remains:

```text
intended product value
→ simplest complete implementation
→ product-level test
→ real canary
→ demonstrated failure
→ smallest necessary correction
```