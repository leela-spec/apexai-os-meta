# CLI Instructions — Archive Transcript Pipeline V1 Safely

**Purpose:** remove V1 recommendation-shaped files from the active research root without deleting history or breaking V2.1 evidence.

**Execute this as a separate CLI session before beginning S00. Do not implement any V2.1 stage in the same session.**

## Target

Move the three superseded V1 authority files into a clearly historical archive so an implementation AI cannot accidentally treat them as current architecture:

- `SourceTranscriptionAnalysisPipeline_Research/PIPELINE_ARCHITECTURE_OPTIONS_AND_V1_DECISION_2026-08-18.md`
- `SourceTranscriptionAnalysisPipeline_Research/PIPELINE_DECISION_CONTRACT_2026-08-18.yaml`
- `SourceTranscriptionAnalysisPipeline_Research/V1_IMPLEMENTATION_PLAN_CLI_SEMANTIC_WORKER_2026-08-18.md`

Archive destination:

`SourceTranscriptionAnalysisPipeline_Research/archive/transcript-pipeline-v1-2026-08-18/`

Do **not** delete Git history. Do **not** archive V2/V2.1 files. Do **not** move benchmark inputs, transcripts, historical evaluation evidence, or TTK runtime code merely because they predate V2.1.

## Context to load

Read only:

1. this file;
2. `v2-reuse-bakeoff/00-START-HERE.md`;
3. the three V1 files listed above;
4. repository references returned by a targeted search for those exact three filenames.

Do not read the full research corpus.

## Procedure

1. Verify repository, branch, and clean/known working state:

```powershell
git rev-parse --show-toplevel
git branch --show-current
git status --short
git pull --ff-only origin main
```

Repository must be `leela-spec/apexai-os-meta`; branch must be `main`.

2. Create the archive directory.

3. Move the three files with `git mv`, preserving filenames.

4. Create `SourceTranscriptionAnalysisPipeline_Research/archive/transcript-pipeline-v1-2026-08-18/README.md` containing:
   - status: historical/superseded;
   - original purpose of V1;
   - exact three archived files;
   - current authority pointer to `v2-reuse-bakeoff/00-START-HERE.md`;
   - explicit warning that V1 component-selection conclusions must not control V2.1 implementation.

5. Search the repository for **exact references to the old paths**. Update only references whose purpose is to navigate to the file. Preserve historical prose that names V1 as historical evidence. Where a current V2.1 file intentionally lists V1 as superseded history, update the path to the archive path rather than deleting the statement.

6. Do not rename V2.1 to V3 and do not rewrite V2.1 architecture during this archival task.

## Tests

Run:

```powershell
git status --short
git diff --check
git grep -n "PIPELINE_ARCHITECTURE_OPTIONS_AND_V1_DECISION_2026-08-18.md"
git grep -n "PIPELINE_DECISION_CONTRACT_2026-08-18.yaml"
git grep -n "V1_IMPLEMENTATION_PLAN_CLI_SEMANTIC_WORKER_2026-08-18.md"
```

Acceptance:

- the three original root paths no longer exist;
- all three archived paths exist;
- current navigation references resolve to archive paths or intentionally describe them as historical;
- `v2-reuse-bakeoff/00-START-HERE.md` remains the current entrypoint;
- no V2/V2.1 runtime or architecture files were unintentionally moved;
- `git diff --check` passes.

## Git

Inspect the diff before staging. Commit only the archive move and reference updates:

```powershell
git add SourceTranscriptionAnalysisPipeline_Research
git diff --cached --stat
git diff --cached --check
git commit -m "docs(transcript): archive superseded V1 architecture"
git push origin main
```

## Required handover back to the orchestrator

Return and save:

`SourceTranscriptionAnalysisPipeline_Research/v2-reuse-bakeoff/execution-modules/handover-V1-archive.md`

with:

```yaml
module: V1_ARCHIVE
status: PASS|FAIL|BLOCKED
start_head: <sha>
end_head: <sha-or-null>
archived_files: []
references_updated: []
tests_run: []
remaining_old_path_references: []
unrelated_dirty_paths: []
notes: []
```

Then **STOP**. Do not begin S00. The operator will give the handover to the orchestrator for review.