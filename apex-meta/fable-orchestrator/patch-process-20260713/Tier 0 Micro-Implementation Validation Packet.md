# Tier 0 Micro-Implementation Validation Packet

## 1. Repository and evidence baseline

**Repository access:** passed.

```okf
repository_baseline:
  repository: "leela-spec/apexai-os-meta"
  branch: "main"
  current_head: "7ab08a57d5b3ad7f2ba67793ba1ec48b28b8ef68"
  current_head_message: "docs: preserve Apex KB harmonization evidence"
  access_mode: "github_connector_read_only"
  repository_mutations: []
```

The authoritative Tier 0 plan was read in full. It proposes:

- **0a:** compact the project activation file and relocate detailed weekly-loop material;
    
- **0b:** shorten skill descriptions;
    
- **0c:** shorten agent descriptions;
    
- **0d:** add a compaction-protection instruction.
    

The two prior validation artifacts were reused:

- `tier0-kb-validation-and-extension-packet.okf.md`;
    
- `tier0-kb-validation-deterministic-addendum.okf.md`.
    

The addendum already limited safe patch scope to activation-file case correction and bounded compaction, while excluding mass description rewrites and unresolved recovery changes.

The current HEAD is three commits beyond the deterministic-addendum baseline. Connector comparison found that those commits added evidence, reports, and prompt artifacts only. None of these live Tier 0 targets changed:

```okf
unchanged_since_prior_addendum:
  - ".claude/Claude.md"
  - ".claude/skills/weekly-orchestrator/SKILL.md"
  - ".claude/skills/*/SKILL.md"
  - ".claude/agents/*.md"
```

The live Claude orchestration KB index was also inspected. It currently contains a stray `test` line, a generated timestamp of July 11, 2026, and numerous duplicate or review-pending pages. It remains supporting design evidence rather than current platform authority.

---

## 2. Executive verdict

```okf
executive_verdict:
  status: "validated_with_qualifications"
  repository_ref: "7ab08a57d5b3ad7f2ba67793ba1ec48b28b8ef68"

  safe_to_plan: true
  safe_to_create_patch_plan: true
  safe_to_create_patch_files: false
  safe_to_apply: false

  recommended_first_patch_scope:
    option: "Minimal first test"
    operations:
      - "Case-correct .claude/Claude.md to .claude/CLAUDE.md."
      - "Prove the corrected instruction file is loaded."
      - "Compact only the corrected activation file by subtraction and canonical pointers."
      - "Remove its stale duplicate weekly-loop material."
    exact_live_target:
      - ".claude/Claude.md"
      - ".claude/CLAUDE.md after rename"

  excluded_from_first_patch:
    - ".claude/skills/weekly-orchestrator/SKILL.md"
    - ".claude/skills/apex-kb/SKILL.md"
    - ".claude/skills/deterministic-markdown-patcher/SKILL.md"
    - "all other skill descriptions"
    - "all agent descriptions"
    - "semantic KB pages and generated KB artifacts"
    - "glossary canonicalization"

  highest_value_change: >
    Establish a platform-recognized project instruction file and remove the stale
    weekly-loop copy that currently competes with weekly-orchestrator.

  highest_risk: >
    Deleting activation-file rules without proving that every still-required rule
    either remains in the activation seed or has exactly one resolvable canonical owner.

  unresolved_blockers:
    - "The case-correct file has not been proven loaded by Claude Code."
    - "No compacted candidate has passed the no-loss checks defined below."
    - "No weekly-loop smoke fixture has run with the compact activation seed."
    - "No generated patch artifact has passed git apply --check."
```

**Decision:** Tier 0a is validated. Tier 0b and 0c are narrowed to measured exceptions and excluded from the first patch. Tier 0d requires changed wording and placement.

---

## 3. Conflicts between original Tier 0 and current evidence

### 3.1 Activation filename

The repository contains `.claude/Claude.md`. It does not contain `.claude/CLAUDE.md` or root `CLAUDE.md`.

Current Claude Code documentation recognizes project instructions at:

- `./CLAUDE.md`;
    
- `./.claude/CLAUDE.md`.
    

```okf
conflict_ACTIVATION_CASE:
  original_assumption: "The current activation file is active and always loaded."
  current_evidence: ".claude/Claude.md has noncanonical case."
  verdict: "qualified"
  correction: "Perform a case-correct Git rename before relying on its contents."
```

### 3.2 The 400–500-token target

Current Claude Code guidance says to keep project instructions concise and targets fewer than 200 lines. It does not prescribe 400–500 tokens. Multi-step or task-specific procedures should move to skills or scoped rules.

```okf
conflict_ACTIVATION_NUMERIC_TARGET:
  original_target: "approximately 400-500 tokens"
  platform_status: "not an official correctness threshold"
  retained_use: "measurement objective"
  governing_test: "smallest complete seed that preserves activation-critical behavior"
```

### 3.3 The 75-word description rule

Claude Code currently applies:

- a configurable **1,536-character per-entry listing cap** for combined `description` and `when_to_use`;
    
- a global skill-listing budget equal by default to 1% of the model context window;
    
- `disable-model-invocation: true` and `skillOverrides: name-only` as alternative context controls.
    

It does not impose a 75-word platform limit.

```okf
conflict_DESCRIPTION_CAP:
  original_rule: "maximum 75 words"
  current_platform_rule: "1536-character listing cap plus global listing budget"
  verdict: "75 words remains a local heuristic, not a bulk-mutation mandate"
  implication: "Shorten only descriptions with demonstrated redundancy or routing cost."
```

### 3.4 Skill descriptions do not all need to begin with one exact phrase

“Use this skill when” is a useful project convention, but current Claude Code routes by description meaning, natural request terms, and invocation configuration. The key use case should appear first.

The convention may be retained, but an otherwise effective description is not defective merely because its first four words differ.

### 3.5 Agent system markers

The plan proposes adding `Fable` or `Weekly loop` to every agent description. Current agent descriptions already encode their actual system, delegation conditions, and boundaries. Adding `Fable` to the seven final APEX orchestration agents would reintroduce an initiative name that the live runtime no longer uses as its primary identity.

Claude delegates based directly on the agent description and current context, making accurate work boundaries more important than a uniform marker.

```okf
conflict_AGENT_MARKER:
  proposed_change: "Add Fable or Weekly loop to every agent description."
  verdict: "reject blanket mutation"
  reason: >
    Weekly agents already identify the Apex weekly loop. Final orchestration agents
    identify APEX accountabilities and their invocation mode. Fable would be stale
    or misleading on several files.
```

### 3.6 Compaction note

Project-root `CLAUDE.md` is reread and reinjected automatically after `/compact`.

The exact original note—

> “on resume/compaction, re-read this contract before gate decisions”

—would therefore be incomplete and incorrectly focused if it merely tells Claude to reload the activation file.

The required recovery behavior is instead:

1. re-invoke `weekly-orchestrator`;
    
2. execute its existing **Locate the loop** procedure;
    
3. rediscover the latest durable packets and pending gate before any gate decision.
    

---

## 4. Exact target inventory

### 4.1 Activation surfaces

