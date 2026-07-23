Title: Agent Skills Overview - Agent Skills

URL Source: https://agentskills.io/

Published Time: Tue, 30 Jun 2026 18:25:54 GMT

Markdown Content:
A standardized way to give AI agents new capabilities and expertise.

## What are Agent Skills?

Agent Skills are a lightweight, open format for extending AI agent capabilities with specialized knowledge and workflows.At its core, a skill is a folder containing a `SKILL.md` file. This file includes metadata (`name` and `description`, at minimum) and instructions that tell an agent how to perform a specific task. Skills can also bundle scripts, reference materials, templates, and other resources.

```
my-skill/
├── SKILL.md          # Required: metadata + instructions
├── scripts/          # Optional: executable code
├── references/       # Optional: documentation
├── assets/           # Optional: templates, resources
└── ...               # Any additional files or directories
```

## Why Agent Skills?

Agents are increasingly capable, but often don’t have the context they need to do real work reliably. Skills solve this by packaging procedural knowledge and company-, team-, and user-specific context into portable, version-controlled folders that agents load on demand. This gives agents:

*   **Domain expertise**: Capture specialized knowledge — from legal review processes to data analysis pipelines to presentation formatting — as reusable instructions and resources.
*   **Repeatable workflows**: Turn multi-step tasks into consistent, auditable procedures.
*   **Cross-product reuse**: Build a skill once and use it across any skills-compatible agent.

## How do Agent Skills work?

Agents load skills through **progressive disclosure**, in three stages:

1.   **Discovery**: At startup, agents load only the name and description of each available skill, just enough to know when it might be relevant.
2.   **Activation**: When a task matches a skill’s description, the agent reads the full `SKILL.md` instructions into context.
3.   **Execution**: The agent follows the instructions, optionally executing bundled code or loading referenced files as needed.

Full instructions load only when a task calls for them, so agents can keep many skills on hand with only a small context footprint.

## Where can I use Agent Skills?

