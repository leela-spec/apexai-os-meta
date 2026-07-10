Good. I now have enough data from web research plus the space files context. Let me compile the full report.

---

# CC Path vs GPT Path: Deterministic AI Patch Infrastructure

**Bottom line first:** The two paths are not genuinely different architectures — they converge on the same two-phase pattern. The CC path emphasizes external CLI tools and hook enforcement; the GPT path emphasizes a Python executor with a schema contract. The correct answer is **merge both into one minimal architecture**, taking the schema discipline from GPT path and the proven CLI tools from CC path.

---

## Part 1: Path Comparison

The CC path uses existing CLI ecosystem tools (rg, yq, remark/mdast, git) stitched together behind Claude Code `PreToolUse` hooks that hard-block direct writes. The GPT path uses a Python executor that owns all live-file reads, resolves targets from semantic anchors, and only surfaces validated diffs

**They are structurally identical in goal.** Both require: (1) a planner AI that emits semantic intent without exact old-text, (2) a deterministic resolver that reads live files and proves uniqueness, (3) a mutation stage that writes only after proof, and (4) git diff as the audit artifact. The CC path outsources resolver logic to shell tools; the GPT path internalizes it in Python. Neither is complete alone — the CC path lacks a schema contract, and the GPT path tends to reinvent Markdown parsing that already exists in remark/mdast.

---

## Part 2: Tool Ranking

