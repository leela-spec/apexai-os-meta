# Apex KB Phase 0 Setup Decision Register

## Status

```yaml
schema: apex.kb.phase0-setup-decision-register.v1
status: operator_reviewed_draft
scope: phase_0_setup_only
repository: leela-spec/apexai-os-meta
source_pack: apex-kb-mechanistic-workflow-pack
last_operator_review: 2026-07-17
implementation_status: not_implemented_by_this_file
```

This file records the current operator-approved direction for the Apex KB Setup module. It is a design and implementation ledger, not runtime authority. Live scripts and schemas remain implementation truth until deliberately changed and tested.

## 1. Product target

Phase 0 Setup should feel like one simple operation:

```text
apexkb start
  -> print fixed Q&A and option guide
  -> operator fills one configuration
  -> deterministic validation and read-only preflight
  -> operator reviews facts, warnings, and expected outputs
  -> operator revises or confirms
  -> same configuration is locked
  -> minimum scaffold and Phase 1 handoff are created
```

The default path must not depend on AI interpretation, AI-generated topics, AI-selected folders, or chat memory.

## 2. Locked operator-facing decisions

| ID | Decision | Status | Rationale |
|---|---|---|---|
| P0-D01 | Use one public start surface: `apexkb start`, with `/apex-kb start` as an optional Claude Code adapter. | locked | The operator should start one process, not choose internal control actions. |
| P0-D02 | Starting without a configuration prints a fixed, versioned Q&A file containing explanations, option effects, and an exact JSON template. | locked | The same guidance must appear every time without model improvisation. |
| P0-D03 | The operator fills one JSON configuration. Scripts read that object directly. | locked | Avoid AI translation drift and competing configuration authorities. |
| P0-D04 | The default setup route is deterministic-only. | locked | AI is not trusted to infer paths, topics, scope, or settings. |
| P0-D05 | AI recommendations are optional and explicitly selected by the operator. | locked | Recommendations can add value, but may never become silent configuration changes. |
| P0-D06 | The preflight checks whether required deterministic capabilities are available. The operator is not asked whether Python or repository commands can run. | locked | Capability detection belongs to scripts. Missing capability produces a blocker. |
| P0-D07 | The operator supplies the source repository, source folders, target repository/folder, KB identity, topics, topic vocabulary, target questions, exclusions, source handling, output tier, deterministic profile, graph option, and special constraints. | locked | These inputs materially control scope, cost, and value. |
| P0-D08 | Topics and target questions are operator-authored. Scripts and AI may not invent, replace, broaden, or silently merge them. | locked | Prior topic drift made outputs unusable. |
| P0-D09 | Multiple operator-defined topics may be listed in the configuration. No additional topics are auto-created after preflight or corpus mapping. | provisional_lock | Backend batching and lifecycle implications still require implementation review. |
| P0-D10 | One configuration flows downstream. Preflight reports, readbacks, and stage results are derived views, not additional configuration authorities. | locked | Prevent configuration duplication and drift. |
| P0-D11 | Source handling is an explicit operator choice: pointer, copy, or snapshot. | locked | It materially affects storage, reproducibility, and source custody. |
| P0-D12 | Output depth is an explicit operator choice with plain-language effects. | locked | The operator must understand the difference between analysis, compiled knowledge, and query-ready output. |
| P0-D13 | Graph/detail options are selected during setup and explained before the operator fills the JSON. | locked | They affect deterministic workload and discovery value. |
| P0-D14 | Preflight reports both safety facts and useful workload statistics before confirmation. | locked | The operator should understand the proposed run before expensive work begins. |
| P0-D15 | The same confirmed configuration is fingerprinted and referenced by run state. A full duplicate run manifest is not accepted without a unique proven consumer. | provisional_lock | A hash plus reference should normally provide drift detection without another full copy. |

## 3. Public versus internal command surface

### Public now

| Command | Purpose |
|---|---|
| `apexkb start` | Print the fixed Q&A, validate a supplied configuration, run read-only preflight, and request confirmation. |

### Reserved for later public design

| Command | Intended purpose | Current decision |
|---|---|---|
| `apexkb status` | Show current run state and last result. | useful, but not part of the current Start micro-design |
| `apexkb continue` | Execute the next legal stage after a confirmed setup. | reserve name; define after Start is proven |
| `apexkb repair` | Run bounded recovery after a reason-coded blocker or configuration change. | reserve name; define after Start is proven |

