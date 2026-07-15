# Leela × Apex KB modular waterfall redesign plan

Status: architecture and implementation plan only. No repository changes were made.

## Executive decision

**KEEP** the useful Apex KB lifecycle: source custody → deterministic structure → targeted semantic analysis → compiled knowledge → independent acceptance → retrieval.

**STOP** using an exhaustive all-source/all-topic custody artifact as the browser's semantic work queue.

**NORMALIZE** each fact so it has one owner:

- source identity, hash, path, type: one source record;
- headings and links: one structure record per readable source;
- topic signals: one sparse topic/source relation;
- semantic judgment: one topic/source review record;
- final claims: compiled page;
- acceptance verdict: acceptance artifact.

**SHARD** browser-facing data into small topic/query/source files. Prefer many bounded files over aggregate JSON. Large derived search databases may remain machine-only and must never be browser prompt inputs.

**NARROW** in waves rather than applying a blind top-N cutoff. Apex requires continued reading while a known readable source could resolve an unanswered critical/routine question.

## 1. Problem statement

The current system contains three good capabilities:

1. deterministic source inventory and structural extraction;
2. semantic relevance/authority review;
3. concise evidence-backed dossiers.

The failure is in their handoffs.

### Confirmed inefficiencies

- **DUPLICATE:** `source-postings.json` and `heading-map.json` contain the same 4,310 headings.
- **MULTIPLY:** the combined topic map embeds those headings once for every topic: 43,100 heading objects.
- **OVER-INCLUDE:** every topic receives all 197 source records, even without a topic signal.
- **ZERO-SIGNAL:** 586 of 1,970 topic/source records have no configured topic signal.
- **RE-EXPAND:** projections, ledgers, and atlasses represent the candidate set again.
- **LOW DENSITY:** Skill Tree reviews 197 candidates to retain 5 material sources; 192 ledger entries say they do not directly support a final material claim.
- **MIX CONCERNS:** exhaustive custody, semantic navigation, review history, and human-readable provenance are treated as simultaneous browser inputs.
- **ATOMIC DELIVERY:** large multi-file semantic batches and raw Git blob/tree actions create transport/action risk unrelated to reasoning quality.

### Root cause

The system lacks a strict distinction between:

```text
“We deterministically considered the entire source universe”
                         versus
“The browser should read this source for this question now.”
```

The first is custody. The second is a work instruction. They must not be the same artifact.

## 2. Verification against the current Apex KB skill

Baseline inspected:

- `.claude/skills/apex-kb/SKILL.md`
- `references/semantic-value-contract.md`
- `references/kb-contract.md`
- `references/browser-git-connector-semantic-runbook.md`
- `references/semantic-run-ledger.schema.json`
- `references/acceptance-tests.md`
- `examples/lifecycle-runbook.md`
- live `apex-meta/scripts/apex_kb.py`
- Leela repository-local semantic contract and manual browser prompts

### What Apex KB currently intends

| Apex principle | Current authoritative intent |
|---|---|
| **TARGET LOCK** | Define stable critical/routine questions and answer requirements before source selection. |
| **RANKING ONLY** | Phase 0 rankings nominate candidates; rankings never prove relevance or authority. |
| **ONE TOPIC** | Browser connector work handles one topic per context. |
| **CONTINUE BY GAP** | Read more only while a known readable source could resolve an unanswered critical/routine query. |
| **MINIMUM TOPOLOGY** | Create only independently useful summary/concept/entity pages. |
| **MATERIAL ONLY** | Compiled pages list reviewed, materially used sources; unopened candidates stay in the ledger. |
| **CLEAN ACCEPTANCE** | Evaluate pages against questions first; then verify selected claims against resolved evidence passages. |
| **TRUTHFUL STATE** | `partial`, `analysis_complete_unvalidated`, `compiled_unvalidated`, and `query_ready` have strict gates. |
| **CANONICAL/DERIVED** | Canonical custody/semantic records survive; Phase 0/search/query outputs are rebuildable. |

### Where Leela diverged

The repository-local semantic contract still says:

- work one topic at a time;
- use Phase 0 rankings only to locate candidates;
- read sources until locked questions are resolved.

But `MANUAL_BROWSER_FULL_EXECUTION_PROMPT.md` adds a stronger, conflicting requirement:

- read the complete 9.17 MB map;
- do not reduce the 197 candidates;
- create one ledger and atlas disposition for all 197 candidates per topic;
- make acceptance compare every candidate against the complete atlas/ledger.

The reason-coded repair prompt preserves this 197-per-topic requirement through projections.

**Finding:** the explosion is not required by the core Apex KB skill. It is introduced by the Leela exhaustive-map/manual-prompt extension and reinforced by the runtime atlas-consistency checks.

### Runtime overlap inside Apex Phase 0

The live runtime currently has two routing mechanisms:

1. `phase0` creates `topic-source-rankings.json` and includes only files with keyword hits, ranked by hit count.
2. `corpus-map` creates an exhaustive topic map and appends every source to every topic, including zero-signal sources.

The first already matches the skill's browser-routing intent. The second is useful only as machine custody evidence, but Leela promoted it into a semantic completeness requirement.

## 3. Target macro flow

### Macro waterfall

```text
MASSIVE SOURCE PILE
197 canonical files remain where they are
        │
        ▼
L0 — SOURCE REGISTRY
One ID/path/hash/type record per source
        │ 100% of sources
        ▼
L1 — STRUCTURE INDEX
One small headings/links/frontmatter record per readable source
        │ no copied source bodies
        ▼
L2 — SPARSE TOPIC ROUTING
Only topic/source relations with actual signals
        │ zero-signal relations are implied, not materialized
        ▼
L3 — QUERY WORK PACK
One topic + one unresolved query + a bounded source wave
        │ only required source IDs and exact sections
        ▼
L4 — SOURCE ANALYSIS
One semantic evidence note per materially reviewed source/topic
        │ claims, contradictions, authority, query linkage
        ▼
L5 — COMPILED KNOWLEDGE
Minimum answer-bearing dossier/concept/entity pages
        │ only materially used sources
        ▼
L6 — CLEAN ACCEPTANCE
One query/page evaluation, then selected claim/evidence checks
        │ reason-coded repairs only
        ▼
L7 — MACHINE POSTFLIGHT + RETRIEVAL
Schema, links, freshness, index; large database remains machine-only
```

### Funnel principle

Every layer must reduce browser scope:

| Layer | Universe | Browser role |
|---|---|---|
| Source registry | all 197 | never read wholesale |
| Structure index | 146 readable sources | lookup only |
| Topic routing | sources with topic signals | navigation only |
| Query work pack | one bounded wave | active semantic input |
| Material analyses | only reviewed useful/contradicting evidence | synthesis input |
| Compiled pages | only answer-bearing knowledge | default retrieval input |
| Acceptance packet | one page/query plus selected passages | evaluator input |

## 4. Target meso architecture

### Layer L0 — source registry

**PURPOSE:** custody and identity.

```text
manifests/sources/
├─ index.json
└─ records/
   ├─ src-001.json
   ├─ src-002.json
   └─ …
```

`index.json` contains only source ID, relative canonical path, hash, media type, bytes, and status. Each record owns richer custody metadata.

**NO:** headings, topic keywords, semantic judgments, copied canonical text.

### Layer L1 — structural index

**PURPOSE:** deterministic navigation facts stored once.

```text
manifests/structure/
├─ index.json
└─ sources/
   ├─ src-001.structure.json
   ├─ src-002.structure.json
   └─ …
```

Each structure record contains:

- `source_id` foreign key;
- H1–H6 headings with line numbers;
- Markdown/wiki links;
- frontmatter keys/status;
- code-block ranges;
- parser warnings.

**REMOVE:** separate heading, link, frontmatter, and source-postings copies as independent stores. If compatibility views remain temporarily, generate them and mark them non-authoritative.

### Layer L2 — sparse topic routing

**PURPOSE:** nominate plausible sources without copying source facts.

