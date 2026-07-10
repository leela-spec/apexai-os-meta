Apex-KB_FixesClaude.md

File

ChatHistroy4.md

File

Apex-KB_FixesClaude2.md

File

# Handover Prompt
— Apex KB Planner for Architecture, Process Flow, and Tool/Plugin Inclusion You are GPT-5.5 Thinking acting as the **Apex KB Change Planner**. Your task is **not** to patch the repo directly. Your task is to produce one clear **macro / meso / micro planning report** for the next implementation phase of Apex KB. The report must explain: 1. What the current problems are. 2. What architecture changes are needed. 3. What process-flow changes are needed. 4. Which deterministic tools/plugins/scripts must be included. 5. Exactly how Codex should realize the changes at the micro implementation level. Do **not** redesign Apex KB from scratch. Do **not** re-open accepted decisions. Do **not** add new guardrail systems unless they are strictly required for the next patch. Do **not** drift into parser-library discussion unless directly relevant. Do **not** reintroduce a mandatory operator gate. Do **not** assume four semantic batches. Do **not** hardcode `claude-code-orchestration-design`, `claude-skill-design`, or any KB slug into generic scripts. --- ## 0. Current State Lock The prior chat history shows a repeated failure pattern: the assistant kept losing the active decision stack, re-opening already-decided issues, and drifting from the actual target into surrounding architecture discussions. The latest accepted target is now locked.

```
yaml
APEX_KB_CURRENT_STATE_LOCK:
  target: "Plan the complete change set, but keep the implementation target focused."

  accepted_decisions:
    - "BagIt-style deterministic source manifest is valuable and should be added."
    - "It must be generic, folder/path-derived, not hardcoded to four semantic batches."
    - "Grouping derives from actual raw/ first-level folders."
    - "Files directly under raw/ belong to group: root."
    - "Optional explicit group-map may be allowed."
    - "No semantic inference from filenames."
    - "Do not replace source-manifest.json; add a companion payload manifest."
    - "Preferred companion output: manifests/source-payload-manifest.json."
    - "Place BagIt-style manifest generation after source-intake and before Phase 0."
    - "Work on main only unless the operator explicitly says otherwise."
    - "Do not reintroduce a mandatory operator gate."
    - "One prompt should be able to run the full lifecycle."
    - "Phase1-only / analysis-only mode may exist as optional safe mode, not as default."
    - "Do not discuss markdown-it-py, PyYAML, or python-frontmatter unless directly relevant to the requested planning report."

  current_next_patch:
    primary_file: "apex-meta/scripts/apex_kb.py"
    primary_command_to_add: "generate-source-payload-manifest"
    output_file: "apex-meta/kb/<kb-slug>/manifests/source-payload-manifest.json"

  must_not_reopen:
    - "Whether BagIt-style source manifest makes sense."
    - "Whether grouping should be batch-hardcoded."
    - "Whether operator gate should remain mandatory."
    - "Whether Apex KB should mutate Plan/Sync/Session/PreCap/FlowRecap/APSU state."
```

--- # 1. Required Output Format Produce exactly one report with this structure:

```
markdown
# Apex KB Change Planner Report

## 1. Executive Verdict

## 2. Macro Level — Architecture

## 3. Meso Level — Process Flow

## 4. Micro Level — Implementation Plan

## 5. Tool / Plugin / Script Inclusion Matrix

## 6. Codex Execution Guidelines

## 7. Acceptance Criteria

## 8. Non-Goals and Drift Guards

## 9. Final Codex Prompt
```

The report must be practical and implementation-ready. It must not be a philosophical architecture essay. --- # 2. Problem Statement The core problem is not that Apex KB lacks concepts. The problem is **source-custody and lifecycle control drift**.

```
yaml
current_problem_stack:
  P1_context_drift:
    problem: >
      Prior chats repeatedly lost accepted decisions and reintroduced old issues.
    practical_effect:
      - "Same decisions were re-debated."
      - "BagIt-style manifest was forgotten."
      - "Parser libraries were discussed instead of the accepted manifest tool."
      - "Operator gates were reintroduced after the operator removed them."

  P2_source_custody_weakness:
    problem: >
      The current source manifest/source-intake flow is not yet strong enough as
      the generic custody spine for a full KB lifecycle.
    practical_effect:
      - "Raw source payload cannot be fully proven at root/group/file level."
      - "Phase 1 and Phase 2 cannot robustly prove the exact source set used."
      - "Source drift is hard to detect deterministically."

  P3_lifecycle_fragmentation:
    problem: >
      The lifecycle was described as too many separate stages and gates.
    practical_effect:
      - "The operator-facing process becomes slow."
      - "The system keeps stopping for approval/validation instead of executing the target."
      - "The assistant over-focuses on surrounding process instead of the actual patch."

  P4_tool_inclusion_failure:
    problem: >
      The recommended BagIt-style deterministic source manifest tool/pattern was
      not consistently inserted into the flow.
    practical_effect:
      - "The most relevant ingestion fix was omitted from later plans."
      - "Unrelated parser libraries were discussed instead."
```

--- # 3. Macro Level — Architecture ## 3.1 Target Architecture Apex KB should become a **one-prompt, source-custodied, deterministic-plus-LLM knowledge-base lifecycle**.

```
yaml
target_architecture:
  core_identity: "Durable source-custodied knowledge-base compiler"
  source_of_truth:
    canonical:
      - "raw source files or source pointers"
      - "source-manifest.json"
      - "source-payload-manifest.json"
      - "compiled wiki pages"
    derived:
      - "Phase 0 navigation artifacts"
      - "retrieval indexes"
      - "query outputs"
      - "lint/status/audit reports"

  deterministic_layer:
    owns:
      - "scaffold / ensure KB root"
      - "source intake mechanics"
      - "file hashing"
      - "BagIt-style payload manifest"
      - "Phase 0 corpus navigation"
      - "index rebuild"
      - "retrieval index build"
      - "lint/status/audit mechanics"
    must_not_own:
      - "semantic interpretation"
      - "concept synthesis"
      - "contradiction interpretation"
      - "wiki prose drafting"

  llm_layer:
    owns:
      - "Phase 1 semantic source analysis"
      - "Phase 2 wiki summaries/concepts/entities"
      - "contradiction/open-question interpretation"
      - "query answer synthesis"
    must_not_own:
      - "file hashing"
      - "source custody proof"
      - "deterministic manifest generation"
      - "path-based source grouping"
```

