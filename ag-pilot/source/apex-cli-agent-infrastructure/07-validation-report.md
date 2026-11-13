---
type: Reference
id: APEX-INFRA-VALIDATION-20261112
title: Cross-Artifact Validation Report
description: Actual source, schema, identity, integration, evaluation and semantic-review checks for the proposed design package.
status: draft
adoption_status: proposed_for_operator_review
source_revision: 6c93ad31e42a72de74119218b9365bdd9d6ee386
tags: [validation, source-fidelity, review, limitations]
---

# Cross-artifact validation report

**Validation establishes a reviewable proposed design, not an installed or empirically winning architecture.** The package preserves current ownership and accepted scope, supplies concrete activation and integration artifacts, and separates all unexecuted native cases from the deterministic checks performed here. The canonical package-check output is [results.json](validation/results.json); its limits are part of the result.

**Package check result:** all 17 cross-artifact checks passed, including the final manifest inventory and hashes. The unchanged retained OKF checker is reported separately below with its nine shape-recognition diagnostics; no native-runtime pass is implied.

## 1. Requirement-to-artifact review

| Assignment requirement | Concrete artifact and validation basis | Remaining boundary |
|---|---|---|
| Complete usable package and manifest | [Overview](00-START-HERE.md), [index](index.md), [manifest](manifest.json); every delivered file listed and hashed | Design approval is not installation authorization |
| Ingest current authority before design | [Findings](01-findings.md), [83 exact source snapshots/register](evidence/repository-sources.json), [guide comparison](evidence/reading-guide-comparison.json) | Targeted relevant reading, not an indiscriminate repository/workstation scan |
| Reconcile decisions and contrary evidence | [26 decisions and 82 options](design/decisions.json), [history](registry/history.json), [empirical appraisal](evidence/empirical-findings.md) | New estimates and paper scenarios are not measured effects |
| Current rule/activation coverage | [145 records](registry/rules.json), [schema](registry/rule-registry.schema.json), [coverage](registry/coverage.md); exact 23-tag equality, 100 authored detailed tags and 22 scoped clauses | Completeness is within the current owners and material boundaries actually inspected |
| Architecture and file integration | [Architecture](03-architecture.md), [95-entry integration map](design/integration-map.json), [six exact unapplied corrections](design/pointer-patch-proposals.json) | Operator review before changing any live owner, carrier, configuration or runtime |
| Fresh cross-CLI research | [49 claims](compatibility/claims.json), [62 primary sources](evidence/external-sources.json), [surface-specific specification](compatibility/compatibility.md) | Fourteen installed/native probes remain unexecuted |
| Concrete examples | [Three workflow candidates](examples/end-to-end-flows.md), [native examples](examples/native/README.md), [state schema](examples/activation-state.schema.json), [architecture comparison](examples/architecture-comparison.md) | Examples remain inert; canaries are not production enforcement logic |
| Realistic evaluation and adoption | [22 cases](evaluation/cases.json), [plan](evaluation/evaluation-plan.md), S0–S4 dependencies; focused assertions across all 23 XML rules | No native case is marked executed; no architecture success rate is claimed |
| Independent verification and failure analysis | Separate contribution/review passes, four scorer counterexamples, native semantic-negative fixtures, current-rule case oracles | Reviewers can share context and blind spots; this was not the repository’s formal blind Detective workflow |
| One ZIP; no live changes | Archive inventory/integrity verification and action boundary recorded in manifest | No branch, PR, commit, installation, CI change or deployment performed |

## 2. Executed checks and reproducible commands

Run commands from the extracted `apex-cli-agent-infrastructure/` root. Python 3.11+ is required; the recorded environment used `jsonschema 4.26.0` and `PyYAML 6.0.3`. The scripts perform only local artifact/synthetic checks. They do not invoke agent hosts, grant trust, alter permissions or contact an external runtime.

```bash
python -B validation/validate_package.py
python -B examples/native/offline_check.py
python -B examples/native/codex_offline_check.py
python -B evaluation/scorer_probe.py --scorer evidence/repository/apex-meta/informatics/final/research/10-ultra-upgrade-validation/score_eval.py --output /tmp/apex-scorer-reproduction.json
python -B validation/retained_validator_probe.py --output /tmp/apex-retained-validator-reproduction.json
```

The first command is read-only by default. The native offline scripts refresh only their local result JSON files; running them after extraction changes those result bytes and may require a new local manifest if the environment differs. For an immutable review copy, run reproduction commands in a disposable copy. The scorer command emits a new timestamped result to the chosen temporary path; the original packaged result remains intact. `-B` prevents Python cache files from becoming package artifacts.

