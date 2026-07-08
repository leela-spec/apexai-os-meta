#!/usr/bin/env python3
"""
Update Patchplan.md and AgentPrompt_v4.md with the corrected Apex patching process.

Purpose:
- ChatGPT/Pro Thinking owns the reasoning and writes this deterministic updater.
- Codex/local executor only runs this script, reviews the diff, fixes syntax/runtime issues if needed,
  and commits the generated changes.
- The two target documents are updated by inserting/replacing binding managed blocks.
- No architecture decisions are delegated to Codex.

Targets, relative to repo root:
- apex-meta/SmallSkills/Patching/AgnetModeNew/Patchplan.md
- apex-meta/SmallSkills/Patching/AgnetModeNew/AgentPrompt_v4.md

A fallback folder spelling `AgentModeNew` is supported only to tolerate the known typo in `AgnetModeNew`.
"""

from __future__ import annotations

import argparse
import difflib
import shutil
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable, Optional


BASE_CANDIDATES = [
    Path("apex-meta/SmallSkills/Patching/AgnetModeNew"),
    Path("apex-meta/SmallSkills/Patching/AgentModeNew"),
]

PATCHPLAN_FILENAME = "Patchplan.md"
AGENT_PROMPT_FILENAME = "AgentPrompt_v4.md"

PATCHPLAN_START = "<!-- APEX_PATCHPLAN_ITERATIVE_CONTRACT_START -->"
PATCHPLAN_END = "<!-- APEX_PATCHPLAN_ITERATIVE_CONTRACT_END -->"
AGENT_START = "<!-- APEX_AGENTPROMPT_V4_SCRIPTED_EXECUTION_START -->"
AGENT_END = "<!-- APEX_AGENTPROMPT_V4_SCRIPTED_EXECUTION_END -->"


