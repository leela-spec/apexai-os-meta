---
type: Handover
title: SEC — OpenProject SECRET_KEY_BASE hygiene (leela-op178) — low-urgency, do-not-break
description: >
  A dedicated, self-contained handover for one chat to (optionally) move the inline OpenProject
  SECRET_KEY_BASE out of the leela-op178 compose files into a local .env — WITHOUT changing the value
  (changing it logs everyone out and can make encrypted data unreadable). Verified low-urgency: the files
  are LOCAL-ONLY (leela-op178 is not a git repo), so the secret is not exposed anywhere. "Leave as-is" is
  a legitimate outcome. Research-and-recommend + tiny local edit only; nothing else.
created: 2026-09-29
status: open (optional / low priority)
authority_order: "LIVE runtime > this handover. If they conflict, STOP and surface."
implementation_authority: local file edit ONLY, value-preserving; no container recreate, no value change, without explicit operator OK.
---

# SEC — OpenProject SECRET_KEY_BASE hygiene (leela-op178)

## 0. Plain-language summary (read first)
`SECRET_KEY_BASE` is the secret OpenProject uses to sign login cookies/sessions. Right now its actual value
is typed **inline** in two compose files under `C:\GitDev\leela-op178\` (`compose.yaml` line 13,
`compose.shared-db.yaml` line 14). Best practice is to keep secrets in a separate `.env` file that the
compose file references as `${OPENPROJECT_SECRET_KEY_BASE}`.

## 1. Verified ground truth (2026-09-29, read-only; values never printed)
- Both files hold the secret as an **inline literal** (not a `${...}` reference).
- **`C:\GitDev\leela-op178` is NOT a git repository** (`git rev-parse` → "not a git repository"; 0 tracked
  files; no remote). ⇒ **the secret is local-only — never committed, not on GitHub, not exposed.** This is
  the key fact: the exposure risk that normally makes a hard-coded secret urgent **does not apply here.**
- No `.env` and no `.gitignore` exist in `leela-op178`.
- Other stacks already follow best practice: `lika-community/compose.wsl.yaml` uses
  `${OPENPROJECT_SECRET_KEY_BASE:?…}` (a reference), and `ki-basis-shared`'s DB passwords live in a
  local-only `.env`. So SEC is scoped **only** to `leela-op178`.

## 2. The one hard rule (why this is "do-not-break")
The value must stay **byte-for-byte identical**. Per OpenProject docs + a published security advisory:
changing `SECRET_KEY_BASE` **invalidates all sessions/cookies/2FA and can make encrypted DB content
unreadable** (everyone logged out; possible data-read breakage). So: **never regenerate/rotate it here**
unless the operator explicitly wants a rotation and accepts the logout. Moving it while preserving the exact
value is functionally invisible.
Sources: OpenProject Docker-compose docs (SECRET_KEY_BASE must be stable/unique); advisory GHSA-r85r-gjq2-f83r
(default `OVERWRITE_ME` → RCE — so it must remain a real unique value); Docker Compose secrets best practice
(`${VAR}` in compose + value in git-ignored `.env`).

## 3. Options
- **Option LEAVE (fully acceptable):** do nothing. It's local-only, unexposed, and working. Zero risk.
  Legitimate given §1.
- **Option MOVE (recommended if you want the hygiene):** value-preserving move to a local `.env`. Low risk
  if the value is copied exactly.
- **Option ROTATE (NOT recommended now):** generate a new value. Only if you believe the value leaked.
  Disruptive (logs everyone out); out of scope unless explicitly requested.

## 4. Exact steps for Option MOVE (operator-gated; all LOCAL, no git in leela-op178)
1. **Read the current value privately** (do NOT print it to chat/logs):
   `wsl -d Ubuntu -u root -- grep -h SECRET_KEY_BASE /mnt/c/GitDev/leela-op178/compose.yaml` — copy the value.
   (Both files should carry the SAME value — verify they match; if they differ, STOP and surface it.)
2. **Create `C:\GitDev\leela-op178\.env`** containing exactly one line (the real value, unquoted):
   `OPENPROJECT_SECRET_KEY_BASE=<paste the exact value>`
3. **Create `C:\GitDev\leela-op178\.gitignore`** with `.env` (belt-and-suspenders even though it's not a repo).
4. **Edit both compose files:** replace the inline `SECRET_KEY_BASE: <value>` with
   `SECRET_KEY_BASE: ${OPENPROJECT_SECRET_KEY_BASE:?OPENPROJECT_SECRET_KEY_BASE is required}` — deterministic,
   value-preserving. (Use a match-once patcher; do not hand-edit near the secret.)
5. **Validate WITHOUT printing secrets:** `docker compose -f compose.shared-db.yaml --env-file .env -p leela-op178 config --quiet`
   (parse-only; `--quiet` prints nothing). Do NOT run plain `config` (it would render the secret).
6. **No recreate needed now.** The running container already has the value; the edit only affects the *next*
   `up`/recreate. Because the value is unchanged, that future recreate keeps all sessions valid.
7. Record done; the secret never appears in chat, logs, or any commit.

## 5. Verification & rollback
- Verify: `docker compose … config --quiet` exits 0; a later intentional recreate leaves OpenProject at
  `127.0.0.1:8083` returning 302→/login and existing logins still valid.
- Rollback: revert the two compose edits (keep a `.bak` of each before editing) and delete `.env`; the inline
  value returns. Zero data risk since the value never changed.

## 6. Blind spots to check before acting
- Confirm both files carry the SAME value (step 1). If not, the running container uses whichever file it was
  started from (`leela-op178-openproject` was created from `compose.shared-db.yaml`) — match `.env` to THAT.
- Confirm nothing else in `leela-op178` (scripts, backups) also hard-codes the value.
- This handover touches ONLY `leela-op178`. It must not modify any other stack.

## 7. Definition of done
Either (a) operator chooses LEAVE and it's recorded, or (b) the value-preserving MOVE is done: `.env` holds
the exact value, both compose files reference `${OPENPROJECT_SECRET_KEY_BASE}`, `config --quiet` passes, the
value never changed, and the secret was never printed or committed.