### Source and registry checks

All 83 repository snapshots match authenticated Git blob SHA-1 and SHA-256 records, byte lengths and line counts. The guide comparison found 49 selected entries with unchanged hashes; none of those file citations depend on stale guide line windows. Six exact-path 404 responses are retained as access limits, not workstation absence claims.

The current XML tag set equals the registry’s 23 XML identities. All seven explicit XML references resolve and appear under mandatory matched delivery. Canonical alias chains terminate; dependency IDs resolve. All 145 source excerpts match their verified windows. One hundred authored priority tags retain exact text, including padded raw values such as `R05`; the 45 unscored XML/scoped records retain null source metrics. Historical candidates and supersessions remain in a separate record. Evidence: [registry validation](registry/validation.json) and [package validation](validation/results.json).

### Machine artifacts and integration checks

The registry validates against its supplied JSON Schema. New authored Markdown uses flat OKF-compatible frontmatter and unique concept IDs. Native configuration examples retain native schemas; frozen source files remain byte-identical instead of being reformatted. Local links, decision references, integration references, case rule IDs and capability source/probe IDs are checked across artifacts.

The six pointer proposals each match their original source exactly once, use the correct original hash, resolve to the actual owner, and remain unapplied. Multiple proposals touching the same file explicitly require grouped planning against the original bytes. They do not claim to be `patch_intent.v1`; the existing exact-match alternative is used, and the actual domain patch schema is preserved.

The optional activation-state example validates as **illustrative and unexecuted**. Negative fixtures reject adding authority promotion or claiming a passed native profile to that unexecuted example. This schema is proposal instrumentation, not a change to handoff, authority-state or native hook contracts.

### Native wire and synthetic scorer checks

The reproduced native examples pass **38 offline checks**: 10 general container/encoding checks and 28 Codex schema, semantic allowlist, configuration and provenance checks. Five Codex schemas plus upstream license/notice retain their release-specific provenance. Schema-valid but documented-unsupported `ask`, `continue:false` and legacy `approve` outputs are negative cases; runtime meaning is checked separately from wire shape. Evidence: [general results](examples/native/offline-results.json), [Codex results](examples/native/codex-offline-results.json), [schema provenance](compatibility/native-schemas/codex/provenance.json).

All **four synthetic scorer counterexamples reproduced** against the exact retained scorer hash: absent validator counted as success, empty deliverable accepted, unsuccessful Glob counted as a read, and unrelated mutation missed in a typo case. These demonstrate insufficient predicates, not false historical scores or an executed agent failure. The packaged [original result](evaluation/scorer-probe-results.json) retains its original timestamp and conditions; the final reproduction used the same source and confirmed the same four findings.

### Retained validator interpretation

The unchanged retained OKF checker is also exercised on a temporary authored-document projection, using temporary sub-bundle boundaries to exclude native configuration and frozen repository source schemas. Its raw diagnostics are retained separately in [retained-validator-results.json](validation/retained-validator-results.json). A checker’s successful execution and its actual diagnostics are distinct; none are silently converted into zero errors. The final diagnostic reconciliation below records the observed result.

### Diagnostic reconciliation for the unchanged OKF checker

After the manifest exists, the retained checker has **zero OKF errors, nine profile-shape diagnostics and 21 sentence-length advisories** on the declared projection. The raw report remains available; it is not a clean validator pass.

| Artifact | Profile diagnostics | Independent reconciliation |
|---|---:|---|
| `02-decisions.md` | 3 | The checker detects incidental phase references as a bake-off and then requires its own literal markers. It also counts zero options because its option regex requires a line to start with the option token; the actual decision options are table rows. JSON and semantic review confirm 26 complete decisions and 82 options. The distinct architecture bake-off is in its owning example file. |
| `01-findings.md` | 2 | Historical phase references are classified as an authored bake-off. This document is findings synthesis; the actual four-phase architecture comparison is separate and passes the checker’s shape recognition. |
| `evaluation/evaluation-plan.md` | 4 | A table of observation questions is classified as an operator decision sheet. Its cells define measures/oracles, not candidate choices. Material choices and the later approval sheet link to the real decision matrix. |

Source: `apex-meta/informatics/final/tools/check_decision_bakeoff_shape.py`, `looks_like_bakeoff`, `looks_like_decision_matrix`, `check_bakeoff_shape` and `check_decision_matrix_shape`. The code is frozen unchanged. The initial assembly-only missing-manifest link was a real defect and was corrected before final validation. The remaining diagnostics concern recognition/format, not missing decision substance; they are not waived as arbitrary test failures.

