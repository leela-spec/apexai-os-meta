---
okf: 0.2
type: cli_execution_handover
id: c02-cli-sync-and-patch-execution
created: 2026-09-23
status: ready
repository: leela-spec/apexai-os-meta
branch: main
expected_start_commit: 62724825f8d454e431b5e60f8c88e97245908853
---

# C02 CLI sync + deterministic patch execution handover

## role

You are the **local CLI patch executor**.

Your job is narrow:

1. sync the local repository to the live remote `main`;
2. verify the repository is at the expected repaired state;
3. apply the already-authored C02 exact-match patches;
4. verify that **only** the intended localized changes occurred;
5. commit and push the patch application to `main`;
6. stop.

Do not perform new research.
Do not rewrite the patch contents.
Do not continue into C03.
Do not make opportunistic cleanup or formatting changes.

Repository:

`leela-spec/apexai-os-meta`

Branch:

`main` only

Preferred local path if present:

`C:\GitDev\apexai-os-meta`

## authority

Read first, in this order:

1. `apex-meta/handoff/universal-ai-instruction-system/18-EXISTING-FILE-MUTATION-GUARDRAIL.md`
2. `apex-meta/handoff/universal-ai-instruction-system/patches/2026-09-22-c02-conditional-research-discipline/README.md`
3. `apex-meta/handoff/universal-ai-instruction-system/patches/2026-09-22-c02-conditional-research-discipline/P01-C02-pilot-research-block.patch.md`
4. `apex-meta/handoff/universal-ai-instruction-system/patches/2026-09-22-c02-conditional-research-discipline/P02-C02-readme-status.patch.md`

The patch artifacts are authoritative for the intended existing-file changes.

Do **not** reconstruct changes from chat history, model memory, or the C02 research README.

## mandatory preflight

### 1. enter repository

PowerShell:

~~~powershell
Set-Location C:\GitDev\apexai-os-meta
~~~

If the repository exists elsewhere, use the actual local path.

### 2. confirm branch and working tree

~~~powershell
git status --short --branch
git branch --show-current
~~~

Requirements:

- current branch must be `main`;
- do not create or switch to another branch;
- unrelated local dirty files must not be overwritten, staged, reverted, reformatted, or included.

If unrelated dirty files overlap either patch target, **STOP** and report the conflict.

### 3. synchronize without destroying local state

~~~powershell
git fetch origin
git status --short --branch
git rev-parse HEAD
git rev-parse origin/main
~~~

If local `main` is clean and only behind remote:

~~~powershell
git pull --ff-only origin main
~~~

If local `main` has unrelated local changes, do not reset them. Use a safe fast-forward only if Git permits it without touching those files. Otherwise STOP and report the condition.

Never use:

- `git reset --hard`
- `git clean -fd`
- force push
- checkout/restore of unrelated files
- branch creation

### 4. verify repaired baseline

Expected remote repaired commit at handover creation:

`62724825f8d454e431b5e60f8c88e97245908853`

The live repository may have advanced since this handover. Therefore:

- do not require HEAD to equal that SHA;
- require the two patch `old` blocks to match current live files exactly once;
- if either match count is not exactly one, STOP;
- do not adapt the patch from memory.

Target files:

1. `apex-meta/handoff/universal-ai-instruction-system/08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md`
2. `apex-meta/handoff/universal-ai-instruction-system/README.md`

## patch execution rule

For each patch:

1. parse the exact `old` block;
2. parse the exact `new` block;
3. read the current target file from disk;
4. count exact occurrences of the `old` block;
5. require count == 1;
6. replace exactly that one occurrence;
7. write the file without altering any other bytes/content;
8. immediately inspect the diff;
9. reject and restore the target file if any unrelated change appears.

Do not regenerate a complete target file from a model-authored copy.

## recommended deterministic application method

Use a small local script or exact string replacement, not free-form model editing.

Example Python pattern:

~~~python
from pathlib import Path

path = Path("TARGET")
old = """EXACT OLD BLOCK"""
new = """EXACT NEW BLOCK"""

text = path.read_text(encoding="utf-8")
count = text.count(old)

if count != 1:
    raise SystemExit(f"STOP: expected exactly 1 match, got {count}")

updated = text.replace(old, new, 1)
path.write_text(updated, encoding="utf-8")
~~~

Important:

- copy `old` and `new` character-for-character from the patch artifact;
- do not normalize whitespace;
- do not reflow Markdown;
- do not change line endings intentionally;
- if line-ending conversion causes broad diff churn, restore and use a method that preserves the existing file format.