## 3.2 Required Architecture Change Add a new deterministic custody artifact:

```
yaml
new_artifact:
  path: "apex-meta/kb/<kb-slug>/manifests/source-payload-manifest.json"
  purpose:
    - "Prove raw source payload state before Phase 0/Phase 1/Phase 2."
    - "Detect source drift."
    - "Record root/group/file-level hashes."
    - "Make source custody auditable without semantic inference."
```

## 3.3 Existing Manifest Relationship Do not replace `source-manifest.json`.

```
yaml
manifest_split:
  source_manifest_json:
    role:
      - "source_id"
      - "source path / pointer"
      - "source type"
      - "storage mode"
      - "ingest status"
      - "wiki source_refs"
    status: "canonical semantic/source-reference ledger"

  source_payload_manifest_json:
    role:
      - "root aggregate hash"
      - "group aggregate hash"
      - "per-file sha256"
      - "file size"
      - "normalized path"
      - "source drift detection"
    status: "canonical deterministic payload-custody ledger"
```

--- # 4. Meso Level — Process Flow ## 4.1 Simplified Operator-Facing Flow Use four operator-facing macro stages, not ten micro-stages.

```
yaml
operator_facing_flow:
  A_prepare:
    purpose: "Ensure KB root exists and has required structure."
    deterministic: true
    commands:
      - "scaffold / ensure"

  B_ingest_and_analyze:
    purpose: "Bring sources into custody, generate payload manifest, run Phase 0, then produce Phase 1 analysis."
    deterministic_part:
      - "source-intake"
      - "generate-source-payload-manifest"
      - "phase0"
    llm_part:
      - "fill Phase 1 analysis"
    key_rule: "BagIt-style payload manifest runs after source-intake and before Phase 0."

  C_compile:
    purpose: "Compile wiki pages in same full-lifecycle run when authorized by initial prompt."
    default_gate_policy: "No separate mandatory approve-ingest phrase."
    optional_modes:
      - "phase1_only"
      - "compile_only"
      - "legacy_require_approval_phrase only if explicitly requested"

  D_postflight:
    purpose: "Make KB usable and auditable."
    deterministic_part:
      - "index"
      - "retrieval build-index"
      - "lint"
      - "status"
      - "audit"
```

## 4.2 Correct Insertion Point for BagIt-Style Manifest

```
yaml
bagit_insertion_point:
  before:
    - "Phase 0 corpus intelligence"
    - "Phase 1 semantic analysis"
    - "Phase 2 wiki compilation"
  after:
    - "source-intake"
  reason: >
    The payload manifest must prove the raw source state that later phases are
    analyzing or compiling from.
```

## 4.3 No Batch Dependency

```
yaml
grouping_policy:
  default:
    method: "derive from actual first-level folders under raw/"
  fallback:
    direct_files_under_raw: "source_group=root"
  optional:
    explicit_group_map: "allowed only if supplied by operator or checked-in config"
  forbidden:
    - "hardcoded semantic batches"
    - "filename-based semantic group inference"
    - "LLM-decided source groups inside deterministic script"
```

--- # 5. Micro Level — Implementation Plan ## 5.1 Patch Scope

```
yaml
patch_scope:
  required_file:
    - "apex-meta/scripts/apex_kb.py"
  optional_docs_if_needed:
    - ".claude/skills/apex-kb/references/script-command-contract.md"
    - ".claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md"
  forbidden_for_this_patch:
    - "wiki/**"
    - "ingest-analysis/**"
    - "retrieval architecture"
    - "Phase 1/2 templates unless they explicitly contradict the accepted one-prompt flow"
    - "Plan/Sync/Session/PreCap/FlowRecap/APSU state"
```

## 5.2 New Command Add this command to `apex_kb.py`:

```
text
generate-source-payload-manifest
```

Command shape:

```
bash
python apex-meta/scripts/apex_kb.py \
  --kb-root apex-meta/kb/<kb-slug> \
  generate-source-payload-manifest \
  --allow-write \
  --json
```

Optional flags:

```
yaml
optional_flags:
  --raw-root:
    default: "<kb-root>/raw"
    purpose: "Override raw root for special migrations."

  --output:
    default: "<kb-root>/manifests/source-payload-manifest.json"
    purpose: "Override output path if needed."

  --group-map:
    default: null
    purpose: "Optional explicit path/group mapping JSON."

  --stable:
    default: true
    purpose: "Omit volatile generated_at or use deterministic timestamp mode if idempotency requires exact byte-for-byte output."

  --dry-run:
    default: true unless allow-write
    purpose: "Preview manifest without writing."
```

## 5.3 Manifest JSON Shape Use this generic schema:

```
json
{
  "manifest_version": "1.0",
  "schema": "apex-source-payload-manifest",
  "hash_algorithm": "sha256",
  "kb_root": "apex-meta/kb/<kb-slug>",
  "payload_root": "apex-meta/kb/<kb-slug>/raw",
  "aggregate": {
    "level": 1,
    "file_count": 0,
    "total_size_bytes": 0,
    "sha256": "<root-aggregate-hash>"
  },
  "source_groups": [
    {
      "level": 2,
      "group_id": "refs",
      "folder": "raw/refs",
      "file_count": 0,
      "total_size_bytes": 0,
      "sha256": "<group-aggregate-hash>",
      "files": [
        {
          "level": 3,
          "path": "raw/refs/example.md",
          "sha256": "<file-sha256>",
          "size_bytes": 0
        }
      ]
    }
  ]
}
```

## 5.4 Hashing Rules

```
yaml
hashing_rules:
  file_hash:
    method: "sha256 over raw bytes"
  file_record_string:
    fields:
      - "normalized relative path"
      - "sha256"
      - "size_bytes"
    ordering: "stable"
  group_hash:
    method: "sha256 over sorted serialized file records"
  root_hash:
    method: "sha256 over sorted serialized group/file records"
  path_normalization:
    separator: "/"
    base: "kb_root"
  sort_order:
    - "group_id ascending"
    - "path ascending"
```

## 5.5 Exclusion Rules Exclude generated/canonical non-payload folders if scanning broader than raw. If scanning only `raw/`, still ignore obvious junk.

