#!/usr/bin/env python3
"""Merge Lika KB source manifest delta records deterministically.

The script only updates manifests/source-manifest.json from JSONL delta records.
If an existing entry changes hash, the prior entry is copied into
manifests/source-history/ before the manifest is updated.
"""

from __future__ import annotations

import argparse
import json
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path


REQUIRED_FIELDS = {
    "source_id",
    "source_path",
    "source_type",
    "title",
    "status",
    "source_storage_mode",
    "hash_algorithm",
    "source_hash",
    "added_at",
    "ingest_status",
    "original_source_path",
    "no_hash_reason",
    "derived_from",
    "run_id",
}


def utc_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def read_delta(path: Path) -> list[dict]:
    rows: list[dict] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            stripped = line.strip()
            if not stripped:
                continue
            record = json.loads(stripped)
            missing = sorted(REQUIRED_FIELDS - set(record))
            if missing:
                raise SystemExit(f"{path}:{line_number}: missing required fields: {missing}")
            rows.append(record)
    return rows


def load_manifest(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if "sources" not in data or not isinstance(data["sources"], list):
        raise SystemExit(f"{path} does not contain a sources list")
    return data


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kb-root", required=True)
    parser.add_argument("--delta", required=True)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true")
    mode.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    kb_root = Path(args.kb_root)
    manifest_path = kb_root / "manifests" / "source-manifest.json"
    delta_path = Path(args.delta)
    if not delta_path.is_absolute():
        delta_path = Path.cwd() / delta_path

    manifest = load_manifest(manifest_path)
    delta = read_delta(delta_path)

    by_id = {source.get("source_id"): source for source in manifest["sources"]}
    by_path = {source.get("source_path"): source for source in manifest["sources"]}
    additions: list[dict] = []
    updates: list[dict] = []
    unchanged: list[dict] = []
    history_rows: list[dict] = []

    for record in delta:
        existing = by_id.get(record["source_id"]) or by_path.get(record["source_path"])
        clean = {key: value for key, value in record.items() if key != "run_id"}
        if existing is None:
            additions.append(clean)
            continue
        if existing.get("source_hash") == record.get("source_hash"):
            unchanged.append(record)
            continue
        history_rows.append(deepcopy(existing))
        updates.append(clean)

    result = {
        "manifest": str(manifest_path),
        "delta": str(delta_path),
        "mode": "dry-run" if args.dry_run else "apply",
        "delta_records": len(delta),
        "additions": len(additions),
        "updates": len(updates),
        "unchanged": len(unchanged),
        "history_records_to_write": len(history_rows),
    }

    if args.dry_run:
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0

    existing_ids = {source.get("source_id") for source in manifest["sources"]}
    for update in updates:
        for idx, source in enumerate(manifest["sources"]):
            if source.get("source_id") == update["source_id"] or source.get("source_path") == update["source_path"]:
                manifest["sources"][idx] = update
                break
    for addition in additions:
        if addition["source_id"] in existing_ids:
            raise SystemExit(f"duplicate source_id after planning: {addition['source_id']}")
        existing_ids.add(addition["source_id"])
        manifest["sources"].append(addition)

    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    manifest["updated_at"] = now
    manifest["sources"] = sorted(manifest["sources"], key=lambda row: row.get("source_path", ""))

    history_dir = kb_root / "manifests" / "source-history"
    if history_rows:
        history_dir.mkdir(parents=True, exist_ok=True)
        history_path = history_dir / f"source-manifest-history_{utc_stamp()}.json"
        with history_path.open("w", encoding="utf-8", newline="\n") as handle:
            json.dump({"created_at": now, "replaced_sources": history_rows}, handle, indent=2, sort_keys=True)
            handle.write("\n")
        result["history_path"] = str(history_path)

    with manifest_path.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(manifest, handle, indent=2, sort_keys=True)
        handle.write("\n")

    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
