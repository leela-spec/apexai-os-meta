# OrchestrationAgentsInCC Source Download Report

Generated: `2026-07-01T09:45:46Z`

## Input Notes

- `apex-meta/kb/claude-orchestration-agents/raw/notes/OrchestrationAgentsInCC_Research_CC.md`
- `apex-meta/kb/claude-orchestration-agents/raw/notes/OrchestrationAgentsInCC_Research_gem.md`

## Run Configuration

```yaml
dry_run: False
force: True
no_jina: False
only_tier: all
limit: 0
timeout_seconds: 35
max_bytes: 52428800
```

## Status Counts

| Status | Count |
|---|---:|
| downloaded | 31 |

## Tier Counts

| Tier | Count |
|---|---:|
| external | 4 |
| primary | 15 |
| repo-example | 5 |
| secondary | 7 |

## Results

| # | Status | Tier | Source | Target | Origin line | Notes/Error |
|---:|---|---|---|---|---:|---|
| 1 | downloaded | primary | `https://code.claude.com/docs/en/sub-agents.md` | `apex-meta/kb/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-sub-agents.md.md` | 11 | **Canonical subagent spec.** Full frontmatter field table (name, description, tools, disallowedTools, model, permissionMode, maxTurns, skills, mcpServers, hooks |
| 2 | downloaded | primary | `https://code.claude.com/docs/en/skills.md` | `apex-meta/kb/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-skills.md.md` | 12 | **Canonical SKILL.md spec.** Full frontmatter reference (name, description, when_to_use, disable-model-invocation, user-invocable, allowed-tools, disallowed-too |
| 3 | downloaded | primary | `https://code.claude.com/docs/llms.txt` | `apex-meta/kb/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-code.claude.com-docs-llms.txt.txt` | 13 | **Complete documentation index** — all ~100 official doc pages with URLs and one-line descriptions. Use as seed for bulk mirror. Single file, no auth. Fetchable |
| 4 | downloaded | primary | `https://code.claude.com/docs/en/agent-teams.md` | `apex-meta/kb/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-agent-teams.md.md` | 14 | **Multi-agent team orchestration spec.** Covers coordinator/teammate patterns, inter-agent messaging, shared tasks. Moderate risk: team patterns require session |
| 5 | downloaded | primary | `https://code.claude.com/docs/en/workflows.md` | `apex-meta/kb/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-workflows.md.md` | 15 | **Dynamic workflow orchestration** — scripts that spawn many subagents, codebase audits, large migrations. Solo-viable but token-heavy. Fetchable: yes. Single f |
| 6 | downloaded | primary | `https://code.claude.com/docs/en/agents.md` | `apex-meta/kb/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-agents.md.md` | 16 | **Parallelism overview** — compares subagents vs agent-view vs agent-teams vs dynamic workflows. Decision map for solo operator. Fetchable: yes. Single file. |
| 7 | downloaded | primary | `https://code.claude.com/docs/en/agent-sdk/subagents.md` | `apex-meta/kb/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-agent-sdk-subagents.md.md` | 17 | **SDK-level subagent API** — programmatic definition and invocation, parallel context isolation. Requires SDK infra. Fetchable: yes. Single file. |
| 8 | downloaded | primary | `https://code.claude.com/docs/en/agent-sdk/skills.md` | `apex-meta/kb/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-agent-sdk-skills.md.md` | 18 | **Agent Skills in the SDK** — how to load/package skills programmatically via Claude Agent SDK. Fetchable: yes. Single file. |
| 9 | downloaded | primary | `https://code.claude.com/docs/en/plugins.md` | `apex-meta/kb/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-plugins.md.md` | 19 | **Plugin system** — the canonical mechanism for bundling multi-agent + multi-skill packages for repo distribution. Covers `agents/`, `skills/`, `hooks/`, `.mcp. |
| 10 | downloaded | primary | `https://code.claude.com/docs/en/plugins-reference.md` | `apex-meta/kb/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-plugins-reference.md.md` | 20 | **Plugin technical reference** — full schema, CLI commands, path behavior rules, agents/ directory spec for plugin subagents. Fetchable: yes. Single file. |
| 11 | downloaded | primary | `https://code.claude.com/docs/en/hooks.md` | `apex-meta/kb/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-hooks.md.md` | 21 | **Hooks reference** — PreToolUse/PostToolUse lifecycle, JSON input schema, exit codes, subagent-scoped hooks. Required for orchestration validation patterns. Fe |
| 12 | downloaded | primary | `https://code.claude.com/docs/en/agent-sdk/overview.md` | `apex-meta/kb/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-agent-sdk-overview.md.md` | 22 | **Agent SDK overview** — build production agents with Claude Code as library. Entry point for SDK path. Fetchable: yes. Single file. |
| 13 | downloaded | primary | `https://code.claude.com/docs/en/best-practices.md` | `apex-meta/kb/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-best-practices.md.md` | 23 | **Official best practices** — CLAUDE.md writing, skill authoring discipline, progressive disclosure patterns for solo operators. Fetchable: yes. Single file. |
| 14 | downloaded | primary | `https://code.claude.com/docs/en/features-overview.md` | `apex-meta/kb/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-features-overview.md.md` | 24 | **Decision matrix**: CLAUDE.md vs Skills vs Subagents vs Hooks vs MCP vs Plugins — when to use each. Critical for architecture decisions. Fetchable: yes. Single |
| 15 | downloaded | primary | `https://code.claude.com/docs/en/claude-directory.md` | `apex-meta/kb/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-claude-directory.md.md` | 25 | **`.claude/` directory reference** — maps every config file: CLAUDE.md, settings.json, hooks, skills, commands, subagents, workflows, rules, auto memory. Fetcha |
| 16 | downloaded | secondary | `https://code.claude.com/docs/en/agent-sdk/agent-loop.md` | `apex-meta/kb/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/secondary-code-claude-com-docs-en-agent-sdk-agent-loop.md.md` | 26 | **Agent loop architecture** — message lifecycle, tool execution, context window internals. Foundational for orchestration token cost analysis. Fetchable: yes. S |
| 17 | downloaded | secondary | `https://code.claude.com/docs/en/mcp.md` | `apex-meta/kb/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/secondary-code-claude-com-docs-en-mcp.md.md` | 27 | **MCP integration** — scoping MCP servers to subagents via frontmatter `mcpServers` field. Fetchable: yes. Single file. |
| 18 | downloaded | secondary | `https://code.claude.com/docs/en/costs.md` | `apex-meta/kb/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/secondary-code-claude-com-docs-en-costs.md.md` | 28 | **Cost management** — model selection per subagent (Haiku routing), context management for multi-agent sessions. Direct solo-operator risk mitigation. Fetchable |
| 19 | downloaded | secondary | `https://code.claude.com/docs/en/agent-view.md` | `apex-meta/kb/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/secondary-code-claude-com-docs-en-agent-view.md.md` | 29 | **Agent view** — manage/monitor many parallel sessions from one screen. Background agents complement subagent orchestration. Fetchable: yes. Single file. |
| 20 | downloaded | secondary | `https://code.claude.com/docs/en/agent-sdk/hosting.md` | `apex-meta/kb/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/secondary-code-claude-com-docs-en-agent-sdk-hosting.md.md` | 30 | **Production hosting** — Docker/K8s/sandbox deployment for SDK agents. Relevant only if scaling beyond solo. Fetchable: yes. Single file. |
| 21 | downloaded | external | `https://agentskills.io/` | `apex-meta/kb/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/external-agentskills-io-agentskills.io.md` | 31 | **Agent Skills open standard** — officially referenced in `skills.md` as the cross-tool standard Claude Code implements. Not Anthropic-owned but canonically cit |
| 22 | downloaded | secondary | `https://code.claude.com/docs/en/` | `apex-meta/kb/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/secondary-code-claude-com-docs-en.md` | 55 | `# After fetching llms.txt, extract all .md URLs and mirror grep -oP 'https://code\.claude\.com/docs/en/[^\s)]+\.md' llms.txt | \   while read url; do    fname= |
| 23 | downloaded | secondary | `https://www.anthropic.com/engineering` | `apex-meta/kb/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/secondary-anthropic-com-engineering.md` | 74 | |Any Anthropic engineering blog post on Agent Skills architecture|**Not found** — `https://www.anthropic.com/engineering` index not fetched. No specific enginee |
| 24 | downloaded | repo-example | `https://raw.githubusercontent.com/agentskills/agentskills/main/README.md` | `apex-meta/kb/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/repo-example-raw-githubusercontent-com-agentskills-agentskills-main-README.md.md` | 6 |  |
| 25 | downloaded | repo-example | `https://raw.githubusercontent.com/vinnie357/claude-skills/main/.claude-plugin/plugin.json` | `apex-meta/kb/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/repo-example-raw-githubusercontent-com-vinnie357-claude-skills-main-.claude-plugin-plugin.json.json` | 17 |  |
| 26 | downloaded | repo-example | `https://raw.githubusercontent.com/vinnie357/claude-skills/main/.claude-plugin/marketplace.json` | `apex-meta/kb/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/repo-example-raw-githubusercontent-com-vinnie357-claude-skills-main-.claude-plugin-marketplace.json.json` | 28 |  |
| 27 | downloaded | repo-example | `https://raw.githubusercontent.com/trailofbits/claude-code-config/main/settings.json` | `apex-meta/kb/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/repo-example-raw-githubusercontent-com-trailofbits-claude-code-config-main-settings.json.json` | 39 |  |
| 28 | downloaded | repo-example | `https://raw.githubusercontent.com/FlorianBruniaux/claude-code-ultimate-guide/main/guide/workflows/agent-teams.md` | `apex-meta/kb/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/repo-example-raw-githubusercontent-com-FlorianBruniaux-claude-code-ultimate-guide-main-guide-workflows-agent-teams.md.md` | 50 |  |
| 29 | downloaded | external | `https://learn.microsoft.com/en-us/agent-framework/agents/skills` | `apex-meta/kb/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/external-learn-microsoft-com-skills.md` | 0 |  |
| 30 | downloaded | external | `https://www.skillsdirectory.com/docs/skill-file-structure` | `apex-meta/kb/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/external-skillsdirectory-com-skill-file-structure.md` | 0 |  |
| 31 | downloaded | external | `https://www.mindstudio.ai/blog/what-are-claude-code-skills` | `apex-meta/kb/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/external-mindstudio-ai-what-are-claude-code-skills.md` | 0 |  |