```text
manifests/topics/<topic-slug>/routing/
├─ index.json
├─ direct/
│  └─ <source-id>.json
├─ contextual/
│  └─ <source-id>.json
└─ coverage.json
```

Each relation card contains only:

```json
{
  "topic_slug": "skill-tree",
  "source_id": "src-…",
  "signal_class": "direct",
  "signals": [
    {"field": "heading", "term": "skill tree", "line": 202},
    {"field": "body", "term": "PathAllocationDraft", "line": 257}
  ],
  "rank": 1
}
```

**NO:** copied path, hash, complete heading list, source snapshot, or semantic authority. Resolve those by `source_id` only when needed.

`coverage.json` proves exhaustive deterministic consideration without creating zero-signal cards:

```json
{
  "source_universe_sha256": "…",
  "source_count_considered": 197,
  "signal_relation_count": 135,
  "zero_signal_count": 62,
  "algorithm_version": "…"
}
```

This preserves custody while avoiding 62 useless Skill Tree cards.

### Layer L3 — query work packs

**PURPOSE:** give the browser exactly one task.

```text
work-packs/<run-id>/<topic>/<query-id>/
├─ brief.md
├─ sources-wave-01.json
├─ passages/
│  ├─ <source-id>-01.md
│  └─ …
└─ state.json
```

The brief contains:

- one question and answer requirements;
- unresolved facts;
- expected page route;
- source IDs in the current wave;
- byte/token preflight;
- stop/continue rule.

Candidate waves are adaptive:

- **Wave A:** canonical specifications and heading/filename direct signals;
- **Wave B:** current contracts and strong body/co-occurrence signals;
- **Wave C:** user stories/examples and linked/context evidence;
- **Wave D:** historical/proposed material only for unresolved conflict or evolution questions.

Do not use a blind top-N completion rule. Open another wave only when a critical/routine answer requirement remains unresolved.

### Layer L4 — modular semantic ledger and Phase 1

**PURPOSE:** store semantic judgments without repeating deterministic source metadata.

Proposed ledger v2:

```text
log/semantic-runs/<run-id>/topics/<topic>/
├─ state.json
├─ queries/
│  └─ <query-id>.json
├─ sources/
│  └─ <source-id>.json
├─ page-decisions.json
├─ candidate-dispositions.json
└─ blockers.json
```

Each reviewed-source shard owns:

- read status and exact passages;
- authority class;
- supported/contradicted query IDs;
- claim IDs/page use;
- next action.

It references `source_id`; it does not repeat path/hash/headings.

Phase 1 remains one bounded analysis per materially useful source/topic. If one source supports several topics, store one source evidence extraction and small topic interpretation files rather than copying the full analysis.

### Layer L5 — compiled pages

**PURPOSE:** final useful knowledge.

Keep Apex's current value contract:

- Target Questions Answered;
- Adaptive Ranked Source Set of materially used sources only;
- Macro/Meso/Micro;
- Key Claims with precise pointers;
- Routes Here;
- Uncertainty/Reopen Triggers.

Split a page only when the child has independent retrieval value. Do not split merely to hit a line count, and do not allow a large cross-topic dossier.

### Layer L6 — acceptance

**PURPOSE:** evaluate usefulness independently.

```text
audit/semantic-acceptance/<run-id>/<topic>/
├─ manifest.json
├─ queries/
│  └─ <query-id>.json
└─ claims/
   └─ <claim-id>.json
```

Sequence:

1. evaluator reads target question and compiled page only;
2. records answerable/partial/not-answerable/blocked;
3. evaluator receives only selected claim passages;
4. records entailment;
5. manifest derives topic verdict.

The evaluator must not read the exhaustive map or every rejected candidate.

### Layer L7 — derived retrieval

Large SQLite/NDJSON indexes are allowed only as rebuildable machine artifacts. They are queried, never loaded wholesale into a browser semantic context.

## 5. Micro flow: one Skill Tree question

Question: “How does Skill Tree hand selected scope to Path?”

