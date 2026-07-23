## 1. Decisive Verdict

Apex KB is fundamentally a **deterministic, manifest-driven knowledge processing pipeline with an embedded LLM semantic worker**, not an autonomous agentic workflow. Its primary execution authority must be an external, strongly typed, modular Command Line Interface (CLI) application (e.g., written in Go, Rust, or Python with Pydantic/Typer). The CLI owns 100% of the workflow state, path resolution, inventory indexing, state transitions, canonical template rendering, and schema validation. This architecture reduces the AI strictly to an isolated, stateless function responsible solely for semantic analysis, synthesis, and Markdown wiki generation within pre-bounded execution packets.

## 2. Option Matrix

The table below evaluates candidate architectures against Apex KB requirements on a scale from 1 to 100.

|**Option**|**Architecture Concept**|**Determinism & Reliability**|**Resume & Recovery**|**Cross-Model Portability**|**Architecture Risk & AI Drift**|**Overall Score**|
|---|---|---|---|---|---|---|
|**A**|Large Skill as Primary Engine|15|20|35|10 (Extreme Drift)|**20**|
|**B**|Skill Invoking Deterministic Scripts|40|45|50|30 (High Drift)|**41**|
|**C**|Monolithic Script|70|60|85|80 (Low Drift)|**73**|
|**D**|**Modular CLI Application**|**95**|**95**|**95**|**95 (Zero Drift)**|**95**|
|**E**|CLI + Thin Manually Invoked Skill|90|95|90|90 (Low Drift)|**91**|
|**F**|Terminal UI (TUI) over CLI Core|90|95|80|90 (Low Drift)|**88**|
|**G**|Desktop or Web Application|85|90|60|85 (Low Drift)|**75**|
|**H**|External Workflow Engine (Temporal/Airflow)|95|95|70|95 (Low Drift)|**65**|
|**I**|Autonomous Agent Orchestrator (LangGraph/AutoGen)|30|35|40|20 (High Drift)|**31**|
|**J**|CLI Core + Lifecycle Hook Enforcement|95|95|85|95 (Zero Drift)|**93**|

### Rationale for Selection (Option D / Option E Integration)

- **Options A, B, and I (Skill / Agent Driven):** Primary research confirms that Agent Skills are prompt-extension packages loaded directly into the LLM context window. They do not possess a separate execution runtime or deterministic state machine. Placing stateful lifecycle control in a Skill inevitably causes template skipping, prompt improvisation, path misinterpretation, and unrecoverable drift.
    
- **Options C & F (Monolithic Script / TUI):** A single script quickly degrades under complex testing, cross-platform path handling, and subcommand maintainability. A TUI adds visual layer overhead before core state mechanics are validated.
    
- **Options H & G (Workflow Engine / Desktop App):** Violate anti-overengineering constraints for a local single-operator pipeline, adding heavy dependency burdens and platform coupling.
    
- **Option D (Modular CLI Application):** Provides absolute state control, deterministic file IO, robust cross-platform path resolution, zero-dependency JSON Schema validation, and mechanical resume capability. Option E can be treated as a secondary interface mode where a thin Skill merely documents CLI commands for an operator inside an AI shell environment.
    

## 3. Minimal Architecture

```
                                  [ Operator ]
                                       │
                                 1. apex init / scan
                                       ▼
                       ┌───────────────────────────────┐
                       │      apex-cli Engine          │
                       │  - Path Topology Validator    │
                       │  - Manifest & State Machine   │
                       └───────────────┬───────────────┘
                                       │
                        2. Creates / updates durable state
                                       ▼
                       ┌───────────────────────────────┐
                       │        apex.run.json          │
                       │   (Corpus Index & Hash Log)   │
                       └───────────────┬───────────────┘
                                       │
                        3. Compiles bounded work packet
                                       ▼
                       ┌───────────────────────────────┐
                       │      task_<id>.json           │
                       └───────────────┬───────────────┘
                                       │
                        4. Pure semantic execution
                                       ▼
                       ┌───────────────────────────────┐
                       │    Semantic Worker (LLM)      │
                       │ (Guided by SKILL.md guidelines)│
                       └───────────────┬───────────────┘
                                       │
                        5. Emits structured response
                                       ▼
                       ┌───────────────────────────────┐
                       │     response_<id>.json        │
                       └───────────────┬───────────────┘
                                       │
                        6. apex ingest & verify
                                       ▼
                       ┌───────────────────────────────┐
                       │     Wiki & Output Store       │
                       │   (Macro / Meso / Micro)      │
                       └───────────────────────────────┘
```

