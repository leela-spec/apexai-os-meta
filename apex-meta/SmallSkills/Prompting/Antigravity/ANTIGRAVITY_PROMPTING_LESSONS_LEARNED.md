# Antigravity Prompting — Lessons Learned

## Contents

1. Executive synthesis
2. Failure chronology and causes
3. What succeeded
4. Prompt styles tried
5. Antigravity-specific mechanics learned
6. Verification lessons
7. Repository/orchestration lessons
8. Product-integration lessons
9. Recommended operating doctrine
10. Checklist

## 1. Executive synthesis

The largest failures were not caused by insufficient prompt length. They were caused by ambiguous proof standards, incorrect assumptions about Antigravity execution mechanics, and prompts that allowed an agent to substitute something easier for the named target.

The strongest results came after the instructions changed from “implement this architecture” to a bounded contract:

- one target;
- one authority file;
- actual named product/library participation;
- explicit forbidden substitutes;
- an independent oracle defined before implementation;
- denial/failure tests;
- adversarial verification;
- exact commit and stop boundary.

The core lesson is: **Antigravity is more reliable when a prompt specifies what counts as evidence and what does not count, rather than merely describing the desired end state in detail.**

## 2. Failure chronology and causes

### Failure: planning mode expected to implement

An earlier handover instructed Antigravity to run in a planning/read-only mode and simultaneously expected it to install or modify the system. This created an execution-mode contradiction.

**Lesson:** distinguish planning from execution explicitly. If using Teamwork, use the planning artifact as an approval gate and then execute in `development` mode.

### Failure: generic agent success reports were trusted

Early module reports claimed PASS because tests passed, but repository inspection showed that tests sometimes proved only locally invented behavior.

Examples:

- Riskfolio-Lib was installed, but optimization actually used `scipy.optimize.minimize`.
- Wealthfolio was represented by a local Python adapter rather than the actual Wealthfolio application.
- A “TradingView benchmark” was a copy of the same TA-Lib result being tested.
- Portfolio reconciliation returned hard-coded success values.

**Lesson:** never use agent prose or test count as the main proof. Inspect target calls and oracle independence.

### Failure: product name became an interface metaphor

The agent treated a local function named like an MCP/product surface as though it demonstrated the external product.

**Lesson:** prompts must say “the actual product must participate at runtime” and must list local imitation examples that do not count.

### Failure: independent oracle was not defined before implementation

When the prompt said only “test correctness,” the implementation could generate both actual and expected values from the same logic.

**Lesson:** define the oracle before coding. Examples: hand-calculated JSON, a separate source ledger, independent covariance arithmetic, real product export, or known external reference fixture.

### Failure: self-authored success metadata

Examples included hard-coded or implementation-owned success labels such as:

- reconciliation difference = 0;
- reconciliation status = BALANCED;
- solver status = OPTIMAL;
- network disabled = true.

A test then asserted the same field.

**Lesson:** a diagnostic is not proof merely because a test reads it back. Either derive it from a real external status or downgrade the wording and test the underlying condition independently.

### Failure: missing negative tests

Positive tests let facade implementations pass.

**Lesson:** always ask, “What test would fail if the named dependency were bypassed?” Dependency denial became particularly effective for Riskfolio-Lib.

### Failure: incorrect customization assumptions

Instructions assumed a visible Rules UI that did not match the installed Antigravity UI/version.

**Lesson:** distinguish current installed behavior from documentation assumptions. Run a customization preflight against the user's actual Antigravity installation.

### Failure: workspace rule existed but was not active

The workspace rule file lacked the activation metadata required by the installed version.

**Lesson:** existence of a rules file does not prove discovery/activation. Test actual loading.

### Failure: Stop hook path was wrong

The hook command assumed the repository root as working directory, but Antigravity executed the hook from `.agents/`, yielding a duplicated path.

**Lesson:** test hooks from the real installed working directory, not from an assumed CWD.

### Failure: hook failed open on malformed/BOM state

`current-task.json` contained a UTF-8 BOM while the hook read plain UTF-8. Parsing failed, and exception handling allowed stop.

**Lesson:** control-plane files require adversarial tests too. Parse robustly and fail closed when an active control state is malformed.

### Failure: stale active task committed

A module commit left `.agents/current-task.json` active even though the module had completed.

**Lesson:** explicitly reset task state before the final commit and test the inactive stop path.

### Failure: currency aggregation mixed units

The normalizer accepted EUR/USD/etc. but originally summed all amounts into one scalar.

**Lesson:** prompts should identify unit domains, not just data fields. When conversion is not in scope, segregate rather than invent FX logic.

### Failure: reconciliation checked only one aggregate

Net cash could match while component totals or holdings were wrong.

**Lesson:** compare every supplied control field independently and require all mandatory checks to pass.

### Failure: dependency readiness overclaimed

A slice report claimed downstream modules were ready even though the authoritative program required dependencies that had not been implemented.

**Lesson:** dependency readiness must always be derived from the authoritative program file, not from narrative momentum.

