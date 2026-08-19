# V1 Implementation Plan — CLI Semantic Worker over TTK

**Date:** 2026-08-18  
**Status:** ready for executing CLI AI  
**Depends on:** `PIPELINE_ARCHITECTURE_OPTIONS_AND_V1_DECISION_2026-08-18.md`

---

# 0. Mission

Implement and test the **smallest valuable repair** to the current transcript-to-knowledge pipeline.

Do **not** redesign the whole subsystem.

V1 must:

1. keep the existing deterministic TTK custody/window/hash/validation/verification/compile lifecycle;
2. remove heuristic pseudo-semantic Map/Reduce generation from the convenience executor;
3. invoke a strong subscription CLI AI for real semantic Map and Reduce work;
4. default to Claude Code CLI for the first implementation;
5. keep the semantic-worker adapter replaceable so Codex/Gemini can be benchmarked later without altering TTK contracts;
6. use the four already-existing benchmark transcripts first;
7. fail closed when a semantic CLI stage does not run or validate;
8. produce truthful receipts;
9. avoid introducing LangExtract, Instructor, DocETL, GLiNER2, NuExtract, DeepEval, WhisperX, Qwen, a vector DB, or a new workflow engine in V1.

The product is the **knowledge artifact**, not simply a transcript. ASR quality remains an upstream gate but should be calibrated only after the semantic path is repaired.

---

# 1. Non-negotiable authority boundary

## Deterministic code owns

- source parsing;
- source SHA-256;
- canonical segment IDs;
- processing-window generation;
- packet hashes;
- state/status/resume;
- JSON structural validation;
- source-reference validation;
- exact quote/sub-string validation where required;
- exact core-coverage validation;
- verification routing;
- stable IDs;
- compilation;
- run receipts.

## Strong CLI AI owns

- themes;
- important points;
- mechanisms;
- protocols/processes;
- arguments/positions;
- real semantic chapter/Meso structure;
- claim formulation;
- claim classification;
- source-support interpretation;
- uncertainty/caveat interpretation;
- Macro synthesis;
- external evidence interpretation.

## Explicitly forbidden

- heuristic Python must not stamp semantic support as `SUPPORTED`;
- deterministic code must not manufacture chapter titles such as fixed “Foundational / Mechanisms / Strategy / Outlook” templates;
- deterministic code must not turn sentence fragments into final semantic claims merely because they are source-verbatim;
- Qwen must not be used for semantic work in V1;
- a successful JSON-schema validation must not be treated as proof of semantic quality;
- an absent semantic worker must never be reported as a completed semantic run.

---

# 2. First implementation target

## Current problem file

`.claude/skills/transcript-to-knowledge/scripts/execute_ttk_lifecycle.py`

The current file performs semantic-looking work using regex/rules. Do not incrementally improve those heuristics.

### Required change

Replace the pseudo-semantic generator role with orchestration only.

The resulting runner should conceptually do:

```text
init/status
  -> get pending Map packet
  -> call semantic worker adapter
  -> write result
  -> ttk validate
  -> repeat only pending/invalid packet
  -> make-reduce
  -> call semantic worker adapter for Reduce
  -> ttk validate
  -> make-verify
  -> optionally call verification worker for queued factual claims
  -> compile
  -> validate --complete
  -> receipt
```

The runner may either replace `execute_ttk_lifecycle.py` or introduce a clearly named new runner and deprecate the old semantic heuristic path. Prefer the smallest change that makes it impossible for the heuristic path to masquerade as semantic execution.

---

# 3. Files to inspect before writing code

Read these in order:

1. `.claude/skills/transcript-to-knowledge/SKILL.md`
2. `.claude/skills/transcript-to-knowledge/references/semantic-contracts.md`
3. `.claude/skills/transcript-to-knowledge/references/architecture.md`
4. `.claude/skills/transcript-to-knowledge/references/operator-runbook.md`
5. `.claude/skills/transcript-to-knowledge/references/evals.md`
6. `.claude/skills/transcript-to-knowledge/scripts/ttk.py`
7. `.claude/skills/transcript-to-knowledge/scripts/test_ttk.py`
8. `.claude/skills/transcript-to-knowledge/scripts/execute_ttk_lifecycle.py`
9. `scripts/Run-BatchMultiPipelineBenchmark.ps1`
10. `artifacts/benchmark_runs/20260818-185245/receipt.json`
11. `SourceTranscriptionAnalysisPipeline_Research/PIPELINE_ARCHITECTURE_OPTIONS_AND_V1_DECISION_2026-08-18.md`
12. `SourceTranscriptionAnalysisPipeline_Research/PIPELINE_DECISION_CONTRACT_2026-08-18.yaml`

