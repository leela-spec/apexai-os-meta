You are right. Keeping every recovery file as a durable peer is **not** the cleanest KB design.

The better system is:

> **Five canonical files are the KB. Supporting files are temporary/control/reference appendices only when they prevent the five files from becoming bloated.**

The repo governance supports this: the per-agent KB root is explicitly the five-file scaffold, with `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md`, and `LEARNING_QUEUE.md` as the accepted/candidate surfaces. `LEARNING_QUEUE.md` is candidate-only, not runtime truth.

## Revised file-ownership model

|Current file|Best treatment|Why|
|---|---|---|
|`AGENT_CARD.md`|**Merge fully into `ESSENCE.md`, then delete/deprecate**|It duplicates identity, triggers, inputs, outputs, Leela surface summary, handoff partners. That is essence-level material.|
|`DOCTRINE.md`|**Merge mostly into `ESSENCE.md`; remaining routing/workflow pieces into `BEST_PRACTICES.md`**|Separate doctrine file creates a second doctrine authority. Bad KB hygiene.|
|`ROLE_BOUNDARIES.md`|**Split across `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`; keep appendix only if still too detailed**|Core owns/does-not-own belongs in Essence. Boundary checks belong in Best Practices. Drift/failure patterns belong in Mistakes.|
|`ROUTING_CONTRACT.md`|**Mostly merge into `BEST_PRACTICES.md` + `TEMPLATES.md`; keep appendix only if detailed route matrix is too long**|Routing behavior is a best practice; route-brief formats are templates.|
|`HANDOFF_SCHEMA.md`|**Merge core schema into `TEMPLATES.md`; invalid handoff patterns into `MISTAKES.md`**|A schema users reuse belongs in Templates. Invalid schema patterns belong in Mistakes.|
|`WORKFLOW_PLAYBOOK.md`|**Merge stable procedures into `BEST_PRACTICES.md`; reusable formats into `TEMPLATES.md`**|Workflow rules are practices unless they are too long, in which case they become a linked appendix.|
|`SOURCE_MANIFEST.md`|**Keep as supporting control file**|This is provenance/source ledger, not doctrine or practice. It should be indexed, not absorbed.|
|`COVERAGE_AUDIT.md`|**Keep as supporting control file for now**|This is validation/audit state. It should constrain canonical files, not become canonical content itself.|
|`README.md`|**Keep as folder index**|It should explain the canonical five-file system and point to appendices.|

## Corrected architecture

### 1. `ESSENCE.md`

Should contain:

- Alfred identity

- purpose

- owns / does-not-own

- adjacent-agent distinctions

- core operating maxim

- minimal Leela interpretation boundary

- links to source/audit files only as provenance, not doctrine


`AGENT_CARD.md` should be fully harvested into this file. The current `AGENT_CARD.md` is a fast identity card with activation triggers, inputs, outputs, Leela surface interpretation, handoff partners, and quality bar. That is too close to `ESSENCE.md` to justify a separate durable file.

### 2. `BEST_PRACTICES.md`

Should contain most of the practical material from:

- `ROLE_BOUNDARIES.md`

- `ROUTING_CONTRACT.md`

- `WORKFLOW_PLAYBOOK.md`

- source-gap protection rules from `SOURCE_MANIFEST.md` / `COVERAGE_AUDIT.md`


But not the raw source ledger or audit tables.

It should answer:

- how Alfred intakes

- how Alfred routes

- how Alfred checks boundaries

- how Alfred protects source gaps

- how Alfred uses EVD/IMP/RSK

- how Alfred prevents scaffold drift

- how Alfred handles one-file write flows


### 3. `MISTAKES.md`

Should contain:

- universal-executive drift

- generic-assistant dilution

- Sid overlap

- Algorithm replacement

- Path/Rhythm inversion

- hidden source-gap hardening

- **new:** scaffold-replacement drift

- **new:** appendix-as-authority drift

- **new:** duplicate-doctrine drift