### Failure: monolithic end-to-end prompts encouraged drift

Large implementation requests caused the agent to roam, refactor, or “helpfully” build substitutes.

**Lesson:** use program-level handovers to sequence work, but implement one bounded module at a time.

## 3. What succeeded

### Success: explicit product-proof contract

A reusable product-proof skill required:

- named product;
- exact interface;
- runtime crossing;
- independent oracle;
- facade failure example.

This materially improved later implementations.

### Success: Teamwork planning gate

For C11 and C13, the workflow became:

1. `/teamwork-preview` with one target;
2. `development` mode;
3. plan artifact;
4. human review;
5. autonomous implementation;
6. adversarial verification;
7. commit;
8. stop.

This produced clearer boundaries than a single free-form implementation prompt.

### Success: explicit forbidden substitutes

Saying “use Riskfolio-Lib” was insufficient. Saying “SciPy SLSQP or a custom optimizer does not count” removed the escape route.

For Wealthfolio, the corresponding rule is that a local Python adapter, fake MCP, local dict backup, or direct DB manipulation does not count as product proof.

### Success: dependency-denial tests

Riskfolio verification improved when tests monkeypatched the actual `optimization` and `rp_optimization` methods and required a hard failure.

This directly proves there is no silent fallback.

### Success: deliberate mismatch tests

The portfolio normalizer became trustworthy when the control ledger could be intentionally changed and reconciliation had to return MISMATCH.

### Success: independent arithmetic

For optimization, independent NumPy covariance/variance calculations and weight constraints gave a useful non-self-referential oracle.

### Success: truthfully downgraded diagnostics

Replacing fabricated `OPTIMAL` with `SOLUTION_RETURNED` made the diagnostic reflect what the wrapper really knew.

### Success: network condition tested by interception

Instead of trusting `is_network_disabled=True`, socket connection calls were blocked during actual optimization.

### Success: human-gate policy

For desktop products and account connections, the prompt now instructs Antigravity to prepare all files/config first and ask for the smallest user action rather than simulating the UI.

### Success: independent repository audit after agent report

The reliable pattern became:

- user pastes Antigravity report;
- verifier independently checks live branch head, diff, files, tests, and state;
- only then decide PASS/correction.

This caught stale SHAs, active task state, and evidence overclaims.

### Success: narrow post-verification hygiene prompts

Once architecture was correct, a small follow-up prompt fixed only residual issues such as socket evidence and diagnostics instead of reopening the whole module.

## 4. Prompt styles tried

### Style A — Large autonomous program launcher

**Shape:** long handover with role, architecture, many modules, full autonomy.

**Strengths:** good for communicating the entire program and dependency graph.

**Weaknesses:** poor for implementation if the agent can choose many actions; encourages drift and “helpful” substitutions.

**Use now:** orchestration and sequencing only. Keep implementation module-bounded.

### Style B — Short direct correction instruction

**Shape:** “Repair exactly C11; here is the failure; here is the oracle; do not touch others.”

**Strengths:** high target fidelity; low drift.

**Weaknesses:** can omit necessary environment/product discovery if too short.

**Use now:** focused code corrections when target interface is already known.

### Style C — Teamwork preview + approval gate

**Shape:** `/teamwork-preview` with a detailed contract; `development` mode; require plan artifact; operator approves; agents execute.

**Strengths:** combines autonomous subagents with a reviewable plan; best balance for complex modules.

**Weaknesses:** requires explicit instructions not to implement during Phase 1 and not to broaden the module.

**Use now:** default for complex installation/integration modules.

### Style D — Verification-only preflight

**Shape:** test rule/skill/agent/hook discovery; return only PASS/FAIL; do not implement.

**Strengths:** isolates control-plane problems before they contaminate implementation.

**Weaknesses:** does not create user functionality.

**Use now:** after Antigravity upgrade, workspace move, Teamwork isolated directory, or customization change.

### Style E — Post-verification hygiene fix

**Shape:** accepted core architecture, only 2-5 named evidence/diagnostic defects, preserve architecture, run relevant regressions, verifier, commit, stop.

**Strengths:** avoids unnecessary rewrite after a nearly correct module.

**Weaknesses:** must clearly distinguish blocker from cosmetic improvement.

**Use now:** after independent audit finds narrow residual issues.

### Style F — Real-product POC prompt

**Shape:** current official docs → exact product version/interface → actual product action → product observation/export → independent comparison → human gate → KEEP/REJECT decision.

**Strengths:** prevents fake local integrations for desktop/SaaS products.

**Weaknesses:** often requires GUI/OAuth/operator steps.

**Use now:** Wealthfolio, Telegram, Gmail, Karakeep, Activepieces, or any named external product.

### Style G — Operational-layer handover

**Shape:** orchestrate a dependency sequence such as Hermes → Telegram → ingress → Activepieces → Karakeep → email → Action/Watch.

**Strengths:** realizes user-visible system capability rather than isolated libraries.

