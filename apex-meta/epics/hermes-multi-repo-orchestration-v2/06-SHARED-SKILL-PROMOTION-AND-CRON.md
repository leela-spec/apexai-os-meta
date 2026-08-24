# 06 — Shared Skill Promotion and Delayed Cron Flow

Status: **D04/D05 VERIFIED DESIGN / LIVE AUTOMATION TEST REQUIRED**  
Date: 2026-08-24

## Core decision

Do **not** synchronize raw Hermes memory or copy learned files directly from one project repo to another.

Use a delayed promotion pipeline:

```text
repo work
  -> role-local learning
  -> deterministic scheduled candidate harvest
  -> independent generalization/review
  -> versioned canonical shared skill in Apex
  -> controlled runtime distribution
  -> other roles/repos can use it when relevant
```

Synchronization can be hourly/daily/on-demand; it does not need to occur during the source task.

## Why skills are the spillover unit

Agent Skills are portable directories with:

```text
skill-name/
  SKILL.md
  scripts/       optional
  references/    optional
  assets/        optional
```

The standard is explicitly designed for progressive disclosure: metadata is cheap at startup, the main procedure loads on activation, and supporting resources load only when required.

That is a much better exchange object than raw profile MEMORY, entire conversations, or copied repo documents.

## Canonical state model

```text
ROLE PROFILE
  ~/.hermes/profiles/<role>/skills/learned/
       |
       | produces candidates
       v
APEX PROMOTION INBOX / REVIEW
       |
       | accepted only
       v
APEX CANONICAL SHARED-SKILL SOURCE (Git)
       |
       +--> Hermes runtime distribution
       +--> future Claude/Codex adapters where verified
```

Project facts never enter this pipeline.

## Stage A — local learning

A role performs one task in one repo.

Example:

```text
research-strategist
board = investment
repo  = Investment
```

Outputs are separated:

| Observation | Destination |
|---|---|
| Investment provider is stale | Investment evidence/decision |
| Task completed/blocked | Investment board |
| User prefers concise source matrix | USER/profile memory if truly global preference |
| Reusable validation procedure | role-local learned skill candidate |

The agent does not write the reusable procedure into ACIM or MasterOfArts.

## Stage B — deterministic scheduled harvest

Purpose: detect **new/changed learning candidates**, not judge them.

Recommended implementation class:

```text
Hermes no-agent cron OR OS scheduler
  -> deterministic script
  -> zero LLM calls
  -> zero model tokens
```

Candidate inventory fields:

```yaml
candidate_id: sha256(...)
profile: research-strategist
source_skill_path: ...
source_hash: ...
first_seen_at: ...
last_seen_at: ...
source_repo_if_known: Investment
review_status: pending
```

The script should compare hashes/manifests so unchanged skills do not repeatedly create work.

### Do not harvest raw MEMORY.md

MEMORY may contain:
- environment facts;
- project conventions;
- user-specific information;
- temporary lessons.

A raw-memory copying pipeline would make factual contamination worse, not better.

## Stage C — create one Apex review item

When changed candidates exist, the deterministic stage may create or refresh an Apex-board review task using an idempotency key.

Conceptual task:

```yaml
title: Review reusable learning candidates 2026-08-24
board: apex
assignee: independent-reviewer
metadata:
  candidate_manifest: <Apex path or local receipt>
  candidate_count: 2
  idempotency_key: learning-review:<manifest-hash>
```

No LLM is required to discover that candidates exist.

## Stage D — semantic/generalization review

The reviewer receives **only the changed candidate + necessary provenance**, not all four repositories.

Pass criteria for promotion:

1. **Generalizable:** useful beyond the source task/repo.
2. **No project facts:** no holdings, private identifiers, current repo status, product facts, transient paths.
3. **No secret material:** no keys/tokens/customer data.
4. **No duplicate:** does not recreate an existing shared skill.
5. **Clear trigger:** description tells an agent when to activate it.
6. **Deterministic where possible:** scripts/checks used for mechanical steps.
7. **Failure guidance:** known failure modes and recovery included.
8. **Verification:** success test is explicit.
9. **Agent Skills valid:** standard frontmatter/structure.
10. **Evidence:** source task/experience is referenced without copying sensitive project content.

Possible verdicts:

```text
PROMOTE
KEEP_ROLE_LOCAL
MERGE_WITH_EXISTING
REJECT_PROJECT_SPECIFIC
REJECT_UNSAFE
NEEDS_HUMAN_DECISION
```

## Stage E — canonical promotion in Apex

Accepted procedure becomes versioned Git content in a future reviewed location such as:

```text
apex-meta/orchestration/hermes/shared-skills/
  authority-first-navigation/
    SKILL.md
    references/
  source-verification/
    SKILL.md
```

Exact production path is an implementation decision; do not create the final library until the two-repo promotion test passes.

Apex is the **reviewed canonical source**, not the runtime scratch directory.

## Stage F — Hermes distribution options

### Option 1 — Hermes external skill directory

Hermes supports:

```yaml
skills:
  external_dirs:
    - /path/to/shared/skills
```

Advantages:
- no per-repo copy;
- discovered by profiles;
- progressive disclosure;
- local profile skills can override same-name external skill.

