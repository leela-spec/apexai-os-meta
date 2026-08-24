# Stack Expansion Research Review Protocol

Status: **MANDATORY PER TRACK**

Use after each R00-R09 draft and before persisting it.

## Reviewer task

Re-check the draft against:

1. its authoritative research specification;
2. current official sources;
3. current repository evidence;
4. the evidence states and integration classes in `PROJECT-INSTRUCTIONS.md`;
5. `MATRIX-SCHEMA.yaml` where a matrix/ranking is involved.

Do not repair a missing capability by designing an integration.

## Mandatory checks

### Coverage

- every Research Task is answered;
- every Required Output is present;
- the stated verdict follows the specification's pass/fail rule;
- real Master of Arts user stories are used where required.

### Evidence

- every load-bearing claim has a current source;
- official source text/source code directly supports the claim;
- vendor claims are labelled as such;
- current issues/PRs are checked against status, affected version and subsequent fixes;
- adoption metrics are not misrepresented as reliability;
- prior Hermes research `SUPPORTED_INFERENCE` claims are not silently promoted to verified.

### Integration

For each claimed connection, verify:

`from | to | exact mechanism | protocol/transport | supported roles both ends | auth/API | persistent state | integration class | source`

Reject these reasoning shortcuts:

- “both use MCP, therefore integrated”;
- “both support Python, therefore easy integration”;
- “an API exists, therefore the integration is established”;
- “Agent Skills compatible, therefore every runtime can execute all tools”;
- “local-first, therefore no external egress”;
- “agent framework, therefore it replaces Hermes Kanban/project context”.

### Operational value

Separate:

- technical capability;
- current maintenance/test evidence;
- reported operational experience;
- proven fit to the specific MoA user story.

A technically real component with weak operational evidence may still be a `PILOT`, but it cannot be described as proven.

### Matrix

For R07-R09:

- every substantive cell has evidence IDs;
- unsupported cells are `OPEN/UNVERIFIED`;
- asymmetric modules are not forced into a whole-stack ranking;
- hard filters are applied before MCDA;
- swing weighting is based on actual performance spread;
- sensitivity/switching conditions are shown;
- a single score is not allowed to hide decisive constraints.

### No invention / duplication

- no custom connector/router/sync/database has been smuggled into the recommendation;
- duplicate task state, facts, agent definitions, memories and retrieval stores are identified explicitly;
- any extra control plane has a verified benefit exceeding its added operational burden.

### Costs and constraints

Verify claims about:

- license/commercial use;
- installation and operating dependencies;
- API keys/provider billing;
- ChatGPT/Codex subscription compatibility;
- local-model path;
- token/context overhead;
- Windows/WSL;
- network/data egress;
- persistence and recovery.

## Verdict format

Return:

```text
VERDICT: PASS | REVISE | BLOCK

CRITICAL_FINDINGS:
- ...

UNSUPPORTED_OR_OVERSTATED_CLAIMS:
- claim:
  problem:
  required correction:

INTEGRATION_EDGES_NOT_PROVEN:
- ...

MATRIX_CELLS_WITHOUT_SUFFICIENT_EVIDENCE:
- ...

STALE_OR_WEAK_SOURCES:
- ...

MISSING_REQUIRED_OUTPUTS:
- ...

CONTRADICTIONS_OR_OPEN_QUESTIONS:
- ...

REQUIRED_REVISIONS:
- ...

DECISION_IMPACT:
- whether any issue could change KEEP/ADD/PILOT/REPLACE/DEFER/REJECT or the overall recommendation
```

If `REVISE`, the producing Work run corrects and re-reviews automatically.

If `BLOCK`, persist the blocked result and reason. Independent downstream research may continue only when it does not depend on the blocked conclusion.

## R08 independence requirement

R08 is not a normal stylistic review. It must independently re-open the load-bearing sources behind R07 and actively try to falsify:

- all proposed additions/replacements;
- all claims that the existing Hermes stack already covers a capability;
- all integration claims;
- all maturity/production-value claims;
- all token/cost/privacy advantages;
- the preliminary MCDA result.

R09 may not begin from an uncorrected R07 if R08 finds decision-changing errors.
