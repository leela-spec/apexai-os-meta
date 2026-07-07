# Apex KB v3 P0–P2 Closure Patch Plan

## 1. Executive Verdict

All P0–P2 items **can be safely included in one patch pack**, provided the pack is split into one Git-generated patch per target file and the P2 items are implemented as **additive deterministic/reporting surfaces**, not as broad semantic rewrites.

```yaml
executive_verdict:
  can_include_all_p0_p2_in_one_patch_pack: true
  preparation_needed_first: false
  recommended_patch_pack_root: "apex-meta/patches/apex-kb-v3-p0-p2-closure/"
  recommended_order:
    - "CLI flag/output compatibility"
    - "pointer_only Phase 0 handling"
    - "wiki/retrieval/payload freshness split"
    - "quality/coverage command"
    - "existing-page repair candidate flow"
    - "query-eval pack"
    - "PowerShell-safe JSON documentation/output path"
    - "lifecycle state-lock and target-drift gates"
    - "graph/process-flow extraction"
    - "docs, templates, acceptance tests"
  highest_risk_item: "P2 graph/process-flow extraction"
  graph_risk_reason: >
    Useful graph signals exist, but correct extraction requires YAML/path/process/contract
    edges, not just Markdown links. Keep it deterministic, additive, and non-blocking.
```

Current v3 is **near-final but not closed**: source-payload manifest, v3 lifecycle docs, retrieval integration, and Phase 2 value contract are already present, but CLI resilience, pointer-only Phase 0, quality/coverage, query eval, and freshness separation remain incomplete. The saved audit explicitly classifies v3 as “near_final_but_not_closed” with those blockers.

The live skill confirms the canonical package is `.claude/skills/apex-kb/`, with `raw/`, `manifests/source-manifest.json`, `manifests/source-payload-manifest.json`, `wiki/`, `audit/`, and `log/` as canonical paths, while `manifests/phase0/`, `derived/search/`, and `outputs/queries/` are derived paths. It also confirms the v3 operator flow already includes `A_prepare`, `B_ingest_and_compile`, `C_postflight`, and `D_query_or_maintain`, with `quality / coverage report` expected in postflight.

The patch-pack method should follow the uploaded Git-native process: Agent Mode creates patch artifacts only; Codex/terminal later applies them. The guide requires live repo source of truth, exact target files, one Git-generated patch per target, `git apply --check`, cumulative validation, marker checks, and an artifact-only final builder state.

---

## 2. Current-State Findings

|priority|issue|current state|consequence|source evidence|must patch?|
|---|---|---|---|---|---|
|P0|CLI flag placement mismatch|Contract says `--allow-write`, `--json`, `--dry-run`, and `--strict` may be placed before or after subcommands, but live parsers define these mainly as root/global flags. `generate-source-payload-manifest` does not define post-subcommand `--allow-write`/`--json`; retrieval parser also defines root-global flags.|Handovers fail despite correct lifecycle logic; PowerShell/Git Bash examples diverge from parser behavior.|Contract promises flexible placement. Live lifecycle parser has root globals and only selected subcommands duplicate `--json`/`--strict`. Retrieval parser follows the same root-global pattern.|yes|
|P0|Pointer-only Phase 0 handling|`source-intake` supports `pointer_only`, but Phase 0 scans files from `sources/` and `raw/` only; manifest pointer targets are not part of the visible Phase 0 input set.|A KB with repo-internal pointer-only sources can produce sparse or empty deterministic navigation without a clear warning.|Source custody allows `pointer_only` for durable repo/local sources. Phase 0 implementation calls `iter_source_files(kb_root)` and writes the eight artifacts from that file list. Saved audit flags pointer-only handling as suspect.|yes|
|P1|Quality / coverage command|Lint has frontmatter, path, wikilink, source-payload, and Phase 2 heading checks, but no deterministic source-to-page coverage, page-to-source map, shell-page density, claim-pointer density, or repair candidate list.|Apex can pass structural lint while still producing low-value wiki pages.|Current lint adds `lint_page_value_contract` report-only findings for missing headings. Saved audit says quality/coverage is only partial and lacks source-to-page coverage, shell density, claim density, and query quality.|yes|
|P1|Split wiki index freshness from retrieval freshness|`status` reports generic `index_status`, `source_payload_manifest_status`, and `search_index_present`, not separate `wiki_index_status` and `retrieval_index_status`. Retrieval has its own `stale_report`, but lifecycle status does not expose both cleanly.|A run can confuse stale `wiki/index.md` with stale `derived/search`; query-ready state remains ambiguous.|`cmd_status` currently returns `index_status` and `search_index_present`. Retrieval has independent stale metadata. Postflight concept says these are distinct surfaces.|yes|
|P1|Query-eval pack|Query packets exist, but no deterministic eval-pack convention validates expected routes, minimal pages, or raw-source-needed status.|Query-ready can mean “indexed” rather than “tested against representative questions.”|Retrieval query returns backend, stale report, results, and policy. Query packet template has answer/evidence/gaps/reuse shape but no eval items. Backlog asks for 5–10 canned query simulations.|yes|
|P1|PowerShell-safe JSON output path or examples|Examples rely on stdout JSON; PowerShell redirection/encoding was identified as a failure surface.|JSON validation can fail on Windows even when command behavior is correct.|CLI concept records PowerShell UTF-16 JSON breakage and wants UTF-8 output or documented `Set-Content -Encoding utf8`. PowerShell example file currently says flexible flag placement is allowed and uses post-subcommand flags in some places.|yes|
|P1|Lifecycle state-lock / target-drift gates|Some deterministic route-lint functions exist, but the runbook/template layer does not yet require a universal state-lock header and target-drift relevance gate.|Future handovers can rewind phases, rank domain-only files as lifecycle authority, or blur executor boundaries.|Executor concept requires state lock fields and one executor/artifact before next work. Target-drift concept requires mission-as-filter and direct lifecycle relevance for read-first files.|yes|
|P2|Graph / process-flow extraction|Markdown structure parser extracts headings, links, wikilinks, code blocks, and frontmatter, but no Apex-specific graph/process-flow artifact exists.|Phase 0 misses high-value edges encoded as package manifests, YAML path fields, ownership blocks, and process sequences.|Current parser extracts Markdown links and wikilinks. Saved audit says graph extraction is V1.5 and must parse YAML/path/process edges, not only Markdown links.|yes, additive|
|P2|Existing-page repair flow|Phase 2 value contract exists for future pages, but old compiled pages are not automatically repaired; quality/lint does not yet generate a repair plan.|Thin pages can remain indefinitely even though new templates are stronger.|Live skill requires Adaptive Ranked Source Set, Macro/Meso/Micro, Key Claims, Routes Here, and Uncertainty triggers. KB contract defines the value contract. Audit says existing pages were not automatically repaired.|yes, no mass rewrite|
|Closed / validate|Source payload manifest|Implemented in live script and docs.|Only smoke-test; do not redesign.|Script defines `SOURCE_PAYLOAD_MANIFEST_PATH` and deterministic manifest builder. KB contract forbids external BagIt and defines grouping/hashes.|validate only|

