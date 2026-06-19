I ran the discovery sweep and then deep-dived the serious candidates against your hard filters. **Verdict up front:** **Backlog.md is the best pure fit** for a Claude Code operator who wants repo-resident, flat-file project/task state. **GSD Core** is the strongest execution/context-engineering companion, and **Task Master AI** has the largest adoption but is less cleanly aligned with a `.claude/skills/` architecture.

## 1. Full Ranked Table

|Rank|System|GitHub stars + forks|Last meaningful commit / activity|How it stores data|Skill / `CLAUDE.md` compatible?|Independent community evidence|Known limitations|
|--:|---|--:|---|---|---|---|---|
|**1**|**Backlog.md**|~**5.7k–5.8k stars**, ~**343–346 forks**|Active in **June 2026**; search result showed latest commit within the last day / hour depending snapshot. ([GitHub](https://github.com/MrLesk/Backlog.md/?utm_source=chatgpt.com "GitHub - MrLesk/Backlog.md: Backlog.md - A tool for managing project ..."))|Plain Markdown task files inside the Git repo; explicitly marketed as “self-contained project board” for any Git folder. ([GitHub](https://github.com/MrLesk/Backlog.md/?utm_source=chatgpt.com "GitHub - MrLesk/Backlog.md: Backlog.md - A tool for managing project ..."))|**Yes.** Has Claude Code skill / MCP support and references to `.claude` integration. ([MCP Market](https://mcpmarket.com/tools/skills/backlog-md-quick-reference?utm_source=chatgpt.com "Backlog.md Quick Reference \| Claude Code Workflow Skill"))|Hacker News discussion, blogs, and tutorials describe real use with repo-stored Markdown tasks. ([news.ycombinator.com](https://news.ycombinator.com/item?id=44483530&utm_source=chatgpt.com "Backlog.md – Markdown‑native Task Manager and Kanban visualizer for any ..."))|CLI/MCP layer adds setup surface; issue tracker shows active bugs and workflow friction. Best as a project/task substrate, not a full multi-agent scheduler.|
|**2**|**GSD Core / open-gsd**|Current `open-gsd/gsd-core`: ~**4.3k stars**, ~**270 forks**; legacy `gsd-build/get-shit-done` shows much larger historical adoption but is no longer active home. ([GitHub](https://github.com/open-gsd/gsd-core/tree/next/gsd-core?utm_source=chatgpt.com "gsd-core/gsd-core at next · open-gsd/gsd-core · GitHub"))|Active 2026; current development moved to `open-gsd`. ([GitHub](https://github.com/open-gsd/gsd-core/blob/next/README.md?utm_source=chatgpt.com "gsd-core/README.md at next · open-gsd/gsd-core · GitHub"))|Human-readable planning artifacts such as `STATE.md`, `CONTEXT.md`, and `.planning/` survive session boundaries. ([GitHub](https://github.com/open-gsd/gsd-core?utm_source=chatgpt.com "GitHub - open-gsd/gsd-core: Git. Ship. Done - Core · GitHub"))|**Yes.** Designed around Claude Code slash commands, agents, hooks, and persistent Markdown state. ([codecentric AG](https://www.codecentric.de/en/knowledge-hub/blog/the-anatomy-of-claude-code-workflows-turning-slash-commands-into-an-ai-development-system?utm_source=chatgpt.com "GSD for Claude Code: A Deep Dive into the Workflow System"))|Independent deep dives from Codecentric, The New Stack, Starlog, and setup walkthroughs. ([codecentric AG](https://www.codecentric.de/en/knowledge-hub/blog/the-anatomy-of-claude-code-workflows-turning-slash-commands-into-an-ai-development-system?utm_source=chatgpt.com "GSD for Claude Code: A Deep Dive into the Workflow System"))|More of a context-engineering / execution framework than a conventional backlog. Governance/migration history is a real caveat. ([GitHub](https://github.com/open-gsd/gsd-core/blob/next/README.md?utm_source=chatgpt.com "gsd-core/README.md at next · open-gsd/gsd-core · GitHub"))|
|**3**|**Task Master AI / `claude-task-master`**|~**27.6k stars**, ~**2.6k forks**. ([GitHub](https://github.com/eyaltoledano/claude-task-master "GitHub - eyaltoledano/claude-task-master: An AI-powered task-management system you can drop into Cursor, Lovable, Windsurf, Roo, and others. · GitHub"))|Release `task-master-ai@0.43.1` on **Mar 31, 2026**. ([GitHub](https://github.com/eyaltoledano/claude-task-master "GitHub - eyaltoledano/claude-task-master: An AI-powered task-management system you can drop into Cursor, Lovable, Windsurf, Roo, and others. · GitHub"))|Local mode uses `.taskmaster/docs/prd.txt`, `tasks.json`, and generated task files. ([GitHub](https://github.com/eyaltoledano/claude-task-master/blob/main/docs/tutorial.md "claude-task-master/docs/tutorial.md at main · eyaltoledano/claude-task-master · GitHub"))|**Yes, with caveat.** Supports Claude Code MCP and Claude Code CLI models; API keys can be avoided when using Claude Code CLI models. ([GitHub](https://github.com/eyaltoledano/claude-task-master "GitHub - eyaltoledano/claude-task-master: An AI-powered task-management system you can drop into Cursor, Lovable, Windsurf, Roo, and others. · GitHub"))|Multiple independent tutorials and registry/writeups. ([pageai.pro](https://pageai.pro/blog/claude-code-taskmaster-ai-tutorial?utm_source=chatgpt.com "How to set up TaskMaster AI in Claude Code - pageai.pro"))|Best in solo/local mode. Team/cloud mode and MCP/API-provider complexity weaken the “zero external infrastructure” purity. Single `tasks.json` can be more merge-conflict-prone than per-task Markdown.|
|**4**|**CCPM / Claude Code PM**|~**8.2k stars**, ~**833 forks**. ([GitHub](https://github.com/automazeio/ccpm "GitHub - automazeio/ccpm: Project management skill system for Agents that uses GitHub Issues and Git worktrees for parallel agent execution. · GitHub"))|Evidence shows active 2025–2026 ecosystem; exact latest commit date was not reliably exposed in fetched GitHub page.|`.claude/prds`, `.claude/epics`, `epic.md`, per-task Markdown files; README says local files are source of truth. ([GitHub](https://github.com/automazeio/ccpm "GitHub - automazeio/ccpm: Project management skill system for Agents that uses GitHub Issues and Git worktrees for parallel agent execution. · GitHub"))|**Very strong.** Built directly around `.claude/` project files and Claude Code PM workflows. ([GitHub](https://github.com/automazeio/ccpm "GitHub - automazeio/ccpm: Project management skill system for Agents that uses GitHub Issues and Git worktrees for parallel agent execution. · GitHub"))|HN, DeepWiki, project writeups, and independent reviews/tutorials exist. ([news.ycombinator.com](https://news.ycombinator.com/item?id=44960594&utm_source=chatgpt.com "Show HN: Project management system for Claude Code \| Hacker News"))|Heavy GitHub Issues / `gh` / worktree workflow. Great for GitHub-native teams, less pure if GitHub Issues becomes operational state instead of mirror.|
|**5**|**Claude-Code-Workflow / CCW**|~**2.1k stars**, ~**167 forks**. ([GitHub](https://github.com/catlog22/Claude-Code-Workflow "GitHub - catlog22/Claude-Code-Workflow: JSON-driven multi-agent  cadence-team development framework with   intelligent CLI orchestration (Gemini/Qwen/Codex),   context-first architecture, and automated workflow   execution · GitHub"))|Latest release shown as **v7.3.14, May 5, 2026**. ([GitHub](https://github.com/catlog22/Claude-Code-Workflow "GitHub - catlog22/Claude-Code-Workflow: JSON-driven multi-agent  cadence-team development framework with   intelligent CLI orchestration (Gemini/Qwen/Codex),   context-first architecture, and automated workflow   execution · GitHub"))|JSON-first state in `.task/IMPL-*.json` as source of truth. ([npmjs.com](https://www.npmjs.com/package/claude-code-workflow?utm_source=chatgpt.com "claude-code-workflow - npm"))|**Yes, but broader than Claude Code.** Multi-CLI orchestration, skills, queues, dashboards, dependency graphs. ([GitHub](https://github.com/catlog22/Claude-Code-Workflow "GitHub - catlog22/Claude-Code-Workflow: JSON-driven multi-agent  cadence-team development framework with   intelligent CLI orchestration (Gemini/Qwen/Codex),   context-first architecture, and automated workflow   execution · GitHub"))|DeepWiki/docs and third-party comparisons exist. ([DeepWiki](https://deepwiki.com/catlog22/Claude-Code-Workflow/2.3-quick-start-tutorial?utm_source=chatgpt.com "Quick Start Tutorial \| catlog22/Claude-Code-Workflow \| DeepWiki"))|Powerful but heavy. More workflow-orchestration suite than simple project manager; multi-CLI assumptions may be overkill.|
|**6**|**claude-mpm**|~**135 stars**, ~**30 forks**. ([GitHub](https://github.com/bobmatnyc/claude-mpm "GitHub - bobmatnyc/claude-mpm: Claude Multi-Agent Project Manager — multi-channel orchestration, GitHub-first SDK mode, and plugin system for Claude · GitHub"))|Release **v6.5.45 on Jun 17, 2026**. ([GitHub](https://github.com/bobmatnyc/claude-mpm "GitHub - bobmatnyc/claude-mpm: Claude Multi-Agent Project Manager — multi-channel orchestration, GitHub-first SDK mode, and plugin system for Claude · GitHub"))|Has project memory/session concepts, but not clearly a repo-resident flat-file task PM system end-to-end. ([GitHub](https://github.com/bobmatnyc/claude-mpm "GitHub - bobmatnyc/claude-mpm: Claude Multi-Agent Project Manager — multi-channel orchestration, GitHub-first SDK mode, and plugin system for Claude · GitHub"))|**Yes for Claude Code orchestration**, agents, skills, MCP, and session management. ([GitHub](https://github.com/bobmatnyc/claude-mpm "GitHub - bobmatnyc/claude-mpm: Claude Multi-Agent Project Manager — multi-channel orchestration, GitHub-first SDK mode, and plugin system for Claude · GitHub"))|Mostly package/docs ecosystem; I found weaker independent tutorial/review evidence than the top systems. ([PyPI](https://pypi.org/project/claude-mpm/?utm_source=chatgpt.com "claude-mpm · PyPI"))|**Does not win.** It is a broader multi-agent platform, not the cleanest file-based PM layer. Recommended memory/search and external integrations reduce the “flat-files only” confidence. ([GitHub](https://github.com/bobmatnyc/claude-mpm "GitHub - bobmatnyc/claude-mpm: Claude Multi-Agent Project Manager — multi-channel orchestration, GitHub-first SDK mode, and plugin system for Claude · GitHub"))|

### Explicit exclusions

|System|Why excluded|
|---|---|
|**Vibe Kanban**|Strong adoption, but uses SQLite / database layer and the project/company status changed; violates the flat-file/no-database requirement. ([DeepWiki](https://deepwiki.com/BloopAI/vibe-kanban/4.5-database-models-and-queries?utm_source=chatgpt.com "Database Models and Queries \| BloopAI/vibe-kanban \| DeepWiki"))|
|**Claude Code Kanban**|Stores task files under `~/.claude/tasks/` and logs under `~/.claude/projects/`, not repo-resident project files; only ~27 stars / 7 forks, so unproven. ([GitHub](https://github.com/NikiforovAll/claude-code-kanban "GitHub - NikiforovAll/claude-code-kanban: A web-based Kanban Board & Agent Orchestration · GitHub"))|
|**Claude Cadence**|Very low adoption in found evidence and includes optional issue microservice/MCP/dev-stack assumptions; fails the independent evidence bar. ([GitHub](https://github.com/dokipen/claude-cadence "GitHub - dokipen/claude-cadence · GitHub"))|
|**OpenSpec / Spec Kit / Superpowers**|Useful spec or skill frameworks, but not complete Claude Code project/task management systems under your flat-file PM criteria. ([openspec.dev](https://openspec.dev/?utm_source=chatgpt.com "OpenSpec — A lightweight spec‑driven framework"))|

---

## 2. Top 3 in Detail

## 1. Backlog.md — best pure project/task layer

**Feature summary:** Backlog.md turns a Git repo into a Markdown-backed project board with CLI/MCP/Claude integrations. Its core advantage is that project state is ordinary repo content, not a side database. ([GitHub](https://github.com/MrLesk/Backlog.md/?utm_source=chatgpt.com "GitHub - MrLesk/Backlog.md: Backlog.md - A tool for managing project ..."))

**What it does well**

- **File-based fit:** Best match to your hard requirements. It uses Markdown files in the repo and is built around Git-native collaboration.
    
- **Claude Code compatibility:** Has a Claude Code skill and MCP path, so it can be operated by Claude without forcing a SaaS backend. ([MCP Market](https://mcpmarket.com/tools/skills/backlog-md-quick-reference?utm_source=chatgpt.com "Backlog.md Quick Reference | Claude Code Workflow Skill"))
    
- **Community evidence:** It has independent discussion and tutorials, not just the author README. ([news.ycombinator.com](https://news.ycombinator.com/item?id=44483530&utm_source=chatgpt.com "Backlog.md – Markdown‑native Task Manager and Kanban visualizer for any ..."))
    
- **Right abstraction:** It behaves like a task/backlog substrate rather than a sprawling agent framework.
    

**What it lacks**

- It is not a full autonomous project manager by itself.
    
- Multi-agent orchestration, worktree isolation, and lifecycle governance need conventions around it.
    
- Claude skill/MCP setup may add friction compared with a pure `CLAUDE.md` workflow.
    

**Best use:** Put Backlog.md at the center of repo task state, then add `.claude/skills/` for Leela-style lifecycle operations: triage, plan, implement, review, update backlog.

---

## 2. GSD Core — best execution/context framework

**Feature summary:** GSD Core is a context-engineering and execution framework for Claude Code. It emphasizes durable Markdown artifacts like `STATE.md`, `CONTEXT.md`, and phase planning so work survives context resets. ([GitHub](https://github.com/open-gsd/gsd-core?utm_source=chatgpt.com "GitHub - open-gsd/gsd-core: Git. Ship. Done - Core · GitHub"))

**What it does well**

- **Claude-native execution:** Strong match for Claude Code slash commands, hooks, subagents, and persistent session artifacts. ([codecentric AG](https://www.codecentric.de/en/knowledge-hub/blog/the-anatomy-of-claude-code-workflows-turning-slash-commands-into-an-ai-development-system?utm_source=chatgpt.com "GSD for Claude Code: A Deep Dive into the Workflow System"))
    
- **Context recovery:** Better than most tools at preserving “where are we and why?” across Claude sessions.
    
- **Independent evidence:** The third-party writeups are unusually substantive. ([codecentric AG](https://www.codecentric.de/en/knowledge-hub/blog/the-anatomy-of-claude-code-workflows-turning-slash-commands-into-an-ai-development-system?utm_source=chatgpt.com "GSD for Claude Code: A Deep Dive into the Workflow System"))
    

**What it lacks**

- It is less of a clean backlog/kanban/task database than Backlog.md.
    
- The project lineage/migration history creates trust and continuity questions. ([GitHub](https://github.com/open-gsd/gsd-core/blob/next/README.md?utm_source=chatgpt.com "gsd-core/README.md at next · open-gsd/gsd-core · GitHub"))
    
- It may impose a heavier process model than a small operator wants.
    

**Best use:** Use GSD as a **Claude execution discipline**, not necessarily as the primary PM database. It pairs well with Backlog.md: Backlog.md owns tasks; GSD owns phase/context execution.

---

## 3. Task Master AI — strongest adoption, less pure architecture

**Feature summary:** Task Master AI parses PRDs into tasks and supports Claude Code via MCP/CLI. It has the strongest adoption metrics of the qualifying tools and supports local file-based state through `.taskmaster` files. ([GitHub](https://github.com/eyaltoledano/claude-task-master "GitHub - eyaltoledano/claude-task-master: An AI-powered task-management system you can drop into Cursor, Lovable, Windsurf, Roo, and others. · GitHub"))

**What it does well**

- **Adoption:** Much larger star/fork base than most alternatives.
    
- **PRD-to-task flow:** Strong for turning product specs into executable tasks.
    
- **Claude Code support:** Explicit Claude Code MCP and CLI-model support. ([GitHub](https://github.com/eyaltoledano/claude-task-master "GitHub - eyaltoledano/claude-task-master: An AI-powered task-management system you can drop into Cursor, Lovable, Windsurf, Roo, and others. · GitHub"))
    
- **Tutorial coverage:** More independent tutorials than most smaller tools. ([pageai.pro](https://pageai.pro/blog/claude-code-taskmaster-ai-tutorial?utm_source=chatgpt.com "How to set up TaskMaster AI in Claude Code - pageai.pro"))
    

**What it lacks**

- The cleanest mode is local/solo. Team/cloud mode weakens the “zero infra” guarantee. ([DeepWiki](https://deepwiki.com/eyaltoledano/claude-task-master "eyaltoledano/claude-task-master | DeepWiki"))
    
- `.taskmaster/tasks/tasks.json` is less pleasant for Git review than one Markdown file per task.
    
- It is not naturally a `.claude/skills/` architecture; it is a parallel `.taskmaster/` architecture.
    

**Best use:** Good if PRD decomposition is the main job. Less ideal if you want human-readable Markdown task state and Claude skills as the central architecture.

---

## 3. Open Gaps

No found system fully nails all of these at once:

|Gap|Why it matters|
|---|---|
|**Repo-native PM + rich visual board without a database**|Visual kanban tools tend to introduce SQLite, web servers, or local app state.|
|**Conflict-safe multi-agent task editing**|JSON single-file stores risk merge conflicts; Markdown-per-task is better but still needs locking/ownership conventions.|
|**Standard `.claude/skills/` lifecycle contract**|Tools invent their own structures: `.taskmaster/`, `.planning/`, `.claude/epics/`, `backlog/`.|
|**Backlog + execution + review in one clean system**|Backlog.md is great at tasks; GSD is great at execution context; CCPM is strong for GitHub issue/worktree flow. None is perfect alone.|
|**High-quality independent evidence**|Many Claude Code tools are new, fast-moving, and documented mostly by authors or auto-generated directories.|
|**Infrastructure-free collaboration at scale**|Git alone works, but concurrent agents and humans need ownership, locking, and review rules. Most tools only partially address this.|

---

## 4. Verdict

**Best option:** **Backlog.md**.

**Confidence:** **82 / 100**.

**Why:** It best satisfies the hard requirements simultaneously: Claude-compatible, flat-file repo state, no mandatory database/SaaS, active in 2026, substantial adoption, and independent community evidence. It is also the least distorted by external assumptions: no mandatory GitHub Issues, no cloud team mode, no SQLite, no hosted backend. ([GitHub](https://github.com/MrLesk/Backlog.md/?utm_source=chatgpt.com "GitHub - MrLesk/Backlog.md: Backlog.md - A tool for managing project ..."))

**For a repo-resident `.claude/skills/` architecture, I would use:**

```text
repo/
  .claude/
    CLAUDE.md
    skills/
      backlog-triage/
      backlog-plan/
      backlog-implement/
      backlog-review/
      backlog-update/
  backlog/
    tasks/
    docs/
    decisions/
```

**Recommended operating model:**

|Layer|Best tool|
|---|---|
|**Canonical task/project state**|**Backlog.md**|
|**Claude execution discipline**|GSD-style `STATE.md` / `CONTEXT.md` conventions|
|**PRD-to-task decomposition when needed**|Borrow Task Master AI patterns, but avoid making `.taskmaster/tasks.json` the canonical source|
|**GitHub issue mirroring**|Optional CCPM-like mirror, not source of truth|

**claude-mpm does not win on merit.** It is current and Claude Code-oriented, but the evidence points to a broader multi-agent/session platform rather than the best flat-file project management system. Its small adoption and external memory/search/integration surface make it weaker for your exact requirements.