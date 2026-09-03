# Module 03 — Restore Test Independent Oracle

## Target

Make the Paperless restore test prove that the restored binary is the expected fixture rather than merely printing the binary's own hash.

## Current defect

The current restore script computes SHA256 after downloading the restored file, but does not assert it against an independently maintained expected SHA256.

## Required design

Use one independent, non-secret fixture oracle.

Preferred repository artifact:

`ki-basis/tests/fixtures/paperless-m5.expected.sha256`

It contains only the expected SHA256 for the already-known non-secret test document. The value must be derived from the original/source fixture or previously accepted independent receipt — **never from the restored output during the same test**.

Patch `ki-basis/scripts/restore-test-paperless.sh` so it:

1. requires an expected SHA value from the fixture file or an explicit `PAPERLESS_RESTORE_EXPECT_SHA256` override;
2. downloads the real document through the real Paperless API;
3. hashes the bytes;
4. asserts exact equality;
5. prints PASS only after equality succeeds.

## Negative tests

- wrong expected SHA -> hard failure;
- missing expected SHA -> hard failure;
- missing media archive -> hard failure;
- wrong expected title -> hard failure.

## Preserve

- disposable network;
- disposable Postgres/Valkey/Paperless containers;
- no writes to live volumes;
- fail-closed `PAPERLESS_SECRET_KEY` requirement;
- Windows path normalization and `docker cp` transport.

## Acceptance

Actual Paperless participates at runtime and a wrong independently supplied SHA makes the test fail.

## Commit boundary

One local restore-oracle commit. No push. STOP.
