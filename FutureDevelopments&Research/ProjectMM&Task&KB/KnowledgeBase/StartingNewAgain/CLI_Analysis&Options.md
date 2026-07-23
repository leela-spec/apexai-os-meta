# Independent Architecture Research — Apex KB Execution Model

## Research basis

OpenAI describes Skills as reusable workflows containing instructions, examples, resources, and optionally code; ChatGPT may invoke them automatically when they appear helpful. Plugins package workflow capabilities—Skills, apps, and app templates—but do not themselves define a durable state machine. ([OpenAI Help Center](https://help.openai.com/en/articles/20001066-skills-in-chatgpt/?utm_source=chatgpt.com "Skills in ChatGPT | OpenAI Help Center"))

The Agent Skills specification defines a Skill as a directory with a required `SKILL.md` and optional `scripts/`, `references/`, and `assets/`. Its reference client model uses progressive loading: metadata first, full instructions after activation, then supporting resources as needed.

Crucially, the Agent Skills client guide says most implementations rely on the model’s own judgment to decide that a Skill is relevant and activate it. Anthropic separately recommends **low degrees of freedom and exact scripts** for fragile operations where consistency and ordering matter. ([Claude Platform](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices?utm_source=chatgpt.com "Skill authoring best practices - Claude Platform Docs"))

---

# 1. Decisive verdict

**Apex KB is fundamentally a local, manifest-driven, finite-state application that delegates bounded meaning-based work to AI workers. Its primary execution authority should be a modular CLI/application core—not a Skill, chat, autonomous agent, workflow engine, or UI.** The core must render the canonical setup interface, preserve operator choices, validate independent source and destination topologies, own legal state transitions, run deterministic stages, generate constrained semantic task packets, validate and import results, and certify completion from durable evidence. A Skill may provide a convenient manual launcher and semantic guidance, but the entire lifecycle must remain executable and recoverable without any Skill being installed or automatically invoked.

This is an architectural inference from the platform behavior: Skills provide reusable model-interpreted guidance, while Claude Code’s executable mechanisms provide noninteractive operation, validated JSON output, permissions, and blocking hooks. ([OpenAI Help Center](https://help.openai.com/en/articles/20001066?utm_source=chatgpt.com "Skills in ChatGPT | OpenAI Help Center"))

---

# 2. Option matrix

The scores below are **architectural judgments**, not measured benchmarks.

For cost, maintenance, dependency, drift, and duplication criteria, a higher number is better:

- `100 implementation cost` = inexpensive to build.
    
- `100 maintenance` = little recurring maintenance.
    
- `100 dependency burden` = few dependencies.
    
- `100 AI drift` = low drift risk.
    
- `100 duplication` = low duplication risk.
    

## Reliability and operating qualities

|Option|Template|Sequence|Resume|Test|Windows|Portability|Paths|Semantic isolation|
|---|--:|--:|--:|--:|--:|--:|--:|--:|
|**A. Large Skill engine**|35|25|20|35|75|55|60|35|
|**B. Skill invoking scripts**|70|65|60|70|75|60|75|70|
|**C. Monolithic script**|90|85|65|80|85|90|85|75|
|**D. Modular CLI**|95|95|90|95|90|95|95|90|
|**E. CLI + thin Skill**|95|95|90|95|90|85|95|90|
|**F. TUI over CLI**|95|95|90|90|85|85|95|90|
|**G. Desktop/web app**|98|95|90|85|80|70|95|90|
|**H. Workflow engine**|90|95|98|90|65|85|85|85|
|**I. Autonomous orchestrator**|45|35|55|45|75|60|70|40|
|**J. CLI kernel + provider-neutral AI adapters**|**98**|**98**|**95**|**97**|**92**|**98**|**97**|**97**|

## Cost, risk, and evolution

|Option|Clarity|Impl. cost|Maintenance|Dependencies|Low drift|Low duplication|Evolution|Average|Disposition|
|---|--:|--:|--:|--:|--:|--:|--:|--:|---|
|**A. Large Skill engine**|60|85|35|85|15|35|50|**47.0**|Reject|
|**B. Skill invoking scripts**|70|75|60|80|55|50|70|**67.0**|Transitional only|
|**C. Monolithic script**|70|85|50|90|95|80|45|**78.0**|Prototype only|
|**D. Modular CLI**|85|70|85|80|95|90|95|**89.7**|Strong core|
|**E. CLI + thin Skill**|95|65|80|75|90|75|95|**87.3**|Good optional surface|
|**F. TUI over CLI**|90|50|65|60|90|70|90|**82.7**|Later|
|**G. Desktop/web app**|95|25|45|30|90|65|85|**75.9**|Premature|
|**H. Workflow engine**|55|30|45|20|95|55|80|**71.5**|Overbuilt|
|**I. Autonomous orchestrator**|70|70|35|65|20|30|60|**51.7**|Reject|
|**J. CLI kernel + provider-neutral AI adapters**|**92**|60|**88**|75|**96**|**92**|**99**|**91.6**|**Select**|

## Why J wins

Option J is a refinement of D rather than a separate heavyweight layer:

> **Modular local workflow kernel + CLI + replaceable semantic-worker protocol + optional Skill/UI shells.**

It keeps all deterministic lifecycle behavior in one core while allowing semantic execution through:

- a manually operated ChatGPT or Claude conversation;
    
- noninteractive Claude Code;
    
- an API adapter;
    
- a future alternative model;
    
- or no automated AI invocation at all.
    

Claude Code already supports noninteractive execution, explicit tool permissions, JSON output, and output constrained by JSON Schema. That makes it a viable worker adapter, but not the workflow authority. ([Claude](https://code.claude.com/docs/en/headless?utm_source=chatgpt.com "Run Claude Code programmatically - Claude Code Docs"))

## Why the alternatives lose

- **A:** Automatic Skill selection and model-interpreted instructions are incompatible with exact startup rendering and legal-state enforcement.
    
- **B:** Better than A, but the model still decides whether and how to call the scripts unless the CLI is independently usable—in which case the CLI is already the real engine.
    
- **C:** Initially cheap, but state logic, validation, corpus work, import, recovery, and retrieval will become one high-coupling file.
    
- **D:** Correct core, but incomplete unless semantic execution is formalized as a replaceable protocol.
    
- **E:** Excellent operator convenience, but still only a shell around J.
    
- **F/G:** Useful only after the CLI contract is stable.
    
- **H:** Mature workflow systems demonstrate valuable checkpoint and artifact patterns, but bring unnecessary runtimes, concepts, and dependencies for a local single-operator application. Nextflow, for example, automatically tracks intermediate outputs for resume, while DVC separates editable pipeline descriptions from generated lock state; Apex should copy those principles, not adopt those systems. ([Nextflow](https://nextflow.io/?utm_source=chatgpt.com "A DSL for parallel and scalable computational pipelines | Nextflow"))
    
- **I:** Recreates the exact failure boundary: the AI becomes responsible for control flow, interpretation, recovery, and completion.
    

---

# 3. Minimal architecture

## Smallest viable component map

```text
┌───────────────────────────────────────────────────────────────┐
│                     APEX KB APPLICATION                       │
│                                                               │
│  CLI commands                                                 │
│       │                                                       │
│       ▼                                                       │
│  Setup renderer + input collector                             │
│       │                                                       │
│       ▼                                                       │
│  Schema and topology validator                                │
│       │                                                       │
│       ▼                                                       │
│  Finite-state workflow kernel ───────► run-state.json         │
│       │                              stage-results/*.json      │
│       │                                                       │
│       ├── deterministic corpus modules                         │
│       │       inventory / structure / topic maps / retrieval  │
│       │                                                       │
│       ├── semantic packet builder                              │
│       │             │                                         │
│       │             ▼                                         │
│       │     provider-neutral worker adapter                    │
│       │        manual | Claude CLI | API | other model         │
│       │             │                                         │
│       │             ▼                                         │
│       ├── result validator and importer                        │
│       │                                                       │
│       ├── independent acceptance gate                          │
│       │                                                       │
│       └── deterministic completion and evidence builder        │
└───────────────────────────────────────────────────────────────┘

Optional shells:
  Skill launcher ───────┐
  Terminal UI ──────────┼── call the same application contract
  Desktop/web UI ───────┘
```

## Information flow

```text
Canonical setup template
        ↓
Operator-entered draft configuration
        ↓
Schema + path/topology validation
        ↓
Immutable canonical run manifest + hash
        ↓
Run state initialized
        ↓
Deterministic corpus stages
        ↓
Bounded semantic task packet
        ↓
AI candidate result
        ↓
Structural validation + allowlist checks
        ↓
Imported semantic artifact
        ↓
Independent semantic acceptance
        ↓
Retrieval build
        ↓
Deterministic completion evidence
```

## Core resilience rules

1. **One workflow kernel:** no Skill state machine, chat orchestrator, or duplicate control script.
    
2. **One immutable manifest:** operator choices are normalized mechanically, hashed, and never reinterpreted by AI.
    
3. **One current-state authority:** `run-state.json`.
    
4. **Append-only stage evidence:** stage results prove how state was reached but do not compete with state ownership.
    
5. **Atomic writes:** write to a temporary sibling, flush, then replace the target.
    
6. **Idempotent stages:** the same inputs and stage version produce either the same outputs or a controlled invalidation.
    
7. **Fail closed:** ambiguous topology, altered fingerprints, missing outputs, or invalid AI responses block advancement.
    
8. **Independent source/destination models:** never assume that sources and KB output share one repository root.
    

## Source/destination topology

The manifest should model them separately:

```text
source_locations[]:
  kind: local_directory | repository_directory | snapshot
  root
  selected_paths[]
  revision/fingerprint
  read_only: true

destination:
  kind: local_directory | repository_directory
  root
  kb_path
```

The schema can use tagged alternatives such as `oneOf`, while runtime validation handles facts that JSON Schema alone cannot prove—existence, permissions, symlinks, repository identity, and source/destination overlap. JSON Schema is designed to declare structure, types, required fields, and constraints; filesystem truth still requires executable validation. ([JSON Schema](https://json-schema.org/learn/getting-started-step-by-step?utm_source=chatgpt.com "JSON Schema"))

---

# 4. Skill decision

## Final classification

|Possible role|Decision|
|---|---|
|**Primary engine**|**No**|
|**Thin launcher**|**Optional, manually invoked**|
|**Semantic guidance package**|**Yes**|
|**Automatically required**|**No**|
|**Required for core execution**|**No**|
|**Useful for discoverability and convenience**|**Yes**|

## Appropriate Skill contents

A small Skill may contain:

- when to offer Apex KB;
    
- how to call the CLI;
    
- how to explain CLI results;
    
- semantic writing guidance;
    
- model-specific tips for executing a generated packet;
    
- links to the installed CLI documentation.
    

It must not contain or own:

- the canonical setup template;
    
- run configuration;
    
- path selection;
    
- current stage;
    
- legal transitions;
    
- next-action derivation;
    
- output locations;
    
- completion certification;
    
- repair logic.
    

OpenAI recommends Skills as small, reusable workflow building blocks rather than one enormous end-to-end Skill. The open specification similarly treats `SKILL.md` as instructions and supporting files as progressively loaded resources. ([OpenAI](https://openai.com/academy/skills/?utm_source=chatgpt.com "Using skills | OpenAI"))

## Invocation policy

For the exact Apex lifecycle:

- **Preferred:** operator explicitly runs `apex-kb start`.
    
- **Permitted:** operator manually invokes `@apex-kb`, and the Skill launches the same CLI.
    
- **Not authoritative:** automatic Skill invocation.
    

Automatic invocation may provide helpful discovery, but it cannot be the only path to the canonical first response because both OpenAI and Agent Skills implementations describe relevance-driven activation. ([OpenAI Help Center](https://help.openai.com/en/articles/20001066?utm_source=chatgpt.com "Skills in ChatGPT | OpenAI Help Center"))

---

# 5. CLI or application contract

## Minimum public commands

### `apex-kb start`

Purpose:

- print the canonical setup template;
    
- optionally run an interactive prompt sequence;
    
- load an already completed draft with `--config`;
    
- validate configuration and topology;
    
- show an exact readback;
    
- after approval, create the canonical manifest and initial state.
    

Important behavior:

```text
apex-kb start --print-template
apex-kb start --interactive
apex-kb start --config run-config.yaml
apex-kb start --config run-config.yaml --check
```

`--print-template` must be a deterministic renderer, not an AI request.

### `apex-kb status`

Purpose:

- display current stage;
    
- show completed and blocked stages;
    
- report manifest hash and invalidations;
    
- provide the mechanically derived next legal action;
    
- support `--json`.
    

It performs no mutation.

### `apex-kb continue`

Purpose:

- execute the next legal deterministic stage;
    
- stop at an operator gate;
    
- stop after producing a semantic task packet;
    
- optionally call a configured semantic adapter;
    
- never skip a failed or unapproved gate.
    

It does not accept a free-form stage name during normal use.

### `apex-kb approve`

Purpose:

- approve a specific pending gate;
    
- require the gate ID, manifest hash, and artifact fingerprint;
    
- reject stale approval attempts.
    

Examples include configuration lock and independent semantic acceptance—not AI self-approval.

### `apex-kb import`

Purpose:

- import a semantic worker result;
    
- validate its schema, task ID, fingerprints, output paths, and write allowlist;
    
- promote valid candidate outputs;
    
- reject lifecycle fields authored by the worker.
    

### `apex-kb repair`

Purpose:

- reconcile state after interruption;
    
- identify incomplete atomic writes;
    
- reconstruct state from manifest and stage-result evidence;
    
- invalidate outputs whose inputs changed;
    
- never guess semantic content.
    

### `apex-kb query`

Purpose:

- perform deterministic retrieval over accepted compiled knowledge;
    
- produce ranked evidence and completion provenance;
    
- never mutate lifecycle state.
    

## Internal, nonpublic stage commands

Testing and diagnostics may expose an expert surface such as:

```text
apex-kb internal run-stage <stage-id>
apex-kb internal validate-artifact <path>
apex-kb internal reconcile
```

These should not be part of the ordinary operator workflow.

Python’s standard CLI tooling directly supports subcommands, while Click’s test runner supports invocation, input streams, captured output, and exit-code assertions for interactive prompt tests. ([Python documentation](https://docs.python.org/3/library/argparse.html?force_isolation=true&utm_source=chatgpt.com "argparse — Parser for command-line options, arguments and subcommands — Python 3.14.6 documentation"))

## Exit contract

Use a compact stable set:

|Exit|Meaning|
|--:|---|
|`0`|Successful command|
|`1`|Runtime or stage failure|
|`2`|Invalid CLI usage or invalid operator input|
|`3`|Blocked; operator action required|
|`4`|State conflict or stale fingerprint|
|`5`|Semantic result rejected|
|`6`|Environment or capability unavailable|

Python treats zero as success and nonzero as abnormal termination; explicit application-specific meanings should stay in a small documented range. ([Python documentation](https://docs.python.org/3/library/sys.html?highlight=exit&utm_source=chatgpt.com "sys — System-specific parameters and functions — Python 3.14.6 documentation"))

---

# 6. Semantic boundary

## AI-owned work

The AI remains responsible for:

- interpreting meaning;
    
- assessing source authority;
    
- determining whether two claims conflict;
    
- distinguishing current, historical, proposed, and superseded concepts;
    
- synthesizing across sources;
    
- writing Macro, Meso, and Micro explanations;
    
- producing source-grounded concept dossiers;
    
- producing source atlases and contradiction records;
    
- performing independent semantic acceptance in a fresh context.
    

## Deterministically owned work

The application owns:

- Skill-independent activation;
    
- exact setup template selection and rendering;
    
- input capture and normalization;
    
- preservation of the operator’s literal choices;
    
- path and topology validation;
    
- source scope and exclusions;
    
- stage sequencing;
    
- legal transition evaluation;
    
- state and recovery;
    
- inventory and hashes;
    
- structural corpus analysis;
    
- task partitioning;
    
- task IDs, source allowlists, and output paths;
    
- schema selection;
    
- worker invocation parameters;
    
- structural import validation;
    
- acceptance-gate mechanics;
    
- retrieval construction;
    
- completion status and evidence.
    

## Semantic worker protocol

Each worker receives a generated packet containing:

```text
task_id
run_id
manifest_hash
task_type
exact questions
exact source paths or resolved source excerpts
source fingerprints
existing accepted artifacts, if required
semantic instructions
allowed output paths
result schema
stop conditions
```

The packet must not ask the AI:

- what stage should happen next;
    
- where to write;
    
- which template to choose;
    
- which source scope is appropriate;
    
- whether the run is complete.
    

The AI result may contain semantic judgments and authored content. It may not contain effective control-plane mutations.

Claude Code can be used as one adapter because noninteractive mode supports tool allowlists, turn limits, JSON output, and JSON-Schema-constrained structured results. Those controls make the worker bounded; they do not make its semantic judgment deterministic. ([Claude](https://code.claude.com/docs/en/headless?utm_source=chatgpt.com "Run Claude Code programmatically - Claude Code Docs"))

## Independent acceptance split

The independent evaluator AI owns the semantic verdict:

```text
semantic_pass
semantic_partial
semantic_fail
insufficient_evidence
```

The application owns:

- selection of the acceptance packet;
    
- ensuring the evaluator did not receive drafting rationale;
    
- validation of the verdict artifact;
    
- deciding mechanically whether the verdict satisfies the configured gate;
    
- advancing or blocking the run.
    

---

# 7. Canonical artifacts

## Static application contracts

These are versioned application resources, not per-run state:

|Artifact|Producer|Consumer|
|---|---|---|
|`setup-template.md`|Application maintainers|`start` renderer|
|`run-config.schema.json`|Application maintainers|Draft validator|
|`run-manifest.schema.json`|Application maintainers|Manifest builder and all stages|
|`run-state.schema.json`|Application maintainers|Workflow kernel|
|`stage-result.schema.json`|Application maintainers|Stage runners and reconciler|
|`semantic-task.schema.json`|Application maintainers|Packet builder and worker adapters|
|`semantic-result.schema.json`|Application maintainers|Worker and importer|
|`acceptance.schema.json`|Application maintainers|Independent evaluator and gate|

## Per-run artifacts

|Artifact|Canonical status|Producer|Primary consumer|
|---|---|---|---|
|`run-config.yaml`|Draft, not authoritative after lock|Operator via `start`|Manifest builder|
|`run-manifest.json`|**Immutable canonical input**|Manifest builder|Every stage|
|`run-state.json`|**Canonical current state**|Workflow kernel|CLI/status/continue|
|`stage-results/<stage>.json`|Append-only execution evidence|Stage runner|Reconciler/audit|
|`corpus/source-inventory.ndjson`|Deterministic derived evidence|Inventory stage|Corpus intelligence|
|`corpus/topic-maps/<topic>.json`|Deterministic candidate contract|Corpus intelligence|Packet builder|
|`semantic-tasks/<task>.json`|Canonical worker assignment|Packet builder|Semantic worker|
|`semantic-results/<task>.json`|Candidate result|Semantic worker|Importer|
|`knowledge/...`|Accepted authored knowledge|Importer after validation|Acceptance and retrieval|
|`acceptance/<topic>.json`|Canonical independent verdict|Independent evaluator|Acceptance gate|
|`retrieval/...`|Regenerable derived index|Retrieval builder|Query|
|`completion.json`|Canonical closure evidence|Completion stage|Operator and future automation|

## Important authority rules

- `run-config.yaml` is human-editable, but it ceases to be authoritative once the manifest is locked.
    
- `run-manifest.json` is immutable. Changes require a new manifest revision and explicit invalidation.
    
- `run-state.json` is the only current-state authority.
    
- Stage results are evidence, not a second state ledger.
    
- Retrieval indexes are disposable and rebuildable.
    
- A database must not hold unique lifecycle truth.
    

Ordinary files are sufficient for this control plane. DVC’s separation between a human-readable pipeline file and generated machine lock state is a useful precedent, while Nextflow demonstrates the value of retained intermediate execution evidence for resume. ([DVC](https://dvc.org/blog/dvc-1-0-release/?utm_source=chatgpt.com "DVC 1.0 release: new features for MLOps – DVC"))

## Files that are not canonical artifacts

Do not create:

- chat handover chains;
    
- orchestration diaries;
    
- duplicate run ledgers;
    
- multiple Q&A template variants;
    
- AI-written next-command files;
    
- self-assessment reports from the drafting AI;
    
- architecture-status prose that competes with schemas or state;
    
- manually maintained artifact inventories that the application can derive.
    

---

# 8. Test strategy

## A. Exact template-rendering test

Acceptance:

- `apex-kb start --print-template` renders the approved template exactly.
    
- The rendered template has a version and content hash.
    
- No model call occurs.
    
- The first interactive output is tested—not just the presence of the template file.
    

Use a golden-file test with controlled newline normalization where platform differences require it.

## B. Full interaction transcript test

Test the actual operator experience:

```text
command
prompts
entered answers
validation errors
corrected answers
readback
approval
files produced
exit status
```

Click’s `CliRunner` can feed stdin, capture prompts and output, and inspect the resulting exit code, making this a suitable product-level transcript test. ([Click Documentation](https://click.palletsprojects.com/en/stable/testing/?utm_source=chatgpt.com "Testing Click Applications — Click Documentation (8.5.x)"))

## C. Topology test matrix

Fixtures must cover:

1. sources and destination in the same repository but separate trees;
    
2. sources and destination in different repositories;
    
3. multiple source roots;
    
4. Windows absolute drive paths;
    
5. UNC paths;
    
6. destination nested inside source—reject;
    
7. source nested inside destination—reject;
    
8. symlink or junction overlap—reject or require explicit policy;
    
9. missing source;
    
10. unwritable destination;
    
11. repository-relative source descriptors;
    
12. snapshot sources with immutable revisions.
    

Python’s `pathlib` explicitly models Windows and POSIX path semantics, including drive letters and UNC shares. ([Python documentation](https://docs.python.org/3.14/library/pathlib.html?utm_source=chatgpt.com "pathlib — Object-oriented filesystem paths — Python 3.14.6 documentation"))

## D. Operator-choice preservation test

Given a completed configuration:

- every operator value appears in the manifest without semantic rewriting;
    
- generated fields are visibly separated from supplied fields;
    
- the manifest hash is reproducible;
    
- reordering irrelevant YAML keys does not change normalized meaning;
    
- material changes produce a different hash;
    
- the AI cannot alter manifest values.
    

## E. Finite-state transition test

For every state:

- enumerate legal successors;
    
- reject every illegal successor;
    
- confirm `continue` selects exactly one legal action;
    
- verify blocked states have stable reason codes;
    
- confirm no model-produced field can change the state.
    

Use property-based tests for transition closure if practical.

## F. Crash-and-resume test

Inject interruption:

- before a stage begins;
    
- during output generation;
    
- after output write but before state update;
    
- after state update;
    
- during result import;
    
- during retrieval rebuild.
    

On restart, the application must:

- retain completed accepted work;
    
- remove or quarantine incomplete temporary output;
    
- not repeat non-idempotent operations;
    
- derive the same next legal action.
    

## G. Semantic packet-generation test

For a fixed manifest and topic map, assert:

- exact task ID;
    
- exact sources;
    
- exact source fingerprints;
    
- exact locked questions;
    
- exact result schema;
    
- exact allowed output path;
    
- no extra source scope;
    
- no lifecycle recommendation request;
    
- no next-stage selection field.
    

## H. Absence-of-AI-lifecycle-control test

Feed a deliberately hostile semantic result containing:

```text
next_stage
new_source_roots
replacement_template
output_path
completed: true
approved: true
```

The importer must reject or discard every control-plane field and leave state unchanged.

This test is more important than a test that merely verifies a prompt mentions the prohibition.

## I. Structural import test

Reject results with:

- wrong task ID;
    
- stale manifest hash;
    
- altered source fingerprints;
    
- missing required properties;
    
- unapproved output paths;
    
- additional files;
    
- invalid citations or provenance shape;
    
- malformed authored artifacts.
    

JSON Schema validates result structure, but application checks must additionally enforce path allowlists, fingerprints, and state correspondence. ([JSON Schema](https://json-schema.org/draft/2020-12/json-schema-validation?utm_source=chatgpt.com "JSON Schema Validation: A Vocabulary for Structural Validation of JSON"))

## J. Independent acceptance test

Prove that:

- the evaluator uses a new context;
    
- drafting rationale is absent;
    
- target questions are unchanged;
    
- page-only answerability is evaluated;
    
- unsupported claims fail;
    
- the drafting AI cannot approve itself;
    
- only a valid independent verdict can satisfy the semantic gate.
    

## K. Completion test

`completion.json` may be created only when:

- all required deterministic stages passed;
    
- every required semantic result was imported;
    
- acceptance gates passed;
    
- retrieval was rebuilt from accepted knowledge;
    
- no unresolved blocking reason remains;
    
- all relevant hashes and artifact paths are recorded.
    

---

# 9. Build sequence

No more than six milestones are required.

## Milestone 1 — Freeze the contracts

Define:

- state graph;
    
- canonical setup template;
    
- topology model;
    
- manifest;
    
- state and stage-result schemas;
    
- semantic task/result schemas;
    
- artifact paths and authority rules.
    

No UI and no Skill work yet.

## Milestone 2 — Build and prove Setup

Implement:

- `start`;
    
- deterministic template rendering;
    
- draft validation;
    
- topology validation;
    
- readback;
    
- manifest lock and hash;
    
- initial state.
    

Pass the golden-output and real transcript tests before continuing.

## Milestone 3 — Build the workflow kernel

Implement:

- `status`;
    
- `continue`;
    
- `approve`;
    
- stage registry;
    
- legal transitions;
    
- atomic writes;
    
- stable reason codes;
    
- `repair`;
    
- crash/resume tests.
    

## Milestone 4 — Integrate deterministic corpus stages

Connect:

- inventory;
    
- hashing;
    
- structural extraction;
    
- exhaustive topic mapping;
    
- semantic packet generation.
    

Do not redesign semantic writing yet.

## Milestone 5 — Add semantic adapters and import

Implement:

- manual handoff adapter;
    
- one noninteractive adapter, preferably Claude Code initially;
    
- structured result validation;
    
- allowlisted import;
    
- independent acceptance packet and gate.
    

## Milestone 6 — Retrieval, completion, and one real canary

Implement:

- deterministic retrieval;
    
- completion evidence;
    
- end-to-end canary with real source/destination topology;
    
- optional thin Skill only after the CLI canary passes.
    

---

# 10. Kill list

Remove, reduce, or make optional the following concepts wherever they exist.

## Remove

1. **Large Skill as lifecycle engine**
    
2. **Automatic Skill invocation as the canonical start path**
    
3. **AI-selected next commands**
    
4. **AI-selected templates**
    
5. **AI interpretation of operator configuration**
    
6. **AI-generated paths or source scope**
    
7. **Drafting-AI self-certification**
    
8. **Multiple overlapping state ledgers**
    
9. **Multiple canonical configuration files**
    
10. **Chat-memory-based resume**
    
11. **Cross-chat handover chains as workflow state**
    
12. **Tests that prove only file presence, headings, flags, or command registration**
    
13. **Design packages placed near live files without an executable installation boundary**
    
14. **Authoritative top-N source truncation**
    
15. **An autonomous agent orchestrator around the CLI**
    

## Reduce

1. **Skill instructions:** keep only launch and semantic guidance.
    
2. **Operator commands:** seven public commands are enough.
    
3. **Schemas:** one schema per contract, versioned centrally.
    
4. **Stage documentation:** derive most operator information from the stage registry.
    
5. **Recovery prose:** encode recovery as executable reconciliation rules.
    
6. **Completion reports:** one deterministic `completion.json`, plus an optional human rendering.
    
7. **Configuration duplication:** one editable draft followed by one immutable canonical manifest.
    

## Make optional

1. Thin Skill
    
2. Claude Code worker adapter
    
3. Hooks
    
4. Terminal UI
    
5. Desktop/web UI
    
6. SQLite retrieval index
    
7. External provider adapters
    
8. Git integration beyond recording revisions and fingerprints
    

## Explicitly defer

- desktop or web application;
    
- terminal UI;
    
- external workflow engine;
    
- server process;
    
- distributed execution;
    
- control-plane database;
    
- autonomous multi-agent orchestration;
    
- vector retrieval.
    

---

# 11. Uncertainties

## Facts established by primary sources

### Skills and Plugins

- OpenAI Skills package reusable workflow instructions, examples, resources, and optional code.
    
- ChatGPT can invoke relevant Skills automatically.
    
- Plugins are packaging and discovery containers that can include Skills, apps, and app templates.
    
- Apps continue to own access to external data and actions. ([OpenAI Help Center](https://help.openai.com/en/articles/20001066-skills-in-chatgpt/?utm_source=chatgpt.com "Skills in ChatGPT | OpenAI Help Center"))
    

### Agent Skills specification

- `SKILL.md` is required.
    
- `scripts/`, `references/`, and `assets/` are optional.
    
- Skills use progressive disclosure.
    
- Supporting resources are loaded as needed.
    
- Most reference client implementations use model judgment for activation.
    

### Anthropic and Claude Code

- Anthropic recommends exact scripts and low degrees of freedom for fragile, sequence-sensitive operations.
    
- Claude Code supports noninteractive execution.
    
- It supports text, JSON, and streaming JSON output.
    
- It can constrain final structured output with JSON Schema.
    
- Permissions and `PreToolUse` hooks can prevent tool execution. ([Claude Platform](https://platform.claude.com/docs/de/agents-and-tools/agent-skills/best-practices?utm_source=chatgpt.com "Best Practices für das Erstellen von Skills - Claude Platform Docs"))
    

### CLI and schemas

- Python supports subcommand-oriented CLIs and platform-aware path handling.
    
- Click supports automated prompt/transcript and exit-code testing.
    
- JSON Schema provides declarative structural validation.
    
- JSON Schema does not prove filesystem existence, permissions, semantic truth, or source authority. ([Python documentation](https://docs.python.org/3/library/argparse.html?force_isolation=true&utm_source=chatgpt.com "argparse — Parser for command-line options, arguments and subcommands — Python 3.14.6 documentation"))
    

## Architectural judgments

These are reasoned conclusions rather than platform guarantees:

1. A Skill is unsuitable as the authoritative Apex KB state machine.
    
2. A modular local application is the smallest architecture satisfying all requirements.
    
3. Ordinary durable files are sufficient for control-plane state.
    
4. A database should be a derived retrieval optimization, not workflow authority.
    
5. Provider-neutral semantic packets are necessary for cross-model portability.
    
6. A CLI should be proven before adding a TUI or graphical application.
    
7. Hooks should enforce prohibitions, not duplicate stage sequencing.
    
8. The best target is Option J.
    

## Unresolved but nonblocking implementation choices

### Python CLI framework

- `argparse` minimizes dependencies.
    
- Click or Typer improves prompt and transcript ergonomics.
    
- Either can satisfy the architecture.
    

**Recommendation:** Click if interactive transcript testing is central; `argparse` if dependency minimization dominates.

### Human-editable configuration format

- YAML is friendlier for editing.
    
- JSON avoids an additional syntax and parser surface.
    

**Recommendation:** YAML draft, immutable JSON manifest. Only the JSON manifest is canonical.

### Initial semantic adapter

- manual file handoff;
    
- Claude Code noninteractive mode;
    
- API invocation.
    

**Recommendation:** support manual handoff first, then one Claude Code adapter. This proves that the lifecycle is independent of a particular model transport.

### Retrieval backend

- generated Markdown index;
    
- JSON/NDJSON lexical index;
    
- SQLite FTS5.
    

**Recommendation:** start with the simplest deterministic index that passes the query tests. Add SQLite only as a derived artifact when corpus scale or query latency justifies it.

### Independent evaluator

A fresh context is mandatory; whether it must use a different model or provider is a policy decision rather than an architectural necessity.

**Recommendation:** require a fresh isolated context and permit a configurable stronger rule—different model/provider—for high-assurance runs.