Agent Skills are supported by a large number of AI tools and agentic clients — see the [Client Showcase](https://agentskills.io/clients) to explore some of them!

[![Image 1: Laravel Boost](https://agentskills.io/images/logos/laravel-boost/boost-light-mode.svg)![Image 2: Laravel Boost](https://agentskills.io/images/logos/laravel-boost/boost-dark-mode.svg)](https://github.com/laravel/boost)

[![Image 3: Kiro](https://agentskills.io/images/logos/kiro/kiro-logo-light.svg)![Image 4: Kiro](https://agentskills.io/images/logos/kiro/kiro-logo-dark.svg)](https://kiro.dev/)

[![Image 5: OpenCode](https://agentskills.io/images/logos/opencode/opencode-wordmark-light.svg)![Image 6: OpenCode](https://agentskills.io/images/logos/opencode/opencode-wordmark-dark.svg)](https://opencode.ai/)

[![Image 7: Superconductor](https://agentskills.io/images/logos/superconductor/superconductor-wordmark-light.svg)![Image 8: Superconductor](https://agentskills.io/images/logos/superconductor/superconductor-wordmark-dark.svg)](https://superconductor.com/)

[![Image 9: Deep Code](https://agentskills.io/images/logos/deepcode/deepcode-logo-light.svg)![Image 10: Deep Code](https://agentskills.io/images/logos/deepcode/deepcode-logo-dark.svg)](https://deepcode.vegamo.cn/en)

[![Image 11: OpenAI Codex](https://agentskills.io/images/logos/oai-codex/OAI_Codex-Lockup_400px.svg)![Image 12: OpenAI Codex](https://agentskills.io/images/logos/oai-codex/OAI_Codex-Lockup_400px_Darkmode.svg)](https://developers.openai.com/codex)

[![Image 13: pi](https://agentskills.io/images/logos/pi/pi-logo-light.svg)![Image 14: pi](https://agentskills.io/images/logos/pi/pi-logo-dark.svg)](https://shittycodingagent.ai/)

[![Image 15: Emdash](https://agentskills.io/images/logos/emdash/emdash-logo-light.svg)![Image 16: Emdash](https://agentskills.io/images/logos/emdash/emdash-logo-dark.svg)](https://emdash.sh/)

[![Image 17: Spring AI](https://agentskills.io/images/logos/spring-ai/spring-ai-logo-light.svg)![Image 18: Spring AI](https://agentskills.io/images/logos/spring-ai/spring-ai-logo-dark.svg)](https://docs.spring.io/spring-ai/reference)

[![Image 19: Mux](https://agentskills.io/images/logos/mux/mux-editor-light.svg)![Image 20: Mux](https://agentskills.io/images/logos/mux/mux-editor-dark.svg)](https://mux.coder.com/)

[![Image 21: Mistral AI Vibe](https://agentskills.io/images/logos/mistral-vibe/vibe-logo_black.svg)![Image 22: Mistral AI Vibe](https://agentskills.io/images/logos/mistral-vibe/vibe-logo_white.svg)](https://github.com/mistralai/mistral-vibe)

[![Image 23: Snowflake Cortex Code](https://agentskills.io/images/logos/snowflake/snowflake-logo-light.svg)![Image 24: Snowflake Cortex Code](https://agentskills.io/images/logos/snowflake/snowflake-logo-dark.svg)](https://docs.snowflake.com/en/user-guide/cortex-code/cortex-code)

[![Image 25: Claude Code](https://agentskills.io/images/logos/claude-code/Claude-Code-logo-Slate.svg)![Image 26: Claude Code](https://agentskills.io/images/logos/claude-code/Claude-Code-logo-Ivory.svg)](https://claude.ai/code)

[![Image 27: Cursor](https://agentskills.io/images/logos/cursor/LOCKUP_HORIZONTAL_2D_LIGHT.svg)![Image 28: Cursor](https://agentskills.io/images/logos/cursor/LOCKUP_HORIZONTAL_2D_DARK.svg)](https://cursor.com/)

[![Image 29: Workshop](https://agentskills.io/images/logos/workshop/workshop-logo-light.svg)![Image 30: Workshop](https://agentskills.io/images/logos/workshop/workshop-logo-dark.svg)](https://workshop.ai/)

[![Image 31: Gemini CLI](https://agentskills.io/images/logos/gemini-cli/gemini-cli-logo_light.svg)![Image 32: Gemini CLI](https://agentskills.io/images/logos/gemini-cli/gemini-cli-logo_dark.svg)](https://geminicli.com/)

[![Image 33: Roo Code](https://agentskills.io/images/logos/roo-code/roo-code-logo-black.svg)![Image 34: Roo Code](https://agentskills.io/images/logos/roo-code/roo-code-logo-white.svg)](https://roocode.com/)

[![Image 35: Goose](https://agentskills.io/images/logos/goose/goose-logo-black.png)![Image 36: Goose](https://agentskills.io/images/logos/goose/goose-logo-white.png)](https://block.github.io/goose/)

[![Image 37: TRAE](https://agentskills.io/images/logos/trae/trae-logo-lightmode.svg)![Image 38: TRAE](https://agentskills.io/images/logos/trae/trae-logo-darkmode.svg)](https://trae.ai/)

[![Image 39: Databricks Genie Code](https://agentskills.io/images/logos/databricks/databricks-logo-light.svg)![Image 40: Databricks Genie Code](https://agentskills.io/images/logos/databricks/databricks-logo-dark.svg)](https://databricks.com/)

[![Image 41: VT Code](https://agentskills.io/images/logos/vtcode/vt_code_light.svg)![Image 42: VT Code](https://agentskills.io/images/logos/vtcode/vt_code_dark.svg)](https://github.com/vinhnx/vtcode)

[![Image 43: Amp](https://agentskills.io/images/logos/amp/amp-logo-light.svg)![Image 44: Amp](https://agentskills.io/images/logos/amp/amp-logo-dark.svg)](https://ampcode.com/)

[![Image 45: OpenHands](https://agentskills.io/images/logos/openhands/openhands-logo-light.svg)![Image 46: OpenHands](https://agentskills.io/images/logos/openhands/openhands-logo-dark.svg)](https://openhands.dev/)

[![Image 47: Command Code](https://agentskills.io/images/logos/command-code/command-code-logo-for-light.svg)![Image 48: Command Code](https://agentskills.io/images/logos/command-code/command-code-logo-for-dark.svg)](https://commandcode.ai/)

[![Image 49: Firebender](https://agentskills.io/images/logos/firebender/firebender-wordmark-light.svg)![Image 50: Firebender](https://agentskills.io/images/logos/firebender/firebender-wordmark-dark.svg)](https://firebender.com/)

[![Image 51: Piebald](https://agentskills.io/images/logos/piebald/Piebald_wordmark_light.svg)![Image 52: Piebald](https://agentskills.io/images/logos/piebald/Piebald_wordmark_dark.svg)](https://piebald.ai/)

[![Image 53: Qodo](https://agentskills.io/images/logos/qodo/qodo-logo-light.png)![Image 54: Qodo](https://agentskills.io/images/logos/qodo/qodo-logo-dark.svg)](https://www.qodo.ai/)

[![Image 55: Agentman](https://agentskills.io/images/logos/agentman/agentman-wordmark-light.svg)![Image 56: Agentman](https://agentskills.io/images/logos/agentman/agentman-wordmark-dark.svg)](https://agentman.ai/)

[![Image 57: nanobot](https://agentskills.io/images/logos/nanobot/nanobot-logo-light.png)![Image 58: nanobot](https://agentskills.io/images/logos/nanobot/nanobot-logo-dark.png)](https://nanobot.wiki/)

[![Image 59: Junie](https://agentskills.io/images/logos/junie/junie-logo-on-white.svg)![Image 60: Junie](https://agentskills.io/images/logos/junie/junie-logo-on-dark.svg)](https://junie.jetbrains.com/)

[![Image 61: Vita](https://agentskills.io/images/logos/vita/logo-horizontal-light.svg)![Image 62: Vita](https://agentskills.io/images/logos/vita/logo-horizontal-dark.svg)](https://www.vita-ai.net/)

[![Image 63: bub](https://agentskills.io/images/logos/bub/bub-light.svg)![Image 64: bub](https://agentskills.io/images/logos/bub/bub-dark.svg)](https://bub.build/)

[![Image 65: Claude](https://agentskills.io/images/logos/claude-ai/Claude-logo-Slate.svg)![Image 66: Claude](https://agentskills.io/images/logos/claude-ai/Claude-logo-Ivory.svg)](https://claude.ai/)

[![Image 67: Letta](https://agentskills.io/images/logos/letta/Letta-logo-RGB_OffBlackonTransparent.svg)![Image 68: Letta](https://agentskills.io/images/logos/letta/Letta-logo-RGB_GreyonTransparent.svg)](https://www.letta.com/)

[![Image 69: Tabnine](https://agentskills.io/images/logos/tabnine/tabnine-logo-light.svg)![Image 70: Tabnine](https://agentskills.io/images/logos/tabnine/tabnine-logo-dark.svg)](https://www.tabnine.com/)

[![Image 71: Ona](https://agentskills.io/images/logos/ona/ona-wordmark-light.svg)![Image 72: Ona](https://agentskills.io/images/logos/ona/ona-wordmark-dark.svg)](https://ona.com/)

[![Image 73: Factory](https://agentskills.io/images/logos/factory/factory-logo-light.svg)![Image 74: Factory](https://agentskills.io/images/logos/factory/factory-logo-dark.svg)](https://factory.ai/)

[![Image 75: Google AI Edge Gallery](https://agentskills.io/images/logos/google-ai-edge-gallery/google-ai-edge-gallery-light.svg)![Image 76: Google AI Edge Gallery](https://agentskills.io/images/logos/google-ai-edge-gallery/google-ai-edge-gallery-dark.svg)](https://github.com/google-ai-edge/gallery)

[![Image 77: Autohand Code CLI](https://agentskills.io/images/logos/autohand/autohand-light.svg)![Image 78: Autohand Code CLI](https://agentskills.io/images/logos/autohand/autohand-dark.svg)](https://autohand.ai/)

[![Image 79: GitHub Copilot](https://agentskills.io/images/logos/github/GitHub_Lockup_Dark.svg)![Image 80: GitHub Copilot](https://agentskills.io/images/logos/github/GitHub_Lockup_Light.svg)](https://github.com/)

[![Image 81: fast-agent](https://agentskills.io/images/logos/fast-agent/fast-agent-light.svg)![Image 82: fast-agent](https://agentskills.io/images/logos/fast-agent/fast-agent-dark.svg)](https://fast-agent.ai/)

[![Image 83: VS Code](https://agentskills.io/images/logos/vscode/vscode.svg)![Image 84: VS Code](https://agentskills.io/images/logos/vscode/vscode-alt.svg)](https://code.visualstudio.com/)

[![Image 85: Laravel Boost](https://agentskills.io/images/logos/laravel-boost/boost-light-mode.svg)![Image 86: Laravel Boost](https://agentskills.io/images/logos/laravel-boost/boost-dark-mode.svg)](https://github.com/laravel/boost)

[![Image 87: Kiro](https://agentskills.io/images/logos/kiro/kiro-logo-light.svg)![Image 88: Kiro](https://agentskills.io/images/logos/kiro/kiro-logo-dark.svg)](https://kiro.dev/)

[![Image 89: OpenCode](https://agentskills.io/images/logos/opencode/opencode-wordmark-light.svg)![Image 90: OpenCode](https://agentskills.io/images/logos/opencode/opencode-wordmark-dark.svg)](https://opencode.ai/)

[![Image 91: Superconductor](https://agentskills.io/images/logos/superconductor/superconductor-wordmark-light.svg)![Image 92: Superconductor](https://agentskills.io/images/logos/superconductor/superconductor-wordmark-dark.svg)](https://superconductor.com/)

[![Image 93: Deep Code](https://agentskills.io/images/logos/deepcode/deepcode-logo-light.svg)![Image 94: Deep Code](https://agentskills.io/images/logos/deepcode/deepcode-logo-dark.svg)](https://deepcode.vegamo.cn/en)

[![Image 95: OpenAI Codex](https://agentskills.io/images/logos/oai-codex/OAI_Codex-Lockup_400px.svg)![Image 96: OpenAI Codex](https://agentskills.io/images/logos/oai-codex/OAI_Codex-Lockup_400px_Darkmode.svg)](https://developers.openai.com/codex)

[![Image 97: pi](https://agentskills.io/images/logos/pi/pi-logo-light.svg)![Image 98: pi](https://agentskills.io/images/logos/pi/pi-logo-dark.svg)](https://shittycodingagent.ai/)

[![Image 99: Emdash](https://agentskills.io/images/logos/emdash/emdash-logo-light.svg)![Image 100: Emdash](https://agentskills.io/images/logos/emdash/emdash-logo-dark.svg)](https://emdash.sh/)

[![Image 101: Spring AI](https://agentskills.io/images/logos/spring-ai/spring-ai-logo-light.svg)![Image 102: Spring AI](https://agentskills.io/images/logos/spring-ai/spring-ai-logo-dark.svg)](https://docs.spring.io/spring-ai/reference)

[![Image 103: Mux](https://agentskills.io/images/logos/mux/mux-editor-light.svg)![Image 104: Mux](https://agentskills.io/images/logos/mux/mux-editor-dark.svg)](https://mux.coder.com/)

[![Image 105: Mistral AI Vibe](https://agentskills.io/images/logos/mistral-vibe/vibe-logo_black.svg)![Image 106: Mistral AI Vibe](https://agentskills.io/images/logos/mistral-vibe/vibe-logo_white.svg)](https://github.com/mistralai/mistral-vibe)

[![Image 107: Snowflake Cortex Code](https://agentskills.io/images/logos/snowflake/snowflake-logo-light.svg)![Image 108: Snowflake Cortex Code](https://agentskills.io/images/logos/snowflake/snowflake-logo-dark.svg)](https://docs.snowflake.com/en/user-guide/cortex-code/cortex-code)

[![Image 109: Claude Code](https://agentskills.io/images/logos/claude-code/Claude-Code-logo-Slate.svg)![Image 110: Claude Code](https://agentskills.io/images/logos/claude-code/Claude-Code-logo-Ivory.svg)](https://claude.ai/code)

[![Image 111: Cursor](https://agentskills.io/images/logos/cursor/LOCKUP_HORIZONTAL_2D_LIGHT.svg)![Image 112: Cursor](https://agentskills.io/images/logos/cursor/LOCKUP_HORIZONTAL_2D_DARK.svg)](https://cursor.com/)

[![Image 113: Workshop](https://agentskills.io/images/logos/workshop/workshop-logo-light.svg)![Image 114: Workshop](https://agentskills.io/images/logos/workshop/workshop-logo-dark.svg)](https://workshop.ai/)

[![Image 115: Gemini CLI](https://agentskills.io/images/logos/gemini-cli/gemini-cli-logo_light.svg)![Image 116: Gemini CLI](https://agentskills.io/images/logos/gemini-cli/gemini-cli-logo_dark.svg)](https://geminicli.com/)

[![Image 117: Roo Code](https://agentskills.io/images/logos/roo-code/roo-code-logo-black.svg)![Image 118: Roo Code](https://agentskills.io/images/logos/roo-code/roo-code-logo-white.svg)](https://roocode.com/)

[![Image 119: Goose](https://agentskills.io/images/logos/goose/goose-logo-black.png)![Image 120: Goose](https://agentskills.io/images/logos/goose/goose-logo-white.png)](https://block.github.io/goose/)

[![Image 121: TRAE](https://agentskills.io/images/logos/trae/trae-logo-lightmode.svg)![Image 122: TRAE](https://agentskills.io/images/logos/trae/trae-logo-darkmode.svg)](https://trae.ai/)

[![Image 123: Databricks Genie Code](https://agentskills.io/images/logos/databricks/databricks-logo-light.svg)![Image 124: Databricks Genie Code](https://agentskills.io/images/logos/databricks/databricks-logo-dark.svg)](https://databricks.com/)

[![Image 125: VT Code](https://agentskills.io/images/logos/vtcode/vt_code_light.svg)![Image 126: VT Code](https://agentskills.io/images/logos/vtcode/vt_code_dark.svg)](https://github.com/vinhnx/vtcode)

[![Image 127: Amp](https://agentskills.io/images/logos/amp/amp-logo-light.svg)![Image 128: Amp](https://agentskills.io/images/logos/amp/amp-logo-dark.svg)](https://ampcode.com/)

[![Image 129: OpenHands](https://agentskills.io/images/logos/openhands/openhands-logo-light.svg)![Image 130: OpenHands](https://agentskills.io/images/logos/openhands/openhands-logo-dark.svg)](https://openhands.dev/)

[![Image 131: Command Code](https://agentskills.io/images/logos/command-code/command-code-logo-for-light.svg)![Image 132: Command Code](https://agentskills.io/images/logos/command-code/command-code-logo-for-dark.svg)](https://commandcode.ai/)

[![Image 133: Firebender](https://agentskills.io/images/logos/firebender/firebender-wordmark-light.svg)![Image 134: Firebender](https://agentskills.io/images/logos/firebender/firebender-wordmark-dark.svg)](https://firebender.com/)

[![Image 135: Piebald](https://agentskills.io/images/logos/piebald/Piebald_wordmark_light.svg)![Image 136: Piebald](https://agentskills.io/images/logos/piebald/Piebald_wordmark_dark.svg)](https://piebald.ai/)

[![Image 137: Qodo](https://agentskills.io/images/logos/qodo/qodo-logo-light.png)![Image 138: Qodo](https://agentskills.io/images/logos/qodo/qodo-logo-dark.svg)](https://www.qodo.ai/)

[![Image 139: Agentman](https://agentskills.io/images/logos/agentman/agentman-wordmark-light.svg)![Image 140: Agentman](https://agentskills.io/images/logos/agentman/agentman-wordmark-dark.svg)](https://agentman.ai/)

[![Image 141: nanobot](https://agentskills.io/images/logos/nanobot/nanobot-logo-light.png)![Image 142: nanobot](https://agentskills.io/images/logos/nanobot/nanobot-logo-dark.png)](https://nanobot.wiki/)

[![Image 143: Junie](https://agentskills.io/images/logos/junie/junie-logo-on-white.svg)![Image 144: Junie](https://agentskills.io/images/logos/junie/junie-logo-on-dark.svg)](https://junie.jetbrains.com/)

[![Image 145: Vita](https://agentskills.io/images/logos/vita/logo-horizontal-light.svg)![Image 146: Vita](https://agentskills.io/images/logos/vita/logo-horizontal-dark.svg)](https://www.vita-ai.net/)

[![Image 147: bub](https://agentskills.io/images/logos/bub/bub-light.svg)![Image 148: bub](https://agentskills.io/images/logos/bub/bub-dark.svg)](https://bub.build/)

[![Image 149: Claude](https://agentskills.io/images/logos/claude-ai/Claude-logo-Slate.svg)![Image 150: Claude](https://agentskills.io/images/logos/claude-ai/Claude-logo-Ivory.svg)](https://claude.ai/)

[![Image 151: Letta](https://agentskills.io/images/logos/letta/Letta-logo-RGB_OffBlackonTransparent.svg)![Image 152: Letta](https://agentskills.io/images/logos/letta/Letta-logo-RGB_GreyonTransparent.svg)](https://www.letta.com/)

[![Image 153: Tabnine](https://agentskills.io/images/logos/tabnine/tabnine-logo-light.svg)![Image 154: Tabnine](https://agentskills.io/images/logos/tabnine/tabnine-logo-dark.svg)](https://www.tabnine.com/)

[![Image 155: Ona](https://agentskills.io/images/logos/ona/ona-wordmark-light.svg)![Image 156: Ona](https://agentskills.io/images/logos/ona/ona-wordmark-dark.svg)](https://ona.com/)

[![Image 157: Factory](https://agentskills.io/images/logos/factory/factory-logo-light.svg)![Image 158: Factory](https://agentskills.io/images/logos/factory/factory-logo-dark.svg)](https://factory.ai/)

[![Image 159: Google AI Edge Gallery](https://agentskills.io/images/logos/google-ai-edge-gallery/google-ai-edge-gallery-light.svg)![Image 160: Google AI Edge Gallery](https://agentskills.io/images/logos/google-ai-edge-gallery/google-ai-edge-gallery-dark.svg)](https://github.com/google-ai-edge/gallery)

[![Image 161: Autohand Code CLI](https://agentskills.io/images/logos/autohand/autohand-light.svg)![Image 162: Autohand Code CLI](https://agentskills.io/images/logos/autohand/autohand-dark.svg)](https://autohand.ai/)

[![Image 163: GitHub Copilot](https://agentskills.io/images/logos/github/GitHub_Lockup_Dark.svg)![Image 164: GitHub Copilot](https://agentskills.io/images/logos/github/GitHub_Lockup_Light.svg)](https://github.com/)

[![Image 165: fast-agent](https://agentskills.io/images/logos/fast-agent/fast-agent-light.svg)![Image 166: fast-agent](https://agentskills.io/images/logos/fast-agent/fast-agent-dark.svg)](https://fast-agent.ai/)

[![Image 167: VS Code](https://agentskills.io/images/logos/vscode/vscode.svg)![Image 168: VS Code](https://agentskills.io/images/logos/vscode/vscode-alt.svg)](https://code.visualstudio.com/)

## Open development

The Agent Skills format was originally developed by [Anthropic](https://www.anthropic.com/), released as an open standard, and has been adopted by a growing number of agent products. The standard is open to contributions from the broader ecosystem.Come join the discussion on [GitHub](https://github.com/agentskills/agentskills) or [Discord](https://discord.gg/MKPE9g8aUy)!

## Get started with Agent Skills