PATCHPLAN_BLOCK = f"""{PATCHPLAN_START}
## Binding Correction — Iterative Patch-Plan Process

This section is binding and supersedes any conflicting instruction elsewhere in this file.

### Correct division of labor

ChatGPT/Pro Thinking owns the reasoning.
Codex/local executor only runs this script.

```yaml
division_of_labor:
  chatgpt_pro_thinking:
    owns:
      - reading the process/source files
      - understanding the repair plan
      - designing the update logic
      - writing deterministic Python updater scripts
      - deciding patch grouping and process doctrine

  codex:
    owns_only:
      - running the provided Python script
      - reporting stdout/stderr
      - fixing small syntax/runtime defects in the script if execution fails
      - showing the resulting diff
      - committing exactly the script-generated file changes after validation
    must_not:
      - redesign the process
      - reinterpret the repair plan
      - choose patch grouping
      - perform architecture reasoning
      - read large source sets to decide what to do
      - generate substitute prose by itself
```

### Iterative patch-pack builder process

The patch pack must be built iteratively by **actual repo target path**, not by repair-area count.

```yaml
iterative_patch_process:
  initial_control_read_only:
    read_once:
      - manifest.json
      - 00-global-rules.md
      - 03-target-file-map.md
      - 04-feature-repair-index.md
      - 06-validation-contract.md
      - 09-final-execution-order.md
    forbidden:
      - reading all target repair plans upfront
      - reading all live target files upfront
      - broad repo inspection before patch groups
      - re-discovering the execution environment after the first preflight

  patch_grouping:
    rule: one_git_generated_patch_per_actual_repo_target_path
    same_target_repairs:
      action: collapse_into_one_patch
      example:
        target: apex-meta/scripts/apex_kb.py
        repair_areas:
          - pointer_only_phase0
          - quality_coverage
          - query_eval
          - graph_process_flow
          - status_freshness_split
          - cli_output_json_regression_if_needed
    forbidden:
      - one patch per repair-area plan file when those plans modify the same target file
      - many independent patches against the same original baseline unless the plan explicitly defines an ordered stack

  per_patch_group_loop:
    for_each_target_path:
      read_only_now:
        - mapped target plan file or files for this target path
        - the single live target file for this group
        - directly relevant validation-contract section
      then:
        - edit only this one target file
        - generate the patch with git diff
        - verify the patch is non-empty when a change is expected
        - run git apply --check for this patch
        - temporarily apply cumulative patch set in order
        - verify changed-file scope remains limited to expected target paths
        - revert runtime/documentation target files before final builder state
        - append validation result to the patch-pack ledger

  stop_rules:
    if_real_source_or_target_file_cannot_be_read:
      action: stop_and_report_missing_file
      forbidden: fabricate_placeholder_content
    if_patch_cannot_be_validated:
      action: stop_and_report_failed_patch
      forbidden:
        - PASS_WITH_WORKAROUNDS
        - manual hunk rewriting without git diff regeneration
        - marker-only validation for executable behavior
```

### Required patch-pack output shape

```yaml
required_patch_pack_shape:
  patch_pack_root: apex-meta/patches/apex-kb-v3-repair/
  implementation_patches:
    - patch: 001-apex-kb-py-repair.patch
      target: apex-meta/scripts/apex_kb.py
      covers:
        - pointer_only_phase0
        - quality_coverage
        - query_eval
        - graph_process_flow
        - status_freshness_split
        - cli_output_json_regression_if_needed
      required: true

    - patch: 002-apex-kb-retrieval-py-repair.patch
      target: apex-meta/scripts/apex_kb_retrieval.py
      covers:
        - retrieval_cli_output_json_regression_if_needed
      required: conditional_after_live_inspection

    - patch: 003-script-command-contract.patch
      target: .claude/skills/apex-kb/references/script-command-contract.md
      covers:
        - script_command_contract_alignment
      required: true

    - patch: 004-kb-contract.patch
      target: .claude/skills/apex-kb/references/kb-contract.md
      covers:
        - kb_contract_alignment
      required: true

    - patch: 005-acceptance-tests.patch
      target: .claude/skills/apex-kb/references/acceptance-tests.md
      covers:
        - acceptance_tests
      required: true

    - patch: 006-ingest-query-lint-audit-rules.patch
      target: .claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md
      covers:
        - phase2_value_contract_alignment
      required: true

    - patch: 007-package-manifest.patch
      target: .claude/skills/apex-kb/package-manifest.md
      covers:
        - package_manifest_plan_ledger
      required: true

  metadata_artifacts:
    - manifest.json
    - validation-report.md
    - 999-codex-apply-handoff.md
```

### Forbidden process patterns

```yaml
forbidden_patterns:
  - Codex decides what the process should be.
  - Codex reads all source files and synthesizes the plan.
  - Agent/Codex reads all target plans upfront before patch grouping.
  - Agent/Codex reads all live targets upfront.
  - The worker searches the filesystem repeatedly after live-git preflight failure.
  - The worker creates a synthetic git repo and calls it Git-native validation.
  - The worker reconstructs target baselines from segmented API snippets.
  - The worker creates placeholder patches.
  - The worker reports PASS when real source access, real target access, or behavior validation failed.
```
{PATCHPLAN_END}
"""


AGENT_PROMPT_BLOCK = f"""{AGENT_START}
## Binding Correction — Scripted Execution, Not Codex Thinking

This section is binding and supersedes any conflicting instruction elsewhere in this prompt.

### Role clarity

```yaml
role_clarity:
  chatgpt_pro_thinking_is_the_intelligence:
    responsibilities:
      - read all selected process/source files
      - define the corrected process
      - encode the correction into deterministic scripts
      - specify exact target files and allowed changes
      - decide patch grouping and validation doctrine

  codex_is_the_executor:
    responsibilities:
      - run the provided script exactly
      - report command output
      - fix small Python syntax/runtime mistakes only when necessary
      - show generated diffs
      - commit only the script-generated changes after validation
    forbidden:
      - deciding architecture
      - selecting process rules
      - rewriting the prompt from its own interpretation
      - generating patch-plan prose manually
      - reading broad context to decide what should happen
```

### Execution constraint

The executor must not think through the Apex patching process. It must run the deterministic updater produced by ChatGPT/Pro Thinking.
ChatGPT/Pro Thinking owns the reasoning.
Codex/local executor only runs this script.

```yaml
execution_contract:
  input:
    - deterministic_python_update_script
  target_files:
    - apex-meta/SmallSkills/Patching/AgnetModeNew/Patchplan.md
    - apex-meta/SmallSkills/Patching/AgnetModeNew/AgentPrompt_v4.md
  allowed_actions:
    - python <script> --check
    - python <script> --apply
    - python -m py_compile <script>
    - git diff -- target files
    - commit script-generated changes
  disallowed_actions:
    - redesigning Patchplan.md
    - redesigning AgentPrompt_v4.md
    - changing additional files because they seem relevant
    - inventing fallback instructions
    - broad repo or file discovery
```

### Iterative process to enforce in the prompt

```yaml
iterative_patch_pack_builder:
  first:
    read_control_files_once:
      - manifest.json
      - 00-global-rules.md
      - 03-target-file-map.md
      - 04-feature-repair-index.md
      - 06-validation-contract.md
      - 09-final-execution-order.md

  then:
    iterate_by_actual_target_path:
      - read mapped target plan file(s) for the current target only
      - read the one live target file
      - make all same-target repairs together
      - generate one git diff patch for that target
      - validate with git apply --check
      - update validation ledger
      - revert target file before final artifact-only state

  never:
    - read all target plans upfront
    - read all live targets upfront
    - rely on memory across patch groups
    - use failed historical patch files as implementation authority
    - use marker-only validation as proof of behavior
```

### Hard stop instead of fabrication

```yaml
fabrication_guard:
  if_budget_or_access_is_insufficient:
    required_action: stop_after_last_real_completed_file_and_report_remaining_files
    forbidden_action: create_placeholder_content_or_dummy_patches
  if_no_real_live_git_worktree_for_git_native_task:
    required_action: WRONG_EXECUTOR_or_stop_according_to_prompt
    forbidden_action:
      - repeated filesystem search
      - git clone
      - git init
      - synthetic repository construction
      - GitHub/API snippet baseline reconstruction
```
{AGENT_END}
"""


