# R07 — MarketingSkills + Hermes Integration — Work Result

**Research date:** 2026-08-23  
**Repository baseline:** `leela-spec/MasterOfArts@52c8ba0d7692e83891cd281f0525ffcabbd353fd`  
**MarketingSkills baseline:** `2.10.2`, commit `3df87f97621e18fbed7f6aa684edba54f49779a7` (2026-08-22)  
**Track status:** **PASS**  
**Verdict:** `MARKETINGSKILLS_HERMES_CONFIRMED`

## Executive decision

Use one upstream MarketingSkills package at the MasterOfArts Git root under the Agent Skills-compatible project location, trust it through Hermes, and keep offer-specific `.agents/product-marketing.md` files inside each family workdir. Every marketing Kanban task must use `dir:<absolute-family-path>` (or start Hermes with that family as cwd) so the package's relative context lookup resolves to that family's file.

No custom path setting exists in the current `product-marketing` skill, and its text does not hardcode a Git-root token; it consistently uses relative `.agents/product-marketing.md`. Ordinary tool path resolution is therefore workdir-relative. This is a `SUPPORTED_INFERENCE` from the exact upstream skill plus Hermes' native `dir:` workspaces, not an explicit MarketingSkills monorepo guarantee. It is acceptable only with a mandatory two-family QA test. If the installed runtime instead coerces those paths to the Git root, that test reaches the launcher's human gate because the locked package would fail required multi-offer scoping. Do not fork or copy the package to hide such a failure.

## Package/version/license evidence

The current upstream marketplace metadata reports version **2.10.2** and **49** marketing skills. The repository is MIT licensed. The project claims compatibility with Claude Code, OpenAI Codex, Cursor, Windsurf and Agent Skills-compatible agents. The current Agent Skills format is a directory with required `SKILL.md` frontmatter/body and optional scripts/references/assets, matching the package structure Hermes consumes.

## Installation/update strategy — **DO NOT EXECUTE**

| Upstream option | Support | Reproducibility/update | Cross-client | Mutation risk | Recommendation |
|---|---|---|---|---|---|
| `npx skills add coreyhaines31/marketingskills` | README-recommended | Installer/lock behavior; review generated diff | Universal `.agents/skills`; agent-specific flag available | Committed project files can be protected/reviewed | Preferred simple install during authorized phase |
| Clone/copy skills | Documented | Copy drift; reinstall needed | Broad | Higher manual-update risk | Not preferred |
| Git submodule at `.agents/marketingskills` | Documented | Commit-pinned, explicit update/rollback | Clients must reference nested `skills/` path | Upstream tree clean; added Git topology | Reproducible alternative only if architecture approves submodule |
| Fork | Documented option | Fully controlled but permanent divergence | Broad | High maintenance | Blocked for reuse-first target |
| SkillKit | Documented third-party option | Extra package/tool | Multi-client | Additional dependency | Not needed |

```bash
# DO NOT EXECUTE — install phase requires separate authorization
npx skills add coreyhaines31/marketingskills
npx skills add coreyhaines31/marketingskills --list
hermes skills trust
```

At installation, record the upstream version/commit and inspect the resulting Git diff/lock file. Updates use the same chosen upstream mechanism, never in-place autonomous edits. Preserve family `.agents/product-marketing.md` because it is project data outside the installed skill directories. Normal Git commit/revert provides rollback. Do not add a submodule merely for theoretical purity; that is an architecture choice for the authorized install stage.

## Hermes discovery, trust and precedence

Hermes discovers project skills only at the nearest Git root in `.hermes/skills/` and `.agents/skills/`. Project skills have precedence over local profile skills and external directories, are scanned/trusted, and are excluded from Curator maintenance. Curator cannot adopt project skills. Ordinary repository write tools could still edit them if permissions allow; prevent this through review/OS/repository policy and treat upstream package directories as immutable except during an approved update.

One root package is the correct monorepo layout. Nested family copies would not be discovered as independent project skill roots and would violate the failure condition.

## Product-marketing context path analysis

The current `product-marketing` v2.1.0 skill says:

- canonical file: `.agents/product-marketing.md`;
- legacy fallbacks: `.claude/product-marketing.md` and `product-marketing-context.md` variants;
- no configurable base-path variable;
- substantive updates increment document version and prepend a dated changelog entry;
- all other marketing skills check the canonical file before asking repeat questions.

| Possibility | Result |
|---|---|
| One root file | Works for one company-wide offer only; unsafe for materially different offers |
| Nested family files | Supported by relative path resolution when the task cwd is the family root |
| Different Hermes workdirs | Native Kanban `dir:` workspaces make the cwd explicit and persistent |
| Worktrees/submodules per offer | Technically separate roots but unnecessary and operationally expensive |
| MarketingSkills path config | None found in current skill/source |
| Hardcoded Git-root behavior | Not present in the skill text; “project” language is conceptual, path is relative |