```okf
activation_inventory:
  - path: ".claude/Claude.md"
    exists: true
    status: "mixed_case_unrecognized_candidate"
    sha: "feb9d511d9b6598ca148a8f202b3518d88481864"

  - path: ".claude/CLAUDE.md"
    exists: false
    status: "required_target"

  - path: "CLAUDE.md"
    exists: false
    status: "not_selected"
```

### 4.2 Canonical owners

```okf
canonical_owner_inventory:
  weekly_runtime:
    path: ".claude/skills/weekly-orchestrator/SKILL.md"
    owns:
      - "weekly stage routing"
      - "G1-G5 handling"
      - "packet-envelope validation"
      - "consequential review dispatch"
      - "loop-position discovery"
      - "confirmed mutation routing through apex-session"

  orchestration_law:
    path: "apex-meta/orchestration/00-START-HERE.md"
    owns:
      - "five global invariants"
      - "system topology"
      - "mutation backbone"
      - "independent-review requirement"
      - "canonical system read order"

  cross_system_navigation:
    path: "apex-meta/ORCHESTRATION-SYSTEMS-INDEX.md"
    owns:
      - "repo-wide orchestration and KB navigation"
      - "live versus historical system classification"

  individual_skill_routing:
    path_pattern: ".claude/skills/*/SKILL.md"
    owns:
      - "skill-specific trigger"
      - "accepted inputs"
      - "output contract"
      - "skill boundary"

  individual_agent_routing:
    path_pattern: ".claude/agents/*.md"
    owns:
      - "delegation condition"
      - "agent-specific tools"
      - "preloaded skills"
      - "non-delegation boundary"
```

The weekly skill already contains the corrected G5 `status_merge` stage and routes confirmed changes through `apex-session`. Its procedure already reconstructs loop position from Session/Sync context and the latest weekly artifacts.

The final orchestration start page separately owns the durable-state, mutation, gate, review, and candidate-state invariants.

### 4.3 In-scope skills for description evaluation

The exact Tier 0 evaluation set is the plan’s named offenders plus the weekly owner:

```okf
tier0_skill_description_scope:
  - ".claude/skills/apex-kb/SKILL.md"
  - ".claude/skills/deterministic-markdown-patcher/SKILL.md"
  - ".claude/skills/deterministic-markdown-patcher2/SKILL.md"
  - ".claude/skills/AIRouting/SKILL.md"
  - ".claude/skills/apex-plan/SKILL.md"
  - ".claude/skills/apex-session/SKILL.md"
  - ".claude/skills/apex-sync/SKILL.md"
  - ".claude/skills/source-authority-and-verdict-packet/SKILL.md"
  - ".claude/skills/weekly-orchestrator/SKILL.md"
```

Other skills are not automatically patch candidates merely because they exist.

### 4.4 Agent set

```okf
tier0_agent_set:
  final_apex_orchestration:
    - "alfred"
    - "meta-strategy"
    - "meta-ops"
    - "meta-detective"
    - "knowledge-bank"
    - "informatics-design"
    - "prompts-workflows"

  weekly_loop:
    - "apex-precap-week"
    - "apex-precap-next-day"
    - "apex-evidence-normalize"
    - "apex-flow-recap"
    - "apex-status-merge"
    - "apex-project-status"
    - "apex-review-validity"
    - "apex-review-alignment"

  project_engine_optional_workers:
    - "apex-plan-ops"
    - "apex-sync-ops"

  total: 17
```

---

## 5. Activation-file path and load-proof decision

```okf
activation_path_decision:
  observed_path: ".claude/Claude.md"
  correct_target_path: ".claude/CLAUDE.md"

  required_operation:
    operation_type: "git_case_rename"
    windows_safe_shape:
      - "git mv .claude/Claude.md .claude/CLAUDE.rename-tmp"
      - "git mv .claude/CLAUDE.rename-tmp .claude/CLAUDE.md"
    content_change_during_rename: false

  load_proof:
    required_session: "fresh Claude Code session launched from repository root"
    primary_method:
      command: "/memory"
      expected_observation: ".claude/CLAUDE.md appears in loaded instruction files"
    stronger_optional_method:
      mechanism: "InstructionsLoaded hook"
      expected_observation: "event logs exact .claude/CLAUDE.md path and load reason"
    after_compact_check:
      - "Run /compact."
      - "Run /memory again."
      - "Confirm .claude/CLAUDE.md remains loaded."

  risk_if_compaction_precedes_load_proof: >
    Claude Code cannot reinject a project instruction file it never recognized.
    A successful /compact therefore does not prove that the mixed-case file was loaded.
```

`/memory` lists the instruction files loaded in the current session; `InstructionsLoaded` can log exactly which files loaded and why.

Git’s supported file-renaming mechanism is `git mv`; it updates the index after a successful rename.

---

## 6. Fact-level relocation and no-loss matrix

The current activation candidate contains the full loop, eleven-skill inventory, agent inventory, project-engine boundary, artifact paths, startup procedure, exclusions, and constraints.

