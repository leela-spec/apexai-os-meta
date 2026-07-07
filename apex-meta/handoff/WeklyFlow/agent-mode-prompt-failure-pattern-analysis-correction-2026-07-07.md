# Correction — Agent Mode Failure Analysis

## Purpose

This is a correction to the earlier failure-pattern analysis for the APEX Step 1 Prompt-Blocker Cleanup Agent Mode runs.

The earlier analysis over-weighted the explanation that the live repo checkout was unavailable. The operator clarified that the correct live checkout was available, as in the working example prompt.

Therefore the better explanation is not simply "missing checkout." The better explanation is:

> The live checkout existed, but the prompt edits changed how Agent Mode was allowed to discover, enter, or use that checkout. Those edits caused the run to fail before reading the source plan or target files.

## Corrected failure explanation

### 1. The prompt changed a working implicit repo-context assumption into brittle explicit environment rules

The working prompt relied on the Agent Mode execution context already being attached to the correct live terminal Git repository. It checked the repo with normal Git preflight commands.

The later patched prompts added environment-specific behavior that was not in the working example:

- force-clone behavior,
- `/home/oai/share/...` assumptions,
- `C:\GitDev\apexai-os-meta` assumptions,
- "must already be inside this exact path" guards,
- hard failure before allowing the agent to use the same repo context mechanism that made the working example succeed.

This means the live checkout could exist, but the prompt could still fail because the prompt required the wrong way of reaching it.

### 2. The clone patch was invalid even if the checkout existed

Adding `git clone` was not only unnecessary. It was actively harmful.

If the live checkout already existed, the correct behavior was to use it. The clone instruction instead forced a new acquisition path that could fail due to network/auth restrictions.

The failure then reflected the bad prompt instruction, not absence of the correct repo.

### 3. The Windows path patch was also invalid even if the checkout existed

Adding `C:\GitDev\apexai-os-meta` as a mandatory Agent Mode start directory was invalid because Agent Mode may not expose the user's local Windows path as its current terminal path.

The correct repo may have been available through Agent Mode's own mounted workspace/context, while the prompt demanded a specific local path that the agent did not see.

So the failure reason:

```yaml
failure_reason: "Prompt was not run from inside the existing apexai-os-meta Git checkout."
```

should be interpreted as:

> The prompt guard was too brittle and checked the wrong access condition.

Not as proof that the checkout was absent.

### 4. The first placeholder-patch failure likely came from allowing an alternate working directory, not from repo absence

The first failed run used `/home/oai/share/patchwork` and produced placeholder patches.

If the correct checkout existed, the failure was not "no repo existed." It was:

- the prompt did not force the agent to stay inside the already-provided repo context,
- the fallback language allowed a substitute local worktree path,
- the prompt did not say that `patchwork`, `git init`, placeholder baselines, and API/file reconstruction must be impossible even in fallback.

The key failure was wrong workspace selection, not necessarily missing workspace.

### 5. The core issue was not repo availability; it was prompt drift from the working example's repo handling

The repeated failures came from replacing the working example's simple repo preflight with new environment logic.

Corrected root cause:

```yaml
root_cause:
  primary: "Prompt drift from working example repo-handling semantics."
  not_primary: "The live repo checkout did not exist."
  mechanism:
    - "Prompt allowed or forced wrong workspace selection."
    - "Prompt added clone/local-path requirements not present in the working prompt."
    - "Prompt did not preserve the working prompt's tested repo-context assumption."
    - "Prompt guarded against failures in ways that prevented the working path from being used."
```

## Correct future invariant

Future prompts should not say:

- clone the repo,
- use `C:\GitDev\...` inside Agent Mode,
- use `/home/oai/share/...`,
- create a repo,
- search arbitrary workspaces,
- use fallback when source plan is unreadable.

Future prompts should preserve the working example pattern:

```text
Use the live terminal Git repository as the only source of truth for patch generation.
Run Git preflight.
If the preflight or source-plan read fails, stop.
Do not create substitute repos or placeholder files.
```

## Updated do-not-repeat rule

Do not diagnose Agent Mode failure as "repo unavailable" merely because a later prompt could not clone or could not satisfy a local path guard.

Instead ask:

1. Did the prompt preserve the working example's repo-context assumption?
2. Did the prompt add a new way to acquire/find/force the repo?
3. Did the prompt allow a substitute directory like `patchwork`?
4. Did the prompt reject the valid mounted checkout because of a bad local-path requirement?
5. Did the prompt fail before executing the exact same preflight shape as the working example?

If yes, the valid explanation is prompt-induced workspace misuse, not missing checkout.

## Corrected one-line conclusion

The repo checkout was available; the prompt edits made Agent Mode use, require, or reject the wrong workspace path. The failure came from not copying the working example's simple repo handling exactly.