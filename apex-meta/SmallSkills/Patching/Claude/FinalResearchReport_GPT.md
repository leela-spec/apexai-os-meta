---

okf_schema: "apex.markdown_patching.research_verification.v1"  
status: "research_for_finalization_not_final_process"  
created_at: "2026-07-09"  
scope:  
primary_question: "Can the current deterministic Markdown patching baseline be verified, simplified, replaced, or improved?"  
baseline_checked:  
thesis: "AI should not author exact patches or exact search strings; deterministic executor should select live spans, replace once, validate, diff, then optionally commit/push."  
internal_support:  
- "Internal Patch Process Analysis explicitly rejects AI-authored exact patches/search strings and assigns AI to intent/location while tools perform exact file operations."  
- "Internal redesign recommends live span extraction, exact once-only replacement, git diff proof, and deterministic validation."  
- "Existing md-patcher skill still centers unified diff hunks, `patch --fuzz=3`, and diff output restrictions, which is safer than full rewrites but weaker than live-span execution."  
web_search_result:  
complete_existing_solution_found: false  
major_correction: "A real Markdown-specific candidate exists: coddingtonbear/markdown-patch / mdpatch. It can likely replace or seed markdown-section-replacer, but not the complete plan/validate/apply/rollback/hook architecture."

source_ledger:

- source_name: "Claude Code official hooks reference"  
    url_or_repo: "code.claude.com/docs/en/hooks"  
    type: "official_docs"  
    freshness: "crawled_today"  
    evidence_summary: "Documents hook lifecycle, PreToolUse, PostToolUse, PostToolBatch, Stop, FileChanged, decision control, exit-code behavior, JSON output, and security considerations."  
    relevance: "High for enforcement layer."  
    copyable_parts:
    
    - "Use PreToolUse to block Write/Edit/MultiEdit/Bash before execution."
        
    - "Use PostToolUse/FileChanged/Stop to detect drift after execution."  
        risks:
        
    - "Hooks are enforcement surfaces, not a full patch executor."
        
    - "Hook scripts themselves become privileged code."  
        citation: "([Claude](https://code.claude.com/docs/en/hooks?utm_source=chatgpt.com "Hooks reference - Claude Code Docs"))"
        
- source_name: "Claude Code hooks guide"  
    url_or_repo: "code.claude.com/docs/en/hooks-guide"  
    type: "official_docs"  
    freshness: "crawled_today"  
    evidence_summary: "States hooks give deterministic control over Claude Code behavior and can enforce project rules or automate repeated actions."  
    relevance: "High; confirms hooks are intended for deterministic guardrails."  
    copyable_parts:
    
    - "Rule enforcement via hooks."
        
    - "Automation of repetitive validation."  
        risks:
        
    - "Prompt/agent hooks reintroduce LLM judgment; deterministic shell hooks should be preferred."  
        citation: "([Claude](https://code.claude.com/docs/en/hooks-guide?utm_source=chatgpt.com "Automate actions with hooks - Claude Code Docs"))"
        
- source_name: "coddingtonbear/markdown-patch"  
    url_or_repo: "github.com/coddingtonbear/markdown-patch"  
    type: "maintained_repo_cli_library"  
    freshness: "repo crawled 2 weeks ago; project appears active enough for investigation"  
    evidence_summary: "Provides targeted, structure-aware Markdown edits using headings, block references, and frontmatter; available as CLI `mdpatch` and TypeScript/JavaScript library."  
    relevance: "Very high; closest external replacement for custom markdown-section-replacer."  
    copyable_parts:
    
    - "Heading-aware append/prepend/replace."
        
    - "Block-reference targeting."
        
    - "Frontmatter replacement instruction model."  
        risks:
        
    - "Does not by itself enforce plan approval, no-agent-write, git scope validation, rollback, or Claude Code hooks."
        
    - "Dependency on Node/TS ecosystem."  
        citation: "([GitHub](https://github.com/coddingtonbear/markdown-patch?utm_source=chatgpt.com "GitHub - coddingtonbear/markdown-patch: Make predictable, controllable ..."))"
        
- source_name: "tylerburleigh/claude-sdd-toolkit + sdd-modify"  
    url_or_repo: "github.com/tylerburleigh/claude-sdd-toolkit / SkillsMP sdd-modify"  
    type: "Claude skill/spec-workflow"  
    freshness: "repo crawled yesterday; skill listing crawled last week"  
    evidence_summary: "Provides spec-driven development with machine-readable JSON specs, atomic tasks, progress tracking, verification; sdd-modify claims safety checks, validation, and rollback for spec modifications."  
    relevance: "Medium-high; useful architecture reference for plan/spec management, not a direct Markdown patch executor."  
    copyable_parts:
    
    - "Machine-readable JSON spec format."
        
    - "Plan-first workflow."
        
    - "Rollback concept."  
        risks:
        
    - "Domain is spec document lifecycle, not general Markdown/config patching."
        
    - "No evidence it blocks Write/Edit/MultiEdit or owns all file mutation."  
        citation: "([GitHub](https://github.com/tylerburleigh/claude-sdd-toolkit?utm_source=chatgpt.com "GitHub - tylerburleigh/claude-sdd-toolkit: Development tools and ..."))"
        