@dataclass(frozen=True)
class Target:
    label: str
    filename: str
    start_marker: str
    end_marker: str
    block: str


TARGETS = [
    Target("patchplan", PATCHPLAN_FILENAME, PATCHPLAN_START, PATCHPLAN_END, PATCHPLAN_BLOCK),
    Target("agent_prompt_v4", AGENT_PROMPT_FILENAME, AGENT_START, AGENT_END, AGENT_PROMPT_BLOCK),
]


def read_text(path: Path) -> str:
    for encoding in ("utf-8-sig", "utf-8"):
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError("utf-8", b"", 0, 1, f"Could not decode {path}")


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8", newline="\n")


def find_base_dir(repo_root: Path) -> Path:
    existing = [repo_root / candidate for candidate in BASE_CANDIDATES if (repo_root / candidate).is_dir()]
    if len(existing) == 1:
        return existing[0]
    if len(existing) > 1:
        preferred = repo_root / BASE_CANDIDATES[0]
        return preferred if preferred in existing else existing[0]
    candidates = "\n".join(f"  - {candidate}" for candidate in BASE_CANDIDATES)
    raise FileNotFoundError(f"Could not find AgentModeNew folder. Checked:\n{candidates}")


def first_h1_insert_index(text: str) -> int:
    lines = text.splitlines(keepends=True)
    for i, line in enumerate(lines):
        if line.startswith("# "):
            return i + 1
    return 0


def replace_or_insert_managed_block(original: str, target: Target) -> tuple[str, str]:
    start = original.find(target.start_marker)
    end = original.find(target.end_marker)

    block = target.block.strip() + "\n\n"

    if start != -1 and end != -1 and end > start:
        end_pos = end + len(target.end_marker)
        while end_pos < len(original) and original[end_pos] in "\r\n":
            end_pos += 1
        updated = original[:start] + block + original[end_pos:]
        return updated, "replaced_existing_managed_block"

    if start != -1 or end != -1:
        raise ValueError(
            f"Partial managed block found in {target.filename}; start/end markers inconsistent. "
            "Fix manually before running this script."
        )

    lines = original.splitlines(keepends=True)
    idx = first_h1_insert_index(original)

    if idx == 0:
        updated = block + original
    else:
        updated = "".join(lines[:idx]) + "\n" + block + "".join(lines[idx:])

    return updated, "inserted_new_managed_block"


def unified_diff(path: Path, before: str, after: str, repo_root: Path) -> str:
    rel = path.relative_to(repo_root).as_posix()
    return "".join(
        difflib.unified_diff(
            before.splitlines(keepends=True),
            after.splitlines(keepends=True),
            fromfile=f"a/{rel}",
            tofile=f"b/{rel}",
        )
    )


