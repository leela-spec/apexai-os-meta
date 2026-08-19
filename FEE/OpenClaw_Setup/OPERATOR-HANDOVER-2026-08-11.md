# Operator handover — running OpenClaw workflows yourself

This is your reference for taking over direct operation of OpenClaw: what's already configured, why the last test succeeded where earlier ones failed, and a step-by-step process for testing each workflow yourself before deciding whether to trust the local model with it.

## Why GPT-4o-mini succeeded and Qwen3-8B did not

Both ran the *exact same task*, same skill instructions, same browser, same tab. The difference was entirely in how each model handled being wrong.

| | Qwen3-8B (local) | GPT-4o-mini (cloud) |
|---|---|---|
| Wrong tool-call field | Used `values` instead of `text`, then later `textGone` instead of `text` | Used `selector` on a `press` action that only accepts `ref` |
| What happened after the error | Repeated the **identical wrong call 4–6 times in a row**, never changing anything | Read the error, **fixed the specific thing it complained about, on the very next call**, every time |
| Result | Every browser call blocked; it invented a plausible-sounding answer from its own training data and reported it as real | Real page navigation happened; it took a screenshot, had it read by a vision model, and reported what the page actually showed |

So this was never about context size (32K was already proven sufficient, zero overflow errors since the switch) and never about guardrails blocking it (once the containment plugin was removed, GPT's calls reached the real browser and worked). It comes down to one specific capability: **whether the model can read a tool-error message and correct the one thing that was wrong.** Qwen3-8B, quantized to 4 bits and running at 8B parameters, could not do this reliably. GPT-4o-mini could, every time, immediately.

This is worth remembering as you test more workflows: if a workflow fails with the local model, check *specifically* whether it's repeating an identical mistake without adapting. That symptom means "this model can't do this job," not "something is misconfigured."

## Current state (as of this handover)

- **Gateway**: running, port 18789. Restart it any time — your browser logins survive, but the browser process itself stops and needs restarting separately (see below).
- **Local model**: Qwen3-8B via llama.cpp, port 8090, 32K context. Still available as `apex-local/qwen3-8b-q4km`.
- **Cloud model**: your OpenAI key is configured as `openai/gpt-4o-mini` and `openai/gpt-4.1-nano`. **`apex-executor`'s default is now `openai/gpt-4.1-nano`** — you don't need to pass `--model` anymore unless you want to override it for one call.
- **Browser**: the *managed* OpenClaw browser profile (not your personal Chrome, not the old extension mode). It launches itself, no clicking "share tab" required. Perplexity, ChatGPT, and Gemini are logged in inside it — that login is saved to disk and survives restarts.
- **Skills loaded for `apex-executor`**: `apex-flow-executor` (capture/receipt rules), `subscription-ai-browser` (our own provider-specific procedure), `browser-automation` (OpenClaw's bundled generic browser mechanics).
- **`openclaw` command**: works from any **new** terminal window (it was already on your PATH; old terminal windows just predate that).

## Step-by-step: how to test a workflow yourself

Repeat this same sequence for each workflow (Perplexity question-answering, ChatGPT, Gemini, and later anything new).

### 1. Check the browser is running and logged in

```bash
openclaw browser profiles
```

Look for `openclaw: running`. If it says `stopped`, start it:

```bash
openclaw browser start
```

Then check which tabs are open:

```bash
openclaw browser tabs --json
```

If the provider tab you need isn't listed, open it (logins persist, so you won't need to log in again):

```bash
openclaw browser open "https://www.perplexity.ai/"
```

**Watch out for**: every time the Gateway restarts, the managed browser process stops too. It does *not* restart itself. You'll always need to run `openclaw browser start` again after a Gateway restart, then re-open whatever tabs you need — but you will not need to log in again.

### 2. Describe the workflow in plain language, then look for a matching skill first

Before writing anything new, check whether a skill already exists for what you're about to do:

```bash
openclaw skills search "<what you're trying to do>"
```

Example: `openclaw skills search "chatgpt image"` or `openclaw skills search "gmail"`. This searches ClawHub live — real, current results, not something I'm guessing at.

**Watch out for**: most search results are API-key-based tools (they need their own separate paid API key, unrelated to your subscriptions) or unrelated to browser automation. Read the description carefully. If nothing fits, that's a real, confirmed answer — not a reason to assume you missed something.

### 3. If nothing fits, write (or point me to write) the smallest possible instruction

This project already has two provider-driving skills:

- `apex-meta/openclaw/skills/subscription-ai-browser/SKILL.md` — the general rules (find the right tab, don't fabricate answers, verify before submitting)
- `apex-meta/openclaw/skills/subscription-ai-browser/references/*.md` — one file per provider with the exact steps (e.g. `#ask-input` is Perplexity's composer)

For a new workflow, the pattern is the same: a short reference file describing the exact UI steps for that specific site. This is genuinely APEX-specific work (nobody else has written "how to drive Perplexity's Learn-step-by-step mode"), not something to search for endlessly.

### 4. Run it manually, with the cloud model, and watch it happen

```bash
openclaw agent --agent apex-executor --message "your exact task description here"
```

Since `apex-executor`'s default is now `gpt-4.1-nano`, you don't need `--model`. If you want to force a specific one for this call only:

```bash
openclaw agent --agent apex-executor --model "openai/gpt-4o-mini" --message "..."
```

**Watch out for — session memory.** If you run the agent multiple times without something to separate them, it remembers the *entire* previous conversation, including old failed attempts, and that can overflow context or confuse a new task. Give each fresh test its own session:

```bash
openclaw agent --agent apex-executor --session-key "agent:apex-executor:my-test-1" --message "..."
```

Change the text after the last `:` each time you want a clean slate.

### 5. Verify — don't just trust the reported answer

This is the step that caught Qwen's fabrication. After a run:

- Check the actual tab: `openclaw browser tabs --json` — does the URL show a real search/conversation, not just the homepage?
- Look at the session transcript yourself if you want the full detail — I can show you how to read one, or just ask me to check a specific run.
- Only trust "it worked" once you've confirmed something real changed on the page.

### 6. Once it works with the cloud model, repeat with the local model

Same message, same steps, just add `--model "apex-local/qwen3-8b-q4km"`:

```bash
openclaw agent --agent apex-executor --model "apex-local/qwen3-8b-q4km" --session-key "agent:apex-executor:my-test-1-local" --message "..."
```

Compare the two transcripts side by side. If the local model repeats an identical wrong call more than once or twice, that's your answer for this workflow: it needs the cloud model, not Qwen.

## Cost note

Every `gpt-4.1-nano` / `gpt-4o-mini` call costs real (small) money on your OpenAI account. Nano is the cheapest tier available on your key. There's no way to test cloud-model behavior without spending a little — budget for it, but it should be cents per test, not dollars.

## What to watch out for, gathered in one place

- **Gateway restart ⇒ browser stops ⇒ tabs disappear (but logins don't).** Always `browser start` then re-`open` your tabs after any Gateway restart.
- **Repeats a wrong call verbatim, no adaptation ⇒ model capability limit**, not a config problem. Don't spend time re-wording skills for this specific failure mode; it didn't help for Qwen.
- **A confident, correct-sounding final answer is not proof it worked.** Always check the actual tab/URL changed.
- **`openclaw` only works in *new* terminal windows** until you close and reopen ones that predate the PATH change.
- **ClawHub search results are mostly API-key tools**, not browser automation of your logged-in subscriptions — read descriptions, don't assume a hit is a fit.
- **Every cloud-model call costs a small amount of real money.** Local model calls are free but currently unreliable for multi-step tool use.