---

## 3. Dependency Order

```yaml
patch_sequence:
  - step: 1
    name: "CLI flag and JSON-output compatibility"
    reason: >
      Later smoke tests depend on command examples working. Fix parser/docs mismatch before
      validating phase0, quality, graph, retrieval, and PowerShell examples.
    depends_on: []
    unlocks:
      - "stable validation commands"
      - "PowerShell-safe command examples"
      - "later smoke tests can use either global or post-subcommand flag placement"

  - step: 2
    name: "Pointer-only Phase 0 source handling"
    reason: >
      Quality/coverage and graph extraction depend on Phase 0 seeing the accessible
      source set or warning explicitly when it cannot.
    depends_on:
      - "CLI flag and JSON-output compatibility"
    unlocks:
      - "accurate Phase 0 file counts"
      - "pointer_only scanned/warning metrics"
      - "coverage command can distinguish source custody from source scan coverage"

  - step: 3
    name: "Freshness status split"
    reason: >
      Status/lint must distinguish wiki index freshness, retrieval index freshness,
      and payload manifest freshness before postflight can claim query-ready state.
    depends_on:
      - "CLI flag and JSON-output compatibility"
    unlocks:
      - "quality command can include freshness state"
      - "query-eval can reject stale retrieval separately from stale wiki index"

  - step: 4
    name: "Quality / coverage command"
    reason: >
      Existing-page repair and query-ready status require deterministic source-to-page
      and page-value metrics, not only structural lint.
    depends_on:
      - "Pointer-only Phase 0 source handling"
      - "Freshness status split"
    unlocks:
      - "phase2_repair_candidates"
      - "source_to_page_map"
      - "page_to_source_map"
      - "shell_page_candidates"
      - "query-ready quality gate"

  - step: 5
    name: "Existing-page repair flow"
    reason: >
      Repair must be candidate-driven. Do not rewrite pages blindly; use quality output
      to list pages that need Phase 2 rerun, merge, deprecation, or review.
    depends_on:
      - "Quality / coverage command"
    unlocks:
      - "targeted later LLM Phase 2 repair"
      - "repair-plan template"
      - "low-value page backlog"

  - step: 6
    name: "Query-eval pack"
    reason: >
      Query-eval should run after retrieval surfaces and freshness states are stable,
      and after quality metrics can identify insufficient evidence pages.
    depends_on:
      - "Freshness status split"
      - "Quality / coverage command"
    unlocks:
      - "query_eval_report"
      - "expected route validation"
      - "query_ready output tier has test evidence"

  - step: 7
    name: "Lifecycle state-lock and target-drift gates"
    reason: >
      These are process/documentation gates. They should be added after the script
      targets are clear, so they describe the actual closure workflow rather than
      another broad process layer.
    depends_on:
      - "Freshness status split"
    unlocks:
      - "handover state locks"
      - "domain-only exclusion rules"
      - "read-first relevance checks"

  - step: 8
    name: "Graph / process-flow extraction"
    reason: >
      Additive V1.5 deterministic artifact. It should not block core lifecycle closure,
      but must be included as a non-semantic command/report.
    depends_on:
      - "Pointer-only Phase 0 source handling"
    unlocks:
      - "process-flow-graph.json"
      - "process-flow-graph.md"
      - "path/YAML/manifest/process edges for LLM navigation"

  - step: 9
    name: "Documentation, templates, examples, acceptance tests"
    reason: >
      Update contracts and examples after script behavior is settled. This prevents
      repeating the current docs/parser mismatch.
    depends_on:
      - "CLI flag and JSON-output compatibility"
      - "Pointer-only Phase 0 source handling"
      - "Freshness status split"
      - "Quality / coverage command"
      - "Existing-page repair flow"
      - "Query-eval pack"
      - "Lifecycle state-lock and target-drift gates"
      - "Graph / process-flow extraction"
    unlocks:
      - "patch-pack acceptance suite"
      - "PowerShell/Git Bash command parity"
      - "operator-runbook closure"
```