|Fact ID|Source block|Atomic fact or rule|Activation-critical|Canonical destination|Coverage|Action|
|---|---|---|--:|---|---|---|
|F001|`identity`|Apex is a Claude-native orchestration system; operator executes; evidence becomes durable state.|Yes|Activation seed|Complete|Keep, update operator name only through separate decision|
|F002|`core_loop`|Weekly loop starts with PreCapWeek/G1.|No|`weekly-orchestrator` Contract|Complete|Remove and point|
|F003|`core_loop`|Daily planning is PreCapNextDay/G2.|No|`weekly-orchestrator` Contract|Complete|Remove and point|
|F004|`core_loop`|Operator execution/evidence intake occupies the G3 boundary.|No|`weekly-orchestrator` Contract|Complete|Remove and point|
|F005|`core_loop`|FlowRecap is routed through G4.|No|`weekly-orchestrator` Contract|Complete|Remove and point|
|F006|`core_loop`|Current G5 owner is status merge, followed by `apex-session` for confirmed mutation.|No|`weekly-orchestrator` Contract and Procedure|Complete|Remove stale copy and point|
|F007|`core_loop`|APSU directly owns G5 and emits `updated_all_project_status_packet`.|No|None|Conflicting/obsolete|Delete; do not relocate|
|F008|`skills`|Weekly stage trigger, path, input/output, and gate details.|No|Individual SKILL files plus weekly stage routing|Complete|Remove table and point|
|F009|`skills`|Standalone skill trigger and output details.|No|Individual SKILL files|Complete|Remove table and point|
|F010|`skills`|“All 11 skills are present as of last check.”|No|Runtime discovery|Obsolete/volatile|Delete; validate with `/doctor` or `/skills`|
|F011|`agents`|Stage work runs in context-isolated subagents with preloaded skills.|No|Agent frontmatter and weekly skill|Complete|Remove and point|
|F012|`agents`|Main thread dispatches stages and holds gates.|Yes, compressed|Weekly skill|Complete|Keep one-sentence boundary plus pointer|
|F013|`agents`|Main thread does not perform stage content work inline.|Yes|Weekly skill Rule and boundaries|Complete|Keep compressed pointer rule|
|F014|`agents`|Consequential packets receive independent validity and alignment review.|Yes|Final orchestration invariant 4 and review wiring|Complete|Keep invariant plus pointer|
|F015|`project_management_engine`|Plan proposes, Sync computes, Session applies confirmed mutations.|Yes|Final orchestration map|Complete|Keep compressed mutation-backbone invariant|
|F016|`project_management_engine`|Weekly orchestration consumes project-engine outputs but does not mutate project state.|Yes|Weekly skill boundaries and final system map|Complete|Keep compressed|
|F017|`artifact_paths`|Read confirmed Session and relevant Sync context before weekly planning.|No|Weekly Procedure step 1|Complete|Remove and point|
|F018|`artifact_paths`|Weekly plans are under `artifacts/weekly-plans/`.|No|Weekly Procedure step 1|Complete|Remove|
|F019|`artifact_paths`|Next-day plans are under `artifacts/next-day-plans/`.|No|Weekly Procedure step 1|Complete|Remove|
|F020|`artifact_paths`|Flow packets are under `artifacts/flow-packets/`.|No|Weekly Procedure step 1|Complete|Remove|
|F021|`artifact_paths`|Flow recaps are under `artifacts/flow-recap-packets/`.|No|Weekly Procedure step 1|Complete|Remove|
|F022|`session_startup`|Do not execute until the operator invokes a capability.|Yes|Activation seed|Complete|Keep|
|F023|`session_startup`|Recheck a hand-maintained skill-status table.|No|Claude `/skills`, `/doctor`, runtime errors|Obsolete|Delete|
|F024|`exclude_from_context`|Do not read backup, recovery, verification, report, or source-knowledge trees by default.|Yes|Activation seed|Complete|Keep, compress as glob set|
|F025|`constraints`|Explicit autonomous-run instruction can waive intermediate confirmations, not unsafe-write or missing-source stops.|Yes|Activation seed|Complete|Keep|
|F026|`constraints`|Read only active skill and task-relevant state.|Yes|Activation seed|Complete|Keep|
|F027|`constraints`|Never write to `source-knowledge/**`.|Yes|Activation seed|Complete|Keep|
|F028|`constraints`|Never auto-trigger skills or create schedulers/calendar tasks.|Yes|Activation seed|Complete|Keep|
|F029|`constraints`|Never silently overwrite state; append or expose conflicts.|Yes|Activation seed|Complete|Keep|
|F030|`constraints`|Multi-file output writes require confirmation unless a valid autonomous override applies.|Yes|Activation seed|Complete|Keep with precedence made explicit|
|F031|`constraints`|Hard-required missing inputs halt; degraded-mode inputs are marked low confidence.|Yes|Activation seed|Complete|Keep|
|F032|`constraints`|Completion reporting should be brief.|Low|Activation seed|Complete|Retain only if operator still wants this global style rule|
|F033|`agents`|Terms are defined by `apex-meta/GLOSSARY.md`.|Potentially|Two competing glossary files|Conflicting|Retain existing pointer temporarily; do not canonicalize in Tier 0|

### Hard-gate result

```okf
no_loss_gate:
  removable_blocks_approved:
    - "core_loop"
    - "skills table"
    - "agents table"
    - "artifact_paths"
    - "session_startup detail"

  conditions:
    - "F001, F012-F016, and F022-F032 remain in compact form."
    - "The compact file uses literal path pointers."
    - "F007, F010, and F023 are deleted as stale or volatile rather than relocated."
    - "F033 is not silently resolved during Tier 0."

  unowned_required_facts: []
  unresolved_semantic_conflict:
    - "Two files currently claim glossary authority."
```

---

## 7. Minimum activation seed

### Keep

```okf
activation_seed_keep:
  - "Project identity and mission."
  - "State lives in files; accepted truth is not reconstructed from chat."
  - "One confirmed mutation path through apex-session."
  - "Consequential work requires independent review and operator confirmation."
  - "Candidate material never auto-promotes."
  - "Never auto-trigger skills."
  - "Never read or write excluded and source-knowledge paths unless explicitly authorized."
  - "Autonomous-run override precedence and irreducible stop conditions."
  - "Hard-required versus degraded missing-input behavior."
  - "Pointers to weekly orchestration, final orchestration law, cross-system map, and glossary."
  - "Apex-specific post-compaction recovery pointer."
```

### Remove and point

```okf
activation_seed_remove_and_point:
  core_loop: ".claude/skills/weekly-orchestrator/SKILL.md"
  weekly_routing_and_gates: ".claude/skills/weekly-orchestrator/SKILL.md"
  handoff_and_review_details:
    - ".claude/skills/weekly-orchestrator/references/handoff-schema.md"
    - ".claude/skills/weekly-orchestrator/references/review-wiring.md"
  system_law: "apex-meta/orchestration/00-START-HERE.md"
  cross_system_inventory: "apex-meta/ORCHESTRATION-SYSTEMS-INDEX.md"
  skill_details: ".claude/skills/<skill>/SKILL.md"
  agent_details: ".claude/agents/<agent>.md"
```

### Reject removal

```okf
activation_seed_reject_removal:
  - "Independent-review invariant."
  - "Single durable mutation path."
  - "Candidate-versus-confirmed state boundary."
  - "No automatic skill execution."
  - "Excluded-path and source-knowledge write prohibition."
  - "Autonomous override limits."
  - "Hard-stop behavior for required missing evidence or unsafe writes."
```

### Proposed pointer language

```text
Weekly loop: invoke `weekly-orchestrator`; its canonical contract is
`.claude/skills/weekly-orchestrator/SKILL.md`.

Final orchestration law and invariants:
`apex-meta/orchestration/00-START-HERE.md`.

Repository-wide orchestration and KB map:
`apex-meta/ORCHESTRATION-SYSTEMS-INDEX.md`.

After resume or compaction during a weekly run, invoke `weekly-orchestrator`
and execute its “Locate the loop” step before making any gate decision.
```

The pointers must remain literal code-formatted paths. Do not use `@path` imports: imported files are expanded into startup context and would defeat the intended context reduction.

### Estimated footprint

```okf
activation_size_estimate:
  before:
    observed_lines: 81
    prior_plan_token_estimate: "~1600"
    estimated_characters: "approximately 6000-6500"
    estimated_words: "approximately 800-950"
    confidence: "medium"
    note: "Exact wc values remain a later execution check."

  after:
    target_lines: "approximately 25-40"
    estimated_characters: "approximately 1600-2200"
    estimated_words: "approximately 220-320"
    approximate_tokens: "approximately 400-550"
    confidence: "medium"

  token_method: >
    Use exact UTF-8 byte and word counts, then disclose the tokenizer used.
    Until a tokenizer is run, characters divided by four is only a planning estimate.

  correctness_rule: >
    The after-size is accepted only if the no-loss and routing fixtures pass.
    No numeric target can justify removing a load-bearing invariant.
```

---

## 8. Skill description findings

Current word counts were calculated from the complete frontmatter descriptions using a deterministic word-token regex. Character counts include spaces and punctuation.

Claude Code uses descriptions to decide whether to invoke skills; default skills expose their descriptions continuously, while manual-only skills can remove descriptions from context with `disable-model-invocation: true`.

### Inventory

