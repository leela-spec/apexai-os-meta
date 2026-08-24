# R05 — Hermes Specialist Agent + Skill Priming — Work Result

**Research date:** 2026-08-23  
**Repository baseline:** `leela-spec/MasterOfArts@52c8ba0d7692e83891cd281f0525ffcabbd353fd`  
**Track status:** **PASS**  
**Verdict:** `SHARED_SPECIALIST_MODEL_CONFIRMED`

## Executive decision

Represent a reusable specialist as a **Hermes profile with a thin, stable identity and routing description**, backed by shared approved skills. Project facts enter through the root→workdir context chain, the current Kanban task/workspace, repository files and explicitly scoped QMD retrieval. Do not copy the profile per project and do not put project facts in SOUL, USER, MEMORY or the specialist skill.

BMAD personas are skills, not substitutes for Hermes profiles. A profile owns persistent process identity, credentials/config, memory and Kanban routing; a BMAD agent/persona skill temporarily supplies a method/persona inside a session. To avoid duplicate/conflicting persona instructions, keep the Hermes profile functional and neutral when a BMAD persona is activated, and do not encode the same character in both layers.

## Identity/priming layer map

| Layer | Purpose | Scope | Automatically loaded? | Mutable by Hermes? | Shared across projects? | Project facts? |
|---|---|---|---:|---:|---:|---:|
| Hermes profile | Separate Hermes home/config/keys/sessions/skills/memory; Kanban routing description | Persistent worker/process | Selected at process start | Config/user controlled | Yes | No |
| `SOUL.md` | Global personality/identity for that Hermes home | Profile | Yes when configured | User/agent only under allowed writes | Yes | No |
| `USER.md` | Small stable operator preferences | Profile | Yes; documented size cap ~1,375 chars | Memory system/user | Yes | No project facts |
| `MEMORY.md` | Small durable cross-session memory | Profile | Yes; documented size cap ~2,200 chars | Automatic or approval-staged | Yes | No canonical project facts |
| Root/family/micro `AGENTS.md` | Operational rules, authority pointers, scoped stable context | Git root→cwd | Yes/progressively | Repository change process | Root/family/micro | Only concise stable pointers/invariants |
| Project skill | Approved reusable method/package at Git root | Repository | Metadata indexed; body on activation | Not Curator-managed; ordinary repo writes possible | Yes in repo | Procedure, not facts |
| Local/profile skill | Worker-local reusable method | Profile home | Metadata indexed; body on activation | Depending provenance/policy | Yes for that profile | Procedure, not facts |
| BMAD persona/agent skill | Task persona/menu/method; loads BMAD config and persistent-fact references | Activated session | No; explicit/semantic activation | Upstream/team override mechanism | Yes | References only |
| Kanban assignee/profile | Durable routing to matching profile | Board/task | On dispatch | Native task operations | Across tasks in board | No hidden facts |
| Task body/comments/attachments/workdir | Objective, current execution/review state and durable artifact pointers | Task | On assignment/review | Maker/reviewer via Kanban | Task-specific | Current task facts, not long-term SSOT |
| QMD | On-demand retrieval from repo truth | Named collection/path | Only on tool call | Derived index | As authorized | No canonical facts |

Hermes project skills are discovered only at the nearest Git root under `.hermes/skills/` or `.agents/skills/`. A nested family `.agents/skills/` in the same monorepo is not a second project-skill root. This supports one package install at the MasterOfArts root. Context files are different: AGENTS-style context chains can be nested to the workdir.

## Recommended specialist representations

All fields below map to an existing upstream artifact, not a custom profile schema.

| Candidate | Persistent profile responsibility | Skills activated | Project priming | Output/review contract |
|---|---|---|---|---|
| Marketing Executive | Thin mission/description for marketing task routing; approved toolset/model | MarketingSkills; BMAD PM/analyst only when its workflow is actually requested | Family workdir, family marketing context, task, scoped QMD | Task body declares artifact; independent reviewer for evidence/claims/public release |
| Research Strategist/Researcher | Official-source research mission and citation discipline | Official research/QMD skill; approved research procedure | Root/family context, evidence sources, track task | Evidence matrix + result at declared path; request review |
| Workshop Designer | Learning/workshop design mission, no marketing persona baked in | Approved workshop method skill if present; relevant BMAD planning skill only when applicable | Family/micro context and accepted research | Workshop design artifact; family reviewer |
| Independent Reviewer | Skeptical evidence/acceptance mission; separate profile/home/memory | Evidence-review/checklist skill only | Review task, maker artifact, cited sources, acceptance criteria | PASS or native request-changes reason; no maker hidden chat |