---

## 4. Implementation Plan by Patch

```yaml
patches:
  - patch: "001-apex-kb-cli-flags-output-json.patch"
    target_file: "apex-meta/scripts/apex_kb.py"
    type: "script behavior"
    changes:
      - "Add a small argv compatibility shim before argparse parsing."
      - "Accept boolean global flags before or after subcommand: --json, --allow-write, --dry-run, --strict."
      - "Add --source alias to source-intake as alias of --source-path."
      - "Add --source alias to hash as alias of --path."
      - "Add --output-json <path> support for JSON-heavy read/report commands."
      - "Add read-only command-contract subcommand if low-risk."
    required_markers:
      - "normalize_global_flag_placement"
      - "--output-json"
      - "command-contract"
      - "source-intake accepts --source"
    forbidden_markers:
      - "click"
      - "typer"
      - "docopt"
      - "external dependency"
      - "hardcoded claude-skill-design"
    acceptance:
      - "python apex-meta/scripts/apex_kb.py --kb-root KB --json status"
      - "python apex-meta/scripts/apex_kb.py --kb-root KB status --json"
      - "python apex-meta/scripts/apex_kb.py --kb-root KB --allow-write index"
      - "python apex-meta/scripts/apex_kb.py --kb-root KB index --allow-write"

  - patch: "002-apex-kb-retrieval-cli-flags-output-json.patch"
    target_file: "apex-meta/scripts/apex_kb_retrieval.py"
    type: "script behavior"
    changes:
      - "Apply the same minimal flag-placement shim."
      - "Add --output-json <path> for JSON command results."
      - "Keep retrieval writes restricted to derived/search and outputs/queries unless output-json is under kb_root/log or outputs/queries."
    required_markers:
      - "normalize_global_flag_placement"
      - "--output-json"
    forbidden_markers:
      - "network"
      - "requests"
      - "vector"
      - "hosted"
    acceptance:
      - "python apex-meta/scripts/apex_kb_retrieval.py --kb-root KB --allow-write build-index"
      - "python apex-meta/scripts/apex_kb_retrieval.py --kb-root KB build-index --allow-write"
      - "python apex-meta/scripts/apex_kb_retrieval.py --kb-root KB stale --json"

  - patch: "003-apex-kb-pointer-only-phase0.patch"
    target_file: "apex-meta/scripts/apex_kb.py"
    type: "script behavior"
    changes:
      - "Add manifest pointer resolver for source_storage_mode == pointer_only."
      - "Resolve only repo-internal or kb-root-contained text files where safe."
      - "Never scan external web URLs or non-existing local paths."
      - "Add pointer_only_source_status to phase0 command output."
      - "Add pointer_only status sections to corpus-profile.md and phase0-navigation-report.md."
    required_markers:
      - "pointer_only_source_status"
      - "pointer_only_scanned_count"
      - "pointer_only_warning_count"
      - "pointer_only_unresolved"
    forbidden_markers:
      - "requests.get"
      - "urllib.request"
      - "network"
      - "semantic_summary"
    acceptance:
      - "pointer_only repo-internal text source is scanned"
      - "inaccessible pointer_only source is warned, not silent"

  - patch: "004-apex-kb-status-freshness-split.patch"
    target_file: "apex-meta/scripts/apex_kb.py"
    type: "script behavior"
    changes:
      - "Rename or supplement index_status with wiki_index_status."
      - "Add retrieval_index_status by reading derived/search/index-meta.json against wiki page state."
      - "Keep source_payload_manifest_status."
      - "Update lint issue types to distinguish wiki_index and retrieval_index."
    required_markers:
      - "wiki_index_status"
      - "retrieval_index_status"
      - "source_payload_manifest_status"
    forbidden_markers:
      - "index_status only"
    acceptance:
      - "status JSON shows all three statuses separately"

  - patch: "005-apex-kb-quality-coverage.patch"
    target_file: "apex-meta/scripts/apex_kb.py"
    type: "script behavior"
    changes:
      - "Add quality command, alias coverage."
      - "Compute source_count and wiki_page_count."
      - "Compute pages_without_source_refs."
      - "Compute pages_missing_phase2_value_sections using existing PHASE2_VALUE_HEADINGS."
      - "Compute low_density_pages and shell_page_candidates with simple deterministic thresholds."
      - "Compute missing_claim_pointer_pages by scanning Key Claims sections for source_pointer."
      - "Compute pages_with_review_flags."
      - "Build source_to_page_map and page_to_source_map from frontmatter source_refs."
      - "Emit phase2_repair_candidates."
      - "Support --strict as fail threshold; default report-only warn."
    required_markers:
      - "cmd_quality"
      - "source_to_page_map"
      - "page_to_source_map"
      - "phase2_repair_candidates"
      - "shell_page_candidates"
      - "deterministic_only"
    forbidden_markers:
      - "LLM"
      - "page_value_score"
      - "semantic grading"
    acceptance:
      - "quality command runs without writes"
      - "coverage alias returns same payload"
      - "low-value test page appears in phase2_repair_candidates"

  - patch: "006-apex-kb-query-eval.patch"
    target_file: "apex-meta/scripts/apex_kb.py"
    type: "script behavior / generated evaluation fixture"
    changes:
      - "Add query-eval command."
      - "Validate or generate outputs/queries/evals/query-eval-pack.json."
      - "Each eval item includes query, expected_routes, expected_minimal_pages, raw_source_needed, rationale, status."
      - "Do not perform LLM answer grading."
    required_markers:
      - "cmd_query_eval"
      - "query-eval-pack.json"
      - "expected_minimal_pages"
      - "raw_source_needed"
    forbidden_markers:
      - "OpenAI"
      - "anthropic"
      - "network"
      - "LLM grading"
    acceptance:
      - "query-eval --init --allow-write creates pack"
      - "query-eval validates schema"
      - "query-eval report is deterministic"

  - patch: "007-apex-kb-graph-process-flow.patch"
    target_file: "apex-meta/scripts/apex_kb.py"
    type: "script behavior"
    changes:
      - "Add graph or process-graph command."
      - "Generate manifests/phase0/process-flow-graph.json and .md."
      - "Extract Markdown links, wikilinks, explicit repo path strings, YAML/path fields, package manifest references, script_path, canonical_source, supporting_files, owns, does_not_own, hands_off_to, and safe process arrow/stage sequences."
      - "Keep deterministic; no visual graph; no semantic ingest."
    required_markers:
      - "cmd_graph"
      - "process-flow-graph.json"
      - "edge_type"
      - "yaml_path_reference"
      - "process_sequence"
    forbidden_markers:
      - "obsidian_required"
      - "network"
      - "semantic_graph"
      - "node"
      - "remark"
    acceptance:
      - "graph command writes two phase0 graph artifacts"
      - "graph output includes at least markdown_link, wikilink, repo_path_reference edge categories on fixture"

  - patch: "008-script-command-contract.patch"
    target_file: ".claude/skills/apex-kb/references/script-command-contract.md"
    type: "docs / command contract"
    changes:
      - "Update CLI flag placement to match implemented shim."
      - "Document --output-json."
      - "Document quality/coverage, query-eval, graph/process-graph."
      - "Document pointer_only Phase 0 behavior."
      - "Keep source-payload manifest closed/validated, not redesigned."
    required_markers:
      - "quality"
      - "coverage"
      - "query-eval"
      - "graph"
      - "--output-json"
      - "pointer_only"
    forbidden_markers:
      - "external BagIt"
      - "Node/remark required"
      - "vector database"

  - patch: "009-ingest-query-lint-audit-rules.patch"
    target_file: ".claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md"
    type: "docs / process contract"
    changes:
      - "Add quality/coverage as distinct from lint."
      - "Add query-eval rules."
      - "Add repair candidate flow."
      - "Add freshness split rules."
      - "Add pointer_only warning requirement."
    required_markers:
      - "quality / coverage"
      - "phase2_repair_candidates"
      - "wiki_index_status"
      - "retrieval_index_status"
      - "query-eval"
    forbidden_markers:
      - "mass rewrite"
      - "automatic delete"

  - patch: "010-lifecycle-state-machine-gates.patch"
    target_file: ".claude/skills/apex-kb/references/lifecycle-state-machine.md"
    type: "docs / state machine"
    changes:
      - "Add explicit state-lock header fields."
      - "Add target-drift gate before read-first source ranking."
      - "Add S7b_quality_coverage_ready and S7c_query_eval_ready."
      - "Add optional graph artifact state under Phase 0/V1.5."
    required_markers:
      - "lifecycle_position"
      - "target_drift_check"
      - "S7b_quality_coverage_ready"
      - "S7c_query_eval_ready"
      - "process-flow-graph"
    forbidden_markers:
      - "Plan mutation"
      - "Session mutation"

  - patch: "011-acceptance-tests.patch"
    target_file: ".claude/skills/apex-kb/references/acceptance-tests.md"
    type: "tests / docs"
    changes:
      - "Add py_compile for both scripts."
      - "Add pre/post flag placement smoke."
      - "Add pointer_only Phase 0 fixture."
      - "Add quality command smoke."
      - "Add graph command smoke."
      - "Add query-eval smoke."
      - "Add PowerShell UTF-8 JSON output test."
    required_markers:
      - "pointer_only Phase 0"
      - "quality"
      - "query-eval"
      - "process-flow-graph"
      - "--output-json"
    forbidden_markers:
      - "requires network"

  - patch: "012-lifecycle-runbook.patch"
    target_file: ".claude/skills/apex-kb/examples/lifecycle-runbook.md"
    type: "runbook"
    changes:
      - "Add state-lock header template."
      - "Add target-drift gate."
      - "Add postflight quality/coverage and query-eval steps."
      - "Add repair flow policy."
    required_markers:
      - "state_lock"
      - "target_drift_check"
      - "quality / coverage"
      - "query-eval"
      - "repair candidates"
    forbidden_markers:
      - "blind rewrite"

  - patch: "013-powershell-commands.patch"
    target_file: ".claude/skills/apex-kb/examples/powershell-commands.md"
    type: "examples"
    changes:
      - "Correct examples to actual supported flexible placement after script patch."
      - "Add --output-json examples."
      - "Prefer Git Bash for redirect-heavy validation, but keep PowerShell-safe commands."
    required_markers:
      - "Set-Content -Encoding utf8"
      - "--output-json"
      - "Git Bash"
    forbidden_markers:
      - "Out-File default encoding"

  - patch: "014-wiki-page-template-repair-flow.patch"
    target_file: ".claude/skills/apex-kb/templates/wiki-page-templates.md"
    type: "template"
    changes:
      - "Add existing-page repair plan template."
      - "Define keep | repair | deprecate | merge | delete_candidate recommendations."
      - "Reinforce no mass rewrite."
    required_markers:
      - "Phase 2 Repair Candidate"
      - "recommended_action"
      - "keep | repair | deprecate | merge | delete_candidate"
    forbidden_markers:
      - "automatically delete"
      - "mass rewrite"

  - patch: "015-query-output-template-evals.patch"
    target_file: ".claude/skills/apex-kb/templates/query-output-template.md"
    type: "template"
    changes:
      - "Add optional query-eval metadata section."
      - "Add expected_routes / expected_minimal_pages / raw_source_needed fields."
    required_markers:
      - "query_eval"
      - "expected_routes"
      - "expected_minimal_pages"
      - "raw_source_needed"
    forbidden_markers:
      - "LLM score"

  - patch: "016-package-manifest.patch"
    target_file: ".claude/skills/apex-kb/package-manifest.md"
    type: "package inventory"
    changes:
      - "Add query-eval / quality / graph artifacts to relevant runtime path descriptions if needed."
      - "Only patch if target-file analysis shows inventory drift."
    required_markers:
      - "process-flow-graph"
      - "query-eval"
      - "quality"
    forbidden_markers:
      - ".claude/skills/apex-kb2"

  - patch: "017-skill-md.patch"
    target_file: ".claude/skills/apex-kb/SKILL.md"
    type: "skill entrypoint"
    changes:
      - "Add quality/coverage, query-eval, graph/process-flow, and repair-candidate terms to procedure only if not already sufficiently covered."
      - "Keep boundary against Plan/Sync/Session/PreCap/FlowRecap/APSU mutation."
    required_markers:
      - "quality / coverage"
      - "query-eval"
      - "process-flow graph"
      - "repair candidates"
    forbidden_markers:
      - "mutate Apex Plan"
      - "apex-kb2"
```