## patch order

### P01 — C02 pilot research block

Apply:

`patches/2026-09-22-c02-conditional-research-discipline/P01-C02-pilot-research-block.patch.md`

Target:

`08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md`

After application:

~~~powershell
git diff -- apex-meta/handoff/universal-ai-instruction-system/08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md
~~~

Acceptance:

- exactly the C02 `<research>` block changes;
- no neighboring XML module changes;
- no full-file rewrite;
- no whitespace-only churn elsewhere.

### P02 — program status

Only after P01 passes verification, apply:

`patches/2026-09-22-c02-conditional-research-discipline/P02-C02-readme-status.patch.md`

Target:

`README.md`

After application:

~~~powershell
git diff -- apex-meta/handoff/universal-ai-instruction-system/README.md
~~~

Acceptance:

- C02 changes `NEXT -> DONE`;
- C03 changes `QUEUED -> NEXT`;
- no other README text changes.

## full verification

Run:

~~~powershell
git status --short
git diff --check
git diff --stat
git diff
~~~

Expected existing-file changes:

- `08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md`
- `README.md`

No other pre-existing file may be modified by this execution.

The already-existing additive C02 artifacts should remain untouched:

- `module-deepening/C02-conditional-research-discipline/README.md`
- `module-deepening/C02-conditional-research-discipline/SKILL.md`
- patch packet files
- mutation guardrail

## semantic verification

Confirm after patching:

### live README

Must show:

~~~text
| C02 | `<research>` | Conditional Research Discipline | **DONE** |
| C03 | `<informatics>` | Conditional Informatics / Formal Authoring | **NEXT** |
~~~

### live pilot

Must contain the C02 block from P01 exactly.

### C02 research artifacts

Confirm these exist:

~~~powershell
Test-Path apex-meta/handoff/universal-ai-instruction-system/module-deepening/C02-conditional-research-discipline/README.md
Test-Path apex-meta/handoff/universal-ai-instruction-system/module-deepening/C02-conditional-research-discipline/SKILL.md
~~~

Both must return `True`.

## commit

Stage **only** the two intended target files:

~~~powershell
git add -- apex-meta/handoff/universal-ai-instruction-system/08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md
git add -- apex-meta/handoff/universal-ai-instruction-system/README.md
git status --short
~~~

Before committing, verify no unrelated file is staged:

~~~powershell
git diff --cached --check
git diff --cached --stat
git diff --cached
~~~

Commit:

~~~powershell
git commit -m "docs(agent-contract): apply verified C02 exact-match patches"
~~~

## push

Before push:

~~~powershell
git fetch origin
git status --short --branch
~~~

If `origin/main` advanced after the patch was prepared:

- do not force push;
- do not blindly rebase through conflicts;
- verify the exact patched regions still represent the intended current state;
- if a conflict touches either target block, STOP and report.

If safe:

~~~powershell
git push origin main
~~~

## post-push verification

Run:

~~~powershell
git fetch origin
git rev-parse HEAD
git rev-parse origin/main
git status --short --branch
~~~

Requirements:

- HEAD == origin/main;
- branch == main;
- no accidental staged changes;
- unrelated local dirty files, if any existed before, remain untouched.

Then inspect the pushed commit:

~~~powershell
git show --stat --oneline HEAD
git show --format=fuller --stat HEAD
~~~

Expected commit change set:

- exactly 2 modified existing files;
- no deleted files;
- no unrelated files.

## stop conditions

STOP without improvising if any of these occurs:

- not on `main`;
- patch old block matches zero times;
- patch old block matches more than once;
- target file has overlapping unrelated local edits;
- applying the patch creates broad whitespace/line-ending churn;
- diff includes any unrelated existing file;
- remote `main` moved in a way that changes either target block;
- merge/rebase conflict touches either patch target;
- patch intent is no longer compatible with live README/current truth.

Do not create a replacement patch yourself unless explicitly instructed by the operator.

## required final report

Return only concise execution evidence:

- starting HEAD;
- synced `origin/main` SHA;
- P01 match count;
- P02 match count;
- changed files;
- `git diff --check` result;
- commit SHA;
- pushed `origin/main` SHA;
- confirmation that C02 is DONE and C03 is NEXT;
- confirmation that no unrelated existing file changed.

## final invariant

~~~text
sync live main
-> verify exact patch preconditions
-> apply P01 exactly once
-> verify localized diff
-> apply P02 exactly once
-> verify localized diff
-> stage only two target files
-> commit
-> push main without force
-> verify
-> stop
~~~
