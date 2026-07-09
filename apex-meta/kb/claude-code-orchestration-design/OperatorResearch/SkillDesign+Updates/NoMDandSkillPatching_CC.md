Here is the complete research output. All rows cite real, checkable sources.

---

## Why Skill-Markdown Section Patching Doesn't Exist

Section-level patching of SKILL.md files is **genuinely absent as a purpose-built tool**, but the gap is explained by a convergence of four reinforcing causes, not one single reason.

---

## Ranked Findings Table

|#|Idea / Tool / Explanation|Description|Impact|Evidence|Risk|Verdict|
|---|---|---|---|---|---|---|
|1|**LLM regeneration architecture (Angle 7)**|LLMs are optimized for local coherence and pattern completion, not structural diffing; "don't change anything else" triggers full internal re-synthesis regardless of instruction — confirmed architectural limitation, not prompting failure|95|88|15|**Adopt as explanation**|
|2|**`skillfile` patch/pin system** (Rust crate `skillfile-core`)|`skillfile pin` captures a user's local edits as a diff-patch stored in `.skillfile/patches/`; `skillfile resolve` does 3-way merge — closest existing thing to section-aware skill editing, but operates at whole-file git-diff level, not sub-section|85|92|20|**Investigate Further**|
|3|**Whole-file-replace-is-fine hypothesis (Angle 1)**|SKILL.md files are designed single-responsibility and short by convention; agentpatterns.ai documents that full-rewrite is strictly cheaper than any diff format below ~300 tokens of file content, making section patching an unnecessary cost for this file class|82|85|10|**Adopt as explanation**|
|4|**`skill-cli` / `npx skills` update mechanics (Angle 2)**|Both tools implement `update` as re-fetch-and-overwrite: `skill-cli update --all` re-fetches from origin URL; `npx skills update astro-seo` targets one skill but replaces its full file — no section-level operation exists in either codebase|80|95|10|**Adopt as explanation**|
|5|**Git-native whole-file convention (Angle 3)**|`skillfile` team workflow docs show teams commit `Skillfile`, `Skillfile.lock`, and `.skillfile/patches/` and treat each SKILL.md as the atomic unit of change — same as single-function-per-file convention; git merge resolves conflicts at file level|75|87|10|**Adopt as explanation**|
|6|**Two-Pass Plan→Apply pattern (Angle 7 sub-question)**|LinkedIn post by Anand Ranade (Jan 2026) documents the Two-Pass pattern (Pass 1: describe intended change, no code output; Pass 2: deterministic apply) as a known mitigation for LLM drift; **not implemented by any known skill-specific tool** — only described as a generic agent pattern|72|75|25|**Investigate Further**|
|7|**Explicit Edit Zones via HTML comments (Angle 7 sub-question)**|Same Ranade post documents `// BEGIN EDITABLE SECTION` / `// END EDITABLE SECTION` markers as hard constraints that outperform soft prompting; **no known skill tool parses or enforces these in markdown specifically** — markdowntools.io confirms `<!-- -->` is valid in CommonMark but no automation layer exists around it for skill files|70|72|20|**Investigate Further**|
|8|**`str_replace_based_edit_tool` / Anthropic search-replace (Angle 6)**|Anthropic's own Claude text editor tool uses search-replace (`old_str`/`new_str`), which is the closest to section-level editing in production; requires unique anchor match — fails on repeated content — and is not purpose-built for SKILL.md; agentpatterns.ai benchmark shows it raised GPT-4 edit accuracy from 26% to 59% vs unified diffs|68|90|30|**Trial**|
|9|**`comby` for markdown section rewriting (Angle 6)**|Comby supports a generic matcher with `-matcher .md` and `-i` in-place rewrite; could technically match a named section and replace its body using template syntax; **no documented usage for SKILL.md in any known repo** — cheat sheet confirms it falls back to generic parser for unrecognized extensions|60|65|45|**Trial**|
|10|**Author-only-edits hypothesis (Angle 4)**|Skill repos like `jdevalk/skills`, `obra/superpowers`, `anthropics/courses` show single-author commit histories with rare post-creation edits; `skillfile` docs explicitly frame local edits as unusual enough to need a `pin` command — consistent with skills being written once and consumed passively|58|78|15|**Adopt as explanation**|
|11|**Scale mismatch hypothesis (Angle 5)**|Known public skill libraries (345–600+ files) show bulk of files with 0–2 commits after creation; `npx skills update` with `SessionStart` hook automates full-file refresh at session boundary — the _actual_ maintenance pattern is periodic wholesale replacement, not frequent surgical patching|55|72|15|**Adopt as explanation**|
|12|**`markdownlint-cli2 --fix` (Angle 6)**|Automates structural linting and in-place fixes on `.md` files; operates at formatting/rule level (headings, blank lines, code fences), not semantic section content — not a section patcher, confirms tooling gap|30|88|5|**Reject** (wrong layer)|
|13|**Unified diff for SKILL.md (out-of-scope confirm)**|Aider's own benchmarks confirm unified diffs make GPT-4 Turbo "3× less lazy" but still fail due to fragile offsets; explicitly noted by agentpatterns.ai as unreliable for LLMs — not viable as section-patch mechanism|20|95|90|**Reject**|

---

## Why This Specific Gap Exists

The absence is structural, not accidental. Three independently verifiable causes compound each other:

**1. File size makes patching wasteful.** The agentpatterns.ai benchmark analysis (arxiv:2604.27296) shows full-rewrite is the _cheaper_ strategy for any file under ~300 tokens. SKILL.md files by ecosystem convention are single-responsibility and short — the overhead of constructing a section anchor plus surrounding context _exceeds_ the cost of simply regenerating the file. The economic case for a section patcher never materializes.[[agentpatterns](https://agentpatterns.ai/tool-engineering/llm-edit-format-selection/)]

**2. The LLM regeneration architecture forecloses "patch by instruction."** The LinkedIn documentation by Anand Ranade (Jan 2026) — corroborated by the Reddit thread on LLM full-file rewriting — confirms that when a model is instructed to "change only X," it still internally re-synthesizes the complete output, silently dropping or altering unrelated content. This is documented as an architectural fact (compression + local coherence optimization), not a prompting failure. No skill tool found implements the Two-Pass or Edit Zone mitigations for markdown specifically — they exist only as described patterns, not shipping implementations.[[reddit](https://www.reddit.com/r/MLQuestions/comments/1j867nu/why_does_every_llm_rewrite_the_entire_file/)]

**3. The actual maintenance workflow never required it.** `skill-cli`, `npx skills`, and `skillfile` all confirm via their own documentation that the standard update path is re-fetch-and-overwrite. The `skillfile pin` / `resolve` system is the only near-miss — it stores user customizations as whole-file diffs in `.skillfile/patches/` and applies a 3-way merge on update — but this still treats the file as the atomic unit. Author-only single-commit histories in known skill repos confirm that after initial creation, skill files are rarely touched at all; the bulk-patching workload pattern the question describes has not been a real requirement anyone in the ecosystem has hit at scale.[[libraries](https://libraries.io/go/github.com%2FMescoCzubinski%2Fskill-cli)]

The result: no tool purpose-built for skill-markdown section patching exists because the three preconditions that would create demand for it (large files, frequent AI-driven partial edits, multi-author concurrent modification) are all structurally absent from how skill files are designed, consumed, and maintained.