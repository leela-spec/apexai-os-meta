# Memory Architecture

> Companion note: this file explains the local memory layout only. It is not `SSOT`, not `OpState`, not `Session Export`, and not project-interface authority.

The memory area uses a lightweight local index plus bounded drill-down files.

- `user/memory/MEMORY.md` is the main local memory index.
- `user/memory/context/active.md` is the current local active-context snapshot.
- `user/memory/MISTAKES.md` holds recurring mistake patterns and standing corrections.
- `user/memory/memory-daily/YYYY-MM-DD.md` holds dated local journals for date-specific detail.
- Additional local detail files may exist, but they stay subordinate to the lightweight index.

Keep durable local context segmented and keep the main index concise.

For formal control and trace surfaces, use:
- `managed/rules/PROJECT_INTERFACE_CONTRACT.md` for project-interface authority
- `managed/rituals/SESSION_EXPORT_PROTOCOL.md` for session trace authority
- `managed/rituals/NIGHT_PLANNING_PROTOCOL.md` for cross-session synthesis authority