Mandatory operating rule: no generic root `.agents/product-marketing.md` for multi-offer work. A marketing task workdir must be exactly the family that owns its context file. Micro-project work may reference deeper files while retaining the family root as task workdir, because a deeper cwd would look for another `.agents` directory and the skill does not walk ancestors.

## Two-project compatibility simulation

### Project A — prospective Awakenings workshop

```text
WORKDIR: /repo/MasterOfArts/Awakenings  (only after the real family exists)
HERMES PROJECT CONTEXT: root -> Awakenings AGENTS
MARKETING SPECIALIST PROFILE: shared Marketing Executive
MARKETINGSKILLS LOCATION: /repo/MasterOfArts/.agents/skills/<skills>
PRODUCT-MARKETING CONTEXT FILE FOUND: /repo/MasterOfArts/Awakenings/.agents/product-marketing.md
OTHER SKILLS ACTIVATED: customer-research, launch, social/video as task requires
PROJECT-SPECIFIC INPUTS: Awakenings evidence/offer/brief
OUTPUTS: task-declared Awakenings artifacts
RISK OF CONTEXT CONTAMINATION: low if cwd and QMD are explicit; fail if root fallback is used
```

### Project B — Lika materially different offer

```text
WORKDIR: /repo/MasterOfArts/Lika
HERMES PROJECT CONTEXT: root -> Lika AGENTS
MARKETING SPECIALIST PROFILE: same shared profile
MARKETINGSKILLS LOCATION: same root package
PRODUCT-MARKETING CONTEXT FILE FOUND: /repo/MasterOfArts/Lika/.agents/product-marketing.md
OTHER SKILLS ACTIVATED: content-strategy, copywriting, pricing as needed
PROJECT-SPECIFIC INPUTS: Lika accepted evidence/governance
OUTPUTS: task-declared Lika artifacts
RISK OF CONTEXT CONTAMINATION: low; Project A path/collection absent
```

QA must create harmless fixture context files in two approved test family directories, run the same skill from two `dir:` workspaces, and verify the reported document version/unique marker without altering real project data. That is a product validation, not custom infrastructure.

## Use-case fit map

| MoA use case | Current skill(s) | Fit |
|---|---|---|
| Product/offer positioning | `product-marketing`, `offers` | `DIRECT_FIT` |
| Customer research | `customer-research` | `DIRECT_FIT` |
| Content strategy | `content-strategy` | `DIRECT_FIT` |
| Website/landing copy | `copywriting`, `cro` | `DIRECT_FIT` |
| Social content/listening | `social` | `NEEDS_PROJECT_CONTEXT_ONLY` |
| Video strategy/scripts/production | `video`, `social` | `NEEDS_PROJECT_CONTEXT_ONLY`; production tools optional/paid |
| Launch planning | `launch` | `DIRECT_FIT` |
| Pricing | `pricing` | `NEEDS_PROJECT_CONTEXT_ONLY` |
| Offer design | `offers` | `DIRECT_FIT` for workshops/coaching/services |
| Full marketing plan | `marketing-plan` | `NEEDS_PROJECT_CONTEXT_ONLY`; software/funding assumptions must be pruned |
| Recurring loops | `marketing-loops` | `NEEDS_PROJECT_CONTEXT_ONLY`; actions require scheduler/tools and guardrails |
| Community/email/PR/influencer/partnership | corresponding current skills | `NEEDS_PROJECT_CONTEXT_ONLY` |

Some examples and metrics are SaaS/software biased, especially marketing-plan/pricing. The skills remain useful when the worker explicitly adapts business type, budget, proof and compliance rather than importing software assumptions.

## Representative skill I/O, token and API matrix

