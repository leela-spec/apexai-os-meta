Yes — I only asked one question because I was going to walk the decisions sequentially. Given your request, that was the wrong interaction model.

You have now **verified all design decisions**, so there are **no remaining operator-decision questions** from the synthesis. The three reports are therefore converted from competing recommendations into one locked design basis.

## Locked decisions

|ID|Decision|Locked choice|
|---|---|---|
|**D01**|Browser/session identity|Dedicated isolated OpenClaw-managed automation profile by default; existing signed-in Chrome only as fallback|
|**D02**|ChatGPT execution|**Oracle primary**, native Browser fallback|
|**D03**|Gemini execution|Native Browser + Gemini-Web provider guidance; **manual authentication only**, no password/TOTP storage|
|**D04**|Perplexity|Native Browser/browser-automation initially|
|**D05**|Large-prompt semantics|**Hybrid:** actual instructions remain literal prompt text; large supporting context can be attached/referenced|
|**D06**|Large-response capture|Direct-to-file where supported; never route large results through Qwen merely for transfer|
|**D07**|Exec security|Allowlist with approval on miss, **fail closed** when approval unavailable; `strictInlineEval=true`; `autoAllowSkills=false`|
|**D08**|Git authority|Separate **executor** and **publisher** authority; direct-to-`main` remains project policy|
|**D09**|Multi-repo|Per-repository OpenClaw agents/workspaces rather than one broad filesystem authority|
|**D10**|Dispatch/scheduling|Native OpenClaw agent dispatch + native Cron/Automations|
|**D11**|Recovery/idempotency|Native restart/task recovery + provider-specific recovery; Oracle for ChatGPT|
|**D12**|Evidence|Native tasks/audit + compact APEX artifact receipt|