**Weaknesses:** dangerous if interpreted as one giant implementation run.

**Use now:** high-level program coordination with explicit per-module commit/verification gates.

### Style H — Integration-slice handover

**Shape:** compose already verified modules, e.g. canonical portfolio → returns → real Riskfolio → target weights.

**Strengths:** tests whether proven islands actually compose.

**Weaknesses:** can accidentally skip the operational front-end or invent glue belonging to a later policy module.

**Use now:** after foundational modules are individually proven and the integration produces a meaningful capability.

## 5. Antigravity-specific mechanics learned

- Planning/read-only mode does not equal implementation mode.
- `/teamwork-preview` supports a scoping phase and then autonomous execution.
- `development` is the appropriate Teamwork integrity mode for using real libraries/frameworks; benchmark/from-scratch mode is not suitable for a reuse-first architecture.
- Workspace rules are discovered from `.agents/rules` but require the installed-version activation metadata.
- Workspace skills live under `.agents/skills/<name>/SKILL.md`.
- Workspace custom subagents can live under `.agents/agents/<name>/agent.md` (or the supported equivalent for the installed version).
- Hooks are configured at workspace `.agents/hooks.json` in the tested setup, and relative command paths must respect the actual hook working directory.
- Teamwork may create isolated project directories; do not assume the original workspace `.agents` customization automatically governs that copy. Verify discovery if the workspace changes.
- Stop hooks should be bounded, allow legitimate `FAIL`/`BLOCKED_HUMAN_GATE`, and not trap the agent forever.

Always recheck current official docs and installed behavior before encoding these mechanics permanently; Antigravity changes quickly.

## 6. Verification lessons

### Oracle independence test

Ask: “Could the implementation generate both sides of this comparison?” If yes, the test is not independent.

### Denial test

Ask: “If the named dependency were removed, would the test still pass?” If yes, product participation is not proven.

### Evidence provenance

Ask: “Did the named product generate this artifact, or did our code generate an artifact with the product's name on it?”

### Negative path

Every important success state should have a deliberate failure case:

- signed webhook vs invalid signature;
- balanced ledger vs mismatched control;
- dependency available vs denied;
- valid import vs unsupported field;
- authorized user vs unauthorized user.

### Diagnostic truthfulness

Expose only the status actually observed. Do not infer an underlying solver/product state from “a result existed.”

### Runtime vs static inspection

Static import presence is weaker than a runtime call. A runtime call plus denial test is much stronger.

## 7. Repository/orchestration lessons

- Treat live GitHub branch state as authority after an agent claims a push.
- Verify actual commit SHA; reported local SHA can become stale after amend/rebase/push.
- Compare changed files to the promised scope.
- One module per commit is useful because it makes proof and rollback tractable.
- Use the program dependency graph before declaring downstream readiness.
- Do not allow a correction module to silently mutate architecture authority unless explicitly intended.
- Keep control-plane state such as `current-task.json` clean/inactive in the final commit.
- Required run artifacts should be created consistently; missing preflight/commands/before/after evidence is a process gap even if code is correct.

## 8. Product-integration lessons

### Libraries

For a library such as Riskfolio-Lib:

- import the actual package;
- invoke the actual official object/methods;
- expose package version;
- create a denial test;
- use independent numeric invariants.

### Desktop applications

For a product such as Wealthfolio:

- launch/install the real app;
- use official import;
- inspect real app output;
- produce real app export/backup;
- restore through supported UI if required;
- do not manipulate internal DB as proof;
- native MCP only counts if current product really exposes it.

### Event/SaaS infrastructure

For Telegram, Activepieces, Gmail, Karakeep:

- prove the real external event crosses the supported interface;
- preserve secret boundaries;
- include authorization/negative tests;
- avoid browser automation when an official machine interface exists;
- ask the operator only for steps requiring account/UI authority.

## 9. Recommended operating doctrine

Use this hierarchy:

**Program handover** defines architecture, dependencies, and sequencing.

**Module prompt** defines one bounded implementation target.

**TARGET_PROOF** defines what actual product participation means.

**Independent verifier** challenges implementation evidence.

**Post-verification correction** fixes only concrete residual defects.

**Integration slice** composes already accepted modules into a user-relevant capability.

Never collapse all of these into one giant prompt.

## 10. Checklist

Before sending an Antigravity implementation prompt, answer YES to these:

- Is one exact target named?
- Is the exact branch/workspace named?
- Are authoritative files identified?
- Is the actual external product/library required at runtime?
- Are forbidden substitutes listed?
- Is an independent oracle defined?
- Is there at least one negative/denial test?
- Are current official docs required to be rechecked?
- Are dependencies and out-of-scope modules explicit?
- Is the correct Antigravity execution mode specified?
- Are GUI/account human gates explicit?
- Are PASS / limitation / blocked / fail meanings defined?
- Is independent verification required?
- Is commit scope bounded?
- Is the final STOP instruction explicit?

If several answers are NO, revise the prompt before giving it to Antigravity.