### Component Flow

1. **Setup & Initialization:** Operator runs `apex init`. The CLI renders the canonical setup template and outputs `apex.config.json`.
    
2. **Path Topology & Inventory:** Operator runs `apex scan`. The CLI verifies source and target topologies, scans files, computes SHA-256 content hashes, and creates `apex.run.json`.
    
3. **Packet Assembly:** Operator runs `apex step`. The CLI checks `apex.run.json`, identifies the next unanalyzed corpus slice, and constructs `task_<id>.json`.
    
4. **Semantic Processing:** The LLM consumes `task_<id>.json` (guided by writing standards in a passive `SKILL.md`) and outputs structured `response_<id>.json`.
    
5. **Validation & Ingestion:** Operator runs `apex ingest response_<id>.json`. The CLI validates JSON Schema adherence, structural integrity, and citation links before writing to the wiki directory and updating `apex.run.json`.
    

## 4. Skill Decision

A Skill is **unnecessary for workflow execution** and is strictly relegated to a **semantic guidance package**.

- **Primary Engine:** No.
    
- **Thin Launcher:** No.
    
- **Semantic Guidance Package:** Yes. The Skill contains _only_ prose quality rules, taxonomy rules, macro/meso/micro wiki structural requirements, and synthesis heuristics.
    
- **Workflow Authority:** Zero. The Skill has no access to step routing, state transitions, filesystem navigation, path validation, or completion verification.
    

## 5. CLI Application Contract

The core CLI application exposes the following non-overlapping public subcommands:

Bash

```
# 1. Collect operator choices using canonical template; write config contract
apex init [--config-out apex.config.json] [--non-interactive]

# 2. Validate paths, scan source corpus, build SHA-256 index in run manifest
apex scan --config apex.config.json

# 3. Compile the next deterministic semantic task packet for the LLM
apex packet --run-manifest apex.run.json --out task_latest.json

# 4. Validate and import AI output, update manifest state machine
apex ingest --run-manifest apex.run.json --input response_latest.json

# 5. Execute full non-interactive pipeline (invokes API/headless LLM worker)
apex run --config apex.config.json [--auto]

# 6. Display current legal stage, completed files, and resume position
apex status --run-manifest apex.run.json

# 7. Mechanically audit generated wiki against source SHA-256 hashes & links
apex verify --run-manifest apex.run.json
```

## 6. Semantic Boundary

To prevent AI drift, system responsibilities are strictly partitioned:

```
┌───────────────────────────────────────┬───────────────────────────────────────┐
│     DETERMINISTIC (CLI Owned)         │       SEMANTIC (AI Owned)             │
├───────────────────────────────────────┼───────────────────────────────────────┤
│ • Canonical setup template rendering  │ • Conceptual meaning extraction       │
│ • Path validation & topology mapping  │ • Weighting source authority          │
│ • Corpus file inventory & hashing     │ • Contradiction & ambiguity analysis  │
│ • State transitions & persistence     │ • Synthesis of unstructured ideas     │
│ • Scope chunking & token budgeting    │ • Macro/Meso/Micro wiki writing       │
│ • Work packet compilation             │ • Semantic categorization & tags      │
│ • Structural schema validation        │ • Identification of implicit concepts │
│ • Citation verification & link checks │                                       │
│ • Completion certification            │                                       │
└───────────────────────────────────────┴───────────────────────────────────────┘
```

## 7. Canonical Artifacts

Every artifact in the system has an explicit producer and consumer:

1. **`apex.schema.json`**
    
    - _Producer:_ System repository / build package.
        
    - _Consumer:_ `apex init` and `apex ingest` (Validation contract).
        
2. **`apex.config.json`**
    
    - _Producer:_ `apex init` (Operator choices preserved without reinterpretation).
        
    - _Consumer:_ `apex scan` and `apex run` (Execution scope and paths).
        
3. **`apex.run.json`**
    
    - _Producer:_ `apex scan` and updated by `apex ingest`.
        
    - _Consumer:_ `apex packet`, `apex status`, `apex verify` (Durable state manifest containing file hashes, completed stages, and resume markers).
        
4. **`task_<id>.json`**
    
    - _Producer:_ `apex packet`.
        
    - _Consumer:_ LLM Semantic Worker (Isolated, bounded prompt + corpus context slice).
        
5. **`response_<id>.json`**
    
    - _Producer:_ LLM Semantic Worker.
        
    - _Consumer:_ `apex ingest` (Generated Markdown pages, metadata, and citation mappings).
        
