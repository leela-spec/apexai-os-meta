#!/usr/bin/env bash
# =============================================================================
# doc-integrity-lint.sh — READ-ONLY audit of the infra documentation set.
# Answers the questions needed to change docs SAFELY:
#   A) which "current" docs still assert RETIRED topology (fix targets)
#   B) is any candidate doc consumed by AUTOMATION (silent-breakage risk)?
#   C) are the 3 architecture-spec copies in sync (mirror drift)?
#   D) known broken cross-repo pointer still broken?
# Run: wsl -d Ubuntu -u root -- bash -c "tr -d '\r' < <this file> | bash"
# Read-only; prints a report. No pass/fail exit gating (informational).
# =============================================================================
set -uo pipefail
APEX=/mnt/c/GitDev/apexai-os-meta
LEELA=/mnt/c/GitDev/Leela-Cloud-2026
GLOBAL=/mnt/c/Users/gehma/.claude
SKILLS=/mnt/c/GitDev/agent-skills
INC=(--include=*.md --include=*.json --include=*.sh --include=*.ps1 --include=*.yaml --include=*.yml --include=SKILL.md)
EXC=(--exclude-dir=.git --exclude-dir=node_modules --exclude-dir=_archive)

hr(){ echo; echo "########## $* ##########"; }

hr "A. Retired-topology assertions in ki-basis + apex-meta docs (candidates to banner/archive)"
echo "-- files mentioning 'Docker Desktop' (excluding ones that also say superseded/retired/historical) --"
grep -rl "${INC[@]}" "${EXC[@]}" -i "docker desktop" "$APEX/ki-basis" "$APEX/apex-meta" 2>/dev/null | while read -r f; do
  if grep -qiE "superseded|retired|rollback reference|historical|MIRROR" "$f"; then :; else echo "  [STALE?] ${f#$APEX/}"; fi
done
echo "-- files naming OpenProject v14 (openproject:14 / 'OpenProject 14' / ki-basis-openproject as live) --"
grep -rl "${INC[@]}" "${EXC[@]}" -iE "openproject:14|openproject 14" "$APEX/ki-basis" "$APEX/apex-meta" 2>/dev/null | while read -r f; do
  grep -qiE "superseded|deleted|retired|D-18|historical" "$f" || echo "  [STALE?] ${f#$APEX/}"
done

hr "B. Automated-consumer scan (is a candidate doc referenced by skills/scripts/manifests?)"
consumer_scan(){ # filename-or-path
  local needle="$1" hits
  hits=$(grep -rl "${INC[@]}" "${EXC[@]}" -F "$needle" \
        "$APEX/.claude" "$APEX"/**/.claude 2>/dev/null; \
        grep -rl -F "$needle" "$GLOBAL" "$SKILLS" 2>/dev/null; \
        grep -rl "${INC[@]}" "${EXC[@]}" -F "$needle" "$APEX" 2>/dev/null | grep -E "/(scripts|\.agents)/|run-state|manifest|\.json$" )
  hits=$(echo "$hits" | sort -u | sed '/^$/d')
  if [ -z "$hits" ]; then
    echo "  [$needle] -> no automated consumer found (safe: human docs only)"
  else
    echo "  [$needle] -> referenced by:"; echo "$hits" | sed 's/^/       /'
  fi
}
for n in ARCHITEKTUR-BASIS.md DUAL_INSTANCE_ARCHITECTURE.md STACK_ARCHITECTURE.md DUAL_INSTANCE_RUNBOOK.md \
         RUNBOOK-openproject-17.8-operations.md "docs/ProjectMM/openproject" BOT_WIRING_AND_PERSONA_HANDOVER.md; do
  consumer_scan "$n"
done

hr "C. Architecture-spec mirror sync (canonical vs 2 mirrors)"
CAN="$APEX/ki-basis/docs/DUAL_INSTANCE_ARCHITECTURE.md"
M1="$APEX/apex-meta/orchestration/new_final_v4/architecture_dossier/01_DUAL_INSTANCE_ARCHITECTURE.md"
M2="$APEX/docs/AUDIT_DOSSIER_DUAL_KI_BASIS/01_DUAL_INSTANCE_ARCHITECTURE.md"
for f in "$CAN" "$M1" "$M2"; do
  if [ -f "$f" ]; then printf "  %-6s lines=%-4s md5=%s  %s\n" "" "$(wc -l < "$f")" "$(md5sum < "$f" | cut -c1-12)" "${f#$APEX/}"; else echo "  MISSING: $f"; fi
done
echo "  (canonical differing from the two mirrors = drift; two mirrors equal each other = they were synced to each other only)"

hr "D. Cross-repo pointer in the moved handover (should be FIXED)"
BR="$APEX/ki-basis/docs/openproject/openproject-cli-agent-handover/openproject-cli-agent-handover.md"
if [ -f "$BR" ]; then
  if grep -q "apexai-os-meta/docs/DUAL_INSTANCE_ARCHITECTURE.md" "$BR" 2>/dev/null; then
    echo "  [BROKEN] $BR references .../docs/DUAL_INSTANCE_ARCHITECTURE.md (real path is .../ki-basis/docs/...)"
  else echo "  [ok] pointer fixed (references ki-basis/docs/... or absent)"; fi
else echo "  (file not found: $BR)"; fi

echo; echo "done."