Role mission and routing description belong to the profile; tone only where it materially improves the role belongs in SOUL. Activation conditions and reusable procedure/output rules belong in skill metadata/body. Allowed tools/models/credentials belong to profile configuration. Project references belong to AGENTS/task; exact facts remain in repository files. Review/escalation belongs to Kanban state plus the task's acceptance criteria.

## Skill activation and trust

Hermes indexes skill name/description metadata at startup (roughly a few thousand tokens for a normal catalog), loads the full `SKILL.md` only when selected, and reads referenced resources only on demand. Project skill precedence is above profile-local and external directories. A Git-root project skill must pass project trust/security scanning. Project skills are excluded from Curator maintenance; hub skills are protected. External writable directories and ordinary repository permissions remain separate risks.

Slash-command exposure depends on the installed skill and runtime integration. Do not assume every upstream skill creates a slash command. Invocation by semantic trigger/explicit skill name remains the portable baseline. Usage telemetry records view/use/patch behavior for eligible local skills; bundled and hub-installed exclusions and Curator provenance are detailed in R06.

## Shared Marketing specialist — two-project simulation

### Project A — prospective Awakenings workshop

```text
PROFILE/ROLE LOADED: Marketing Executive profile; neutral functional SOUL
ROOT CONTEXT LOADED: MasterOfArts authority/privacy/routing
FAMILY CONTEXT LOADED: Awakenings context (only once a real path exists)
MICRO CONTEXT LOADED: workshop constraints if a micro AGENTS file exists
KANBAN TASK STATE: launch objective, deps, reviewer, dir:/repo/.../Awakenings
SKILL INDEX: one root MarketingSkills catalog + approved BMAD catalog
FULL SKILLS ACTIVATED: product-marketing, customer-research, launch, social as needed
QMD COLLECTION/SCOPE: future explicit Awakenings collection/path
PROJECT FILES RETRIEVED: accepted offer/audience/evidence only
MODEL CALLS: provider reasoning + local QMD retrieval/model work
OUTPUT: task-declared launch artifact in Awakenings family
```

This is a prospective simulation because no Awakenings/workshop directory exists at the baseline.

### Project B — Lika offer

```text
PROFILE/ROLE LOADED: same Marketing Executive profile
ROOT CONTEXT LOADED: same root authority/privacy/routing
FAMILY CONTEXT LOADED: Lika governance/evidence routing
MICRO CONTEXT LOADED: only the selected Lika subproject context
KANBAN TASK STATE: distinct task/reviewer; dir:/repo/MasterOfArts/Lika
SKILL INDEX: same root packages
FULL SKILLS ACTIVATED: product-marketing, content-strategy, copywriting as needed
QMD COLLECTION/SCOPE: [moa-lika]
PROJECT FILES RETRIEVED: Lika evidence and accepted SSOT only
MODEL CALLS: provider reasoning + local retrieval
OUTPUT: task-declared Lika marketing artifact
```

The role/profile/skills do not change. Workdir, context, task, marketing-context file, retrieval scope and output path do. This passes the non-duplication test.

## Reviewer separation simulation

1. Researcher task declares artifact, evidence sources and acceptance criteria.
2. Maker profile writes the artifact and calls native `kanban_request_review(summary, reviewer)`.
3. Review state, summary, comments, attachments and the `dir:` workspace are durable in the Kanban DB.
4. A distinct reviewer profile/process is assigned. Its own profile/memory/session is separate; it receives task state and durable artifacts, not hidden maker chat.
5. Reviewer reopens cited sources and either passes according to the workflow or calls `kanban_request_changes(reason)`.
6. Hermes routes changes back to the original implementer with the reason preserved; the maker revises and requests review again.

A separate profile/process is required for genuine context separation and is upstream-native. The token cost is the reviewer's own concise profile/context plus task/artifact/evidence; it avoids paying for the maker's full conversation history.

## BMAD agents versus Hermes profiles

Current BMAD has a first-party `hermes` installer target at project `.agents/skills/` and profile-local `~/.hermes/skills`. BMAD agent skills such as `bmad-agent-architect` load a `customize.toml`, `_bmad` config and persona/menu, and keep the persona active in the session. They are therefore task methodology/persona packages.

