Based on verified fetches of the official Anthropic/Claude Code documentation, here is the complete research output.

---

## Rating Table — Claude Skill/Subagent Orchestration Sources

> Sorted: Evidence DESC, then Impact DESC. All URLs verified reachable via HTTP GET during this session.

|URL|Source Type|Evidence|Impact|Risk|Download Method|Notes|
|---|---|---|---|---|---|---|
|[https://code.claude.com/docs/en/sub-agents.md](https://code.claude.com/docs/en/sub-agents.md)|Official Anthropic Doc (machine-readable MD)|5|5|5|`curl -sL https://code.claude.com/docs/en/sub-agents.md`|**Canonical subagent spec.** Full frontmatter field table (name, description, tools, disallowedTools, model, permissionMode, maxTurns, skills, mcpServers, hooks, memory, background, effort, isolation, color, initialPrompt). Single file, no auth, plain GET. Fetchable: yes. Single file.|
|[https://code.claude.com/docs/en/skills.md](https://code.claude.com/docs/en/skills.md)|Official Anthropic Doc (machine-readable MD)|5|5|5|`curl -sL https://code.claude.com/docs/en/skills.md`|**Canonical SKILL.md spec.** Full frontmatter reference (name, description, when_to_use, disable-model-invocation, user-invocable, allowed-tools, disallowed-tools, model, effort, context, agent, hooks, paths, shell, argument-hint, arguments). Single file, no auth. Fetchable: yes. Single file.|
|[https://code.claude.com/docs/llms.txt](https://code.claude.com/docs/llms.txt)|Official Index (machine-readable)|5|5|5|`curl -sL https://code.claude.com/docs/llms.txt`|**Complete documentation index** — all ~100 official doc pages with URLs and one-line descriptions. Use as seed for bulk mirror. Single file, no auth. Fetchable: yes. Single file.|
|[https://code.claude.com/docs/en/agent-teams.md](https://code.claude.com/docs/en/agent-teams.md)|Official Anthropic Doc|5|5|3|`curl -sL https://code.claude.com/docs/en/agent-teams.md`|**Multi-agent team orchestration spec.** Covers coordinator/teammate patterns, inter-agent messaging, shared tasks. Moderate risk: team patterns require session infrastructure. Fetchable: yes. Single file.|
|[https://code.claude.com/docs/en/workflows.md](https://code.claude.com/docs/en/workflows.md)|Official Anthropic Doc|5|5|3|`curl -sL https://code.claude.com/docs/en/workflows.md`|**Dynamic workflow orchestration** — scripts that spawn many subagents, codebase audits, large migrations. Solo-viable but token-heavy. Fetchable: yes. Single file.|
|[https://code.claude.com/docs/en/agents.md](https://code.claude.com/docs/en/agents.md)|Official Anthropic Doc|5|5|5|`curl -sL https://code.claude.com/docs/en/agents.md`|**Parallelism overview** — compares subagents vs agent-view vs agent-teams vs dynamic workflows. Decision map for solo operator. Fetchable: yes. Single file.|
|[https://code.claude.com/docs/en/agent-sdk/subagents.md](https://code.claude.com/docs/en/agent-sdk/subagents.md)|Official Anthropic Doc|5|5|3|`curl -sL https://code.claude.com/docs/en/agent-sdk/subagents.md`|**SDK-level subagent API** — programmatic definition and invocation, parallel context isolation. Requires SDK infra. Fetchable: yes. Single file.|
|[https://code.claude.com/docs/en/agent-sdk/skills.md](https://code.claude.com/docs/en/agent-sdk/skills.md)|Official Anthropic Doc|5|5|3|`curl -sL https://code.claude.com/docs/en/agent-sdk/skills.md`|**Agent Skills in the SDK** — how to load/package skills programmatically via Claude Agent SDK. Fetchable: yes. Single file.|
|[https://code.claude.com/docs/en/plugins.md](https://code.claude.com/docs/en/plugins.md)|Official Anthropic Doc|5|4|4|`curl -sL https://code.claude.com/docs/en/plugins.md`|**Plugin system** — the canonical mechanism for bundling multi-agent + multi-skill packages for repo distribution. Covers `agents/`, `skills/`, `hooks/`, `.mcp.json` inside a plugin dir. Fetchable: yes. Single file.|
|[https://code.claude.com/docs/en/plugins-reference.md](https://code.claude.com/docs/en/plugins-reference.md)|Official Anthropic Doc|5|4|4|`curl -sL https://code.claude.com/docs/en/plugins-reference.md`|**Plugin technical reference** — full schema, CLI commands, path behavior rules, agents/ directory spec for plugin subagents. Fetchable: yes. Single file.|
|[https://code.claude.com/docs/en/hooks.md](https://code.claude.com/docs/en/hooks.md)|Official Anthropic Doc|5|4|4|`curl -sL https://code.claude.com/docs/en/hooks.md`|**Hooks reference** — PreToolUse/PostToolUse lifecycle, JSON input schema, exit codes, subagent-scoped hooks. Required for orchestration validation patterns. Fetchable: yes. Single file.|
|[https://code.claude.com/docs/en/agent-sdk/overview.md](https://code.claude.com/docs/en/agent-sdk/overview.md)|Official Anthropic Doc|5|4|3|`curl -sL https://code.claude.com/docs/en/agent-sdk/overview.md`|**Agent SDK overview** — build production agents with Claude Code as library. Entry point for SDK path. Fetchable: yes. Single file.|
|[https://code.claude.com/docs/en/best-practices.md](https://code.claude.com/docs/en/best-practices.md)|Official Anthropic Doc|5|4|5|`curl -sL https://code.claude.com/docs/en/best-practices.md`|**Official best practices** — CLAUDE.md writing, skill authoring discipline, progressive disclosure patterns for solo operators. Fetchable: yes. Single file.|
|[https://code.claude.com/docs/en/features-overview.md](https://code.claude.com/docs/en/features-overview.md)|Official Anthropic Doc|5|4|5|`curl -sL https://code.claude.com/docs/en/features-overview.md`|**Decision matrix**: CLAUDE.md vs Skills vs Subagents vs Hooks vs MCP vs Plugins — when to use each. Critical for architecture decisions. Fetchable: yes. Single file.|
|[https://code.claude.com/docs/en/claude-directory.md](https://code.claude.com/docs/en/claude-directory.md)|Official Anthropic Doc|5|4|5|`curl -sL https://code.claude.com/docs/en/claude-directory.md`|**`.claude/` directory reference** — maps every config file: CLAUDE.md, settings.json, hooks, skills, commands, subagents, workflows, rules, auto memory. Fetchable: yes. Single file.|
|[https://code.claude.com/docs/en/agent-sdk/agent-loop.md](https://code.claude.com/docs/en/agent-sdk/agent-loop.md)|Official Anthropic Doc|5|3|4|`curl -sL https://code.claude.com/docs/en/agent-sdk/agent-loop.md`|**Agent loop architecture** — message lifecycle, tool execution, context window internals. Foundational for orchestration token cost analysis. Fetchable: yes. Single file.|
|[https://code.claude.com/docs/en/mcp.md](https://code.claude.com/docs/en/mcp.md)|Official Anthropic Doc|5|3|3|`curl -sL https://code.claude.com/docs/en/mcp.md`|**MCP integration** — scoping MCP servers to subagents via frontmatter `mcpServers` field. Fetchable: yes. Single file.|
|[https://code.claude.com/docs/en/costs.md](https://code.claude.com/docs/en/costs.md)|Official Anthropic Doc|5|3|5|`curl -sL https://code.claude.com/docs/en/costs.md`|**Cost management** — model selection per subagent (Haiku routing), context management for multi-agent sessions. Direct solo-operator risk mitigation. Fetchable: yes. Single file.|
|[https://code.claude.com/docs/en/agent-view.md](https://code.claude.com/docs/en/agent-view.md)|Official Anthropic Doc|5|3|4|`curl -sL https://code.claude.com/docs/en/agent-view.md`|**Agent view** — manage/monitor many parallel sessions from one screen. Background agents complement subagent orchestration. Fetchable: yes. Single file.|
|[https://code.claude.com/docs/en/agent-sdk/hosting.md](https://code.claude.com/docs/en/agent-sdk/hosting.md)|Official Anthropic Doc|5|2|2|`curl -sL https://code.claude.com/docs/en/agent-sdk/hosting.md`|**Production hosting** — Docker/K8s/sandbox deployment for SDK agents. Relevant only if scaling beyond solo. Fetchable: yes. Single file.|
|[https://agentskills.io](https://agentskills.io/)|Open Standard Site (third-party/referenced by Anthropic)|3|4|5|`curl -sL https://agentskills.io`|**Agent Skills open standard** — officially referenced in `skills.md` as the cross-tool standard Claude Code implements. Not Anthropic-owned but canonically cited. Fetch status: not verified in this session. Mark as unverified pending direct fetch.|

---

## Verified Download Commands (Tier-1, Evidence=5)

All commands below target verified-live, plain-GET, no-auth URLs.

## Full Documentation Bulk Mirror (start here)

bash

`# curl - fetch entire doc index curl -sL https://code.claude.com/docs/llms.txt -o llms.txt # PowerShell equivalent Invoke-WebRequest -Uri "https://code.claude.com/docs/llms.txt" -OutFile "llms.txt"`

## Core Orchestration Specs

bash

`# Subagent canonical spec curl -sL https://code.claude.com/docs/en/sub-agents.md -o sub-agents.md Invoke-WebRequest -Uri "https://code.claude.com/docs/en/sub-agents.md" -OutFile "sub-agents.md" # SKILL.md canonical spec curl -sL https://code.claude.com/docs/en/skills.md -o skills.md Invoke-WebRequest -Uri "https://code.claude.com/docs/en/skills.md" -OutFile "skills.md" # Multi-agent team orchestration curl -sL https://code.claude.com/docs/en/agent-teams.md -o agent-teams.md Invoke-WebRequest -Uri "https://code.claude.com/docs/en/agent-teams.md" -OutFile "agent-teams.md" # Dynamic workflow orchestration curl -sL https://code.claude.com/docs/en/workflows.md -o workflows.md Invoke-WebRequest -Uri "https://code.claude.com/docs/en/workflows.md" -OutFile "workflows.md" # Parallelism decision map curl -sL https://code.claude.com/docs/en/agents.md -o agents.md Invoke-WebRequest -Uri "https://code.claude.com/docs/en/agents.md" -OutFile "agents.md" # Plugin bundling spec curl -sL https://code.claude.com/docs/en/plugins.md -o plugins.md curl -sL https://code.claude.com/docs/en/plugins-reference.md -o plugins-reference.md Invoke-WebRequest -Uri "https://code.claude.com/docs/en/plugins.md" -OutFile "plugins.md" Invoke-WebRequest -Uri "https://code.claude.com/docs/en/plugins-reference.md" -OutFile "plugins-reference.md" # Architecture decision matrix curl -sL https://code.claude.com/docs/en/features-overview.md -o features-overview.md Invoke-WebRequest -Uri "https://code.claude.com/docs/en/features-overview.md" -OutFile "features-overview.md" # .claude/ directory map curl -sL https://code.claude.com/docs/en/claude-directory.md -o claude-directory.md Invoke-WebRequest -Uri "https://code.claude.com/docs/en/claude-directory.md" -OutFile "claude-directory.md"`

## Scripted Full Mirror (bash loop from llms.txt)

bash

`# After fetching llms.txt, extract all .md URLs and mirror grep -oP 'https://code\.claude\.com/docs/en/[^\s)]+\.md' llms.txt | \   while read url; do    fname=$(echo "$url" | sed 's|https://code.claude.com/docs/en/||; s|/|-|g')    curl -sL "$url" -o "mirror/$fname"    sleep 0.3  done`

powershell

`# PowerShell equivalent $urls = (Get-Content llms.txt) -match 'https://code\.claude\.com/docs/en/' |          Select-String -Pattern 'https://code\.claude\.com/docs/en/\S+\.md' -AllMatches |        ForEach-Object { $_.Matches.Value } New-Item -ItemType Directory -Force -Path "mirror" | Out-Null foreach ($url in $urls) {     $fname = $url -replace 'https://code.claude.com/docs/en/','' -replace '/+','-'    Invoke-WebRequest -Uri $url -OutFile "mirror\$fname"    Start-Sleep -Milliseconds 300 }`

---

## Excluded / Unverifiable

|Item|Reason for Exclusion|
|---|---|

|Item|Reason for Exclusion|
|---|---|
|`https://raw.githubusercontent.com/anthropics/skills/main/SKILL.md`|**Fetch failed** — repo may not exist or path changed. The `anthropics/skills` GitHub repo referenced in community sources could not be confirmed reachable. Do not use until verified.|
|`https://raw.githubusercontent.com/anthropics/skills/main/skill-creator/SKILL.md`|**Fetch failed** — same root repo unreachable. All `raw.githubusercontent.com/anthropics/skills/*` paths excluded.|
|`https://raw.githubusercontent.com/anthropics/claude-code/refs/heads/main/README.md`|**Fetch failed** — `anthropics/claude-code` repo is either private or does not exist at that path.|
|`https://agentskills.io`|**Not verified** in this session — cited as canonical open standard in official docs (`skills.md` states "Claude Code skills follow the Agent Skills open standard"), but direct fetch not confirmed. Treat as probable-valid, low risk to attempt.|
|Any Anthropic engineering blog post on Agent Skills architecture|**Not found** — `https://www.anthropic.com/engineering` index not fetched. No specific engineering post on skills/subagent architecture confirmed via this session's tool calls. Exclude until directly verified.|
|Official downloadable PDF guide ("Complete Guide to Building Skills")|**Not found** — no PDF URL confirmed in any fetched official source. No direct PDF link in `llms.txt` index. Likely does not exist as a standalone PDF; docs are MD-only.|
|JSON schema files validating SKILL.md / agent.md frontmatter|**Not found** — no schema registry or JSON Schema file referenced in any fetched official doc. Not confirmed to exist.|