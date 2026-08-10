---
title: "OpenClaw Local Executor — Current Implementation Handover"
doc_type: implementation_handover
created: 2026-08-10
status: browser-policy-installed-vertical-slice-not-run
branch: main
canonical_plan: FEE/OpenClaw Local Executor — Installation and Implementation Plan.md
canonical_decision: FEE/OpenClaw Local Executor — Operator Decision Lock.md
verification_report: FEE/OpenClaw Local Executor — Verification Report 2026-08-10.md
---

# OpenClaw Local Executor — current implementation handover

## Read this first

The implementation is installed and close to its first real browser run, but it is **not complete**. Do not reinstall OpenClaw, replace Qwen, add a cloud fallback, create another service, or manually perform the browser task as the coding agent. The next useful action is to finish verification of the already-built path and let **OpenClaw/Qwen** perform one harmless validated Perplexity execution.

The operator stopped this session because of token consumption and requested a complete repository handover. Optimize for a short path to evidence. Do not resume the deferred roadmap until the first vertical slice either passes or produces a precise blocker.

## Mission and authority boundary

APEX and its reasoning models own workflow, prompt creation, provider choice, web-model choice, evaluation, scheduling decisions, and next-step decisions. The local executor is one persistent OpenClaw agent using Qwen3-8B. It receives a validated, frozen request; operates one explicitly shared signed-in browser tab; submits immutable prompt bytes; captures the response verbatim; and returns deterministic evidence.

The executor is not a planner, evaluator, router, scheduler, or autonomous orchestration layer. It must not run the repository's orchestration skills. There is no FEE daemon, global queue, separate control plane, community-skill dependency, or cloud inference fallback.

Canonical authority order:

1. `FEE/OpenClaw Local Executor — Operator Decision Lock.md`
2. `FEE/OpenClaw Local Executor — Installation and Implementation Plan.md`
3. this handover for current machine/repository state
4. `FEE/OpenClaw Local Executor — Verification Report 2026-08-10.md`
5. `OPENCLAW-LOCAL-LLM-MASTER-BRIEF.md` as historical orientation

The decision lock was previously verified at 593 lines and SHA-256 `909BADEDE92D9DC8CAF2F35845B413597DF31D123B82B503004EA1D5E83C5F51`. The installation plan was verified at 1,497 lines and SHA-256 `78DFEBF47E969319485CB874CEFAC28B5EB956CBC9D41B81A12BB8FF73884749`. Recompute before relying on those hashes because later canonical design edits may have changed them.

## Current outcome

Completed:

- standalone Qwen3-8B/llama.cpp structured tool calls
- exact OpenClaw host version `2026.7.1-2`
- protected immutable OpenClaw/Node runtime
- loopback Gateway with token SecretRef
- dedicated `apex-executor` agent at 8K context
- selected-tab official Chrome extension pairing
- closed-world execution-request v2 validator
- bounded script, exact-command, and Git wrappers
- protected versioned guard installation
- request freeze, evidence hardening, idempotency, and config recovery dispatcher
- APEX-owned provider UI skill for ChatGPT, Perplexity, and Gemini
- request-scoped browser policy plugin using the official `before_tool_call` hook
- active Gateway moved from the user-level OpenClaw install to the protected runtime
- repository OpenClaw template refreshed to match the active design

Not completed or not proven:

- the three opt-in live dispatcher tests were started after the newest guard install but the test command was interrupted by the operator after a few seconds; do not report them as passing for guard `aecae18e...`
- runtime proof that the browser hook blocks a real OpenClaw/Qwen browser call when policy is absent or mismatched
- first Qwen-driven Perplexity prompt submission/capture
- hostile-page browser integration fixture
- independent receipt verification for a subscription response
- restart/idempotency browser proof
- persistent Windows Gateway task
- context promotion beyond 8K
- Cron/Automations gates
- real Git mutation in the main repository
- post-vertical-slice FEE reconciliation

## Exact live machine state at handover

Observed at `2026-08-10T23:32:49.5035225+02:00`:

