# S12 — Selective External Verification

**Execute only S12, then stop.**  
**Input:** S11 validated Reduce result  
**Next:** S13

## Outcome

Externally verify only important/checkworthy factual claims while preserving the distinction between what the source said and whether external evidence supports it.

## Context to load

- this file;
- S11 handoff/Reduce result;
- TTK `make-verify` routing code/contract;
- verification-result validator;
- `06-TRIAL1-TRANSPORT-LOCK.yaml`;
- selected allowed CLI's actual web/search capability documentation/config only as needed.

Do not load unrelated web research or all source history.

## Routing authority

TTK deterministically creates the checkworthiness queue. Do not ask the AI to decide from the entire transcript what should be researched.

Default route only:

- important/checkworthy `fact` claims;
- externally testable estimates where material.

Do not routinely verify opinions, predictions, recommendations, anecdotes, or every sentence.

## Trial-1 transport

Allowed semantic/research execution:

- Claude Code subscription CLI with permitted WebSearch/WebFetch capabilities;
- Codex CLI using ChatGPT-plan authentication and its available search capability;
- Antigravity only after its real headless smoke PASS and only if its research tooling is actually usable.

Forbidden: browser AI, Gemini CLI, paid/API-key model transport.

## Work

1. Generate current verification queue from S11 result.
2. If queue is empty, record successful no-op with reason.
3. For each queued claim, supply only the claim, relevant source context/provenance, and verification task to the allowed CLI.
4. Prefer primary/official external sources.
5. Preserve external evidence references sufficient for an evaluator to inspect.
6. Use `UNVERIFIED` when evidence is insufficient; never manufacture a decisive verdict.
7. Validate verification results with TTK.

## Tests

- queue contains only permitted checkworthy claim types;
- verification result maps to the exact queued claim ID;
- decisive verdicts contain actual supporting/contradicting external evidence where contract requires it;
- source support field is not overwritten by external verdict;
- unavailable research capability yields `UNVERIFIED`/BLOCKED rather than browser/API fallback;
- no credentials stored.

## Outputs

- TTK verification queue/results under the run;
- compact external source/evidence records already required by contract;
- S12 handoff.

Handoff must state queue count, verified/contradicted/mixed/unverified counts, actual CLI transport, evidence limitations, and exact verification-results path/hash.

## Acceptance

PASS means the queue was processed truthfully under Trial-1 policy, including valid `UNVERIFIED` outcomes.

Commit/push stage code/test fixes if needed, return handoff, **STOP.**