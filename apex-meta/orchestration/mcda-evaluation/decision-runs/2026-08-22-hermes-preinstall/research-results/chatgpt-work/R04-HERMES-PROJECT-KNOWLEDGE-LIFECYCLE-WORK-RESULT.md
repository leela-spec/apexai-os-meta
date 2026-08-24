# R04 — Hermes Project Knowledge Lifecycle — Work Result

**Research date:** 2026-08-23  
**Repository baseline:** `leela-spec/MasterOfArts@52c8ba0d7692e83891cd281f0525ffcabbd353fd`  
**Track status:** **PASS**  
**Verdict:** `PROJECT_KNOWLEDGE_LIFECYCLE_CONFIRMED`

## Executive decision

Project truth remains in ordinary, human-readable repository files. Hermes context files route workers to that truth; Kanban owns execution state; QMD owns only a rebuildable retrieval index; profile memory owns small cross-session user/worker preferences; skills own reusable procedures. This single-owner model supports messy existing families, new micro-projects, change, closure and restart without a custom KB or repeated rewriting of facts.

The implementation stage must identify an authoritative entrypoint and supersession/status signals for each active family. It must not normalize the tree or duplicate all content into a new template.

## Source-of-truth matrix

| Information type | Authoritative owner | Consumers | Update trigger | Explicitly not owner |
|---|---|---|---|---|
| Organization scope/architecture/policy | Approved root Orchestration/ADR/scope files | Humans, root context, all agents | Human-approved decision | Memory, QMD, task comments |
| Family facts/domain model | Existing approved family SSOT/governance/entrypoint | Family workers, reviewers, QMD | Accepted evidence/decision | Profile/SOUL, skill body |
| Micro-project facts/requirements | Nearest approved brief/spec/source file | Task worker/reviewer | Requirement or source change | Global memory |
| Evidence/raw sources | Existing source/research files with citations | Researchers/reviewers/QMD | Source acquisition/correction | Synthesized summary alone |
| Accepted decision | ADR/governance/decision file with status/supersession | All downstream work | Decision gate | Kanban status alone |
| Current execution state | Hermes Kanban task status, assignee, deps, comments, attachments | Dispatcher, maker, reviewer | Work event | Repo factual SSOT |
| Accepted deliverable | Declared repository output path; task attachment points to it | Humans/downstream agents | Review PASS | Hidden chat/session |
| Organization/user preference | Root policy when normative; `USER.md` only for small stable operator preference | Profile sessions | Operator approval | Family fact files |
| Reusable procedure | Approved skill | Supporting runtimes | Review/promotion/upstream update | MEMORY.md fact dump |
| Retrieval state | QMD index/config/status | Hermes QMD client | `qmd update/embed` | Canonical truth |
| Emergency file recovery | Hermes checkpoint and Git history | Operator | Pre-write/commit | Decision record |

## Operable project knowledge package

An active project is operable when the following roles are satisfied by existing or deliberately added ordinary files; filenames may follow the family's existing convention.

| Role | Minimum artifact | Consumer |
|---|---|---|
| Entry/routing | Family entrypoint naming current scope, authority and important paths | Human, AGENTS/context, web AI |
| Stable automatic context | Concise root/family AGENTS chain; micro only if repeated local constraints exist | Hermes/Codex and explicit readers |
| Evidence | Source files/links with provenance and date | Researcher, reviewer, QMD |
| Current accepted facts | One named SSOT/governance/brief, not a copied summary in every agent | Specialists, downstream work |
| Decisions | Status-bearing ADR/decision/governance artifact with supersession references | All clients |
| Work state | Kanban task with objective, deps, assignee, comments, reviewer, workdir and attachments | Hermes dispatcher/reviewer |
| Output | Declared durable path and acceptance evidence | Humans/downstream work |
| Retrieval | QMD collection/path metadata and successful freshness check | Hermes only |

For `Lika/`, current governance/evidence/patch documents already satisfy many roles, but the entrypoint must expose whether patches are proposed/applied and fix broken/misspelled references. For `Business/Invoices`, the declared SSOT is useful but sensitivity and path drift must be made explicit. For `IPOS/`, the entrypoint must say the documents are OpenClaw-era research/design inputs, not current Hermes architecture. For `ACIM/`, a maintainer must distinguish personal reference material from active project decisions.

## Freshness lifecycle

```text
new/changed source
 -> evidence file updated with date/provenance
 -> researcher updates synthesis only where conclusion changes
 -> decision owner/reviewer accepts, rejects, or marks OPEN
 -> authoritative file records status/supersession
 -> Kanban task links the accepted artifact and closes/reopens dependencies
 -> qmd update + qmd embed refresh derived index
 -> downstream worker retrieves the accepted source and cites it
```

The same fact is not manually copied into AGENTS, MEMORY and QMD context. AGENTS contains only the stable routing rule (for example, which file is authoritative). QMD indexes the updated file. Kanban records that the update happened and which artifact passed.

## Staleness and conflict handling

Use the workflow evidence states: `VERIFIED_OFFICIAL`, `SUPPORTED_INFERENCE`, `OPEN`, and `CONTRADICTED`. When files disagree:

1. preserve both sources;
2. identify authority, date and scope;
3. mark the contradiction in the current synthesis/decision artifact;
4. do not silently merge or overwrite evidence;
5. escalate only if the contradiction reaches a launcher human gate;
6. record the accepted resolution/supersession and refresh QMD.

