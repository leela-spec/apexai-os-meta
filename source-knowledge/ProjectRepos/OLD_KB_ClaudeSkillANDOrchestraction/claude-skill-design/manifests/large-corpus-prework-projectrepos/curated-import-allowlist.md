# Claude Skill Design Curated Import Allowlist

## 1. Executive Verdict

- Is the current KB already enough for official-baseline Phase 1? Yes, if the existing curated official docs/repos remain the source of canonical rules; ProjectRepos should not replace them.
- Additional repo files should be imported before final synthesis: a compact set of real SKILL.md examples, skillcheck/evaluation fixtures, prompt/instruction examples, MCP/tool-boundary examples, and package/template/reference examples from the generated ProjectRepos candidates.
- Repos/folders to exclude: duplicate antigravity plugin/bundle copies, large generated JSON catalogs, binary/media assets, dependency/build files, task-management-only files, and generic app implementation code.

Bucket interpretation:
- `canonical_official`: No new ProjectRepos candidate is treated as canonical official. Use existing official-docs/official-repos as baseline.
- `skill_package_examples`: Real SKILL.md examples and package structures for comparative analysis.
- `skill_quality_and_evaluation`: Validation, testing, linting, rubric, and negative examples.
- `prompt_and_instruction_design`: Prompt, instruction, context, role, and planning design relevant to SKILL.md authoring.
- `tool_script_boundaries`: Sources involving scripts, CLI, MCP, tools, references, and command boundaries.
- `subskill_or_package_architecture`: Nested paths, manifests, templates, references, memory, or modular workflow structure.
- `comparative_agent_frameworks`: Agent/process frameworks used only when transferable to skill package design.
- `noise_or_exclude`: Assets, generated files, duplicate plugin copies, generic app code, and project-management-only files.

## 2. Include First