|Skill|Words|Chars|Invocation mode|Verdict|
|---|--:|--:|---|---|
|`apex-kb`|110|811|user + model|`defer_until_trigger_eval`|
|`deterministic-markdown-patcher`|113|770|user + model|`defer_until_trigger_eval`|
|`deterministic-markdown-patcher2`|48|396|user + model|`retain_unchanged`|
|`ai-routing-and-usage-tracking`|51|450|user + model|`retain_unchanged`|
|`apex-plan`|66|488|user + model|`retain_unchanged`|
|`apex-session`|57|401|user + model|`retain_unchanged`|
|`apex-sync`|54|426|user + model|`retain_unchanged`|
|`source-authority-and-verdict-packet`|60|469|user + model|`retain_unchanged`|
|`weekly-orchestrator`|76|483|user + model|`retain_unchanged`|

### Records

```okf
skill_description_findings:
  - path: ".claude/skills/apex-kb/SKILL.md"
    skill_name: "apex-kb"
    current_word_count: 110
    invocation_mode: "user_and_model_invocable"
    current_trigger_terms:
      - "scaffold"
      - "intake sources"
      - "ingest"
      - "compile wiki"
      - "query"
      - "retrieve"
      - "lint"
      - "audit"
      - "maintain Apex knowledge base"
    current_boundary: "KB root only; no plan/session/sync mutation or external contact"
    violation: >
      Materially longer than needed because the description reproduces the
      complete adaptive-page contract rather than only routing metadata.
    proposed_description: >
      Use this skill when the operator asks to scaffold, ingest, compile, query,
      retrieve, lint, audit, or maintain an Apex knowledge base under
      apex-meta/kb/<kb-slug>/. Accepts a KB root, source set, or KB operation.
      Produces source-preserving ingest, wiki, index, retrieval, query, lint, and
      audit artifacts. Does not mutate project/session/sync state, contact external
      services, or write outside the KB root.
    proposed_word_count: 57
    should_trigger_examples:
      - "Run a lint audit on this Apex KB."
      - "Ingest these sources into the KB and stop after Phase 1."
    should_not_trigger_examples:
      - "Plan my next project tasks."
      - "Rebuild the project task registry."
    regression_risk: "medium"
    recommendation: "defer_until_trigger_eval"

  - path: ".claude/skills/deterministic-markdown-patcher/SKILL.md"
    skill_name: "deterministic-markdown-patcher"
    current_word_count: 113
    invocation_mode: "user_and_model_invocable"
    current_trigger_terms:
      - "modify Markdown"
      - "skill files"
      - "frontmatter"
      - "patch packs"
      - "repository documentation"
      - "deterministic"
    current_boundary: "no hand-authored diff or default full-file rewrite"
    violation: >
      The description narrates executor internals and supported suboperations that
      belong in the body or references.
    proposed_description: >
      Use this skill when the operator asks to plan, execute, validate, or report
      a deterministic Markdown, frontmatter, skill-file, or repository-document
      change. Accepts a change request, target files, patch intent, or patch plan.
      Produces executor-validated edits, fixtures, patch artifacts, or reports.
      Does not hand-author unified diffs or perform full-file rewrites when a
      bounded executor operation is available.
    proposed_word_count: 56
    should_trigger_examples:
      - "Replace this Markdown section deterministically."
      - "Validate and execute this patch-intent file."
    should_not_trigger_examples:
      - "Rewrite this paragraph to sound friendlier."
      - "Review a pull request."
    regression_risk: "medium"
    recommendation: "defer_until_trigger_eval"

  - path: ".claude/skills/deterministic-markdown-patcher2/SKILL.md"
    skill_name: "deterministic-markdown-patcher2"
    current_word_count: 48
    invocation_mode: "user_and_model_invocable"
    violation: null
    regression_risk: "low if unchanged"
    recommendation: "retain_unchanged"

  - path: ".claude/skills/AIRouting/SKILL.md"
    skill_name: "ai-routing-and-usage-tracking"
    current_word_count: 51
    invocation_mode: "user_and_model_invocable"
    violation: null
    regression_risk: "low if unchanged"
    recommendation: "retain_unchanged"

  - path: ".claude/skills/apex-plan/SKILL.md"
    skill_name: "apex-plan"
    current_word_count: 66
    invocation_mode: "user_and_model_invocable"
    violation: null
    regression_risk: "high if shortened carelessly because Plan/Sync/Session separation is load-bearing"
    recommendation: "retain_unchanged"

  - path: ".claude/skills/apex-session/SKILL.md"
    skill_name: "apex-session"
    current_word_count: 57
    invocation_mode: "user_and_model_invocable"
    violation: null
    regression_risk: "high if mutation boundaries are weakened"
    recommendation: "retain_unchanged"

  - path: ".claude/skills/apex-sync/SKILL.md"
    skill_name: "apex-sync"
    current_word_count: 54
    invocation_mode: "user_and_model_invocable"
    violation: null
    regression_risk: "high if deterministic read-side boundary is weakened"
    recommendation: "retain_unchanged"

  - path: ".claude/skills/source-authority-and-verdict-packet/SKILL.md"
    skill_name: "source-authority-and-verdict-packet"
    current_word_count: 60
    invocation_mode: "user_and_model_invocable"
    violation: null
    regression_risk: "high if validator/executor separation is weakened"
    recommendation: "retain_unchanged"

  - path: ".claude/skills/weekly-orchestrator/SKILL.md"
    skill_name: "weekly-orchestrator"
    current_word_count: 76
    invocation_mode: "user_and_model_invocable"
    violation: >
      One word over the local heuristic but materially below the platform cap,
      routing-specific, and not redundantly verbose.
    regression_risk: "high because it is the main loop-routing description"
    recommendation: "retain_unchanged"
```

**Decision:** only two descriptions have a credible compaction candidate. Neither belongs in the first patch because current Claude guidance recommends validating both trigger selection and output behavior in fresh sessions.

---

## 9. Agent description findings

Claude automatically delegates based on the request, current context, and each agent’s `description`. Skills listed in agent frontmatter are injected in full at startup.

All 17 descriptions already communicate bounded delegation. None should be changed in Tier 0.

