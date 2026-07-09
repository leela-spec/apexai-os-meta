Here is the full verification matrix across all five objectives. All claims sourced from primary Anthropic docs first, then maintained repos, then dated blogs.

---

## Objective 1 — Token/Context Management Primitives

## `/compact` Slash Command

|Claim|Status|Evidence|
|---|---|---|
|`/compact` exists as a manual slash command in current Claude Code|**CONFIRMED**|[code.claude.com/docs/en/agent-sdk/slash-commands](https://code.claude.com/docs/en/agent-sdk/slash-commands) lists it natively; cross-confirmed by April 2026 blog [[howdoiuseai](https://www.howdoiuseai.com/blog/2026-04-16-what-does-compact-do-in-claude-code-context-management)]|
|Auto-compaction triggers at ~83.5% context utilization (~167K tokens on 200K window)|**PARTIALLY CONFIRMED / UNVERIFIED as "official"**|The 83.5% figure is from a third-party blog [[howdoiuseai](https://www.howdoiuseai.com/blog/2026-04-16-what-does-compact-do-in-claude-code-context-management)], not from official Anthropic docs. Official docs state only `"value": 150000` as the **default API trigger threshold** for server-side compaction, not a percentage [[platform.claude](https://platform.claude.com/docs/en/build-with-claude/compaction)]|
|`/compact [focus instructions]` accepts custom text argument to guide summarization|**CONFIRMED**|Documented in the April 2026 blog [[howdoiuseai](https://www.howdoiuseai.com/blog/2026-04-16-what-does-compact-do-in-claude-code-context-management)] and consistent with the API's `instructions` parameter behavior|
|Version checked: **v2.1.178+** (agent teams page specifies this; compaction beta header `compact-2026-01-12`)|**CONFIRMED** [[code.claude](https://code.claude.com/docs/en/agent-teams)]||

## API-Level Compaction (Platform Docs)

The official compaction mechanism is the **Messages API beta**, not just the CLI slash command:[[platform.claude](https://platform.claude.com/docs/en/build-with-claude/compaction)]

- Beta header: `compact-2026-01-12`
    
- Trigger param: `{"type": "input_tokens", "value": 150000}` (min: 50,000 tokens; default: 150,000)
    
- Supported models: Claude Opus 4.6–4.8, Sonnet 4.6–5, Mythos 5, Fable 5
    
- `pause_after_compaction: true` enables budget-gate logic (example: `n_compactions * TRIGGER_THRESHOLD >= TOTAL_TOKEN_BUDGET` → inject wrap-up message)
    
- Returns a `compaction` block; all prior content dropped on next request
    

## `/context` Command for Live Token Usage

|Claim|Status|Evidence|
|---|---|---|
|A `/context` command showing live token usage exists natively|**UNVERIFIED**|Not found in official slash command docs or the April 2026 command reference [[aiopsschool](https://aiopsschool.com/blog/the-master-tutorial-every-claude-code-slash-command-explained-april-2026-edition/)]. No official Anthropic source confirms this command name.|

## Other Context-Preservation Mechanisms

- **`CLAUDE.md`**: CONFIRMED as a persistent memory file loaded by all sessions and teammates at startup[[code.claude](https://code.claude.com/docs/en/agent-teams)]
    
- **`pause_after_compaction`**: CONFIRMED — API-level hook to inject messages post-summary before continuing[[platform.claude](https://platform.claude.com/docs/en/build-with-claude/compaction)]
    
- **`/count_tokens` endpoint**: CONFIRMED — applies existing compaction blocks, does not trigger new ones; returns `context_management.original_input_tokens` vs. current effective tokens[[platform.claude](https://platform.claude.com/docs/en/build-with-claude/compaction)]
    
- **Prompt caching on compaction blocks**: CONFIRMED — `cache_control: {type: "ephemeral"}` on the compaction block maximizes cache hit rates across compaction events[[platform.claude](https://platform.claude.com/docs/en/build-with-claude/compaction)]
    

---

## Objective 2 — Unattended/Headless Execution Flags

## `--dangerously-skip-permissions`

|Claim|Status|Evidence|
|---|---|---|
|Flag name spelling: `--dangerously-skip-permissions` (CLI flag, not env var)|**CONFIRMED**|Multiple 2026 sources [[theaiarchitects](https://theaiarchitects.com/blog/claude-code-dangerously-skip-permissions)]|
|Scope: skips **all** permission prompts in a session|**CONFIRMED**|[[theaiarchitects](https://theaiarchitects.com/blog/claude-code-dangerously-skip-permissions)] explicitly: "Bypasses every Claude Code permission prompt"|
|Official warning: flag is explicitly labeled "dangerous"; Anthropic docs warn against use in production/root environments|**CONFIRMED**|v2.1.126 added refusal when running as root [[morphllm](https://www.morphllm.com/claude-code-dangerously-skip-permissions)]|
|Teammates inherit this flag if the lead uses it|**CONFIRMED** — official doc|"If the lead runs with `--dangerously-skip-permissions`, all teammates do too." [[code.claude](https://code.claude.com/docs/en/agent-teams)]|

## Non-Interactive / Headless Invocation

|Pattern|Status|Evidence|
|---|---|---|
|`claude -p "prompt text"` or `claude --print "prompt text"` — print mode, non-interactive|**CONFIRMED**|Referenced in official CLI docs and multiple 2026 sources [[heyuan110](https://www.heyuan110.com/posts/ai/2026-03-05-claude-code-slash-commands/)]|
|Piped stdin: `echo "prompt" \\| claude -p`|**CONFIRMED**|Standard invocation pattern per maintained guides [[heyuan110](https://www.heyuan110.com/posts/ai/2026-03-05-claude-code-slash-commands/)]|
|Combined headless+no-prompts: `claude -p "task" --dangerously-skip-permissions`|**CONFIRMED** as functional|Used in unattended pipeline recipes [[theaiarchitects](https://theaiarchitects.com/blog/claude-code-dangerously-skip-permissions)]|

Minimal working example (from official-adjacent maintained sources):

bash

`echo "Refactor auth.py to use dataclasses" \   | claude -p --dangerously-skip-permissions`

---

## Objective 3 — Multi-Agent State Synchronization Patterns

## File-Based State Registries in the Wild

|Repo / Pattern|File Structure|Status|
|---|---|---|
|**ruvnet/ruflo** — `CLAUDE.md` + task queue files under `.claude/`|`.claude/skills/`, `.claude/memory/`, `CLAUDE.md` as persistent routing context; task states written to JSON under team session dirs|**CONFIRMED active** — last commit May 20, 2026 [[github](https://github.com/ruvnet/ruflo/blob/main/v3/@claude-flow/codex/AGENTS.md)]|
|**stevescargall MemMachine writeup** (April 2026) — 22-agent team with `TODO`-driven docs handoff and `/mm:` custom command surface|Markdown TODO files as shared state; `/mm:` skill commands route tasks between agents|**CONFIRMED dated** — blog April 2026 [[stevescargall](https://stevescargall.com/blog/2026/04/building-an-agentic-team-for-an-open-source-project-with-claude-code/)]|
|**smtg-ai/claude-squad** — git worktrees as isolation + file-based task separation|Each agent gets isolated git worktree branch; no shared JSON task registry built in — file sharing requires manual convention|**CONFIRMED** — latest release v1.0.13, Aug 28, 2025 [[github](https://github.com/smtg-ai/claude-squad/releases)]|

## Native Agent Teams vs. File-Based State — Overlap/Redundancy

|Aspect|Agent Teams (native)|File-Based Registry|
|---|---|---|
|Task list location|`~/.claude/tasks/{team-name}/` — auto-managed, file-locked|Arbitrary JSON/Markdown in project repo|
|Cross-session persistence|Task dir persists; team config deleted on session end|Persists indefinitely across sessions|
|Non-Claude-Code consumers|Not accessible outside Claude Code|Any process can read/write|
|Portability (API-only use)|Requires Claude Code CLI|Works with raw API or any agent framework|
|Verdict|**Replaces** file-based routing for pure Claude Code workflows|**Complementary** for hybrid/multi-tool pipelines|

The official doc explicitly states the team config directory is **removed when the session ends**, but the task list persists for resumed sessions. For pure Claude Code use with Agent Teams enabled, native task tools (`TaskCreate`/`TaskUpdate`/`TaskList`/`SendMessage`) are the recommended path. File-based state is not obsolete — it remains the only cross-session, cross-framework-compatible option.[[code.claude](https://code.claude.com/docs/en/agent-teams)]

---

## Objective 4 — Long-Duration Autonomous Loop Examples (60+ minutes, 60+ iterations)

## Real Dated Evidence (2026)

|Source|Date|Evidence Type|Content|
|---|---|---|---|
|stevescargall.com — 22-agent MemMachine team|April 2026 [[stevescargall](https://stevescargall.com/blog/2026/04/building-an-agentic-team-for-an-open-source-project-with-claude-code/)]|Blog with commit history link|Documents multi-agent maintenance team run on existing repo; includes `/mm:` command surface and TODO-driven docs handoff — implies extended autonomous operation but does not publish raw run logs|
|ruflo GitHub issues/wiki|Last issue: May 29, 2026 [[github](https://github.com/ruvnet/ruflo/issues)]; wiki May 24, 2026 [[github](https://github.com/ruvnet/ruflo/wiki)]|Active repo with issue tracker|User-reported workflows; no single canonical "60+ minute run log" link found in search results|
|developersdigest.tech — Ruflo 37,700 stars writeup|May 2026 [[developersdigest](https://developersdigest.tech/blog/github-trending-ruflo-2026-05-03)]|Third-party blog|Claims distributed vector memory and 100+ agent coordination but cites no run logs|

**Verdict on 60+ min run evidence**: **PARTIALLY CONFIRMED** — real use cases documented, but no publicly accessible single gist/commit log showing a timestamped 60+ minute, 60+ iteration unattended run was found in this search pass. The MemMachine blog is the closest primary evidence of a real multi-agent extended run.[[stevescargall](https://stevescargall.com/blog/2026/04/building-an-agentic-team-for-an-open-source-project-with-claude-code/)]

## Ruflo "30–50% Token Cost Reduction" Claim

|Claim|Status|Evidence|
|---|---|---|
|Ruflo claims 30–50% token cost reduction|**UNVERIFIED / MARKETING CLAIM**|No independent benchmark, academic paper, or user-reproducible test found. The claim appears in Ruflo's own marketing copy. No third-party replication found in May 2026 blog coverage [[developersdigest](https://developersdigest.tech/blog/github-trending-ruflo-2026-05-03)].|

---

## Objective 5 — Skills Activation in Multi-Step Workflows

## Claude Code Local Skills

|Aspect|Detail|Status|
|---|---|---|
|Directory convention|`.claude/skills/<skill-name>/SKILL.md` in project dir, or `~/.claude/skills/` for user-scope|**CONFIRMED** — ruflo uses this pattern [[github](https://github.com/ruvnet/ruflo/blob/main/.claude/skills/agentic-jujutsu/SKILL.md?plain=1)]; official agent-teams doc: "teammates load skills...from your project and user settings" [[code.claude](https://code.claude.com/docs/en/agent-teams)]|
|Invocation in workflow|Skills invoked via `/skill-name` slash commands; lead session and teammates both load project + user skills on startup|**CONFIRMED** [[code.claude](https://code.claude.com/docs/en/agent-teams)]|
|Teammate skill inheritance|Teammates load skills from project/user settings automatically; `skills` frontmatter in subagent definitions **NOT applied** when running as teammate|**CONFIRMED** — official doc: "The `skills` and `mcpServers` frontmatter fields in a subagent definition are not applied when that definition runs as a teammate." [[code.claude](https://code.claude.com/docs/en/agent-teams)]|
|MCP-server-based skill exposure|MCP servers defined in project or user settings are loaded by all teammates; explicit `mcpServers` in subagent frontmatter ignored when teammate|**CONFIRMED** [[code.claude](https://code.claude.com/docs/en/agent-teams)]|

## API-Level Skill Routing

|Aspect|Detail|Status|
|---|---|---|
|Native Claude API "Skills" product|Anthropic's Claude.ai Skills product (separate from Claude Code local skills) routes to domain-specific model configurations; not directly invocable via Messages API flags as of current docs|**UNVERIFIED for programmatic workflow invocation** — no official API-level skill routing syntax found in current platform docs|
|Ruflo skill files (`.claude/skills/`)|32+ Claude Code plugins exposed as skill files in ruflo, loadable as MCP tools via `npx ruflo@latest init wizard`|**CONFIRMED** — ruflo wiki [[github](https://github.com/ruvnet/ruflo/wiki)] and SKILL.md [[github](https://github.com/ruvnet/ruflo/blob/main/.claude/skills/agentic-jujutsu/SKILL.md?plain=1)]|

## Ruflo Baseline Verification

|Baseline Claim|Status|Evidence|
|---|---|---|
|Installable via `npx ruflo@latest init wizard`|**CONFIRMED**|npm package `ruflo@latest` confirmed [[github](https://github.com/ruvnet/ruflo/wiki)]|
|MCP server mode supported|**CONFIRMED**|Wiki lists MCP integration as core feature [[github](https://github.com/ruvnet/ruflo/wiki)]|
|`--topology hierarchical --max-agents 8` swarm flags|**UNVERIFIED** — exact flag syntax not confirmed|Swarm topologies documented conceptually but specific CLI flags not found in official ruflo docs in this pass [[github](https://github.com/ruvnet/ruflo/wiki)]|
|Last commit date|May 20, 2026 [[github](https://github.com/ruvnet/ruflo/blob/main/v3/@claude-flow/codex/AGENTS.md)]|Active|

## Agent Teams Baseline Verification

|Baseline Claim|Status|Evidence|
|---|---|---|

|Baseline Claim|Status|Evidence|
|---|---|---|
|`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` is a real, documented flag|**CONFIRMED**|Official doc: code.claude.com/docs/en/agent-teams [[code.claude](https://code.claude.com/docs/en/agent-teams)]|
|Enables Lead + independent Teammate sessions with separate context windows|**CONFIRMED** [[code.claude](https://code.claude.com/docs/en/agent-teams)]||
|Peer-to-peer messaging via `SendMessage` tool|**CONFIRMED** [[code.claude](https://code.claude.com/docs/en/agent-teams)]||
|Viewable via tmux/iTerm2 split panes or in-process Shift+Up/Down toggling|**PARTIALLY CONTRADICTED** — navigation is **Up/Down arrow keys + Enter**, not Shift+Up/Down|Official doc: "Use the up and down arrow keys in the agent panel to select a teammate, then press Enter" [[code.claude](https://code.claude.com/docs/en/agent-teams)]|
|`TeamCreate` / `TeamDelete` tools referenced in baseline|**OUTDATED** — deprecated as of v2.1.178|Official doc: "Both tools no longer exist." [[code.claude](https://code.claude.com/docs/en/agent-teams)]|

## claude-squad Baseline Verification

| Baseline Claim                                                                              | Status                                                                                                                                    | Evidence                   |
| ------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| tmux-based terminal multiplexer managing multiple Claude Code agents in isolated workspaces | **CONFIRMED** [[github](https://github.com/smtg-ai/claude-squad)]                                                                         |                            |
| File-locking between agents                                                                 | **CONFIRMED** — via git worktree isolation (branch-level, not explicit file lock API) [[github](https://github.com/smtg-ai/claude-squad)] |                            |
| Supports Claude Code, Codex, Gemini, Aider                                                  | **CONFIRMED** — also adds OpenCode and Amp [[github](https://github.com/smtg-ai/claude-squad)]                                            |                            |
| Latest release                                                                              | v1.0.13, Aug 28, 2025 [[github](https://github.com/smtg-ai/claude-squad/releases)] — **no 2026 release found**                            | Active but no 2026 release |