| priority | bucket | repo | path | reason | expected KB value |
| ---: | --- | --- | --- | --- | --- |
| 1 | skill_package_examples | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/skill-writer/SKILL.md` | Directly about writing skills; high-value meta example for SKILL.md authoring. | Shows how a skill about skill creation frames scope, triggers, and workflow. |
| 1 | skill_package_examples | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/using-superpowers/SKILL.md` | Directly about using skills; strong evidence for skill activation and usage patterns. | Helps define user-facing skill behavior and boundaries. |
| 1 | skill_quality_and_evaluation | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/skill-check/SKILL.md` | Skill quality/checking package surfaced by deterministic ranking. | Useful for evaluation criteria and bad-pattern detection. |
| 1 | skill_quality_and_evaluation | skillcheck | `skillcheck/skills/skillcheck/SKILL.md` | Dedicated skillcheck repo candidate. | Likely strongest external evaluation/linting source in ProjectRepos. |
| 1 | skill_quality_and_evaluation | crewAI-main | `crewAI-main/lib/crewai/tests/skills/fixtures/valid-skill/SKILL.md` | Valid fixture for skill parsing/validation. | Gives concrete pass-case evidence for minimum expected structure. |
| 1 | skill_quality_and_evaluation | crewAI-main | `crewAI-main/lib/crewai/tests/skills/fixtures/minimal-skill/SKILL.md` | Minimal fixture for skill parsing/validation. | Clarifies lower bound of acceptable skill package shape. |
| 1 | skill_quality_and_evaluation | crewAI-main | `crewAI-main/lib/crewai/tests/skills/fixtures/invalid-name/SKILL.md` | Invalid fixture for skill parsing/validation. | Useful negative example for lint/rubric design. |
| 1 | subskill_or_package_architecture | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/manifest/SKILL.md` | Manifest-focused skill package. | Useful for package metadata and source manifest boundaries. |
| 1 | tool_script_boundaries | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/reference-builder/SKILL.md` | Reference-building package. | Shows how references can be created and routed as supporting material. |
| 1 | subskill_or_package_architecture | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/app-builder/templates/SKILL.md` | Nested templates skill under a larger package path. | Evidence for nested package/subskill-like organization. |
| 1 | subskill_or_package_architecture | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/documentation-templates/SKILL.md` | Template-oriented package. | Useful for template folder semantics and reusable artifacts. |
| 1 | skill_package_examples | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/ai-agent-development/SKILL.md` | Highest ranked agent-development skill. | Representative high-signal workflow skill for agent design. |
| 1 | skill_package_examples | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/documentation/SKILL.md` | High-ranked documentation workflow bundle. | Shows bundle-style skill description and documentation workflow framing. |
| 1 | skill_package_examples | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/rag-implementation/SKILL.md` | High-ranked RAG implementation workflow. | Relevant to KB/retrieval skill design and reference use. |
| 1 | skill_quality_and_evaluation | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/agenttrace-session-audit/SKILL.md` | Audit/session package with high agent signal. | Useful for quality, trace, and completion-audit patterns. |
| 1 | comparative_agent_frameworks | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/parallel-agents/SKILL.md` | Parallel agent package with strong agent/workflow signal. | Transfers orchestration ideas into skill-package boundaries. |
| 1 | skill_quality_and_evaluation | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/testing-qa/SKILL.md` | Testing/QA workflow bundle. | Supports evaluation, validation, and QA sections of the KB. |
| 1 | prompt_and_instruction_design | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/writing-plans/SKILL.md` | Planning/instruction skill with strong workflow signal. | Useful for instruction sequencing and task-plan prompt structure. |
| 1 | skill_quality_and_evaluation | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/security-audit/SKILL.md` | Security auditing workflow bundle. | Good exemplar for safety/risk-oriented skill behavior. |
| 1 | skill_quality_and_evaluation | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/api-security-testing/SKILL.md` | API security testing workflow. | Supports evaluation and tool-boundary examples. |
| 1 | tool_script_boundaries | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/mcp-tool-developer/SKILL.md` | MCP tool developer skill. | Strong source for tools/connectors and skill-tool boundaries. |
| 1 | tool_script_boundaries | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/runapi-cli/SKILL.md` | CLI-oriented skill package. | Concrete example of command/tool usage boundaries. |
| 1 | tool_script_boundaries | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/tool-use-guardian/SKILL.md` | Tool-use governance package. | Likely useful for safe allowed-tools and command discipline. |
| 1 | subskill_or_package_architecture | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/agent-memory-mcp/SKILL.md` | Agent memory MCP package. | Useful for memory/context boundaries in skill packages. |
| 1 | subskill_or_package_architecture | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/hierarchical-agent-memory/SKILL.md` | Hierarchical memory package. | Potential evidence for modular memory/reference design. |
| 1 | comparative_agent_frameworks | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/multi-agent-brainstorming/SKILL.md` | Structured multi-agent design review package. | Transferable patterns for staged workflows and role separation. |
| 1 | subskill_or_package_architecture | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/design-orchestration/SKILL.md` | Meta-skill for design orchestration. | Good evidence for package orchestration and nested workflow design. |
| 1 | subskill_or_package_architecture | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/open-dynamic-workflows/SKILL.md` | Workflow/package metadata candidate. | May clarify dynamic workflow declaration and upstream/license metadata. |
| 1 | prompt_and_instruction_design | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/recursive-context-pruning-token-budgeting/SKILL.md` | Context/token budgeting skill. | Useful for progressive disclosure and bounded context design. |
| 1 | prompt_and_instruction_design | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/llm-application-dev-prompt-optimize/SKILL.md` | Prompt optimization package. | Directly relevant to description/prompt/instruction design. |
| 1 | skill_quality_and_evaluation | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/verification-before-completion/SKILL.md` | Verification-before-completion package. | Good source for completion gates and quality rubrics. |
| 1 | prompt_and_instruction_design | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/claude-code-guide/SKILL.md` | Claude-code guide package. | Relevant to Claude-specific instruction style and operational boundaries. |
| 1 | prompt_and_instruction_design | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/agents-md/SKILL.md` | AGENTS.md maintenance package. | Useful comparative instruction-file pattern for skills. |
| 1 | skill_package_examples | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/api-documentation/SKILL.md` | API documentation workflow. | Representative docs-oriented package with references/tool boundaries. |
| 1 | skill_package_examples | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/yao-meta-skill/SKILL.md` | Meta-skill with high skill-package keyword signal. | Useful for studying meta-skill anti/patterns. |
| 1 | tool_script_boundaries | claude-skills-main | `claude-skills-main/skills/mcp-developer/SKILL.md` | MCP Developer skill from a separate Claude-skills repo. | Cross-repo example for MCP/tool skill design. |
| 1 | skill_package_examples | claude-skills-main | `claude-skills-main/skills/code-documenter/SKILL.md` | Documentation-oriented Claude skill. | Compare against antigravity documentation package. |
| 1 | skill_quality_and_evaluation | claude-skills-main | `claude-skills-main/skills/security-reviewer/SKILL.md` | Security reviewer Claude skill. | Quality/risk review example from another repo family. |
| 1 | skill_quality_and_evaluation | claude-skills-main | `claude-skills-main/skills/code-reviewer/SKILL.md` | Code reviewer Claude skill. | Evaluation/review behavior example. |
| 1 | tool_script_boundaries | claude-skills-main | `claude-skills-main/skills/cli-developer/SKILL.md` | CLI developer Claude skill. | Good tool/command boundary comparison. |
| 1 | prompt_and_instruction_design | claude-skills-main | `claude-skills-main/skills/spec-miner/SKILL.md` | Spec mining skill. | Useful for source extraction and requirements-oriented prompts. |
| 1 | skill_quality_and_evaluation | claude-skills-main | `claude-skills-main/skills/test-master/SKILL.md` | Testing-focused Claude skill. | Cross-repo test/evaluation source. |
| 1 | subskill_or_package_architecture | claude-skills-main | `claude-skills-main/skills/architecture-designer/SKILL.md` | Architecture-design Claude skill. | Useful for comparing design role packaging. |
| 1 | prompt_and_instruction_design | claude-skills-main | `claude-skills-main/skills/feature-forge/SKILL.md` | Feature generation/planning skill. | Instruction design example for turning requirements into work. |
| 1 | skill_package_examples | claude-skills-main | `claude-skills-main/skills/playwright-expert/SKILL.md` | High-ranked concrete tool/domain skill. | Representative real-world skill package with testing/tool angle. |

## 3. Maybe Later

| bucket | repo | path | reason | condition |
| --- | --- | --- | --- | --- |
| skill_package_examples | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/react-nextjs-development/SKILL.md` | Ranked ProjectRepos candidate not essential for first import. | Representative app-development package; import if needing broader examples. |
| skill_package_examples | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/python-fastapi-development/SKILL.md` | Ranked ProjectRepos candidate not essential for first import. | Representative backend/API package. |
| tool_script_boundaries | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/seek-and-analyze-video/SKILL.md` | Ranked ProjectRepos candidate not essential for first import. | Media analysis package; useful if studying tool/reference boundaries. |
| skill_package_examples | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/agentfolio/SKILL.md` | Ranked ProjectRepos candidate not essential for first import. | Agent/persona portfolio package; maybe useful for meta-agent examples. |
| skill_quality_and_evaluation | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/web-security-testing/SKILL.md` | Ranked ProjectRepos candidate not essential for first import. | Security testing package; include if expanding safety/eval examples. |
| skill_package_examples | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/database/SKILL.md` | Ranked ProjectRepos candidate not essential for first import. | Database workflow bundle; representative technical package. |
| skill_package_examples | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/postgresql-optimization/SKILL.md` | Ranked ProjectRepos candidate not essential for first import. | Concrete optimization package; useful domain example. |
| skill_quality_and_evaluation | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/e2e-testing/SKILL.md` | Ranked ProjectRepos candidate not essential for first import. | Testing workflow package; include if QA coverage needs more examples. |
| tool_script_boundaries | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/bash-scripting/SKILL.md` | Ranked ProjectRepos candidate not essential for first import. | Script-heavy package; useful for command boundary analysis. |
| tool_script_boundaries | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/cloud-devops/SKILL.md` | Ranked ProjectRepos candidate not essential for first import. | DevOps package likely to contain command/tool boundaries. |
| subskill_or_package_architecture | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/antigravity-workflows/SKILL.md` | Ranked ProjectRepos candidate not essential for first import. | Workflow-level package; useful for architecture comparison. |
| comparative_agent_frameworks | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/global-chat-agent-discovery/SKILL.md` | Ranked ProjectRepos candidate not essential for first import. | Agent discovery package; useful but not core. |
| subskill_or_package_architecture | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/recallmax/SKILL.md` | Ranked ProjectRepos candidate not essential for first import. | Long-context memory package; maybe useful for context design. |
| prompt_and_instruction_design | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/bdistill-knowledge-extraction/SKILL.md` | Ranked ProjectRepos candidate not essential for first import. | Knowledge extraction package; useful if source-analysis coverage is thin. |
| skill_package_examples | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/uxui-principles/SKILL.md` | Ranked ProjectRepos candidate not essential for first import. | Small domain skill example. |
| comparative_agent_frameworks | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/antigravity-agent-manager/SKILL.md` | Ranked ProjectRepos candidate not essential for first import. | Agent manager package; useful but may drift from skill design. |
| skill_quality_and_evaluation | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/tdd-workflow/SKILL.md` | Ranked ProjectRepos candidate not essential for first import. | TDD workflow source; include if evaluation needs development-process examples. |
| skill_quality_and_evaluation | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/tdd/SKILL.md` | Ranked ProjectRepos candidate not essential for first import. | TDD package; maybe duplicate with tdd-workflow. |
| skill_package_examples | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/senior-architect/SKILL.md` | Ranked ProjectRepos candidate not essential for first import. | Role-based skill example; include only if studying personas. |
| skill_package_examples | antigravity-awesome-skills-main | `antigravity-awesome-skills-main/skills/senior-fullstack/SKILL.md` | Ranked ProjectRepos candidate not essential for first import. | Role-based fullstack package; non-core. |
| skill_package_examples | claude-skills-main | `claude-skills-main/skills/dotnet-core-expert/SKILL.md` | Ranked ProjectRepos candidate not essential for first import. | High-ranked concrete Claude-skill example. |
| skill_package_examples | claude-skills-main | `claude-skills-main/skills/flutter-expert/SKILL.md` | Ranked ProjectRepos candidate not essential for first import. | Concrete domain skill; maybe later. |
| skill_package_examples | claude-skills-main | `claude-skills-main/skills/vue-expert/SKILL.md` | Ranked ProjectRepos candidate not essential for first import. | Concrete frontend skill; maybe later. |
| skill_package_examples | claude-skills-main | `claude-skills-main/skills/golang-pro/SKILL.md` | Ranked ProjectRepos candidate not essential for first import. | Concrete language skill; maybe later. |
| tool_script_boundaries | claude-skills-main | `claude-skills-main/skills/atlassian-mcp/SKILL.md` | Ranked ProjectRepos candidate not essential for first import. | MCP/tool-focused Claude skill; useful if MCP coverage expands. |
| skill_package_examples | claude-skills-main | `claude-skills-main/skills/react-expert/SKILL.md` | Ranked ProjectRepos candidate not essential for first import. | Concrete frontend skill; maybe later. |
| subskill_or_package_architecture | claude-skills-main | `claude-skills-main/skills/java-architect/SKILL.md` | Ranked ProjectRepos candidate not essential for first import. | Architecture/persona example. |
| skill_package_examples | claude-skills-main | `claude-skills-main/skills/typescript-pro/SKILL.md` | Ranked ProjectRepos candidate not essential for first import. | Concrete language skill; maybe later. |
| skill_quality_and_evaluation | claude-skills-main | `claude-skills-main/skills/debugging-wizard/SKILL.md` | Ranked ProjectRepos candidate not essential for first import. | Debugging workflow example. |
| skill_package_examples | claude-skills-main | `claude-skills-main/skills/javascript-pro/SKILL.md` | Ranked ProjectRepos candidate not essential for first import. | Concrete language skill; maybe later. |
| skill_package_examples | claude-skills-main | `claude-skills-main/skills/nextjs-developer/SKILL.md` | Ranked ProjectRepos candidate not essential for first import. | Concrete framework skill; maybe later. |
| skill_package_examples | claude-skills-main | `claude-skills-main/skills/sql-pro/SKILL.md` | Ranked ProjectRepos candidate not essential for first import. | Concrete data skill; maybe later. |
| subskill_or_package_architecture | claude-skills-main | `claude-skills-main/skills/graphql-architect/SKILL.md` | Ranked ProjectRepos candidate not essential for first import. | Architecture example; maybe later. |
| skill_package_examples | claude-skills-main | `claude-skills-main/skills/cpp-pro/SKILL.md` | Ranked ProjectRepos candidate not essential for first import. | Concrete language skill; maybe later. |