Filename words such as `final`, `new`, `SSOT`, or `v2` are not sufficient authority. Lika's dry-run finding that cumulative patches drifted into editorial rewriting is a concrete reason to require status/supersession evidence. Historical OpenClaw architecture cannot overrule ADR-002.

## Update responsibility

| Event | Responsible role | Review/gate |
|---|---|---|
| New external evidence | Researcher | Independent evidence review before decision use |
| Family fact correction | Family owner/maker | Family reviewer; CEO only if decision gate is reached |
| Architecture/scope change | Decision owner | Explicit human CEO gate |
| Task progress | Assigned Hermes profile | Native Kanban state/comment |
| Accepted artifact | Maker plus distinct reviewer where required | `request_review` / PASS or `request_changes` |
| QMD refresh | Task owner/operator | Deterministic freshness check before dependent retrieval |
| Memory/procedure promotion | Operator/skill reviewer | Governance from R06, not automatic fact promotion |

## QMD refresh mechanism

QMD scans the canonical checkout. After an accepted material file change, run native `qmd update`, then `qmd embed` for new/changed content, and verify `qmd status`. Record completion in the Kanban task. If a task begins after an uncertain interval, refresh before high-stakes retrieval. QMD's index/config is rebuildable local state and must not be committed as a second truth store.

## Restart/resume simulation

1. A Hermes process stops after a maker writes a draft and comments on the task.
2. Repository draft persists at its declared path; Kanban SQLite preserves status, comments, assignee, workdir and attachments; the profile session record may help but is not required authority.
3. Dispatcher reclaims or reassigns the durable task under documented failure/reclaim behavior.
4. New process loads profile plus root→workdir context, reads task body/comments/attachments and exact repository artifact.
5. It checks QMD freshness, retrieves only missing evidence, and continues.
6. Reviewer receives the artifact/evidence/task state, not hidden maker conversation, and either passes or requests changes.

No manual chat copy is needed.

## Cross-project learning without factual contamination

| Example | Destination | Why |
|---|---|---|
| “Awakenings audience prefers X” | Awakenings family evidence/SSOT | Project fact |
| “For launch work, check positioning before copy” | Approved reusable skill | Procedure |
| “Operator forbids public S+ content” | Root normative policy (and small USER preference only if non-project) | Organization/operator rule |
| “QMD scope was stale” | Task incident/comment; promote a generic refresh procedure only after review | Operational observation vs procedure |

Project B can use the accepted generic launch procedure while QMD and workdir stay scoped to B; it cannot see A's factual collection unless the task explicitly authorizes it.

## Required user stories

### US-A — Existing messy project enters the system

Inspect rather than move files; name the existing authoritative entrypoint and current/stale signals; add concise routing context only when approved; create family QMD scope; create a Kanban assessment task. Lika is the representative case. PASS because content is not reorganized or rewritten into another KB.

### US-B — New concrete project under existing family

Create a Kanban child task with `dir:` family/micro workdir, point to the approved family entrypoint and task brief, add a micro context file only if stable repeated constraints exist, declare the output path, and query only the family collection.

### US-C — Project changes over time

Update evidence, review the conclusion, record decision/supersession, attach accepted artifact, refresh QMD, then reopen/unblock dependent native tasks. Old evidence stays available and marked, not silently deleted.

### US-D — Project closes

Mark final task/parent done or archived; make the final status/decision/output discoverable in the family entrypoint; preserve sources and accepted artifacts; refresh QMD or exclude the closed collection from default queries. Do not convert the whole project into profile memory.

## Human/web-AI access

Repository Markdown remains readable by humans and any web AI with authorized repo access. This run verified that ChatGPT Work cloud could read the private repository through GitHub and persist designated result files. Web agents cannot be assumed to access local Kanban SQLite, Hermes profiles/memory, or QMD. Therefore every durable handoff needed outside Hermes must point to repository artifacts; Kanban/QMD remain operational accelerators, not sole knowledge owners.

## Manual burden

Humans approve material decisions, curate authority/supersession, review sensitive changes, and resolve decision-gate contradictions. Workers maintain one fact location plus a task link and perform a deterministic index refresh. They do not paste facts into multiple agents, rewrite a separate KB, or synchronize runtimes. This is a reasonable governance burden, not duplicate manual truth.

## Unresolved implementation checks

- Choose/repair family entrypoints for ACIM, Business, IPOS and Lika.
- Decide board/profile access isolation for sensitive Business/ACIM content.
- Validate root/family context size and authority links.
- Pilot the QMD freshness checklist and restart/reviewer handoff.
- Do not create an Awakenings package until its real source material/path exists.

## Evidence review

Review removed a proposed universal directory template because it would reorganize data and become a framework. The result now specifies semantic roles that existing files can satisfy, keeps one owner per fact, and makes QMD/Kanban derived operational state.

**Review result:** **PASS** — the lifecycle is complete, restartable and cross-client-readable without a custom KB or duplicate truth.

## Sources

- [Hermes context files](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files/)
- [Hermes Kanban](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban)
- [Hermes memory](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory/)
- [Hermes skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/)
- [QMD upstream](https://github.com/tobi/qmd)
- Live repository samples listed in R02 at the baseline commit.