```okf
agent_description_findings:
  - {path: ".claude/agents/alfred.md", agent_name: "alfred", current_word_count: 60,
     intended_delegation: "operator intake and gate presentation as a main-thread accountability",
     non_delegation_boundary: "do not spawn; does not execute project work",
     overlap_with: ["meta-ops at operator gates"],
     violation: null, proposed_description: null, proposed_word_count: null,
     should_delegate_examples: ["Adopt Alfred for presenting the operator gate."],
     should_not_delegate_examples: ["Spawn Alfred to edit a project file."],
     regression_risk: "critical", recommendation: "retain_unchanged"}

  - {path: ".claude/agents/meta-ops.md", agent_name: "meta-ops", current_word_count: 73,
     intended_delegation: "main-thread meso workflow, routing, integration, and mutation-backbone coordination",
     non_delegation_boundary: "do not spawn; no self-validation or silent mutation",
     overlap_with: ["weekly-orchestrator", "apex-plan-ops", "apex-sync-ops"],
     violation: null, proposed_description: null, proposed_word_count: null,
     should_delegate_examples: ["Adopt Meta Ops to run the file-backed orchestration workflow."],
     should_not_delegate_examples: ["Spawn Meta Ops as an isolated worker."],
     regression_risk: "critical", recommendation: "retain_unchanged"}

  - {path: ".claude/agents/meta-strategy.md", agent_name: "meta-strategy", current_word_count: 32,
     intended_delegation: "macro framing and strategic-alignment analysis",
     non_delegation_boundary: "read-only; no implementation or self-validation",
     overlap_with: ["apex-review-alignment"],
     violation: null, proposed_description: null, proposed_word_count: null,
     should_delegate_examples: ["Frame strategic options for phase 2."],
     should_not_delegate_examples: ["Apply the selected implementation."],
     regression_risk: "low", recommendation: "retain_unchanged"}

  - {path: ".claude/agents/meta-detective.md", agent_name: "meta-detective", current_word_count: 33,
     intended_delegation: "fresh isolated independent review under one named lens",
     non_delegation_boundary: "never implements or orchestrates",
     overlap_with: ["apex-review-validity", "apex-review-alignment"],
     violation: null, proposed_description: null, proposed_word_count: null,
     should_delegate_examples: ["Review this artifact for validity only."],
     should_not_delegate_examples: ["Repair the defect you found."],
     regression_risk: "high", recommendation: "retain_unchanged"}

  - {path: ".claude/agents/knowledge-bank.md", agent_name: "knowledge-bank", current_word_count: 33,
     intended_delegation: "one bounded KB custody, placement, status, or retrieval objective",
     non_delegation_boundary: "returns an artifact and stops; does not inherit orchestration",
     overlap_with: ["apex-kb skill"],
     violation: null, proposed_description: null, proposed_word_count: null,
     should_delegate_examples: ["Determine the canonical KB placement for this source."],
     should_not_delegate_examples: ["Run the entire project workflow."],
     regression_risk: "low", recommendation: "retain_unchanged"}

  - {path: ".claude/agents/informatics-design.md", agent_name: "informatics-design", current_word_count: 33,
     intended_delegation: "bounded taxonomy, naming, structure, or consistency work",
     non_delegation_boundary: "returns an artifact and stops",
     overlap_with: ["prompts-workflows for artifact templates"],
     violation: null, proposed_description: null, proposed_word_count: null,
     should_delegate_examples: ["Audit terminology consistency."],
     should_not_delegate_examples: ["Choose the project strategy."],
     regression_risk: "low", recommendation: "retain_unchanged"}

  - {path: ".claude/agents/prompts-workflows.md", agent_name: "prompts-workflows", current_word_count: 37,
     intended_delegation: "bounded method, workflow, prompt, or handoff-template creation",
     non_delegation_boundary: "returns an artifact and does not inherit orchestration",
     overlap_with: ["informatics-design"],
     violation: null, proposed_description: null, proposed_word_count: null,
     should_delegate_examples: ["Draft a reusable prompt pack."],
     should_not_delegate_examples: ["Approve a durable mutation."],
     regression_risk: "low", recommendation: "retain_unchanged"}

  - {path: ".claude/agents/apex-precap-week.md", agent_name: "apex-precap-week", current_word_count: 50,
     intended_delegation: "weekly G1 planning",
     non_delegation_boundary: "no detailed day planning, execution, or durable writes",
     overlap_with: ["meta-strategy"],
     violation: null, proposed_description: null, proposed_word_count: null,
     should_delegate_examples: ["Create the weekly plan packet."],
     should_not_delegate_examples: ["Create tomorrow's detailed flow packets."],
     regression_risk: "medium", recommendation: "retain_unchanged"}

  - {path: ".claude/agents/apex-precap-next-day.md", agent_name: "apex-precap-next-day", current_word_count: 50,
     intended_delegation: "daily G2 planning and flow/prompt packets",
     non_delegation_boundary: "no execution, FlowRecap, or status merge",
     overlap_with: ["apex-precap-week"],
     violation: null, proposed_description: null, proposed_word_count: null,
     should_delegate_examples: ["Create tomorrow's next-day plan."],
     should_not_delegate_examples: ["Merge yesterday's project status."],
     regression_risk: "medium", recommendation: "retain_unchanged"}

  - {path: ".claude/agents/apex-evidence-normalize.md", agent_name: "apex-evidence-normalize", current_word_count: 48,
     intended_delegation: "normalize raw post-execution evidence",
     non_delegation_boundary: "no project interpretation or recap conclusion",
     overlap_with: ["apex-flow-recap"],
     violation: null, proposed_description: null, proposed_word_count: null,
     should_delegate_examples: ["Normalize these execution notes."],
     should_not_delegate_examples: ["Determine the project's status delta."],
     regression_risk: "medium", recommendation: "retain_unchanged"}

  - {path: ".claude/agents/apex-flow-recap.md", agent_name: "apex-flow-recap", current_word_count: 51,
     intended_delegation: "G4 recap and candidate deltas",
     non_delegation_boundary: "candidate-only; no accepted state or durable writes",
     overlap_with: ["apex-evidence-normalize", "apex-status-merge"],
     violation: null, proposed_description: null, proposed_word_count: null,
     should_delegate_examples: ["Produce a recap from the normalized evidence."],
     should_not_delegate_examples: ["Apply the status change."],
     regression_risk: "high", recommendation: "retain_unchanged"}

  - {path: ".claude/agents/apex-status-merge.md", agent_name: "apex-status-merge", current_word_count: 46,
     intended_delegation: "G5 proposal-only status reconciliation",
     non_delegation_boundary: "never mutates durable state",
     overlap_with: ["apex-flow-recap", "apex-session"],
     violation: null, proposed_description: null, proposed_word_count: null,
     should_delegate_examples: ["Reconcile these unconsumed recap deltas."],
     should_not_delegate_examples: ["Write the accepted changes to project state."],
     regression_risk: "high", recommendation: "retain_unchanged"}

  - {path: ".claude/agents/apex-project-status.md", agent_name: "apex-project-status", current_word_count: 52,
     intended_delegation: "confirmed cross-project overview generation",
     non_delegation_boundary: "confirmed truth only; no candidates or durable database",
     overlap_with: ["ProjectStatus skill"],
     violation: null, proposed_description: null, proposed_word_count: null,
     should_delegate_examples: ["Generate the confirmed project overview."],
     should_not_delegate_examples: ["Promote candidate status changes."],
     regression_risk: "medium", recommendation: "retain_unchanged"}

  - {path: ".claude/agents/apex-review-validity.md", agent_name: "apex-review-validity", current_word_count: 48,
     intended_delegation: "blind validity review through review wiring",
     non_delegation_boundary: "no producer rationale, alignment verdict, or implementation",
     overlap_with: ["apex-review-alignment", "meta-detective"],
     violation: null, proposed_description: null, proposed_word_count: null,
     should_delegate_examples: ["Check whether each frozen claim is evidence-supported."],
     should_not_delegate_examples: ["Assess strategic alignment or repair failures."],
     regression_risk: "critical", recommendation: "retain_unchanged"}

  - {path: ".claude/agents/apex-review-alignment.md", agent_name: "apex-review-alignment", current_word_count: 47,
     intended_delegation: "blind alignment review through review wiring",
     non_delegation_boundary: "no validity verdict, producer rationale, or implementation",
     overlap_with: ["apex-review-validity", "meta-detective", "meta-strategy"],
     violation: null, proposed_description: null, proposed_word_count: null,
     should_delegate_examples: ["Check alignment with the confirmed weekly intent."],
     should_not_delegate_examples: ["Re-evaluate source validity or implement fixes."],
     regression_risk: "critical", recommendation: "retain_unchanged"}

  - {path: ".claude/agents/apex-plan-ops.md", agent_name: "apex-plan-ops", current_word_count: 23,
     intended_delegation: "explicit project capture and native Apex Plan packet creation",
     non_delegation_boundary: "optional project-engine worker, not a weekly stage",
     overlap_with: ["meta-ops"],
     violation: null, proposed_description: null, proposed_word_count: null,
     should_delegate_examples: ["Create a native Apex Plan packet."],
     should_not_delegate_examples: ["Run the weekly loop."],
     regression_risk: "low", recommendation: "retain_unchanged"}

  - {path: ".claude/agents/apex-sync-ops.md", agent_name: "apex-sync-ops", current_word_count: 17,
     intended_delegation: "explicit deterministic Apex read-side reports",
     non_delegation_boundary: "optional project-engine worker, not a weekly stage",
     overlap_with: ["meta-ops"],
     violation: null, proposed_description: null, proposed_word_count: null,
     should_delegate_examples: ["Compute a deterministic blocker report."],
     should_not_delegate_examples: ["Interpret and mutate project state."],
     regression_risk: "low", recommendation: "retain_unchanged"
```