```
yaml
exclude:
  directories:
    - ".git"
    - "__pycache__"
    - ".DS_Store"
  files:
    - ".DS_Store"
  generated_kb_dirs_not_payload:
    - "manifests"
    - "wiki"
    - "ingest-analysis"
    - "derived"
    - "outputs"
    - "audit"
    - "log"
```

## 5.6 Idempotency Rules

```
yaml
idempotency:
  same_input_same_manifest: true
  sorted_paths: true
  normalized_paths: true
  no_random_ids: true
  generated_at:
    recommendation: "omit by default or put under metadata.generated_at only when --include-generated-at is set"
  validation:
    - "run command twice"
    - "diff outputs"
    - "diff must be empty in stable mode"
```

--- # 6. Tool / Plugin / Script Inclusion Matrix | Tool / Pattern | Include? | Role | Implementation Rule | | ------------------------------------------------- | ----------------: | -------------------------------- | ------------------------------------------------------ | | BagIt-style deterministic source payload manifest | Yes | Source custody / drift detection | Add `generate-source-payload-manifest` to `apex_kb.py` | | Python `hashlib` | Yes | SHA-256 hashing | Required stdlib | | Python `pathlib` | Yes | Path handling | Required stdlib | | Python `json` | Yes | Manifest output | Required stdlib | | Python `datetime` | Optional | Metadata timestamp | Avoid by default if exact idempotency matters | | `markdown-it-py` | No for this patch | Markdown parser validation | Do not discuss unless Phase 0 parser work is requested | | PyYAML / python-frontmatter | No for this patch | Frontmatter parsing | Not relevant to payload manifest patch | | SQLite FTS5/BM25 | No for this patch | Retrieval | Postflight/retrieval work, not source custody patch | | Node/remark | No | Markdown AST | Deferred / not relevant | | BagIt external package | No | Full BagIt compliance | Not needed; implement BagIt-style pattern only | --- # 7. Codex Execution Guidelines Codex should implement only the accepted patch target.

```
yaml
codex_rules:
  branch_policy:
    default: "main"
    instruction: "Do not create branch unless operator explicitly changes policy."

  allowed_changes:
    - "apex-meta/scripts/apex_kb.py"
    - "minimal command-contract docs only if required"

  forbidden_changes:
    - "wiki pages"
    - "Phase 1 analysis files"
    - "Phase 2 compile files"
    - "retrieval engine changes"
    - "parser library work"
    - "operator-gate reintroduction"
    - "hardcoded four batch names"

  required_validation:
    - "python -m py_compile apex-meta/scripts/apex_kb.py"
    - "python apex-meta/scripts/apex_kb.py --help"
    - "create temporary KB root"
    - "create raw/refs/a.md, raw/notes/b.md, raw/root-file.md"
    - "run generate-source-payload-manifest --allow-write --json"
    - "verify output file exists"
    - "verify groups: refs, notes, root"
    - "verify per-file sha256 exists"
    - "verify group/root aggregate exists"
    - "run command twice in stable mode"
    - "verify diff empty"
```

--- # 8. Acceptance Criteria

```
yaml
acceptance_criteria:
  command_surface:
    - "generate-source-payload-manifest appears in --help"

  manifest_output:
    - "source-payload-manifest.json is written under manifests/"
    - "contains aggregate level 1"
    - "contains source_groups level 2"
    - "contains files level 3"
    - "contains sha256 for each file"
    - "contains size_bytes for each file"
    - "uses normalized POSIX paths"

  grouping:
    - "first-level raw folders become groups"
    - "direct files under raw become group root"
    - "no semantic batch names are inferred"

  determinism:
    - "same source tree produces same manifest in stable mode"
    - "paths sorted"
    - "aggregate hashes stable"

  boundaries:
    - "no wiki files changed"
    - "no ingest-analysis files changed"
    - "no retrieval files changed"
    - "no Plan/Sync/Session/PreCap/FlowRecap/APSU files changed"

  lifecycle_integration:
    - "documented placement after source-intake and before Phase 0"
```

--- # 9. Non-Goals and Drift Guards

```
yaml
non_goals:
  - "Do not redesign the full Apex KB skill."
  - "Do not rebuild retrieval."
  - "Do not add vector search."
  - "Do not create semantic source batches."
  - "Do not add mandatory approval phrase."
  - "Do not create wiki pages."
  - "Do not perform Phase 1 or Phase 2 work."
  - "Do not debate whether BagIt-style source custody is useful."

drift_guards:
  if_about_to_discuss_parser_libraries:
    action: "stop unless directly required"
  if_about_to_discuss_operator_gate:
    action: "stop unless directly required"
  if_about_to_discuss_four_batches:
    action: "state that groups derive from folders, then move on"
  if_about_to_request_new_architecture_research:
    action: "stop; current accepted patch is already known"
```

--- # 10. Final Codex Prompt Use this exact prompt for Codex after the planner report is accepted.