---

## 5. Target File Plan

### `apex-meta/scripts/apex_kb.py`

Current role: deterministic lifecycle helper; owns scaffold, source hashing/custody, Phase 0 artifacts, index/lint/audit/status, source-payload manifest, and deterministic validation.

Edits:

```yaml
apex_kb_py_plan:
  add_helpers:
    - normalize_global_flag_placement(argv)
    - maybe_write_output_json(args, result, kb_root)
    - pointer_only_manifest_sources(kb_root)
    - resolve_pointer_only_text_files(kb_root, manifest)
    - retrieval_index_status(kb_root)
    - quality_report(kb_root)
    - query_eval_pack_path(kb_root)
    - process_graph_extract(kb_root)

  modify_existing:
    - main(argv): run compatibility shim before parse_args
    - emit(args, obj): support --output-json
    - cmd_phase0: include pointer_only source resolution and status
    - corpus_profile: include pointer_only source status
    - phase0_report: include pointer_only source status
    - cmd_status: split wiki_index_status, retrieval_index_status, source_payload_manifest_status
    - cmd_lint: use distinct wiki/retrieval/source-payload issue types

  add_commands:
    - quality
    - coverage alias
    - query-eval
    - graph / process-graph alias
    - command-contract if low-risk
```

Tests:

```bash
python -m py_compile apex-meta/scripts/apex_kb.py
python apex-meta/scripts/apex_kb.py --kb-root "$KB" status --json
python apex-meta/scripts/apex_kb.py --kb-root "$KB" --json status
python apex-meta/scripts/apex_kb.py --kb-root "$KB" quality --json
python apex-meta/scripts/apex_kb.py --kb-root "$KB" graph --json --allow-write
python apex-meta/scripts/apex_kb.py --kb-root "$KB" query-eval --json
```

