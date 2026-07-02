Title: Profiles: Running Multiple Agents | Hermes Agent

URL Source: https://hermes-agent.nousresearch.com/docs/user-guide/profiles

Markdown Content:
Run multiple independent Hermes agents on the same machine — each with its own config, API keys, memory, sessions, skills, and gateway state.

## What are profiles?[​](https://hermes-agent.nousresearch.com/docs/user-guide/profiles#what-are-profiles "Direct link to What are profiles?")

A profile is a separate Hermes home directory. Each profile gets its own directory containing its own `config.yaml`, `.env`, `SOUL.md`, memories, sessions, skills, cron jobs, and state database. Profiles let you run separate agents for different purposes — a coding assistant, a personal bot, a research agent — without mixing up Hermes state.

When you create a profile, it automatically becomes its own command. Create a profile called `coder` and you immediately have `coder chat`, `coder setup`, `coder gateway start`, etc.

## Quick start[​](https://hermes-agent.nousresearch.com/docs/user-guide/profiles#quick-start "Direct link to Quick start")

`hermes profile create coder       # creates profile + "coder" command aliascoder setup                       # configure API keys and modelcoder chat                        # start chatting`

That's it. `coder` is now its own Hermes profile with its own config, memory, and state.

## Creating a profile[​](https://hermes-agent.nousresearch.com/docs/user-guide/profiles#creating-a-profile "Direct link to Creating a profile")

tip