```
text
You are Codex working in leela-spec/apexai-os-meta.

Hard rule:
Work on main only. Do not create a branch. Do not open a PR. Do not redesign Apex KB.

Start:
cd C:\GitDev\apexai-os-meta
git checkout main
git pull --ff-only
git status --short --branch

Mission:
Patch Apex KB source custody by adding a generic BagIt-style deterministic source payload manifest generator.

Patch target:
apex-meta/scripts/apex_kb.py

Do not touch:
- wiki/**
- ingest-analysis/**
- retrieval scripts
- Phase 1/Phase 2 logic
- parser libraries
- operator-gate logic
- Plan/Sync/Session/PreCap/FlowRecap/APSU files

Add command:
generate-source-payload-manifest

Command behavior:
- Uses global --kb-root.
- Defaults raw root to <kb-root>/raw.
- Defaults output to <kb-root>/manifests/source-payload-manifest.json.
- Supports --dry-run.
- Writes only with --allow-write.
- Supports --json.
- Optional --raw-root override is acceptable.
- Optional --output override is acceptable.
- Optional --group-map is acceptable only if simple.

Manifest behavior:
- Scan raw/ recursively.
- Derive source groups from actual first-level folders under raw/.
- Files directly under raw/ go into group "root".
- Never infer semantic batch names.
- Never hardcode the four old Phase 1 batch names.
- Compute sha256 per file over raw bytes.
- Include file size in bytes.
- Normalize paths to POSIX separators.
- Sort paths deterministically.
- Compute group aggregate hash from sorted file records.
- Compute root aggregate hash from sorted group/file records.
- Output JSON to manifests/source-payload-manifest.json.
- Stable mode must produce byte-identical output on rerun.

Expected JSON structure:
{
  "manifest_version": "1.0",
  "schema": "apex-source-payload-manifest",
  "hash_algorithm": "sha256",
  "kb_root": "...",
  "payload_root": "...",
  "aggregate": {
    "level": 1,
    "file_count": 0,
    "total_size_bytes": 0,
    "sha256": "..."
  },
  "source_groups": [
    {
      "level": 2,
      "group_id": "...",
      "folder": "raw/...",
      "file_count": 0,
      "total_size_bytes": 0,
      "sha256": "...",
      "files": [
        {
          "level": 3,
          "path": "raw/.../file.md",
          "sha256": "...",
          "size_bytes": 0
        }
      ]
    }
  ]
}

Validation:
1. python -m py_compile apex-meta/scripts/apex_kb.py
2. python apex-meta/scripts/apex_kb.py --help
3. Create temporary KB root: apex-meta/kb/_tmp-payload-manifest-test/
4. Create:
   - raw/refs/a.md
   - raw/notes/b.md
   - raw/root-file.md
5. Run generate-source-payload-manifest with --allow-write --json
6. Verify output exists at manifests/source-payload-manifest.json
7. Verify groups include refs, notes, root
8. Verify all three files have sha256 and size_bytes
9. Run command twice
10. Verify stable output diff is empty
11. Delete temporary KB root if safe
12. git diff must show only intended changes

Commit only if validation passes.

Final output:
PATCH_REPORT:
  branch: main
  commit_sha:
  files_changed:
  command_added:
  manifest_output_path:
  grouping_behavior:
  hash_behavior:
  idempotency_result:
  validation_commands:
  remaining_gaps:
```

Thought for 10s

# Apex KB Change Planner Report

## 1. Executive Verdict

The next implementation phase should be a **focused source-custody patch**, not a lifecycle redesign.

The current architectural problem is not missing concepts, missing parser libraries, or missing retrieval ambition. The actual failure is:

```
verdict:  root_problem: "source-custody and lifecycle-control drift"  next_patch_type: "surgical deterministic CLI extension"  primary_file: "apex-meta/scripts/apex_kb.py"  command_to_add: "generate-source-payload-manifest"  output: "apex-meta/kb/<kb-slug>/manifests/source-payload-manifest.json"  implementation_policy:    - "generic --kb-root based"    - "folder/path-derived grouping"    - "no hardcoded KB slug"    - "no hardcoded four semantic batches"    - "no mandatory operator gate reintroduction"    - "no parser-library discussion"    - "no retrieval-engine patching"
```

The accepted BagIt-style source payload manifest should be added as a **companion deterministic custody artifact** beside `source-manifest.json`.

`source-manifest.json` remains the semantic/source-reference ledger.  
`source-payload-manifest.json` becomes the deterministic raw-payload custody ledger.

This patch should make later Phase 0, Phase 1, Phase 2, retrieval, lint, and audit runs able to prove the exact raw source payload state they operated on.

## 2. Macro Level — Architecture

### 2.1 Target Architecture

Apex KB should operate as a:

```
target_architecture:  identity: "one-prompt, source-custodied, deterministic-plus-LLM KB compiler"  core_rule: "deterministic tools prove custody; LLMs synthesize meaning"
```

The architecture should preserve the existing ownership split:

```
deterministic_layer:  owns:    - scaffold / ensure KB root    - source intake mechanics    - source hashing    - payload manifest generation    - Phase 0 corpus navigation artifacts    - index rebuilds    - retrieval index builds    - lint / status / audit mechanics  must_not_own:    - semantic interpretation    - concept synthesis    - contradiction interpretation    - wiki prose draftingllm_layer:  owns:    - Phase 1 semantic source analysis    - Phase 2 wiki summaries / concepts / entities    - contradiction and open-question interpretation    - query answer synthesis  must_not_own:    - raw file hashing    - source custody proof    - deterministic grouping    - aggregate hash generation
```

### 2.2 Required Architecture Change

Add one deterministic custody artifact:

```
new_artifact:  path: "apex-meta/kb/<kb-slug>/manifests/source-payload-manifest.json"  role: "canonical deterministic payload-custody ledger"  purpose:    - "prove exact raw source payload state"    - "record per-file hashes and sizes"    - "record group-level aggregate hashes"    - "record root-level aggregate hash"    - "detect source drift before semantic or retrieval work"
```

### 2.3 Manifest Split

Do **not** replace `source-manifest.json`.

```
source_manifest_json:  role:    - source_id ledger    - source path / pointer ledger    - source type    - storage mode    - ingest status    - source_refs for wiki pages  nature: "semantic/source-reference custody"source_payload_manifest_json:  role:    - raw payload file inventory    - per-file sha256    - per-file byte size    - group aggregate sha256    - root aggregate sha256    - source drift detection  nature: "deterministic payload custody"
```

### 2.4 Generic Grouping Architecture

Grouping must be derived from the filesystem, not inferred semantically.

```
grouping_architecture:  default_grouping:    method: "first-level folder under raw/"    examples:      - "raw/refs/a.md -> group refs"      - "raw/notes/b.md -> group notes"  root_file_grouping:    rule: "files directly under raw/ belong to group root"    example: "raw/root-file.md -> group root"  optional_override:    group_map: "allowed only if explicit JSON is supplied"  forbidden:    - "hardcoded four Phase 1 batch names"    - "semantic grouping by filename"    - "LLM-decided grouping inside deterministic script"    - "KB-slug-specific logic"
```

## 3. Meso Level — Process Flow

### 3.1 Simplified Operator-Facing Lifecycle

The operator-facing process should be four macro stages, not ten separate gates.