- model endpoint: `127.0.0.1:8090`
- model PID: `27564`
- model command: `C:\LocalModels\runtimes\llama.cpp\llama-server.exe --model C:\LocalModels\qwen3-8b\gguf-q4km\Qwen3-8B-Q4_K_M.gguf --host 127.0.0.1 --port 8090 --ctx-size 8192 --parallel 1 --gpu-layers 999 --jinja --reasoning-budget 128`
- Gateway endpoint: `127.0.0.1:18789`
- Gateway PID: `50332` (ephemeral; re-resolve by port)
- Gateway command uses the protected runtime, not the user npm install
- Chrome extension relay: `127.0.0.1:18799` when the browser plugin is initialized
- active provider topology: standalone llama.cpp only for generation
- active Qwen inference lanes: one (`--parallel 1`)
- cloud fallback: none
- config recovery journal: absent
- exactly one shared browser tab was visible
- shared tab: Perplexity, `https://www.perplexity.ai/?login-new=false&login-source=signupButton`
- shared stable ID at the final observation: `t1`
- raw target ID: `2A6D4FAE26A5B9D5E595A804B3A95F6B`

Stable tab aliases can change after a Gateway/extension reconnect. Never bake `t1` into a request or source file. The dispatcher must inspect and freeze the single live tab immediately before a turn.

### Protected runtime

- path: `C:\ProgramData\ApexExecutor\runtime\openclaw-2026.7.1-2-38f1eec9e8e5c087`
- identity: `38f1eec9e8e5c087567ef21a16304a6a544921551580f5b017305305a9aa9fa1`
- version: OpenClaw `2026.7.1-2`
- file count: 32,079
- owner/protection: Administrators-owned, protected ACL; operator RX only

Do not use `C:\Users\gehma\AppData\Local\Programs\ApexNpm\node_modules\openclaw\openclaw.mjs` for acceptance. That user-level entry was the prior foreground Gateway and was replaced.

### Protected guard

Newest guard:

- path: `C:\ProgramData\ApexExecutor\guards\guards-v1-aecae18ef55759b1`
- identity: `aecae18ef55759b18e0c11b0eb25ea7ff28ae402a4a7b5f7ce539834dc7512ad`
- ACL protected: true
- all five installed manifest file hashes matched their installed bytes
- protected preparation suite: 11 tests, 8 passed and 3 live integrations skipped

Older immutable guard versions intentionally remain. Do not delete them merely because multiple versions exist. The dispatcher binds a deployed copy to its sibling validator/manifest and repository-source diagnostics select deterministically among byte-identical protected validators.

