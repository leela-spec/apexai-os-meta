# Executor Contract

## Purpose

Define the boundary between planner output and deterministic mutation. The planner supplies semantic intent and replacement content. The executor reads live files, resolves exact targets, mutates only after deterministic checks pass, and reports proof or failure.

## CLI Contract

The approved executor should expose one entrypoint named by the operator or repository policy. The canonical invocation shape is:

```text
python <executor> <command> --intent <patch_intent.json> --policy <patch_policy.json> --repo <repo-root> --report-dir <report-dir>
```

Supported command roles:

| Command | Required behavior |
|---|---|
| `inspect` | Read target files and report candidates without writing. |
| `locate` | Resolve candidate spans, heading sections, or frontmatter blocks and fail on ambiguity. |
| `extract-span` | Copy exact live text selected by the executor into a report for review. |
| `validate-intent` | Validate schema, policy, operation, and path scope before mutation. |
| `apply-intent` | Apply one bounded mutation only after live target uniqueness is proven. |
| `diff` | Emit git-generated diff proof after mutation. |

## Inputs

The executor receives `patch_intent.json`, `patch_policy.json`, a repository root, and a report directory. It may receive natural-language notes only as non-executable report context. It must ignore line numbers, AI-authored old text, and AI-authored unified diff hunks as mutation instructions.

## Reports

Each run writes one machine-readable report into the policy report directory. Success reports include operation status, resolved target summary, changed paths, git diff reference, validation command results, and rollback status. Failure reports include failure mode, rejected input, candidate targets when safe to disclose, command output, and rollback status.

## Exit Behavior

| Exit code | Meaning |
|---:|---|
| 0 | Command succeeded and all requested validations passed. |
| 2 | Input schema or policy validation failed. |
| 3 | Target resolution failed because zero or multiple matches were found. |
| 4 | Mutation occurred but validation failed and rollback was attempted. |
| 5 | Diff scope touched an unallowed path. |

## Rollback Behavior

The executor must run in a clean worktree or an isolated checkpoint. When any post-mutation validation fails, it must roll back touched files or discard the worktree before reporting failure. It must not commit or push. Git-generated diff is proof after deterministic mutation, not the planner's primary input.