### `apex-meta/scripts/apex_kb_retrieval.py`

Current role: derived local retrieval; no network, no shell-outs, standard library only; writes restricted to `derived/search` and `outputs/queries`, with FTS5 runtime probe and JSON fallback.

Edits:

```yaml
apex_kb_retrieval_py_plan:
  add_helpers:
    - normalize_global_flag_placement(argv)
    - maybe_write_output_json(args, result, kb_root)

  modify_existing:
    - main(argv): run compatibility shim
    - emit(args, obj): support --output-json
    - build_parser: document flexible flag placement and output path

  preserve:
    - FTS5 runtime probe
    - JSON fallback
    - derived-only writes
    - clear-index confirmation
```

Tests:

```bash
python -m py_compile apex-meta/scripts/apex_kb_retrieval.py
python apex-meta/scripts/apex_kb_retrieval.py --kb-root "$KB" --allow-write build-index
python apex-meta/scripts/apex_kb_retrieval.py --kb-root "$KB" build-index --allow-write
python apex-meta/scripts/apex_kb_retrieval.py --kb-root "$KB" stale --json
python apex-meta/scripts/apex_kb_retrieval.py --kb-root "$KB" query --query "retrieval" --limit 3 --json
```

### `.claude/skills/apex-kb/references/script-command-contract.md`