Changing any guard source requires recomputing the validator pin where applicable, running tests, and asking the operator to rerun elevated:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File "C:\GitDev\apexai-os-meta\scripts\openclaw\install-guards.ps1"
```

Do not request elevation unless guard source bytes actually changed.

### Active configuration

- active path: `C:\Users\gehma\.openclaw\openclaw.json`
- active SHA-256 at handover: `F74CE0C3FCF71BCBC1D621F4F5DDD0937B69CA832A78A77C56B119059E8820A0`
- reviewed repository template: `apex-meta/openclaw/openclaw.json`
- template SHA-256 at handover: `C4B37C87471AF0C957CAAA8E0C41812F65DD5C7AFED6F5D7E9D97E1FBB5E94D7`

The two files are semantically aligned but not byte-identical: the active file is strict JSON and contains OpenClaw metadata; the repository file is a commented JSON5 template.

Important active settings:

- `gateway.bind = loopback`
- `gateway.auth.mode = token`
- token comes from user environment SecretRef `OPENCLAW_GATEWAY_TOKEN`
- `apex-executor.model = apex-local/qwen3-8b-q4km`
- `contextTokens = 8192`
- default executor tools allow only `session_status`; dispatcher temporarily shapes request-specific tools
- skills exactly `apex-flow-executor`, `subscription-ai-browser`, `browser-automation`
- skill watcher enabled for `C:/GitDev/apexai-os-meta/apex-meta/openclaw/skills`
- elevated execution disabled
- inline eval strict
- plugin allowlist exactly `llama-cpp`, `apex-browser-policy`, `browser`
- browser policy directory `C:\Users\gehma\AppData\Local\ApexExecutor\browser-policies`

Never print the Gateway token. Load it only with:

```powershell
$env:OPENCLAW_GATEWAY_TOKEN = [Environment]::GetEnvironmentVariable('OPENCLAW_GATEWAY_TOKEN', 'User')
```

and remove it from the process environment afterward.

## Browser/profile state and operator actions already performed

The operator created/used the isolated Chrome data directory `C:\Users\gehma\AppData\Local\ApexExecutor\Chrome\User`. A Chrome profile is a browser data directory, not another provider account. Chrome automatically associated the operator's normal Google account; ChatGPT, Perplexity, and Gemini were manually logged in.

The official OpenClaw extension was loaded unpacked from the protected OpenClaw distribution, paired with the loopback Gateway, and used in selected-tab mode. The operator separately shared ChatGPT and Perplexity during discovery and revoked tabs when asked. Gateway restarts can temporarily clear sharing; the extension later reconnected. At final observation exactly one Perplexity tab was shared.

Do not ask the operator to recreate the profile or reinstall/pair the extension unless the relay actually fails. First check:

```powershell
$runtime = 'C:\ProgramData\ApexExecutor\runtime\openclaw-2026.7.1-2-38f1eec9e8e5c087'
$env:OPENCLAW_GATEWAY_TOKEN = [Environment]::GetEnvironmentVariable('OPENCLAW_GATEWAY_TOKEN', 'User')
& "$runtime\node.exe" "$runtime\node_modules\openclaw\openclaw.mjs" browser --browser-profile chrome tabs --json
Remove-Item Env:OPENCLAW_GATEWAY_TOKEN
```

If there are zero tabs, ask the operator only to click the extension on the desired provider tab and share that tab. If there are multiple tabs, ask the operator to revoke all but the intended tab. Do not select or close tabs on the operator's behalf.

## Browser policy plugin

Repository source:

- `apex-meta/openclaw/plugins/apex-browser-policy/policy.js`
- `apex-meta/openclaw/plugins/apex-browser-policy/plugin.js`
- `apex-meta/openclaw/plugins/apex-browser-policy/index.js`
- manifest/package/tests alongside them

Installed copied plugin:

- `C:\Users\gehma\.openclaw\extensions\apex-browser-policy`

It was installed as a copy, not `--link`, so subsequent repository edits do not affect the running plugin. If source changes, explicitly reinstall/overwrite the plugin and restart the Gateway; do not assume the skill watcher updates plugin code.

OpenClaw installer quirks encountered:

1. `openclaw.compat.pluginApi` must be a semver range. Exact `2026.7.1-2` was rejected even though the runtime printed the same version. The working value is `>=2026.7.1-2`.
2. Plugin installation copied files, then failed because required `policyDir` config had not yet been written. The active config was manually given the required entry, after which validation and plugin doctor passed.
3. `plugins.allow` gates bundled plugins too. Adding only `llama-cpp` and `apex-browser-policy` disabled the `browser` CLI. The final allowlist includes `browser` as the third and only additional entry.
4. `plugins registry --refresh` was run. Plugin doctor reports the hook-only compatibility path as supported informational output.

Policy lifecycle:

1. dispatcher validates request v2
2. request hash produces deterministic OpenClaw session key
3. dispatcher queries live tabs using the protected CLI
4. exactly one HTTPS tab and exact declared hostname are required
5. dispatcher writes `apex.browser-policy/v1` outside the agent workspace using SHA-256(session key) as filename
6. policy binds execution ID, agent ID, session key, browser profile, hostname, stable tab ID, and three-minute expiry
7. plugin `before_tool_call` reads policy and independently re-queries live tabs before each browser call
8. only `status`, `tabs`, targeted `snapshot`, `screenshot`, `focus`, same-host `navigate`, and native `click`, `type`, `press`, `wait` are allowed
9. arbitrary JavaScript evaluation, missing target IDs, other profiles/tabs/hosts, multiple tabs, expired/missing policy, nodes, and unneeded actions fail closed
10. dispatcher removes the policy in `finally`

Residual limitation: a click can navigate before the pre-tool hook knows the destination. OpenClaw performs its generic post-navigation SSRF checks, and the next policy check blocks if the hostname changed, but the hook is not a network-layer exact-host allowlist for blind clicks. This limitation was consciously accepted for the minimal first slice. Do not expand into a custom browser stack without an explicit new operator decision.

## Request v2 and provider lock

`scripts/openclaw/validate-execution-request.py` now requires `apex.execution-request/v2` and a complete `provider_settings` object. It rejects unknown fields and instruction-shaped provider labels. The initial closed-world combinations are intentionally tiny:

- ChatGPT: `standard/default/off`, new conversation or reuse tab
- Perplexity: `learn_step_by_step/claude_sonnet_5/thinking`, new conversation or reuse tab
- Gemini: `standard/default/off`, new conversation or reuse tab
- provider `none`: inert `none/none/off/none`

Subscription providers require the `browser` tool. Provider `none` forbids it. `result_path` must be a file beneath `evidence_dir`, matching the executor's workspace boundary.

The operator's requested first provider state is Perplexity **Learn step by step**, web model **Claude Sonnet 5**, reasoning **thinking**, normally with `new_conversation`. Claude Sonnet 5 is the web model selected inside Perplexity; Qwen3-8B remains the local OpenClaw executor. If Perplexity hides the model control after selecting Learn step by step and the joint state cannot be verified, Qwen must stop with `declared_provider_settings_unavailable`. It must not guess or substitute.

## Skills and the reason there are two

OpenClaw's bundled `browser-automation` skill supplies generic browser mechanics. It does not contain the APEX provider authority contract. `subscription-ai-browser` is the small APEX-owned provider procedure. `apex-flow-executor` holds capture/receipt semantics.

Important corrections made:

- removed ChatGPT instruction to rewrite multiline prompts; prompts remain immutable
- removed Perplexity JavaScript `document.execCommand` guidance; browser JavaScript evaluation is forbidden
- Perplexity uses one native browser `type` action on a snapshotted contenteditable composer
- every browser call must explicitly pass the declared profile; consequential calls explicitly pass the frozen tab ID
- extra shared tabs are a stop condition, not ignorable noise

Do not install a community Perplexity/ChatGPT/ClawHub skill. No official provider-specific bundled skill was found; the APEX provider skill is intentionally small and first-party.

## Verification evidence from the final session

Green before the newest protected install:

- validator + wrappers + provider-skill suite: 44 tests passed
- policy plugin Node suite: 11 tests passed
- repository template: OpenClaw config validation passed with no warnings when the installed plugin load path was supplied
- active config: validation passed with no warnings
- plugin doctor: no error; one informational hook-only compatibility message
- protected Gateway health: passed

After newest guard `aecae18e...`:

- manifest hashes: all five matched
- dispatch suite: 11 tests total; 8 passed, 3 opt-in live tests skipped

Then the three opt-in live tests were launched with:

```powershell
$env:APEX_DISPATCHER_PATH='C:\ProgramData\ApexExecutor\guards\guards-v1-aecae18ef55759b1\dispatch-execution-request.ps1'
$env:APEX_OPENCLAW_INTEGRATION='1'
python -m unittest scripts.openclaw.tests.test_dispatch -v
```

The command was interrupted by the operator after roughly four seconds. No result should be inferred. Post-interruption inspection found no live dispatcher/test/model-turn child, no configuration journal, and healthy Gateway/model listeners.

## Minimal continuation sequence

Keep this sequence small. Stop after the first useful failure.

1. Confirm repository is clean and on `main`, then read the three canonical files named at the top and this handover.
2. Confirm ports 8090 and 18789, protected Gateway command path, active config validation, and exactly one shared Perplexity tab.
3. Rerun the opt-in live dispatcher suite through guard `aecae18e...`. This is a local Qwen/config-recovery test, not a browser submission.
4. Prove the installed browser hook fails closed without a policy using a harmless agent fixture, or proceed through the dispatcher where policy creation is automatic. Do not bypass the dispatcher for the real test.
5. Create a tiny immutable prompt and a valid Perplexity request v2 under a disposable evidence directory. The prompt should be harmless and cheap, e.g. ask for one short factual sentence. It is a transport/capture test, not research.
6. Use the protected dispatcher path. Do not click/type/submit as Codex/Claude Code. Qwen must inspect settings, select Learn step by step + Claude Sonnet 5 + thinking, submit, capture, and report—or stop honestly if the tuple cannot be jointly verified.
7. Verify policy cleanup, config byte restoration, output hash/byte count, actual provider URL/settings, and no duplicate submission on retry.
8. Add one hostile-page fixture proving direct cross-host navigation is denied and a changed live hostname blocks the next call.
9. Update the verification report and ask the operator whether to continue. Do not automatically start Cron, persistence, context promotion, or multi-provider work.

## What to defer to avoid overengineering

The following are in the research plan but are not needed to answer the immediate question “can the local executor safely perform one bounded subscription task?”:

- persistent Windows Gateway Scheduled Task
- 16K/32K context tuning
- Cron/Automations, including deterministic command jobs
- real repository Git commit/push by Qwen
- ChatGPT and Gemini vertical slices
- FEE renaming or `scripts/fee` migration
- old-document archival/deletion
- recurring production workflows
- replacing standalone llama.cpp with an in-process generative provider

The official `@openclaw/llama-cpp-provider@2026.7.1` installed during earlier work is embeddings-only. It cannot replace the standalone chat endpoint. Do not revisit that research unless OpenClaw publishes a reviewed generative provider.

Overengineering assessment: the immutable runtime, validator, evidence hardening, and browser hook are defensible because Qwen3-8B previously obeyed prompt injection in benchmark evidence and now controls authenticated tabs. The work became inefficient by trying to cover future script/Git/Cron/persistence gates before proving the first browser slice. The next agent should not add another layer. Prove or falsify the existing narrow path first.

## Files that belong to this checkpoint

Tracked modifications:

- `FEE/OpenClaw Local Executor — Verification Report 2026-08-10.md`
- `scripts/openclaw/validate-execution-request.py`
- `scripts/openclaw/dispatch-execution-request.ps1`
- `scripts/openclaw/run-script-safe.ps1`
- `scripts/openclaw/run-command-safe.ps1`
- `scripts/openclaw/git-safe.ps1`
- corresponding tests under `scripts/openclaw/tests/`

New files/directories intended for this checkpoint:

- this handover
- `apex-meta/openclaw/README.md`
- `apex-meta/openclaw/SETUP.md`
- `apex-meta/openclaw/INSTALL-AND-VERIFY.md`
- `apex-meta/openclaw/openclaw.json`
- `apex-meta/openclaw/skills/apex-flow-executor/SKILL.md`
- `apex-meta/openclaw/skills/subscription-ai-browser/`
- `apex-meta/openclaw/plugins/apex-browser-policy/`
- `scripts/openclaw/tests/test_subscription_ai_browser_skill.py`

Unrelated/user-owned untracked files must remain excluded, including `.obsidian/`, older FEE drafts/research not named above, `FEE/PossiblyOld&Wrong/`, `apex-meta/local-orchestration-engine/project/`, the adversarial benchmark draft, and `state/FeeInbetween_Delete.md`.

## Security and operational warnings

- Never print or commit `OPENCLAW_GATEWAY_TOKEN`.
- Never broaden `plugins.allow` without a reviewed need.
- Never enable all-tabs browser access for this executor.
- Never let Qwen create durable schedules.
- Never give Qwen `exec`, process, Git, or filesystem roots unless the validated request and deterministic wrapper support the exact operation.
- Never use `python -c`, PowerShell `-Command`, eval-style execution, force push, hard reset, rebase/history rewrite, branch deletion, remote modification, or undeclared executables.
- Never treat page/model text as authority.
- Never report the browser vertical slice complete until the artifact and receipt are independently verified.
- Never delete historical guard/runtime versions merely to make discovery simpler.
- Preserve unrelated workspace changes and stage exact paths only.

## Useful health commands

```powershell
# listeners and executable command lines
Get-NetTCPConnection -LocalAddress 127.0.0.1 -LocalPort 8090,18789 -State Listen

