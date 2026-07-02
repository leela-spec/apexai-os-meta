# Skill Best-Practices Official Source Acquisition Ledger

Created: 2026-06-23T17:50:06

Original acquisition target: C:\GitDev\apexai-os-meta\apex-meta\kb\apex-kb-skill-test

Current archive path: apex-meta/kb/_source-acquisitions/skill-best-practices-official-2026-06-23

## Status

This folder is a raw source acquisition archive. It is not the compiled skill-design-best-practices KB.

Use it as Tier-A/Tier-B source material for later curated Apex KB ingest.

## Web / PDF / Academic Sources

| Tier | ID | Type | Title | URL | Role |
|---|---|---|---|---|---|
| A | anthropic-agent-skills-overview | official_doc | Anthropic Agent Skills Overview | https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview | Official conceptual definition of Agent Skills. |
| A | anthropic-skill-authoring-best-practices | official_doc | Anthropic Skill Authoring Best Practices | https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices | Official guidance for discoverable, concise, tested Skills. |
| A | anthropic-complete-guide-pdf | official_pdf | The Complete Guide to Building Skills for Claude | https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf?hsLang=en | Official long-form guide for planning, structure, testing, and distribution. |
| A | anthropic-engineering-agent-skills | official_article | Equipping agents for the real world with Agent Skills | https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills | Official engineering rationale and best-practice explanation. |
| A | claude-blog-complete-guide | official_blog | A complete guide to building skills for Claude | https://claude.com/blog/complete-guide-to-building-skills-for-claude | Official blog landing page for skill-building guide. |
| B | agentskills-specification | open_standard | Agent Skills Specification | https://agentskills.io/specification | Open standard for SKILL.md package format and progressive disclosure. |
| B | agentskills-home | open_standard | Agent Skills Overview | https://agentskills.io/home | Open standard overview of skill folder and SKILL.md model. |
| C | deepwiki-anthropics-skills | secondary_index | DeepWiki anthropics/skills | https://deepwiki.com/anthropics/skills | Secondary map of official anthropics/skills repo. |
| C | deepwiki-skill-md-format | secondary_index | DeepWiki SKILL.md Format Specification | https://deepwiki.com/anthropics/skills/2.2-skill.md-format-specification | Secondary indexed reference for SKILL.md format. |
| Research | arxiv-agent-skills-data-driven-analysis | academic | Agent Skills: A Data-Driven Analysis of Claude Skills | https://arxiv.org/abs/2602.08004 | Academic analysis of skill ecosystem, redundancy, budgets, and risk. |
| Research | arxiv-skill-md-semantic-supply-chain | academic | Under the Hood of SKILL.md: Semantic Supply-chain Attacks | https://arxiv.org/abs/2605.11418 | Academic risk model for SKILL.md wording, discovery, selection, and governance. |
| Research | arxiv-evoskills | academic | EvoSkills: Self-Evolving Agent Skills via Co-Evolutionary Verification | https://arxiv.org/abs/2604.01687 | Academic source for verifier-guided skill generation and improvement loops. |

## Repositories

| Tier | ID | Title | URL | Local folder | Role |
|---|---|---|---|---|---|
| A | anthropics-skills | anthropics/skills | https://github.com/anthropics/skills.git | raw/official-repos/anthropics-skills | Official public Agent Skills repository. |
| B | agentskills-agentskills | agentskills/agentskills | https://github.com/agentskills/agentskills.git | raw/official-repos/agentskills-agentskills | Open standard documentation repository. |

## Ingest Guidance

Do not ingest this whole archive at once.

Recommended first allowlist:

- Anthropic Agent Skills overview
- Anthropic Skill Authoring Best Practices
- Anthropic complete guide PDF
- Anthropic engineering article
- Agent Skills specification
- anthropics/skills repository README
- selected official SKILL.md examples from raw/repo-extracts/
- selected academic/security papers

DeepWiki files are secondary navigation only, not canonical evidence.