Current role: command surface contract. It currently promises flexible flag placement.

Edits:

```yaml
script_command_contract_plan:
  add_or_update:
    - exact accepted flag placement rules
    - --output-json path policy
    - quality / coverage command contract
    - query-eval command contract
    - graph / process-graph command contract
    - pointer_only Phase 0 status fields
    - status freshness fields
```

### `.claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md`

Current role: ingest/query/lint/audit rules; currently lists Phase 0 artifacts and lint surfaces.

Edits:

```yaml
ingest_query_lint_audit_rules_plan:
  add:
    - "quality/coverage is separate from lint"
    - "query-eval pack validates route/readiness, not answer truth"
    - "phase2_repair_candidates generated by quality command"
    - "pointer_only Phase 0 must scan or warn"
    - "wiki_index_status and retrieval_index_status are separate"
```

### `.claude/skills/apex-kb/references/lifecycle-state-machine.md`

Current role: lifecycle states; already has S2b payload manifest and operator v3 macro states.

Edits:

```yaml
lifecycle_state_machine_plan:
  add:
    - S3b_process_graph_ready optional additive state
    - S7b_quality_coverage_ready
    - S7c_query_eval_ready
    - lifecycle state-lock header
    - target drift gate before source ranking
```

### `.claude/skills/apex-kb/references/acceptance-tests.md`

Current role: smoke/acceptance commands; already covers scaffold, source intake, payload manifest, Phase 0, index, retrieval, and maintenance.

Edits:

```yaml
acceptance_tests_plan:
  add:
    - py_compile both scripts
    - CLI pre/post flag placement tests
    - --output-json UTF-8 test
    - pointer_only Phase0 smoke fixture
    - quality/coverage command smoke
    - query-eval smoke
    - graph/process-flow smoke
    - regression greps for forbidden dependencies
```

### `.claude/skills/apex-kb/templates/wiki-page-templates.md`

Current role: Phase 2 page template; already requires adaptive source set, Macro/Meso/Micro, Key Claims, Routes Here, and Uncertainty triggers.

Edits:

```yaml
wiki_page_templates_plan:
  add:
    - "Phase 2 Repair Candidate template"
    - candidate_page
    - missing_value_contract_sections
    - likely_source_set
    - raw_source_reopen_trigger
    - recommended_action: keep | repair | deprecate | merge | delete_candidate
  preserve:
    - no fixed source count
    - no page_value_score
    - warning-first approach
```

### `.claude/skills/apex-kb/templates/query-output-template.md`

Current role: query output template; has evidence pages, citations, gaps, and reuse notes.

Edits:

```yaml
query_output_template_plan:
  add:
    - optional query_eval metadata
    - expected_routes
    - expected_minimal_pages
    - raw_source_needed
    - eval_status
```

### `.claude/skills/apex-kb/examples/lifecycle-runbook.md`

Current role: operator runbook; already lists Prepare, Ingest/Compile, Postflight, Query/Maintain and mentions quality/coverage in postflight.

Edits:

```yaml
lifecycle_runbook_plan:
  add:
    - state_lock header template
    - target_drift_check
    - graph/process-flow optional Phase 0+ artifact
    - quality/coverage and query-eval postflight order
    - repair candidate review flow
```

### `.claude/skills/apex-kb/examples/powershell-commands.md`

Current role: PowerShell command examples; currently says flexible flag placement is supported and uses post-subcommand flags in places.

Edits:

```yaml
powershell_commands_plan:
  add:
    - --output-json examples
    - Set-Content -Encoding utf8 fallback where redirection is used
    - Git Bash preferred note for redirect-heavy validation
  update:
    - examples to match implemented parser behavior after patch
```

### `.claude/skills/apex-kb/package-manifest.md`

Current role: package inventory and canonical/derived path contract.

Edits:

```yaml
package_manifest_plan:
  patch_only_if_needed: true
  possible_additions:
    - manifests/phase0/process-flow-graph.json
    - manifests/phase0/process-flow-graph.md
    - outputs/queries/evals/
    - quality/coverage report path
```

### `.claude/skills/apex-kb/SKILL.md`

Current role: skill entrypoint and operating procedure; already lists lifecycle, output tiers, payload manifest, Phase 2 value contract, and retrieval.

Edits:

```yaml
skill_md_plan:
  patch_only_if_needed: true
  possible_additions:
    - quality / coverage command named explicitly in Procedure
    - query-eval pack named explicitly in Procedure
    - process-flow graph artifact named as optional Phase 0/V1.5 artifact
    - repair candidates in D_query_or_maintain
  must_preserve:
    - boundary against Plan/Sync/Session/PreCap/FlowRecap/APSU mutation
```