- source_name: "disler/claude-code-hooks-mastery"  
    url_or_repo: "github.com/disler/claude-code-hooks-mastery"  
    type: "hook_examples_repo"  
    freshness: "repo crawled today; last commit approx 5 months ago"  
    evidence_summary: "Large example repo for Claude Code hooks, deterministic/non-deterministic control, subagents, and validation patterns."  
    relevance: "Medium-high for hook examples; not a patching package."  
    copyable_parts:
    
    - "Hook layout patterns."
        
    - "Validation hook examples."  
        risks:
        
    - "Do not copy wholesale; includes non-deterministic/agent orchestration patterns that can add cost and complexity."  
        citation: "([GitHub](https://github.com/disler/claude-code-hooks-mastery?utm_source=chatgpt.com "disler/claude-code-hooks-mastery - GitHub"))"
        
- source_name: "alirezarezvani/claude-skills"  
    url_or_repo: "github.com/alirezarezvani/claude-skills"  
    type: "large_skill_collection"  
    freshness: "repo crawled today; last commit 3 days ago"  
    evidence_summary: "Large collection of Claude Code skills/plugins across many domains."  
    relevance: "Low-medium; confirms broad skill ecosystem but did not surface a complete deterministic Markdown patch executor."  
    copyable_parts:
    
    - "Skill packaging conventions only after security review."  
        risks:
        
    - "Supply-chain and prompt-injection risk; high surface area; many unrelated skills."  
        citation: "([GitHub](https://github.com/alirezarezvani/claude-skills?utm_source=chatgpt.com "GitHub - alirezarezvani/claude-skills: 345 Claude Code skills & agent ..."))"
        
- source_name: "Anthropic public skills repo"  
    url_or_repo: "github.com/anthropics/skills"  
    type: "official_examples_repo"  
    freshness: "crawled today"  
    evidence_summary: "Official public repository demonstrating Claude skills across creative, technical, and enterprise workflows."  
    relevance: "Medium for packaging standards; low for direct patching."  
    copyable_parts:
    
    - "Skill structure and progressive-disclosure examples."  
        risks:
        
    - "Examples, not a complete deterministic patching solution."  
        citation: "([GitHub](https://github.com/anthropics/skills?utm_source=chatgpt.com "GitHub - anthropics/skills: Public repository for Agent Skills"))"
        
- source_name: "yq front matter docs"  
    url_or_repo: "mikefarah.gitbook.io/yq/usage/front-matter"  
    type: "official_docs"  
    freshness: "crawled 5 days ago"  
    evidence_summary: "Documents `yq --front-matter/-f`; supports processing Markdown files with YAML frontmatter and shows batch update via `find ... yq --front-matter=process`."  
    relevance: "Very high for frontmatter-only patching."  
    copyable_parts:
    
    - "Use yq for frontmatter-only metadata changes."
        
    - "Batch metadata edits without loading prose into LLM."  
        risks:
        
    - "Only processes first passed file for frontmatter; multi-file operation must loop."
        
    - "Not sufficient for prose section replacement."  
        citation: "([mikefarah.gitbook.io](https://mikefarah.gitbook.io/yq/usage/front-matter?utm_source=chatgpt.com "Front Matter | yq - GitBook"))"
        
- source_name: "dasel"  
    url_or_repo: "github.com/TomWright/dasel"  
    type: "maintained_cli_library"  
    freshness: "repo crawled yesterday; recent commits within weeks"  
    evidence_summary: "CLI/library for querying, modifying, and transforming JSON, YAML, TOML, XML, CSV, KDL with consistent selector syntax."  
    relevance: "Medium for structured config files; lower for Markdown frontmatter unless paired with extraction wrapper."  
    copyable_parts:
    
    - "Config-file patching for non-Markdown structured files."  
        risks:
        
    - "No native Markdown frontmatter boundary handling found in searched result."  
        citation: "([GitHub](https://github.com/TomWright/dasel?utm_source=chatgpt.com "GitHub - TomWright/dasel: Unified querying, transformation, and ..."))"
        
- source_name: "python-frontmatter"  
    url_or_repo: "github.com/eyeseast/python-frontmatter / PyPI"  
    type: "Python_library"  
    freshness: "PyPI release May 20 2026; repo crawled 2 days ago"  
    evidence_summary: "Loads and parses text files with YAML/JSON/TOML frontmatter; maintained Python option for custom frontmatter parser/writer."  
    relevance: "High if the final executor is Python stdlib-plus-few-deps rather than shell-only."  
    copyable_parts:
    
    - "Frontmatter parser/writer inside custom executor."  
        risks:
        
    - "Adds Python dependency; line formatting/stability must be tested against repo conventions."  
        citation: "([PyPI](https://pypi.org/project/python-frontmatter/?utm_source=chatgpt.com "python-frontmatter · PyPI"))"
        
