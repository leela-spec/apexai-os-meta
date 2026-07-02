Title: Vision & Image Paste | Hermes Agent

URL Source: https://hermes-agent.nousresearch.com/docs/user-guide/features/vision

Published Time: Fri, 29 May 2026 12:35:12 GMT

Markdown Content:
Hermes Agent supports **multimodal vision** — you can paste images from your clipboard directly into the CLI and ask the agent to analyze, describe, or work with them. Images are sent to the model as base64-encoded content blocks, so any vision-capable model can process them.

tip

Portal subscribers get vision-capable models (Claude, GPT-5, Gemini) in the same catalog — no extra credentials needed. See [Nous Portal](https://hermes-agent.nousresearch.com/docs/integrations/nous-portal).

## How It Works[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/vision#how-it-works "Direct link to How It Works")

1.   Copy an image to your clipboard (screenshot, browser image, etc.)
2.   Attach it using one of the methods below
3.   Type your question and press Enter
4.   The image appears as a `[📎 Image #1]` badge above the input
5.   On submit, the image is sent to the model as a vision content block

You can attach multiple images before sending — each gets its own badge. Press `Ctrl+C` to clear all attached images.

Images are saved to `~/.hermes/images/` as PNG files with timestamped filenames.

## Paste Methods[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/vision#paste-methods "Direct link to Paste Methods")

How you attach an image depends on your terminal environment. Not all methods work everywhere — here's the full breakdown:

### `/paste` Command[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/vision#paste-command "Direct link to paste-command")

**The most reliable explicit image-attach fallback.**

`/paste`

Type `/paste` and press Enter. Hermes checks your clipboard for an image and attaches it. This is the safest option when your terminal rewrites `Cmd+V`/`Ctrl+V`, or when you copied only an image and there is no bracketed-paste text payload to inspect.

### Ctrl+V / Cmd+V[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/vision#ctrlv--cmdv "Direct link to Ctrl+V / Cmd+V")

Hermes now treats paste as a layered flow:

*   normal text paste first
*   native clipboard / OSC52 text fallback if the terminal did not deliver text cleanly
*   image attach when the clipboard or pasted payload resolves to an image or image path

This means pasted macOS screenshot temp paths and `file://...` image URIs can attach immediately instead of sitting in the composer as raw text.

warning

If your clipboard has **only an image** (no text), terminals still cannot send binary image bytes directly. Use `/paste` as the explicit image-attach fallback.

### `/terminal-setup` for VS Code / Cursor / Windsurf[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/vision#terminal-setup-for-vs-code--cursor--windsurf "Direct link to terminal-setup-for-vs-code--cursor--windsurf")

If you run the TUI inside a local VS Code-family integrated terminal on macOS, Hermes can install the recommended `workbench.action.terminal.sendSequence` bindings for better multiline and undo/redo parity:

`/terminal-setup`

This is especially useful when `Cmd+Enter`, `Cmd+Z`, or `Shift+Cmd+Z` are being intercepted by the IDE. Run it on the local machine only — not inside an SSH session.

## Platform Compatibility[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/vision#platform-compatibility "Direct link to Platform Compatibility")

| Environment | `/paste` | Cmd/Ctrl+V | `/terminal-setup` | Notes |
| --- | --- | --- | --- | --- |
| **macOS Terminal / iTerm2** | ✅ | ✅ | n/a | Best experience — native clipboard + screenshot-path recovery |
| **Apple Terminal** | ✅ | ✅ | n/a | If Cmd+←/→/⌫ gets rewritten, use Ctrl+A / Ctrl+E / Ctrl+U fallbacks |
| **Linux X11 desktop** | ✅ | ✅ | n/a | Requires `xclip` (`apt install xclip`) |
| **Linux Wayland desktop** | ✅ | ✅ | n/a | Requires `wl-paste` (`apt install wl-clipboard`) |
| **WSL2 (Windows Terminal)** | ✅ | ✅ | n/a | Uses `powershell.exe` — no extra install needed |
| **VS Code / Cursor / Windsurf (local)** | ✅ | ✅ | ✅ | Recommended for better Cmd+Enter / undo / redo parity |
| **VS Code / Cursor / Windsurf (SSH)** | ❌² | ❌² | ❌³ | Run `/terminal-setup` on the local machine instead |
| **SSH terminal (any)** | ❌² | ❌² | n/a | Remote clipboard not accessible |

² See [SSH & Remote Sessions](https://hermes-agent.nousresearch.com/docs/user-guide/features/vision#ssh--remote-sessions) below ³ The command writes local IDE keybindings and should not be run from the remote host

## Platform-Specific Setup[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/vision#platform-specific-setup "Direct link to Platform-Specific Setup")

### macOS[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/vision#macos "Direct link to macOS")

**No setup required.** Hermes uses `osascript` (built into macOS) to read the clipboard. For faster performance, optionally install `pngpaste`:

`brew install pngpaste`

### Linux (X11)[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/vision#linux-x11 "Direct link to Linux (X11)")

Install `xclip`:

`# Ubuntu/Debiansudo apt install xclip# Fedorasudo dnf install xclip# Archsudo pacman -S xclip`

### Linux (Wayland)[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/vision#linux-wayland "Direct link to Linux (Wayland)")

Modern Linux desktops (Ubuntu 22.04+, Fedora 34+) often use Wayland by default. Install `wl-clipboard`:

`# Ubuntu/Debiansudo apt install wl-clipboard# Fedorasudo dnf install wl-clipboard# Archsudo pacman -S wl-clipboard`

How to check if you're on Wayland

`echo $XDG_SESSION_TYPE# "wayland" = Wayland, "x11" = X11, "tty" = no display server`

### WSL2[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/vision#wsl2 "Direct link to WSL2")

**No extra setup required.** Hermes detects WSL2 automatically (via `/proc/version`) and uses `powershell.exe` to access the Windows clipboard through .NET's `System.Windows.Forms.Clipboard`. This is built into WSL2's Windows interop — `powershell.exe` is available by default.

The clipboard data is transferred as base64-encoded PNG over stdout, so no file path conversion or temp files are needed.

WSLg Note

If you're running WSLg (WSL2 with GUI support), Hermes tries the PowerShell path first, then falls back to `wl-paste`. WSLg's clipboard bridge only supports BMP format for images — Hermes auto-converts BMP to PNG using Pillow (if installed) or ImageMagick's `convert` command.

#### Verify WSL2 clipboard access[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/vision#verify-wsl2-clipboard-access "Direct link to Verify WSL2 clipboard access")

`# 1. Check WSL detectiongrep -i microsoft /proc/version# 2. Check PowerShell is accessiblewhich powershell.exe# 3. Copy an image, then checkpowershell.exe -NoProfile -Command "Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.Clipboard]::ContainsImage()"# Should print "True"`

## SSH & Remote Sessions[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/vision#ssh--remote-sessions "Direct link to SSH & Remote Sessions")

**Clipboard image paste does not fully work over SSH.** When you SSH into a remote machine, the Hermes CLI runs on the remote host. Clipboard tools (`xclip`, `wl-paste`, `powershell.exe`, `osascript`) read the clipboard of the machine they run on — which is the remote server, not your local machine. Your local clipboard image is therefore inaccessible from the remote side.

Text can sometimes still bridge through terminal paste or OSC52, but image clipboard access and local screenshot temp paths remain tied to the machine running Hermes.

### Workarounds for SSH[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/vision#workarounds-for-ssh "Direct link to Workarounds for SSH")

1.   **Upload the image file** — Save the image locally, upload it to the remote server via `scp`, VSCode's file explorer (drag-and-drop), or any file transfer method. Then reference it by path. _(A `/attach <filepath>` command is planned for a future release.)_

2.   **Use a URL** — If the image is accessible online, just paste the URL in your message. The agent can use `vision_analyze` to look at any image URL directly.

3.   **X11 forwarding** — Connect with `ssh -X` to forward X11. This lets `xclip` on the remote machine access your local X11 clipboard. Requires an X server running locally (XQuartz on macOS, built-in on Linux X11 desktops). Slow for large images.

4.   **Use a messaging platform** — Send images to Hermes via Telegram, Discord, Slack, or WhatsApp. These platforms handle image upload natively and are not affected by clipboard/terminal limitations.

## Why Terminals Can't Paste Images[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/vision#why-terminals-cant-paste-images "Direct link to Why Terminals Can't Paste Images")

This is a common source of confusion, so here's the technical explanation:

Terminals are **text-based** interfaces. When you press Ctrl+V (or Cmd+V), the terminal emulator:

1.   Reads the clipboard for **text content**
2.   Wraps it in [bracketed paste](https://en.wikipedia.org/wiki/Bracketed-paste) escape sequences
3.   Sends it to the application through the terminal's text stream

If the clipboard contains only an image (no text), the terminal has nothing to send. There is no standard terminal escape sequence for binary image data. The terminal simply does nothing.

This is why Hermes uses a separate clipboard check — instead of receiving image data through the terminal paste event, it calls OS-level tools (`osascript`, `powershell.exe`, `xclip`, `wl-paste`) directly via subprocess to read the clipboard independently.

## Supported Models[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/vision#supported-models "Direct link to Supported Models")

Image paste works with any vision-capable model. The image is sent as a base64-encoded data URL in the OpenAI vision content format:

`{  "type": "image_url",  "image_url": {    "url": "data:image/png;base64,..."  }}`

Most modern models support this format, including GPT-4 Vision, Claude (with vision), Gemini, and open-source multimodal models served through OpenRouter.

## Image Routing (Vision-Capable vs Text-Only Models)[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/vision#image-routing-vision-capable-vs-text-only-models "Direct link to Image Routing (Vision-Capable vs Text-Only Models)")

When a user attaches an image — from the CLI clipboard, the gateway (Telegram/Discord photo), or any other entry point — Hermes routes it based on whether your current model actually supports vision:

| Your model | What happens to the image |
| --- | --- |
| **Vision-capable** (GPT-4V, Claude with vision, Gemini, Qwen-VL, MiMo-VL, etc.) | Sent as **real pixels** using the provider's native image content format above. No text summary layer. |
| **Text-only** (DeepSeek V3, smaller open-source models, older chat-only endpoints) | Routed through the `vision_analyze` auxiliary tool — an auxiliary vision model describes the image, and the text description is injected into the conversation. |

You don't configure this — Hermes looks up your current model's capability in the provider metadata and picks the right path automatically. The practical effect: you can switch between vision and non-vision models mid-session and image handling "just works" without changing your workflow. Text-only models get coherent context about the image rather than a broken multimodal payload they'd have to reject.

Which auxiliary model handles the text-description path is configurable under `auxiliary.vision` — see [Auxiliary Models](https://hermes-agent.nousresearch.com/docs/user-guide/configuration#auxiliary-models).

### `vision_analyze` has the same dual behavior[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/vision#vision_analyze-has-the-same-dual-behavior "Direct link to vision_analyze-has-the-same-dual-behavior")

The `vision_analyze` tool itself follows the same routing. When the active main model is vision-capable **and** its provider supports image content inside tool results (currently the Anthropic, OpenAI, Azure-OpenAI, and Gemini 3.x stacks), `vision_analyze` short-circuits the auxiliary describer and returns the raw image pixels as a multimodal tool-result envelope. The main model sees the image natively on its next turn — no aux call, no text-summary information loss, no extra latency.

For text-only main models (or providers whose tool-result channel doesn't carry images), `vision_analyze` falls back to the legacy path: it asks the configured auxiliary vision model to describe the image and returns the description as plain text. Either way the calling tool signature is the same — the tool decides which path to take at runtime based on the active model.
