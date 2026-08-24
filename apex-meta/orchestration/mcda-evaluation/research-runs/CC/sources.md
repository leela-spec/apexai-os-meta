# Source Registry — perplexity-research

One row per source used for load-bearing claims. Evidence type P1-P5 per policy; strength A-D per policy.

| ID | candidate | claim/capability | source type | date/version | URL | notes |
|---|---|---|---|---|---|---|
| web:1 | Anthropic Agent Skills | Native shipped capability across Claude.ai, Claude Code, Agent SDK, Developer Platform | P1 | 2025-10-16 | https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills | Official Anthropic engineering post announcing Agent Skills |
| web:2 | BMAD-METHOD | Module list (BMM/BMB/TEA/GDS/CIS), web-bundles for Gemini Gems/ChatGPT Custom GPTs, non-code planning use cases | P1 | 2026-05-25 (README last updated) | https://github.com/bmad-code-org/BMAD-METHOD | Official repo README |
| web:3 | Anthropic Agent Skills marketplace | Official example/document skills, Claude Code plugin marketplace install commands | P1 | 2025-09-22 | https://github.com/anthropics/skills | Official Anthropic skills repo |
| web:6 | GitHub Spec Kit | Workflow engine with conditional logic, loops, fan-out/fan-in, pause/resume; `/speckit.*` commands | P1 | current | https://github.github.com/spec-kit/reference/overview.html | Official Spec Kit reference docs |
| web:7 | BMAD-METHOD official modules | BMad Builder, Creative Intelligence Suite, Game Dev Studio, Test Architecture module descriptions | P1 | current | https://docs.bmad-method.org/reference/modules/ | Official BMAD docs |
| web:8 | BMAD web bundles | Install steps for Gemini Gem / ChatGPT Custom GPT, bmadcode.com/web-bundles as sole install path | P1 | current | https://docs.bmad-method.org/how-to/use-web-bundles/ | Official BMAD docs |
| web:9 | BMAD web bundles concept | SKILL.md protocol, INSTRUCTIONS.md, persona inheritance, bundle generation via bmad-os-skill-to-bundle | P1 | current | https://docs.bmad-method.org/explanation/web-bundles/ | Official BMAD docs |
| web:12 | Claude Skills marketplaces (third-party) | 7,200+ community skills across official/community sources | P4 | current | https://skillsclaude.org/ | Independent marketplace, adoption-signal only |
| web:13 | BMAD-METHOD release | v6.0.0-alpha.7 web bundle support for BMM module (8 agents), active release cadence, npm install command | P1 | 2025-11-07 | https://newreleases.io/project/github/bmad-code-org/BMAD-METHOD/release/v6.0.0-alpha.7 | Release notes aggregator citing official GitHub release |
| web:15 | GitHub Spec Kit | `specify workflow` command group (v0.7.0+), resumable multi-step YAML pipelines | P3 | 2026-04-20 | https://deepwiki.com/github/spec-kit/4.6-specify-workflow | Third-party documentation aggregator (DeepWiki), corroborates web:6 |
| web:17 | Ruflo / Claude-Flow | "100+ specialized agents," MCP server, npx install | P1 | 2025-06-02 (repo), ongoing | https://github.com/ruvnet/ruflo | Official repo README |
| web:19 | Beads | Distributed graph issue tracker for AI agents, install/init commands | P1 | 2025-10-12 | https://github.com/gastownhall/beads | Official repo README |
| web:21 | Ruflo | Install commands, swarm init, MCP registration | P1 | 2026-05-25 | https://github.com/ruvnet/ruflo/wiki | Official wiki |
| web:23 | Ruflo | 56,000+ GitHub stars, 6,400 forks, 20-person contributor team claim | P4 | 2026-05-28 | https://www.decisioncrafters.com/ruflo-multi-agent-orchestration-for-claude-code-with-56k-github-stars/ | Independent write-up; adoption-signal only, not capability proof |
| web:29 | Ruflo (Claude Flow plugin) | 74+ specialized agents, 150+ commands, SPARC methodology, MCP config | P3 | current | https://claudemarketplaces.com/plugins/ruvnet-ruflo/claude-flow | Community-curated plugin directory |
| web:30 | Ruflo | UnifiedSwarmCoordinator, hierarchical/mesh/adaptive topologies | P3 | 2026-08-03 | https://deepwiki.com/ruvnet/ruflo/6.2-swarm-orchestration | Third-party doc aggregator |
| web:32 | Task Master AI | MCP server, 36 tools, editor configs (Cursor/Windsurf/VS Code), PRD-based task decomposition | P1 | 2025-03-04 | https://github.com/eyaltoledano/claude-task-master | Official repo README |
| web:38 | OpenSpec | Spec-driven development for AI coding assistants | P1 | 2025-08-05 | https://github.com/Fission-AI/OpenSpec | Official repo |
| web:40 | OpenSpec | Proposals/Specifications/Task Checklists/Archives workflow; 30+ supported tools | P3 | 2026-02-26 | https://github.com/speclib/awesome-openspec | Curated third-party list, corroborates official repo |
| web:43 | Task Master AI | 27,200+ stars, 36 tools, built by Eyal Toledano, companion "Hamster" platform | P4 | 2026-04-20 | https://chatforest.com/reviews/task-master-mcp-server/ | Independent review; adoption-signal only |
| web:46 | Superpowers Skills | Community-editable skills library for Claude Code superpowers plugin | P3 | 2026-08-12 | https://context7.com/obra/superpowers-skills | Third-party doc index of official repo |
| web:49 | Superpowers | SKILL.md invocation mechanics in Claude Code and Gemini CLI | P1 | 2025-10-09 | https://github.com/obra/superpowers/blob/main/skills/using-superpowers/SKILL.md | Official repo file |
| web:51 | Superpowers | "Complete software development methodology," marketplace install commands | P1 | 2026-08-12 | https://github.com/obra/superpowers | Official repo README |
| web:52 | Superpowers | Supported clients: Claude Code, Antigravity, Codex App/CLI, Cursor, Factory Droid, Gemini CLI, GitHub Copilot CLI, Kimi Code, OpenCode, Pi | P1 | 2025-10-09 | https://github.com/obra/Superpowers | Official repo README |
| web:56 | Superpowers | 14 skills, install command `npx -y skills add obra/superpowers --agent claude-code` | P3 | current | https://claudemarketplaces.com/skills/obra/superpowers | Community-curated skills directory |

Repository grounding attempt (not usable as a source in this run):
| gh:1 | leela-spec/MasterOfArts | Attempted retrieval of 07-INTEGRATED-AGENT-OPERATING-MODEL.md, 03-SCOPE-LOCK.md, 06-USER-STORIES-AND-EXECUTOR-MATRIX.md, 04-EVIDENCE-MATRIX.md, 05-MCDA-SCORES.md | P1 (attempted) | ref b4dceb52abb7327d50887f085fe4db7326969d40 | https://github.com/leela-spec/MasterOfArts/tree/main/Orchestration | Tool returned only a download confirmation, not the file text; raw.githubusercontent.com fetch failed (private repo, no auth token usable by fetch tool). Content of these five files is therefore NOT verified in this report. |