The 21 sentence-length advisories are retained as nonblocking orientations. Long sentences carrying exact authority/version distinctions are justified under WP-01/FA-04; no material requirement is removed to satisfy an advisory. A future approved checker repair should recognize explicit artifact intent and table rows, while preserving positive/negative fixtures and per-option checks. This package does not rewrite the live checker to obtain a green result.

## 3. Semantic review and corrections

Separate contributors reviewed the source registry, platform claims and empirical/evaluation design, then reviewed the root synthesis and integration artifacts. This is bounded independent artifact review. Reviewers had shared task context and could see the proposal; it is not described as blind cross-family experimentation or the named Multi-Agent Detective process.

The review produced concrete corrections before packaging:

- Preserved the current 23rd tag `align`, rather than importing the old 22-rule list; retained historical candidate IDs without promoting them.
- Corrected an initially overbroad pointer diagnosis: the governance schema link is valid; only the deeper patch-discipline link traverses too few parents. Reused the existing standalone `git-sync.md` and disclosed duplicate EM-12 ownership.
- Restored mandatory EM-07/GS-13 weighted criterion comparison when applicable, keeping it separate from unaggregated I/E/R. New evidence estimates were reduced/qualified where documentation did not establish empirical efficacy.
- Added contrary Stage-1 handover/placement results and retained system-prompt, scorer and model/task limitations. Kept the Round-2 hook/reminder confound explicit.
- Corrected platform source-ID mappings, false uniform L2 depth framing and schema-mismatched Claude permission wording. Added the conditional Claude hook adapter to its existing configuration integration entry without changing permission intent.
- Distinguished missing enforcement readiness from missing authorization; preserved an already-authorized supported fallback. Qualified EM-13 preflight by its actual unapproved/nontrivial scope.
- Named EM-09’s four real delegation dimensions and kept proposed transport metadata separate from the named-system handoff schema.
- Added substantive product-first/two-failure pivot and authorized disposable Git-sync cases. Split native compaction, explicit restart and synthetic replay into different recovery experiments.
- Corrected a criterion sensitivity arithmetic error and retained its consequence: alternate maintenance-heavy preferences can favor the improved-existing-only option.

These corrections improve source fidelity, not merely artifact shape. The operator can trace a conclusion from findings through decision, registry, architecture, integration entry, example and evaluation case without reconstructing the research.

## 4. Complexity and usability review

The proposed registry is detailed because it must account for every applicable current rule; it is not intended as a universal prompt payload. Shared lifecycle profiles prevent each entry from inventing a new mechanism. The three workflow candidates reuse existing owners; native adapters handle only their actual host differences. Existing skills, role definitions, board/state ownership and named-system boundaries are retained.

There is no new always-running service, database, permission authority or automatic scheduler. Production policy code is conditional on a justified pilot; the executable examples are deliberately narrow canaries and artifact checks. New schemas are limited to the requested registry and optional observation sidecar. The integration map references evidence without installing it. The ZIP includes frozen sources to make operator review self-contained, while the overview supplies a short review route.

The architecture comparison retains serious alternatives and shows sensitivity to maintenance priorities. Better outcomes for the improved-existing-system baseline would justify using that smaller design. Structural green checks cannot override that empirical result or the operator’s accepted constraints.

## 5. Remaining limitations and adoption boundary

The operator’s installed versions, account roots, effective trust/permissions and native tool coverage remain unknown. No cross-repository/global workstation inspection or original external trace-directory reproduction was performed. Current vendor documentation can change; version/surface claims and pinned schemas are recorded to bound that uncertainty.

All 22 agent cases and 14 native probes remain unexecuted. No numerical reliability claim for the proposed architecture, no causal hook-only gain and no local model/hardware selection follows from this package. The architecture bake-off uses explicitly estimated criteria, and its ranking can reverse under a different justified preference. An interactive L3 deployment review is not claimed complete.

The raw retained validator can have narrower shape recognition than the source-owned semantics. Its diagnostics require the reconciliation recorded below and do not certify the full product. Package-level JSON/schema/hash/link checks and semantic review support review readiness, not native installation acceptance.

**Failure guard:** treat this as a complete proposed design for review. Do not promote it to accepted or installed state, claim unexecuted trials, broaden permissions or modify live files without subsequent scoped operator authorization.
