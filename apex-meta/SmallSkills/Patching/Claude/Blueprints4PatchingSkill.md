## Research Result: No Exact Match Found — Here's What Exists

**No publicly available, complete skill package exists that fully satisfies all five criteria simultaneously** — particularly the combination of PreToolUse/PostToolUse hook enforcement + plan/validate/apply as three separate scripts + zero-LLM apply step. Here is a precise breakdown of the landscape.

---

## Closest Candidate: `@tylerburleigh/claude-sdd-toolkit`

**Repo/Source:** [claude-plugins.dev/skills/@tylerburleigh/claude-sdd-toolkit](https://claude-plugins.dev/skills/@tylerburleigh/claude-sdd-toolkit/sdd-modify)[[claude-plugins](https://claude-plugins.dev/skills/@tylerburleigh/claude-sdd-toolkit/sdd-modify)]

|Criterion|Status|
|---|---|
|Plan step (LLM → JSON only)|✅ `sdd-plan` produces structured JSON spec, LLM never writes target file|
|Validate step (zero-LLM)|✅ `sdd validate-modifications` — pure CLI, schema check, no tokens consumed|
|Apply step (zero-LLM)|✅ `sdd apply-modifications` — deterministic CLI, no LLM at write time|
|Rollback / backup|✅ Auto-backup before every apply; transaction rollback if post-apply validation fails|
|Hook enforcement (PreToolUse/PostToolUse)|❌ **Partially** — SKILL.md instructions govern sequence; hooks embedded in `/plan_w_team` command frontmatter, not global PreToolUse guards|
|Markdown-specific|❌ Spec-file (JSON) domain, not general markdown/config|

The toolkit's `sdd-modify` SKILL.md explicitly defines the pattern: `Review → Parse → Preview → Apply → Validate → Re-review`. Rollback is fully deterministic — if post-apply validation fails, all changes are rolled back and the backup is preserved. **Token cost: zero at validate/apply time** — only `sdd parse-review` may use LLM to extract modifications from a review report.[[claude-plugins](https://claude-plugins.dev/skills/@tylerburleigh/claude-sdd-toolkit/sdd-modify)]

**Gap:** Sequence enforcement is instruction-based (SKILL.md prohibits chaining commands), not enforced via `PreToolUse` hooks that would block the LLM from skipping to apply directly.[[claude-plugins](https://claude-plugins.dev/skills/@tylerburleigh/claude-sdd-toolkit/sdd-modify)]

---

## Second Candidate: `disler/claude-code-hooks-mastery`

**Repo:** [github.com/disler/claude-code-hooks-mastery](https://github.com/disler/claude-code-hooks-mastery) — Last commit: **Feb 1, 2026**, 3.7k stars[[github](https://github.com/disler/claude-code-hooks-mastery)]

|Criterion|Status|
|---|---|
|Plan/validate/apply separation|❌ No plan.json pattern; focuses on hook lifecycle demo|
|PreToolUse/PostToolUse enforcement|✅ Full implementation with `decision: "block"` JSON output, exit code 2 blocking [[github](https://github.com/disler/claude-code-hooks-mastery)]|
|Zero-LLM validate/apply|Partial — validators (Ruff, Ty) are zero-LLM, but no plan→apply pipeline|
|Rollback|❌ Not implemented|
|Markdown/config file specific|❌ Python code quality focus|

This repo is the most complete **hook enforcement reference** — PreToolUse blocking patterns are production-grade — but it has no plan/validate/apply pipeline for files.[[github](https://github.com/disler/claude-code-hooks-mastery)]

---

## Pattern Gap Analysis

The specific combination you require — **plan.json produced by LLM → validated by deterministic script → applied by deterministic script → enforced via PreToolUse/PostToolUse hooks** — does not exist as a packaged skill. What exists:

- **`sdd-toolkit`**: Has the plan→validate→apply→rollback pipeline, missing hook-level enforcement
    
- **`claude-code-hooks-mastery`**: Has the hook enforcement primitives, missing the pipeline
    
- **`alirezarezvani/claude-skills`** (345 skills, [github.com/alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)): No plan-validate-apply pattern found in search results[[github](https://github.com/alirezarezvani/claude-skills)]
    
- **npm/pip search**: No package matching "claude skill plan validate apply" exists
    

---

## Build Recommendation

Given your existing files, the fastest path is composing from two existing primitives:[[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bf26939d-29f7-4641-a6f4-56b0c9f8c83e/722a954c-1b2e-4dc6-ad9e-155d81d13521/Patchplan.md?AWSAccessKeyId=ASIA2F3EMEYE5OGZYLG5&Signature=saKWHUOtYvlvUNUJ%2Fr%2FYmDmdtok%3D&x-amz-security-token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQC9wqey7M2HYZySh8S%2FSGyTgUCccvGNNGNSYonttYgmOAIgQ3o2FgF5Ee5YxA7L3FvRbCuyRDYVTGDadIjBnPRL8jMq%2FAQIoP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDNYBzq4Ni0QrtbDM3SrQBD5L7NwnIuD4kUfA7FoOn6LcPe3yyPLgWcW4XykoJTOBF14RU0fr4WfEkZfB%2B6LseV7GkZzz7%2FSDnzc685tv0JmpmJ2Aptu3RuEtaojqqr89Kc95g0U286mjDSXBI6Pi8efZkQbaJ4e%2BWGawQ49%2BM0NmoQYJH%2FZggXVtr5VdkCALr3KhZxsNSeDeSHUAPHSj7pmN1zTi7UfT3tnKpcmAIkLLpkbZqAFeXZft1QrPHQ2KhUcQQvyV7MidGFocIL94OJ5qCLNy%2Fxs0wcNxNdBDr1fYC2XAzieIQQ8awJS28uCbZopWrLmWuS5tMEc14WluzFfb%2FlcYAI%2BjZu%2F3TKWTIAvPQTBRCaZgDktDg1XHw3c1%2BYN1n%2BxllN7CGxm11HB7a6ozZ2rQUCNg73tjfCFIBre65s%2BIHUu37gSXjNpKgGBvQ0tHV3ZBN3W06Vc8yldV%2Bq%2FisGQn1uIHMLvdLZPYjVs%2Brqvkt%2FoR6Stn53HAlCC77wwEJHPhKHSJV7pHCbYUu15q4JWJb5f04dWQjp0xFICs6zUqdgj4OouOBQJFFPyUctFv4bqisRoJJh1aY4%2Fpp6sUu%2FdL0%2Fx1pZ%2BFrPm64xD%2BFvl6agPtO5zxt6SyrGwD%2BbGUk7K23wfGgyvJd17%2FSymSpe46uDtW5kRIpInRHa2Pq9VABUFKTje0w3foVbHASXVt%2FZzFNpMOHc4QnCiTbuFP03zcB0QIJ1iT9rZ%2Fkq9ROKtTVfie5tgpE5LKI47laDUoE95x%2FzEq%2FyjQae6ynCwB1xULargAEqABlI7VeokwxfG%2B0gY6mAF6aX8uA6EzuS%2BKaEzag2zv0gIlR7kXRd8xjz7fK2UnOwhJQhLT%2Bb1Auc%2FnnoIZWbNNXxEA1fgkLQy%2BxRIkuAPQ6%2Bg93IQMPNjwkcOA88JKweYVSDViJCw%2B2yHYS0m8HKWY8iaytSP1oFsgS%2FkDujL%2FnriMgmRAA0BTgDB2Y%2FyYCKzt88FKK%2FGISnXHnWVQeMY5jDLmZwiqVQ%3D%3D&Expires=1783613080)]

1. **Copy hook enforcement patterns** from `disler/claude-code-hooks-mastery` (`.claude/hooks/pre_tool_use.py` with `decision: "block"`) — use PreToolUse to block any `Write`/`Edit` tool call unless a validated `plan.json` exists in a sentinel path
    
2. **Adopt `sdd-toolkit`'s** `apply-modifications` + backup/rollback logic as the deterministic apply script
    
3. Wire them: PreToolUse checks for `plan.validated` flag → if absent, blocks and instructs LLM to run validate script first
    

This assembly requires ~3 files: `pre_tool_use.py` (gate), `validate_plan.py` (schema check), `apply_plan.py` (write step). None of the existing packages ship all three wired together for markdown/config targets.