Risk:
- Hermes explicitly states external dirs are not a write-protection boundary; if writable, `skill_manage` can edit/delete skills in place.

Therefore do not point autonomous profiles directly at a writable canonical Apex Git source unless that mutation policy is intentional.

### Option 2 — deployed read-only copy of Apex shared skills

```text
Apex Git canonical source
  -> deterministic deployment
  -> ~/.agents/skills/apex-reviewed/
  -> Hermes external_dirs
```

Advantages:
- separates learning scratch from reviewed source;
- canonical Git stays protected from routine agent self-editing;
- runtime remains simple.

Cost:
- one deterministic deployment step.

### Option 3 — Hermes Skills Tap

Hermes supports GitHub-backed custom skill taps. A tap is a Git repo/path containing standard SKILL.md directories.

Advantages:
- native install/update mechanism;
- source is Git/versioned.

Cost:
- installed copies are profile-local;
- multi-profile update policy must be defined/tested.

**Initial recommendation:** test Option 2 and Option 3; choose the simpler proven behavior on the installed version. Do not build a custom registry.

## Why not copy promoted skills into every repo?

Repo-local copies create:

- version drift;
- repeated updates;
- stale duplicated procedures;
- confusion about which copy is canonical;
- unnecessary Git churn.

Only install a shared procedure into a repo when a specific external tool requires repo-local discovery or the procedure is intentionally project-owned.

## Hermes Cron verification

Official Hermes Cron supports:

- recurring jobs;
- project `workdir`;
- no-agent script-only mode;
- zero-token execution in no-agent mode;
- fresh sessions for agent-mode jobs;
- scripts constrained under `$HERMES_HOME/scripts/`;
- sanitized provider credentials for script subprocesses.

### Important current risks

1. **#20353:** a script can intentionally/accidentally exit 0 with no output and appear silent; do not treat silence as health.
2. **#77131:** v0.19.1 had a lifecycle-guard false positive blocking Python no-agent scripts using ordinary `pathlib` syntax. Test installed version before relying on Python cron.
3. **#80624:** a high-severity August 2026 cron persistence bug was filed and then closed/fixed; still regression-test persistence while gateway is running.
4. Workdir cron jobs are intentionally serialized; this is safe but can delay many scheduled jobs.

### Cron health contract

Every deterministic automation must write/maintain a health receipt:

```yaml
job: learning-candidate-harvest
last_attempt_at: ...
last_success_at: ...
input_fingerprint: ...
output_fingerprint: ...
candidates_found: 0
status: success|failed|partial
error: null
```

Rules:

```text
parse/query error -> non-zero exit
partial board/profile scan -> non-zero exit
schema invalid -> non-zero exit
no changes -> success + candidates=0
```

Do not use `empty stdout` as the sole success signal.

## Initial scheduling policy

Because the user does not require immediate synchronization:

```text
candidate harvest: daily or after meaningful execution batch
promotion review: only when candidates exist
shared-skill deployment: after accepted promotion
```

This is more efficient than running an LLM reviewer every hour.

## Autonomous but controlled flow

```text
[repo task completes]
        |
        v
[role learns locally]
        |
        | later
        v
[no-agent candidate hash scan]         0 model calls
        |
     changes?
      /    \
    no      yes
    |        |
  stop       v
       [Apex review task]
              |
              v
       [independent-reviewer]
              |
       promote only if general
              |
              v
       [Apex Git shared skill]
              |
              v
       [deterministic deployment]
```

## MarketingSkills and BMAD exclusions

This shared-learning pipeline does **not** imply globally installing every third-party skill pack.

Current policy:

- MarketingSkills: **MasterOfArts only** until another repo has a real marketing need.
- BMAD: install project-locally in each repo that needs it; do not global-link based on unshipped proposals.
- repo-specific skills: stay in the repo.
- only independently promoted generic procedures enter Apex shared skills.

## Acceptance tests

- [ ] role learns one harmless procedural candidate in repo A;
- [ ] deterministic harvest detects it exactly once;
- [ ] unchanged second run produces zero new candidates;
- [ ] candidate with repo fact is rejected/kept local;
- [ ] candidate with generic method is promoted;
- [ ] promoted skill validates against Agent Skills spec;
- [ ] runtime profile can discover promoted skill without copying it into repo B;
- [ ] local repo skill of same name correctly overrides shared one where intended;
- [ ] canonical Apex source cannot be silently mutated by normal runtime self-improvement path;
- [ ] cron failure yields non-zero/error health state;
- [ ] cron survives gateway/restart acceptance test;
- [ ] no MEMORY.md is synchronized.

## Primary sources

- Hermes Skills: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/
- Agent Skills specification: https://agentskills.io/specification
- Hermes Cron: https://hermes-agent.nousresearch.com/docs/user-guide/features/cron
- Hermes no-agent cron guide: https://github.com/NousResearch/hermes-agent/blob/main/website/docs/guides/cron-script-only.md
- Cron silent-output issue #20353: https://github.com/NousResearch/hermes-agent/issues/20353
- Cron Python guard issue #77131: https://github.com/NousResearch/hermes-agent/issues/77131
- Cron persistence issue #80624: https://github.com/NousResearch/hermes-agent/issues/80624
- Hermes Profile Distributions: https://hermes-agent.nousresearch.com/docs/user-guide/profile-distributions
