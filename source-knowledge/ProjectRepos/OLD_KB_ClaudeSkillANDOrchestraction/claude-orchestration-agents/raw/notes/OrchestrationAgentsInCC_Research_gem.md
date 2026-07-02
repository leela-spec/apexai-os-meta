
### Agent Skills Core Open Specification

- **Target Component Type**: Markdown Specification Text & Frontmatter Constraints
    
- **Exact Raw Download URL**: [https://raw.githubusercontent.com/agentskills/agentskills/main/README.md](https://www.google.com/search?q=https://raw.githubusercontent.com/agentskills/agentskills/main/README.md)
    
- **Structural Integrity Key**: `SKILL.md`, `scripts/`, `references/`, `assets/`, `name` (Max 64 characters), `description` (Max 1024 characters), `compatibility` (Max 500 characters), `license`, `Progressive Disclosure Model`
    
- **Verification Method**: Verified locally via the native repository reference implementation CLI utility command: `skills-ref validate ./my-skill`
    

### Claude Code Plugin Manifest Blueprint (vinnie357/claude-skills)

- **Target Component Type**: JSON Manifest Configuration
    
- **Exact Raw Download URL**: [https://raw.githubusercontent.com/vinnie357/claude-skills/main/plugin.json](https://www.google.com/search?q=https://raw.githubusercontent.com/vinnie357/claude-skills/main/plugin.json)
    
- **Structural Integrity Key**: `skills`, `name`, `description`, `version`, `license`, `kebab-case directory matching`, `skills/sources.md`
    
- **Verification Method**: Programmatically evaluated against automated test blocks via Nushell (`nu`) validation tools inside the plugin suite checking for schema compliance and local path integrity.
    

### Claude Code Marketplace Registry Definition (vinnie357/claude-skills)

- **Target Component Type**: JSON Schema Marketplace Manifest
    
- **Exact Raw Download URL**: [https://raw.githubusercontent.com/vinnie357/claude-skills/main/marketplace.json](https://www.google.com/search?q=https://raw.githubusercontent.com/vinnie357/claude-skills/main/marketplace.json)
    
- **Structural Integrity Key**: `plugins`, `core/`, `languages/`, `tools/`, `all-skills` meta-plugin definitions, required package entry keys, structural file graphs
    
- **Verification Method**: Verified via automated Nushell script pipelines executing schema compliance runs, ensuring required field layouts, and running dependency graph analysis across all mapped plugin variants.
    

### Trail of Bits Hardened Claude Code Enterprise Template

- **Target Component Type**: JSON Configuration & Sandboxing Policy Fabric
    
- **Exact Raw Download URL**: [https://raw.githubusercontent.com/trailofbits/claude-code-config/main/settings.json](https://www.google.com/search?q=https://raw.githubusercontent.com/trailofbits/claude-code-config/main/settings.json)
    
- **Structural Integrity Key**: `$schema`, `cleanupPeriodDays`, `env` (`DISABLE_TELEMETRY`, `DISABLE_ERROR_REPORTING`, `CLAUDE_CODE_DISABLE_FEEDBACK_SURVEY`, `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`), `enableAllProjectMcpServers`, `alwaysThinkingEnabled`, `permissions.deny` block patterns, `hooks.PreToolUse` shell execution pipelines
    
- **Verification Method**: Parsed directly by the Claude Code binary runtime on terminal initialization or configuration ingestion inside the local system workspace.
    

### Claude Code Multi-Agent Team Layout & Directory Mapping

- **Target Component Type**: Folder Architecture Map & Parallel Orchestration Schema
    
- **Exact Raw Download URL**: [https://raw.githubusercontent.com/FlorianBruniaux/claude-code-ultimate-guide/main/guide/workflows/agent-teams.md](https://www.google.com/search?q=https://raw.githubusercontent.com/FlorianBruniaux/claude-code-ultimate-guide/main/guide/workflows/agent-teams.md)
    
- **Structural Integrity Key**: `.claude/tasks/` lockfile allocations, `.claude/rules/`, `.claude/skills/`, `.claude/commands/`, `.claude/agents/`, `.claude/agent-memory/`, `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`, `teammateMode`
    
- **Verification Method**: Orchestrated and checked autonomously via a shared Git-backed lock mechanism where parallel Claude session instances claim, update, and resolve workspace trees dynamically across split execution environments.
    

this is not an accaeplatble research. attached you find what the same prompt resulted in claude. you dont want to loose to it right?

  

extend and find other sources than claude

### Agent Skills Open Standard Core Specification

- **Target Component Type**: Open Specification Text & Frontmatter Constraints Manifest
    
    Strapi
    
- **Exact Raw Download URL**: [https://raw.githubusercontent.com/agentskills/agentskills/main/README.md](https://www.google.com/search?q=https://raw.githubusercontent.com/agentskills/agentskills/main/README.md)
    
- **Structural Integrity Key**: `name`, `description`, `compatibility`, `Progressive Disclosure Model`, `SKILL.md` file targets, `scripts/`, `references/`, `assets/`
    
- **Verification Method**: Validated programmatically using `skills-ref validate ./my-skill` or equivalent Markdown validation sweeps within repo pipelines to enforce schema compliance.
    

### Claude Code Official Skills Schema Specification

- **Target Component Type**: Machine-Readable Markdown Functional Specification[cite: 1]
    
- **Exact Raw Download URL**: [https://code.claude.com/docs/en/skills.md](https://www.google.com/search?q=https://code.claude.com/docs/en/skills.md)
    
- **Structural Integrity Key**: `name`, `description`, `when_to_use`, `disable-model-invocation`, `user-invocable`, `allowed-tools`, `disallowed-tools`, `model`, `effort`, `context`, `agent`, `hooks`, `paths`, `shell`, `argument-hint`, `arguments`[cite: 1]
    
- **Verification Method**: Parsed dynamically by the Claude Code environment upon session initialization or runtime workspace discovery via `--add-dir` pathways.
    

### Claude Code Autonomous Subagents Specification

- **Target Component Type**: Machine-Readable Markdown Functional Specification[cite: 1]
    
- **Exact Raw Download URL**: [https://code.claude.com/docs/en/sub-agents.md](https://www.google.com/search?q=https://code.claude.com/docs/en/sub-agents.md)
    
- **Structural Integrity Key**: `name`, `description`, `tools`, `disallowedTools`, `model`, `permissionMode`, `maxTurns`, `skills`, `mcpServers`, `hooks`, `memory`, `background`, `effort`, `isolation`, `color`, `initialPrompt`[cite: 1]
    
- **Verification Method**: Evaluated during operational runtime whenever a parent agent issues execution orders to spawn an isolated sub-agent context.
    

### Claude Code Multi-Agent Team Orchestration Protocol

- **Target Component Type**: Machine-Readable Markdown Functional Specification[cite: 1]
    
- **Exact Raw Download URL**: [https://code.claude.com/docs/en/agent-teams.md](https://www.google.com/search?q=https://code.claude.com/docs/en/agent-teams.md)
    
- **Structural Integrity Key**: `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`, `teammateMode`, `TeamCreate`, `TeamDelete`, `.claude/tasks/` lockfile allocations, continuous merge pathways, peer-to-peer mailbox networks
    
    Claude
    
- **Verification Method**: Synchronized through a Git-backed workspace layout where independent model instances claim tasks via lockfiles and auto-resolve merge actions.
    

### vinnie357/claude-skills Plugin Framework Manifest

- **Target Component Type**: JSON Manifest Schema
    
    GitHub
    
- **Exact Raw Download URL**: [https://raw.githubusercontent.com/vinnie357/claude-skills/main/.claude-plugin/plugin.json](https://www.google.com/search?q=https://raw.githubusercontent.com/vinnie357/claude-skills/main/.claude-plugin/plugin.json)
    
- **Structural Integrity Key**: `skills`, `name`, `description`, `version`, `author`, `license`, `kebab-case directory rules`
    
- **Verification Method**: Evaluated via automated testing toolchains (such as Nushell script workflows) verifying exact local tool folder structures.
    

### vinnie357/claude-skills Global Marketplace Configuration

- **Target Component Type**: JSON Schema Marketplace Definition
    
    GitHub
    
- **Exact Raw Download URL**: [https://raw.githubusercontent.com/vinnie357/claude-skills/main/.claude-plugin/marketplace.json](https://www.google.com/search?q=https://raw.githubusercontent.com/vinnie357/claude-skills/main/.claude-plugin/marketplace.json)
    
- **Structural Integrity Key**: `plugins`, `core/skills/`, `languages/`, `tools/`, required meta-plugin package array definitions
    
- **Verification Method**: Evaluated via integration validation suites mapping dependency graphs across registered system plug-ins.
    

### Trail of Bits Hardened Enterprise Configuration Engine

- **Target Component Type**: JSON Deployment Configuration & Security Policy Fabric
    
    tl;dr sec
    
- **Exact Raw Download URL**: [https://raw.githubusercontent.com/trailofbits/claude-code-config/main/settings.json](https://www.google.com/search?q=https://raw.githubusercontent.com/trailofbits/claude-code-config/main/settings.json)
    
- **Structural Integrity Key**: `$schema`, `cleanupPeriodDays`, `env` (`DISABLE_TELEMETRY`, `DISABLE_ERROR_REPORTING`, `CLAUDE_CODE_DISABLE_FEEDBACK_SURVEY`, `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`), `enableAllProjectMcpServers`, `alwaysThinkingEnabled`, `permissions.deny`, `hooks.PreToolUse`
    
- **Verification Method**: Consumed directly by the terminal application binary upon startup to implement firm sandbox constraints, command blocks, and execution barriers.
    

### Claude Code Project Workspace Layout Reference

Strapi+ 2

- **Target Component Type**: Complete File System Tree Layout Map[cite: 1]
    
- **Exact Raw Download URL**: [https://code.claude.com/docs/en/claude-directory.md](https://www.google.com/search?q=https://code.claude.com/docs/en/claude-directory.md)
    
- **Structural Integrity Key**: `.claude/`, `CLAUDE.md`, `settings.json`, `hooks/`, `skills/`, `commands/`, `subagents/`, `workflows/`, `rules/`, `auto memory/`[cite: 1]
    
- **Verification Method**: Scanned natively by the terminal agent at the execution root directory to load project rules, tools, and cross-session memory banks.