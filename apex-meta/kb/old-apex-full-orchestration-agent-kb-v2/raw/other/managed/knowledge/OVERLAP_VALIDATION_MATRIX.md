# OVERLAP_VALIDATION_MATRIX

## Purpose

This matrix records the mandatory cross-checks for the most drift-prone overlap boundaries in the final v1 first-wave agent system.

## Matrix

| Boundary | Primary owner | Risk if blurred | Required validator | Required check | Required record / stop condition |
|---|---|---|---|---|---|
| Alfred vs Meta Ops | `alfred` / `meta_ops` | intake collapses into unbounded orchestration | `meta_ops` | did Alfred stop at intake, route brief, constraint capture, and missing-input surfacing? | record validator result before durable handoff; stop if Alfred assigns execution order or claims orchestration ownership |
| Meta Ops vs Meta Strategy | `meta_ops` / `meta_strategy` | execution routing and strategic recommendation collapse into one voice | `meta_detective` | is there still a distinct options or recommendation packet and a distinct execution owner? | stop if recommendation is treated as execution without explicit owner and validation |
| Meta Strategy vs Meta Detective | `meta_strategy` / `meta_detective` | recommendation and challenge become self-justifying | `meta_ops` | was the recommendation independently challenged without the challenge becoming the execution plan? | stop if the same output both recommends and validates a durable decision without independent review |
| Meta Detective vs Execution Ownership | `meta_detective` / `meta_ops` | validator posture becomes executor authority | `special_ops__hygiene_clean` | did Meta Detective remain validator/challenger rather than patch author or execution owner? | stop if Meta Detective mutates target truth, owns application, or bypasses assigned execution owner |
| Knowledge Bank vs Informatics Design | `special_ops__knowledge_bank` / `special_ops__informatics_design` | storage ownership and readability/shape ownership collapse | `special_ops__informatics_design` | did Knowledge Bank decide placement and Informatics Design decide shape/readability? | record both placement and shape rationale; stop if one lane silently owns both |
| Knowledge Bank vs Promotion / Candidate Material | `special_ops__knowledge_bank` / promotion path | source, queue, and accepted canon separation collapses | `meta_detective` | was source or candidate material routed through promotion before accepted use? | stop if Knowledge Bank self-promotes source material, candidate material, or queue entries into runtime truth |
| Agent KB Scaffold vs Learning Queue | `special_ops__knowledge_bank` / first-wave agents | non-5-file KB variants appear or learning queues become runtime truth | `meta_detective` | does each first-wave KB root retain exactly `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md`, and `LEARNING_QUEUE.md`, with queue content candidate-only? | stop on any 3-file or 4-file KB variant, or if `LEARNING_QUEUE.md` is treated as accepted/canon truth |
| Informatics Design vs Hygiene Clean | `special_ops__informatics_design` / `special_ops__hygiene_clean` | structural design and structural audit merge | `special_ops__hygiene_clean` | was the artifact shaped first and audited second? | stop if cleanup reshapes the artifact without a separate design decision or review trace |
| Hygiene Clean vs Meta Detective | `special_ops__hygiene_clean` / `meta_detective` | structural QA and adversarial plausibility challenge become interchangeable | `meta_detective` | is the issue structural correctness, authority plausibility, or both with separate dispositions? | record finding class and validator; stop if QA backlog becomes adversarial doctrine or vice versa |
| Hygiene Clean vs Truth Mutation | `special_ops__hygiene_clean` / promotion path | cleanup becomes unreviewed accepted-truth mutation | `meta_detective` | did Hygiene Clean produce findings, holds, backlog items, or bounded patches without changing truth by cleanup alone? | stop if hygiene cleanup mutates accepted truth or hides unresolved authority risk |
| Prompts/Workflows vs AI Handling/Routing | `special_ops__prompts_workflows` / `special_ops__ai_handling_routing` | reusable workflows start dictating runtime posture or model/tool policy | `meta_ops` | is the workflow reusable independent of advisory model/tool-choice guidance? | stop if a reusable workflow embeds unreviewed runtime posture or config advice as law |
| AI Handling/Routing vs Runtime Config | `special_ops__ai_handling_routing` / runtime config | advisory routing becomes unreviewed config change | `meta_detective` | did the recommendation remain advisory and leave `openclaw.json` untouched? | stop if model/tool advice edits runtime config or is treated as config authority |
| Meta Ops vs Promotion | `meta_ops` / promotion path | orchestration silently mutates accepted truth | `meta_detective` | was a packet required, scored, reviewed, and approved before application? | stop if orchestration applies a durable truth change without packet trace, approval, and EVD/IMP/RSK |

## Rule

Any durable change above T0 that crosses one of these boundaries must record the validator, check result, required record/stop disposition, and any applicable `EVD`/`IMP`/`RSK` scores in its handoff or ledger entry.

## Boundary note

This matrix is a managed validation companion surface.
It does not replace the canons, the promotion protocol, the handoff contracts, or the per-agent KB index.