---

## 10. Compaction-recovery decision

```okf
compaction_recovery_decision:
  verdict: "replace_with_apex_state_recovery_note"

  reject_exact_original_note: true
  rejection_reason: >
    Project-root CLAUDE.md reinjection is automatic. Telling Claude to reread
    the activation file duplicates platform behavior and does not restore the
    activated weekly skill body or discover current Apex state.

  existing_recovery_coverage:
    weekly_skill:
      heading: "## Procedure"
      step: "1. Locate the loop"
      coverage:
        - "latest confirmed Session planning feed"
        - "relevant Sync reports"
        - "newest weekly-plan packet"
        - "newest next-day plan"
        - "newest flow packet"
        - "newest flow-recap packet"
        - "current stage determination"
    destination_coverage: "complete"

  minimum_replacement_text: >
    After resume or compaction during a weekly run, invoke `weekly-orchestrator`
    and execute its “Locate the loop” step before making any gate decision.

  first_patch_placement: ".claude/CLAUDE.md"
  weekly_skill_mutation_required: false

  rationale: >
    The recognized root file survives compaction and can restore the routing
    pointer. The weekly skill already owns the actual state-discovery procedure.
```

**Decision:** 0d remains valid as an outcome but not in its proposed wording or location.

---

## 11. Additional high-impact, low-risk candidates

```okf
additional_candidates:
  - candidate_id: "ADD-001"
    finding: "Use literal pointers, not CLAUDE.md @imports."
    admission_test:
      direct_tier0_support: true
      impact: "high"
      risk: "low"
      new_mechanism: false
      operation: "pointer wording only"
    reason: >
      Imported files enter startup context. Literal code-formatted paths preserve
      lazy loading and the intended token reduction.
    recommendation: "include_in_activation_compaction"

  - candidate_id: "ADD-002"
    finding: "Delete volatile availability claims instead of relocating them."
    current_text_class:
      - "All 11 skills above are present as of last check."
      - "Confirm skill status against the table above."
    reason: >
      Availability is runtime state. Moving the claims would create another stale
      inventory rather than a canonical owner.
    replacement: "Use /skills, /doctor, or the actual invocation result."
    recommendation: "include_in_activation_compaction"

  - candidate_id: "ADD-003"
    finding: "Preserve one compressed cross-system mutation boundary."
    reason: >
      Removing the entire project-management-engine section could allow weekly
      orchestration to appear authorized to mutate project state.
    replacement: >
      Weekly orchestration proposes and routes; only `apex-session` applies
      operator-confirmed project/task mutations.
    recommendation: "include_in_activation_compaction"
```

### Candidate not admitted

```okf
not_admitted:
  - proposal: "Change the glossary pointer during Tier 0."
    reason: >
      Both apex-meta/GLOSSARY.md and apex-meta/orchestration/GLOSSARY.md currently
      claim canonical authority. Choosing one is terminology reconciliation, not
      a low-risk pointer correction.
```

The root glossary says it wins conflicting interpretations, while the orchestration glossary separately declares itself the terminology authority for the entire orchestration system.

---

## 12. Rejected, already-covered, and deferred changes

```okf
disposition:
  already_covered:
    - change: "Weekly state and artifact discovery"
      owner: ".claude/skills/weekly-orchestrator/SKILL.md#Procedure step 1"
    - change: "Correct G5 status-merge routing"
      owner: ".claude/skills/weekly-orchestrator/SKILL.md#Contract"
    - change: "PrecapWeek preload name"
      status: "already fixed"
    - change: "PrecapNextDay preload name"
      status: "already fixed"
    - change: "ProjectStatus preload name"
      status: "already fixed"

  rejected:
    - "Repair the stale APSU/G5 loop inside the activation file."
    - "Move the full skill table into weekly-orchestrator."
    - "Move the full agent table into weekly-orchestrator."
    - "Add Fable or Weekly-loop markers to every agent."
    - "Apply a universal 75-word correctness threshold."
    - "Create a new agents/skills map."
    - "Create a new recovery file, hook, registry, or state machine."
    - "Use @imports for the canonical pointers."
    - "Resolve the conflicting glossaries during Tier 0."

  deferred:
    - "apex-kb description compaction pending trigger tests."
    - "deterministic-markdown-patcher description compaction pending trigger tests."
    - "Any use of disable-model-invocation or skillOverrides pending invocation analysis."
    - "Semantic KB repairs pending a separate approved ingest lifecycle."
    - "Glossary consolidation pending terminology reconciliation."
```

---

## 13. Micro-implementation packet

