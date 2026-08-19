# Continue OpenClaw Local Executor: run the live vertical slice, then trim over-engineering

## Context

The prior session built an elaborate local-executor stack (immutable OpenClaw runtime, versioned/ACL-protected guards, a closed-world request validator, a browser-containment plugin, an atomic-config-swap dispatcher) so a local Qwen3-8B model can safely drive a real, authenticated browser tab (Perplexity/ChatGPT/Gemini). Per the handover (`FEE/HANDOVER-2026-08-10-OPENCLAW-LOCAL-EXECUTOR-CURRENT.md`), everything is installed and passing tests, but **no live Qwen-controlled browser submission has ever actually happened.**

This session re-verified machine state (ports, config hash, single shared Perplexity tab all matched the handover exactly) and reran the previously-interrupted opt-in live dispatcher test suite (all 11 passed, including the 3 live-integration tests). A valid, disposable Perplexity request v2 was built and validated against the real validator — see `C:\Users\gehma\AppData\Local\Temp\claude\C--GitDev\1eed0e8a-4dc9-4b24-b7e4-e9d70b62cbb9\scratchpad\vertical-slice\request.json` (harmless prompt: "what year was the first web browser released").

The operator's feedback: too much time/tokens have gone into test ceremony instead of just running the target capability (a local LLM coordinating a real browser through OpenClaw). This plan reflects that: **run the already-built thing now**, report the true result, and only then trim the specific parts of the stack that are ceremony rather than load-bearing safety — without weakening the parts that actually keep an LLM with a documented prompt-injection history from misusing an authenticated account.

## Step A — Run live vertical slices for all three providers now

Current status per provider (from the handover — none of the three has a proven live capture yet):

| Provider | Status |
|---|---|
| Perplexity | Never run live. Operator explicitly locked this as the intended *first* target (Learn step by step / Claude Sonnet 5 / thinking). Request already built and validated this session. |
| ChatGPT | Only an early "harmless transport probe" during extension-pairing discovery (proved the tab-sharing/click mechanics work) — **no verified prompt submission or response capture** ever happened. Schema tuple: `standard/default/off`. |
| Gemini | Zero live testing of any kind. Only the request-schema tuple exists (`standard/default/off`). |

So this plan runs a real vertical slice for all three, not just Perplexity. No more test suites, no hostile-page fixture, no additional prep beyond building the two missing request files — just run them.

1. Build two more disposable request v2 files alongside the existing Perplexity one, same shape, each with its own tiny harmless prompt: one for ChatGPT (`hostname: chatgpt.com`, `standard/default/off`) and one for Gemini (`hostname: gemini.google.com`, `standard/default/off`). Validate each with `scripts/openclaw/validate-execution-request.py` before use.
2. **Tab-sharing constraint**: the browser-policy plugin requires *exactly one* shared tab matching the request's declared hostname. The three providers can't be shared simultaneously. Run them one at a time, and before each run ask the operator to share only that provider's tab via the OpenClaw extension (they already have ChatGPT/Perplexity/Gemini logged in in the isolated Chrome profile per the handover) — confirm with `openclaw browser tabs --json` that exactly one tab, matching hostname, is visible before dispatching that provider.
3. For each provider, run the protected dispatcher **without** `-PrepareOnly`:
   ```powershell
   $dispatcher = 'C:\ProgramData\ApexExecutor\guards\guards-v1-aecae18ef55759b1\dispatch-execution-request.ps1'
   powershell -NoProfile -NonInteractive -ExecutionPolicy Bypass -File $dispatcher -RequestPath <that provider's request.json>
   ```
   Each call temporarily rewrites `openclaw.json` (tool grants/workspace), writes a 3-minute browser policy binding that live tab, and shells out to `openclaw agent --agent apex-executor ...`, which runs Qwen through the `subscription-ai-browser` skill against the operator's real, authenticated tab.
