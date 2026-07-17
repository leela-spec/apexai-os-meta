# Phase 0 Start Mapping and Worktree Resolution

```yaml
schema: apex.kb.phase0-start-resolution.v1
status: partially_implemented
frontend_schema: .claude/skills/apex-kb/references/start-input.schema.json
frontend_adapter: apex-meta/scripts/apex_kb_start.py
regression_tests: apex-meta/scripts/tests/test_apex_kb_start.py
public_alias_status: not_yet_wired_into_apex_kb.py
```

## 1. Plain-language answer

The Q&A is the **frontend**. It contains only information the operator should reasonably know and choose.

The Start adapter is the **backend transformer**. It generates the technical values required by the existing Apex KB control plane, writes the topic registry, and starts the controlled run.

The operator no longer supplies IDs, slugs, execution route, target commit, output rationale, corpus breadth, success definition, or machine timestamps. These values still exist internally because current scripts consume them.

## 2. Resolved option mappings

### Output

| Q&A option | Current runtime value | Meaning |
|---|---|---|
| `analysis_only` | `analysis_only` | Stop after deterministic mapping and semantic analysis |
| `compiled_kb` | `compiled_full` | Produce the complete compiled KB, not the smaller legacy/minimal tier |
| `query_ready` | `query_ready` | Produce accepted compiled knowledge and complete postflight/retrieval |

`compiled_minimal` remains supported by the existing low-level runtime for legacy or specialist use, but it is deliberately **not offered in the normal Start Q&A**. The operator-facing `compiled_kb` means the full useful compiled product.

### Detail

| Q&A option | Current implemented mapping | Intended Phase 0 effect |
|---|---:|---|
| `quick` | Phase 1 minimum source coverage `0.4` | Lower-cost mapping and smaller concentrated review set |
| `standard` | Phase 1 minimum source coverage `0.6` | Default balance of coverage, cost, and resilience |
| `deep` | Phase 1 minimum source coverage `0.8` | Higher required evidence coverage before semantic completion |

The adapter now records this mapping. A later patch must additionally let Phase 0 extraction breadth itself consume `detail_profile`; the existing Phase 0 implementation does not yet have one canonical quick/standard/deep switch.

### Non-text policy

| Q&A option | Required behavior |
|---|---|
| `inventory_and_report` | Inventory every file, do not claim unsupported content was read, and report extraction gaps |
| `extract_when_supported` | Use approved installed extractors; preserve every extraction failure visibly |
| `block_on_unsupported` | Stop before corpus processing when any in-scope file has no approved extraction route |

The value is now validated and preserved in `manifests/start-input.json`. The existing intake/Phase 0 runtime does **not yet consume it**, so it must not be described as fully operational until the downstream extractor/preflight patch is added.

### Structured exclusions

An exclusion is not free prose. It is a stable pair:

```yaml
exclusions:
  - path: "operations/generated-reports"
    reason: "generated_output"
```

- `path` tells the deterministic inventory exactly which subtree is excluded.
- `reason` tells later reports why it was excluded.
- `exclusions: []` means no exclusions.
- malformed bullets, missing keys, or unknown reason codes fail schema validation.

The Start adapter currently preserves exclusions in the immutable Start input and converts them into current `out_of_scope` records for `control init`. Full inventory-time path filtering still requires a downstream Phase 0 consumer patch.

## 3. Variables removed from the operator surface

These values are no longer manually requested:

- KB ID, title, and purpose;
- run ID;
- KB slug;
- branch/ref or target commit;
- execution route;
- mode;
- success definition;
- output-tier rationale;
- corpus breadth;
- topic slugs;
- query IDs;
- expected page paths;
- target repository repeated a second time;
- timestamps and schema metadata;
- free-form special constraints.

## 4. Downstream problem check

| Hidden value | Backend producer | Existing consumer | Problem status |
|---|---|---|---|
| run ID | Start adapter | run state, logs, packets | safe |
| KB slug | destination folder name | run intent/state, pages | safe |
| operator intent | deterministic summary of topics/output | `control init`, readback | safe but operator must review |
| KB identity | deterministic topic/repository summary | scaffold/readback | safe but operator must review |
| source locus | repository + source folders | run intent/readback | safe |
| success definition | selected output + questions | run intent/readback | safe but operator must review |
| output rationale | fixed mapping table | run intent/readback | safe |
| execution route | Start capability path | control plane | safe for this terminal Start adapter |
| corpus breadth | repository-root versus narrower roots | control plane/readback | safe |
| topic/query IDs | collision-safe slug and sequence generator | registry, Phase 0, semantic packets | safe; tests added |
| target commit | primary main worktree HEAD | Git guard, reproducibility | safe |
| detail profile | Start adapter | only coverage floor currently | partial; Phase 0 breadth consumer still needed |
| non-text policy | immutable Start input | no live downstream consumer yet | partial; extractor/preflight consumer still needed |
| exclusions | Start input + current `out_of_scope` conversion | readback only today | partial; inventory filtering consumer still needed |
| source handling | Start input | current root-intake delegation defaults to pointer-only | partial for copy/snapshot root modes; control delegation patch still needed |

The frontend does not break the existing infrastructure because it still produces the required internal values. However, the four rows marked `partial` must remain visible implementation tasks; silently ignoring them would be a false implementation claim.

## 5. Worktree safety policy

### Locked behavior

1. Apex KB never creates a worktree.
2. Apex KB never switches branches.
3. Apex KB never merges, rebases, pulls, resets, stashes, prunes, or removes worktrees.
4. Apex KB never mixes files from several worktrees or branches into one source corpus.
5. `git worktree list --porcelain` is used read-only.
6. The first Git worktree is treated as the primary worktree.
7. Automatic fallback is allowed only when that primary worktree is on `main`, matches the configured repository, and passes read-only Git safety classification.
8. Linked worktrees are recorded and ignored.
9. If the primary worktree is missing, detached, not on `main`, mismatched, conflicted, or in a Git operation, Start fails closed with a reason code.

### Why this is resilient

The fallback prevents an AI from accidentally building the KB in a duplicated feature worktree while still avoiding any automatic Git mutation. The exact canonical root, HEAD, fallback decision, and ignored worktrees are stored in `manifests/worktree-safety.json`.

## 6. Files now added

| File | Role |
|---|---|
| `.claude/skills/apex-kb/references/start-input.schema.json` | Canonical operator-input validation |
| `apex-meta/scripts/apex_kb_start.py` | Strict parser, mapper, worktree safety fallback, and `control init` adapter |
| `apex-meta/scripts/tests/test_apex_kb_start.py` | Mapping, slug collision, remote identity, path, and worktree parsing tests |

## 7. Remaining wiring

The additive adapter is committed, but the normal `apex_kb.py` command parser does not yet expose `start`, and a friendly `apexkb start` launcher does not yet exist.

Before calling the public surface complete:

1. confirm PyYAML as an approved runtime dependency or replace it with a maintained internal YAML parser;
2. wire `start` into `apex_kb.py` or a stable launcher;
3. patch source-root intake to consume `source_handling` for pointer/copy/snapshot modes;
4. patch preflight and Phase 0 to consume `detail_profile`, `non_text_policy`, and structured exclusions;
5. add integration tests against a temporary Git repository with primary and linked worktrees;
6. run the full existing Apex KB test suite in a live checkout.

The present status is therefore **implemented adapter plus schema and unit tests, not yet the final public command**.
