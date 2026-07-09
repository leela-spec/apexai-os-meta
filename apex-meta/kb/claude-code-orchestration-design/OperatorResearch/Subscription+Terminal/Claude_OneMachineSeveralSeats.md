**Confirmed: No hardware/machine lock exists in Claude Code.** Anthropic imposes no "one seat per machine" restriction — multiple accounts can run simultaneously on one laptop. The mechanism is well-documented and widely used.

## Core Mechanism: `CLAUDE_CONFIG_DIR`

Claude Code stores all auth, config, and session data in a single directory (default: `~/.claude`). By overriding the env var `CLAUDE_CONFIG_DIR`, each account gets a fully isolated environment.[blog.codeminer42](https://blog.codeminer42.com/ai-tip-running-two-claude-code-accounts/)

**Setup (zsh/bash):**

bash

`# 1. Create dirs per seat/account mkdir ~/.claude-account1 ~/.claude-account2 ~/.claude-account3 # 2. Add aliases to ~/.zshrc alias cc1='CLAUDE_CONFIG_DIR=~/.claude-account1 claude' alias cc2='CLAUDE_CONFIG_DIR=~/.claude-account2 claude' alias cc3='CLAUDE_CONFIG_DIR=~/.claude-account3 claude' # 3. Auth each account once cc1 auth login   # opens browser OAuth, saves to account1 dir cc2 auth login cc3 auth login # 4. Reload shell source ~/.zshrc`

After setup: run `cc1`, `cc2`, `cc3` in separate terminal tabs — all **simultaneously**, each with its own session, usage quota, and project context.gist.github+1

## Enterprise Seat Behavior

- Each Claude Code seat is tied to a **user account (email)**, not a machine or MAC address[support.claude](https://support.claude.com/en/articles/11845131-using-claude-code-with-your-team-or-enterprise-plan)
    
- Enterprise seats authenticate via **OAuth token** — the token lives in the config dir, not in hardware[gist.github](https://gist.github.com/fortunto2/b326e4727e32f9af1742f0710dcc5f75)
    
- Anthropic explicitly supports `/login` switching within a single install: `run /login to select a different login method`[support.claude](https://support.claude.com/en/articles/11845131-using-claude-code-with-your-team-or-enterprise-plan)
    
- No IP lock, no device fingerprinting documented anywhere in Anthropic's enterprise terms[support.claude](https://support.claude.com/en/articles/11845131-using-claude-code-with-your-team-or-enterprise-plan)
    

## Tooling Options (Beyond DIY)

|Tool|Method|Simultaneous?|
|---|---|---|
|`CLAUDE_CONFIG_DIR` aliases|Manual shell aliases|✅ Yes|
|`claude-switch` / `ccs`|CLI wrapper, named profiles|✅ Yes [claudeswitch](https://claudeswitch.dev)|
|`cc-account-switcher`|Script, sequential switch|⚠️ One at a time [github](https://github.com/ming86/cc-account-switcher)|
|`direnv` + per-project `.envrc`|Auto-switches by folder|✅ Yes [gist.github](https://gist.github.com/fortunto2/b326e4727e32f9af1742f0710dcc5f75)|

## Your Use Case (5 Seats, 1 Laptop)

- **2-3 seats for yourself** (e.g. personal, work-project-A, work-project-B) → use `direnv` with per-project `.envrc` so switching is **automatic by folder**harryy+1
    
- **2-3 seats for friends** → they log in from their own machines normally; you could also hold their config dirs locally if needed
    
- The `claude setup-token` command generates **long-lived OAuth tokens** that won't expire on every refresh — store per-account, reference via env var[gist.github](https://gist.github.com/fortunto2/b326e4727e32f9af1742f0710dcc5f75)
    

Your instinct is correct — this is standard, well-supported behavior with no machine-level restriction. The `CLAUDE_CONFIG_DIR` pattern is the canonical solution, and the ecosystem already has multiple polished CLI tools built around it.