- source_name: "gray-matter / @11ty/gray-matter"  
    url_or_repo: "npm gray-matter / @11ty/gray-matter"  
    type: "Node_library"  
    freshness: "npm crawled last month/week"  
    evidence_summary: "Parses YAML frontmatter by default, supports YAML/JSON/TOML and custom delimiters; used by many static-site/documentation tools."  
    relevance: "Medium-high if executor is Node/TS."  
    copyable_parts:
    
    - "Frontmatter parsing/stringifying."  
        risks:
        
    - "Node dependency; not enough alone for scoped patch enforcement."  
        citation: "([npm](https://www.npmjs.com/package/%4011ty/gray-matter?utm_source=chatgpt.com "@11ty/gray-matter - npm"))"
        
- source_name: "remark / unified / remark-cli"  
    url_or_repo: "remarkjs/remark, unifiedjs.com"  
    type: "Markdown_AST_ecosystem"  
    freshness: "crawled within days"  
    evidence_summary: "Remark is a Markdown processor using ASTs; remark-cli can process Markdown from CLI and plugin ecosystem supports AST-based inspection/transformation."  
    relevance: "High for robust Markdown parsing; medium for simple patching because custom plugin/script likely needed."  
    copyable_parts:
    
    - "AST parse/transform/stringify."
        
    - "Lint/format pipeline."  
        risks:
        
    - "Stringification can reformat entire files unless carefully constrained."
        
    - "Higher setup cost than mdpatch."  
        citation: "([GitHub](https://github.com/remarkjs/remark?utm_source=chatgpt.com "GitHub - remarkjs/remark: markdown processor powered by plugins part of ..."))"
        
- source_name: "markdown-it-front-matter"  
    url_or_repo: "github.com/ParkSB/markdown-it-front-matter / npm"  
    type: "Markdown_parser_plugin"  
    freshness: "crawled within 2 days/month"  
    evidence_summary: "markdown-it plugin detects frontmatter fenced block and passes content to a callback; parsing/rendering utility, not patch executor."  
    relevance: "Low-medium; useful parser component only."  
    copyable_parts:
    
    - "Frontmatter detection rules."  
        risks:
        
    - "Bring-your-own frontmatter parser; not a mutation workflow."  
        citation: "([GitHub](https://github.com/ParkSB/markdown-it-front-matter?utm_source=chatgpt.com "parksb/markdown-it-front-matter - GitHub"))"
        
- source_name: "Comby"  
    url_or_repo: "comby.dev / comby-tools/comby"  
    type: "structural_search_replace_cli"  
    freshness: "crawled within days"  
    evidence_summary: "Structural search/replace for many languages; avoids regex pitfalls for code-like structures and supports interactive review."  
    relevance: "Medium; useful for code/config structural edits, not ideal as primary Markdown heading-section tool."  
    copyable_parts:
    
    - "Structural search/replace for repeated code-like Markdown snippets."  
        risks:
        
    - "Markdown prose has weak syntactic structure; can still be ambiguous."
        
    - "Less direct than mdpatch/AST heading boundaries for Markdown."  
        citation: "([comby.dev](https://comby.dev/?utm_source=chatgpt.com "Comby · Structural code search and replace for ~every language."))"
        
- source_name: "Git apply docs"  
    url_or_repo: "git-scm.com/docs/git-apply"  
    type: "official_docs"  
    freshness: "crawled today"  
    evidence_summary: "Documents unified diff expectations, context matching, and safety behavior around applying patches."  
    relevance: "High for patch-pack validation and proof artifacts."  
    copyable_parts:
    
    - "`git apply --check` before write."
        
    - "Context line requirements."  
        risks:
        
    - "Validates hunk applicability, not semantic correctness."  
        citation: "([Git](https://git-scm.com/docs/git-apply?utm_source=chatgpt.com "Git - git-apply Documentation"))"
        
- source_name: "ripgrep"  
    url_or_repo: "github.com/BurntSushi/ripgrep"  
    type: "search_cli"  
    freshness: "repo crawled today; recent commits"  
    evidence_summary: "Fast recursive regex search, respects gitignore by default, cross-platform binaries."  
    relevance: "High as location layer; not a mutator."  
    copyable_parts:
    
    - "Candidate target discovery."
        
    - "Match count validation."  
        risks:
        
    - "Regex search can be noisy; should not be the final selection mechanism for complex edits."  
        citation: "([GitHub](https://github.com/BurntSushi/ripgrep?utm_source=chatgpt.com "GitHub - BurntSushi/ripgrep: ripgrep recursively searches directories ..."))"
        