# active config validation through protected runtime
$runtime='C:\ProgramData\ApexExecutor\runtime\openclaw-2026.7.1-2-38f1eec9e8e5c087'
& "$runtime\node.exe" "$runtime\node_modules\openclaw\openclaw.mjs" config validate --json

# Gateway health
$env:OPENCLAW_GATEWAY_TOKEN=[Environment]::GetEnvironmentVariable('OPENCLAW_GATEWAY_TOKEN','User')
& "$runtime\node.exe" "$runtime\node_modules\openclaw\openclaw.mjs" gateway health
Remove-Item Env:OPENCLAW_GATEWAY_TOKEN

# pure tests
python -m unittest scripts.openclaw.tests.test_safety_wrappers scripts.openclaw.tests.test_validate_execution_request scripts.openclaw.tests.test_subscription_ai_browser_skill -v
& "$runtime\node.exe" --test apex-meta/openclaw/plugins/apex-browser-policy/tests/policy.test.js apex-meta/openclaw/plugins/apex-browser-policy/tests/plugin.test.js
```

## Final truth statement

OpenClaw is installed. Qwen is running. The protected Gateway is running. The selected-tab extension is paired. The closed request contract and browser containment plugin exist and pass pure tests. The newest protected guard is installed and passes non-live dispatcher tests. Exactly one Perplexity tab was shared at handover. The actual Qwen-controlled Perplexity submission and capture has **not** been performed, and that is the next decisive gate.
