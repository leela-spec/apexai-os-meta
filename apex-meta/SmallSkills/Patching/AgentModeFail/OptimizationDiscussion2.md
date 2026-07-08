## Verdict

Your concern is valid in general. **Blind `git apply` is not a sufficient Codex strategy** when patches were AI-generated or copied through chat. But in this specific package, the pre-check is unusually strong:

- all nine patch files are syntactically parseable unified diffs;
- each patch touches exactly one expected target file;
- every patch has a Git `index <old>..<new>` line;
- every `old` blob prefix matches the current live `main` blob SHA for the target file.

That last point is important: it means the patches were generated against the exact live file versions I fetched from `leela-spec/apexai-os-meta/main`, not against a stale local copy. I verified the live SHAs for all nine target files from GitHub.

## Web validation

`git apply` is viable **only as a first deterministic path**, not as the whole recovery plan. Git documents `git apply --check` as the way to test applicability without changing the worktree, and `--3way` as a fallback when the patch records blob identities and those blobs exist locally. Git also documents `--reject`, but explicitly says normal `git apply` is atomic by default and `--reject` creates partial application plus `.rej` files, so I would not use `--reject` in the final worktree. Git also provides whitespace and recount options for common AI/copy-paste patch defects.

For Codex specifically, OpenAI describes Codex as able to read/edit files and run test harnesses, linters, and type checkers in a repo sandbox, but OpenAI also says users should manually review and validate agent-generated code before integration. So the right model is: **Codex runs a deterministic script; Codex does not improvise patch edits unless every deterministic path fails.**

## Pre-check summary

|Patch|Target|Old blob matches live `main`?|Risk|
|---|---|---|---|
|`001-wiki-page-templates.patch`|`wiki-page-templates.md`|yes|medium, largest patch|
|`002-ingest-analysis-template.patch`|`ingest-analysis-template.md`|yes|low|
|`003-kb-contract.patch`|`kb-contract.md`|yes|low|
|`004-ingest-query-lint-audit-rules.patch`|`ingest-query-lint-audit-rules.md`|yes|low|
|`005-acceptance-tests.patch`|`acceptance-tests.md`|yes|low|
|`006-skill.patch`|`SKILL.md`|yes|low|
|`007-lifecycle-state-machine.patch`|`lifecycle-state-machine.md`|yes|low|
|`008-knowledge-promotion-rules.patch`|`knowledge-promotion-rules.md`|yes|very low|
|`009-kb-schema-template.patch`|`kb-schema-template.md`|yes|low|