```text
1. Registry locks question + answer requirements.
2. Routing finds heading/body signals in five plausible sources.
3. Work pack Wave A contains two canonical sources and exact section pointers.
4. Browser reads those sections.
5. Source-review shards record:
   - source A supports hierarchy/projection;
   - source B supports PathAllocationDraft handoff.
6. Query state becomes answered; no Wave B is opened.
7. Phase 1 analysis records the handoff evidence.
8. Skill Tree dossier writes one direct answer and two claims.
9. Fresh evaluator reads the dossier and answers the question.
10. Evaluator checks the two source passages.
11. Topic passes or receives a narrowly reason-coded repair.
```

No step reads 197 candidates. No source headings are copied. No atlas restates 192 rejected records.

## 6. File-size and batch policy

These are proposed engineering defaults, not claims about a hidden connector limit.

| Signal | Default |
|---|---|
| **TARGET** browser-facing control file | ≤ 64 KB |
| **HARD SHARD** browser-facing JSON/Markdown | split when > 128 KB |
| **TARGET** ledger/review shard | ≤ 32 KB |
| **TARGET** compiled page | ≤ 80 KB; split only by independent value |
| **WORK PACK** metadata | ≤ 100 KB total |
| **WORK PACK** source wave | ≤ 8 sources and preflighted readable-token estimate |
| **CONTEXT GATE** | stop before delegation when planned input exceeds configured budget |
| **MACHINE-ONLY** | SQLite/search indexes may exceed limits but cannot be semantic inputs |

Canonical source files remain unchanged even when large. The work pack points to relevant sections; it does not copy or split canonical truth.

## 7. No-overlap ownership matrix

| Fact | Single owner | Referenced by |
|---|---|---|
| source path/hash/type/bytes | source record | all later layers via `source_id` |
| headings/links/frontmatter/parser warnings | structure record | routing/work-pack resolver |
| topic term hits/rank | topic/source relation | work-pack builder |
| source reading and semantic judgment | review shard | Phase 1/pages/acceptance |
| topic answer status | query-state shard | topic state/acceptance |
| material claim wording | compiled page | acceptance/retrieval |
| claim verdict | acceptance claim shard | acceptance manifest |
| search chunks | derived index | retrieval runtime |

**RULE:** later layers reference upstream IDs; they do not copy upstream records.

## 8. OKRs

### Objective O1 — One fact, one owner

- **KR1:** 100% of headings exist in exactly one authoritative structure record.
- **KR2:** topic relation cards contain zero copied hashes, paths, or full heading arrays.
- **KR3:** ledgers contain semantic judgments only; deterministic metadata is resolved by ID.
- **KR4:** atlasses are eliminated as independent truth or generated on demand from ledger shards.

### Objective O2 — Bounded browser work

- **KR1:** no browser prompt references the combined exhaustive map.
- **KR2:** 100% of delegations include byte/token/source-count preflight.
- **KR3:** every browser context owns exactly one topic and normally one unresolved query.
- **KR4:** no control artifact exceeds 128 KB; oversized artifacts fail preflight and shard.

### Objective O3 — Progressive narrowing without coverage loss

- **KR1:** every routing run records source-universe hash/count and zero-signal count.
- **KR2:** zero-signal sources remain provably considered but are not routine semantic inputs.
- **KR3:** each additional source wave is justified by a named unresolved answer requirement.
- **KR4:** a topic cannot complete while a known readable source could resolve a critical/routine gap.

### Objective O4 — Semantic value first

- **KR1:** completion reports lead with answered queries, material sources, claim verdicts, and blockers—not candidate/file counts.
- **KR2:** compiled pages contain only reviewed/materially used sources.
- **KR3:** each critical/routine query has a direct answer route.
- **KR4:** sampled material claims are independently supported.

### Objective O5 — Safe modular migration

- **KR1:** canonical Leela source files remain in place and pointer-only.
- **KR2:** old derived maps can be rebuilt or archived after parity evidence; no canonical evidence is lost.
- **KR3:** Skill Tree pilot achieves the same or better accepted answers with materially lower browser input.
- **KR4:** postflight, retrieval freshness, and truthful state gates remain intact.

