# Sources Registry: Master of Arts Integrated Agent Operating System

Researcher ID: gemini-deep-research  
Date: 2026-08-21  
Scope Reference: leela-spec/MasterOfArts@main (b4dceb5)

---

| Source ID | Candidate / Technology | Claim / Capability | Source Type | Date / Version | URL | Verification Notes |
|---|---|---|---|---|---|---|
| SRC-SPEC-01 | GitHub Spec Kit | Workflow engine: commands, prompts, shell steps, human gates, conditionals, loops, fan-out/fan-in | P1 | 2026-04 / v0.5+ | https://github.com/github/spec-kit/blob/main/docs/reference/workflows.md | Official workflow specification showing JSON state persistence and step resume |
| SRC-SPEC-02 | GitHub Spec Kit | 35+ Assistant integrations (Claude Code, Codex CLI, Antigravity, etc.) | P1 | 2026-04 / v0.5+ | https://github.com/github/spec-kit/blob/main/docs/reference/integrations.md | Official CLI integration reference |
| SRC-SPEC-03 | GitHub Spec Kit | 	askstoissues template: turns dependency-ordered task markdown into GitHub Issues | P1 | 2026-04 | https://github.com/github/spec-kit/blob/main/templates/commands/taskstoissues.md | Official command for bridge between workflow tasks and GitHub Issues |
| SRC-SPEC-04 | GitHub Spec Kit | Fiction Book Writing preset (non-software multi-stage writing workflow) | P2 | 2026-03 | https://github.com/github/spec-kit/blob/main/docs/community/presets.md | Proof of non-software business/creative workflow adaptation |
| SRC-SPEC-05 | GitHub Spec Kit | Workflow state architecture: .specify/workflows/runs/<run_id>/ (state.json, inputs.json, log.jsonl) | P1 | 2026-04 | https://github.com/github/spec-kit/blob/main/workflows/ARCHITECTURE.md | Confirms machine-readable state persistence and crash recovery |
| SRC-GH-01 | GitHub Projects | Custom fields, table/board/roadmap views, automation, and project templates | P1 | 2026-08 | https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects | Official GitHub Projects documentation |
| SRC-GH-02 | GitHub Issues | Blocking dependencies (locked by / locking) and sub-issue hierarchies | P1 | 2026-08 | https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-issue-dependencies | Native portfolio dependency graph support |
| SRC-GH-03 | GitHub Issues | Sub-issues hierarchy navigation and machine CLI queries | P1 | 2026-08 | https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/browsing-sub-issues | Native hierarchical breakdown of complex projects |
| SRC-SKILL-01| Agent Skills | Open SKILL.md specification: progressive disclosure, scripts, references, assets | P1 | 2026-02 / v1.0 | https://agentskills.io/specification | Portable multi-executor skill format supported by Codex, Claude Code, Antigravity |
| SRC-SKILL-02| OpenAI Skills | OpenAI Agent Skills adoption in Codex CLI and ChatGPT | P1 | 2026-03 | https://openai.com/academy/skills/ | Confirms standard skill portability across ChatGPT/Codex |
| SRC-BEADS-01| Beads | Dolt-backed distributed graph issue tracker: d ready, atomic claim, dependencies | P1 | 2026-08 / v0.4+ | https://github.com/gastownhall/beads | Core graph issue tracker docs |
| SRC-BEADS-02| Beads | Multi-persona workflows: architect/implementer/reviewer examples and compaction | P1 | 2026-08 | https://github.com/gastownhall/beads/blob/main/examples/README.md | Verified role separation and memory compaction |
| SRC-BEADS-03| Beads | Dolt SQL sync and branch merging mechanics | P1 | 2026-08 | https://github.com/gastownhall/beads/blob/main/docs/reference/faq.md | Details on Dolt database requirements and remote synchronization |
| SRC-GASC-01 | Gas City | Orchestration-builder SDK, city.toml, multi-agent controller loop | P1 | 2026-08 / v0.2+ | https://github.com/gastownhall/gascity | Multi-agent runtime framework |
| SRC-GASC-02 | Gas City Packs | Official packs adapting BMAD, Superpowers, and Compound Engineering into formulas | P2 | 2026-08 | https://github.com/gastownhall/gascity-packs | Confirms multi-agent workflow formulas |
| SRC-SUPR-01 | Superpowers | Process skills: subagent-driven-development, executing-plans | P1 | 2026-08 / v0.3+ | https://github.com/obra/superpowers/blob/main/skills/subagent-driven-development/SKILL.md | Two-stage review loop (spec compliance & quality review) |
| SRC-SUPR-02 | Superpowers | erification-before-completion "Iron Law" of fresh command verification | P1 | 2026-08 | https://github.com/obra/superpowers/blob/main/skills/verification-before-completion/SKILL.md | Proven maker/reviewer verification discipline |
| SRC-SUPR-03 | Superpowers | Document review loop system design (clarity, completeness, consistency) | P1 | 2026-01 | https://github.com/obra/superpowers/blob/main/docs/superpowers/specs/2026-01-22-document-review-system-design.md | Formal document quality gate architecture |
| SRC-BMAD-01 | BMAD Method | Web Bundles for ChatGPT Custom GPTs and Gemini Gems (Brainstorming, PRD, Market Research) | P1 | 2026-08 / v4.0+ | https://docs.bmad-method.org/explanation/web-bundles/ | Official web-subscription planning handoff protocol |
| SRC-BMAD-02 | BMAD Method | Core modules: mad-method install, 34+ structured workflows and specialist roles | P1 | 2026-08 | https://github.com/bmad-code-org/BMAD-METHOD | Shipped agent roles and workflow catalog |
| SRC-RUFL-01 | Ruflo | Agent meta-harness architecture, Claude Code / Codex execution layer | P1 | 2026-08 / v1.2+ | https://github.com/ruvnet/ruflo | Swarm and workflow meta-harness documentation |
| SRC-RUFL-02 | Ruflo | 
uflo-workflows and 
uflo-rag-memory (AgentDB vector store, hybrid search) | P1 | 2026-08 | https://github.com/ruvnet/ruflo/blob/main/plugins/ruflo-workflows/README.md | Shipped workflow and RAG memory plugin specs |
| SRC-RUFL-03 | Ruflo | Agent catalog: 60+ specialized agents, MCP tool registry | P1 | 2026-08 | https://github.com/ruvnet/ruflo/blob/main/AGENTS.md | Prebuilt software and analysis agent registry |
| SRC-HERM-01 | Hermes Agent | Agent features overview: web/browser tools, terminal execution, persistent memory | P1 | 2026-08 / v0.5+ | https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/overview.md | Official Hermes Agent documentation |
| SRC-HERM-02 | Hermes Agent | Delegation: child subagent dispatch with isolated context and summary return | P1 | 2026-08 | https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/delegation.md | Subagent fan-out mechanics |
| SRC-HERM-03 | Hermes Agent | Scheduled jobs (cron) with attached Agent Skills and headless script execution | P1 | 2026-08 | https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/cron.md | Persistent recurring task scheduler |
| SRC-HERM-04 | Hermes Agent | External memory providers (Mem0, Letta, Qdrant) and built-in MEMORY.md | P1 | 2026-08 | https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/memory-providers.md | Memory architecture documentation |
| SRC-OCLW-01 | OpenClaw | Subagents tool: background tasks, isolated execution, parent context protection | P1 | 2026-08 / v1.0+ | https://docs.openclaw.ai/tools/subagents | Official OpenClaw subagent docs |
| SRC-OCLW-02 | OpenClaw | Automations / Cron jobs: persistent scheduling with isolated/main session modes | P1 | 2026-08 | https://docs.openclaw.ai/automation/cron-jobs | Recurring automation documentation |
| SRC-OCLW-03 | OpenClaw | Workspace skills: AgentSkills-compatible SKILL.md loading | P1 | 2026-08 | https://docs.openclaw.ai/tools/skills | Project-level skill integration |
| SRC-OPNS-01 | OpenSpec | Spec-driven development schema: proposal -> specs -> design -> tasks -> apply -> archive | P1 | 2026-08 / v0.8+ | https://github.com/Fission-AI/OpenSpec/blob/main/schemas/spec-driven/schema.yaml | Structured change control schema |
| SRC-TASK-01 | Task Master | Hierarchical task management, PRD parser, Claude Code / Codex provider modes | P1 | 2026-04 / v0.4+ | https://github.com/eyaltoledano/claude-task-master | Task decomposition and CLI provider docs |
| SRC-CREW-01 | CrewAI | CrewAI Crews & Flows: YAML configuration, routing, deep research loops | P1 | 2026-08 / v0.70+ | https://github.com/crewAIInc/crewAI | Official CrewAI documentation |
| SRC-CREW-02 | CrewAI | Local execution (Ollama) & Cloud LLM API support | P1 | 2026-08 | https://docs.crewai.com/how-to/LLM-Connections/ | Local and cloud model configuration guide |
| SRC-AG2-01  | AG2 (AutoGen) | Community AutoGen continuation: conversational multi-agent, UserProxyAgent HITL | P1 | 2026-08 / v0.4+ | https://github.com/ag2ai/ag2 | AG2 framework repository |
| SRC-LANG-01 | LangGraph | State persistence, Checkpointers (PostgresSaver), interrupts / HITL approval | P1 | 2026-08 / v0.2+ | https://langchain-ai.github.io/langgraph/ | LangGraph persistence and HITL docs |
| SRC-AGNC-01 | Agency Swarm | Multi-agent framework built exclusively on OpenAI Assistants API threads | P1 | 2026-07 / v0.3+ | https://github.com/vrsen/agency-swarm | Agency Swarm repository |
| SRC-META-01 | MetaGPT | Multi-agent framework simulating software company roles with SOPs | P1 | 2026-08 / v0.8+ | https://github.com/geekan/MetaGPT | MetaGPT repository and documentation |
| SRC-AGY-01  | Antigravity | Antigravity Customization System: progressive skills, rules (AGENTS.md), MCP | P1 | 2026-08 | https://antigravity.google/docs/skills | Built-in AGY Customization specification |