## 4. Exclude / Pollution

| repo/path | reason |
| --- | --- |
| `antigravity-awesome-skills-main/plugins/antigravity-awesome-skills-claude/skills/*` | Mostly duplicate copies of top-level antigravity skills; import cleaner top-level skills first. |
| `antigravity-awesome-skills-main/plugins/antigravity-awesome-skills/skills/*` | Mostly duplicate plugin copies of top-level skills; avoid duplicate import pollution. |
| `antigravity-awesome-skills-main/plugins/antigravity-bundle-*/skills/*` | Bundle copies duplicate canonical/top-level skill examples unless package architecture is specifically under review. |
| `antigravity-awesome-skills-main/data/catalog.json` | Large generated catalog skipped by byte limit; use schema-specific extractor later if needed. |
| `antigravity-awesome-skills-main/data/skills_index.json` | Large generated skill index; do not import raw JSON catalog into KB sources. |
| `antigravity-awesome-skills-main/skills_index.json` | Duplicate/generated skill index; not a curated source file. |
| `crewAI-main/docs/images/*` | Binary/assets and screenshots; not text evidence for skill design. |
| `crewAI-main/docs/docs.json` | Large generated docs index; schema-specific extraction required before use. |
| `crewAI-main/lib/crewai/tests/cassettes/*` | Test cassette data; not skill-package design evidence. |
| `claude-task-master-main/.taskmaster/tasks/tasks.json` | Large task-management data; project-management artifact, not skill package design. |
| `claude-task-master-main/package-lock.json` | Build/dependency lockfile; exclude. |
| `backlog-main/*` | Project/task management family absent from top candidate set; include only if later studying process tooling, not Claude skill packaging. |
| `ccpm-main/*` | Project-management/process framework; not core for Claude Skill Design KB. |
| `planning-with-files-master/media/*` | Media assets; exclude from text KB import. |
| `source-knowledge/ProjectRepos/**/node_modules/**` | Generated dependency trees; never import. |
| `source-knowledge/ProjectRepos/**/.git/**` | Git internals; never import. |
| `source-knowledge/ProjectRepos/**/*.png|*.jpg|*.jpeg|*.gif|*.mov|*.mp4|*.ttf|*.woff*` | Binary assets/fonts/media; not text source evidence. |
| `generic app source code under antigravity/crewAI/other repos` | Only include code when it explains skill package boundaries; generic app implementation is pollution. |