| Skill | Trigger/input | Context | AI? | Deterministic/external tools | Output/token driver |
|---|---|---|---:|---|---|
| `product-marketing` | New/update positioning | Canonical family file | Yes | Repo read/write only | Versioned context; repo scan + 12 sections |
| `customer-research` | Interviews/assets or online research | Product context | Yes | Web/data sources optional | Synthesis/personas; source volume |
| `content-strategy` | What to publish/topics | Product context | Yes | Keyword/forum/competitor data optional | Pillars/priority map; research volume |
| `copywriting` | Page/CTA copy | Product context + page goal | Yes | None required | Page copy/variants; page length |
| `social` | Posts/calendar/listening | Product context | Yes | Curl/browser/platform tools optional | Calendar/scripts; platforms/cadence |
| `video` | Script/production | Product context + production goal | Yes | Hyperframes/Remotion local; HeyGen MCP/video APIs optional | Script/spec or video; generation service dominates cost |
| `launch` | Product/feature launch | Product context | Yes | Partner/research tools optional | Phased plan/checklist |
| `offers` | Value/bonuses/guarantee | Product context | Yes | None required | Offer design/diagnostic |
| `pricing` | Tier/value metric/research | Product context + performance | Yes | Surveys/data optional | Pricing recommendation/audit |
| `marketing-plan` | AARRR/90-day/12-month plan | Product context + budget/team/funnel | Yes | Wired MCP/API inputs optional | 13-section files; high token volume |
| `marketing-loops` | Recurring workflow | Product context + cadence/tools | Yes | Scheduler/action APIs depend on loop | Loop spec; repeated execution cost |

The base instruction skills require provider reasoning but generally no paid SaaS. They are not “local/free” in the sense of model use: Hermes still calls the configured provider. Final video generation, analytics ingestion, ads, email/send, CRM, scheduling, social publishing and some research integrations may require API keys, paid accounts and external data egress. They are optional for planning/copy outputs but required when the task explicitly asks the external action or rendered asset.

## External-service/billing rules

| Category | Examples | Key/billing/egress | Requirement |
|---|---|---|---|
| Pure instruction | copywriting, offers, launch plan | Provider tokens only | Base capability |
| Deterministic local | Hyperframes/Remotion, public curl recipes | Local dependencies/network; no SaaS fee necessarily | Optional by output |
| External SaaS/MCP/API | HeyGen, analytics/CRM/email/ad/social tools | Account/key, possible usage fee, source data sent to service/provider | Optional unless action/data is requested |
| Marketing loop actions | send/spend/publish/PII workflows | Consequential external side effects | Must use package guardrails, caps, kill switch and human gates |

Never describe a complete video, send, paid-media or live automation result as free/local unless the selected tool actually is. MarketingSkills' `marketing-loops` explicitly requires two-tier gated actions, spend/send caps, compliance mapping and a kill switch.

## Cross-client reuse

| Client | Same skill content? | Native activation | Runtime-specific boundary |
|---|---:|---:|---|
| Hermes | Yes | Root `.agents/skills`, trusted | Profile/Kanban/QMD local |
| Codex | Yes | `.agents/skills`/installed skill support; explicit selection available | Codex sandbox/AGENTS config |
| Claude Code | Yes | Upstream installer targets `.claude/skills` | May require separate install path, not copied source logic |
| Other Agent Skills CLIs | Yes | If spec/path supported | Tool availability varies |
| Web ChatGPT/Claude repo access | Files readable | Not guaranteed from repo path alone; install/select product skill or follow explicitly | Cannot access local Hermes profile/QMD/Kanban by default |

OpenAI documents skills as reusable versioned bundles compatible with the Agent Skills standard, but ChatGPT Work cloud access still depends on installed skills/plugins and authorized apps. A checked-in package is not automatically a cloud connector.

## Unresolved blocker test

There is no current blocker under the documented workdir model. The one material uncertainty is whether every installed Hermes file tool resolves the MarketingSkills relative path to the Kanban `dir:` workspace exactly as normal cwd semantics imply. The mandatory pilot test decides it. A failing test is not permission to invent a wrapper, manually swap files or maintain copies; it triggers the launcher's locked-component/human decision gate.

## Evidence review

The first draft nearly treated nested AGENTS discovery as proof of nested MarketingSkills context. Review separated the mechanisms: the marketing file is found by the skill's relative filesystem instruction, while AGENTS has its own ancestor chain. The final result pins the family cwd, retains one root package, labels the path behavior `SUPPORTED_INFERENCE`, and adds a falsifiable two-family QA gate.

**Review result:** **PASS** — upstream package reuse is viable without middleware/fork/copies, subject to the explicit native-workdir validation in the existing QA runbook.

## Sources

- [MarketingSkills repository/README](https://github.com/coreyhaines31/marketingskills)
- [MarketingSkills product-marketing skill](https://github.com/coreyhaines31/marketingskills/blob/main/skills/product-marketing/SKILL.md)
- [MarketingSkills MIT license](https://github.com/coreyhaines31/marketingskills/blob/main/LICENSE)
- [Hermes skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/)
- [Hermes context files](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files/)
- [Hermes Kanban/workspaces](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban)
- [Agent Skills specification](https://agentskills.io/specification)
- [OpenAI Skills & Plugins](https://learn.chatgpt.com/docs/skills-and-plugins)

