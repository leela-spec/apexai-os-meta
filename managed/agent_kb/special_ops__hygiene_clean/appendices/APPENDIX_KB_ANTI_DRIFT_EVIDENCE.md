# APPENDIX_KB_ANTI_DRIFT_EVIDENCE

## Purpose

Evidence appendix for `special_ops__hygiene_clean` anti-drift and cleanup discipline.

This file preserves postmortem and process evidence as evidence. It does not promote any evidence item into accepted runtime truth by itself.

## Evidence status boundary

- **Rule:** Failure evidence may support safeguards, but it is not automatic universal doctrine.
- **Rule:** A hygiene finding remains a finding until routed, verified, closed, or escalated.
- **Rule:** A candidate improvement remains candidate-only until promotion or explicit acceptance occurs through the governed path.

## Authority and verification gates

| Evidence id | Source class | Failure or control signal | Hygiene extraction | Reusable safeguard |
|---|---|---|---|---|
| HC-EVID-001 | authority_and_verification | Source authority and output verification are often collapsed. | Treat authority as pre-step and verification as post-step. | Require source tier, missing-input check, and evidence-backed verification before approval. |
| HC-EVID-002 | authority_and_verification | Agents guess through missing sources or conflicts. | Missing authority is a stop condition. | Use `NEEDS_INPUT`, `ESCALATE`, or `REFUSE` states rather than silent invention. |
| HC-EVID-003 | authority_and_verification | Fluent output is mistaken for verified output. | Self-check alone is not enough for factual or file-state claims. | Require file, diff, source, test, or trace evidence. |

## Migration and patch drift

| Evidence id | Source class | Failure or control signal | Hygiene extraction | Reusable safeguard |
|---|---|---|---|---|
| HC-EVID-004 | migration_process | Execution drift occurs when a task is framed as design rather than bounded execution. | Lock authority order, mode, target set, and stop conditions. | Use exact preflight block before edits. |
| HC-EVID-005 | migration_process | Move/path repair becomes semantic redesign. | Preserve wording unless exact path-truth correction is authorized. | If minimal repair is impossible, stop and report. |
| HC-EVID-006 | migration_process | Broad multi-file passes cause context loss and rewrite cascades. | One-file-at-a-time is a hygiene control for drift-sensitive files. | Patch one target, validate, then proceed. |

## Wording and rewrite drift

| Evidence id | Source class | Failure or control signal | Hygiene extraction | Reusable safeguard |
|---|---|---|---|---|
| HC-EVID-007 | drift_validation | A file was semantically rewritten instead of path-normalized. | Drift can be useful-looking but still non-compliant. | Classify content-preservation violations explicitly and restore/narrow. |
| HC-EVID-008 | drift_validation | Multiple protected files had non-required wording changes. | Cleanup edits may be practical yet still outside scope. | Distinguish defensible path truth from unauthorized behavior changes. |
| HC-EVID-009 | drift_validation | Repair by interpretation was the recurring failure. | Dead references create decision points. | Choose minimal exact repair or stop; do not reinterpret. |

## Execute-not-explain failure

| Evidence id | Source class | Failure or control signal | Hygiene extraction | Reusable safeguard |
|---|---|---|---|---|
| HC-EVID-010 | execution_failure | The agent explained process instead of executing the requested bounded task. | Explanation drift is a task-compliance failure. | If asked to execute, perform the next authorized action unless blocked. |
| HC-EVID-011 | execution_failure | Agent proposed rewrite/reconstruction for bounded repair. | Rewrite instinct is a protocol violation for bounded defects unless authorized. | Use exact-span patching and stop on uncertain source text. |
| HC-EVID-012 | execution_failure | Process-critical rules existed but were not re-anchored during execution. | Rules must be re-read or represented as hard task locks. | Require task lock with exact file, spans, allowed action, forbidden action, completion condition. |

## Process-gate bypass

| Evidence id | Source class | Failure or control signal | Hygiene extraction | Reusable safeguard |
|---|---|---|---|---|
| HC-EVID-013 | process_gate | Process pack was treated as design inspiration rather than execution constraints. | Citing rules is insufficient. | A run must prove compliance with active gates before action. |
| HC-EVID-014 | process_gate | Move-only mode silently became move + edit + scaffolding. | Mode drift must be detected immediately. | Declare one mode and block if successful completion requires mode crossing. |

## Topology and merge-mode drift

| Evidence id | Source class | Failure or control signal | Hygiene extraction | Reusable safeguard |
|---|---|---|---|---|
| HC-EVID-015 | topology_drift | Target-state design began before merge into living files was proven impossible. | New-file creation requires no-fit proof. | Insert merge-map or no-fit gate before target-file matrix. |
| HC-EVID-016 | topology_drift | Execution artifacts outran upstream content acceptance. | Downstream execution must not outrun target/file acceptance. | Demote later execution artifacts until upstream target logic is re-verified. |

## Validation evidence patterns

| Evidence id | Source class | Failure or control signal | Hygiene extraction | Reusable safeguard |
|---|---|---|---|---|
| HC-EVID-017 | validation_pattern | Exact file-copy validation used file count, missing/extra detection, bytes, chars, lines, and SHA-256. | Exact preservation can be mechanically verified. | Use checksum/metric validation when content equality matters. |
| HC-EVID-018 | residual_guidance | Confirmed structure, recommended extensions, optional omissions, and cautions were separated. | Residual guidance must not silently become implementation law. | Type residual items by confidence and allowed next action. |

## Anti-drift control map

| Drift class | Detection cue | Required hygiene response |
|---|---|---|
| Authority drift | summary used as primary, conflict hidden, missing source guessed through | stop or mark `NEEDS_INPUT`; identify primary source |
| Verification drift | output forwarded without file/diff/source/test evidence | mark unverified; require verification artifact |
| Rewrite drift | bounded task causes whole-file rewrite or semantic replacement | stop; require exact span patch or authorization |
| Mode drift | move becomes edit, validate becomes patch, research becomes execution | stop; re-lock mode |
| Scope drift | undeclared file, new target, new architecture, or extra cleanup appears | stop; report scope expansion |
| Closure drift | severe finding disappears from prose without evidence-backed closure | reopen or escalate finding |
| Candidate/truth drift | candidate or hygiene finding is treated as accepted truth | route through promotion or keep candidate-only |

## Use in scaffold files

- `BEST_PRACTICES.md` may summarize safeguards.
- `MISTAKES.md` may summarize reusable failure patterns.
- `TEMPLATES.md` may provide record shapes.
- `ESSENCE.md` may point here for evidence.
- `LEARNING_QUEUE.md` may capture future candidate improvements with evidence references.