Do not rely on conversation memory if repository content conflicts with it.

---

# 4. Semantic-worker adapter design

Add **one small adapter**, not a provider framework.

Suggested path:

`.claude/skills/transcript-to-knowledge/scripts/semantic_worker.py`

Suggested interface:

```text
python semantic_worker.py map \
  --packet <path> \
  --output <path> \
  --provider claude

python semantic_worker.py reduce \
  --packet <path> \
  --output <path> \
  --provider claude

python semantic_worker.py verify \
  --packet <path> \
  --output <path> \
  --provider claude
```

V1 only needs the `claude` provider implementation, but provider selection should be isolated to one adapter boundary.

Do not build:

- dynamic routing;
- failover graphs;
- provider registries with dozens of fields;
- model scorecards inside production code.

A simple `if provider == "claude": ...` is acceptable in V1.

---

# 5. Claude CLI invocation — V1

Use official Claude Code print/headless mode.

Desired properties:

- non-interactive `-p`;
- strict JSON Schema using `--json-schema`;
- `--output-format json` if useful for invocation telemetry;
- finite turn limit;
- no shell/file-write/web tools for Map and Reduce;
- no session persistence unless proven useful;
- model configurable via argument/config rather than hard-coded deep in logic;
- capture stdout/stderr/exit code;
- save invocation receipt without saving secrets.

Official CLI capability reference:

- https://code.claude.com/docs/en/cli-usage
- https://code.claude.com/docs/en/headless

## 5.1 Map security/capability posture

Map needs **no tools**.

Give the model only:

- the semantic instructions;
- the result contract/schema;
- one packet file’s content.

Do not let Map browse, shell, edit repository files, or inspect neighboring packets.

This makes every Map call a bounded pure semantic transformation.

## 5.2 Reduce security/capability posture

Reduce likewise needs **no tools**.

Give it only:

- Reduce semantic instructions;
- result contract/schema;
- compact validated Reduce packet.

The Reduce worker must never independently reread the entire raw transcript.

## 5.3 Verification posture

Verification is separate.

Only this stage may enable web-research tools such as `WebSearch`/`WebFetch`, because the queue contains only selected factual claims.

This prevents ordinary semantic extraction from becoming an uncontrolled research agent.

---

# 6. JSON Schema source of truth

Do not manually maintain unrelated duplicate schemas in three places.

Preferred V1 approach:

1. derive or hand-maintain one Map JSON schema corresponding exactly to `ttk.map-result.v2`;
2. derive or hand-maintain one Reduce JSON schema corresponding exactly to `ttk.reduce-result.v2`;
3. one Verify JSON schema corresponding to `ttk.verify-results.v2`;
4. keep deterministic TTK validation authoritative even after CLI schema validation.

CLI schema validation ensures shape.

TTK validation ensures pipeline-specific invariants such as:

- packet hash matches;
- source segment exists;
- core-only evidence;
- quote exists when required;
- references resolve;
- stale results rejected.

---

# 7. Required semantic-contract update for operator decision D35

The current Map contract says every candidate claim requires a verbatim quote. The operator decision is now more nuanced.

Update the contract/tests so:

## Exact quote required

- `fact`;
- `estimate` where it states an externally testable quantity;
- any other claim explicitly routed as an externally testable factual assertion.

## Source segment IDs required, exact quote optional

- opinion;
- prediction;
- recommendation;
- decision;
- anecdote;
- mechanism;
- hypothesis;
- non-factual definitions/interpretive objects.

Do not remove provenance for non-factual objects. Only remove the unnecessary requirement that all semantic objects carry verbatim quote text.

The Reduce contract should preserve lineage from Macro/Meso to Micro/source evidence without requiring Macro/Meso prose to be verbatim.

### Tests required

Add tests proving at least:

1. factual claim without quote fails;
2. factual claim with invented quote fails;
3. factual claim citing `context_only` fails;
4. opinion with valid core segment IDs and no quote succeeds;
5. prediction with valid core segment IDs and no quote succeeds;
6. mechanism with valid core segment IDs and no quote succeeds if schema allows it;
7. unsupported source refs fail regardless of claim kind;
8. an old packet hash fails;
9. Reduce still rejects unresolved claim refs;
10. verification queue includes only routed factual claims.