### Internal backend operations

The following may remain internally because they provide implementation value, but they should not be exposed as normal operator choices:

| Existing action | Disposition | Public replacement |
|---|---|---|
| `init` | keep internally or merge into `start` | `apexkb start --config <path>` |
| `confirm` | keep internally as the lock action | confirmation inside the Start flow |
| `run` | keep internally | future `continue` |
| `next` | keep internally for deterministic transition selection | future `continue`/`status` output |
| `reconcile` | keep internally for recovery and invalidation | future `repair` |
| `git-state` | keep as an internal preflight check | preflight report |
| `doctor` | keep as an internal package diagnostic | preflight blocker or explicit maintenance command |

Do not delete reliable backend behavior merely to make the public interface smaller. Simplification means hiding or merging internal operations, not removing recovery and validation guarantees.

## 4. Two setup modes

### Mode A — deterministic only

```yaml
preflight_assistance: deterministic_only
```

The runtime:

1. validates the configuration schema;
2. checks repositories, paths, overlap, permissions, and capabilities;
3. calculates factual scope and workload statistics;
4. returns pass, pass-with-warnings, or fail;
5. does not recommend alternative topics, questions, folders, scope, or settings.

### Mode B — optional AI recommendations

```yaml
preflight_assistance: ai_recommendations
```

The runtime first completes the same deterministic preflight. A bounded AI may then explain warnings or propose operator-reviewable changes.

The AI may:

- summarize deterministic evidence;
- explain tradeoffs between already-defined options;
- recommend changing an option when the deterministic report provides a concrete reason;
- propose wording improvements for an operator-supplied target question without replacing the original;
- identify missing information and ask for an explicit operator decision.

The AI may not:

- change the configuration;
- invent or add topics, aliases, keywords, questions, paths, exclusions, or source roots;
- infer topic scope from filenames or prior chat memory;
- broaden the corpus;
- select the target KB folder;
- convert a warning into a pass;
- run the next stage;
- claim semantic relevance, authority, freshness, or supersession from deterministic signals;
- use recommendations as confirmation.

Every recommendation must include the exact deterministic fact that triggered it. The operator accepts or rejects each proposed change explicitly.

## 5. Start flow

| Step | Operator-visible action | Deterministic action | Persistent artifact |
|---:|---|---|---|
| 0.1 | Run `apexkb start`. | Render the fixed Q&A and exact JSON template verbatim. | none |
| 0.2 | Fill and save the JSON configuration. | Parse the named file only. | draft configuration |
| 0.3 | Review field-specific errors, if any. | Validate schema and permitted values. | validation result |
| 0.4 | Wait for the preflight result. | Inspect repositories, paths, overlap, capabilities, exclusions, formats, and lightweight scope statistics without source intake or KB writes. | derived preflight report |
| 0.5A | Deterministic mode: review facts and warnings. | Render factual compact report. | derived readback |
| 0.5B | AI mode: review facts plus bounded recommendations. | AI reads only the configuration and deterministic preflight report. | derived recommendation section |
| 0.6 | Revise the same config or confirm it. | Revalidate on every revision. | same configuration, higher revision if changed |
| 0.7 | Confirm. | Normalize and hash the confirmed configuration; initialize state with config reference/hash. | locked configuration reference + run state |
| 0.8 | Receive Setup complete / blocked. | Create minimum scaffold only after confirmation and emit exact Phase 1 handoff. | scaffold + stage result |

## 6. Q&A content requirements

The fixed Q&A must explain and collect:

1. source repository and source roots;
2. target repository and KB root;
3. KB slug, title, and one-sentence identity;
4. operator-defined topic list;
5. per-topic strong phrases, aliases, supporting terms, ambiguous terms, and negative terms;
6. per-topic target questions as a bullet list or structured JSON list;
7. explicit exclusions with reasons;
8. source storage mode;
9. deterministic corpus-intelligence profile;
10. Git date handling;
11. graph-signal depth;
12. non-text handling;
13. output tier;
14. deterministic-only versus optional AI recommendations;
15. preflight detail level;
16. special constraints.

