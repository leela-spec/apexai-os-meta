# Install OpenClaw — the actual commands

> Current state (2026-08-10): installation and extension pairing are complete. This page preserves the bootstrap procedure; do not rerun the unpinned installer or overwrite the active user configuration. The reviewed repository template is `openclaw.json`, and live evidence is recorded in the dated FEE verification report.

**Goal of this page: get OpenClaw running with the local Qwen3-8B, and confirm it can drive a signed-in Chrome tab.** Nothing else.

Everything that can be pre-staged already is. `openclaw.json` in this folder is a working config with your llama.cpp endpoint and this repo's skill directory already wired. You run five commands.

## 0. Prerequisites — already satisfied

Node 22.22.3+ / 24.15+ / 25.9+ is required. Your machine reports Node **24.18.0**. If the install script disagrees it will provision its own Node.

## 1. Start the local model

The endpoint OpenClaw will use is `http://127.0.0.1:8090/v1`, which is the one `scripts/lmbench/adapter.py` already talks to.

```powershell
# from C:\LocalModels\runtimes\<llama.cpp dir>
.\llama-server.exe ^
  -m C:\LocalModels\qwen3-8b\gguf-q4km\Qwen3-8B-Q4_K_M.gguf ^
  --host 127.0.0.1 --port 8090 ^
  --gpu-layers 999 --ctx-size 32768 ^
  --jinja
```

`--jinja` matters. It makes llama.cpp apply the model's own chat template, which is what produces **structured tool calls** rather than prose containing JSON. This is the single most likely thing to go wrong, and it is a launch flag rather than an OpenClaw setting.

Leave this running in its own window. Verify:

```powershell
curl http://127.0.0.1:8090/v1/models
```

## 2. Install OpenClaw

```powershell
iwr -useb https://openclaw.ai/install.ps1 | iex
```

Then:

```powershell
openclaw --version
openclaw doctor
```

If `openclaw` is not recognised, it is a PATH problem — the most common Windows issue. Open a new terminal before assuming the install failed.

## 3. Point it at the config

Either copy the config into place:

```powershell
mkdir $HOME\.openclaw -Force
copy C:\GitDev\apexai-os-meta\apex-meta\openclaw\openclaw.json $HOME\.openclaw\openclaw.json
```

**Or** leave it in the repo and point at it, which keeps it versioned in git:

```powershell
setx OPENCLAW_CONFIG_PATH "C:\GitDev\apexai-os-meta\apex-meta\openclaw\openclaw.json"
```

Then open a new terminal and confirm the model and skill are visible:

```powershell
openclaw doctor
openclaw gateway status
```

## 4. Install the Chrome extension

This is what lets it drive your **already signed-in** tabs rather than a separate browser.

```powershell
openclaw browser extension path
```

Copy the path it prints. Then in Chrome: `chrome://extensions` → enable **Developer mode** → **Load unpacked** → select that directory.

```powershell
openclaw browser extension pair
```

Click the OpenClaw toolbar icon, paste the pairing string, and choose **Selected tabs** — not "All tabs". In selected-tabs mode, tab-group membership is the access boundary, so the executor is confined to the tabs you put in the group.

## 5. Verify it works — four checks

Open a ChatGPT tab, sign in if needed, and add it to the OpenClaw tab group.

**Check 1 — does the model emit structured tool calls?**

```powershell
openclaw run "List the files in the current directory."
```

Look at whether it produced a real tool call or prose containing JSON. **If it's prose, that's the `--jinja` flag or the chat template — fix it at the llama.cpp end, not with a proxy.**

**Check 2 — can it see your signed-in tab?**

```powershell
openclaw run "What tabs can you see? Report their titles and URLs. Do not click anything."
```

Confirm it names your ChatGPT tab, and confirm it does **not** see a tab you left out of the group.

**Check 3 — can it drive it?**

```powershell
openclaw run "In the ChatGPT tab, type this into the composer but DO NOT submit: Hello from OpenClaw. Then read the composer back and tell me exactly what it contains."
```

Type-then-read-back, no submit. If a CDP `dispatchKeyEvent` timeout appears, check the actual state before retrying — the text is usually there anyway (`BAO-008`).

**Check 4 — does memory persist?**

```powershell
openclaw run "Remember that the APEX capture path is artifacts/flow-packets/<date>/prompt-packs/bodies/."
```

Then look in `%USERPROFILE%\.openclaw\workspace\` for `MEMORY.md` or `memory\<today>.md`. Start a new session and ask what it remembers.

## 6. Resource check

While all of it is running — model, OpenClaw, Chrome with three AI tabs, an IDE — look at Task Manager and record peak RAM.

You have ~31.6 GB and the model alone takes 10.76–14.16 GB. OpenClaw's own docs suggest far heavier hardware for a comfortable agent loop, so this is worth knowing early. It may well be fine for a copy-paster with a tiny action set, but nobody has measured it.

## What to report back

```yaml
openclaw_version:
node_version:
check_1_structured_tool_calls: PASS | FAIL | PASS_ONLY_WITH_JINJA
check_2_sees_signed_in_tab: PASS | FAIL
check_2_scoping_held: true | false      # could NOT see an out-of-group tab
check_3_can_type_into_composer: PASS | FAIL
check_4_memory_file_created: true | false
check_4_survived_new_session: true | false
peak_ram_full_stack_gb:
machine_stayed_usable: true | false
blocking_problems: []
```

## Do not, yet

- do not enable Automations or cron
- do not install any ClawHub community skill — OpenClaw's own guidance is to treat third-party skills as untrusted code
- do not submit a real prompt to a subscription AI until checks 1–3 pass
- do not modify anything under `scripts/lmbench/`

## If check 1 fails

That is the one that blocks everything. In order:

1. confirm `--jinja` is on the llama.cpp command line
2. confirm the GGUF carries a chat template — `llama-server` logs it at startup
3. try `api: "openai-responses"` in `openclaw.json`
4. as a last resort only, `compat: { supportsTools: false }` — but that disables tool-dependent skills, so it is a diagnostic, not a fix

Report which step resolved it, or that none did.