```okf
micro_implementation_packet:
  - candidate_id: "T0-M01"
    priority: 1
    current_path: ".claude/Claude.md"
    artifact_class: "project_activation_file"
    exact_current_heading_or_anchor: "entire path; content unchanged"
    problem: "Filename case does not match recognized Claude Code project instructions."
    intended_result: "Recognized .claude/CLAUDE.md with identical bytes."
    operation_type: "git_case_rename"
    content_to_retain: "all bytes"
    content_to_remove: "none"
    canonical_destination: ".claude/CLAUDE.md"
    minimum_replacement_or_pointer_text: null
    dependencies: []
    validation_required:
      - "git diff --summary shows rename"
      - "old path absent and new path present"
      - "/memory lists .claude/CLAUDE.md"
    rollback_condition:
      - "Claude Code does not list the corrected file"
      - "both case variants remain"
    evidence:
      repository: "direct"
      platform: "official_current_docs"
    impact: 99
    risk: 25
    confidence: 99
    recommended_patch_run: "Run A1"

  - candidate_id: "T0-M02"
    priority: 2
    current_path: ".claude/CLAUDE.md"
    artifact_class: "project_activation_file"
    exact_current_heading_or_anchor:
      - "## core_loop"
      - "## skills"
      - "## agents"
      - "## project_management_engine"
      - "## artifact_paths"
      - "## session_startup"
      - "## exclude_from_context"
      - "## constraints"
    problem: >
      Detailed weekly runtime content duplicates canonical owners and includes
      stale G5/APSU routing.
    intended_result: "Compact activation seed with no loss of global invariants."
    operation_type: "bounded_replace_with_pointer"
    content_to_retain:
      - "identity"
      - "global state/mutation/review invariants"
      - "excluded-path rules"
      - "autonomous override limits"
      - "missing-input behavior"
      - "literal canonical pointers"
    content_to_remove:
      - "detailed core_loop"
      - "skill inventory table"
      - "agent inventory table"
      - "detailed artifact paths"
      - "weekly session-startup procedure"
      - "volatile skill-presence claim"
    canonical_destination:
      weekly_runtime: ".claude/skills/weekly-orchestrator/SKILL.md"
      system_law: "apex-meta/orchestration/00-START-HERE.md"
      system_index: "apex-meta/ORCHESTRATION-SYSTEMS-INDEX.md"
    minimum_replacement_or_pointer_text:
      - "Weekly loop: invoke `weekly-orchestrator`; canonical contract: `.claude/skills/weekly-orchestrator/SKILL.md`."
      - "Final orchestration law: `apex-meta/orchestration/00-START-HERE.md`."
      - "Repo-wide orchestration map: `apex-meta/ORCHESTRATION-SYSTEMS-INDEX.md`."
      - "After resume or compaction, invoke weekly-orchestrator and run Locate the loop before gate decisions."
    dependencies:
      - "T0-M01"
      - "successful load proof"
      - "approved fact-level no-loss ledger"
    validation_required:
      - "before/after size report"
      - "no-loss checks"
      - "weekly routing smoke scenarios"
      - "changed-file allowlist"
      - "fresh-session /memory proof"
      - "post-/compact recovery scenario"
    rollback_condition:
      - "any global invariant is absent"
      - "weekly-orchestrator cannot be discovered or invoked"
      - "a routing smoke scenario changes destination"
    evidence:
      repository: "direct"
      kb: "supporting"
      platform: "official_current_docs"
    impact: 97
    risk: 51
    confidence: 96
    recommended_patch_run: "Run A2 after A1 proof"

  - candidate_id: "T0-M03"
    priority: 3
    current_path: ".claude/skills/weekly-orchestrator/SKILL.md"
    artifact_class: "skill_contract"
    exact_current_heading_or_anchor: "## Procedure / 1. Locate the loop"
    problem: "No separate defect remains after activation recovery pointer is added."
    intended_result: "Preserve current canonical owner unchanged."
    operation_type: "retain_no_change"
    content_to_retain: "entire file"
    content_to_remove: []
    canonical_destination: ".claude/skills/weekly-orchestrator/SKILL.md"
    dependencies: []
    validation_required:
      - "invoke after /compact"
      - "confirm Locate the loop reconstructs position"
    rollback_condition: null
    evidence: "current procedure already covers state discovery"
    impact: 76
    risk: 8
    confidence: 94
    recommended_patch_run: "excluded"

  - candidate_id: "T0-M04"
    priority: 4
    current_path: ".claude/skills/apex-kb/SKILL.md"
    artifact_class: "skill_frontmatter"
    exact_current_heading_or_anchor: "frontmatter description"
    problem: "Description carries body-level page-contract detail."
    intended_result: "Shorter routing description with same trigger surface."
    operation_type: "retain_no_change"
    content_to_retain: "current description until trigger evaluation passes"
    content_to_remove: []
    canonical_destination: null
    minimum_replacement_or_pointer_text: "57-word candidate recorded in section 8"
    dependencies:
      - "fresh-session should-trigger tests"
      - "fresh-session should-not-trigger tests"
    validation_required:
      - "routing comparison"
      - "output behavior comparison"
    rollback_condition: "any false negative or false positive increase"
    evidence: "measured description inventory"
    impact: 55
    risk: 58
    confidence: 82
    recommended_patch_run: "defer"

  - candidate_id: "T0-M05"
    priority: 5
    current_path: ".claude/skills/deterministic-markdown-patcher/SKILL.md"
    artifact_class: "skill_frontmatter"
    exact_current_heading_or_anchor: "frontmatter description"
    problem: "Description narrates executor mechanics and secondary capabilities."
    intended_result: "Shorter routing description with same trigger surface."
    operation_type: "retain_no_change"
    content_to_retain: "current description until trigger evaluation passes"
    content_to_remove: []
    canonical_destination: null
    minimum_replacement_or_pointer_text: "56-word candidate recorded in section 8"
    dependencies:
      - "fresh-session should-trigger tests"
      - "fresh-session should-not-trigger tests"
    validation_required:
      - "routing comparison"
      - "ambiguity test against deterministic-markdown-patcher2"
    rollback_condition: "increased confusion between patcher versions"
    evidence: "measured description inventory"
    impact: 58
    risk: 65
    confidence: 80
    recommended_patch_run: "defer"
```

---

## 14. Recommended first patch run

### Verdict: choose Option A, but enforce an internal load-proof gate

```okf
recommended_first_patch_run:
  selected_option: "Option A — Minimal first test"

  run_A1:
    target_files:
      - ".claude/Claude.md"
      - ".claude/CLAUDE.md"
    operations:
      - "case-only rename"
    stop_condition: "Do not compact until load proof succeeds."

  load_gate:
    required:
      - "/memory lists .claude/CLAUDE.md"
      - "old mixed-case path is absent"
      - "fresh session receives the project instructions"

  run_A2:
    target_files:
      - ".claude/CLAUDE.md"
    operations:
      - "bounded activation-seed replacement"
      - "delete stale duplicate weekly-loop material"
      - "add literal canonical pointers"
      - "add Apex-specific recovery pointer"
    changed_file_allowlist:
      - ".claude/CLAUDE.md"

  first_run_exclusions:
    - ".claude/skills/weekly-orchestrator/SKILL.md"
    - ".claude/skills/apex-kb/SKILL.md"
    - ".claude/skills/deterministic-markdown-patcher/SKILL.md"
    - ".claude/agents/*.md"
    - "apex-meta/GLOSSARY.md"
    - "apex-meta/orchestration/GLOSSARY.md"
```

### Why Option B should wait

- **Skill descriptions:** two possible candidates exist, but trigger regressions have not been measured.
    
- **Agent descriptions:** no current defect was found.
    
- **Weekly recovery note:** the state-discovery behavior already exists; adding another copy would duplicate it.
    
- **Glossary pointer:** authority is currently conflicted.
    
- **Semantic KB work:** unrelated to the runtime patch and outside the approved gate.
    

---

## 15. Required later validation commands and fixtures

These are specifications only. None was executed during this read-only validation.

### 15.1 Repository and allowlist preflight

```powershell
git checkout main
git pull --ff-only origin main
git rev-parse HEAD
git status --short
```

Expected target baseline for a plan built from this packet:

```text
7ab08a57d5b3ad7f2ba67793ba1ec48b28b8ef68
```

If `main` advances, reread all candidate files and update the packet before patch generation.

### 15.2 Case-rename proof

```powershell
git mv .claude/Claude.md .claude/CLAUDE.rename-tmp
git mv .claude/CLAUDE.rename-tmp .claude/CLAUDE.md
git diff --summary
git status --short
```