- source_name: "markdownlint-cli / pre-commit"  
    url_or_repo: "markdownlint/markdownlint, markdownlint-cli"  
    type: "validation_cli"  
    freshness: "crawled within days/weeks"  
    evidence_summary: "Markdown linting can be integrated with pre-commit; markdownlint-cli supports globs."  
    relevance: "Medium; style validation, not patch correctness."  
    copyable_parts:
    
    - "Pre-commit validation gate."  
        risks:
        
    - "May create noise if style rules fight existing corpus."  
        citation: "([DeepWiki](https://deepwiki.com/markdownlint/markdownlint/2.3-pre-commit-hook-integration?utm_source=chatgpt.com "Pre-commit Hook Integration | markdownlint/markdownlint | DeepWiki"))"
        
- source_name: "agent skill security research"  
    url_or_repo: "arXiv skill security papers"  
    type: "security_research"  
    freshness: "2025-2026"  
    evidence_summary: "Recent papers identify realistic risks in third-party agent skills, including malicious skills, prompt injection, abandoned repo hijacking, and difficulty detecting code+instruction attacks."  
    relevance: "High for copy/no-copy decision."  
    copyable_parts:
    
    - "Security review requirement before copying skills/hooks."  
        risks:
        
    - "Confirms third-party skill reuse is a supply-chain risk."  
        citation: "([arXiv](https://arxiv.org/abs/2606.07131?utm_source=chatgpt.com "MalSkillBench: A Runtime-Verified Benchmark of Malicious Agent Skills"))"
        

candidate_tools_ranked:

- rank: 1  
    name: "custom no-agent-write executor: live span extraction + replace_once + git diff proof"  
    category: "custom_executor_architecture"  
    evd: 88  
    imp: 96  
    rsk: 18  
    cost: 28  
    best_use_case: "Default architecture for reliable Markdown/code/config patching where AI should not mutate files directly."  
    not_for: "Purely manual one-line human edits."  
    copy_or_build_decision: "Build minimal custom executor; copy internal replace_once concept and stub_repair_toolkit validation patterns."  
    evidence:
    
    - "Internal baseline already defines exact live-span extraction and replacement as the corrected model."
        
    - "Internal helper concept refuses unless old span appears exactly once."
        
- rank: 2  
    name: "markdown-patch / mdpatch"  
    category: "Markdown_structure_aware_CLI_library"  
    evd: 76  
    imp: 88  
    rsk: 28  
    cost: 32  
    best_use_case: "Heading/block/frontmatter-aware Markdown section edits."  
    not_for: "Whole process enforcement, rollback, hook policy, commit/push finalization."  
    copy_or_build_decision: "Evaluate as replacement for markdown-section-replacer; wrap inside executor rather than let agent call it freely."  
    evidence: "Targets headings, block references, and frontmatter via CLI/library. ([GitHub](https://github.com/coddingtonbear/markdown-patch?utm_source=chatgpt.com "GitHub - coddingtonbear/markdown-patch: Make predictable, controllable ..."))"
    
- rank: 3  
    name: "yq --front-matter=process"  
    category: "frontmatter_patcher"  
    evd: 92  
    imp: 84  
    rsk: 20  
    cost: 16  
    best_use_case: "Metadata-only changes across many Markdown files."  
    not_for: "Body prose, heading section replacement, custom order-preserving formatting guarantees."  
    copy_or_build_decision: "Use directly for simple frontmatter changes; wrap in loop and git diff validation."  
    evidence: "Official docs support YAML frontmatter processing and multi-file loops. ([mikefarah.gitbook.io](https://mikefarah.gitbook.io/yq/usage/front-matter?utm_source=chatgpt.com "Front Matter | yq - GitBook"))"
    
- rank: 4  
    name: "git worktree + git diff generated patches + git apply --check"  
    category: "patch_pack_validation"  
    evd: 94  
    imp: 82  
    rsk: 18  
    cost: 24  
    best_use_case: "Proof artifact generation and deterministic patch-pack validation."  
    not_for: "Selecting semantic edit spans."  
    copy_or_build_decision: "Keep; patch as proof artifact, not AI-authored artifact."  
    evidence: "Git docs define context matching and apply behavior; internal process uses local git operations as deterministic gates. ([Git](https://git-scm.com/docs/git-apply?utm_source=chatgpt.com "Git - git-apply Documentation")) "
    
- rank: 5  
    name: "ripgrep"  
    category: "location_layer"  
    evd: 95  
    imp: 78  
    rsk: 22  
    cost: 10  
    best_use_case: "Fast candidate discovery and match-count checks."  
    not_for: "Final mutation or semantic replacement."  
    copy_or_build_decision: "Use directly."  
    evidence: "Fast recursive search, gitignore-aware, cross-platform. ([GitHub](https://github.com/BurntSushi/ripgrep?utm_source=chatgpt.com "GitHub - BurntSushi/ripgrep: ripgrep recursively searches directories ..."))"
    
