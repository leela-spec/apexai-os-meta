# R02 — Hermes Macro/Meso/Micro Project Knowledge — Work Result

**Research date:** 2026-08-23  
**Repository baseline:** `leela-spec/MasterOfArts@52c8ba0d7692e83891cd281f0525ffcabbd353fd`  
**Track status:** **PASS**  
**Verdict:** `HERMES_NATIVE_MODEL_NEEDS_DOCUMENTED_CONFIGURATION`

## Executive decision

Hermes can represent the required hierarchy without a custom project framework. Use the existing Git repository as the factual artifact store, Hermes context-file discovery as the instruction/context chain, native Kanban parent/dependency/workdir state as the work hierarchy, profiles as shared worker identities, and QMD only as an index over repository truth.

The repository does not yet contain the small root/family/micro context files needed for reliable automatic loading, and its project families have different levels of maturity. Therefore the native model is confirmed but needs documented configuration during the later implementation stage. This research does not add those files or reorganize data.

## Current-repository diagnosis

The live tree contains portfolio families such as `ACIM/`, `Business/`, `IPOS/`, `Lika/`, `OpenClaw/`, and orchestration/reference areas. The root `README.md` establishes the useful invariant that first-level directories are project families and family-internal structure stays inside the family, but it is incomplete relative to the current tree.

Representative findings:

- `ACIM/MyTherapy.md` is a long synthesis blending methods, links and private working material without explicit current/stale/decision markers. It demonstrates rich knowledge but weak lifecycle metadata.
- `Business/Invoices/ssot_rechnungserstellung_macro_meso_micro.md` explicitly declares itself canonical and records rules/decisions/TODOs, but it contains highly sensitive financial and identity data and proposes paths that do not match the current tree. This family requires strict workdir/read scope.
- `IPOS/` is primarily an OpenClaw-era architecture/runbook set with assumptions and future patches; it is useful domain evidence but not authority for the locked Hermes architecture.
- `Lika/Lika Operating System/` and `Lika/Research Files & Problems/` show strong separation of governance, evidence and outputs. The dry-run report also documents cumulative patches, editorial drift and unresolved patch application; this is exactly the kind of active/stale distinction the context chain must expose.
- No current root/family `AGENTS.md` or `.hermes.md` is present. Historical examples under OpenClaw do not configure the current Git root.
- No Awakenings/workshop family currently exists in the live tree. Required workshop simulations are therefore pattern simulations, not claims about an existing path.

## Hermes primitive map

| Primitive | Native purpose | Scope/loading | MoA ownership |
|---|---|---|---|
| Git root/workdir | Project boundary and filesystem scope | Session/task | Entire repository or selected family/micro directory |
| Root `AGENTS.md` | Repository-wide operational rules | Loaded at startup in root→cwd chain | Public/private policy, authority order, routing rules |
| Family `AGENTS.md` | Family rules and pointers | Loaded when cwd/path enters family; deeper wins | Family invariants, canonical entrypoints, exclusions |
| Micro `AGENTS.md` | Deliverable-local constraints | Loaded at/start or progressive navigation | Local acceptance criteria and nearby owners |
| `.hermes.md`/`HERMES.md` | Highest-priority single context-file type | Git-root walk behavior | Alternative to AGENTS, not a second duplicate chain |
| Kanban board/task | Durable work state | Local SQLite, shared by configured profiles | Objective, status, parent/deps, assignee, review, comments, attachments |
| `dir:<absolute path>` workspace | Existing shared directory | Per task | Pins actual family/micro workdir without copying data |
| Profile | Persistent worker identity/config/memory | Across sessions for that profile | Shared specialist, not project facts |
| Project skill | Reusable method | Metadata indexed; body loaded on demand | BMAD/MarketingSkills and approved repo procedures |
| QMD collection | Retrieval index | Queried on demand | Non-authoritative index over files |
| Repository files | Durable factual truth/artifacts | Read on demand or through QMD | Sources, decisions, status, outputs |

Hermes context discovery is decisive: with AGENTS-style files it builds a Git-root-to-cwd chain at startup and can discover deeper files as it navigates. Only one context filename is chosen at a level/session according to precedence. Subdirectory context has a per-file limit and startup context has a total cap, so these files must remain routing/invariant documents rather than mini knowledge bases.

## Macro/meso/micro mapping

| Level | Repository | Kanban | Context | Knowledge retrieval | Output |
|---|---|---|---|---|---|
| Macro — Master of Arts portfolio | Git root + `Orchestration/` authority | One portfolio board by default; top-level parent outcomes | Root AGENTS chain | `moa-orchestration` plus explicit family collections | Cross-family decision/report in repo |
| Meso — project family/offer | First-level family directory | Family parent task; optionally separate native board for sensitivity isolation | Family `AGENTS.md` | Named family collection | Family decision/status/accepted artifacts |
| Micro — concrete deliverable | Existing subdirectory or task-bound output path | Child task with deps, reviewer and `dir:` workspace | Deeper `AGENTS.md` only when repeated local constraints justify it | Family collection filtered to path or exact `get` | Declared task artifact/attachment |

One board preserves native parent/dependency links across the portfolio. Separate boards are justified for access or confidentiality isolation, but Hermes does not support cross-board links; cross-board relationships are then ordinary cited paths/free-text references, not a hidden dependency graph.

## Repeating project pattern