The current `MISTAKES.md` already has several of these patterns, but it does not yet explicitly name the new scaffold/appendix problem.

### 4. `TEMPLATES.md`

Should contain:

- first-contact intake template

- weekly alignment template

- day-start frame template

- rhythm repair template

- recommendation handoff template

- escalation template

- compact route brief template

- canonical handoff YAML from `HANDOFF_SCHEMA.md`


The current `TEMPLATES.md` already contains several accepted templates, but it should link/absorb the most usable handoff schema content instead of leaving `HANDOFF_SCHEMA.md` as a parallel authority.

### 5. `LEARNING_QUEUE.md`

Should stay exactly candidate-only. No accepted material should be moved there unless it is a future candidate awaiting promotion.

## What should remain outside the five files?

Only these categories:

|Category|Keep outside?|Reason|
|---|--:|---|
|Source ledger|yes|`SOURCE_MANIFEST.md` is provenance.|
|Coverage/audit register|yes|`COVERAGE_AUDIT.md` is validation state.|
|Large route matrix|maybe|Keep only if too large for `BEST_PRACTICES.md`.|
|Large handoff schema examples|maybe|Keep only if too large for `TEMPLATES.md`.|
|Large workflow playbook|maybe|Keep only if too procedural for `BEST_PRACTICES.md`.|
|Duplicate doctrine summary|no|Merge into `ESSENCE.md`; delete/deprecate.|
|Duplicate agent card|no|Merge into `ESSENCE.md`; delete/deprecate.|

## Revised patch process

### Pass 1 — Consolidate canonical ownership

Patch one file at a time:

1. `ESSENCE.md`
    Merge `AGENT_CARD.md`, core `DOCTRINE.md`, and core `ROLE_BOUNDARIES.md`.

2. `BEST_PRACTICES.md`
    Merge routing practices, workflow practices, source-gap controls, boundary checks.

3. `MISTAKES.md`
    Add scaffold drift, duplicate doctrine, appendix-as-authority, source-gap hardening.

4. `TEMPLATES.md`
    Merge handoff schema and route-brief templates.

5. `LEARNING_QUEUE.md`
    Verify candidate-only. Probably no patch.


### Pass 2 — Collapse or demote extension files

After canonical files are strengthened:

|File|Action|
|---|---|
|`AGENT_CARD.md`|delete or replace with one-line redirect to `ESSENCE.md`|
|`DOCTRINE.md`|delete or replace with one-line redirect to `ESSENCE.md`|
|`ROLE_BOUNDARIES.md`|keep only if needed as boundary appendix; otherwise redirect|
|`ROUTING_CONTRACT.md`|keep only if detailed appendix remains useful|
|`HANDOFF_SCHEMA.md`|keep only if detailed appendix remains useful|
|`WORKFLOW_PLAYBOOK.md`|keep only if detailed appendix remains useful|
|`SOURCE_MANIFEST.md`|keep|
|`COVERAGE_AUDIT.md`|keep|
|`README.md`|keep folder index|

### Pass 3 — Update README again

After consolidation, patch `README.md` to classify extension files as:

- **absorbed**

- **active appendix**

- **source/audit control**

- **deprecated redirect**


## Revised immediate next action

Do **not** patch `ESSENCE.md` merely by adding links.

Patch `ESSENCE.md` by **absorbing `AGENT_CARD.md` and the core identity/boundary doctrine from `DOCTRINE.md` and `ROLE_BOUNDARIES.md`**.

Then mark `AGENT_CARD.md` as redundant in the backlog.

That gives you a KB system that makes actual sense:

> `ESSENCE.md` = Alfred’s identity and authority.
> `BEST_PRACTICES.md` = Alfred’s operating method.
> `MISTAKES.md` = Alfred’s known failure modes.
> `TEMPLATES.md` = Alfred’s reusable forms.
> `LEARNING_QUEUE.md` = non-truth candidate intake.
> Everything else = source/audit/appendix, never a second scaffold.