- rank: 6  
    name: "python-frontmatter"  
    category: "frontmatter_parser_library"  
    evd: 82  
    imp: 74  
    rsk: 30  
    cost: 34  
    best_use_case: "Python executor that needs parse/write frontmatter safely."  
    not_for: "Zero-dependency shell-only flow."  
    copy_or_build_decision: "Use only if yq formatting/edge cases are insufficient."  
    evidence: "Maintained Python library released May 2026; supports YAML/JSON/TOML frontmatter. ([PyPI](https://pypi.org/project/python-frontmatter/?utm_source=chatgpt.com "python-frontmatter · PyPI"))"
    
- rank: 7  
    name: "remark / unified / mdast"  
    category: "Markdown_AST_framework"  
    evd: 90  
    imp: 76  
    rsk: 42  
    cost: 62  
    best_use_case: "Complex Markdown transformations requiring AST semantics."  
    not_for: "Small section replacement where mdpatch or heading-boundary parser is enough."  
    copy_or_build_decision: "Reserve for V2; avoid as V1 dependency unless mdpatch fails."  
    evidence: "AST-based Markdown ecosystem with CLI and plugin system. ([unified](https://unifiedjs.com/explore/package/remark-cli/?utm_source=chatgpt.com "remark-cli - unified"))"
    
- rank: 8  
    name: "Claude Code deterministic hooks"  
    category: "agent_enforcement_layer"  
    evd: 92  
    imp: 80  
    rsk: 45  
    cost: 40  
    best_use_case: "Blocking direct Write/Edit/MultiEdit and dangerous Bash unless executor protocol is satisfied."  
    not_for: "Replacing executor logic."  
    copy_or_build_decision: "Build small project-local hooks; do not use broad hook packs wholesale."  
    evidence: "Official docs and guide support deterministic hook control and decision blocking. ([Claude](https://code.claude.com/docs/en/hooks?utm_source=chatgpt.com "Hooks reference - Claude Code Docs"))"
    
- rank: 9  
    name: "Comby"  
    category: "structural_search_replace"  
    evd: 78  
    imp: 66  
    rsk: 46  
    cost: 42  
    best_use_case: "Repeated code-like structural replacements embedded in Markdown or config."  
    not_for: "Prose-heavy Markdown section replacement."  
    copy_or_build_decision: "Optional tool; not core."  
    evidence: "Structural search/replace across many languages, easier than regex for code structures. ([comby.dev](https://comby.dev/?utm_source=chatgpt.com "Comby · Structural code search and replace for ~every language."))"
    
- rank: 10  
    name: "markdownlint-cli / remark-lint / pre-commit"  
    category: "validation"  
    evd: 80  
    imp: 52  
    rsk: 26  
    cost: 34  
    best_use_case: "Post-edit style/schema validation."  
    not_for: "Semantic correctness or span safety."  
    copy_or_build_decision: "Use as optional validation gate; do not block finalization on full-corpus lint unless baseline already clean."  
    evidence: "Markdown linting and pre-commit integration documented. ([DeepWiki](https://deepwiki.com/markdownlint/markdownlint/2.3-pre-commit-hook-integration?utm_source=chatgpt.com "Pre-commit Hook Integration | markdownlint/markdownlint | DeepWiki"))"
    
- rank: 11  
    name: "dasel"  
    category: "structured_config_patcher"  
    evd: 82  
    imp: 58  
    rsk: 32  
    cost: 26  
    best_use_case: "JSON/YAML/TOML/XML/KDL config edits outside Markdown."  
    not_for: "Native Markdown section/frontmatter patching without extraction wrapper."  
    copy_or_build_decision: "Optional for non-Markdown config patching."  
    evidence: "Multi-format query/modify CLI and library. ([GitHub](https://github.com/TomWright/dasel?utm_source=chatgpt.com "GitHub - TomWright/dasel: Unified querying, transformation, and ..."))"
    
- rank: 12  
    name: "SDD Toolkit / sdd-modify"  
    category: "spec_workflow_skill"  
    evd: 68  
    imp: 55  
    rsk: 52  
    cost: 55  
    best_use_case: "Spec plan management, progress state, rollback ideas."  
    not_for: "Direct Markdown patch execution."  
    copy_or_build_decision: "Adapt concepts only; do not make it core."  
    evidence: "Spec-driven JSON workflow; sdd-modify claims validation and rollback for spec modifications. ([GitHub](https://github.com/tylerburleigh/claude-sdd-toolkit?utm_source=chatgpt.com "GitHub - tylerburleigh/claude-sdd-toolkit: Development tools and ..."))"
    
