# Apex Harmonization Validation Fixtures

## 0. Purpose

Define minimal deterministic test fixtures for the Apex harmonization scripts and the canonical task schema. By supplying a small set of task files and handoff documents with known statuses and dependencies, these fixtures allow consistent static and runtime testing of the scripts without relying on the broader repository state. The fixtures must not be mutated by the scripts under test.

## 1. Fixture file tree

```
apex-meta/epics/fixture-alpha/  001.md  002.md  003.mdapex-meta/handoff/  task_plan.md  findings.md  progress.md  next-session.md
```

The `fixture-alpha` epic contains three task files in Markdown front‑matter format. The `handoff` directory provides session artefacts used by session and stall detection scripts.

## 2. Fixture task records

|File|status|priority|due_date|depends_on|
|---|---|---|---|---|
|**001.md**|done|high|2026‑06‑25|[]|
|**002.md**|open|medium|2026‑06‑26|[1]|
|**003.md**|open|high|2026‑06‑27|[2]|

Each task file will include YAML front‑matter matching the field schema (`id`, `status`, `priority`, `due_date`, `depends_on`) followed by a title and body. Task 002 depends on Task 001, and Task 003 depends on Task 002. Task 001 is marked `done`, so Task 002 is actionable; Task 003 is blocked until Task 002 is done.

## 3. Expected script behavior

|Script|Static check|Runtime check|Fixture check|Expected result|
|---|---|---|---|---|
|`find_next_task.py`|Should ignore tasks with `status` of `done` or `deferred`, and enforce that all dependencies exist and are done.|Should produce a deterministic ordering based on priority (high > medium), fewer dependencies first, then by numeric ID.|With the fixture, 002 is the next actionable task; 001 is done and excluded; 003 is blocked by 002.|Returns Task 002 as the sole actionable task.|
|`show_blocked.py`|Must distinguish between tasks blocked because dependencies are missing vs. incomplete, and sort deterministically.|Should not mutate any files.|In the fixture, Task 003 is blocked because Task 002 is not yet done.|Reports that Task 003 is blocked by Task 002.|
|`update_index.py --dry-run`|Should traverse `apex-meta/epics` and the handoff directory, build an index that includes explicit relative file paths, and respect the `--dry-run` flag by not writing to the registry.|Must output the index to STDOUT in dry‑run mode without writing files.|Running against the fixture should list the three tasks with their relative paths and the four handoff files.|Index includes explicit paths like `epics/fixture-alpha/001.md` and does not write `registry/index.md`.|
|`drift_check.py`|Should parse the registry index (when present) and compare it with the actual file system, ignoring table headers and separators.|Should report missing entries and orphan files deterministically.|After rebuilding the index (not in dry‑run), running drift check against the fixture should report no drift.|Reports “No drift detected” because the index matches the files.|
|`stall_detect.py`|Should define the expected `progress.md` format in its docstring and parse task ID, status, updated timestamp, and title deterministically.|Must avoid false stalls when a task appears in fewer than the required number of sessions and report insufficient history clearly.|Using the fixture’s `progress.md`, the script should identify tasks with no updates across the defined threshold as stalled.|Reports any tasks that have not been updated within the expected window, or notes insufficient history.|

## 4. No‑write validation

All read‑only scripts (`find_next_task.py`, `show_blocked.py`, `update_index.py` with `--dry-run`, `drift_check.py`, `stall_detect.py`) must not mutate any fixture files. Their behavior should be tested by running them against these fixtures, verifying outputs, and then ensuring that the contents of `apex-meta/epics/fixture-alpha` and `apex-meta/handoff` remain unchanged.