# Target File Map

## 1. Batch map

```yaml
batch:
  id: 1
  file_count: 12
  max_target_plan_files: 12
  patch_pack_root_for_later_builder: apex-meta/patches/apex-kb-v3-repair/
````

## 2. Target plans

|target plan|target repo path|feature|action|
|---|---|---|---|
|`targets/001-apex-kb-py-pointer-only-phase0.md`|`apex-meta/scripts/apex_kb.py`|pointer_only_phase0|replace stub|
|`targets/002-apex-kb-py-quality-coverage.md`|`apex-meta/scripts/apex_kb.py`|quality_coverage|replace stub|
|`targets/003-apex-kb-py-query-eval.md`|`apex-meta/scripts/apex_kb.py`|query_eval|replace stub|
|`targets/004-apex-kb-py-graph-process-flow.md`|`apex-meta/scripts/apex_kb.py`|graph_process_flow|replace stub|
|`targets/005-apex-kb-py-status-freshness.md`|`apex-meta/scripts/apex_kb.py`|status_freshness_split|repair partial|
|`targets/006-apex-kb-py-cli-output-json.md`|`apex-meta/scripts/apex_kb.py`|cli_output_json|keep and regression-test|
|`targets/007-apex-kb-retrieval-cli-output-json.md`|`apex-meta/scripts/apex_kb_retrieval.py`|retrieval_cli_output_json|keep and regression-test|
|`targets/008-script-command-contract.md`|`.claude/skills/apex-kb/references/script-command-contract.md`|script_command_contract_alignment|docs repair|
|`targets/009-kb-contract-doc-alignment.md`|`.claude/skills/apex-kb/references/kb-contract.md`|kb_contract_alignment|docs alignment|
|`targets/010-acceptance-tests.md`|`.claude/skills/apex-kb/references/acceptance-tests.md`|acceptance_tests|add repair tests|
|`targets/011-phase2-value-contract-alignment.md`|`.claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md`|phase2_value_contract_alignment|rules alignment|
|`targets/012-package-manifest-plan-ledger.md`|`.claude/skills/apex-kb/package-manifest.md`|package_manifest_plan_ledger|manifest alignment|

## 3. Multi-feature single-file rule

`apex-meta/scripts/apex_kb.py` appears in multiple target plans because it owns multiple cohesive behavior repairs. The later patch-pack builder may either create one cumulative patch for `apex_kb.py` or one patch per cohesive script feature only if every patch applies cumulatively and all patch files are Git-generated. If the one-patch-per-target-file rule is interpreted strictly by the builder, merge targets 001–006 into a single script patch and keep the target-plan files as implementation subcontracts.

## 4. Forbidden targets

```yaml
forbidden_targets:
  - ".claude/skills/apex-kb2/**"
  - "apex-meta/kb/*/wiki/**"
  - "apex-meta/kb/*/ingest-analysis/**"
  - "apex-meta/patches/apex-kb-v3-p0-p2-closure/*.patch"
  - "Plan/Sync/Session/PreCap/FlowRecap/APSU/personal orchestration files"
```