## 5. Recommended Phase 1 Batches After Import

1. Official baseline refresh: read existing `sources/curated/official-docs/`, `sources/curated/official-pdfs/`, and official repo spec/template sources before any ProjectRepos examples.
2. Skill package anatomy examples: import and analyze the include-first SKILL.md files focused on skill writer, using skills, manifest, reference builder, templates, documentation, RAG, and agent development.
3. Quality and evaluation examples: process `skillcheck`, CrewAI valid/minimal/invalid fixtures, testing/QA, verification, code review, and security review files.
4. Prompt/tool boundary examples: process prompt optimization, Claude code guide, AGENTS.md, MCP developer, CLI developer, runapi-cli, tool-use guardian, and bash/CLI candidates if later needed.
5. Architecture/modularity examples: process app-builder/templates, documentation-templates, design orchestration, agent memory, hierarchical memory, and multi-agent examples only after official rules are fixed.

## 6. Remaining Source Gaps

- ProjectRepos prework does not itself add canonical official Claude/Anthropic Agent Skills guidance; keep official baseline from curated official docs/repos.
- Need source-backed confirmation for subskills/nested package semantics from official or near-official sources before treating nested examples as canonical.
- Need stronger official guidance on description/frontmatter/allowed-tools constraints if not already covered by existing official sources.
- Need a focused evaluation/rubric source beyond skillcheck and fixture examples for high-confidence quality scoring.
- Need explicit bad-pattern examples for overbroad descriptions, unsafe tools, missing references, and generated-package pollution.
