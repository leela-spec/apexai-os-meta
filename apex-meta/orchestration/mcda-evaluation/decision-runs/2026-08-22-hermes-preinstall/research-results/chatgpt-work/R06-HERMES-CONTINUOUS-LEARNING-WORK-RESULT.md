# R06 — Hermes Continuous Learning — Work Result

**Research date:** 2026-08-23  
**Repository baseline:** `leela-spec/MasterOfArts@52c8ba0d7692e83891cd281f0525ffcabbd353fd`  
**Track status:** **PASS**  
**Verdict:** `LEARNING_REQUIRES_GOVERNANCE_CONFIGURATION`

## Executive decision

Hermes' native memory, skill self-improvement, usage provenance, Curator, backups, ledger and rollback are sufficient. Configure conservative governance: memory writes require approval; repository facts stay in repository files; upstream BMAD/MarketingSkills remain project skills managed by their upstream update path; Curator is prune-only, excludes bundled skills, retains backups, never auto-purges, and is first exercised with dry-run/on-demand review. LLM consolidation remains off until the pilot shows a real duplicate-skill problem.

No cross-runtime memory synchronization is required or allowed. Cross-client learning is shared only when it is an approved repository artifact or portable skill.

## Learning-destination matrix

| Learning type | Exact storage | Created by | Auto/manual | Curator? | Cross-project? | Canonical truth? | Token impact |
|---|---|---|---|---:|---:|---:|---|
| Current reasoning | Conversation/session | Provider/Hermes | Automatic | No | No | No | Conversation context |
| Stable operator preference | Profile `USER.md` | User/memory process | Approval-staged | No | Profile only | Preference only | Injected every session; ~500 tokens cap class |
| Small durable lesson | Profile `MEMORY.md` | Memory tool/background review | Auto by default; configure approval | No | Profile only | No project truth | Injected every session; ~800 tokens cap class |
| Background-created procedure | `~/.hermes/skills/<skill>/` with agent-created provenance | Background self-improvement review | Automatic candidate creation | Yes | Profile skills across its projects | Procedural only | Metadata always; body on use |
| User-directed procedure | `~/.hermes/skills/<skill>/` | Foreground user-directed `skill_manage` | Manual intent | Unmanaged unless explicitly adopted | Profile | Procedural only | Same |
| Bundled skill | Hermes distribution | Upstream | Install/update | Archive-eligible by default; configure exempt | Profile/install | Upstream procedure | Index/body |
| Hub skill | Hub lock/provenance | Upstream installer | Manual install/update | Always exempt | Profile/install | Upstream procedure | Index/body |
| Project BMAD/MarketingSkills | Git-root `.agents/skills/` | Upstream package install/update | Manual approved | Excluded | Repository | Upstream procedure | Index/body |
| Project fact/evidence/decision | Repository family files | Maker/reviewer/decision owner | Reviewed | No | Only by authorized file access | **Yes** | On demand/QMD |
| Kanban state | `~/.hermes/kanban.db` | Worker/dispatcher/reviewer | Native work events | No | Board | Execution state only | On assignment/review |
| QMD index | Local QMD SQLite/cache | `qmd update/embed` | Deterministic/manual gate | No | Authorized collections | No; derived | Query passages only |

## Exact learning triggers and model calls

| Trigger | Destination/action | Model call? | Governance |
|---|---|---:|---|
| Agent notices a novel repeatable method during task | May offer/save a skill through supported self-improvement path | Provider/background auxiliary call | Candidate; review before reliance |
| User explicitly asks to create/update skill | Foreground `skill_manage`; user-directed/unmanaged provenance | Normal provider call | Review, optionally pin; do not auto-adopt |
| Background memory review | Proposes/writes USER/MEMORY according to configuration | Auxiliary provider call | `memory.write_approval: true` stages writes |
| Curator inactivity pass | Deterministic active→stale→archive transitions | No for pruning | Dry-run/audit; conservative thresholds |
| Curator consolidation | Reads/patches/merges eligible agent-created skills | Yes; official docs estimate a sweep can take 50–100 API calls | Keep off initially |
| User edits project knowledge | Repository change + review | Normal task calls | Canonical project workflow |
| QMD refresh | Rescan/embed local index | Local deterministic/local model | Not learning truth; rebuild derived state |

Only the background self-improvement path marks a skill agent-created automatically. Foreground user-directed skills are deliberately unmanaged until `hermes curator adopt` is explicitly used. Curator never manages hub, external or project-local skills; bundled skill pruning is separately configurable.

## Upstream-skill protection

Install BMAD and MarketingSkills at the Git root through their supported package paths and review the committed/pinned upstream content. Project skills are outside Curator scope. Do not `adopt` them; do not edit upstream files with `skill_manage`; rely on repository permissions/review and the upstream update process. Hermes documentation notes that project skills have highest precedence and are security scanned/trusted.

Set `curator.prune_builtins: false` so bundled Hermes skills are not archived. Hub skills are already immutable to Curator. For an approved local learned skill, pinning prevents automatic transitions and tool-driven deletion, but current docs state edits/patches can still occur; use user-directed provenance plus review/OS permissions when content must be frozen.