- rank: 13  
    name: "existing md-patcher skill"  
    category: "AI_diff_generation_skill"  
    evd: 50  
    imp: 44  
    rsk: 66  
    cost: 30  
    best_use_case: "Fallback when executor cannot be used and user needs a patch-shaped artifact."  
    not_for: "Primary reliable patching."  
    copy_or_build_decision: "Demote to fallback; supersede with executor-based skill."  
    evidence: "Internal md-patcher forces diff hunks and `patch --fuzz=3`; it still relies on AI-authored hunks. "
    
- rank: 14  
    name: "large third-party Claude skill collections"  
    category: "skill_marketplace_source"  
    evd: 64  
    imp: 30  
    rsk: 78  
    cost: 64  
    best_use_case: "Pattern mining after security review."  
    not_for: "Wholesale copying into patch executor."  
    copy_or_build_decision: "Do not copy wholesale."  
    evidence: "Large collections exist, but skill security research shows real supply-chain/prompt-injection risks. ([GitHub](https://github.com/alirezarezvani/claude-skills?utm_source=chatgpt.com "GitHub - alirezarezvani/claude-skills: 345 Claude Code skills & agent ..."))"
    

existing_skill_gap_verdict:  
complete_package_found: false  
closest_existing_package:  
name: "markdown-patch/mdpatch + SDD Toolkit concepts + Claude Code hooks"  
verdict: "Closest combination, not a complete package."  
missing_capabilities:  
- "Single package combining LLM plan/spec, deterministic live-span selection, deterministic apply, git diff proof, rollback, changed-file scope validation, and Claude Code PreToolUse/PostToolUse/FileChanged/Stop enforcement."  
- "Markdown/config support under one no-agent-write executor."  
- "Mandatory uniqueness checks before write."  
- "Direct Write/Edit/MultiEdit blocking unless executor protocol passes."  
- "Patch-pack finalizer that owns validation and optional commit/push."  
confidence: "high"  
explanation:  
- "markdown-patch covers Markdown targeting but not agent enforcement."  
- "SDD Toolkit covers spec workflow and rollback concepts but not general file mutation ownership."  
- "Claude hooks can block or monitor tools but do not supply patch semantics."  
- "Large skill collections exist, but no searched result showed the full combined architecture."

architecture_options:

- option: "A: current live-span replacer architecture"  
    description: "AI states intent and candidate target; executor extracts exact live span, verifies uniqueness, replaces once, shows git diff, validates, optionally finalizes."  
    files_needed:
    
    - "patch_executor.py"
        
    - "patch_policy.json"
        
    - "validate_patch_pack.py or executor subcommand"
        
    - "minimal SKILL.md wrapper"  
        runtime_dependencies:
        
    - "Python stdlib"
        
    - "git"
        
    - "ripgrep optional"
        
    - "yq optional"  
        how_it_blocks_AI_mistakes:
        
    - "No AI-authored exact search string."
        
    - "No direct full-file rewrite."
        
    - "Old span must exist exactly once."
        
    - "Git diff is source of truth."  
        evd: 88  
        imp: 96  
        rsk: 18  
        cost: 28  
        finalization_readiness: "high"
        
- option: "B: markdown-patch/mdpatch-based architecture"  
    description: "Use mdpatch for Markdown heading/block/frontmatter targets, wrapped by custom executor and git validation."  
    files_needed:
    
    - "mdpatch wrapper script"
        
    - "scope validator"
        
    - "hook policy"
        
    - "manifest schema"  
        runtime_dependencies:
        
    - "Node/TypeScript package markdown-patch"
        
    - "git"  
        how_it_blocks_AI_mistakes:
        
    - "Uses Markdown structure rather than approximate diff hunks."
        
    - "Better target semantics than sed."
        
    - "Still needs wrapper to prevent direct agent mutation."  
        evd: 76  
        imp: 88  
        rsk: 28  
        cost: 32  
        finalization_readiness: "medium-high; run a fixture bakeoff before adopting"
        
- option: "C: SDD-toolkit + Claude hooks architecture"  
    description: "Use SDD Toolkit-style JSON specs and Claude hooks to enforce spec-first edits."  
    files_needed:
    
    - "plan/spec schema"
        
    - "hooks"
        
    - "adapter from spec to executor"  
        runtime_dependencies:
        
    - "Claude Code hooks"
        
    - "possibly SDD Toolkit"
        
    - "git"  
        how_it_blocks_AI_mistakes:
        
    - "Plan-first state makes scope explicit."
        
    - "Hooks can block non-compliant tool calls."  
        evd: 68  
        imp: 65  
        rsk: 55  
        cost: 62  
        finalization_readiness: "low-medium; adapt concepts, do not base core on it"
        