This is a file convention consumed by existing Hermes/Git/QMD mechanisms, not a new service or database:

| Artifact | Owner | Consumer | Rule |
|---|---|---|---|
| Root/family/micro `AGENTS.md` | Repository maintainer/approved reviewer | Hermes, Codex, Claude-compatible clients by explicit/native reading | Concise instructions, authority pointers, privacy and routing only |
| Existing family entrypoint (`README.md` or named SSOT) | Family owner | Humans and all agents | Identifies current scope and canonical facts; do not duplicate source facts into AGENTS |
| Existing sources/evidence files | Research owner | Humans, QMD, specialists | Immutable or versioned evidence, source attribution |
| Existing decision/ADR/governance files | Decision owner | All workers/reviewers | Current accepted decision and supersession links |
| Kanban task | Assignee/reviewer | Hermes workers and dashboard | Transient execution state; not long-term factual truth |
| Accepted output file | Task owner plus reviewer | Downstream tasks/humans | Durable result at declared path |
| QMD index | Operator | Hermes retrieval | Derived and rebuildable; never canonical |

Do not impose empty boilerplate directories on every family. Apply the pattern to active work by pointing context to structures that already exist. Add a micro context file only when the subdirectory has stable repeated constraints; otherwise the Kanban task and family context are sufficient.

## Shared-specialist simulation

### Workshop A (prospective `Awakenings/...` path)

```text
PROFILE: shared Marketing Executive profile
WORKDIR: dir:/repo/MasterOfArts/Awakenings/<workshop-A> (once such a family exists)
AUTO CONTEXT: root AGENTS -> Awakenings AGENTS -> optional micro AGENTS
KANBAN: family parent -> launch child; attachments cite accepted evidence
SKILLS: root-installed MarketingSkills metadata, then selected full skills
QMD: explicit Awakenings collection/path only
OUTPUT: task-declared launch artifact under that family
```

### Existing materially different family (`Lika/`)

```text
PROFILE: same shared Marketing Executive profile
WORKDIR: dir:/repo/MasterOfArts/Lika
AUTO CONTEXT: root AGENTS -> Lika AGENTS
KANBAN: different parent/task/body/reviewer
SKILLS: same installed package; only relevant skill bodies load
QMD: lika collection; no Awakenings collection
OUTPUT: task-declared Lika artifact
```

Only workdir, context chain, task state, collection scope and retrieved files change. The specialist definition and skill package are not copied.

## Token-loading matrix

| Material | When loaded | Relative cost | Control |
|---|---|---:|---|
| Root→cwd context chain | Startup/progressive navigation | Low if concise; capped | Keep rules/pointers, not archives |
| Profile/SOUL/memory | Session start | Low but repeated every session | Keep project facts out |
| Skill metadata index | Startup/discovery | About a few thousand tokens for a normal catalog | Good descriptions; one root install |
| Full skill body/references | Only on activation/need | Medium to high | Activate minimum relevant skills |
| Kanban task/comments/attachments | Assignment/review | Low to medium | Attach durable artifact paths; summarize long history |
| QMD snippets | Query time | Variable | Explicit collection, limit, threshold, then exact `get` |
| Repository source files | On demand | Variable | Read only authoritative/needed files |

## Web-AI and other-client compatibility

Codex natively reads a root-to-cwd `AGENTS.md` chain. Hermes natively supports the same AGENTS chain and project skills at the Git root. MarketingSkills/BMAD use Agent Skills packaging and `.agents/skills/`, which is portable among supporting CLIs. A web ChatGPT/Claude session with repository access can read the same files and follow them explicitly, but cannot be assumed to inherit the local Hermes profile, Kanban database, QMD index, or native project-skill discovery. ChatGPT Work cloud runs on remote infrastructure and accesses the repo through authorized connected apps; this run itself verified private GitHub read/write but not local Hermes/QMD access.

## Gaps and required configuration

- Add and validate the concise context chain during implementation; none exists yet.
- Name the authoritative entrypoint in families where current/stale files are ambiguous.
- Establish workdir discipline and sensitive-family access boundaries.
- Create QMD collections only after the family boundaries and exclusions are approved.
- Do not claim an Awakenings structure exists until it is actually present.
- Validate board design against whether Business/private material requires a separate board/profile.

These are ordinary repository and upstream-Hermes configuration tasks, not missing infrastructure.

## Evidence review

The first draft risked treating every first-level directory as equally current and treating a hypothetical workshop path as real. It was corrected using live-tree samples, explicit sensitivity/staleness findings, and a simulation label. It also avoids duplicating facts into context files or QMD metadata.

**Review result:** **PASS** — the model uses only native Git, context, Kanban, profile, skill and QMD primitives and retains a single factual source.

## Sources

- [Hermes context files](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files/)
- [Hermes Kanban](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban)
- [Hermes profiles](https://hermes-agent.nousresearch.com/docs/user-guide/profiles)
- [Hermes skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/)
- [Codex AGENTS.md discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- Live repository evidence: `README.md`, `ACIM/MyTherapy.md`, `Business/Invoices/ssot_rechnungserstellung_macro_meso_micro.md`, `IPOS/IPOS_AGENT_OPERATING_MODEL.md`, `Lika/Lika Operating System/Governance v1.1.md`, and `Lika/Lika Operating System/Patches/dry-run-report.md` at the baseline commit.

