# Research Report: Star-Rated Execution-Agent & Orchestration Repos for Apex

**Bottom line:** The highest-signal repos for Apex are `shanraisshan/claude-code-best-practice` (61.6k ★), `hesreallyhim/awesome-claude-code` (47.6k ★), and `bmad-code-org/BMAD-METHOD` (36k ★). The rest fill specific gaps in subagent design, plugin libraries, and comparable non-Claude orchestration systems.

---

## 6.1 Executive Verdict

**best_overall_sources:**

- `shanraisshan/claude-code-best-practice` — most complete reference for `.claude/` layout, 16 frontmatter fields, 70+ commands, orchestration workflow diagrams, all verified with real file trees[[youtube](https://www.youtube.com/watch?v=9rgDMm8QUIg)][[github.attentionvc](https://github.attentionvc.ai/repos/shanraisshan/claude-code-best-practice)]
    
- `bmad-code-org/BMAD-METHOD` — only repo with a complete orchestrator→agent→workflow→task chain in production use, 36k ★, directly copyable agent markdown files[[github](https://github.com/bmad-code-org/bmad-method)]
    

**best_for_claude_code_layout:**

- `shanraisshan/claude-code-best-practice` — documents exact `.claude/agents/`, `.claude/commands/`, `.claude/rules/`, `.claude/skills/` with real implementation files[[youtube](https://www.youtube.com/watch?v=9rgDMm8QUIg)]
    
- `jeremylongshore/claude-code-plugins-plus-skills` — 425 plugins, 2,810 skills, 200 agents, ccpi CLI package manager, tonsofskills.com marketplace[[ai-toolbase](https://ai-toolbase.com/en/tools/claude-code-plugins-plus-skills)]
    

**best_for_personal_orchestration:**

- `bmad-code-org/BMAD-METHOD` — orchestrator agent with role-based subagents, story/task/plan workflow, markdown-native, local-runnable[[github](https://github.com/bmadcode/BMAD-METHOD/tree/main/bmad-agent)]
    
- `amanaiproduct/personal-os` — explicit personal-OS repo pattern, GOALS.md, AGENTS.md, Claude Code compatible, bash-first setup[[github](https://github.com/amanaiproduct/personal-os)]
    
- `itseffi/agentic-os` — personal OS for high-leverage workflows with Claude Code and other runtimes[[github](https://github.com/itseffi/agentic-os)]
    

**best_for_project_execution_repos:**

- `Aider-AI/aider` — 46.8k ★, terminal-native, Git-aware, every change = discrete commit, repo-map for full codebase context; teach Git-backed execution state[[theaiagentindex](https://theaiagentindex.com/agents/aider)]
    
- `princeton-nlp/SWE-agent` — 19.6k ★, issue→fix loop pattern, ACIformat (agent-computer interface), MIT, useful for understanding task→execution→validation loops[[enterprisedna](https://enterprisedna.co/directories/open-source/swe-agent/)]
    

**best_for_knowledge_base_and_memory:**

- `shanraisshan/claude-code-best-practice` — `.claude/rules/` hierarchy, auto-memory, conditional `important_if` tags, 200-line-per-file discipline[[youtube](https://www.youtube.com/watch?v=9rgDMm8QUIg)]
    
- `hesreallyhim/awesome-claude-code` — curated list including KB/memory patterns, hooks, skills, session management resources[[gitstar.co](https://www.gitstar.co.kr/hesreallyhim/awesome-claude-code)]
    

**best_to_avoid:**

- `OpenHands/OpenHands` — 70k ★, Docker/Kubernetes-required, enterprise-scale, VC-backed, multi-tenant; local solo use is officially supported but architecturally complex[[tekai](https://tekai.dev/references/2026-04-03-openhands-open-platform-cloud-coding-agents)][[youtube](https://www.youtube.com/watch?v=t-MnWuuqB-k)]
    
- `crewAIInc/crewAI` — 53k ★, framework-abstract, Python SDK-heavy, shifting to runtime backends; too much indirection for file-native Apex workflows[[linkedin](https://www.linkedin.com/posts/s-gopi_crewai-agenticai-opensourceai-activity-7471522861929795584-VYB3)]
    

---

## 6.2 Ranked Table

|Rank|Repo/System|Stars|Category|Copyability|Local Viability|Orch. Relevance|Repo Structure Value|Token-Cost Fit|Resilience|Maturity|Apex Fit|Main Usefulness|Main Risk|Verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|1|[shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)|61.6k|Claude Code layout|★★★★★|★★★★★|★★★★☆|★★★★★|★★★★★|★★★☆☆|★★★★★|★★★★★|Drop-in `.claude/` files, 16 agent frontmatter fields, command→agent→skill pattern|No session/planning layer|**Must download**|
|2|[hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)|47.6k|Curated index|★★★★☆|★★★★★|★★★★☆|★★★★☆|★★★★★|★★☆☆☆|★★★★★|★★★★★|Discovery hub for all CC patterns, hooks, orchestrators, skills|Curation only, no own architecture|**Must read**|
|3|[bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD)|36.2k|Agentic methodology|★★★★☆|★★★★☆|★★★★★|★★★★★|★★★★☆|★★★★☆|★★★★★|★★★★★|Orchestrator→agent→task chain, story/epic/sprint workflow, multi-platform|Can be verbose, some IDE-coupling|**Must study**|
|4|[Aider-AI/aider](https://github.com/Aider-AI/aider)|46.8k|Coding execution|★★★★☆|★★★★★|★★★☆☆|★★★☆☆|★★★★★|★★★★★|★★★★★|★★★☆☆|Git-commit-per-change, repo-map, BYOK, terminal-native|Not orchestration-native, no planning|**Study Git-state patterns**|
|5|[jeremylongshore/claude-code-plugins-plus-skills](https://github.com/jeremylongshore/claude-code-plugins-plus-skills)|~2.4k|Plugin/skill library|★★★★★|★★★★★|★★★☆☆|★★★★★|★★★★★|★★☆☆☆|★★★★☆|★★★★☆|425 plugins, 200 agents, ccpi installer, tonsofskills.com|Plugin quantity over system design|**Mine for components**|
|6|[dl-ezo/claude-code-sub-agents](https://github.com/dl-ezo/claude-code-sub-agents)|~500|Subagent collection|★★★★★|★★★★★|★★★☆☆|★★★★☆|★★★★★|★★☆☆☆|★★★☆☆|★★★★☆|35 specialized subagents, end-to-end software dev automation|Small community, no orchestration layer|**Copy agent templates**|
|7|[0xfurai/claude-code-subagents](https://github.com/0xfurai/claude-code-subagents)|~800|Subagent collection|★★★★★|★★★★★|★★★☆☆|★★★★☆|★★★★★|★★☆☆☆|★★★☆☆|★★★★☆|100+ production subagents, broad coverage|Quantity, not system design|**Mine for agent specs**|
|8|[amanaiproduct/personal-os](https://github.com/amanaiproduct/personal-os)|Low|Personal OS|★★★★★|★★★★★|★★★★☆|★★★★☆|★★★★★|★★★☆☆|★★☆☆☆|★★★★★|GOALS.md, AGENTS.md, bash-first, 2-min setup, directly Apex-analogous|Low stars, low community validation|**Directly copy structure**|
|9|[itseffi/agentic-os](https://github.com/itseffi/agentic-os)|Low|Personal OS|★★★★☆|★★★★★|★★★★☆|★★★☆☆|★★★★☆|★★★☆☆|★★☆☆☆|★★★★☆|Personal OS for high-leverage workflows, multi-runtime|Unverified structure, small|**Inspect + extract**|
|10|[princeton-nlp/SWE-agent](https://github.com/princeton-nlp/SWE-agent)|19.6k|Coding agent|★★★☆☆|★★★★☆|★★★★☆|★★★☆☆|★★★★☆|★★★★☆|★★★★★|★★★☆☆|ACI pattern, issue→fix→validate loop, structured tool calls|Research-oriented, not daily workflow|**Study ACI + validation**|
|11|[iannuttall/claude-agents](https://github.com/iannuttall/claude-agents)|Low|Subagent collection|★★★★★|★★★★★|★★★☆☆|★★★★★|★★★★★|★★☆☆☆|★★★☆☆|★★★★☆|Clean minimal agent templates, project + global install pattern|7 agents only|**Copy install pattern**|
|12|[24601/BMAD-AT-CLAUDE](https://github.com/24601/BMAD-AT-CLAUDE)|Low|BMAD port|★★★★☆|★★★★★|★★★★☆|★★★★☆|★★★★☆|★★★☆☆|★★★☆☆|★★★★☆|BMAD ported to Claude Code specifically|Derivative, small community|**Check for CC-specific adaptations**|
|13|[OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)|70k+|Full agent platform|★★☆☆☆|★★★☆☆|★★★★★|★★★☆☆|★★☆☆☆|★★★★★|★★★★★|★★☆☆☆|Architecture reference, sandbox patterns|Docker-required, enterprise-scale|**Architecture study only**|
|14|[crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)|53k|Agent framework|★★☆☆☆|★★★★☆|★★★★☆|★★★☆☆|★★★☆☆|★★★★☆|★★★★★|★★★☆☆|Role-based crew orchestration, routing patterns|SDK-heavy, not file-native|**Study role/routing patterns**|
|15|[zhsama/claude-sub-agent](https://github.com/zhsama/claude-sub-agent)|Low|Workflow system|★★★★☆|★★★★★|★★★★☆|★★★★☆|★★★★★|★★★☆☆|★★★☆☆|★★★★☆|AI-driven dev workflow on CC subagents, spec→build pattern|Small, unverified|**Inspect workflow chain**|

---

## 6.3 Detailed Candidate Profiles (Top 6)

## 1. shanraisshan/claude-code-best-practice

text

`repo: shanraisshan/claude-code-best-practice url: https://github.com/shanraisshan/claude-code-best-practice stars: 61,600 last_updated: active (Jun 2026) license: unspecified category: Claude Code layout + methodology what_it_is: >   Comprehensive reference repo maintained by a Claude Certified Architect.  Documents every Claude Code feature with real implementation files. why_it_matters: >   The single densest source of verified .claude/ file patterns, agent  frontmatter fields, command→agent→skill orchestration, memory hierarchy,  and settings. Includes Boris Cherney's (Anthropic) 13 pro tips. repo_structure_observed:   - .claude/agents/[name].md (5 official + custom templates)  - .claude/commands/ (70+ slash commands)  - .claude/rules/ (memory hierarchy, conditional important_if tags)  - .claude/skills/[name]/skill.md (context forking)  - .mcp.json + .claude/settings.json  - CLAUDE.md  - best-practice/ docs per feature  - implementation/ drop-in files  - orchestration/ SVG diagrams + working weather demo  - tips/ + reports/ copyable_patterns:   - pattern: command→agent→skill chain    how_apex_could_use: /apex_weekly → orchestrator-agent → session-skill  - pattern: .claude/rules/ with 200-line limit + conditional tags    how_apex_could_use: Per-project CLAUDE.md + cross-project Apex rules  - pattern: agent frontmatter (model, maxTurns, permissionMode, tools)    how_apex_could_use: Each Apex subagent (KB, Sync, Plan, Session) gets own spec  - pattern: auto-memory writes to .claude/rules/    how_apex_could_use: Session learnings auto-persisted to KB cost_token_assessment: All patterns token-conservative; maxTurns field prevents runaway local_setup_assessment: Zero infra; copy files, run claude limitations: No session logging, no planning/sync layer, no weekly workflow risk_flags: [] final_score: 5/5`

## 2. hesreallyhim/awesome-claude-code

text

`repo: hesreallyhim/awesome-claude-code url: https://github.com/hesreallyhim/awesome-claude-code stars: 47,600 last_updated: active (weekly pushes as of Jun 2026) license: CC0-1.0 category: Curated index what_it_is: >   Community-maintained curated list of skills, hooks, commands,  agent orchestrators, apps, and plugins for Claude Code. why_it_matters: >   Best discovery hub. Points to dozens of real working repos with  concrete .claude/ layouts. Second repo (awesome-claude-code-agents)  specifically for subagents. copyable_patterns:   - pattern: Hooks catalog → PreToolUse, PostToolUse, Notification    how_apex_could_use: Apex sync hooks, session-open/close hooks  - pattern: Orchestrator listings with architecture notes    how_apex_could_use: Pick orchestration pattern for Apex central repo cost_token_assessment: Index only; zero token cost to use local_setup_assessment: Read-only reference limitations: Curation, not own architecture; link rot possible risk_flags: [no_real_repo_patterns_itself] final_score: 4.5/5`

## 3. bmad-code-org/BMAD-METHOD

text

`repo: bmad-code-org/BMAD-METHOD url: https://github.com/bmad-code-org/BMAD-METHOD stars: 36,200 last_updated: Feb 2026 license: MIT category: Agentic methodology + orchestration what_it_is: >   Breakthrough Method for Agile AI-Driven Development. Full framework:  orchestrator agent, role-based team agents, story/epic/task workflow,  multi-platform (Claude Code, Cursor, Cline, Copilot). why_it_matters: >   Only repo with a complete orchestrator→analyst→architect→dev→QA chain  with real markdown agent files, workflow templates, and team configs.  V6 adds cross-platform subagent support. repo_structure_observed:   - bmad-core/agents/ (orchestrator, analyst, architect, dev, QA, PM)  - bmad-core/tasks/ (per-task workflow docs)  - bmad-core/templates/ (story, epic, architecture templates)  - bmad-core/workflows/ (create-story, dev-story, code-review)  - dist/teams/team-fullstack.txt (bundled team configs)  - docs/ (user-guide, tutorials)  - .claude/agents/ (Claude Code subagent versions) copyable_patterns:   - pattern: bmad-orchestrator.md routes tasks to specialized agents    how_apex_could_use: apex-orchestrator.md routes to KB/Sync/Plan/Session agents  - pattern: Story template: goal→tasks→acceptance-criteria    how_apex_could_use: Apex session spec template  - pattern: dist/teams/ bundled configs    how_apex_could_use: Apex dist/ with pre-bundled agent team for project type cost_token_assessment: Designed for solo dev; orchestrator dispatches selectively local_setup_assessment: Markdown files only; paste into .claude/agents/ limitations: Some complexity from multi-platform support; can over-engineer simple tasks risk_flags: [] final_score: 4.5/5`

## 4. Aider-AI/aider

text

`repo: Aider-AI/aider url: https://github.com/Aider-AI/aider stars: 46,800 last_updated: active 2026 license: Apache 2.0 category: Git-native coding execution what_it_is: >   Terminal AI pair programmer. Every LLM change → discrete Git commit.  Repo-map gives LLM architectural context across entire codebase.  BYOK, 100+ LLMs, $5-50/month typical cost. copyable_patterns:   - pattern: Every action = Git commit (atomic, reversible)    how_apex_could_use: Apex session executor commits per task step; rollback on failure  - pattern: Repo-map = LLM sees full codebase structure    how_apex_could_use: Apex project index = synthetic repo-map per project  - pattern: --yes flag for autonomous mode vs confirmation mode    how_apex_could_use: Apex session permission levels (auto vs supervised) local_setup_assessment: pip install aider-chat; runs anywhere limitations: Not orchestration-native; no planning, routing, or session management risk_flags: [] final_score: 3.5/5 for Apex (4.5/5 as execution tool)`

## 5. amanaiproduct/personal-os

text

`repo: amanaiproduct/personal-os url: https://github.com/amanaiproduct/personal-os stars: low (unverified exact count) last_updated: 2025 license: unspecified category: Personal AI operating system what_it_is: >   Framework for local AI agent-powered task management. Setup via  ./setup.sh: creates workspace dirs, generates GOALS.md from user  questions, copies templates. Works with Claude Code via AGENTS.md. why_it_matters: >   Most directly Apex-analogous open repo found. GOALS.md + AGENTS.md  + workspace dirs = exact pattern Apex needs at central orchestration level. repo_structure_observed:   - GOALS.md (generated from setup questionnaire)  - AGENTS.md (entry point for Claude Code)  - setup.sh  - workspace/ (dirs per project type)  - templates/  - Optional: MCP server (Python 3.10+) copyable_patterns:   - pattern: setup.sh → GOALS.md generation via user Q&A    how_apex_could_use: apex-init.sh bootstraps Apex central repo  - pattern: AGENTS.md as Claude Code entry point    how_apex_could_use: APEX.md = central orchestration entry  - pattern: Bash-first, LLM-assisted second    how_apex_could_use: Deterministic sync/init scripts; LLM only for reasoning tasks cost_token_assessment: Minimal; bash-first reduces LLM calls local_setup_assessment: 2-min setup, no infra limitations: Low community validation; structure unverified beyond README risk_flags: [low_maturity, unverified_file_tree] final_score: 4/5 for Apex fit despite low stars`

## 6. jeremylongshore/claude-code-plugins-plus-skills

text

`repo: jeremylongshore/claude-code-plugins-plus-skills url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills stars: ~2,400 last_updated: active (May 2026) license: MIT category: Plugin/skill/agent library what_it_is: >   425 plugins, 2,810 skills, 200 agents for Claude Code. ccpi CLI package  manager. tonsofskills.com marketplace. All markdown-native. copyable_patterns:   - pattern: ccpi install pattern (install skill by URL or name)    how_apex_could_use: apex-skill-install.sh installs Apex skills to project repos  - pattern: Skill isolation via context forking    how_apex_could_use: Apex session skills fork context to prevent cross-contamination  - pattern: ORCHESTRATION-PATTERN.md in workspace/lab/    how_apex_could_use: Direct template for Apex orchestration spec cost_token_assessment: Markdown-only; zero overhead local_setup_assessment: npm install @intentsolutionsio/ccpi limitations: Volume over coherence; needs curation for Apex use risk_flags: [] final_score: 4/5`

---

## 6.4 Repo Structure Extraction (Confirmed or Partially Confirmed)

## shanraisshan/claude-code-best-practice[[youtube](https://www.youtube.com/watch?v=9rgDMm8QUIg)]

text

`claude-code-best-practice/   .claude/    agents/      general-purpose.md      explore.md      plan.md      status-line.md      claude-code-guide.md      [custom].md    commands/      [70+ slash command .md files]    rules/      [memory hierarchy files, <200 lines each]    skills/      [name]/skill.md    settings.json  .mcp.json  CLAUDE.md  best-practice/    [per-feature docs]  implementation/    [drop-in agent/skill/command files]  orchestration/    [SVG diagrams, weather demo]  tips/  reports/`

**Status: Largely confirmed via YouTube walkthrough and best-practice/claude-subagents.md**[[github](https://github.com/shanraisshan/claude-code-best-practice/blob/main/best-practice/claude-subagents.md)][[youtube](https://www.youtube.com/watch?v=9rgDMm8QUIg)]

## bmad-code-org/BMAD-METHOD[[github](https://github.com/bmadcode/BMAD-METHOD/blob/main/bmad-core/agents/bmad-orchestrator.md)]

text

`BMAD-METHOD/   bmad-core/    agents/      bmad-orchestrator.md      analyst.md      architect.md      dev.md      qa.md      pm.md    tasks/    templates/      story-template.md      epic-template.md    workflows/      create-story.md      dev-story.md      code-review.md  dist/    teams/      team-fullstack.txt      team-minimal.txt  docs/    user-guide.md    tutorials/getting-started.md  .claude/    agents/ [Claude Code subagent versions]`

**Status: Confirmed from directory browsing and search results**

## iannuttall/claude-agents[[github](https://github.com/iannuttall/claude-agents)]

text

`claude-agents/   agents/    code-refactorer.md    content-writer.md    frontend-designer.md    prd-writer.md    project-task-planner.md    security-auditor.md    vibe-coding-coach.md  README.md`

Install: `cp agents/*.md .claude/agents/` or `~/.claude/agents/`  
**Status: Confirmed from README**

## amanaiproduct/personal-os[[github](https://github.com/amanaiproduct/personal-os)]

text

`personal-os/   GOALS.md          [generated]  AGENTS.md         [Claude Code entry point]  setup.sh  workspace/    [dirs per goal/project type]  templates/  [optional mcp_server/]`

**Status: Confirmed from README quick-start**

## dl-ezo/claude-code-sub-agents[[github](https://github.com/dl-ezo/claude-code-sub-agents)]

text

`claude-code-sub-agents/   agents/    [35 .md files for specialized roles]  README.md`

**Status: Partially confirmed (35 agents confirmed, exact filenames unverified)**

---

## 6.5 Apex Mapping

## Apex KB

text

`useful_repos:   - shanraisshan/claude-code-best-practice (.claude/rules/ auto-memory)  - hesreallyhim/awesome-claude-code (hooks for KB update triggers) copyable_patterns:   - .claude/rules/ directory with <200 line files  - conditional important_if tags for context-aware rule loading  - auto-memory: Claude writes to memory files when learning persists recommended_design_moves:   - apex-orchestration/kb/[domain]/[topic].md flat structure  - SQLite FTS5 index (from your prior research files) for retrieval  - CLAUDE.md references KB via !import or glob patterns  - hook on session-close to write learned facts to kb/`

## Apex Sync

text

`useful_repos:   - amanaiproduct/personal-os (setup.sh bash-first pattern)  - Aider-AI/aider (Git-commit-per-action discipline) copyable_patterns:   - Deterministic bash sync scripts (not LLM-driven)  - Git commit every sync action for rollback  - Cross-project index.md maintained by sync script recommended_design_moves:   - apex-sync.sh: deterministic, no LLM; just git pull/push + index rebuild  - LLM only called for conflict resolution, not routine sync  - Sync writes to apex-orchestration/cross-project/index.md`

## Apex Plan

text

`useful_repos:   - bmad-code-org/BMAD-METHOD (story/task/epic templates, PM agent)  - shanraisshan/claude-code-best-practice (plan agent frontmatter) copyable_patterns:   - story-template.md: goal→tasks→acceptance-criteria  - plan subagent with maxTurns limit  - weekly plan = markdown file with session blocks recommended_design_moves:   - apex-orchestration/plans/YYYY-WW.md per week  - BMAD story template adapted as apex-session-spec.md  - Plan agent reads KB + project indices, outputs session specs`

## Apex Session

text

`useful_repos:   - shanraisshan/claude-code-best-practice (command→agent→skill)  - bmad-code-org/BMAD-METHOD (dev-story workflow)  - Aider-AI/aider (atomic commit discipline) copyable_patterns:   - Session spec: goal, context pointers, tools allowed, maxTurns  - Session log: markdown file written during/after execution  - PostToolUse hook writes action to session log recommended_design_moves:   - apex-orchestration/sessions/YYYY-MM-DD-[task].md  - session-open hook: load KB context, write session header  - session-close hook: summarize, update KB, git commit`

## Weekly Workflow

text

`useful_repos:   - bmad-code-org/BMAD-METHOD (full workflow: review→plan→execute→report)  - amanaiproduct/personal-os (GOALS.md drives weekly direction) copyable_patterns:   - Weekly review agent: reads sessions/, plans/, blockers  - Plan update: diff last week vs this week  - Session scheduling: priority-ordered list with pre-loaded prompts recommended_design_moves:   - /apex_weekly command → apex-weekly-agent → runs 5-step workflow  - Output: YYYY-WW-review.md + YYYY-WW-plan.md  - All steps deterministic except LLM-assisted synthesis`

---

## 6.6 Recommended Minimal Apex Architecture

Based on research findings:

text

`apex-orchestration/                    ← Central repo (private)   APEX.md                              ← Entry point for Claude Code (like AGENTS.md)  .claude/    agents/      apex-orchestrator.md             ← Routes tasks to subagents      apex-kb-agent.md                 ← KB query/update      apex-plan-agent.md               ← Weekly planning      apex-session-agent.md            ← Session spec generation      apex-sync-agent.md               ← Repo sync oversight    commands/      apex_weekly.md                   ← /apex_weekly trigger      apex_session.md                  ← /apex_session [task]      apex_sync.md                     ← /apex_sync    rules/      core-principles.md               ← <200 lines      project-index.md                 ← Auto-updated by sync    hooks/      session-open.sh                  ← Load context, write log header      session-close.sh                 ← Summarize, update KB, git commit    settings.json  kb/    [domain]/[topic].md                ← Flat markdown KB    index.db                           ← SQLite FTS5 (deterministic)  plans/    YYYY-WW.md                         ← Weekly plans  sessions/    YYYY-MM-DD-[task].md               ← Session logs  cross-project/    index.md                           ← All project repos, statuses    blockers.md  scripts/    apex-sync.sh                       ← Deterministic, no LLM    apex-init.sh                       ← Bootstrap new project repo    kb-index-rebuild.sh                ← Rebuild SQLite index project-repo/                          ← Per-project (can be many)   .claude/    agents/                            ← Project-specific subagents    commands/                          ← Project-specific commands    rules/      project-context.md               ← Pointers to Apex KB  CLAUDE.md                            ← Project entry, imports from Apex  tasks/    [task-id].md                       ← BMAD-style task specs  logs/    [session-id].md                    ← Execution logs  src/                                 ← Source code  docs/`

**What should be deterministic (no LLM):**

- `apex-sync.sh` — git pull/push, index rebuild, file moves
    
- `kb-index-rebuild.sh` — FTS5 rebuild from markdown files
    
- Session log headers/footers (templated)
    
- Git commits after each session
    

**What should be LLM-assisted:**

- Weekly review synthesis
    
- Session spec generation from task description + KB context
    
- KB update decisions (what to persist)
    
- Conflict resolution during sync
    
- Cross-project dependency detection
    

**Session log model:**

text

`# Session: [task-id] — YYYY-MM-DD ## Goal ## Context loaded (KB refs) ## Actions - [timestamp] [tool] [result] ## Outcome ## KB updates ## Next session seeds`

**What to avoid:**

- Long-running autonomous loops without maxTurns
    
- Storing session state in LLM context (use files)
    
- LLM-driven sync (always deterministic scripts)
    
- One giant CLAUDE.md (use modular .claude/rules/ files <200 lines each)
    

---

## 6.7 Source Download Manifest

text

`sources:   - name: claude-code-best-practice    url: https://github.com/shanraisshan/claude-code-best-practice    type: github_repo    priority: 1    why: Most complete .claude/ layout with real implementation files, 61.6k stars    recommended_download:      method: git_clone      include_paths:        - .claude/        - CLAUDE.md        - best-practice/        - implementation/        - orchestration/      exclude_paths:        - .git/        - node_modules/    apex_component_fit:      - Apex KB      - Apex Session      - Apex Plan      - Weekly Workflow   - name: BMAD-METHOD    url: https://github.com/bmad-code-org/BMAD-METHOD    type: github_repo    priority: 1    why: Only complete orchestrator→agent→task chain with copyable markdown files    recommended_download:      method: git_clone      include_paths:        - bmad-core/agents/        - bmad-core/tasks/        - bmad-core/templates/        - bmad-core/workflows/        - dist/teams/        - docs/      exclude_paths:        - .git/        - node_modules/    apex_component_fit:      - Apex Plan      - Apex Session      - Weekly Workflow   - name: awesome-claude-code    url: https://github.com/hesreallyhim/awesome-claude-code    type: github_repo    priority: 2    why: Index of all CC patterns; mine for orchestrator and hooks references    recommended_download:      method: git_clone      include_paths:        - README.md        - CONTRIBUTING.md      exclude_paths:        - .git/    apex_component_fit:      - Apex KB      - Apex Sync      - Apex Session   - name: personal-os    url: https://github.com/amanaiproduct/personal-os    type: github_repo    priority: 2    why: Most Apex-analogous personal OS repo; GOALS.md + AGENTS.md pattern    recommended_download:      method: git_clone      include_paths:        - GOALS.md        - AGENTS.md        - setup.sh        - templates/      exclude_paths:        - .git/    apex_component_fit:      - Apex KB      - Apex Plan      - Weekly Workflow   - name: claude-code-plugins-plus-skills    url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills    type: github_repo    priority: 2    why: 425 plugins, 200 agents; mine for skill/plugin templates and ccpi pattern    recommended_download:      method: git_clone      include_paths:        - workspace/lab/ORCHESTRATION-PATTERN.md        - agents/        - skills/        - plugins/      exclude_paths:        - .git/        - node_modules/    apex_component_fit:      - Apex Session      - Apex KB   - name: iannuttall-claude-agents    url: https://github.com/iannuttall/claude-agents    type: github_repo    priority: 3    why: Minimal clean agent templates with verified install pattern    recommended_download:      method: github_zip      include_paths:        - agents/      exclude_paths: []    apex_component_fit:      - Apex Session   - name: agentic-os    url: https://github.com/itseffi/agentic-os    type: github_repo    priority: 3    why: Personal high-leverage workflow OS; inspect structure    recommended_download:      method: github_zip      include_paths:        - "**"      exclude_paths:        - .git/    apex_component_fit:      - Weekly Workflow      - Apex Sync   - name: BMAD-AT-CLAUDE    url: https://github.com/24601/BMAD-AT-CLAUDE    type: github_repo    priority: 3    why: BMAD ported specifically to Claude Code; check for CC-specific adaptations    recommended_download:      method: github_zip      include_paths:        - "**"      exclude_paths:        - .git/    apex_component_fit:      - Apex Plan      - Apex Session   - name: aider    url: https://github.com/Aider-AI/aider    type: github_repo    priority: 3    why: Study Git-commit-per-action discipline and repo-map concept    recommended_download:      method: jina_reader      include_paths:        - docs/        - CONVENTIONS.md        - README.md      exclude_paths:        - .git/        - aider/    apex_component_fit:      - Apex Sync      - Apex Session   - name: SWE-agent    url: https://github.com/princeton-nlp/SWE-agent    type: github_repo    priority: 4    why: ACI pattern and issue→fix→validate loop; architecture study    recommended_download:      method: jina_reader      include_paths:        - docs/        - README.md      exclude_paths:        - .git/        - sweagent/    apex_component_fit:      - Apex Session`

---

## 6.8 Final Recommendation

text

`recommended_next_actions:   - Clone shanraisshan/claude-code-best-practice; extract .claude/ as Apex template base  - Clone BMAD-METHOD; adapt bmad-orchestrator.md as apex-orchestrator.md  - Clone amanaiproduct/personal-os; adapt GOALS.md + AGENTS.md → APEX.md pattern  - Build apex-sync.sh as pure bash (no LLM); test git-backed sync first  - Implement hooks: session-open.sh writes log header; session-close.sh commits + KB update  - Set maxTurns on all Apex subagents to prevent runaway sessions  - Use ccpi (jeremylongshore) to install specific skills into project repos on demand  - Do NOT implement planning, routing, or KB updates as LLM-autonomous loops; keep deterministic top_5_to_download_first:   - shanraisshan/claude-code-best-practice  - bmad-code-org/BMAD-METHOD  - amanaiproduct/personal-os  - jeremylongshore/claude-code-plugins-plus-skills  - iannuttall/claude-agents top_5_to_read_first:   - shanraisshan/claude-code-best-practice README + orchestration/ SVG  - bmad-code-org/BMAD-METHOD docs/user-guide.md  - hesreallyhim/awesome-claude-code README (hooks + orchestrators sections)  - amanaiproduct/personal-os README (setup flow)  - shanraisshan/claude-code-best-practice best-practice/claude-subagents.md (frontmatter fields) top_5_patterns_to_copy:   - command→agent→skill chain (shanraisshan): /apex_weekly → apex-orchestrator → session-skill  - BMAD story template: goal→tasks→acceptance-criteria → adapt as apex-session-spec.md  - .claude/rules/ with <200 line files + conditional important_if tags  - Git-commit-per-action discipline (Aider pattern) → apex-sync.sh atomic commits  - GOALS.md + AGENTS.md personal OS entry pattern (personal-os) → APEX.md central entry`