4. Read back whatever the dispatcher reports for each provider: `completed` with a result file, or an honest stop (e.g. `declared_provider_settings_unavailable`, a policy/hostname mismatch, an auth wall). Read the evidence file(s) and quote the actual captured content or actual failure back to the operator per provider — do not paraphrase or improve on it.
5. After each run, confirm: the browser policy file was deleted and `openclaw.json` byte-restored (hash matches pre-run hash) before moving to the next provider.
6. Report all three results plainly, including any that fail. A clean, precise stop condition is a useful and acceptable outcome, not something to fix before reporting.

No other verification, fixture-building, or report-writing happens before these three runs.

## Step B — Trim identified over-engineering (after Step A, informed by what actually happened)

Scope: remove ceremony that doesn't serve the real threat model (a single local operator's own machine), while explicitly **preserving** the mechanisms that are the actual point of this system (Qwen has previously obeyed prompt injection in benchmark evidence and now controls an authenticated tab). Keep unchanged: the immutable/ACL-protected OpenClaw runtime, the browser-policy plugin's live-tab/hostname binding and fail-closed `before_tool_call` hook, prompt-hash immutability, and exact-byte config restore. These are load-bearing, not ceremony.

Concrete edits, all in repo source (`scripts/openclaw/dispatch-execution-request.ps1`, `apex-meta/openclaw/plugins/apex-browser-policy/plugin.js`):

1. **Remove the unexplained fixed delay.** `Start-Sleep -Milliseconds 750` before the Qwen invocation (dispatcher, ~line 780) has no comment, no retry/backoff, and nothing it's waiting on is checked. Delete it, or replace with an actual readiness check if one turns out to be needed (find out by running Step A without it first).
2. **Enforce or delete the browser-policy expiry.** `expires_at` (+3 min) is written into the policy JSON (`plugin.js`/dispatcher ~line 334-343) but nothing ever reads it — it's currently a field that *looks* like a safety control but does nothing. Either add the ~3-line check in the plugin's `before_tool_call` hook (reject if `Date.now() > expires_at`), or remove the field so it stops implying protection it doesn't provide.
3. **Right-size defense-in-depth on disposable per-run artifacts.** Reparse-point-chain checks, hard-link-count checks, and symlink rejection are applied uniformly to every path the dispatcher touches — including throwaway per-run files (empty `openclaw-result.json`/`openclaw-failure.txt` placeholders, the copied prompt, the result file). Keep these checks for identities that are reused and trust-bearing (pinned executable/script hashes, the guard manifest, the protected runtime). Drop them for single-run, immediately-deleted evidence files where the only realistic actor is the operator's own process.
4. **Stop re-running the full live-integration suite as a precondition to every live attempt.** Add a short note (in the handover or a new `FEE/` note) making explicit: the opt-in live dispatcher tests exist to catch *regressions after a source change*, not as a ritual gate before each real Perplexity run. This directly documents the behavior change requested this session so it doesn't recur.

Explicitly deferred (flagged, not acted on this pass — bigger structural change, not clearly a net risk reduction, and changing guard source requires the operator's own elevated reinstall regardless of how small the diff is): the proliferation of hash-versioned `guards-v1-<hash>` directories under `C:\ProgramData\ApexExecutor\guards`. Worth a dedicated follow-up if the operator wants fewer versions to track, but not bundled into this pass.

After making the repo-source edits in item 1-3, the operator will need to run the existing elevated guard-install script themselves (per the handover's existing, unchanged process) for the changes to reach the protected guard actually used by the dispatcher — this plan does not change or bypass that Windows ACL boundary.

## Verification

- Step A's own result *is* the verification — either a real captured Perplexity response or an honest, precise stop condition, read back verbatim from the evidence files (not summarized).
- After Step B edits: rerun the fast pure suites only (`python -m unittest scripts.openclaw.tests.test_safety_wrappers scripts.openclaw.tests.test_validate_execution_request scripts.openclaw.tests.test_subscription_ai_browser_skill -v` and the plugin Node tests) to confirm nothing broke — not the full live-integration suite again.
- Report to the operator: what Step A actually produced, exactly what was simplified in Step B and why each item was judged ceremony vs. load-bearing, and the one manual step they still need to take (rerunning the elevated guard installer) to make Step B's changes live.