Quickest setup: run `hermes setup --portal` inside the new profile to wire up models + tools at once. See [Nous Portal](https://hermes-agent.nousresearch.com/docs/integrations/nous-portal).

### Blank profile[​](https://hermes-agent.nousresearch.com/docs/user-guide/profiles#blank-profile "Direct link to Blank profile")

`hermes profile create mybot`

Creates a fresh profile with bundled skills seeded. Run `mybot setup` to configure API keys, model, and gateway tokens.

If you plan to use this profile as a kanban worker (or want the kanban orchestrator to route work to it), pass `--description "<role>"` at create time so the orchestrator knows what it's good at:

`hermes profile create researcher --description "Reads source code and external docs, writes findings."`

You can also set or auto-generate the description later with `hermes profile describe` — see the [Kanban guide](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban#auto-vs-manual-orchestration) for the full routing model.

### Clone config only (`--clone`)[​](https://hermes-agent.nousresearch.com/docs/user-guide/profiles#clone-config-only---clone "Direct link to clone-config-only---clone")

`hermes profile create work --clone`

Copies your current profile's `config.yaml`, `.env`, and `SOUL.md` into the new profile. Same API keys and model, but fresh sessions and memory. Edit `~/.hermes/profiles/work/.env` for different API keys, or `~/.hermes/profiles/work/SOUL.md` for a different personality.

### Clone everything (`--clone-all`)[​](https://hermes-agent.nousresearch.com/docs/user-guide/profiles#clone-everything---clone-all "Direct link to clone-everything---clone-all")

`hermes profile create backup --clone-all`

Copies **everything** — config, API keys, personality, all memories, full session history, skills, cron jobs, plugins. A complete snapshot. Useful for backups or forking an agent that already has context.

### Clone from a specific profile[​](https://hermes-agent.nousresearch.com/docs/user-guide/profiles#clone-from-a-specific-profile "Direct link to Clone from a specific profile")

`hermes profile create work --clone --clone-from coder`

Honcho memory + profiles

When Honcho is enabled, `--clone` automatically creates a dedicated AI peer for the new profile while sharing the same user workspace. Each profile builds its own observations and identity. See [Honcho -- Multi-agent / Profiles](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory-providers#honcho) for details.

## Using profiles[​](https://hermes-agent.nousresearch.com/docs/user-guide/profiles#using-profiles "Direct link to Using profiles")

### Command aliases[​](https://hermes-agent.nousresearch.com/docs/user-guide/profiles#command-aliases "Direct link to Command aliases")

Every profile automatically gets a command alias at `~/.local/bin/<name>`:

`coder chat                    # chat with the coder agentcoder setup                   # configure coder's settingscoder gateway start           # start coder's gatewaycoder doctor                  # check coder's healthcoder skills list             # list coder's skillscoder config set model.default anthropic/claude-sonnet-4`

The alias works with every hermes subcommand — it's just `hermes -p <name>` under the hood.

### The `-p` flag[​](https://hermes-agent.nousresearch.com/docs/user-guide/profiles#the--p-flag "Direct link to the--p-flag")

You can also target a profile explicitly with any command:

`hermes -p coder chathermes --profile=coder doctorhermes chat -p coder -q "hello"    # works in any position`

### Sticky default (`hermes profile use`)[​](https://hermes-agent.nousresearch.com/docs/user-guide/profiles#sticky-default-hermes-profile-use "Direct link to sticky-default-hermes-profile-use")

`hermes profile use coderhermes chat                   # now targets coderhermes tools                  # configures coder's toolshermes profile use default    # switch back`

Sets a default so plain `hermes` commands target that profile. Like `kubectl config use-context`.

### Knowing where you are[​](https://hermes-agent.nousresearch.com/docs/user-guide/profiles#knowing-where-you-are "Direct link to Knowing where you are")

The CLI always shows which profile is active:

*   **Prompt**: `coder ❯` instead of `❯`
*   **Banner**: Shows `Profile: coder` on startup
*   **`hermes profile`**: Shows current profile name, path, model, gateway status

## Profiles vs workspaces vs sandboxing[​](https://hermes-agent.nousresearch.com/docs/user-guide/profiles#profiles-vs-workspaces-vs-sandboxing "Direct link to Profiles vs workspaces vs sandboxing")

Profiles are often confused with workspaces or sandboxes, but they are different things:

*   A **profile** gives Hermes its own state directory: `config.yaml`, `.env`, `SOUL.md`, sessions, memory, logs, cron jobs, and gateway state.
*   A **workspace** or **working directory** is where terminal commands start. That is controlled separately by `terminal.cwd`.
*   A **sandbox** is what limits filesystem access. Profiles do **not** sandbox the agent.

On the default `local` terminal backend, the agent still has the same filesystem access as your user account. A profile does not stop it from accessing folders outside the profile directory.

If you want a profile to start in a specific project folder, set an explicit absolute `terminal.cwd` in that profile's `config.yaml`:

`terminal:  backend: local  cwd: /absolute/path/to/project`

Using `cwd: "."` on the local backend means "the directory Hermes was launched from", not "the profile directory".

Also note:

*   `SOUL.md` can guide the model, but it does not enforce a workspace boundary.
*   Changes to `SOUL.md` take effect cleanly on a new session. Existing sessions may still be using the old prompt state.
*   Asking the model "what directory are you in?" is not a reliable isolation test. If you need a predictable starting directory for tools, set `terminal.cwd` explicitly.

## Running gateways[​](https://hermes-agent.nousresearch.com/docs/user-guide/profiles#running-gateways "Direct link to Running gateways")

Each profile runs its own gateway as a separate process with its own bot token:

`coder gateway start           # starts coder's gatewayassistant gateway start       # starts assistant's gateway (separate process)`

### Different bot tokens[​](https://hermes-agent.nousresearch.com/docs/user-guide/profiles#different-bot-tokens "Direct link to Different bot tokens")

Each profile has its own `.env` file. Configure a different Telegram/Discord/Slack bot token in each:

`# Edit coder's tokensnano ~/.hermes/profiles/coder/.env# Edit assistant's tokensnano ~/.hermes/profiles/assistant/.env`

### Safety: token locks[​](https://hermes-agent.nousresearch.com/docs/user-guide/profiles#safety-token-locks "Direct link to Safety: token locks")

If two profiles accidentally use the same bot token, the second gateway will be blocked with a clear error naming the conflicting profile. Supported for Telegram, Discord, Slack, WhatsApp, and Signal.

### Persistent services[​](https://hermes-agent.nousresearch.com/docs/user-guide/profiles#persistent-services "Direct link to Persistent services")

`coder gateway install         # creates hermes-gateway-coder systemd/launchd serviceassistant gateway install     # creates hermes-gateway-assistant service`

Each profile gets its own service name. They run independently.

Inside the official Docker image

Per-profile gateways are supervised by [s6-overlay](https://github.com/just-containers/s6-overlay) (PID 1 in the container), so `hermes profile create <name>` automatically registers an s6 service slot at `/run/service/gateway-<name>/`. `hermes -p <name> gateway start/stop/restart` dispatches to `s6-svc` instead of spawning a bare process — crashes are auto-restarted and `docker restart` preserves the previously-running set of gateways. See [Per-profile gateway supervision](https://hermes-agent.nousresearch.com/docs/user-guide/docker#per-profile-gateway-supervision) for details.

## Configuring profiles[​](https://hermes-agent.nousresearch.com/docs/user-guide/profiles#configuring-profiles "Direct link to Configuring profiles")

Each profile has its own:

*   **`config.yaml`** — model, provider, toolsets, all settings
*   **`.env`** — API keys, bot tokens
*   **`SOUL.md`** — personality and instructions

`coder config set model.default anthropic/claude-sonnet-4echo "You are a focused coding assistant." > ~/.hermes/profiles/coder/SOUL.md`

If you want this profile to work in a specific project by default, also set its own `terminal.cwd`:

`coder config set terminal.cwd /absolute/path/to/project`

## Updating[​](https://hermes-agent.nousresearch.com/docs/user-guide/profiles#updating "Direct link to Updating")

`hermes update` pulls code once (shared) and syncs new bundled skills to **all** profiles automatically:

`hermes update# → Code updated (12 commits)# → Skills synced: default (up to date), coder (+2 new), assistant (+2 new)`

User-modified skills are never overwritten.

## Managing profiles[​](https://hermes-agent.nousresearch.com/docs/user-guide/profiles#managing-profiles "Direct link to Managing profiles")

`hermes profile list           # show all profiles with statushermes profile show coder     # detailed info for one profilehermes profile rename coder dev-bot   # rename (updates alias + service)hermes profile export coder   # export to coder.tar.gzhermes profile import coder.tar.gz   # import from archive`

## Deleting a profile[​](https://hermes-agent.nousresearch.com/docs/user-guide/profiles#deleting-a-profile "Direct link to Deleting a profile")

`hermes profile delete coder`

This stops the gateway, removes the systemd/launchd service, removes the command alias, and deletes all profile data. You'll be asked to type the profile name to confirm.

Use `--yes` to skip confirmation: `hermes profile delete coder --yes`

note

You cannot delete the default profile (`~/.hermes`). To remove everything, use `hermes uninstall`.

## Tab completion[​](https://hermes-agent.nousresearch.com/docs/user-guide/profiles#tab-completion "Direct link to Tab completion")

`# Basheval "$(hermes completion bash)"# Zsheval "$(hermes completion zsh)"`

Add the line to your `~/.bashrc` or `~/.zshrc` for persistent completion. Completes profile names after `-p`, profile subcommands, and top-level commands.

## How it works[​](https://hermes-agent.nousresearch.com/docs/user-guide/profiles#how-it-works "Direct link to How it works")

Profiles use the `HERMES_HOME` environment variable. When you run `coder chat`, the wrapper script sets `HERMES_HOME=~/.hermes/profiles/coder` before launching hermes. Since 119+ files in the codebase resolve paths via `get_hermes_home()`, Hermes state automatically scopes to the profile's directory — config, sessions, memory, skills, state database, gateway PID, logs, and cron jobs.

This is separate from terminal working directory. Tool execution starts from `terminal.cwd` (or the launch directory when `cwd: "."` on the local backend), not automatically from `HERMES_HOME`.

The default profile is simply `~/.hermes` itself. No migration needed — existing installs work identically.

## Sharing profiles as distributions[​](https://hermes-agent.nousresearch.com/docs/user-guide/profiles#sharing-profiles-as-distributions "Direct link to Sharing profiles as distributions")

A profile you built on one machine can be packaged as a **git repository** and installed with one command on another machine — your own workstation, a teammate's laptop, or a community user's environment. The shared package includes the SOUL, config, skills, cron jobs, and MCP connections. Credentials, memories, and sessions stay per-machine.

`# Install a whole agent from a git repohermes profile install github.com/you/research-bot --alias# Update later when the author ships a new version (keeps your memories + .env)hermes profile update research-bot`

See **[Profile Distributions: Share a Whole Agent](https://hermes-agent.nousresearch.com/docs/user-guide/profile-distributions)** for the full guide — authoring, publishing, update semantics, security model, and use cases.
