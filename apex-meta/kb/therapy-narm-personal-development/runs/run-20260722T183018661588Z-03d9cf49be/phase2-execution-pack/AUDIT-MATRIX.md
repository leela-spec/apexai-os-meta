# Phase 2 audit matrix

| Requirement | Earlier behavior | Corrected contract | Verification |
|---|---|---|---|
| Whole-run execution | One `continue` action at a time | `drive` runs deterministic actions to the next semantic or terminal boundary | CLI and lifecycle tests |
| Repair | Invalid `a01` remained active and blocked progress | Invalid result records a repair and creates `a02`/`a03` | Numbered-repair test and live topic-1 `a02` |
| Topic context | Context boundaries were implicit | Each topic reads only its packet-listed Phase 1 analysis and capsules | Packet contract and five prompts |
| Source atlas | AI copied the complete Phase 1 ledger | Application renders it deterministically from Phase 1 | Deterministic rebuild tests |
| Citation integrity | Phase 1 answer pointers were not cross-checked | Every imported Phase 1 answer pointer must exist in its source review | Semantic integrity tests |
| Page value | Basic Macro/Meso/Micro and answers | Purpose; Why/What/How; ranked sources; routes; boundaries; claims; evolution; tensions; uncertainty; reopen triggers | Phase 2 schema and renderer |
| Evidence states | Prompt encouraged enum coverage | Include only states supported by evidence | Phase 2 task contract |
| Acceptance | Mandatory second semantic worker | Disabled by default; explicit compatibility option remains | Default and opt-in tests |
| Progress | Operator repeatedly restarted the CLI | Agent reports concise progress and continues automatically | README execution loop |
| Publishing | Push could be forgotten | One validated semantic topic per commit/push; final deterministic commit/push | README and per-topic prompts |