Required observations:

```okf
rename_gate:
  new_path_exists: true
  old_path_exists: false
  duplicate_case_variants: false
  content_changed: false
```

### 15.3 Claude loading proof

```okf
instruction_loading_fixture:
  setup:
    - "Launch a fresh Claude Code session from repository root."
  actions:
    - "Run /memory."
    - "Record all project instruction files."
  assertions:
    - "The exact path .claude/CLAUDE.md appears."
    - "The mixed-case path does not appear."
    - "No unexpected project CLAUDE.md shadows it."
  optional_stronger_evidence:
    - "Use an existing InstructionsLoaded inspection facility to capture path and reason."
```

### 15.4 Size measurements

Git Bash or WSL:

```bash
wc -l -w -c .claude/CLAUDE.md
```

PowerShell:

```powershell
$text = Get-Content -Raw .claude/CLAUDE.md
[pscustomobject]@{
  Lines = ($text -split "`n").Count
  Words = ([regex]::Matches($text, '\S+')).Count
  Characters = $text.Length
  Utf8Bytes = [Text.Encoding]::UTF8.GetByteCount($text)
}
```

Token reporting must identify the tokenizer. Character division is only an estimate.

### 15.5 No-loss destination checks

```okf
no_loss_assertions:
  activation_seed_must_contain:
    - "state lives in files"
    - "single confirmed mutation path"
    - "independent review before consequential mutation"
    - "operator confirmation"
    - "candidate never auto-promotes"
    - "never auto-trigger skills"
    - "source-knowledge write prohibition"
    - "autonomous override stop conditions"
    - "weekly-orchestrator pointer"

  weekly_skill_must_contain:
    - "precap_week"
    - "precap_next_day"
    - "operator_execution"
    - "evidence_normalize"
    - "flow_recap"
    - "status_merge"
    - "project_status"
    - "review"
    - "G1"
    - "G2"
    - "G3"
    - "G4"
    - "G5"
    - "apex-session"

  forbidden_in_activation_after_compaction:
    - "updated_all_project_status_packet"
    - "full skills table"
    - "full agents table"
    - "All 11 skills above are present"
```

### 15.6 Skill trigger fixtures

Each changed skill description must run in a fresh session with the current and candidate descriptions.

```okf
skill_trigger_eval:
  apex_kb:
    should_trigger:
      - "Audit this Apex KB."
      - "Run Phase 1 ingest for this source set."
      - "Query the compiled KB."
    should_not_trigger:
      - "Plan my next tasks."
      - "Synchronize the project registry."
      - "Update session state."

  deterministic_markdown_patcher:
    should_trigger:
      - "Replace this Markdown section deterministically."
      - "Build a patch intent for these documentation changes."
      - "Validate this Markdown patch plan."
    should_not_trigger:
      - "Rewrite this paragraph."
      - "Summarize this Markdown file."
      - "Review the latest pull request."

  pass_condition:
    - "No should-trigger regression."
    - "No new should-not-trigger activation."
    - "No increased ambiguity between deterministic-markdown-patcher and deterministic-markdown-patcher2."
```

### 15.7 Agent delegation fixtures

```okf
agent_delegation_eval:
  must_delegate:
    - prompt: "Independently validate whether these claims are source-supported."
      expected: "meta-detective or apex-review-validity according to routing context"
    - prompt: "Create the weekly plan packet."
      expected: "apex-precap-week"
    - prompt: "Normalize these post-flow notes."
      expected: "apex-evidence-normalize"
    - prompt: "Compute a deterministic blockers report."
      expected: "apex-sync-ops"

  must_not_delegate:
    - prompt: "Present this operator gate."
      forbidden: "spawning alfred"
    - prompt: "Run the main mutation workflow."
      forbidden: "spawning meta-ops"
    - prompt: "Fix the defect found by the reviewer."
      forbidden: "meta-detective performs implementation"

  current_requirement: "baseline only; no agent description change proposed"
```

### 15.8 Weekly routing smoke scenarios

```okf
weekly_loop_smoke_scenarios:
  - input: "run weekly-orchestrator at week start"
    expected_route: "apex-precap-week / G1"

  - input: "resume the loop after a confirmed weekly packet"
    expected_route: "locate artifacts then apex-precap-next-day / G2"

  - input: "raw execution notes arrive"
    expected_route: "apex-evidence-normalize"

  - input: "normalized evidence and flow packet are ready"
    expected_route: "apex-flow-recap / G4"

  - input: "unconsumed confirmed recap packets exist"
    expected_route: "apex-status-merge / G5"

  - input: "G5 status merge is operator-confirmed"
    expected_route: "apex-session applies mutation"

  - input: "session resumes after /compact"
    expected_route:
      - "root activation file is reinjected"
      - "weekly-orchestrator is invoked"
      - "Locate the loop runs before any gate decision"
```

### 15.9 Diff and patch validation

```bash
git status --short
git diff --stat
git diff --check
git diff -- .claude/CLAUDE.md
```

For later generated patch artifacts:

```bash
git apply --check <patch-file>
```

The final changed-file allowlist for Option A must contain only:

```text
.claude/Claude.md
.claude/CLAUDE.md
```

The first appears only as the rename source; the second is the final file.

---

## 16. Orchestrator return packet

```okf
orchestrator_return_packet:
  task: "Tier 0 plan versus KB independent validation"
  repository: "leela-spec/apexai-os-meta"
  tested_ref: "7ab08a57d5b3ad7f2ba67793ba1ec48b28b8ef68"

  conclusion: "validated_with_qualifications"

  accepted:
    - "Case-correct the activation filename."
    - "Prove loading before content mutation."
    - "Compact the activation file by subtraction."
    - "Keep global invariants in the activation seed."
    - "Point weekly mechanics to weekly-orchestrator."
    - "Delete stale and volatile activation copies rather than relocating them."
    - "Use literal paths, not eager @imports."
    - "Recover after compaction by reinvoking weekly-orchestrator and running Locate the loop."

  qualified:
    - "400-500 tokens is an objective, not a pass/fail threshold."
    - "75 words is a local heuristic, not a Claude Code platform limit."
    - "Only apex-kb and deterministic-markdown-patcher have credible description-compaction candidates."
    - "Those two candidates require trigger evaluation before patching."

  rejected:
    - "Blanket skill description rewrites."
    - "Any agent description rewrite in the first patch."
    - "Uniform Fable or Weekly-loop markers."
    - "A duplicate recovery procedure in weekly-orchestrator."
    - "Repairing the stale APSU/G5 copy."
    - "A new map, hook, state machine, registry, or recovery file."
    - "Glossary canonicalization during Tier 0."

  recommended_sequence:
    - "Run A1: case-only rename."
    - "Prove load with /memory or InstructionsLoaded."
    - "Run A2: compact only .claude/CLAUDE.md."
    - "Run no-loss and routing fixtures."
    - "Generate a git-derived patch artifact."
    - "Run git apply --check."
    - "Only then consider application."

  exact_first_run_targets:
    - ".claude/Claude.md"
    - ".claude/CLAUDE.md"

  safety:
    safe_to_plan: true
    safe_to_create_patch_plan: true
    safe_to_create_patch_files: false
    safe_to_apply: false

  repository_changes_made_by_this_validation: []
```