6. **`kb_index.json`**
    
    - _Producer:_ `apex ingest`.
        
    - _Consumer:_ `apex verify` and retrieval queries (Deterministic map of generated wiki topics to source hashes).
        

## 8. Test Strategy

Product-level acceptance testing must validate execution guarantees without reliance on mock LLM assertions:

- **Exact Template Rendering Test:** Run `apex init` in interactive mode via standard IO stream capturing. Verify that output stdout matches the canonical template byte-for-byte and rejects unmapped operator inputs.
    
- **Topology Validation Test:** Execute `apex scan` against relative paths, absolute paths, network paths, and symlinks on both POSIX and Windows systems. Verify fail-fast behavior on missing directories or overlapping source/destination paths.
    
- **Interrupt and Resume Test:** Trigger `apex run`, send `SIGKILL` mid-execution, re-run `apex status`, and execute `apex packet`. Verify that the system resumes at the exact unfulfilled task step in `apex.run.json` without re-indexing or duplicating completed work.
    
- **Structural Ingestion Gate Test:** Feed `apex ingest` intentionally corrupted responses (missing required schema properties, broken Markdown link syntax, non-existent source references). Confirm 100% rejection with zero mutation of `apex.run.json`.
    
- **Zero AI Control Audit:** Run automated transcript and execution trace analysis to confirm that no model output ever dictates stage selection, alters config flags, or bypasses CLI verification gates.
    

## 9. Build Sequence

1. **Milestone 1: Schemas & State Machine Core**
    
    Define `apex.schema.json` contracts for configuration and execution manifests. Build the CLI state machine with atomic JSON reading and writing.
    
2. **Milestone 2: Topology & Config Engine**
    
    Implement `apex init` and `apex scan` with cross-platform path validation, directory indexing, and SHA-256 hash generation.
    
3. **Milestone 3: Packetizer & Ingestion Gate**
    
    Build `apex packet` context slicer and `apex ingest` schema validator to enforce mechanical boundary isolation around AI IO.
    
4. **Milestone 4: Verification Engine**
    
    Implement `apex verify` to deterministically audit wiki file structures, internal links, and source citations against `apex.run.json`.
    
5. **Milestone 5: Headless Orchestrator & CLI Runner**
    
    Implement `apex run` with non-interactive execution modes and optional lifecycle hooks for automated LLM invocation.
    
6. **Milestone 6: Integration Suite & Guidance Packaging**
    
    Build end-to-end acceptance tests (resume, path failure, schema rejection) and author the passive `SKILL.md` semantic writing guide.
    

## 10. Kill List

The following elements must be permanently removed or suppressed:

- **Skill-Driven Lifecycle Logic:** Remove all instructions in `SKILL.md` that tell the model when to proceed, what files to read next, or where to write outputs.
    
- **Chat Memory State:** Eliminate reliance on LLM conversation histories or agent session context for workflow continuity.
    
- **Self-Certifying AI Prompts:** Remove prompt clauses asking the LLM to "verify complete execution" or "confirm directory readiness."
    
- **Large Routing & Handover Documents:** Delete redundant instruction hierarchies, manual recovery guides, and natural-language state descriptions.
    
- **Duplicate Execution Scripts:** Remove ad-hoc helper scripts or wrapper functions that bypass the central CLI state engine.
    

## 11. Uncertainties

### Established Primary-Source Facts

- **Skill Limits:** Agent Skills (open standard) are plain text prompt expansions loaded into the LLM context window; they lack execution sandboxing, deterministic state persistence, or control flow guarantees.
    
- **Lifecycle Hooks:** Platforms like Claude Code support deterministic CLI hooks (`PreToolUse`, `Stop`) via standard IO JSON protocols and exit codes (Exit 0 allow, Exit 2 block).
    
- **Typed Contracts:** JSON Schema provides unambiguous, cross-platform validation for structural data handoffs.
    

### Architectural Judgments

- **CLI Language Selection:** Python with Pydantic/Typer provides fast iteration and native JSON Schema integration; compiling to a single binary via Go/Rust eliminates runtime environment dependencies on target operator machines.
    
- **Semantic Worker Invocation:** A headless API runner inside `apex run` is preferred for speed, but file-based handoff (`task_<id>.json` $\rightarrow$ `response_<id>.json`) provides the highest level of operator transparency and inspection.
    

### Unresolved Choices

- **Rate-Limit Strategy:** The specific backoff and chunk-sizing parameters for processing high-volume token workloads depend on chosen LLM provider quota limits during `apex run`.