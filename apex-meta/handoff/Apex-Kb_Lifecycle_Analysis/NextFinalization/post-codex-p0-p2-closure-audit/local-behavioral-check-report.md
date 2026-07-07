# Local Behavioral Check Report — Apex KB v3 P0-P2 Closure

## Source

This report records the operator's local PowerShell execution after pulling commit `f9ed211092af5aa512778480470b5510cb350b6b` on `main`.

## Local repo state

```yaml
repo_path: C:\GitDev\apexai-os-meta
branch: main
pull_result: fast_forward_to_f9ed2110
compile:
  apex_kb_py: PASS
  apex_kb_retrieval_py: PASS
untracked_files_present: true
untracked_files_overlap_runtime_targets: false
```

Untracked files reported locally:

```text
?? apex-meta/SmallSkills/Patching/AgentMode/AgentModePatchGuide_v4.md.bak_20260707_132948
?? apex-meta/SmallSkills/Patching/AgentMode/ChatHistory_ConstantFailurePrompts.md
?? apex-meta/SmallSkills/Patching/AgentMode/Example_NotFullExecution_ThenFail.md
?? apex-meta/SmallSkills/Patching/AgentMode/FailureAgentModeNew_ThinkingProcess.md
?? apex-meta/SmallSkills/Patching/AgentMode/ThinkinProcessWorkingAgentMode.md
?? apex-meta/handoff/WeklyFlow/step1_prompt_blocker_cleanup_full_plan.okf.md
```

These do not overlap the Apex KB P0-P2 repair target files.

## Commands executed

```powershell
python -m py_compile apex-meta/scripts/apex_kb.py
python -m py_compile apex-meta/scripts/apex_kb_retrieval.py

python apex-meta/scripts/apex_kb.py --kb-root $KbRoot status --json --output-json "$OutDir/status-after-patch.json"
python apex-meta/scripts/apex_kb.py --kb-root $KbRoot quality --json --output-json "$OutDir/quality-after-patch.json"
python apex-meta/scripts/apex_kb.py --kb-root $KbRoot query-eval --init --json --output-json "$OutDir/query-eval-after-patch.json"
python apex-meta/scripts/apex_kb.py --kb-root $KbRoot graph --json --output-json "$OutDir/graph-after-patch.json"
python apex-meta/scripts/apex_kb_retrieval.py --kb-root $KbRoot stale --json --output-json "$OutDir/retrieval-stale-after-patch.json"
```

`$KbRoot` was:

```text
apex-meta/kb/claude-skill-design
```

`$OutDir` was:

```text
log/post-codex-p0-p2-audit
```

## Observed outputs

### status

```json
{
  "audit_item_count": 0,
  "command": "status",
  "exists": true,
  "kb_root": "C:\\GitDev\\apexai-os-meta\\apex-meta\\kb\\claude-skill-design",
  "phase0_artifacts_present": false,
  "retrieval_index_status": "missing",
  "search_index_present": false,
  "source_count": 0,
  "source_payload_manifest_status": "missing",
  "wiki_index_status": "missing",
  "wiki_page_count": 0
}
```

### quality

```json
{
  "command": "quality",
  "deterministic_only": true,
  "page_to_source_map": {},
  "phase2_repair_candidates": [],
  "shell_page_candidates": [],
  "source_to_page_map": {}
}
```

### query-eval --init

```json
{
  "command": "query-eval",
  "expected_minimal_pages": [],
  "query-eval-pack.json": "outputs/queries/evals/query-eval-pack.json",
  "raw_source_needed": []
}
```

### graph

```json
{
  "command": "graph",
  "edge_type": [],
  "process_sequence": [],
  "yaml_path_reference": []
}
```

### retrieval stale

```json
{
  "added": [],
  "command": "stale",
  "deleted": [],
  "kb_root": "C:\\GitDev\\apexai-os-meta\\apex-meta\\kb\\claude-skill-design",
  "message": "index metadata missing or unreadable",
  "modified": [],
  "status": "missing"
}
```

## Verdict

```yaml
verdict: PARTIAL_FAIL_CONFIRMED
compile_status: PASS
useful_changes_confirmed:
  - "CLI flag placement compatibility did not prevent these calls."
  - "--output-json accepted relative paths inside kb_root."
  - "status exposes wiki_index_status, retrieval_index_status, source_payload_manifest_status."
failed_or_stubbed_changes_confirmed:
  - "quality/coverage returns empty maps and empty candidate lists."
  - "query-eval --init does not write or populate a real eval pack."
  - "graph/process-graph returns empty edge lists."
  - "retrieval stale reports missing index metadata, which is acceptable status behavior but not a closure repair."
```

## Decision

Proceed with targeted repair, not rollback.

Preserve:

```yaml
preserve:
  - CLI global flag normalization
  - --output-json support
  - status freshness split
```

Repair:

```yaml
repair:
  - pointer_only Phase 0 should scan resolved repo-local/kb-local pointer files or report unresolved pointers.
  - quality/coverage should populate source_to_page_map and page_to_source_map from wiki frontmatter source_refs and manifest sources.
  - quality/coverage should detect shell_page_candidates and phase2_repair_candidates using Phase 2 value-contract headings, body density, and source-ref density.
  - query-eval --init should create a deterministic starter pack and validate existing pack shape.
  - graph/process-graph should extract actual markdown links, wikilinks, repo/path references, YAML/path edges, and process-sequence edges.
  - script-command-contract.md should be updated only to match real implemented behavior.
```

## Agent Mode repair instruction pointer

Use this report together with:

```text
apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NextFinalization/post-codex-p0-p2-closure-audit/connector-detective-audit-and-repair-plan.md
```

The next worker should create a Git-native repair patch pack under:

```text
apex-meta/patches/apex-kb-v3-p0-p2-closure-repair/
```

It must generate real patches from `git diff`, run `git apply --check`, and leave target files clean in the patch-pack builder final state.