## Learning-promotion workflow

```text
Project A launch task experience
 -> task comment records observed improvement and evidence
 -> classify: project fact or reusable procedure
 -> project fact updates family evidence/SSOT only
 -> procedure becomes a candidate user-directed local skill (or background candidate)
 -> independent review checks generality, sources, privacy and overlap
 -> accept: keep/pin or explicitly adopt under Curator policy
 -> reject: archive/delete with ledger/backup evidence
 -> Project B discovers metadata, activates skill on matching task
 -> usage telemetry records actual use; B gets only its own files/QMD scope
```

The review is ordinary human/Kanban/repository governance around an existing skill mechanism, not a new service.

## Fact versus procedure

| Observation | Destination | Reason |
|---|---|---|
| “Awakenings audience prefers X” | Awakenings evidence/SSOT | Family fact; must not leak globally |
| “For launch tasks, first check positioning context” | Approved reusable skill | General procedure |
| “Operator prefers no public S+ content” | Root normative policy; small USER preference only if appropriate | Organization/operator constraint |
| “Task failed because QMD collection was stale” | Task incident first; promote a generic refresh checklist after repeated/reviewed evidence | Separate event from reusable method |

Everything is not dumped into MEMORY and every lesson is not automatically converted into a skill.

## Curator/memory recommendation — **DO NOT EXECUTE**

```yaml
# Profile config.yaml — DO NOT EXECUTE; validate in QA against installed release
memory:
  write_approval: true

curator:
  enabled: true
  interval_hours: 168
  min_idle_hours: 2
  stale_after_days: 30
  archive_after_days: 90
  consolidate: false
  prune_builtins: false
  archive_ttl_days: 0
  backup:
    enabled: true
    keep: 5

skills:
  ledger: true
```

Operational start:

```bash
# DO NOT EXECUTE
hermes curator status
hermes curator list-unmanaged
hermes curator run --dry-run
hermes curator ledger
```

Keep automatic deterministic pruning enabled only after the dry-run inventory is understood. Never bulk-adopt unmanaged skills. Consolidation stays false because it is costly and structurally mutative. Archive is recoverable; purge is explicit only and remains disabled by TTL 0. Review reports and ledger after each early run.

## Token/cost analysis

| Mechanism | Cost behavior |
|---|---|
| USER/MEMORY | Injected every profile session; hard small caps, so every line has recurring cost |
| Skill index | Metadata only at startup, roughly a few thousand tokens for normal catalogs; duplicates pollute routing |
| Full skill | Loaded only on activation; references/resources on need |
| Background memory/self-improvement | Auxiliary provider calls; frequency/content dependent |
| Curator prune | Deterministic, no LLM/API cost |
| Curator consolidation | Optional and expensive; official docs say a full sweep commonly uses 50–100 API calls |
| QMD | Local model/index cost; only selected passages consume provider input tokens |

## Cross-project simulation

1. Lika launch task observes a strong evidence-review ordering; event and evidence remain in Lika task/files.
2. A generic procedure is written as a user-directed local skill, reviewed for removal of Lika facts, and kept outside upstream skill trees.
3. Later the shared Marketing profile receives a different family task. Skill metadata matches and the body loads on demand.
4. Workdir/context and QMD are scoped to Project B. The learned procedure says how to work, not what Lika's audience/facts are.
5. Usage telemetry increments. If the procedure proves narrow or redundant, it is reviewed/archived with ledger and backup.

## Failure/rollback simulation

| Failure | Detection | Native response |
|---|---|---|
| Bad learned skill | Output review/usage report | Disable/archive; inspect ledger; rollback entry or restore backup |
| Near-duplicate skills | Catalog/Curator report | Manual review; consolidation remains opt-in; archive rejected duplicate |
| Needed skill archived | `list-archived`, missing activation | `hermes curator restore <skill>`; pin if appropriate |
| Wrong skill patched | Append-only ledger | `hermes curator rollback <entry-id>` for exact mutation |
| Bad whole Curator run | Run report/snapshot | `hermes curator rollback --list` then rollback chosen snapshot |
| BMAD/MarketingSkills update | Git/package diff and upstream version | Review native update; project context remains separate; revert normal Git commit if rejected |
| Learned skill conflicts with upstream name | Precedence/routing review | Rename/archive learned skill; do not patch upstream package |

Backups occur before real Curator runs and default to five. Whole-run rollback itself snapshots the pre-rollback state. Single-entry rollback is fail-closed on safety capture. The ledger is audit evidence but not a mutation gate; repository protections still matter.

## Evidence review

Review corrected three material risks: treating foreground-created skills as automatically Curator-managed, assuming pinning freezes edits, and enabling LLM consolidation by default. Current official Curator docs contradict all three. The result now uses explicit provenance, review, backups and minimal recurring memory.

**Review result:** **PASS** — native learning is valuable and recoverable with configuration; no synchronization service or factual contamination is required.

## Sources

- [Hermes memory](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory/)
- [Hermes skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/)
- [Hermes Curator](https://hermes-agent.nousresearch.com/docs/user-guide/features/curator)
- [Work with skills](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills)
- [Hermes Kanban](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban)

