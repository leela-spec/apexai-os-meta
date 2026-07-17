# Phase 0 Q&A Field Compatibility and Simplification Audit

```yaml
schema: apex.kb.phase0-qa-compatibility-audit.v1
status: design_review_complete
reviewed_frontend: templates/start-qa-option-a-v3-example-guidance.md
reviewed_runtime:
  - .claude/skills/apex-kb/SKILL.md
  - .claude/skills/apex-kb/references/run-intent.schema.json
  - apex-meta/scripts/apex_kb_control.py
runtime_change_status: not_implemented
```

## 1. Executive verdict

The simplified operator Q&A is viable **only as a frontend input projection**. It is not currently a drop-in replacement for `manifests/run-intent.md` or the arguments required by `control init`.

The correct architecture is:

```text
operator-facing Q&A
    -> strict parser and normalization
    -> deterministic derivation of internal values
    -> explicit operator readback
    -> canonical run-intent.v1 + topic-registry
    -> existing run-state control plane
```

This preserves a simple operator experience without deleting information the current lifecycle still consumes.

## 2. Operator fields and downstream necessity

| Operator field | Required later? | Primary consumer | Verdict |
|---|---:|---|---|
| `repository` | yes | source resolution, Git classification, target repository | keep |
| `source_folders[]` | yes | source intake, preflight, Phase 0 inventory | keep |
| `exclusions[]` | yes when applicable | scope lock and recursive-output prevention | keep as an always-present array; allow `[]` |
| `kb_destination.folder` | yes | `--kb-root`, scaffold, canonical path ownership | keep |
| `topics[].name` | yes | topic slug derivation, work packs, semantic stages | keep |
| `topics[].phrases[]` | strongly recommended | deterministic candidate discovery and sanity check | keep; permit empty only with warning |
| `topics[].ambiguous_or_negative_terms[]` | optional | false-positive suppression and routing caution | keep as optional array |
| `topics[].questions[]` | required for compiled tiers | semantic analysis, page planning, independent acceptance | keep; require at least one for `compiled_kb` and `query_ready` |
| `run_options.source_handling` | yes | source intake storage mode | keep |
| `run_options.detail` | yes after implementation | corpus-intelligence profile | keep in frontend; map to runtime profile/corpus settings |
| `run_options.output` | yes | stage plan and truthful completion target | keep; map `compiled_kb` to a canonical live tier |
| `run_options.non_text` | yes after implementation | format extraction and block policy | keep; current runtime needs an explicit mapping added |
| `run_options.ai_help_after_preflight` | setup-only | optional recommendation renderer | keep outside canonical semantic truth; do not let it affect lifecycle completion |

## 3. Internal fields hidden from the operator

The live `run-intent.v1` schema currently requires fields not present in the simplified Q&A. They must be derived, defaulted, or retained internally until the runtime contract is migrated.

| Internal field | Derivation / source | Can be removed now? |
|---|---|---:|
| `schema`, `schema_version` | fixed runtime constants | no |
| `run_id` | generated deterministically or uniquely at Start | no |
| `kb_root` | repository root + `kb_destination.folder` | no |
| `kb_slug` | normalized final destination segment; shown in readback | no |
| `mode` | derived from whether destination exists and chosen output | not yet |
| `operator_intent` | deterministic summary of submitted repository, topics, questions, and output | not yet; schema requires it |
| `kb_identity` | deterministic summary of topic names and destination; shown in readback | not yet; schema requires it |
| `source_locus` | repository + source folders | no |
| `source_roots` | normalized `source_folders[]` | no |
| `source_inputs` | generated per root/storage choice or left empty where root intake owns it | no |
| `out_of_scope` | normalized exclusions | no |
| `success_definition` | generated from output tier plus target questions; shown in readback | not yet |
| `output_tier` | mapping from frontend value | no |
| `output_tier_rationale` | deterministic explanation of the selected tier | not yet; schema requires it |
| `execution_route` | capability preflight result, not operator choice | no |
| `corpus_breadth` | derived from scope size/root selection, subject to readback | no |
| `topic_slugs` | generated from topic names with collision handling | no |
| `topic_sanity_check` | produced by deterministic preflight | no |
| confirmation fields | written only after operator confirmation | no |
| `target_repository` | same as `repository` under the current same-repository rule | no |
| `target_commit` | resolved read-only from the selected runtime state; shown in readback | no |
| timestamps | runtime generated | no |

## 4. Compatibility gaps that must be implemented

| Gap | Current live behavior | Required change |
|---|---|---|
| Frontend schema | No canonical parser for the simplified Q&A | Add a small frontend schema and parser; never parse by conversational guesswork |
| Output tier names | Live tiers include `compiled_minimal` and `compiled_full`; frontend says `compiled_kb` | Select one deterministic mapping, provisionally `compiled_kb -> compiled_full`, or rename the frontend option |
| Detail profile | Frontend uses `quick/standard/deep`; current run intent uses `corpus_breadth` and optional coverage, not a direct profile | Add a profile owner and explicit mapping rather than hiding unrelated settings behind one word |
| Non-text policy | Frontend exposes three policies; current run-intent schema has no field | Add a canonical field consumed by preflight/intake/Phase 0 or remove it from the form |
| AI help | No canonical runtime field is required | Keep as presentation-layer preference; never fingerprint it as semantic run truth unless recommendations become auditable artifacts |
| Exclusions | Current schema stores free-text `out_of_scope`; frontend uses path/reason objects | Introduce structured exclusions or normalize objects into stable strings without losing paths/reason codes |
| Topic questions | Current topic registry requires stable query IDs, priority, answer requirements, and expected routes | Generate provisional IDs/default priorities/routes, show them in readback, and require correction where derivation is unsafe |
| Branch/worktree fallback | Current control plane classifies one Git/worktree state and may enforce a target commit | Do not silently aggregate branches. Implement branch/worktree investigation as a separate read-only evidence-gap action with provenance and operator-visible results |
| Source type | `source_inputs` requires a source type for each source spec | Root intake should derive source types per file; the operator should not provide one global type |

