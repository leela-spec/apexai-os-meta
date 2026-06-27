# Apex Link Graph Summary

## Verdict

- Graph useful now: partial
- Main reason: deterministic process and package edges exist, but they are mostly encoded as YAML/path fields and prose sequence blocks rather than dense Markdown links or wikilinks.
- Recommended extraction phase: V1.5
- Need Obsidian app: no

## Summary

The current repo can already produce a useful file graph for LLM navigation if the extractor supports:

- explicit path strings,
- package manifest `file_list` / `supporting_files`,
- `canonical_source`, `script_path`, `hands_off_to`, `owns`, `does_not_own`,
- explicit arrow/sequence text,
- skill index entries in `.claude/Claude.md`.

A pure Obsidian-style parser that only reads `[text](path)` and `[[wikilinks]]` would undercount the graph heavily.

## Strong hubs

| Hub | Why |
|---|---|
| `.claude/Claude.md` | Defines core loop, skill index, artifact paths, present/missing skill status. |
| `.claude/skills/PrecapNextDay/Skill_precap-next-day.md` | Defines daily plan outputs, flow packets, prompt packs, dependency interfaces, FlowRecap handoff. |
| `.claude/skills/PrecapNextDay/precap-next-day-package-manifest.md` | Dense package file index with many explicit paths. |
| `.claude/skills/apex-kb/SKILL.md` | Defines KB modes, data layout, ownership, boundaries, handoffs to plan/session/sync. |
| `.claude/skills/apex-kb/package-manifest.md` | Dense KB file inventory and runtime script reference. |
| `.claude/skills/apex-sync/SKILL.md` | Script-backed deterministic sync boundary. |
| `.claude/skills/apex-session/SKILL.md` | Session mutation and handoff boundary. |

## Weak spots

- `FlowRecap` and `status-merge/APSU` are represented in loop/index references but are marked missing in the current `.claude/Claude.md` skill index.
- Many support paths are relative and would require path normalization.
- Wikilinks exist in repo/source snapshots, but not as the main Apex process graph mechanism.
- Markdown links appear less important than YAML-ish path references and package manifests.

## V1.5 output set

Recommended files:

```text
apex-meta/kb/claude-skill-design/manifests/link-graph.sample.json
apex-meta/kb/claude-skill-design/manifests/graph-summary.md
apex-meta/kb/claude-skill-design/manifests/process-flow-graph-audit.md
```