---

## 6. Acceptance Checks

```bash
# 0. Baseline
git checkout main
git pull --ff-only origin main
git status --short

# 1. Compile
python -m py_compile apex-meta/scripts/apex_kb.py
python -m py_compile apex-meta/scripts/apex_kb_retrieval.py

# 2. Help surfaces
python apex-meta/scripts/apex_kb.py --help > /tmp/apex-kb-help.txt
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/apex-kb-v3-closure-smoke quality --help > /tmp/apex-kb-quality-help.txt
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/apex-kb-v3-closure-smoke query-eval --help > /tmp/apex-kb-query-eval-help.txt
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/apex-kb-v3-closure-smoke graph --help > /tmp/apex-kb-graph-help.txt
python apex-meta/scripts/apex_kb_retrieval.py --help > /tmp/apex-kb-retrieval-help.txt

grep -q "quality" /tmp/apex-kb-help.txt
grep -q "coverage" /tmp/apex-kb-help.txt
grep -q "query-eval" /tmp/apex-kb-help.txt
grep -q "graph" /tmp/apex-kb-help.txt
grep -q -- "--output-json" /tmp/apex-kb-help.txt
grep -q -- "--output-json" /tmp/apex-kb-retrieval-help.txt

# 3. Smoke KB
KB="apex-meta/kb/apex-kb-v3-closure-smoke"
rm -rf "$KB"
python apex-meta/scripts/apex_kb.py --kb-root "$KB" scaffold --allow-write --json
mkdir -p tmp
printf '# Smoke Source\n\nApex KB retrieval, Phase 0, source manifest, and query eval.\n' > tmp/smoke-source.md
python apex-meta/scripts/apex_kb.py --kb-root "$KB" source-intake --source tmp/smoke-source.md --source-type note --storage-mode copy_into_kb --source-id smoke-source --allow-write --json
python apex-meta/scripts/apex_kb.py --kb-root "$KB" generate-source-payload-manifest --allow-write --json
python apex-meta/scripts/apex_kb.py --kb-root "$KB" phase0 --allow-write --json

test -f "$KB/manifests/source-payload-manifest.json"
test -f "$KB/manifests/phase0/phase0-navigation-report.md"

# 4. CLI flag placement
python apex-meta/scripts/apex_kb.py --kb-root "$KB" --json status
python apex-meta/scripts/apex_kb.py --kb-root "$KB" status --json
python apex-meta/scripts/apex_kb.py --kb-root "$KB" --allow-write index
python apex-meta/scripts/apex_kb.py --kb-root "$KB" index --allow-write
python apex-meta/scripts/apex_kb_retrieval.py --kb-root "$KB" --allow-write build-index
python apex-meta/scripts/apex_kb_retrieval.py --kb-root "$KB" build-index --allow-write

# 5. Pointer-only Phase 0 fixture
POINTER_KB="apex-meta/kb/apex-kb-pointer-smoke"
rm -rf "$POINTER_KB"
python apex-meta/scripts/apex_kb.py --kb-root "$POINTER_KB" scaffold --allow-write --json
mkdir -p "$POINTER_KB/raw/notes"
printf '# Repo Internal Pointer Source\n\npointer_only test content for phase0.\n' > "$POINTER_KB/raw/notes/pointer-target.md"
python apex-meta/scripts/apex_kb.py --kb-root "$POINTER_KB" source-intake --pointer "$POINTER_KB/raw/notes/pointer-target.md" --storage-mode pointer_only --source-id pointer-target --source-type note --allow-write --json
python apex-meta/scripts/apex_kb.py --kb-root "$POINTER_KB" phase0 --allow-write --json > /tmp/pointer-phase0.json
grep -q "pointer_only" /tmp/pointer-phase0.json
grep -q "pointer_only" "$POINTER_KB/manifests/phase0/corpus-profile.md"
grep -q "pointer_only" "$POINTER_KB/manifests/phase0/phase0-navigation-report.md"

# 6. Quality / coverage
python apex-meta/scripts/apex_kb.py --kb-root "$KB" quality --json > /tmp/quality.json
python apex-meta/scripts/apex_kb.py --kb-root "$KB" coverage --json > /tmp/coverage.json
grep -q "source_to_page_map" /tmp/quality.json
grep -q "page_to_source_map" /tmp/quality.json
grep -q "phase2_repair_candidates" /tmp/quality.json

# 7. Query eval
python apex-meta/scripts/apex_kb.py --kb-root "$KB" query-eval --init --allow-write --json
test -f "$KB/outputs/queries/evals/query-eval-pack.json"
python apex-meta/scripts/apex_kb.py --kb-root "$KB" query-eval --json > /tmp/query-eval.json
grep -q "expected_minimal_pages" /tmp/query-eval.json

# 8. Graph / process-flow
python apex-meta/scripts/apex_kb.py --kb-root "$KB" graph --allow-write --json
test -f "$KB/manifests/phase0/process-flow-graph.json"
test -f "$KB/manifests/phase0/process-flow-graph.md"
grep -q "edge_type" "$KB/manifests/phase0/process-flow-graph.json"

# 9. Retrieval
python apex-meta/scripts/apex_kb_retrieval.py --kb-root "$KB" build-index --allow-write --json
python apex-meta/scripts/apex_kb_retrieval.py --kb-root "$KB" stale --json
python apex-meta/scripts/apex_kb_retrieval.py --kb-root "$KB" query --query "retrieval" --limit 3 --json

# 10. PowerShell-safe JSON output path equivalent
python apex-meta/scripts/apex_kb.py --kb-root "$KB" status --json --output-json "$KB/log/status-output.json"
python - <<'PY'
import json
json.load(open("apex-meta/kb/apex-kb-v3-closure-smoke/log/status-output.json", encoding="utf-8"))
PY

# 11. Regression greps
! grep -R "external BagIt" .claude/skills/apex-kb apex-meta/scripts/apex_kb.py
! grep -R "Node/remark required" .claude/skills/apex-kb apex-meta/scripts/apex_kb.py
! grep -R "vector database" .claude/skills/apex-kb apex-meta/scripts/apex_kb.py
! grep -R ".claude/skills/apex-kb2" .claude/skills/apex-kb apex-meta/scripts/apex_kb.py apex-meta/scripts/apex_kb_retrieval.py
```