|Rank|Tool/Component|Phase Role|Evidence|Impact|Resilience|Effectiveness|Token Eff.|Impl. Cost|Risk|Adopt/Trial/Reject|Rationale|
|---|---|---|---|---|---|---|---|---|---|---|---|
|1|`patch_intent.schema.json`|Phase 1 output contract|High — schema-first is standard|95|92|90|95|85|15|**ADOPT**|Forces planner AI to emit only what it can reliably produce: semantic anchors + new text|
|2|`git worktree` + `git diff` + `git apply --check`|Phase 2 proof layer|High — well-documented|92|95|95|90|80|10|**ADOPT**|Only trusted audit trail; `--check` before commit is non-negotiable|
|3|`rg` (ripgrep)|Phase 2 discovery/match-count|High — multiline `-U`, PCRE2 supported [[publish.obsidian](https://publish.obsidian.md/xybre/permalink/a66b313e-a7d7-49ba-8196-610c4b49af9f)]|88|85|88|92|90|12|**ADOPT**|Fastest way to count candidate matches and detect ambiguity before mutation|
|4|`yq --front-matter=process`|Phase 2 frontmatter ops|Good — `process` mode preserves body, risk if no `---` present [[latchkey](https://latchkey.dev/learn/command-reference/yq-front-matter)]|85|72|85|85|82|22|**ADOPT with guard**|Must pre-check for `---` delimiter before calling; fail if absent|
|5|`mdast-util-heading-range` / remark|Phase 2 section boundary resolver|Good — actively maintained via unified ecosystem [[github](https://github.com/Rokt33r/remark-collapse)]|82|80|85|75|65|30|**ADOPT**|Only reliable way to resolve H1→H2→H3 heading paths without line-number dependency|
|6|`patch_resolver.py` (custom)|Phase 2 span scoring|Medium — must be built|75|82|85|88|60|28|**ADOPT — minimal**|Orchestrates rg + mdast; keeps logic in one auditable place|
|7|Claude Code `PreToolUse` hooks|Enforcement layer|High — confirmed hard-block capability [[code.claude](https://code.claude.com/docs/en/hooks)]|90|95|85|88|72|18|**ADOPT**|Shell-enforced, not model-enforced; blocks Write/Edit/MultiEdit on protected files|
|8|`mdpatch` / markdown-patch|Phase 2 section edit backend|Low — repo exists [[github](https://github.com/coddingtonbear/markdown-patch)] but maintenance status unclear|40|55|55|60|55|55|**TRIAL only**|Use only if remark/mdast integration proves too complex; test against fixture suite first|
|9|`comby`|Phase 2 structural match|Medium — works on structured code but Markdown support is weak|45|50|45|55|60|40|**TRIAL**|Useful for code fences inside Markdown; not reliable for prose sections|
|10|`sed` / `awk` / `perl`|Phase 2 low-level mutation|High availability, zero resilience on wrong span|35|15|40|70|90|85|**REJECT as first-class**|Wrap-only inside resolver; never exposed to planner AI; no span proof|

---

## Part 3: Failure-Mode Matrix

|Test Scenario|CC Path|GPT Path|Verdict|
|---|---|---|---|
|`simple_exact_span` — correct file, no exact old text|✅ rg counts match, resolver applies|✅ resolver scores span|Both handle|
|`wrong_line_numbers` — stale by 20 lines|✅ hooks block line-based edits; rg finds by content|✅ schema forbids line numbers entirely|Both handle if schema bans line numbers|
|`duplicate_heading` — two identical headings|⚠️ rg finds 2 matches; must reject or require heading path|✅ ambiguity report emitted, pipeline halts|GPT path cleaner; CC needs explicit rg count-check|
|`nested_heading_path` — same H2 under different H1|✅ mdast heading-range with path|✅ resolver uses H1→H2 path from schema|Both handle via mdast|
|`paraphrased_anchor` — semantically close but not exact|⚠️ rg fixed-string fails; fuzzy match needed|⚠️ scoring required, threshold risk|**Both fragile** — need fuzzy-match fallback or human escalation|
|`frontmatter_update`|✅ yq `--front-matter=process` with `---` guard [[latchkey](https://latchkey.dev/learn/command-reference/yq-front-matter)]|✅ same, or custom parser|Both handle with guard|
|`table_row_update`|⚠️ no standard tool; custom row matcher needed|⚠️ same|**Tool gap** — rg + line-rewrite, fragile|
|`large_file_small_edit`|✅ rg isolates section; mdast scopes edit|✅ resolver reads only target section|Both handle|
|`multi_file_patch_pack`|✅ scope allowlist in policy.json + hooks|✅ scope allowlist in patch_policy.json|Both handle|
|`bad_ai_patch` — invalid unified diff|✅ hooks block `git apply` of AI-authored diff|✅ schema rejects unified diff as input type|Both handle if schema forbids diff input|
|`formatting_preservation`|⚠️ remark reformats on parse/serialize; must use range-only mode|⚠️ same risk|**Both fragile** — must use heading-range edit, not full reparse|
|`failed_validation_rollback`|✅ git worktree isolation; delete branch on failure|✅ same|Both handle via worktree|

**Key gaps:** paraphrased anchors and table row edits have no clean solution in either path. Both require an explicit "escalate to human" exit rather than a silent wrong write.

---

## Part 4: Recommended Final Architecture

## Minimum Viable Stack

**Phase 1 — Planner AI produces `patch_intent.yaml`:**

text

`# patch_intent.yaml — exact schema target_file: "docs/SKILL.md"           # guess only; executor verifies operation: replace_section             # replace_section | prepend_section | append_section | update_frontmatter | replace_table_row heading_path: ["Configuration", "Defaults"]   # H1 → H2 ordered path nearby_phrase: "rate_limit:"           # optional fuzzy anchor; executor may ignore if ambiguous replacement_text: |   ## Defaults  rate_limit: 100 validation:   must_contain: ["rate_limit: 100"]  must_not_reformat: true scope_token: "docs/SKILL.md"          # must match scope allowlist`

**What Phase 1 must NOT emit:** exact old_text, line numbers, hunk headers, unified diffs. The schema enforces this by not having those fields.[[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bf26939d-29f7-4641-a6f4-56b0c9f8c83e/722a954c-1b2e-4dc6-ad9e-155d81d13521/Patchplan.md?AWSAccessKeyId=ASIA2F3EMEYEWFSTMK2Q&Signature=CoKmjBbE7pHrYziGqMA4m%2FAvvEk%3D&x-amz-security-token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIG0KSfDvIX0dddeoJR7CvPhE%2B6I4cj4NFgngzVB6L2PCAiEA6nnMkt%2BfN8e2aTRgnp1zahlnOUYM2ZTVs%2FFqam6JrZEq%2FAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDAJAVu8kf1s6TpURlirQBKfhaRMXG86FiS8az33VOtRw612dgpACWjMxS2Lyq5k7kZhDfg5lOfrl%2FjKZNgDssb3IRRsUT53uqlHvrg%2BCm7AbfqREigQE9cSW6zZNn0%2BBcNfFjXTBMerZyxFewz%2B95sAISryzV1Gmilka4xvbKI1SmS0onbumCf7Mv9eaC%2BYZ1Pa4MoHLJAGqKvoB44lVv2dZVD3OqlDUcBbpwWBZ%2BTB7tajxLrPo4osOjYQYv2iQdYR7NOyDg8IGLor6MDuCV7PC%2FoBEhkzGICK3zD3ZGk3evZM7g97fuxQxaFEfZQX%2Bx0OqabAMKy1tH8vZR8g%2Fd8vmAmMLeR9iF%2FDS%2Fzz0578CpbIk3UqfX1%2BynsuugaaTCesR0%2F4ZURrON%2BJwPgHAbMiyPhr%2FSVDygU7NFSt3NCMMB6ob718K8T5JspDQr92zz5f3nOfgq31l9eRMleJfMp9vfthfjIb9p9YGJrwu4c4hKxd81QvkP%2Fy0%2B105VOGYqwwnrCLryTrrZwX7EFN3TKL49U0%2F3JyyRzXiWIliNnxwyrkkAvyE4BQfunufNRLE927WrW%2FzLv4Bf4dl%2BJvtNKQrSUouqxUdikKeyjb%2FPnXZr3%2FNCL%2FrSF8wg%2F47lFVIncIQ2BCgdE4P0Ld1VB58SxJ7f%2Fnz1py7BhR46iN%2FsLUA8OfK9gxDCGYe%2FjIUdat8lWdEIa0tVv92Gcr6mGvJ%2FsrD5jYvykFQNmCifuG3qcAOVSTA8%2Fa4Bqfhjy7dHlml8UzzSSRdq9DRnGxZNZH9HKcanxpodqL8QZpPlkbFmxYwuNm%2F0gY6mAFNIma8MAKQWDpdyOqC1qaUr5GugWJYnMaqEQUSxKoBvYuUamBz73usjvD2nTFaF1OGhPPl1GvCs%2BGtzbn0R2R4fptf7eyAe6eO7l8cXwC2FQgQrVrdcKoSXsoBv8HhmrjS9gn%2F8NdPVijZgroX9bU0cyUJpzFCaafx4L3rDH%2FEiOBnuus2I%2BEXGMCjy9es%2FEYByCFJKJVEXA%3D%3D&Expires=1783626379)]

**Phase 2 — Deterministic executor (in order):**

1. **Scope check** — `patch_policy.json` allowlist; reject unknown files immediately
    
2. **File existence** — fail if target_file not found; suggest rg search of repo
    
3. **Frontmatter ops** — `yq --front-matter=process` only; pre-check `---` present[[latchkey](https://latchkey.dev/learn/command-reference/yq-front-matter)]
    
4. **Section resolution** — `mdast-util-heading-range` with full heading path; count matches via rg; reject if count ≠ 1
    
5. **Paraphrase fallback** — if nearby_phrase supplied and unique via `rg -c`, use as secondary anchor; if count > 1, emit ambiguity report and halt
    
6. **Mutation in git worktree** — never on live branch directly
    
7. **Diff proof** — `git diff` captured to `patch_proof.diff`
    
8. **Validation** — `git apply --check`, must_contain assertions, optional py_compile/lint
    
9. **Rollback** — delete worktree on any failure; emit structured `patch_failure.json`
    

## Optional Later Additions

- comby for code-fence edits inside Markdown
    
- mdpatch as section-edit backend after fixture bakeoff
    
- rg PCRE2 multiline for table-row resolution[[stackoverflow](https://stackoverflow.com/questions/67713798/ripgrep-to-find-files-which-contain-multiple-words-possibly-on-different-lines)]
    

## Rejected

- AI-authored unified diffs as input
    
- sed/perl/awk as first-class mutation tools (wrap-only)
    
- Line numbers in any Phase 1 artifact
    
- Full-file rewrite via remark (formatting preservation violation)
    

---

## Part 5: Build Prompt for Codex/Claude Code

text

`TASK: Build deterministic patch executor. Two files only this session. FILE 1: patch_resolver.py - Read patch_intent.yaml (schema: target_file, operation, heading_path, nearby_phrase, replacement_text, validation, scope_token) - Load patch_policy.json scope allowlist; reject if target_file not in allowlist - If operation == update_frontmatter: verify file starts with '---'; run yq --front-matter=process - If operation == replace_section: use mdast-util-heading-range via subprocess node call OR pure-Python heading scanner; count rg matches for heading; reject if != 1 - If paraphrased anchor: run rg -c nearby_phrase; reject if count != 1 - Write mutation to git worktree (not live branch) - Capture git diff to patch_proof.diff - Run git apply --check on diff - Validate must_contain assertions on mutated file - On any failure: delete worktree, write patch_failure.json with reason - On success: write patch_success.json with diff summary FILE 2: patch_policy.json - scope allowlist of permitted file paths CONSTRAINTS: - No full-file rewrites - No line numbers - No AI-authored diffs as input - No sed/perl/awk direct mutation - Emit ambiguity report if rg count > 1, do not guess VALIDATION COMMANDS TO RUN AFTER BUILD: git apply --check patch_proof.diff rg -c "must_contain_string" mutated_file python3 -c "import patch_resolver; print('import OK')"`

---

## Part 6: Final Verdict

**Verdict: Merge both paths into one minimal architecture.**

The CC path and GPT path are the same two-phase design expressed in different vocabularies. The CC path's real contribution is `PreToolUse` hooks as hard enforcement and CLI tools (rg, yq, mdast) as proven resolvers. The GPT path's real contribution is the schema contract that forces Phase 1 to emit only what an LLM can reliably produce. Neither path alone is complete. The merged architecture — **strict YAML intent schema + Python orchestrator + rg/yq/mdast as resolver backends + git worktree isolation + PreToolUse hooks blocking direct writes** — satisfies every constraint: it fails safely on ambiguity, generates auditable git diff proof, does not require full-file rewrites, handles frontmatter/tables/sections distinctly, and keeps Claude/Codex token use minimal because the executor does all the reading and reasoning mechanically. The single biggest risk in both paths is the paraphrased anchor scenario and table row edits — both need an explicit "cannot resolve, escalate" exit rather than a low-confidence write.[[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bf26939d-29f7-4641-a6f4-56b0c9f8c83e/8dfe57a8-2a61-438c-8cbd-507b0f1d0879/MASTER_HANDOVER_learnings_and_rankings.md?AWSAccessKeyId=ASIA2F3EMEYEWFSTMK2Q&Signature=V%2BGuYYuDdZ1n7o%2B%2B65oDWwKeQ2o%3D&x-amz-security-token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIG0KSfDvIX0dddeoJR7CvPhE%2B6I4cj4NFgngzVB6L2PCAiEA6nnMkt%2BfN8e2aTRgnp1zahlnOUYM2ZTVs%2FFqam6JrZEq%2FAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDAJAVu8kf1s6TpURlirQBKfhaRMXG86FiS8az33VOtRw612dgpACWjMxS2Lyq5k7kZhDfg5lOfrl%2FjKZNgDssb3IRRsUT53uqlHvrg%2BCm7AbfqREigQE9cSW6zZNn0%2BBcNfFjXTBMerZyxFewz%2B95sAISryzV1Gmilka4xvbKI1SmS0onbumCf7Mv9eaC%2BYZ1Pa4MoHLJAGqKvoB44lVv2dZVD3OqlDUcBbpwWBZ%2BTB7tajxLrPo4osOjYQYv2iQdYR7NOyDg8IGLor6MDuCV7PC%2FoBEhkzGICK3zD3ZGk3evZM7g97fuxQxaFEfZQX%2Bx0OqabAMKy1tH8vZR8g%2Fd8vmAmMLeR9iF%2FDS%2Fzz0578CpbIk3UqfX1%2BynsuugaaTCesR0%2F4ZURrON%2BJwPgHAbMiyPhr%2FSVDygU7NFSt3NCMMB6ob718K8T5JspDQr92zz5f3nOfgq31l9eRMleJfMp9vfthfjIb9p9YGJrwu4c4hKxd81QvkP%2Fy0%2B105VOGYqwwnrCLryTrrZwX7EFN3TKL49U0%2F3JyyRzXiWIliNnxwyrkkAvyE4BQfunufNRLE927WrW%2FzLv4Bf4dl%2BJvtNKQrSUouqxUdikKeyjb%2FPnXZr3%2FNCL%2FrSF8wg%2F47lFVIncIQ2BCgdE4P0Ld1VB58SxJ7f%2Fnz1py7BhR46iN%2FsLUA8OfK9gxDCGYe%2FjIUdat8lWdEIa0tVv92Gcr6mGvJ%2FsrD5jYvykFQNmCifuG3qcAOVSTA8%2Fa4Bqfhjy7dHlml8UzzSSRdq9DRnGxZNZH9HKcanxpodqL8QZpPlkbFmxYwuNm%2F0gY6mAFNIma8MAKQWDpdyOqC1qaUr5GugWJYnMaqEQUSxKoBvYuUamBz73usjvD2nTFaF1OGhPPl1GvCs%2BGtzbn0R2R4fptf7eyAe6eO7l8cXwC2FQgQrVrdcKoSXsoBv8HhmrjS9gn%2F8NdPVijZgroX9bU0cyUJpzFCaafx4L3rDH%2FEiOBnuus2I%2BEXGMCjy9es%2FEYByCFJKJVEXA%3D%3D&Expires=1783626379)][[code.claude](https://code.claude.com/docs/en/hooks)][[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bf26939d-29f7-4641-a6f4-56b0c9f8c83e/a0da7961-d34c-4156-854e-525cb17b8073/AgentMode-GitNative-PatchPack-Process.okf.md?AWSAccessKeyId=ASIA2F3EMEYEWFSTMK2Q&Signature=WRUWt6vjaYVptqIlHHVtMHxIonQ%3D&x-amz-security-token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIG0KSfDvIX0dddeoJR7CvPhE%2B6I4cj4NFgngzVB6L2PCAiEA6nnMkt%2BfN8e2aTRgnp1zahlnOUYM2ZTVs%2FFqam6JrZEq%2FAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDAJAVu8kf1s6TpURlirQBKfhaRMXG86FiS8az33VOtRw612dgpACWjMxS2Lyq5k7kZhDfg5lOfrl%2FjKZNgDssb3IRRsUT53uqlHvrg%2BCm7AbfqREigQE9cSW6zZNn0%2BBcNfFjXTBMerZyxFewz%2B95sAISryzV1Gmilka4xvbKI1SmS0onbumCf7Mv9eaC%2BYZ1Pa4MoHLJAGqKvoB44lVv2dZVD3OqlDUcBbpwWBZ%2BTB7tajxLrPo4osOjYQYv2iQdYR7NOyDg8IGLor6MDuCV7PC%2FoBEhkzGICK3zD3ZGk3evZM7g97fuxQxaFEfZQX%2Bx0OqabAMKy1tH8vZR8g%2Fd8vmAmMLeR9iF%2FDS%2Fzz0578CpbIk3UqfX1%2BynsuugaaTCesR0%2F4ZURrON%2BJwPgHAbMiyPhr%2FSVDygU7NFSt3NCMMB6ob718K8T5JspDQr92zz5f3nOfgq31l9eRMleJfMp9vfthfjIb9p9YGJrwu4c4hKxd81QvkP%2Fy0%2B105VOGYqwwnrCLryTrrZwX7EFN3TKL49U0%2F3JyyRzXiWIliNnxwyrkkAvyE4BQfunufNRLE927WrW%2FzLv4Bf4dl%2BJvtNKQrSUouqxUdikKeyjb%2FPnXZr3%2FNCL%2FrSF8wg%2F47lFVIncIQ2BCgdE4P0Ld1VB58SxJ7f%2Fnz1py7BhR46iN%2FsLUA8OfK9gxDCGYe%2FjIUdat8lWdEIa0tVv92Gcr6mGvJ%2FsrD5jYvykFQNmCifuG3qcAOVSTA8%2Fa4Bqfhjy7dHlml8UzzSSRdq9DRnGxZNZH9HKcanxpodqL8QZpPlkbFmxYwuNm%2F0gY6mAFNIma8MAKQWDpdyOqC1qaUr5GugWJYnMaqEQUSxKoBvYuUamBz73usjvD2nTFaF1OGhPPl1GvCs%2BGtzbn0R2R4fptf7eyAe6eO7l8cXwC2FQgQrVrdcKoSXsoBv8HhmrjS9gn%2F8NdPVijZgroX9bU0cyUJpzFCaafx4L3rDH%2FEiOBnuus2I%2BEXGMCjy9es%2FEYByCFJKJVEXA%3D%3D&Expires=1783626379)]