```
operator_facing_flow:  A_prepare:    purpose: "Ensure KB root exists and has required structure."    deterministic:      - scaffold      - health / status if available  B_ingest_and_analyze:    purpose: "Bring sources into custody, prove payload state, run Phase 0, then produce Phase 1 analysis."    deterministic:      - source-intake      - generate-source-payload-manifest      - phase0    llm:      - ingest-phase1 semantic analysis    key_rule: "payload manifest runs after source-intake and before Phase 0"  C_compile:    purpose: "Compile wiki pages in the same full-lifecycle run when authorized by the initial prompt."    llm:      - ingest-phase2 wiki compile    gate_policy:      default: "no new mandatory separate approve-ingest phrase for the one-prompt lifecycle"      optional: "phase1_only mode may stop before compile"  D_postflight:    purpose: "Make the KB usable and auditable."    deterministic:      - index      - retrieval build-index      - query if requested      - lint      - status      - audit
```

### 3.2 Correct Manifest Insertion Point

```
payload_manifest_insertion:  after:    - source-intake  before:    - phase0    - ingest-phase1    - ingest-phase2    - retrieval build-index    - query    - lint / audit claims about source freshness
```

Reason:

```
reason:  - "Phase 0 should navigate a proven raw payload, not an implicit folder state."  - "Phase 1 should cite sources whose payload state is recorded."  - "Phase 2 should compile from sources whose hashes are auditable."  - "Retrieval should be rebuildable against known compiled pages and known source custody."
```

### 3.3 Lifecycle Control Fix

The full lifecycle should be runnable from one operator prompt, while still allowing safe modes.

```
lifecycle_modes:  default_full_lifecycle:    behavior: "run prepare -> ingest/analyze -> compile if authorized -> postflight"  optional_phase1_only:    behavior: "stop after Phase 1 analysis"    purpose: "safe review mode"    status: "optional, not default"  optional_compile_only:    behavior: "compile from existing approved Phase 1 analysis"    purpose: "resume mode"  legacy_require_approval_phrase:    behavior: "only if explicitly requested by operator"    status: "not default"
```

## 4. Micro Level — Implementation Plan

### 4.1 Patch Scope

```
patch_scope:  required:    - "apex-meta/scripts/apex_kb.py"  optional_minimal_docs:    - ".claude/skills/apex-kb/references/script-command-contract.md"    - ".claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md"  forbidden_for_this_patch:    - "wiki/**"    - "ingest-analysis/**"    - "retrieval scripts"    - "Phase 1 templates"    - "Phase 2 templates"    - "Plan/Sync/Session/PreCap/FlowRecap/APSU files"    - "parser-library changes"
```

### 4.2 New CLI Command

Add:

```
python apex-meta/scripts/apex_kb.py \  --kb-root apex-meta/kb/<kb-slug> \  generate-source-payload-manifest \  --allow-write \  --json
```

Command requirements:

```
command_requirements:  name: "generate-source-payload-manifest"  uses_global_kb_root: true  default_raw_root: "<kb-root>/raw"  default_output: "<kb-root>/manifests/source-payload-manifest.json"  writes_only_with_allow_write: true  supports_json_output: true  stable_by_default: true
```

Recommended flags:

```
flags:  --raw-root:    required: false    default: "<kb-root>/raw"    purpose: "override payload root for migrations or tests"  --output:    required: false    default: "<kb-root>/manifests/source-payload-manifest.json"    purpose: "override output path"  --group-map:    required: false    default: null    purpose: "optional explicit path/group mapping JSON"  --dry-run:    required: false    default: true unless --allow-write is present    purpose: "preview without writing"  --include-generated-at:    required: false    default: false    purpose: "only include volatile timestamp if explicitly requested"
```

### 4.3 Manifest JSON Shape

Implement this shape:

```
{  "manifest_version": "1.0",  "schema": "apex-source-payload-manifest",  "hash_algorithm": "sha256",  "kb_root": "apex-meta/kb/<kb-slug>",  "payload_root": "apex-meta/kb/<kb-slug>/raw",  "aggregate": {    "level": 1,    "file_count": 0,    "total_size_bytes": 0,    "sha256": "<root-aggregate-hash>"  },  "source_groups": [    {      "level": 2,      "group_id": "refs",      "folder": "raw/refs",      "file_count": 0,      "total_size_bytes": 0,      "sha256": "<group-aggregate-hash>",      "files": [        {          "level": 3,          "path": "raw/refs/example.md",          "sha256": "<file-sha256>",          "size_bytes": 0        }      ]    }  ]}
```

### 4.4 Hashing Rules

```
hashing_rules:  file_hash:    method: "sha256 over raw bytes"  file_record_string:    serialized_fields:      - "normalized relative path"      - "sha256"      - "size_bytes"    serialization: "stable JSON with sorted keys or explicit delimiter format"  group_hash:    method: "sha256 over sorted serialized file records"  root_hash:    method: "sha256 over sorted serialized group records"  path_normalization:    separator: "/"    base: "kb_root"    output_paths: "relative POSIX paths"  sorting:    groups: "group_id ascending"    files: "path ascending"
```

### 4.5 Grouping Algorithm

Implementation logic:

```
# Pseudocode onlyfor file in raw_root.rglob("*"):    if file is directory:        continue    if excluded(file):        continue    rel_to_raw = file.relative_to(raw_root)    if len(rel_to_raw.parts) == 1:        group_id = "root"        folder = "raw"    else:        group_id = rel_to_raw.parts[0]        folder = f"raw/{group_id}"    record = {        "level": 3,        "path": posix_path_relative_to_kb_root(file),        "sha256": sha256_bytes(file),        "size_bytes": file.stat().st_size    }    add record to source_groups[group_id]
```

### 4.6 Exclusion Rules

When scanning `raw/`, ignore obvious local junk:

```
exclude_inside_raw:  directories:    - ".git"    - "__pycache__"  files:    - ".DS_Store"    - "Thumbs.db"
```

If implementation allows scanning broader than `raw/`, also exclude generated KB folders:

```
exclude_if_broader_scan:  generated_kb_dirs:    - "manifests"    - "wiki"    - "ingest-analysis"    - "derived"    - "outputs"    - "audit"    - "log"
```

### 4.7 Idempotency Rules

```
idempotency_rules:  stable_default: true  no_random_ids: true  no_generated_at_by_default: true  sorted_paths: true  sorted_groups: true  normalized_paths: true  same_input_same_bytes: true
```

Validation must include:

```
idempotency_validation:  - "run command once"  - "copy output to temp file"  - "run command again"  - "diff output against temp file"  - "diff must be empty"
```