| Question | Result |
|---|---|
| Does BMAD skill replace Hermes profile? | No. It does not own a separate Hermes home, credentials, sessions, memory or Kanban routing process. |
| Can profile load BMAD persona/workflow skill? | Yes; BMAD explicitly installs as Agent Skills for Hermes. |
| Persistent identity owner | Hermes profile/SOUL/config. |
| Temporary method/persona owner | Activated BMAD agent/workflow skill. |
| Conflict risk | Yes if the same persona, mission or output contract is duplicated. Keep profile neutral and activate one task persona. |

Do not encode Winston or another BMAD character into the Marketing/Researcher profile. Do not use BMAD `persistent_facts` to mirror project SSOT; if used, point only to approved files and accept the activation token cost.

## Organization/project ownership matrix

| Knowledge | Upstream place |
|---|---|
| Public/private and architecture policy | Root approved repository context/Orchestration authority |
| General brand/business identity | Root/family approved factual file, linked by context |
| Specialist behavior | Profile mission/config plus approved skill |
| Family facts | Family repository SSOT/evidence and family context pointer |
| Micro facts | Task/brief/source file and optional micro context |
| Reusable procedure | Project/local/hub skill by ownership/provenance |

## Cross-client portability

| Artifact | Hermes | Codex CLI | Claude Code | Web ChatGPT/Claude with repo access |
|---|---|---|---|---|
| Root/family `AGENTS.md` | Native chain | Native chain | Explicit/native depending client | Explicit file reading |
| `.agents/skills/` package | Native at Git root | Agent Skills/native | Upstream often uses `.claude/skills`; `.agents` support depends client | Ordinary files unless installed as product skill/plugin |
| BMAD persona skill | Native after Hermes target install | BMAD Codex target | BMAD Claude target | Explicit file reading; local `_bmad` scripts unavailable unless execution environment has them |
| Hermes profile/SOUL/memory | Native | Inaccessible/runtime-specific | Inaccessible/runtime-specific | Inaccessible local state |
| Kanban DB | Native | Not inherently accessible | Not inherently accessible | Inaccessible local state |
| Repository artifacts | Native files | Native files | Native files | Available through authorized repo connector |
| QMD index/MCP | Native local MCP | Only if separately connected | Only if separately connected | Not available to cloud web session by default |

OpenAI official documentation confirms ChatGPT Work cloud runs remotely and reaches local/device resources only through uploads, projects or authorized apps; this run observed private GitHub access but no local Hermes/QMD connector.

## Token-loading estimate

| Input | Typical order of magnitude | Loading rule |
|---|---:|---|
| Profile/SOUL + `USER.md`/`MEMORY.md` | ~1–2k tokens if kept within documented caps | Every profile session |
| Root/family/micro context | ~1–6k target, bounded by Hermes caps | Startup/progressive path |
| Skill index | ~3k for normal catalog | Startup/discovery |
| Full Marketing/BMAD skill | ~2–10k each plus needed references | Only on activation |
| Kanban task/comments | ~0.5–3k | Assignment/review |
| QMD passages | ~1–4k per bounded retrieval round | Tool call |
| Output | Task-dependent | Provider generation |

The control is native progressive disclosure: concise profile/context, minimum skill activation, scoped QMD, exact `get`, and durable artifact handoffs. No custom prompt compressor/router is proposed.

## Required configuration only

- One Hermes profile per durable shared specialist/reviewer role where separate memory/process identity is needed; never share one profile concurrently across processes.
- Clear profile descriptions for Kanban routing; distinct reviewer profile.
- Root/family context chain and `dir:` workspaces from R02.
- Root project skills plus trust review; no nested copied packages.
- Approved tool/model/credential configuration per profile.
- QMD family scoping and task output/review contracts.

## Evidence review

Review corrected an intuitive but unsafe merger of BMAD persona and Hermes profile. Upstream BMAD evidence shows the agent persona persists inside a session, while Hermes profiles own persistent runtime identity. The final design assigns one owner per concern and proves the reviewer handoff using durable native state.

**Review result:** **PASS** — shared specialists work across projects without a prompt router, per-project agent copies or manual context paste.

## Sources

- [Hermes profiles](https://hermes-agent.nousresearch.com/docs/user-guide/profiles)
- [Hermes context files](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files/)
- [Hermes skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/)
- [Hermes Kanban](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban)
- [Hermes memory](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory/)
- [BMAD Hermes/Codex platform targets](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/tools/installer/ide/platform-codes.yaml)
- [BMAD architect agent skill](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/src/bmm-skills/agents/bmad-agent-architect/SKILL.md)
- [Agent Skills specification](https://agentskills.io/specification)
- [OpenAI ChatGPT Work overview](https://learn.chatgpt.com/docs/enterprise/chatgpt-work-overview)