---

# 8. Prompt design

Do not make prompts enormous.

Use:

- a compact invariant block;
- exact result schema;
- a few failure-preventing instructions;
- packet content.

## Map prompt must emphasize

- Processing window is **not** a chapter.
- `context_only` is for understanding only and cannot be cited.
- Capture **valuable distinct semantics**, not every sentence.
- Do not force quotas.
- Empty arrays are correct.
- Do not create an entity/protocol/mechanism because the schema has a field.
- Claim types are semantic categories, not keyword rules.
- Factual claims need exact source quote evidence.
- Preserve corrections, contradictions, ambiguity, and uncertainty.

## Reduce prompt must emphasize

- Consume the validated evidence ledger, not raw transcript.
- Determine real semantic Meso modules independent of Map-window boundaries.
- Prefer useful synthesis over exhaustive claim atomization.
- Represent important evidence from across the source; do not simply favor earliest windows.
- Preserve disagreements/uncertainty.
- Separate `source_support` from external-world truth.
- Do not stamp everything `SUPPORTED`; use `PARTIAL`, `AMBIGUOUS`, or reject when appropriate.
- Macro/Meso prose may synthesize; lineage must remain traceable.

---

# 9. Retry policy

Keep retry logic minimal.

## Map

1. call CLI once;
2. if CLI exits non-zero: record failure;
3. if JSON/schema invalid: one retry with validator error appended;
4. if TTK invariant validation fails: one retry with exact validation error;
5. if second attempt fails: mark that packet failed and stop/return incomplete.

Do not silently substitute heuristics.

## Reduce

Same policy: initial attempt + at most one validation-informed retry in V1.

## Verify

If search/research cannot establish an evidence-backed verdict, output `UNVERIFIED`; that is valid completion, not a reason to hallucinate or retry indefinitely.

---

# 10. Resumability

Do not invent new hidden workflow state.

Use TTK’s existing files and packet hashes.

Runner behavior:

```text
status/next
  if pending Map -> run only that Map
  if invalid/stale Map -> regenerate only that Map
  if all Map valid and Reduce packet absent/stale -> make-reduce
  if Reduce absent/stale -> run Reduce
  if verification queue stale -> regenerate queue
  if verification incomplete -> run/leave explicit UNVERIFIED as contract permits
  if compile stale -> compile
  if all current -> no-op success
```

A rerun must not burn semantic quota on already-valid current packets.

---

# 11. Invocation receipts and observability

Every semantic call should write compact metadata adjacent to the result or under a run receipts directory.

Suggested fields:

```json
{
  "stage": "map",
  "packet_id": "map-window-0001",
  "packet_sha256": "...",
  "provider": "claude-code",
  "model": "...",
  "started_at": "...",
  "finished_at": "...",
  "exit_code": 0,
  "attempt": 1,
  "validation": "PASS",
  "input_tokens": null,
  "output_tokens": null,
  "reported_cost_or_credit": null
}
```

Populate token/cost fields only where CLI output exposes them reliably. Do not fabricate estimates and label them as measured.

Final run receipt must include:

- exact Git commit at run start;
- dirty flag;
- transcript source SHA;
- ASR provenance when a fresh transcription was performed;
- number of Map packets expected/valid/failed;
- semantic provider/model;
- Reduce status;
- verification queue/result counts;
- compiler status;
- final validation status;
- artifact hashes/paths;
- `all_passed` must be false if any required stage is incomplete.

---

# 12. Phase 1 test — repair semantics without re-running ASR

Use current transcript artifacts so ASR quality does not confound the semantic repair.

Corpus:

| ID | Content role |
|---|---|
| `P-h5WSQG1Sw` | long English science/interview |
| `CygwqaNg2PY` | technical finance |
| `vFTuLylvYnA` | German financial commentary |
| `oZIsMX6WgFs` | long technical procedure/cycle analysis |

## Phase 1 acceptance gates

### Mechanical gates

- all Map result files were created by semantic-worker invocations;
- no heuristic Map/Reduce function was used;
- all expected Map packet hashes match;
- all Map TTK validators pass;
- Reduce TTK validator passes;
- compile succeeds;
- complete validation succeeds where verification state permits;
- receipt truthfully reports incomplete stages.

### Semantic sanity gates