def assert_required_content(texts: dict[str, str]) -> None:
    combined = "\n".join(texts.values())
    required = [
        "ChatGPT/Pro Thinking owns the reasoning",
        "Codex/local executor only runs this script",
        "one_git_generated_patch_per_actual_repo_target_path",
        "read_control_files_once",
        "read all target plans upfront",
        "placeholder patches",
        "synthetic git repo",
        "stop_after_last_real_completed_file_and_report_remaining_files",
        "001-apex-kb-py-repair.patch",
        "pointer_only_phase0",
        "quality_coverage",
        "query_eval",
        "graph_process_flow",
        "status_freshness_split",
    ]
    missing = [item for item in required if item not in combined]
    if missing:
        raise AssertionError("Updated files are missing required terms:\n" + "\n".join(f"- {m}" for m in missing))


def build_report(
    base_dir: Path,
    actions: list[tuple[Path, str]],
    mode: str,
    changed: bool,
    diffs: dict[Path, str],
    repo_root: Path,
) -> str:
    timestamp = datetime.now().isoformat(timespec="seconds")
    action_lines = "\n".join(
        f"  - path: {path.relative_to(repo_root).as_posix()}\n    action: {action}"
        for path, action in actions
    )
    changed_files = "\n".join(f"  - {path.relative_to(repo_root).as_posix()}" for path in diffs if diffs[path])
    return f"""# AgentModeNew Process Update Report

```yaml
generated_at: "{timestamp}"
mode: "{mode}"
base_dir: "{base_dir.relative_to(repo_root).as_posix()}"
changed: {str(changed).lower()}
changed_files:
{changed_files if changed_files else "  []"}
actions:
{action_lines if action_lines else "  []"}
validation:
  required_content_present: true
  target_files_only: true
```

## Purpose

This report was generated by `update_agentmode_new_patch_process.py`.

The script updates `Patchplan.md` and `AgentPrompt_v4.md` so that Codex is treated as a deterministic executor only. The reasoning and process design are encoded into the script and managed blocks.
"""


def parse_args(argv: Optional[Iterable[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="Preview changes and validate required content. Do not write target files.")
    mode.add_argument("--apply", action="store_true", help="Apply changes, create backups, and write a report.")
    parser.add_argument("--repo-root", default=".", help="Repository root. Defaults to current directory.")
    parser.add_argument("--no-backup", action="store_true", help="Do not create backups in --apply mode.")
    return parser.parse_args(argv)


def main(argv: Optional[Iterable[str]] = None) -> int:
    args = parse_args(argv)
    repo_root = Path(args.repo_root).resolve()
    base_dir = find_base_dir(repo_root)

    desired_texts: dict[str, str] = {}
    originals: dict[Path, str] = {}
    updates: dict[Path, str] = {}
    actions: list[tuple[Path, str]] = []
    diffs: dict[Path, str] = {}

    for target in TARGETS:
        path = base_dir / target.filename
        if not path.is_file():
            raise FileNotFoundError(f"Required target file not found: {path}")

        original = read_text(path)
        updated, action = replace_or_insert_managed_block(original, target)

        originals[path] = original
        updates[path] = updated
        desired_texts[target.label] = updated
        actions.append((path, action))
        diffs[path] = unified_diff(path, original, updated, repo_root)

    assert_required_content(desired_texts)

    changed = any(originals[p] != updates[p] for p in updates)
    mode = "check" if args.check else "apply"

    print(f"MODE: {mode}")
    print(f"BASE_DIR: {base_dir.relative_to(repo_root).as_posix()}")
    print(f"CHANGED: {changed}")

    for path, diff in diffs.items():
        rel = path.relative_to(repo_root).as_posix()
        print(f"\n--- DIFF: {rel} ---")
        print(diff if diff else "(no changes)")

    if args.check:
        print("\nCHECK_RESULT: PASS")
        return 0

    backup_dir = None
    if changed and not args.no_backup:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        backup_dir = base_dir / "_script-backups" / timestamp
        backup_dir.mkdir(parents=True, exist_ok=False)
        for path in originals:
            shutil.copy2(path, backup_dir / path.name)

    for path, updated in updates.items():
        if originals[path] != updated:
            write_text(path, updated)

    report = build_report(base_dir, actions, mode, changed, diffs, repo_root)
    report_path = base_dir / f"update-report-{datetime.now().strftime('%Y%m%d-%H%M%S')}.md"
    write_text(report_path, report)

    print(f"\nAPPLY_RESULT: PASS")
    if backup_dir:
        print(f"BACKUP_DIR: {backup_dir.relative_to(repo_root).as_posix()}")
    print(f"REPORT: {report_path.relative_to(repo_root).as_posix()}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
