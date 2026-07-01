# Codex Process Report: Scripted File Movement Token Burn

Date: 2026-07-01
Repository: `C:\GitDev\apexai-os-meta`
Context: Claude orchestration KB merge script execution and push to `main`

## What went wrong

The task was operationally simple: copy an already-defined PowerShell script into the repo, run it locally, fix only direct syntax/runtime issues, and push the resulting local state to `main`.

The execution became too complex because the agent allowed Git branch state, push rejection handling, very large generated files, and verbose readbacks to expand the work beyond the user's intended "local first, then push main" workflow.

Specific friction points:

- The work started from a non-main branch instead of first normalizing to `main`.
- The branch reconciliation became a prominent part of the workflow instead of a small prerequisite.
- The agent spent too many tokens narrating and inspecting broad output from large file operations.
- GitHub's 100 MB blob rejection was handled only after a large push attempt, instead of checking large tracked blobs before push.
- The script output and commit output were allowed to flood the context.
- The final reporting focused on the completed operation, but did not sufficiently acknowledge the process cost.

## Better operating model

For deterministic local file movement, use a short, command-driven workflow:

1. Start on `main`.
2. Pull `main`.
3. Check dirty state.
4. Copy or create the requested script.
5. Run only the requested script.
6. Fix only syntax/runtime failures needed for that script.
7. Verify expected output files exist.
8. Check Git for oversized blobs before commit or push.
9. Commit and push to `main`.
10. Report concise facts.

Avoid turning file movement into lifecycle analysis, semantic review, branch design, or broad repo discovery unless the script fails in a way that requires it.

## Rules for future script execution

### Branch and sync rules

- Default to `main` unless the user explicitly asks for another branch.
- If a prerequisite folder exists only on another branch, merge or restore the needed files into `main` as a short setup step, then continue on `main`.
- Do not create new working branches for local deterministic operations when the user says to push to `main`.
- Before pushing, run:

```powershell
git status --short --branch
git rev-parse HEAD
git rev-parse origin/main
```

### Token control rules

- Do not print full commit output for thousands of files.
- Use summary commands:

```powershell
git diff --stat
git status --short
Get-ChildItem <expected-output-dir> | Select-Object Name, Length
```

- Redirect or summarize noisy command output where possible.
- Do not read generated ledgers in full. Read only headers, counts, and required report fields.
- Prefer machine checks over prose inspection.

### Script execution rules

- Treat the provided script as the source of truth.
- Do not replace explicit copy plans with heuristic discovery.
- Dynamic discovery, if present in the script, is audit-only.
- Fix only:
  - PowerShell parser errors
  - runtime compatibility errors
  - missing required local paths
  - Git transport blockers
- Do not run unrelated lifecycle commands unless explicitly requested.

### File movement rules

- Preserve existing source KB roots.
- Do not delete or move existing KB roots.
- If destination files already exist, let the script's conflict behavior decide.
- If a copied tree contains nested `.git` directories, remove only nested `.git` directories inside the newly created destination copy before staging.
- Never remove nested `.git` directories from original source roots unless explicitly instructed.

### Large file rules

Before commit or push, check tracked blobs:

```powershell
@'
import subprocess
out = subprocess.check_output(["git", "ls-tree", "-r", "-l", "HEAD"], text=True, encoding="utf-8", errors="replace")
for line in out.splitlines():
    parts = line.split(None, 4)
    if len(parts) >= 5 and parts[3].isdigit() and int(parts[3]) > 100_000_000:
        print(parts[3], parts[4])
'@ | python -
```

If a generated uncompressed artifact exceeds GitHub's blob limit:

- Prefer tracking the compressed equivalent if one exists.
- Add a narrow `.gitignore` entry for the oversized generated artifact.
- Report the omission clearly.
- Do not repeatedly attempt doomed pushes.

### Commit and push rules

- Stage intentionally:

```powershell
git add <script> <destination-kb> <required-source-files>
```

- Commit once if practical.
- If a transport-only fix is required, amend the same commit before pushing.
- Push only after confirming no oversized tracked blobs.

### Reporting rules

Final reports for simple script operations should fit in one screen and include:

- verdict
- branch
- commit pushed
- script run
- files/reports created
- source roots copied
- missing roots
- conflicts
- audit-only candidates
- duplicate hash group count
- lifecycle commands executed: true/false
- known local untracked files left untouched
- next step

Do not paste massive command output into the conversation.

## Recommended reusable preflight wrapper

For future deterministic copy scripts, create a small wrapper that:

1. Confirms branch is `main`.
2. Pulls `origin main`.
3. Runs `git status --short`.
4. Runs the target script.
5. Verifies expected report paths.
6. Checks for tracked blobs over 100 MB.
7. Prints a compact JSON/YAML summary.

The wrapper should not perform semantic KB lifecycle actions. Its role is operational hygiene only.

## Bottom line

For already-defined file movement scripts, Codex should be a careful local executor, not a workflow designer. The right behavior is to keep the process narrow, reduce output volume, check Git transport constraints early, and push the resulting `main` state with a compact audit trail.