- option: "D: yq/frontmatter-first architecture"  
    description: "Move recurring state into YAML frontmatter; mutate metadata with yq; reserve prose edits for executor."  
    files_needed:
    
    - "frontmatter schema"
        
    - "yq wrapper"
        
    - "schema validator"  
        runtime_dependencies:
        
    - "yq"
        
    - "git"  
        how_it_blocks_AI_mistakes:
        
    - "Most recurring edits avoid prose entirely."
        
    - "Metadata mutations become deterministic."  
        evd: 92  
        imp: 84  
        rsk: 20  
        cost: 16  
        finalization_readiness: "high for metadata; incomplete for prose"
        
- option: "E: no-agent-write architecture where only executor script mutates files"  
    description: "Claude Code Write/Edit/MultiEdit disabled or blocked for target files; only approved executor writes files."  
    files_needed:
    
    - "executor.py"
        
    - "PreToolUse hook"
        
    - "PostToolUse/FileChanged/Stop audit hook"
        
    - "policy file"  
        runtime_dependencies:
        
    - "Claude Code hooks"
        
    - "Python"
        
    - "git"  
        how_it_blocks_AI_mistakes:
        
    - "Agent cannot directly mutate protected paths."
        
    - "All writes pass through validate-before-apply."
        
    - "FileChanged catches out-of-band drift."  
        evd: 86  
        imp: 98  
        rsk: 22  
        cost: 45  
        finalization_readiness: "highest reliability; slightly higher setup cost"
        
- option: "F: generated Markdown from structured store"  
    description: "Store canonical state in frontmatter/JSON/SQLite/OKF-like schema; generate Markdown as output artifact."  
    files_needed:
    
    - "schema"
        
    - "generator"
        
    - "diff validator"  
        runtime_dependencies:
        
    - "Python or Node"
        
    - "git"  
        how_it_blocks_AI_mistakes:
        
    - "Reduces direct prose mutation."
        
    - "Generated files can be replaced deterministically."  
        evd: 52  
        imp: 62  
        rsk: 48  
        cost: 72  
        finalization_readiness: "low for now; only for high-volume recurring KB state"
        

recommended_final_architecture:  
thesis: "Adopt no-agent-write live-span execution as the core. Add mdpatch as the Markdown section engine if fixture tests prove it preserves surrounding formatting. Keep git-generated diffs as proof artifacts. Do not use AI-authored unified diffs except emergency fallback."  
minimum_files_to_build:  
- path: "SKILL.md"  
purpose: "Short rule wrapper: AI only writes intent/spec, never direct patches."  
- path: "patch_executor.py"  
purpose: "Subcommands: locate, extract, replace-once, replace-heading-section, frontmatter-set, validate, finalize."  
- path: "patch_policy.json"  
purpose: "Allowed target roots, forbidden tools, allowed commands, validation commands."  
- path: "hooks/pre_tool_use.py"  
purpose: "Block Write/Edit/MultiEdit on protected Markdown/config paths; block Bash mutation commands unless executor command is used."  
- path: "hooks/post_tool_use_or_file_changed.py"  
purpose: "Detect unexpected file drift and require git diff/scope validation."  
- path: "fixtures/"  
purpose: "Golden Markdown fixtures for headings, duplicate headings, frontmatter, repeated spans, path-scope violations."  
existing_code_to_copy:  
- "Internal replace_once concept from ClaudePatchRedesign."  
- "Internal stub_repair_toolkit ideas: git worktree, git apply checks, no-cache compile, fixture JSON assertions."  
- "Optional: mdpatch semantics if tests prove reliable."  
custom_code_needed:  
- "Exact span extractor."  
- "Markdown heading-boundary fallback if mdpatch unsuitable."  
- "Policy-aware executor wrapper."  
- "Changed-file scope validator."  
- "Hook scripts."  
hook_policy:  
PreToolUse:  
- "Block Write/Edit/MultiEdit for protected paths."  
- "Block Bash commands containing sed -i, perl -i, python write_text, cat > file, mv over protected file, git apply, patch unless command invokes approved executor/finalizer."  
- "Allow read-only rg/git diff/git status."  
PostToolUse:  
- "After any allowed executor write, require git diff summary and scope report."  
- "Block continuation if unexpected paths changed."  
FileChanged:  
- "Detect writes outside executor."  
- "Mark session dirty until rollback or explicit operator approval."  
Stop:  
- "Prevent final success report unless validation manifest exists."  
script_policy:  
- "Executor owns all mutation."  
- "Agent may generate replacement content into temp/new-span file, but executor performs final replace."  
- "No exact old search string typed by AI; old span is extracted from live file."  
- "No full-file rewrite unless policy flag `allow_full_file_rewrite: true` is explicitly set for generated files."  
validation_policy:  
- "Match count must equal 1 for exact-span replacement."  
- "Heading target must resolve to exactly one section unless explicit duplicate-handling mode is set."  
- "Frontmatter parse must succeed before and after mutation."  
- "git diff must show only allowed files."  
- "Optional markdownlint/remark-lint only if baseline corpus is lint-clean or rule-scoped."  
rollback_policy:  
- "Before apply: dry-run/plan mode outputs proposed diff."  
- "During apply: write through temp file + atomic replace."  
- "After apply failure: git checkout -- allowed changed files or worktree discard."  
- "Before commit/push: git status and scope validator must pass."

