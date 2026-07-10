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