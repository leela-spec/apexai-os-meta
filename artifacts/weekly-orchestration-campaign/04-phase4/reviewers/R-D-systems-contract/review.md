# review.md — R-D Systems / Contract Architecture

```yaml
reviewer_id: R-D
lens: systems_contract_architecture
model_profile: "ox-alpha via Hermes Agent session (openrouter/stealth-ox-alpha)"
execution_primitive: "campaign-orchestrator file-dispatched bounded packet; fresh task context"
isolation_status: "ISOLATED per packet rules; same base model family as orchestrator - disclosed for parent weighting"
measurements_performed: none - contract analysis and reference-resolution checks only
```

## a. Diagnosed root causes

1. **[F02 root] Ownership rules exist as prose but carry no enforcement surface.**
   Evidence: PrecapWeek SKILL `downstream.transfer: reference_plus_minimal_seed`; PrecapNextDay boundary "Do not duplicate the full flow context across the Brief, a Flow Execution Card, and its prompt files." Yet nothing in any template makes duplication structurally impossible — Case-A generation needed generator discipline to avoid restating card content in flow blocks. Root cause: contracts are addressed to agent behavior, not encoded in template structure (no reference-only field types).
2. **[F04 root] Provenance is a section, not a schema obligation on facts.**
   Evidence: weekly template provenance block has four generic fields (project-state input, other sources, freshness, confidence) — none bound to individual claims. The eval case W-Q9 requires per-fact resolution; no template construct can satisfy it.
3. **[F10 residual] Gate semantics remain unqualified inside loop artifacts.**
   Evidence: contradiction register C-01 resolution requires qualified identifiers (`loop-G*`), but templates' handoff yaml blocks have `review_status` fields with free-text values — nothing prevents an agent writing `G1 approved` into them. The collision is documented but not structurally blocked at artifact level.
4. **[R-D-N1, new] The handoff chain has no schema-version coupling.** Evidence: each template's compact_downstream_handoff block names its own consumer, but there is no version/reference field letting a downstream skill verify the upstream artifact matches the contract it expects. State can drift silently across template revisions.
5. **[F05 root] Capacity states lack a contract vocabulary at template level.**
   Evidence: deformation doctrine defines full/compressed/minimal/omitted; daily template status enum covers PLANNED|COMPRESSED|SKIPPED|BLOCKED|OMITTED — two different vocabularies for adjacent concepts (COMPRESSED vs MINIMAL missing entirely from the enum). Contract mismatch between doctrine and schema.
6. **[R-D-N2, new] Receipts are unstandardized.** Phase-2 receipts were improvised per case; the campaign's own evidence rules (no self-certification, identity recording) have no template, so future generations will drift.

## b. Proposed information architecture

Contract-first layering:

- Every cross-layer content transfer happens through TYPED REFERENCE FIELDS only (ref + digest), never inline copies: weekly handoff block references priority IDs; daily brief references card paths; cards reference prompt files.
- Per-fact source tags become part of the content schema: any load-bearing line carries `[src: <ledger-id>]`; the ledger (one table, one place per artifact) maps ids to authority path + date + freshness class.
- Status enums unify with doctrine vocabulary: FULL | COMPRESSED | MINIMAL | OMITTED (+ BLOCKED for external stops), used identically in weekly deformation columns and daily flow statuses.
- Handoff blocks gain `schema_version` + `upstream_artifact_digest` fields.
- Gate/status values inside handoffs are constrained tokens (READY_WITH_REVIEW etc.), never free text that could smuggle bare `G1` claims.

## c. Redesigned example (full fidelity)

Redesign of Case-A weekly brief "Compact downstream handoff" + priorities interface (facts unchanged):

```yaml
presentation_handoff:
  schema_version: 2
  upstream_digest: "sha256:<computed-at-write>"
  artifact_type: "Weekly_Command_Brief"
  artifact_ref: ".../case-A-normal-week/weekly-command-brief.md"
  week: "2026-W36"
  result_state: READY            # token enum, not free text
  weekly_intent: "Consolidate W1 SSoT lock; start ACIM workshop outline"
  project_priorities:
    - project_ref: lika
      priority_id: P1-validation-walk
      desired_result_ref: "priorities.md#lika-p1"   # typed ref, not restated text
      day_emphasis: {MON: lead, TUE: parallel}       # directional tokens only
    - project_ref: acim
      priority_id: P1-outline-skeleton
      depends_on_priority: P1-validation-walk        # dependency as data
  capacity_class: STANDARD            # STANDARD|REDUCED|CRITICAL
  open_decisions:
    - id: provisional-vocabulary
      affects: [acim]
      bite_day: THU
  next_consumer: "PreCap_Next_Day_Brief@2"
```

Mechanism: the daily brief then CONSUMES this block — its delta table diffs
declared day-emphasis against actuals; wrong-layer sprint content cannot enter
because the schema has no field for it.

## d. What should be removed

| Remove | From | Finding |
| :-- | :-- | :-- |
| Inline restatement of weekly targets inside daily flow blocks | daily template | F02 |
| Free-text `review_status` values | all handoff blocks | F10 |
| SKIPPED status (redundant vs OMITTED/BLOCKED pair) or map it to MINIMAL | daily template enum | R-D-N1/F05 |
| Generic four-field provenance blob (as sole mechanism) | all templates | F04 |

## e. What moves between layers

| Content | From | To | Why |
| :-- | :-- | :-- | :-- |
| Priority/desired-result text | duplicated across layers | single owned location + typed refs | F02 enforcement |
| Dependency relations (Lika→ACIM) | prose ("Must happen first") | structured `depends_on` fields in handoff | machine-checkable sequencing |
| Freshness/confidence | artifact-level blob | fact-level ledger entries | F04/Q8/Q9 |
| Deformation vocabulary | doctrine-only | shared template enum | F05 |

## f. Expected Q-job improvements (mechanism-based)

| Job | Mechanism | Claim |
| :-- | :-- | :-- |
| Q9/Q8 | per-fact source tags make provenance answerable where the fact is read; confirmed-vs-assumed becomes a ledger column | improves Q9 objectively (tag presence); Q8 via ledger |
| Q12/Q15 | typed refs guarantee references resolve and never restate → duplicate encounters drop | improves; measurable via shingle comparison |
| Q6 | open_decisions as structured entries with bite-day | improves precision of what's pending when |
| Q13 | unified deformation enum aligns doctrine and artifacts | improves consistency; judgment to confirm readability |
| Q20 | prompt files gain required input-binding fields (inputs:, return:, done:) in their block template → label-swap prompts fail validation | improves; mechanically testable |
| Q1/Q11 | schema_version + digests make stale-consumption detectable | indirect improvement; detection not prevention |

## g. Risks/regressions

- Typed-reference discipline raises generation complexity; agents may emit broken refs → mitigate with resolve-checks (every ref must resolve before artifact completes); regression signal: unresolvable-ref rate.
- Stricter schemas reduce flexible degraded-mode output (Case D) → schemas must allow `null + reason`, else staleness weeks get fabricated data. Detect via D-type reruns.
- Enum unification could break existing packets mid-transition → needs version field (included) plus a compat window.
- Digest computation adds write-time cost; trivial but must be deterministic — specify algorithm or agents will improvise hashes.
- Same-model-family reviewers (disclosed in receipt): parent should treat convergent R-C/R-D conclusions as weaker evidence than divergent ones.

## Blocker note

status: NONE_BLOCKED