The operator should not be asked to choose an execution route such as `terminal_backed` or `connector_only`. The preflight detects whether the required deterministic runtime is available. If it is not, Setup fails with an exact blocker.

## 7. High-value, low-cost preflight facts

The compact preflight should include, when available without semantic analysis:

- repository and source-root existence;
- target-root existence and source/output overlap;
- read/write capability for required locations;
- deterministic runtime and required dependency availability;
- Git repository identity and selected ref;
- dirty/untracked status as an informational safety fact;
- total files and total bytes in scope;
- file count and bytes by extension;
- top-level folder counts;
- largest files and unusually large-file warnings;
- hidden-file, symlink, generated-folder, cache, dependency, and nested-output candidates;
- excluded file/folder counts by rule;
- unreadable files;
- unsupported or extraction-limited formats;
- estimated extraction coverage by file count and bytes;
- lightweight path/filename phrase-hit counts for each operator topic;
- questions with no path/filename evidence, clearly labeled as a weak early signal rather than semantic failure;
- expected deterministic outputs for the selected profile;
- expected semantic/final outputs for the selected output tier.

Exact duplicate hashing, full-body topic mapping, version-family detection, and semantic relevance are not required in Setup preflight unless they are already available at negligible incremental cost. They belong primarily to Phase 1 Deterministic Corpus Intelligence.

## 8. Keep, change, add, defer, reject

### Keep

- `apex_kb_control.py` as the single lifecycle controller;
- durable run state;
- reason-coded blockers;
- configuration drift detection;
- exact next-stage derivation;
- recovery/reconciliation logic;
- deterministic preflight and later corpus scripts;
- source-preserving and fail-closed behavior.

### Change

- replace the public multi-command setup with `apexkb start`;
- remove the initial operator question about Python/terminal capability;
- start with the fixed Q&A, not an AI interview;
- move setup preflight before scaffold and consequential writes;
- make AI recommendations optional and bounded;
- support an operator-authored topic list without AI topic generation;
- render configuration errors and preflight facts in plain language.

### Add

- fixed Start Q&A and option guide;
- one exact JSON configuration template;
- `preflight_assistance` option;
- high-value lightweight preflight statistics;
- explicit public/internal command mapping;
- tests proving the fixed message renders verbatim and AI cannot mutate configuration.

### Defer

- final `continue`, `status`, and `repair` UX;
- existing-KB update lifecycle;
- post-Phase-1 topic discovery workflow;
- final decision on whether topics remain embedded or move to a separate canonical topic registry;
- final decision on retaining a duplicated `run-manifest`;
- full graph/process extraction behavior beyond the setup option definition.

### Reject

- AI-led intake as the default;
- silent AI defaults;
- AI-generated or AI-expanded topic scope;
- an operator capability questionnaire;
- multiple full configuration copies without unique consumers;
- exposing low-level lifecycle commands as the normal operator interface;
- fake numerical estimates of semantic value before semantic analysis.

## 9. Open implementation questions

| ID | Question | Why unresolved |
|---|---|---|
| P0-Q01 | Should the command be exactly `apexkb start`, `apex-kb start`, or both with one canonical binary? | Naming and packaging need live CLI integration review. |
| P0-Q02 | Should multiple topics be embedded in the run config or referenced from `topic-registry.json`? | Must avoid duplication while preserving direct operator control. |
| P0-Q03 | Is a separate `run-manifest.json` needed, or is confirmed config revision + hash + run state sufficient? | Requires producer/consumer trace. |
| P0-Q04 | What is the exact Leela KB target repository folder? | Operator confirmation still required. |
| P0-Q05 | Which preflight facts are available without recursively hashing or parsing the full corpus? | Must be measured in the canary implementation. |
| P0-Q06 | Should deterministic-only be the hard default with AI recommendations opt-in per run? | Current operator direction says yes; confirm during Q&A review. |

## 10. Immediate next work

1. Review the Start Q&A draft beside this register.
2. Decide each field and option in operator language.
3. Reconcile the accepted Q&A fields with the live config/state schemas.
4. Produce a minimal implementation patch for `start` only.
5. Test Start against the Leela repositories without source mutation.
6. Feed actual preflight output back into this register before designing `continue` or `repair`.