## 5. Exclusion-format resilience

The safest operator format is always:

```yaml
exclusions: []
```

or:

```yaml
exclusions:
  - path: "generated-folder"
    reason: "generated_output"
```

Rules for the parser:

- YAML spacing may vary, but indentation must still form a valid YAML structure.
- Comments beginning with `#` are discarded by the YAML parser and are never runtime evidence.
- A dangling `-`, missing `path`, missing `reason`, unknown reason code, or scalar where an array is expected must fail validation with an exact correction message.
- The operator should not be instructed to delete the whole field. Empty arrays are more resilient than section deletion.
- Human prose reasons are insufficient for routing. Use a stable reason code plus an optional note when needed.

Recommended initial reason codes:

- `generated_output`
- `duplicate_export`
- `dependency`
- `cache`
- `archive`
- `irrelevant`
- `sensitive_out_of_scope`
- `other`

The runtime, not "later files," interprets these reason codes. Generated manifests should preserve both the code and the exact excluded path.

## 6. Reverse audit: what can be simplified

### Remove from the operator surface

| Existing/proposed input | Reason |
|---|---|
| Manual KB ID/title/purpose | Destination and topic configuration can derive identifiers and a provisional identity; operator reviews the readback |
| Manual branch/ref | Default and fallback policy should be deterministic and evidence-triggered |
| Manual execution route | Capability preflight determines it |
| Manual target repository repeated separately | Same-repository rule makes it equal to `repository` |
| Manual topic IDs/slugs | Deterministically generated with collision checks |
| Manual query IDs | Generated; operator owns question text |
| Manual output rationale | Generated from the selected option and shown for approval |
| Manual corpus breadth | Derived from selected roots and preflight facts; surfaced in readback |
| Free-form special constraints | Unbounded prose is not reliably machine-consumed; add future typed fields only when a real consumer exists |

### Keep internally, but stop asking for it

- run ID;
- KB slug;
- target commit;
- execution route;
- mode;
- success definition;
- output-tier rationale;
- topic/query IDs;
- expected page routes;
- timestamps and schema metadata.

### Do not delete yet

| Component | Why it remains necessary |
|---|---|
| `run-intent.md` | Canonical confirmed setup and drift boundary |
| `run-state.json` | Legal transitions, recovery, invalidation, exact next action |
| `topic-registry.json` | Stable target questions and deterministic vocabulary |
| source manifests | Custody, hashes, source modes, provenance |
| stage results | Restartable evidence and reason-coded failures |
| semantic packets | Bounded AI handoff without chat-memory dependence |
| Git classification | Write safety and reproducibility |
| independent semantic acceptance | Prevents structural completion from masquerading as useful knowledge |

## 7. Scripts and processes no longer fed directly

The new form no longer directly feeds several current `control init` arguments. That is acceptable **only after a deterministic adapter supplies them**.

| Current argument/process | New source | Safe? |
|---|---|---:|
| `--operator-intent` | generated summary + readback | yes after adapter |
| `--kb-identity` | generated identity + readback | yes after adapter |
| `--source-locus` | repository + source folders | yes |
| `--source-spec` | generated from source roots/storage mode where needed | yes after adapter |
| `--out-of-scope` | structured exclusion normalization | yes after adapter |
| `--success-definition` | output tier + questions | yes after adapter |
| `--output-tier-rationale` | deterministic option explanation | yes |
| `--execution-route` | capability preflight | yes; better ownership |
| `--corpus-breadth` | preflight-derived recommendation + confirmation | yes |
| `--topic-slug` | slug generator | yes |
| `--target-repository` | `repository` | yes under same-repository rule |
| `--target-commit` | Git resolution | yes if visible in readback |

Without this adapter, the simplified form breaks `control init` because those arguments and schema fields remain required.

## 8. Recommended minimal implementation sequence

1. Lock the v3 operator form and option names.
2. Add `start-input.schema.json` for the operator projection.
3. Add a strict YAML parser/normalizer that rejects example residue and slash-separated unresolved choices.
4. Add a deterministic adapter from Start input to run-intent/topic-registry inputs.
5. Resolve output-tier, detail-profile, non-text, and exclusion mappings explicitly.
6. Render a compact readback that shows submitted values, derived values, warnings, and target commit.
7. Add tests for empty exclusions, multiple topics, duplicate topic names, malformed bullets, path overlap, leftover examples, and unsupported options.
8. Only then replace the live Step 0 operator flow or expose `apexkb start`.

## 9. Final conclusion

The operator Q&A can be much smaller than the internal runtime contract. That is a healthy simplification.

The safe principle is:

> Remove machine-owned data from the operator form, not from the machine contract until every producer and consumer has been migrated and tested.

The strongest current simplification is therefore a **thin, strict Start frontend over the existing control plane**, not deletion of the control plane or its recovery artifacts.
