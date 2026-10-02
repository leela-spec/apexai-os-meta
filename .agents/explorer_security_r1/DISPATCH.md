# Dispatch: Explorer Security (explorer_security_r1)
Assigned task: Benchmark workspace isolation options against OWASP Top 10 for AI Agents, analyze context bleeding & persona protection.

## 2026-09-22T10:17:33Z
You are explorer_security_r1, a specialized Security & Isolation Explorer.
Your working directory is: C:\GitDev\apexai-os-meta\.agents\explorer_security_r1
The authoritative user request is in: C:\GitDev\apexai-os-meta\.agents\ORIGINAL_REQUEST.md (under section ## 2026-09-22T10:15:42Z). Read this file first.

Mission:
Evaluate the architectural options for isolating AI agent workspaces, instruction files (AGENTS.md, SOUL.md), and Docker environments between Community Operations (Safer Space e.V. / Equinox / @LikasSlave_bot) and Private Business, with primary focus on Security, Zero Context Bleeding, and OWASP Top 10 for AI Agents.

Key Investigations:
1. Benchmark 4 architectural options:
   - Option 1: Subfolder Separation inside Repo (ki-basis/community/ vs ki-basis/private/, each opened as its own Antigravity workspace root).
   - Option 2: Decoupled Standalone Directories outside Repo (C:\GitDev\lika-community\ vs C:\GitDev\private-business\).
   - Option 3: Dynamic Workspace Profile / Environment Switching Protocols.
   - Option 4: Git Worktrees / Multi-root Workspaces.
2. Evaluate against OWASP Top 10 for AI Agents:
   - ASI-01 Prompt Injection / Cross-Tenant Contamination: Can external input from Telegram or community files leak into private context or prompt private actions?
   - ASI-02 Insecure Output Handling.
   - ASI-06 Sensitive Information Disclosure: Context bleeding, persona leakage, financial/business confidentiality.
   - ASI-07 Insecure Plugin / Tool Design: Skill execution isolation (equinox-intake vs executive/financial skills).
   - ASI-08 Vector/Memory Contamination: Shared session databases, RAG indices, or memory caches.
3. Hermes persona and instruction isolation:
   - Community: dedicated @LikasSlave_bot persona (SOUL.md), equinox-intake skill, Telegram polling enabled, Port Band 908x.
   - Private: dedicated executive business/financial persona (SOUL.md), Telegram disabled, Port Band 808x.
   - Ensure neither container mounts shared persona files, shared skill folders, or shared workspace volumes.
4. Synthesize your evaluation with a scoring matrix across Isolation, Simplicity, Token Efficiency, and Fragility.

Deliverable:
Write a comprehensive, evidence-backed report to C:\GitDev\apexai-os-meta\.agents\explorer_security_r1\handoff.md.
When finished, send a message to your parent orchestrator with a summary of your findings and the path to your handoff file.