The relevant underlying mechanisms remain current in OpenClaw: managed browser profiles are first-class; exec approvals support per-agent allowlists, argument restrictions, on-miss approvals and fail-closed fallback; Cron supports exact-command execution; and Gateway restart recovery persists/reconciles sessions, tasks and scheduled work. ([OpenClaw](https://docs.openclaw.ai/tools/browser?utm_source=chatgpt.com "Browser (OpenClaw-managed) - OpenClaw"))

Oracle also currently provides the specific ChatGPT features behind D02/D06/D11: Deep Research handling, reattachment/session metadata, duplicate-prompt protection, durable transcripts/research artifacts and `--write-output`. ([GitHub](https://github.com/steipete/oracle/blob/main/docs/browser-mode.md?utm_source=chatgpt.com "oracle/docs/browser-mode.md at main · steipete/oracle · GitHub"))

# Complete remaining question list

There are **zero remaining questions requiring an operator preference** before implementation.

There are, however, factual questions that implementation must answer through testing. These should be encoded as **LIVE TEST REQUIRED** OKF concepts rather than asked of you as design questions.

## LT01 — Managed browser login persistence

**Question:** After Windows restart, sleep and Gateway restart, do the dedicated ChatGPT, Gemini and Perplexity sessions remain authenticated?

**Pass:** normal automation resumes without credentials.

**Fail:** request operator reauthentication; do not automate account recovery.

---

## LT02 — Oracle Windows qualification

**Question:** Does Oracle work reliably on this exact Windows/OpenClaw/Chrome configuration?

Test:

```text
short ChatGPT prompt
→ result

long prompt
→ result file

Deep Research
→ wait
→ full final report

Gateway restart / detach
→ reattach
→ no duplicate submission
```

Oracle's current implementation has durable browser-session/research-output features, but the target Windows machine still needs qualification. ([GitHub](https://github.com/steipete/oracle/blob/main/docs/browser-mode.md?utm_source=chatgpt.com "oracle/docs/browser-mode.md at main · steipete/oracle · GitHub"))

---

## LT03 — Literal large-prompt insertion

**Question:** How large a literal prompt can Gemini and Perplexity receive reliably using existing OpenClaw browser mechanisms?

Test at minimum:

```text
1 KB
20 KB
50 KB
100–150 KB
```

Verify:

```text
expected bytes/chars
actual composer content
start marker
end marker
Send only after verification
```

This test determines whether any adapter is needed.

---

## LT04 — Attachment semantics

**Question:** For Gemini and Perplexity, does attaching Markdown/source artifacts preserve the intended semantics for **supporting context**?

This does **not** replace literal instruction text under D05.

Pass means large supporting materials can remain fully pass-by-reference.

---

## LT05 — Direct response capture

**Question:** Can Gemini and Perplexity final outputs be extracted directly to durable storage without returning the entire response through Qwen?

Test:

```text
browser-targeted extraction
→ deterministic host redirection/write
→ SHA-256
→ byte count
→ compact receipt
```

The browser supports page-context evaluation and managed file operations, but page JavaScript should **not** be assumed to have arbitrary host-filesystem access. ([OpenClaw](https://docs.openclaw.ai/tools/browser?utm_source=chatgpt.com "Browser (OpenClaw-managed) - OpenClaw"))

---

## LT06 — Completion detection

For each provider:

**Question:** Which observable state reliably means “the response is actually complete”?

Test:

- normal answer;
    
- long answer;
    
- Deep Research;
    
- reload while generating;
    
- tab switch;
    
- reconnect after Gateway restart;
    
- temporarily missing/lazy-loaded final report.
    

Especially avoid interpreting a temporarily incomplete rendered page as truncation.

---

## LT07 — Browser recovery loop

**Question:** Does Qwen3-8B reliably operate using the efficient browser snapshot mode without requiring full accessibility dumps?

Test:

```text
snapshot
→ select action
→ UI changes
→ stale ref
→ resnapshot
→ recover
```

The managed browser exposes an efficient snapshot default, so this is primarily a model-behavior qualification rather than a missing platform capability. ([OpenClaw](https://docs.openclaw.ai/tools/browser?utm_source=chatgpt.com "Browser (OpenClaw-managed) - OpenClaw"))

---

## LT08 — CAPTCHA/auth blocker handling

**Question:** Does every provider flow reliably stop instead of improvising when confronted with:

```text
CAPTCHA
2FA
password prompt
account recovery
suspicious-login challenge
terms/reconsent
```

Expected outcome:

```text
BLOCKED_AUTH
+ screenshot/status
+ compact escalation receipt
```

No automated bypass.

---

## LT09 — Exec allowlist enforcement

Test that these execute automatically:

```text
approved Python script
approved PowerShell script
git status
git diff
approved tests
```

Test that these do not:

```text
python -c ...
pwsh -Command ...
unapproved executable
unexpected arguments
```

OpenClaw currently supports `argPattern`, `ask: on-miss`, `askFallback: deny`, and stricter handling of inline interpreter evaluation. ([OpenClaw](https://docs.openclaw.ai/tools/exec-approvals?utm_source=chatgpt.com "Exec approvals - OpenClaw"))

---

## LT10 — Git execution/publisher separation

**Executor agent must demonstrate:**

```text
status       PASS
diff         PASS
edit         PASS
test         PASS
add          PASS
commit       PASS

push         BLOCK
force push   BLOCK
reset --hard BLOCK
rebase       BLOCK
worktree     BLOCK
branch -D    BLOCK
```

**Publisher agent must demonstrate:**

```text
inspect current repository state
push origin main
```

while remaining unable to perform broad unrelated host execution.

---

## LT11 — Immediate dispatch

**Question:** Can APEX hand a compact work order to the intended repository executor/session and get a durable task identity immediately?

Test:

```text
APEX
→ openclaw agent / Gateway dispatch
→ target agent
→ task/session id
→ execution
→ receipt
```

No Cron polling dependency.

---

## LT12 — Deterministic Cron without Qwen

**Question:** Can an exact approved command execute via native scheduling without starting the model?

Expected:

```text
Cron
→ exact argv
→ stdout/stderr
→ exit code
→ task/run history
```

OpenClaw currently supports exact `--command-argv` scheduled execution. ([OpenClaw](https://docs.openclaw.ai/cli/cron?utm_source=chatgpt.com "Cron - OpenClaw"))

---

## LT13 — Model-backed Cron

**Question:** Can a scheduled executor turn target the correct agent/workspace and recover correctly after restart?

OpenClaw supports agent targeting for scheduled jobs and persistent scheduling/reconciliation. ([OpenClaw](https://docs.openclaw.ai/automation/cron-jobs?utm_source=chatgpt.com "Scheduled tasks - OpenClaw"))

---

## LT14 — Gateway restart during execution

Test interruptions during:

```text
Qwen turn
script
ChatGPT Deep Research
Gemini wait
Perplexity wait
Cron job
```

Expected:

```text
no silent loss
no duplicate browser submission
task state reconciled
recover or explicit failure
```

OpenClaw documents persistence/recovery of conversations, transcripts, schedules, background-task records and queued messages across Gateway restarts. ([OpenClaw](https://docs.openclaw.ai/gateway/restart-recovery?utm_source=chatgpt.com "Restart recovery - OpenClaw"))

---

## LT15 — Receipt contract

Every successful artifact-producing workflow must produce something equivalent to:

```json
{
  "work_order_id": "...",
  "status": "succeeded",
  "artifact_path": "...",
  "artifact_sha256": "...",
  "artifact_bytes": 0,
  "prompt_sha256": "...",
  "provider": "...",
  "conversation_ref": "...",
  "openclaw_task_id": "...",
  "started_at": "...",
  "completed_at": "..."
}
```

And failures must use the same envelope with an explicit failure code.

---

## LT16 — Multi-repository isolation

Prove that:

```text
apex-meta-executor
```

cannot accidentally edit another project's files, and:

```text
leela-executor
```

cannot edit `apexai-os-meta` unless explicitly granted.

This test is essential because the architecture relies on **mechanical least authority**, not only agent instructions.

---

# Implementation gate

So the final state is:

```text
OPERATOR DECISIONS        12 / 12 LOCKED
UNRESOLVED DESIGN CHOICES  0
LIVE TESTS                16
CUSTOM SKILLS APPROVED     0
CUSTOM FRAMEWORKS          0
POSSIBLE ADAPTERS          0–2, gated by LT03/LT05
```

The correct next step is therefore **not another Q&A round**. It is to write the OKF decision set with all twelve decisions marked accepted, encode these sixteen items as validation concepts, and then use them as the implementation/vertical-slice acceptance specification.