### 4.8 JSON Output Behavior

When `--json` is supplied, command should emit a compact machine-readable report:

```
{  "ok": true,  "command": "generate-source-payload-manifest",  "kb_root": "apex-meta/kb/<kb-slug>",  "payload_root": "apex-meta/kb/<kb-slug>/raw",  "output": "apex-meta/kb/<kb-slug>/manifests/source-payload-manifest.json",  "dry_run": false,  "file_count": 3,  "group_count": 3,  "groups": ["notes", "refs", "root"],  "sha256": "<root-aggregate-hash>"}
```

## 5. Tool / Plugin / Script Inclusion Matrix

|Tool / Pattern|Include?|Role|Implementation Rule|
|---|---|---|---|
|BagIt-style deterministic source payload manifest|Yes|Payload custody / drift detection|Add `generate-source-payload-manifest` to `apex_kb.py`|
|Python `hashlib`|Yes|SHA-256 file and aggregate hashing|Required stdlib|
|Python `pathlib`|Yes|Cross-platform path handling|Required stdlib|
|Python `json`|Yes|Stable JSON output|Required stdlib|
|Python `argparse`|Yes|CLI subcommand integration|Use existing parser style|
|Python `datetime`|Optional|Optional timestamp metadata|Do not use by default|
|`markdown-it-py`|No|Markdown parser validation|Not relevant to this patch|
|PyYAML / python-frontmatter|No|Frontmatter parsing|Not relevant to payload manifest|
|SQLite FTS5/BM25|No|Retrieval|Postflight/retrieval layer, not this patch|
|Node/remark|No|Markdown AST|Deferred / not relevant|
|External BagIt package|No|Full BagIt compliance|Not needed; implement BagIt-style pattern only|
|GitHub connector|No for implementation|Repo inspection if needed|Codex/local repo is the execution surface|
|Web search|No|External facts|Not needed for this locked patch|
|LLM semantic analysis|No|Meaning extraction|Forbidden inside deterministic command|

## 6. Codex Execution Guidelines

Codex should implement only the accepted patch target.

```
codex_execution_policy:  repo: "leela-spec/apexai-os-meta"  local_path: "C:\\GitDev\\apexai-os-meta"  branch_policy:    default: "main"    rule: "work on main only unless operator explicitly says otherwise"  implementation_target:    - "apex-meta/scripts/apex_kb.py"  optional_docs:    - ".claude/skills/apex-kb/references/script-command-contract.md"    - ".claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md"  forbidden_changes:    - "wiki/**"    - "ingest-analysis/**"    - "retrieval scripts"    - "Phase 1 logic"    - "Phase 2 logic"    - "parser libraries"    - "operator-gate logic"    - "Plan/Sync/Session/PreCap/FlowRecap/APSU files"    - "hardcoded four batch names"
```

Required validation:

```
required_validation:  static:    - "python -m py_compile apex-meta/scripts/apex_kb.py"    - "python apex-meta/scripts/apex_kb.py --help"    - "confirm generate-source-payload-manifest appears in help"  temp_kb_test:    setup:      - "create apex-meta/kb/_tmp-payload-manifest-test/raw/refs/a.md"      - "create apex-meta/kb/_tmp-payload-manifest-test/raw/notes/b.md"      - "create apex-meta/kb/_tmp-payload-manifest-test/raw/root-file.md"    run:      - "python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/_tmp-payload-manifest-test generate-source-payload-manifest --allow-write --json"    verify:      - "output exists at manifests/source-payload-manifest.json"      - "groups include refs, notes, root"      - "all files have sha256"      - "all files have size_bytes"      - "aggregate hash exists"      - "group hashes exist"  idempotency:    - "run command twice"    - "diff outputs"    - "diff must be empty"  cleanup:    - "delete temporary KB root if safe"  diff_boundary:    - "git diff must show only intended changes"
```

## 7. Acceptance Criteria

```
acceptance_criteria:  command_surface:    - "generate-source-payload-manifest appears in --help"    - "command accepts --raw-root if implemented"    - "command accepts --output if implemented"    - "command writes only with --allow-write"  manifest_output:    - "writes manifests/source-payload-manifest.json"    - "contains manifest_version"    - "contains schema apex-source-payload-manifest"    - "contains hash_algorithm sha256"    - "contains aggregate level 1"    - "contains source_groups level 2"    - "contains files level 3"    - "contains sha256 for every file"    - "contains size_bytes for every file"    - "uses normalized POSIX paths"  grouping:    - "first-level folders under raw become groups"    - "direct files under raw become group root"    - "no semantic group inference"    - "no hardcoded four batch names"    - "no hardcoded KB slug"  determinism:    - "same source tree produces byte-identical manifest in stable mode"    - "paths are sorted"    - "groups are sorted"    - "aggregate hashes are stable"  boundaries:    - "no wiki files changed"    - "no ingest-analysis files changed"    - "no retrieval files changed"    - "no operator gate reintroduced"    - "no Plan/Sync/Session/PreCap/FlowRecap/APSU files changed"  lifecycle_integration:    - "placement documented after source-intake and before Phase 0"    - "source-manifest.json remains unchanged in role"    - "source-payload-manifest.json is companion artifact, not replacement"
```

## 8. Non-Goals and Drift Guards

```
non_goals:  - "Do not redesign Apex KB."  - "Do not rebuild retrieval."  - "Do not add vector search."  - "Do not add parser libraries."  - "Do not create semantic source batches."  - "Do not add a mandatory approval phrase."  - "Do not create wiki pages."  - "Do not perform Phase 1 or Phase 2 work."  - "Do not mutate Plan/Sync/Session/PreCap/FlowRecap/APSU state."  - "Do not debate whether BagIt-style source custody is useful."drift_guards:  if_about_to_discuss_parser_libraries:    action: "stop; not relevant to payload manifest"  if_about_to_discuss_operator_gate:    action: "stop; do not reintroduce mandatory gate"  if_about_to_discuss_four_batches:    action: "state groups derive from raw/ folders, then continue"  if_about_to_hardcode_kb_slug:    action: "replace with --kb-root generic behavior"  if_about_to_patch_retrieval:    action: "stop; retrieval is not in patch scope"  if_about_to_write_wiki_or_ingest_analysis:    action: "stop; semantic artifacts are forbidden in this patch"  if_about_to_request_new_architecture_research:    action: "stop; accepted patch is already known"
```

