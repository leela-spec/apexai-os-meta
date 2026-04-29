# HEARTBEAT.md

<!--
Your AI reads this on every heartbeat poll.
Keep it SMALL - scripts are free, model time is expensive.
Only wake the model when scripts produce output.
-->

## Purpose

Maintain stable project progress without allowing overlapping loops to create silent drift.

This file is a small, script-first maintenance ritual.
It is subordinate to escalation law, QA/Hygiene authority, promotion authority, and night-planning authority.

## Rules

- one active foreground flow should be the default baseline
- any background heartbeat must be staggered and low-impact until validation proves broader overlap is safe
- heartbeat lag, queue growth, and memory-write delays are failure signals
- project updates should reference the governing taxonomy rather than inventing new categories ad hoc
- do not use heartbeat as hidden planning or synthesis authority
- do not treat heartbeat output as a truth-mutation path
- route material hygiene issues into `managed/rules/QA_HYGIENE_PROTOCOL.md` or `managed/rules/ESCALATION_EXCEPTION_BLOCK.md` rather than masking them as routine progress
- route truth-change issues into `managed/rules/PROMOTION_PROTOCOL.md` rather than treating them as routine maintenance
- route bounded next-cycle planning needs into `managed/rituals/NIGHT_PLANNING_PROTOCOL.md` rather than expanding heartbeat into a planning hub

## Checks

<!-- Add your check scripts here. Only act on output. -->
<!-- Example:
```bash
/path/to/check-email.sh
/path/to/check-calendar.sh
/path/to/check-mentions.sh
```
-->

## Memory Maintenance (once per day, first heartbeat after 6pm)
If today's date differs from "Last updated" in user/memory/MEMORY.md:
1. Read recent `user/memory/memory-daily/YYYY-MM-DD.md` files (today + yesterday)
2. Update user/memory/MEMORY.md with anything significant
3. Remove outdated info
4. If MEMORY.md > 10k chars, archive completed items to `docs/archive/memory-archive-YYYY-MM-DD.md`
5. Update the "Last updated" date

## If All Scripts Return Nothing
Reply: HEARTBEAT_OK

---

**Philosophy**: Scripts are free. Model time is expensive.
Don't burn tokens deciding "nothing happening" - let scripts decide that.