---

## 7. Patch-Pack Constraints for Later Execution

The later builder should not directly leave target files edited. The uploaded process guide says the builder must generate patches with `git diff`, revert targets, validate each patch with `git apply --check`, validate the cumulative sequence, check markers/scope, and restore target files so only patch artifacts remain.

```yaml
patch_pack_constraints:
  builder_role: "Agent Mode patch-pack builder"
  applier_role: "Codex or terminal executor"
  source_of_truth: "live main branch"
  method:
    - "one patch per target file"
    - "git diff --no-ext-diff only"
    - "no hand-written hunks"
    - "git apply --check per patch"
    - "cumulative disposable apply validation"
    - "changed-file scope equals target_files"
    - "required/forbidden marker checks"
    - "final builder state has patch artifacts only"
  forbidden:
    - "direct runtime wiki page rewrite"
    - "apex-kb2"
    - "Plan/Sync/Session/PreCap/FlowRecap/APSU mutation"
    - "external BagIt dependency"
    - "Node/remark required dependency"
    - "vector database"
    - "network calls"
```

Recommended patch-pack file map:

```yaml
patch_pack:
  root: "apex-meta/patches/apex-kb-v3-p0-p2-closure/"
  metadata:
    - "000-patch-manifest.md"
    - "999-codex-apply-handoff.md"
    - "validation-report.md"
  patches:
    - "001-apex-kb-cli-flags-output-json.patch"
    - "002-apex-kb-retrieval-cli-flags-output-json.patch"
    - "003-apex-kb-pointer-only-phase0.patch"
    - "004-apex-kb-status-freshness-split.patch"
    - "005-apex-kb-quality-coverage.patch"
    - "006-apex-kb-query-eval.patch"
    - "007-apex-kb-graph-process-flow.patch"
    - "008-script-command-contract.patch"
    - "009-ingest-query-lint-audit-rules.patch"
    - "010-lifecycle-state-machine-gates.patch"
    - "011-acceptance-tests.patch"
    - "012-lifecycle-runbook.patch"
    - "013-powershell-commands.patch"
    - "014-wiki-page-template-repair-flow.patch"
    - "015-query-output-template-evals.patch"
    - "016-package-manifest.patch"
    - "017-skill-md.patch"
```

---

## 8. Preparation Needed Before Patch-Pack Build

```yaml
preparation_needed_before_agent_mode:
  verdict: none
  source_access:
    live_repo_target_files: "sufficient for planning"
    uploaded_patch_process_guide: "available through project resources"
  unresolved_design_choices:
    - item: "Graph/process-flow extraction depth"
      resolution_for_patch_pack: "implement deterministic V1.5-lite artifact; no semantic graph, no visual graph, no Node/remark dependency"
    - item: "Existing-page repair"
      resolution_for_patch_pack: "quality/coverage lists repair candidates and template; no runtime page rewrite"
    - item: "PowerShell JSON"
      resolution_for_patch_pack: "prefer --output-json path plus examples; do not rely on shell redirection"
  execute_directly: true
  caution: >
    The later builder must have a real Git workspace or scratch Git repo. Connector-only chat
    can plan but cannot certify git apply readiness.
```

I did not find the repo path `apex-meta/SmallSkills/Patching/AgentMode-GitNative-PatchPack-Process.okf.md` via GitHub fetch, but the uploaded project-resource copy of that guide was readable and sufficient for the patch-pack constraints. The protocol itself says connector excerpts alone cannot certify a patch pack; a real Git workspace or scratch Git repo is required for patch creation and validation.

---

## 9. Final Recommendation

Proceed to a single Agent Mode patch-pack build for all P0–P2 items. Do **not** cut P2, but keep P2 bounded: graph/process-flow becomes a deterministic optional artifact under `manifests/phase0/`, and existing-page repair becomes a quality/coverage-driven candidate workflow, not a mass rewrite. The operator should next paste a patch-pack builder prompt generated from this plan into Agent Mode, with the patch-pack root `apex-meta/patches/apex-kb-v3-p0-p2-closure/`, and require Git-generated patches plus `git apply --check` validation before Codex applies anything.