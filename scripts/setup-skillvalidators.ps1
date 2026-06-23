# ============================================================
# download-hermes-docs.ps1
# Downloads ALL Hermes Agent docs as clean Markdown files.
# No extra tools needed — uses only built-in PowerShell (Invoke-WebRequest).
# Output: a folder called hermes-docs on your Desktop
# ============================================================

$base = "$env:USERPROFILE\Desktop\hermes-docs"
$jina = "https://r.jina.ai"

# Create all needed subfolders
New-Item -ItemType Directory -Force -Path "$base\getting-started" | Out-Null
New-Item -ItemType Directory -Force -Path "$base\guides" | Out-Null
New-Item -ItemType Directory -Force -Path "$base\integrations" | Out-Null
New-Item -ItemType Directory -Force -Path "$base\reference" | Out-Null
New-Item -ItemType Directory -Force -Path "$base\user-guide" | Out-Null
New-Item -ItemType Directory -Force -Path "$base\user-guide\features" | Out-Null
New-Item -ItemType Directory -Force -Path "$base\user-guide\messaging" | Out-Null

Write-Host "Downloading 85 pages to $base ..."

Write-Host "  [1/85] getting-started/installation"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/getting-started/installation" -OutFile "$base\getting-started\installation.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [2/85] getting-started/quickstart"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/getting-started/quickstart" -OutFile "$base\getting-started\quickstart.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [3/85] getting-started/learning-path"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/getting-started/learning-path" -OutFile "$base\getting-started\learning-path.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [4/85] getting-started/updating"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/getting-started/updating" -OutFile "$base\getting-started\updating.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [5/85] getting-started/termux"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/getting-started/termux" -OutFile "$base\getting-started\termux.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [6/85] getting-started/nix-setup"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/getting-started/nix-setup" -OutFile "$base\getting-started\nix-setup.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [7/85] user-guide/cli"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/cli" -OutFile "$base\user-guide\cli.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [8/85] user-guide/tui"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/tui" -OutFile "$base\user-guide\tui.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [9/85] user-guide/configuration"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/configuration" -OutFile "$base\user-guide\configuration.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [10/85] user-guide/configuring-models"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/configuring-models" -OutFile "$base\user-guide\configuring-models.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [11/85] user-guide/sessions"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/sessions" -OutFile "$base\user-guide\sessions.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [12/85] user-guide/profiles"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/profiles" -OutFile "$base\user-guide\profiles.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [13/85] user-guide/git-worktrees"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/git-worktrees" -OutFile "$base\user-guide\git-worktrees.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [14/85] user-guide/docker"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/docker" -OutFile "$base\user-guide\docker.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [15/85] user-guide/security"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/security" -OutFile "$base\user-guide\security.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [16/85] user-guide/checkpoints-and-rollback"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/checkpoints-and-rollback" -OutFile "$base\user-guide\checkpoints-and-rollback.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [17/85] user-guide/features/overview"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/features/overview" -OutFile "$base\user-guide\features\overview.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [18/85] user-guide/features/tools"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/features/tools" -OutFile "$base\user-guide\features\tools.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [19/85] user-guide/features/skills"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/features/skills" -OutFile "$base\user-guide\features\skills.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [20/85] user-guide/features/curator"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/features/curator" -OutFile "$base\user-guide\features\curator.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [21/85] user-guide/features/memory"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/features/memory" -OutFile "$base\user-guide\features\memory.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [22/85] user-guide/features/memory-providers"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/features/memory-providers" -OutFile "$base\user-guide\features\memory-providers.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [23/85] user-guide/features/context-files"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files" -OutFile "$base\user-guide\features\context-files.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [24/85] user-guide/features/context-references"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references" -OutFile "$base\user-guide\features\context-references.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [25/85] user-guide/features/personality"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/features/personality" -OutFile "$base\user-guide\features\personality.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [26/85] user-guide/features/plugins"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins" -OutFile "$base\user-guide\features\plugins.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [27/85] user-guide/features/built-in-plugins"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/features/built-in-plugins" -OutFile "$base\user-guide\features\built-in-plugins.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [28/85] user-guide/features/cron"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/features/cron" -OutFile "$base\user-guide\features\cron.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [29/85] user-guide/features/delegation"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation" -OutFile "$base\user-guide\features\delegation.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [30/85] user-guide/features/kanban"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban" -OutFile "$base\user-guide\features\kanban.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [31/85] user-guide/features/kanban-tutorial"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban-tutorial" -OutFile "$base\user-guide\features\kanban-tutorial.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [32/85] user-guide/features/goals"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/features/goals" -OutFile "$base\user-guide\features\goals.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [33/85] user-guide/features/code-execution"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution" -OutFile "$base\user-guide\features\code-execution.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [34/85] user-guide/features/hooks"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks" -OutFile "$base\user-guide\features\hooks.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [35/85] user-guide/features/batch-processing"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/features/batch-processing" -OutFile "$base\user-guide\features\batch-processing.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [36/85] user-guide/features/voice-mode"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/features/voice-mode" -OutFile "$base\user-guide\features\voice-mode.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [37/85] user-guide/features/browser"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/features/browser" -OutFile "$base\user-guide\features\browser.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [38/85] user-guide/features/vision"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/features/vision" -OutFile "$base\user-guide\features\vision.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [39/85] user-guide/features/image-generation"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/features/image-generation" -OutFile "$base\user-guide\features\image-generation.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [40/85] user-guide/features/tts"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/features/tts" -OutFile "$base\user-guide\features\tts.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [41/85] user-guide/messaging/index"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/messaging/index" -OutFile "$base\user-guide\messaging\index.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [42/85] user-guide/messaging/telegram"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/messaging/telegram" -OutFile "$base\user-guide\messaging\telegram.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [43/85] user-guide/messaging/discord"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/messaging/discord" -OutFile "$base\user-guide\messaging\discord.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [44/85] user-guide/messaging/slack"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/messaging/slack" -OutFile "$base\user-guide\messaging\slack.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [45/85] user-guide/messaging/whatsapp"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/messaging/whatsapp" -OutFile "$base\user-guide\messaging\whatsapp.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [46/85] user-guide/messaging/signal"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/messaging/signal" -OutFile "$base\user-guide\messaging\signal.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [47/85] user-guide/messaging/email"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/messaging/email" -OutFile "$base\user-guide\messaging\email.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [48/85] user-guide/messaging/sms"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/messaging/sms" -OutFile "$base\user-guide\messaging\sms.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [49/85] user-guide/messaging/matrix"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/messaging/matrix" -OutFile "$base\user-guide\messaging\matrix.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [50/85] user-guide/messaging/mattermost"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/messaging/mattermost" -OutFile "$base\user-guide\messaging\mattermost.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [51/85] user-guide/messaging/homeassistant"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/messaging/homeassistant" -OutFile "$base\user-guide\messaging\homeassistant.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [52/85] user-guide/messaging/webhooks"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/messaging/webhooks" -OutFile "$base\user-guide\messaging\webhooks.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [53/85] integrations/index"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/integrations/index" -OutFile "$base\integrations\index.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [54/85] integrations/providers"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/integrations/providers" -OutFile "$base\integrations\providers.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [55/85] user-guide/features/mcp"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp" -OutFile "$base\user-guide\features\mcp.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [56/85] user-guide/features/acp"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/features/acp" -OutFile "$base\user-guide\features\acp.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [57/85] user-guide/features/api-server"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server" -OutFile "$base\user-guide\features\api-server.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [58/85] user-guide/features/honcho"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/features/honcho" -OutFile "$base\user-guide\features\honcho.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [59/85] user-guide/features/provider-routing"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing" -OutFile "$base\user-guide\features\provider-routing.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [60/85] user-guide/features/fallback-providers"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/features/fallback-providers" -OutFile "$base\user-guide\features\fallback-providers.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [61/85] user-guide/features/credential-pools"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/user-guide/features/credential-pools" -OutFile "$base\user-guide\features\credential-pools.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [62/85] guides/tips"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/guides/tips" -OutFile "$base\guides\tips.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [63/85] guides/local-llm-on-mac"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/guides/local-llm-on-mac" -OutFile "$base\guides\local-llm-on-mac.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [64/85] guides/daily-briefing-bot"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot" -OutFile "$base\guides\daily-briefing-bot.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [65/85] guides/team-telegram-assistant"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/guides/team-telegram-assistant" -OutFile "$base\guides\team-telegram-assistant.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [66/85] guides/python-library"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/guides/python-library" -OutFile "$base\guides\python-library.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [67/85] guides/use-mcp-with-hermes"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/guides/use-mcp-with-hermes" -OutFile "$base\guides\use-mcp-with-hermes.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [68/85] guides/use-voice-mode-with-hermes"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/guides/use-voice-mode-with-hermes" -OutFile "$base\guides\use-voice-mode-with-hermes.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [69/85] guides/use-soul-with-hermes"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/guides/use-soul-with-hermes" -OutFile "$base\guides\use-soul-with-hermes.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [70/85] guides/build-a-hermes-plugin"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin" -OutFile "$base\guides\build-a-hermes-plugin.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [71/85] guides/automate-with-cron"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/guides/automate-with-cron" -OutFile "$base\guides\automate-with-cron.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [72/85] guides/work-with-skills"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/guides/work-with-skills" -OutFile "$base\guides\work-with-skills.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [73/85] guides/delegation-patterns"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/guides/delegation-patterns" -OutFile "$base\guides\delegation-patterns.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [74/85] guides/github-pr-review-agent"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/guides/github-pr-review-agent" -OutFile "$base\guides\github-pr-review-agent.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [75/85] reference/cli-commands"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/reference/cli-commands" -OutFile "$base\reference\cli-commands.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [76/85] reference/slash-commands"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/reference/slash-commands" -OutFile "$base\reference\slash-commands.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [77/85] reference/profile-commands"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/reference/profile-commands" -OutFile "$base\reference\profile-commands.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [78/85] reference/environment-variables"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/reference/environment-variables" -OutFile "$base\reference\environment-variables.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [79/85] reference/tools-reference"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/reference/tools-reference" -OutFile "$base\reference\tools-reference.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [80/85] reference/toolsets-reference"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/reference/toolsets-reference" -OutFile "$base\reference\toolsets-reference.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [81/85] reference/mcp-config-reference"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/reference/mcp-config-reference" -OutFile "$base\reference\mcp-config-reference.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [82/85] reference/model-catalog"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/reference/model-catalog" -OutFile "$base\reference\model-catalog.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [83/85] reference/skills-catalog"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/reference/skills-catalog" -OutFile "$base\reference\skills-catalog.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [84/85] reference/optional-skills-catalog"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog" -OutFile "$base\reference\optional-skills-catalog.md" -UseBasicParsing
Start-Sleep -Seconds 1

Write-Host "  [85/85] reference/faq"
Invoke-WebRequest -Uri "$jina/https://hermes-agent.nousresearch.com/docs/reference/faq" -OutFile "$base\reference\faq.md" -UseBasicParsing
Start-Sleep -Seconds 1

# Save the master index
Invoke-WebRequest -Uri "https://hermes-agent.nousresearch.com/docs/llms.txt" -OutFile "$base\INDEX.txt" -UseBasicParsing

Write-Host ""
Write-Host "Done! All files saved to: $base"
$count = (Get-ChildItem -Path $base -Recurse -Filter "*.md").Count
Write-Host "$count markdown files downloaded."
Write-Host "Opening folder..."
explorer.exe $base