## 9. Implementation plan

### Phase 1 — contract correction

**CHANGE:**

- remove full-map/every-candidate requirements from Leela browser prompts;
- define exhaustive map as machine custody only;
- make Phase 0 rankings/sparse routing the browser entry point;
- stop requiring a 197-block source atlas for semantic pass;
- restore page-first acceptance before evidence checks.

**VERIFY:** repository-local contract, manual prompts, runtime validation, and acceptance all express the same rules.

### Phase 2 — normalize Phase 0

**BUILD:**

- per-source registry records;
- one structural record per readable source;
- sparse topic/source relations with exact signal locations;
- per-topic coverage summaries anchored to the complete source-universe hash.

**DEPRECATE:** overlapping `source-postings`, `heading-map`, full topic map as browser input, and duplicated content pointers.

### Phase 3 — bounded work-pack generator

**BUILD:** a deterministic read-only command that accepts topic/query IDs and returns:

- current unanswered requirements;
- next source wave;
- exact source/section pointers;
- bytes and estimated tokens;
- reason for including each source;
- stop/continue state.

The command nominates evidence. It never performs semantic judgment.

### Phase 4 — ledger v2 shards

**CHANGE:** evolve `semantic-run-ledger.schema.json` from one topic object to a directory manifest plus query/source/decision shards.

**COMPATIBILITY:** provide a deterministic compact v1 export only for tools that still need it. The export is derived, not authoritative and not a browser input.

### Phase 5 — acceptance shards

**BUILD:** one query result and one sampled-claim result per file, plus a small derived topic verdict manifest.

**REMOVE:** exhaustive candidate/atlas comparison from the page-only evaluator.

### Phase 6 — Skill Tree pilot

Run only Skill Tree through the new process:

1. compare current 197-candidate inputs with sparse routing;
2. compare source waves with the five known material sources;
3. compile/repair the dossier against the same locked questions;
4. perform clean acceptance;
5. measure browser bytes, source opens, semantic claims, and acceptance result.

Do not migrate all ten topics until the pilot proves equal or better semantic coverage.

### Phase 7 — controlled rollout

Migrate one topic per commit. Rebuild derived artifacts locally, validate, then delegate only the bounded semantic work. Keep rollback possible by retaining the old derived artifacts until parity is demonstrated.

## 10. Validation matrix

| Test | Pass condition |
|---|---|
| Source parity | all 197 selected source IDs represented once in registry |
| Structure parity | same 4,310 headings recoverable from structure shards |
| Sparse routing | no zero-signal candidate card; coverage summary still reports all 197 considered |
| No overlap | schema/lint rejects copied path/hash/headings in downstream cards |
| Size gate | every browser-facing file ≤ 128 KB |
| Work-pack gate | planned files, bytes, estimated tokens, source count, and query ID recorded |
| Semantic continuation | unresolved critical/routine query with known source forces next wave/partial |
| Material traceability | every compiled claim resolves to review shard and canonical passage |
| Acceptance isolation | evaluator receives pages first, not drafting ledger/full map |
| Truthful promotion | semantic pass + deterministic postflight + fresh retrieval required for `query_ready` |

## 11. Decisions required before implementation

- **DECIDE:** whether atlasses are removed entirely or retained only as generated human views.
- **DECIDE:** default 64/128 KB file limits and browser work-pack token budget.
- **DECIDE:** whether Phase 1 source evidence is shared across topics with topic-specific interpretation shards.
- **DECIDE:** migration compatibility window for old map/ledger consumers.

Recommended defaults:

- generated atlas only, never authoritative;
- 64 KB target / 128 KB hard browser-file limit;
- shared source evidence extraction plus topic interpretation;
- one-pilot-plus-two-topic compatibility window before old derived interfaces are retired.

## Final operating rule

```text
Broad machine custody.
Sparse deterministic routing.
Bounded semantic reading.
Minimal evidence-backed synthesis.
Independent narrow acceptance.
Large indexes only behind retrieval tools.
```

That is the streamlined waterfall: each stage adds meaning while reducing what the next stage must read.