kill_list:

- id: "ai_authored_unified_diff_as_primary"  
    decision: "remove"  
    reason: "Internal failure model and web research both favor deterministic live-state operations; existing md-patcher is only fallback."
    
- id: "patch_fuzz_as_reliability_strategy"  
    decision: "demote"  
    reason: "`patch --fuzz=3` may make stale hunks apply too generously; prefer exact span or git apply generated from real diff."
    
- id: "large_multifile_process_contracts"  
    decision: "remove_or_compress"  
    reason: "Use one compact OKF policy/spec, not many repetitive process files."
    
- id: "subagent_design_review_by_default"  
    decision: "remove"  
    reason: "Internal inefficiency report shows design subagents re-derived already-read context and increased cost."
    
- id: "full_corpus_lint_as_default_gate"  
    decision: "avoid"  
    reason: "Can block unrelated legacy Markdown style issues; use target-file validation unless baseline is clean."
    
- id: "copy_public_skills_wholesale"  
    decision: "forbid"  
    reason: "Recent skill security research shows code+instruction supply-chain risk."
    
- id: "Comby_as_core_markdown_tool"  
    decision: "demote_to_optional"  
    reason: "Useful for code-like structures; Markdown headings/frontmatter are better handled by mdpatch/yq/custom heading parser."
    
- id: "SDD_toolkit_as_core_patch_engine"  
    decision: "do_not_use_as_core"  
    reason: "Spec workflow is useful, but searched evidence does not show it owns deterministic Markdown/config mutation."
    

open_research:

- id: "mdpatch_fixture_bakeoff"  
    question: "Can markdown-patch preserve exact formatting and correctly reject duplicate/ambiguous headings across Apex-style Markdown?"  
    materiality: "High; determines whether custom markdown-section-replacer can be reduced."  
    test: "Run fixtures: duplicate heading, nested heading, heading in fenced code, frontmatter plus first H1, CRLF, no trailing newline."
    
- id: "Claude_Code_hook_parameter_depth"  
    question: "Do current hook payloads expose enough tool parameters to reliably block Write/Edit/MultiEdit and dangerous Bash patterns in the user's exact environment?"  
    materiality: "High; determines whether hook enforcement is sufficient."  
    test: "Implement audit-only hooks first; log payloads for Write/Edit/MultiEdit/Bash/FileChanged."
    
- id: "yq_format_stability"  
    question: "Does yq preserve frontmatter ordering/comments/quoting sufficiently for Apex OKF files?"  
    materiality: "Medium."  
    test: "Fixture compare before/after for comments, arrays, dates, multiline strings."
    
- id: "executor_language"  
    question: "Should executor be Python-only for portability or Node-based to reuse mdpatch directly?"  
    materiality: "Medium."  
    decision_signal: "If mdpatch passes bakeoff, Node wrapper may be cheaper; otherwise Python stdlib/custom parser is safer."
    
- id: "generated_markdown_store"  
    question: "Should some KB state move to structured JSON/frontmatter and regenerate Markdown?"  
    materiality: "Low-medium now; high only if recurring patch volume remains large."
    

finalization_prompt:  
prompt_type: "deterministic_build_prompt"  
role: "patch_skill_finalizer"  
instructions:  
- "Repo: apexai-os-meta."  
- "Branch: main."  
- "Work directly on main."  
- "Do not create a branch or PR."  
- "Target files: apex-meta/SmallSkills/Patching/."  
- "Build final deterministic Markdown patching skill/process from the research report."  
- "Create or update only the minimum files: SKILL.md, patch_executor.py, patch_policy.json, hooks/pre_tool_use.py, hooks/post_tool_use_or_file_changed.py, fixtures/README.md."  
- "Primary rule: AI never authors final unified diffs or exact old search strings."  
- "Executor must support: extract live span, replace once, heading-section replace, frontmatter-set via yq or parser, git diff proof, scope validation, rollback."  
- "Hooks must block protected-path Write/Edit/MultiEdit and dangerous Bash unless using executor."  
- "Run commands: python -m py_compile patch_executor.py hooks/pre_tool_use.py hooks/post_tool_use_or_file_changed.py; run executor fixture tests; git diff -- apex-meta/SmallSkills/Patching."  
- "Expected result: tests pass; no unrelated files changed."  
- "Commit message: Add deterministic Markdown patch executor skill."  
- "Commit and push origin main."  
- "Final report format: changed files, commands run, pass/fail, commit SHA."