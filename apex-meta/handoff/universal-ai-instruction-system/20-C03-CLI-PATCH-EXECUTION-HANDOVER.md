---
okf: 0.2
type: cli_execution_handover
id: c03-cli-exact-match-patch-execution
created: 2026-09-23
status: ready
repository: leela-spec/apexai-os-meta
branch: main
expected_patch_authoring_base: 244c2d15a91d60e06f9989ae402efd00871c0700
---

# C03 CLI exact-match patch execution

## objective

Apply the already-authored C03 patch packet deterministically to live `main`, verify the diff, commit, push, and stop.

Do not research C03 again.
Do not edit patch content.
Do not modify any other existing file.
Do not start cross-module synthesis in this run.

## read first

1. `apex-meta/handoff/universal-ai-instruction-system/18-EXISTING-FILE-MUTATION-GUARDRAIL.md`
2. `apex-meta/handoff/universal-ai-instruction-system/patches/2026-09-23-c03-conditional-informatics/README.md`
3. `apex-meta/handoff/universal-ai-instruction-system/patches/2026-09-23-c03-conditional-informatics/P01-C03-pilot-informatics-router.patch.md`
4. `apex-meta/handoff/universal-ai-instruction-system/patches/2026-09-23-c03-conditional-informatics/P02-C03-readme-status.patch.md`

## sync

~~~powershell
Set-Location C:\GitDev\apexai-os-meta
git status --short --branch
git branch --show-current
git fetch origin
git pull --ff-only origin main
~~~

Requirements:

- branch = `main`;
- preserve unrelated dirty files;
- if unrelated local edits overlap either target, STOP;
- never use reset --hard, clean -fd, force push, or branch creation.

## apply P01

Target:

`apex-meta/handoff/universal-ai-instruction-system/08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md`

Use exact string replacement from the patch artifact.

Require old block count == 1.

After writing:

~~~powershell
git diff -- apex-meta/handoff/universal-ai-instruction-system/08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md
~~~

Accept only the localized C03 block replacement.

## apply P02

Only after P01 passes.

Target:

`apex-meta/handoff/universal-ai-instruction-system/README.md`

Require old row count == 1.

After writing:

~~~powershell
git diff -- apex-meta/handoff/universal-ai-instruction-system/README.md
~~~

Accept only C03 `NEXT -> DONE`.

## full verification

~~~powershell
git status --short
git diff --check
git diff --stat
git diff
~~~

Expected modified existing files: exactly 2.

Do not alter the C03 result or patch packet.

## commit

~~~powershell
git add -- apex-meta/handoff/universal-ai-instruction-system/08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md
git add -- apex-meta/handoff/universal-ai-instruction-system/README.md
git diff --cached --check
git diff --cached --stat
git diff --cached
git commit -m "docs(agent-contract): apply verified C03 exact-match patches"
~~~

## push

~~~powershell
git fetch origin
git status --short --branch
git push origin main
~~~

If remote `main` moved and either target region conflicts, STOP. Do not force or improvise.

## post-push verification

~~~powershell
git fetch origin
git rev-parse HEAD
git rev-parse origin/main
git status --short --branch
git show --stat --oneline HEAD
~~~

Verify:

- HEAD == origin/main;
- exactly two existing files changed in the patch commit;
- C03 = DONE;
- no module is marked NEXT;
- no unrelated file changed.

## stop

The existing Program stop condition now applies.

Do not start another module.

The next project phase is separate cross-module synthesis and controlled evaluation.
