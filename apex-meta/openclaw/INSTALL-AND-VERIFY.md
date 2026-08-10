# Claude Code task — install OpenClaw and verify the four things that could invalidate the design

**Run this on the operator's Windows laptop, in `C:\GitDev\apexai-os-meta`.**

Paste everything below the line into Claude Code.

---

## Role

You are Claude Code with local filesystem and shell access on the operator's Windows 11 laptop. Your job is to install OpenClaw, wire it to the already-installed local model, and **answer four empirical questions**. You are not building the APEX system. You are finding out whether the intended design is viable on this machine.

Report findings. Do not paper over failures — a clean negative answer is worth more than an optimistic one.

## Machine and existing state

```text
HP OmniBook X Flip 16-as0xxx · Windows 11
Intel Core Ultra 7 258V · ~31.6 GB RAM
Intel Arc 140V integrated graphics (shared memory, no dedicated VRAM)

Already installed:
  Qwen3-8B-Q4_K_M.gguf  (sha256 d98cdcbd03e17ce47681435b5150e34c1417f50b5c0019dd560e4882c5745785)
  llama.cpp b10333 (commit 08659901c), Vulkan backend
  Qwen3-8B OpenVINO GenAI INT4 (~5.0 GB) — second config, not benchmarked
  Chrome, with live signed-in sessions for ChatGPT, Perplexity, Gemini
Repo: C:\GitDev\apexai-os-meta
```

`scripts/lmbench/adapter.py` already talks to llama.cpp over an OpenAI-compatible endpoint. Read it to find the exact host, port and launch flags in use rather than guessing.

## Hard constraints

- **Do not enable any Automations or cron schedule.** Manual invocation only.
- **Do not install any third-party ClawHub skill.** OpenClaw's own guidance is to treat them as untrusted code.
- **Do not modify anything under `scripts/lmbench/`.** It is the measuring instrument and must stay untouched.
- **Do not commit or push** unless the operator asks. Report what you would commit.
- **Use "selected tabs" access mode**, not "all tabs", when pairing the Chrome extension.
- If a step requires entering a password or solving a CAPTCHA, **stop and hand it to the operator.**

## Q1 — Does the local model emit real structured tool calls?

This is the most likely thing to break, and OpenClaw's docs name it: local models often emit *"raw JSON/XML/ReAct text"* instead of structured tool calls, and the documented fix is **the serving chat template, not a proxy conversion layer**.

1. Start the llama.cpp server as `scripts/lmbench` does. Record the exact command.
2. Install OpenClaw. Record the version and the install method.
3. Configure the local provider in OpenClaw's JSON5 config:

```json5
{
  agents: { defaults: { model: { primary: "local/qwen3-8b" } } },
  models: {
    mode: "merge",
    providers: {
      local: {
        baseUrl: "http://127.0.0.1:<port>/v1",
        apiKey: "local",
        api: "openai-completions",
      },
    },
  },
}
```

4. Give the agent one trivial tool-requiring task and inspect the raw exchange.

**Report:** does it emit a structured tool call, or prose containing JSON? If prose, try the correct Qwen3 chat template on the llama.cpp side and report whether that fixes it. Also try `api: "openai-responses"` and report which works. If tool calling cannot be made to work, say so plainly — everything downstream depends on it.

## Q2 — Can it drive a signed-in Chrome tab?

The docs say yes: *"lets an agent control your signed-in Chrome tabs without launching a separate managed browser."* Verify it on this machine, with these accounts.

```powershell
openclaw browser extension path
# load unpacked at that path via chrome://extensions with Developer mode on
openclaw browser extension pair
# paste the pairing string into the toolbar popup, choose SELECTED TABS
```

Then, with a signed-in ChatGPT tab in the OpenClaw tab group, have the agent:

1. focus that tab
2. read the composer
3. insert a short harmless prompt — **as one flowing paragraph with no literal newlines**, because ChatGPT's composer sends on a bare Enter (`BAO-001`)
4. read the composer back to confirm the full text landed **before** submitting (`BAO-002`)
5. submit, wait, extract the response

**Report:** did it reach the authenticated session without a re-login? Did tab-group scoping hold — confirm it cannot see a tab outside the group. Did a CDP `dispatchKeyEvent` timeout appear, and if so was the text actually present anyway (`BAO-008`)? Capture the raw extracted text and its character count.

## Q3 — What does it cost in RAM, and does the machine stay usable?

`QG-6` resource coexistence is a hard gate that no other score compensates for, it is unmeasured for every candidate, and this is the cheapest test available.

Measure resident memory and subjective responsiveness at each step, cumulatively:

1. baseline, nothing running
2. llama.cpp with Qwen3-8B loaded
3. plus OpenClaw running
4. plus Chrome with three signed-in AI tabs
5. plus an IDE or terminal session
6. during an actual generation from step 4's flow

**Report:** a table of peak RAM and shared GPU memory at each step, whether the machine stayed interactive, and any swapping, thrash, OOM or crash. State plainly whether this configuration fits in ~31.6 GB.

## Q4 — Do skills load, and does memory actually persist and learn?

1. Point OpenClaw at the repo skill directory via `skills.load.extraDirs`:

```json5
skills: { load: { extraDirs: ["C:/GitDev/apexai-os-meta/apex-meta/openclaw/skills"] } }
```

2. Confirm `apex-flow-executor` is discovered and appears as an invocable command.
3. Ask the agent to remember one specific fact.
4. Inspect the agent workspace — default `~/.openclaw/workspace` — and confirm which of `USER.md`, `MEMORY.md`, `memory/YYYY-MM-DD.md`, `DREAMS.md` exist and what landed in them.
5. End the session, start a new one, and check whether the fact survived.
6. Report whether the "dreaming sweep" consolidation ran, and what if anything it promoted.

**Report:** does skill discovery work from a repo path outside the workspace? Is memory genuinely per-agent? Does it persist across sessions unprompted, or only when explicitly told to remember? This decides whether the "it learns" property the operator is counting on is real on this setup.

## Deliverable

One Markdown report at `apex-meta/openclaw/VERIFY-RESULT-<YYYY-MM-DD>.md`:

```yaml
openclaw_version: <version>
install_method: <method>
Q1_structured_tool_calls: PASS | FAIL | PASS_AFTER_TEMPLATE_FIX
Q1_working_api_setting: openai-responses | openai-completions | neither
Q2_signed_in_chrome_control: PASS | FAIL
Q2_tab_group_scoping_held: true | false
Q3_fits_in_31_6_GB: true | false
Q3_peak_ram_full_stack_mb: <int>
Q3_machine_stayed_interactive: true | false
Q4_skill_discovered_from_repo_path: true | false
Q4_memory_persisted_across_sessions: true | false
Q4_memory_required_explicit_instruction: true | false
blocking_problems: []
verdict: VIABLE | VIABLE_WITH_CHANGES | NOT_VIABLE_ON_THIS_MACHINE
```

Plus, for each question, the raw evidence — exact commands, exact output, screenshots where a UI decided the answer.

## Do not

- do not build the APEX flow loop
- do not write a prompt body or a flow packet
- do not enable scheduling
- do not install community skills
- do not touch `scripts/lmbench/`
- do not conclude `VIABLE` if Q1 or Q2 failed — they are prerequisites, not preferences
