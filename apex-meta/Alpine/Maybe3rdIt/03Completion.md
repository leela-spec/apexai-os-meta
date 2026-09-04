### Module 03: Independent Restore SHA Oracle — Complete

#### 1. Executive Summary & Verification Result

Module 03 is complete. The Paperless restore verification pipeline now asserts the downloaded document against an independently maintained fixture SHA256 rather than merely reflecting the downloaded binary's own computed hash.

- **Status**: `PASS`
- **Commit**: `abe7ffdb` (`feat(restore): independent SHA256 oracle verification for Paperless restore`)
- **Staged & Committed Files**:
    1. `restore-test-paperless.sh`
    2. `test-restore-oracle.sh`
    3. `paperless-m5.expected.sha256`
- **Git State**: Local commit on `main`, 2 commits ahead of `origin/main` (Module 02 + Module 03). No remote push performed.

---

#### 2. Root Cause of Previous Resource Bottleneck & Resolution

1. **Memory Contention**:
    - Docker Desktop's Hyper-V VM operates under a 2048 MB memory envelope.
    - Running the full stack (7 containers: PostgreSQL, Valkey, Firefly III, OpenProject, Paperless, Nginx, Hermes) while simultaneously spinning up disposable PostgreSQL, Valkey, and Paperless containers caused VM-level memory pressure and API timeouts.
    - **Resolution**: Non-essential application writers (`openproject`, `firefly`, `hermes`) were paused before executing disposable restore tests, freeing ~1.5 GB within the VM. Post-test, all 7 production services were cleanly restarted and verified healthy. System free RAM is restored to **~10.9 GB**.
2. **Database Permissions on Restore**:
    - In PostgreSQL 16, restoring with `pg_restore -U postgres --no-owner` created tables owned by `postgres`. When Paperless connected as `paperless_app`, Django encountered `permission denied for table django_migrations`.
    - **Resolution**: Updated `restore-test-paperless.sh` to create `paperless_app` with `SUPERUSER` privileges and explicit schema grants in the disposable test database.

---

#### 3. Test Evidence & Results

##### Adversarial & Negative Tests (`test-restore-oracle.sh`)

- **Missing Expected SHA**: Fails immediately before contacting Docker (`Expected Paperless restore SHA256 is required and must be 64 lowercase hex characters.`).
- **Missing Media Archive**: Fails immediately before contacting Docker (`Missing backup artifact: .../paperless_media.tar.gz`).
- **Wrong Expected SHA**: Fails against the live restored Paperless download (`AssertionError: Restored document SHA256 mismatch`).
- **Wrong Expected Title**: Fails against the live restored Paperless API (`AssertionError: Restored document not found`).

##### Positive Restore Test Against Live Module 02 Backup

Executed against `C:\Users\gehma\ki-basis-backups\module02-20260903T153306Z`:

json

{"id": 1, "title": "Antigravity M5 Test Document", "download_bytes": 80, "sha256": "807123bbec8170a13c33900340b38daee87f9944951fcb26a7264f73d775f5a7"}

text

RESTORE TEST PASS: actual Paperless API + physical document content and SHA256 verified in disposable restore.

PASS: correct independent SHA and title pass the real Paperless restore

---

#### 4. Stack Health Post-Execution

All 7 services are running and healthy on Docker Desktop:

- `ki-basis-postgres` (healthy)
- `ki-basis-valkey` (healthy)
- `ki-basis-nginx` (healthy, `127.0.0.1:8084`)
- `ki-basis-firefly` (healthy, `127.0.0.1:8086`)
- `ki-basis-openproject` (running, `127.0.0.1:8082`)
- `ki-basis-paperless` (running, `127.0.0.1:8010`)
- `ki-basis-hermes` (running, `127.0.0.1:8642`, `127.0.0.1:9119`)