The executing AI must inspect generated artifacts, not merely rely on schema PASS.

Reject the V1 output if it shows recurring symptoms such as:

- Map `claim_text` is just arbitrary transcript sentences with no semantic selection;
- every claim is `fact`;
- entity list contains obvious discourse words (`they`, `well`, `what`, etc.);
- Meso modules are fixed time quartiles or generic boilerplate;
- Macro thesis says only that “a comprehensive extraction was performed”;
- source support is uniformly `SUPPORTED` without meaningful discrimination;
- important later-window concepts disappear from Reduce.

For each of the four sources, write a short evaluation note containing:

- Macro usefulness;
- Meso semantic coherence;
- Micro factual-grounding correctness;
- major omissions;
- obvious semantic fabrications;
- approximate operator usefulness versus current artifact.

No new framework should be added during this evaluation round.

---

# 13. Phase 2 ASR calibration

Only after the semantic pipeline works.

## Goal

Choose the smallest/fastest faster-whisper model/config that makes B (knowledge quality) trustworthy.

Do not optimize raw ASR speed independently of downstream usefulness.

## Build a compact gold-slice fixture

Use manually checked snippets across the four benchmark videos, selected for:

- named people/companies;
- scientific terms;
- numbers/percentages;
- Elliott Wave vocabulary;
- German finance terms;
- current known failure examples.

The gold set should be small enough to review manually but difficult enough to distinguish ASR configurations.

## First comparison

Run the same clips through:

- faster-whisper `base`;
- faster-whisper `small`;
- faster-whisper `medium`.

Keep equivalent:

- language choice;
- VAD;
- word timestamps;
- diagnostic serialization;
- decoding parameters unless deliberately tested.

Test hotwords separately; do not mix model-size and hotword changes into one comparison if it prevents attribution.

Measure:

- normalized word error on gold slices where practical;
- named/domain term correctness;
- numeric correctness;
- timing availability;
- wall time;
- memory footprint if material.

Select the smallest configuration that clears the quality gate.

## If faster-whisper fails

Benchmark **NVIDIA Parakeet TDT 0.6B v3** next, especially on German/domain vocabulary.

Do not create an AI transcript-rewriter as the first response.

---

# 14. Phase 3 fresh end-to-end run

After semantic V1 and ASR calibration pass:

1. fresh German source (`vFTuLylvYnA`);
2. fresh shorter English technical source (`CygwqaNg2PY`);
3. then Huberman long source;
4. then Market Cycles.

Fresh means force/rebuild source transcription rather than silently reusing prior SRT/JSON.

Receipt must distinguish:

- `ASR_COMPLETE`;
- `SOURCE_CUSTODY_VALID`;
- `MAP_COMPLETE`;
- `MAP_VALID`;
- `REDUCE_COMPLETE`;
- `REDUCE_VALID`;
- `VERIFICATION_ROUTED`;
- `VERIFICATION_COMPLETE_OR_EXPLICIT_UNVERIFIED`;
- `OPERATOR_ARTIFACT_COMPLETE`;
- `COMPLETE_VALIDATION_PASS`.

Do not report one generic green “complete” state before those conditions are satisfied.

---

# 15. Provider challenger plan — only after Claude V1 exists

Do not implement multi-provider production routing yet.

After V1 passes mechanically, select **one representative Map packet and one Reduce packet** and compare:

1. Claude Code CLI default;
2. Codex CLI `exec --output-schema`;
3. Gemini CLI headless prompted JSON + deterministic TTK validation.

Compare:

- semantic quality;
- factual quote correctness;
- insight recall;
- source-support correctness;
- tokens/usage reported;
- wall time;
- operator friction;
- retry rate.

If one challenger is clearly better, changing the provider adapter should be a small patch.

Do not build an ensemble unless a measured single-provider failure demonstrates that an ensemble is valuable.

---

# 16. External verification V1

Operator decision: externally verify only important/checkworthy factual claims.

Use existing TTK queue routing.

Default V1 verification worker:

- Claude Code headless;
- web tools enabled only for this stage;
- prefer primary/official sources;
- make the smallest number of searches needed to resolve the specific factual question;
- if evidence is conflicting or insufficient, emit `UNVERIFIED` or `MIXED` as justified;
- do not modify the transcript/source quote;
- do not research opinions, predictions, recommendations, decisions, anecdotes by default.

Future alternatives retained:

- Gemini CLI Google Search;
- Codex web search;
- OpenClaw browser subscription AI if CLI research quotas/capabilities are poor;
- paid research/model APIs only when their value outweighs cost.

---

# 17. Regression tests required before declaring V1 implemented

At minimum, retain all existing TTK tests and add coverage for:

## Semantic worker

- missing CLI executable => explicit infrastructure failure;
- non-zero CLI exit => no semantic success state;
- empty output => failure;
- invalid JSON => retry then fail;
- packet hash mismatch => TTK reject;
- stale result => reject;
- successful result writes only intended result path;
- Map/Reduce invocations have tools disabled;
- verification invocation is the only web-enabled semantic call.

## Fail-closed behavior

- disable/rename `claude` executable and run benchmark => `all_passed=false`;
- remove one Map result => incomplete;
- corrupt factual quote => validation failure;
- remove Reduce output => incomplete;
- dirty git state is recorded, not hidden;
- receipt `git_commit` refers to actual run-start HEAD.

## Anti-pseudo-semantic regression

Add a code/static test that rejects reintroduction of functions that claim to produce semantic Map/Reduce results using keyword matching or fixed chapter grouping in the production runner.

The goal is not to ban all heuristics in the repository; it is to prevent heuristics from masquerading as the semantic worker.

---

# 18. “Do not add yet” list

The executing AI must not add any of these unless the current V1 implementation encounters the specifically named failure and documents evidence:

| Component | Allowed trigger |
|---|---|
| LangExtract | TTK exact source/span mapping proves inadequate or Map evidence extraction remains materially unreliable after prompt/provider comparison |
| Instructor | native CLI structured output/retry handling proves insufficient or provider abstraction genuinely needs it |
| DocETL | TTK semantic orchestration itself becomes a measured maintenance/quality bottleneck |
| GLiNER2 | semantic Map token usage becomes a dominant measured cost and local pre-extraction proves adequate on a gold set |
| NuExtract | same trigger after simpler GLiNER2 comparison |
| DeepEval | repeated semantic regression evaluation becomes expensive/manual enough to justify a judge framework |
| WhisperX | word alignment or speaker attribution is a measured quality requirement |
| Parakeet | calibrated faster-whisper fails the ASR quality gate |
| OpenVINO Whisper | chosen faster-whisper quality model is too slow and Intel acceleration could materially help |
| paid APIs | local/subscription paths fail a material quality/reliability target and the paid option has a clear cost/value case |
| new workflow engine | TTK/OpenClaw resume/orchestration fails under demonstrated scale/concurrency needs |

---

# 19. Required implementation artifacts

The executing AI should leave, at minimum:

- semantic worker adapter;
- Map/Reduce/Verify JSON schemas if not generated from existing contracts;
- repaired orchestration runner;
- updated semantic contract/tests for D35;
- regression tests;
- V1 benchmark receipts;
- semantic output quality evaluation report for the four sources;
- ASR calibration report (Phase 2, after semantic gate);
- updated master index/handover pointers.

Do not overwrite the historical comparison artifacts; retain them as evidence of prior failure modes.

---

# 20. Stop conditions for the executing AI

Stop and report instead of inventing architecture when:

- authentication for all strong CLI AIs is missing;
- TTK contract and current implementation conflict in a way that changes product semantics rather than being a simple bug;
- a required source artifact is missing and cannot be regenerated deterministically;
- Claude CLI cannot provide schema-constrained output in the installed environment;
- a change would require adding one of the deferred frameworks without first showing the named failure trigger;
- validation shows a fundamental mismatch between D35 and existing compiler semantics that requires an operator/product decision.

For ordinary code/test failures, diagnose and repair without escalating unnecessarily.

---

# 21. Definition of V1 success

V1 succeeds when:

1. a local runner can be triggered by OpenClaw/APEX and complete/resume the TTK lifecycle;
2. all actual semantic work is done by a strong CLI AI, not heuristics/Qwen;
3. four existing transcript runs produce semantically useful grounded artifacts;
4. factual Micro claims have exact source evidence;
5. non-factual semantic objects retain provenance without forced meaningless quote quotas;
6. semantic Meso and Macro outputs are genuinely source-specific;
7. verification is selective and explicit;
8. deterministic validation catches provenance/staleness failures;
9. a missing/failed semantic worker produces an incomplete/failing receipt;
10. no unnecessary new framework was added.

Only after this should the project optimize ASR, provider choice, token use, UI, or additional extraction frameworks.