## 9. Final Codex Prompt

```
You are Codex working in leela-spec/apexai-os-meta.Hard rule:Work on main only. Do not create a branch. Do not open a PR. Do not redesign Apex KB.Start:cd C:\GitDev\apexai-os-metagit checkout maingit pull --ff-onlygit status --short --branchMission:Patch Apex KB source custody by adding a generic BagIt-style deterministic source payload manifest generator.Patch target:apex-meta/scripts/apex_kb.pyDo not touch:- wiki/**- ingest-analysis/**- retrieval scripts- Phase 1/Phase 2 logic- parser libraries- operator-gate logic- Plan/Sync/Session/PreCap/FlowRecap/APSU filesAdd command:generate-source-payload-manifestCommand behavior:- Uses global --kb-root.- Defaults raw root to <kb-root>/raw.- Defaults output to <kb-root>/manifests/source-payload-manifest.json.- Supports --dry-run.- Writes only with --allow-write.- Supports --json.- Optional --raw-root override is acceptable.- Optional --output override is acceptable.- Optional --group-map is acceptable only if simple.- Stable mode must be default.- Do not include generated_at unless a separate explicit flag is added.Manifest behavior:- Scan raw/ recursively.- Derive source groups from actual first-level folders under raw/.- Files directly under raw/ go into group "root".- Never infer semantic batch names.- Never hardcode the four old Phase 1 batch names.- Never hardcode claude-code-orchestration-design, claude-skill-design, or any KB slug.- Compute sha256 per file over raw bytes.- Include file size in bytes.- Normalize paths to POSIX separators.- Sort paths deterministically.- Compute group aggregate hash from sorted file records.- Compute root aggregate hash from sorted group records.- Output JSON to manifests/source-payload-manifest.json.- Stable mode must produce byte-identical output on rerun.Expected JSON structure:{  "manifest_version": "1.0",  "schema": "apex-source-payload-manifest",  "hash_algorithm": "sha256",  "kb_root": "...",  "payload_root": "...",  "aggregate": {    "level": 1,    "file_count": 0,    "total_size_bytes": 0,    "sha256": "..."  },  "source_groups": [    {      "level": 2,      "group_id": "...",      "folder": "raw/...",      "file_count": 0,      "total_size_bytes": 0,      "sha256": "...",      "files": [        {          "level": 3,          "path": "raw/.../file.md",          "sha256": "...",          "size_bytes": 0        }      ]    }  ]}Validation:1. python -m py_compile apex-meta/scripts/apex_kb.py2. python apex-meta/scripts/apex_kb.py --help3. Confirm generate-source-payload-manifest appears in help.4. Create temporary KB root: apex-meta/kb/_tmp-payload-manifest-test/5. Create:   - raw/refs/a.md   - raw/notes/b.md   - raw/root-file.md6. Run:   python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/_tmp-payload-manifest-test generate-source-payload-manifest --allow-write --json7. Verify output exists at:   apex-meta/kb/_tmp-payload-manifest-test/manifests/source-payload-manifest.json8. Verify groups include refs, notes, root.9. Verify all three files have sha256 and size_bytes.10. Verify group hashes and root aggregate hash exist.11. Run command twice.12. Verify stable output diff is empty.13. Delete temporary KB root if safe.14. git diff must show only intended changes.Commit only if validation passes.Final output:PATCH_REPORT:  branch: main  commit_sha:  files_changed:  command_added:  manifest_output_path:  grouping_behavior:  hash_behavior:  idempotency_result:  validation_commands:  remaining_gaps:
```

![58f460f7-85b3-46b6-9795-2922830b3d6d.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000862c71f49294d5d576897c7b&ts=495301&p=fs&cid=1&sig=9aedc05659f5c23118fa09af8da3bb12a0d17809d71ce6c2742aa74e85c832b2&v=0)

explain to me why these are not included: give options recommednations and alternatives each with their own value and cost estiamte and if the are not part of the prcoess already

Thought for 9s

The key point: **“No” here means “not included in this specific custody patch,” not “never useful for Apex KB.”**  
This patch’s job is narrow: prove the exact raw payload state under `raw/` with hashes and deterministic grouping. Anything that parses meaning, builds retrieval, browses externally, or writes semantic artifacts belongs to another lifecycle layer.

## Inclusion Logic

```
current_patch:  purpose: "deterministic raw source payload custody"  command: "generate-source-payload-manifest"  owns:    - scan raw/    - derive groups from folders    - hash files    - compute aggregate hashes    - write source-payload-manifest.json  does_not_own:    - markdown parsing    - frontmatter parsing    - retrieval    - semantic analysis    - external research    - repo/GitHub writes
```

---

## Excluded / Deferred Tools Explained

|Tool / Pattern|Why not in this patch|Already part of broader process?|Value if added|Cost estimate|Recommendation|
|---|---|---|---|---|---|
|`markdown-it-py`|Payload manifest hashes raw files. It does not need to understand Markdown structure.|Partly: useful for Phase 0 V1.5 parser validation.|Medium|Low–Medium, ~2–5h integration/testing|Defer. Add only to Phase 0 parser validation if current simple parser fails on real Markdown edge cases.|
|PyYAML / `python-frontmatter`|Payload custody must not parse frontmatter. It only records bytes, paths, sizes, hashes.|Partly: useful for wiki/frontmatter lint and retrieval metadata.|Medium–High|Medium, ~3–8h plus dependency policy|Defer. Consider for lint/retrieval if stdlib parsing becomes fragile. Do not include in custody command.|
|SQLite FTS5/BM25|Retrieval index belongs after wiki compilation, not before source custody.|Yes, broader retrieval layer.|High|Medium–High, ~1–2 days with runtime probe and fallback|Keep as postflight/retrieval work. Not part of this PR.|
|Node/remark|Markdown AST parsing is unrelated to file hashing. Adds Node dependency chain.|Not core; possible future parser spike only.|Medium|High, ~1–3 days because dependency/runtime expands|Avoid for now. Only use if Python parser/markdown-it-py cannot handle corpus structure.|
|External BagIt package|We need BagIt-style custody, not full BagIt compliance. External package adds dependency and schema lock-in.|No.|Low–Medium|Medium, ~4–10h plus dependency review|Do not use. Implement minimal BagIt-style hash ledger with stdlib.|
|GitHub connector|Implementation must run in local Codex/repo context. Connector can inspect files, but cannot reliably run local validation.|Yes, useful for repo inspection and PR review.|Medium|Low for inspection; high risk if used as execution substitute|Use for audit/review only. Do not make it part of deterministic lifecycle.|
|Web search|This patch uses locked project decisions and local files. External facts are irrelevant.|Only for external research phases.|Low here|Medium due to drift/noise|Do not use. It would create scope drift.|
|LLM semantic analysis|The manifest must be deterministic and non-semantic. LLM grouping would reintroduce drift.|Yes, Phase 1/Phase 2.|High in correct layer|High token/process cost|Keep in Phase 1/2 only. Never inside payload manifest generation.|

