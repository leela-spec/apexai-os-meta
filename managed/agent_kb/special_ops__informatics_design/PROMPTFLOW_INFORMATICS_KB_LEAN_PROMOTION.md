---
status: active_promptflow
created_at: 2026-05-03
repo: leela-spec/apexai-os-meta
branch: main
target_agent: special_ops__informatics_design
target_root: managed/agent_kb/special_ops__informatics_design
scope: informatics_kb_lean_promotion
mode: newversion_base_plus_missing_apex_logic
---

# PROMPTFLOW — Informatics KB Lean Promotion

## 0. Purpose

Promote the already-final Informatics KB files from `newversion/` into the standard Informatics KB paths while preserving only valid Apex AI OS logic that exists in the current standard files but is missing from the new files.

This is not a full rebuild, research pass, or governance expansion.

## 1. Role

You are an Apex AI OS KB migration agent.

Your job is to make the new Informatics KB files become the standard KB files with the smallest useful patch: add only missing Apex-specific operating logic from the old standard files.

## 2. Hard scope

Only modify files under:

```text
managed/agent_kb/special_ops__informatics_design/
```

Default target files:

```text
ESSENCE.md
BEST_PRACTICES.md
MISTAKES.md
TEMPLATES.md
LEARNING_QUEUE.md
appendices/APPENDIX_KB_SOURCE_MANIFEST.md
appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md
appendices/APPENDIX_KB_CANDIDATE_LEDGER.md
appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md
```

Default source folder:

```text
managed/agent_kb/special_ops__informatics_design/newversion/
```

Do not modify:

```text
openclaw.json
runtime config
provider/model config
shared governance files
other agent KB folders
managed/agents/**
```

## 3. Core rule

For every target file:

```text
newversion file is the base
current standard file is only a source of missing Apex AI OS logic
```

Do not preserve old wording merely because it exists.
Do not create new doctrine.
Do not add process appendices by default.
Do not expand the KB unless the missing Apex logic requires it.

## 4. Minimal workflow

For each file:

1. Read the current standard file.
2. Read the matching file under `newversion/`.
3. Identify Apex-specific logic that is present only in the current standard file.
4. Keep only old logic that is still valid for Apex AI OS.
5. Patch that logic into the newversion file with minimal wording.
6. Replace the standard file with the patched newversion file.
7. Fetch back the written file from `main`.

## 5. Matching rule

Use filename matching by default:

```text
newversion/ESSENCE.md -> ESSENCE.md
newversion/BEST_PRACTICES.md -> BEST_PRACTICES.md
newversion/MISTAKES.md -> MISTAKES.md
newversion/TEMPLATES.md -> TEMPLATES.md
newversion/LEARNING_QUEUE.md -> LEARNING_QUEUE.md
newversion/appendices/<name>.md -> appendices/<name>.md
```

If a `newversion/` file is visibly misfiled, pause that file only and report:

```text
file_identity_ambiguous
```

Do not create a full identity-map appendix unless multiple files are misfiled or the operator asks for it.

## 6. What counts as Apex AI OS logic

Preserve old-only logic only when it directly supports Apex AI OS operation, such as:

```text
Apex repo/home assumptions
MetaOps or Special Ops orchestration boundaries
Apex-specific agent authority boundaries
Apex truth/promotion/status constraints
project-to-meta or meta-to-project learning flow
federated repo / release-pack assumptions
no direct runtime/config mutation constraints
QA severity, closure, and escalation rules used by Apex
```

Do not preserve:

```text
generic informatics prose
old phrasing that duplicates the new file
obsolete MasterOfArts-only context
deprecated promptflow notes
branch/process history unless needed for current Apex operation
Apex mentions that only say Apex was forbidden in old runs
```

## 7. Patch discipline

Keep edits compact.

Preferred patch style:

```text
- one short paragraph
- one compact bullet
- one small table row
- one explicit status note
```

Avoid:

```text
large new sections
new appendices
research essays
full migration reports
unnecessary provenance expansion
```

## 8. File order

Patch in this order:

```text
BEST_PRACTICES.md
MISTAKES.md
TEMPLATES.md
LEARNING_QUEUE.md
appendices/APPENDIX_KB_SOURCE_MANIFEST.md
appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md
appendices/APPENDIX_KB_CANDIDATE_LEDGER.md
appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md
ESSENCE.md
```

Patch `ESSENCE.md` last because it is the activation surface.

## 9. Optional single summary artifact

Do not create process artifacts by default.

If a trace is needed, create only this compact file:

```text
appendices/APPENDIX_INFORMATICS_KB_APEX_LOGIC_DELTA.md
```

Use this table only:

```text
|file|apex_logic_added|source_old_file|status|
|---|---|---|---|
```

Allowed status values:

```text
added
not_needed
skipped_ambiguous
skipped_obsolete
```

## 10. Stop conditions

Stop or skip the affected file only when:

```text
matching newversion file is missing
file identity is ambiguous
old Apex logic conflicts with new KB logic
patch would touch non-informatics files
patch would mutate runtime config or governance authority
```

For skipped files, record the skip in the final response or optional delta appendix.

## 11. Final response format

Return:

```text
repo:
branch:
target_root:
files_promoted:
files_skipped:
apex_logic_added:
new_appendices_created:
fetch_back_status:
remaining_questions:
```

Do not claim completion unless every promoted file was fetched back from `main`.