---

## Per-Tool Detail

### 1. `markdown-it-py`

**Why excluded:**  
The source payload manifest asks: “What files exist, what are their hashes, and how are they grouped by folder?” It does not ask: “What headings, links, or code blocks are inside this Markdown?”

**Best alternative:**  
Use a simple Python scanner for Phase 0 V1, then optionally add `markdown-it-py` as a **validator** for headings/links/code-block boundaries.

```
recommendation:  current_patch: exclude  later_layer: "Phase 0 corpus intelligence V1.5"  trigger_to_add:    - "simple parser misses heading/link boundaries"    - "MDX-heavy corpus creates parser warnings"
```

---

### 2. PyYAML / `python-frontmatter`

**Why excluded:**  
The payload manifest must hash the raw bytes exactly. Parsing YAML/frontmatter would mix semantic/metadata interpretation into custody.

**Where it belongs:**  
Frontmatter parsing is valuable for:

```
good_use_cases:  - wiki page lint  - query packet validation  - retrieval metadata extraction  - source_refs validation  - confidence / claim_label checks
```

**Recommendation:**  
Do **not** add it to `generate-source-payload-manifest`. Consider it later for `lint`, `status`, or retrieval metadata if manual/stdlib parsing becomes brittle.

---

### 3. SQLite FTS5/BM25

**Why excluded:**  
FTS5/BM25 indexes compiled KB pages for retrieval. This patch proves raw source custody **before** Phase 0/Phase 1/Phase 2.

Correct sequence:

```
sequence:  1_source_intake: "copy/pointer/register sources"  2_payload_manifest: "prove raw payload state"  3_phase0: "deterministic navigation"  4_phase1: "semantic analysis"  5_phase2: "wiki compile"  6_retrieval: "FTS5/BM25 over compiled pages"
```

**Recommendation:**  
Keep SQLite FTS5/BM25 as a postflight layer. It is important, but not for this PR.

---

### 4. Node/remark

**Why excluded:**  
Node/remark is useful for Markdown AST extraction, but this command does not parse Markdown. Adding Node would expand runtime assumptions and increase maintenance surface.

**Alternative stack:**

```
parser_path:  V1: "Python stdlib state-machine parser"  V1_5: "markdown-it-py validator"  V2_if_needed: "Node/remark only if Python path fails materially"
```

**Recommendation:**  
Avoid for now. Node/remark is too heavy for a custody patch.

---

### 5. External BagIt Package

**Why excluded:**  
The accepted decision is **BagIt-style**, not full BagIt compliance. Full BagIt introduces conventions and files we do not need.

What we need:

```
needed:  - per-file sha256  - group aggregate hashes  - root aggregate hash  - stable JSON  - folder-derived grouping
```

What full BagIt may add unnecessarily:

```
not_needed_now:  - bagit.txt  - tagmanifest files  - payload manifests in BagIt-specific layout  - package-specific validation semantics
```

**Recommendation:**  
Use stdlib `hashlib`, `pathlib`, and `json`. Keep it Apex-native.

---

### 6. GitHub Connector

**Why excluded from implementation:**  
The connector is good for reading repo files and reviewing PRs. It is not the right executor for local deterministic validation because it cannot reliably run:

```
python -m py_compilepython apex-meta/scripts/apex_kb.py ...diff output1 output2
```

**Recommendation:**  
Use GitHub connector for:

```
good_use:  - inspect current files  - review PR diffs  - verify merged files  - comment on PRs
```

Do not make it part of the Apex KB lifecycle itself.

---

### 7. Web Search

**Why excluded:**  
The patch is based on locked internal decisions. Web search would add fresh but irrelevant external input and increase decision drift.

**Recommendation:**  
Use web search only for external research questions, such as current Claude Code docs or library behavior. Not for a deterministic Apex repo patch.

---

### 8. LLM Semantic Analysis

**Why excluded:**  
The manifest must be reproducible without model judgment. If an LLM decides groups, source importance, or file meaning, source custody becomes non-deterministic again.

**Correct use of LLMs:**

```
llm_layer:  phase1:    - source relevance judgment    - concept extraction    - contradictions    - open questions  phase2:    - wiki summaries    - concepts    - entities    - synthesis
```

**Recommendation:**  
Keep LLM semantic work after payload custody and Phase 0.

---

## Practical Roadmap

```
roadmap:  patch_1_now:    name: "source payload manifest"    tools:      - hashlib      - pathlib      - json      - argparse    output:      - manifests/source-payload-manifest.json  patch_2_later:    name: "Phase 0 parser hardening"    candidate_tools:      - markdown-it-py      - optional frontmatter parser    trigger:      - parser warnings      - MDX/code-block failures      - bad heading/link maps  patch_3_later:    name: "retrieval postflight"    candidate_tools:      - SQLite FTS5/BM25      - JSON fallback    trigger:      - compiled wiki pages exist      - query layer needs ranking  patch_4_only_if_needed:    name: "heavy parser / AST pipeline"    candidate_tools:      - Node/remark    trigger:      - Python parser and markdown-it-py fail materially
```

## Recommendation

For the current PR, keep the tool set minimal:

```
include_now:  - hashlib  - pathlib  - json  - argparseexclude_now:  - markdown-it-py  - PyYAML  - python-frontmatter  - SQLite FTS5/BM25  - Node/remark  - external BagIt package  - web search  - LLM semantic analysis
```

This keeps the patch small, deterministic, auditable, and hard to drift.