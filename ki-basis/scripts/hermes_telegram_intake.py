#!/usr/bin/env python3
"""
Hermes Telegram Intake Bridge for Equinox Fundraiser (Lika OS / Safer Space e.V.)
Handles:
  1. Staging receipt photos/PDFs into Paperless-ngx with tag 'STAGED-FOR-REVIEW'.
  2. Creating tracked work packages in OpenProject (Project 3) for Ideation & Receipts.
Adheres strictly to the Tiered Autonomy model: Staging and triage only; no autonomous Firefly ledger mutation.
"""

import os
import sys
import json
import base64
import argparse
import urllib.request
import urllib.error
import urllib.parse
from datetime import datetime
from pathlib import Path

# Defaults
DEFAULT_PAPERLESS_TOKEN = "c0b591378103b3328b1bb3269fcf581191864a06"
DEFAULT_OPENPROJECT_KEY = "21bf818464d30262e7012561ac934ad423df60d33d1debf29bf6880ea8c1f7ad"
PROJECT_ID = 3  # Fundraiser Hamburg — Equinox

def check_reachable(host, port, timeout=1):
    import socket
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False

def get_base_urls():
    paperless_url = os.environ.get("PAPERLESS_URL")
    openproject_url = os.environ.get("OPENPROJECT_URL")

    if not paperless_url:
        if check_reachable("paperless", 8000):
            paperless_url = "http://paperless:8000"
        else:
            paperless_url = "http://127.0.0.1:8010"

    if not openproject_url:
        if check_reachable("openproject", 80):
            openproject_url = "http://openproject:80"
        else:
            openproject_url = "http://127.0.0.1:8082"

    return paperless_url, openproject_url

def get_tag_ids(paperless_url, paperless_token, tag_names):
    tag_ids = []
    try:
        req = urllib.request.Request(
            f"{paperless_url}/api/tags/",
            headers={"Authorization": f"Token {paperless_token}"}
        )
        with urllib.request.urlopen(req) as res:
            tags_data = json.loads(res.read().decode("utf-8"))
            name_to_id = {t["name"]: t["id"] for t in tags_data.get("results", [])}
            for name in tag_names:
                if name in name_to_id:
                    tag_ids.append(name_to_id[name])
    except Exception:
        pass
    return tag_ids or [4, 6]

def post_multipart(url, fields, files, headers):
    boundary = "----WebKitFormBoundary7MA4YWxkTrZu0gW"
    body = bytearray()

    for k, v in fields.items():
        if isinstance(v, (list, tuple)):
            for item in v:
                body.extend(f"--{boundary}\r\n".encode("utf-8"))
                body.extend(f'Content-Disposition: form-data; name="{k}"\r\n\r\n'.encode("utf-8"))
                body.extend(f"{item}\r\n".encode("utf-8"))
        else:
            body.extend(f"--{boundary}\r\n".encode("utf-8"))
            body.extend(f'Content-Disposition: form-data; name="{k}"\r\n\r\n'.encode("utf-8"))
            body.extend(f"{v}\r\n".encode("utf-8"))

    for k, (filename, filedata, content_type) in files.items():
        body.extend(f"--{boundary}\r\n".encode("utf-8"))
        body.extend(f'Content-Disposition: form-data; name="{k}"; filename="{filename}"\r\n'.encode("utf-8"))
        body.extend(f"Content-Type: {content_type}\r\n\r\n".encode("utf-8"))
        body.extend(filedata)
        body.extend(b"\r\n")

    body.extend(f"--{boundary}--\r\n".encode("utf-8"))

    headers["Content-Type"] = f"multipart/form-data; boundary={boundary}"
    headers["Content-Length"] = str(len(body))

    req = urllib.request.Request(url, data=body, headers=headers)
    return urllib.request.urlopen(req)

def stage_receipt(file_path: str, caption: str, user: str):
    paperless_url, openproject_url = get_base_urls()
    paperless_token = os.environ.get("PAPERLESS_TOKEN", DEFAULT_PAPERLESS_TOKEN)
    openproject_key = os.environ.get("OPENPROJECT_KEY", DEFAULT_OPENPROJECT_KEY)

    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Receipt file not found: {file_path}")

    # 1. Upload to Paperless
    clean_caption = caption.strip() if caption else "Volunteer Receipt"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    doc_title = f"Receipt: {clean_caption} ({datetime.now().strftime('%Y%m%d_%H%M%S')})"

    content_type = "image/jpeg"
    suffix = path.suffix.lower()
    if suffix == ".png":
        content_type = "image/png"
    elif suffix == ".pdf":
        content_type = "application/pdf"

    with open(path, "rb") as f:
        file_bytes = f.read()

    # Tags: 4 (HAMBURG-FUNDRAISER-2026), 6 (STAGED-FOR-REVIEW)
    tag_ids = get_tag_ids(paperless_url, paperless_token, ["HAMBURG-FUNDRAISER-2026", "STAGED-FOR-REVIEW"])
    fields = {
        "title": doc_title,
        "tags": tag_ids,
    }
    files = {
        "document": (path.name, file_bytes, content_type)
    }
    headers = {
        "Authorization": f"Token {paperless_token}"
    }

    upload_url = f"{paperless_url}/api/documents/post_document/"
    res = post_multipart(upload_url, fields, files, headers)
    task_id = res.read().decode("utf-8").strip().replace('"', '')

    # 2. File Work Package in OpenProject
    wp_subject = f"[Receipt Staged] {clean_caption}"
    wp_desc = f"""### 🧾 Receipt Staged via Telegram
- **Uploaded By:** `{user}`
- **Received At:** {timestamp}
- **Original File:** `{path.name}`
- **Paperless Task / Document:** `{task_id}`
- **Caption / Notes:** {clean_caption}

---
### 🛡️ Operator / Treasurer Review Checklist (Tiered Autonomy)
- [ ] Inspect document in Paperless-ngx (`Tag: STAGED-FOR-REVIEW`)
- [ ] Validate tax sphere (Ideeller Bereich / Zweckbetrieb / WGB) & VAT rate (7% / 19% / 0%)
- [ ] Verify vendor, receipt date, and matching bank debit / volunteer payout claim
- [ ] Record validated double-entry transaction in Firefly III
- [ ] Update this task status to **Closed**
"""

    auth_str = base64.b64encode(f"apikey:{openproject_key}".encode()).decode()
    wp_data = {
        "subject": wp_subject,
        "description": {"raw": wp_desc},
        "_links": {
            "type": {"href": "/api/v3/types/1"},      # Task
            "status": {"href": "/api/v3/statuses/1"},  # New
        }
    }
    op_req = urllib.request.Request(
        f"{openproject_url}/api/v3/projects/{PROJECT_ID}/work_packages",
        data=json.dumps(wp_data).encode("utf-8"),
        headers={
            "Authorization": f"Basic {auth_str}",
            "Host": "127.0.0.1:8082",
            "Content-Type": "application/json"
        }
    )
    op_res = urllib.request.urlopen(op_req)
    wp_info = json.loads(op_res.read().decode("utf-8"))
    wp_id = wp_info.get("id")

    return {
        "status": "success",
        "action": "receipt_staged",
        "paperless_task_id": task_id,
        "openproject_wp_id": wp_id,
        "openproject_subject": wp_subject,
        "user": user,
        "timestamp": timestamp
    }

def create_task(text: str, user: str, category: str = "Ideation"):
    _, openproject_url = get_base_urls()
    openproject_key = os.environ.get("OPENPROJECT_KEY", DEFAULT_OPENPROJECT_KEY)

    clean_text = text.strip()
    first_line = clean_text.splitlines()[0] if clean_text else "Community Task"
    first_line = first_line[:80]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    wp_subject = f"[{category}] {first_line}"
    wp_desc = f"""### 💡 Community Idea / Task from Telegram
- **Created By:** `{user}`
- **Topic / Category:** `{category}`
- **Logged At:** {timestamp}

---
### Details
{clean_text}

---
*Created automatically by Hermes Telegram Agent.*
"""

    auth_str = base64.b64encode(f"apikey:{openproject_key}".encode()).decode()
    wp_data = {
        "subject": wp_subject,
        "description": {"raw": wp_desc},
        "_links": {
            "type": {"href": "/api/v3/types/1"},      # Task
            "status": {"href": "/api/v3/statuses/1"},  # New
        }
    }
    op_req = urllib.request.Request(
        f"{openproject_url}/api/v3/projects/{PROJECT_ID}/work_packages",
        data=json.dumps(wp_data).encode("utf-8"),
        headers={
            "Authorization": f"Basic {auth_str}",
            "Host": "127.0.0.1:8082",
            "Content-Type": "application/json"
        }
    )
    op_res = urllib.request.urlopen(op_req)
    wp_info = json.loads(op_res.read().decode("utf-8"))
    wp_id = wp_info.get("id")

    return {
        "status": "success",
        "action": "task_created",
        "openproject_wp_id": wp_id,
        "openproject_subject": wp_subject,
        "category": category,
        "user": user,
        "timestamp": timestamp
    }

def main():
    parser = argparse.ArgumentParser(description="Hermes Telegram Intake CLI")
    subparsers = parser.add_subparsers(dest="subcommand", required=True)

    # Receipt subcommand
    p_receipt = subparsers.add_parser("receipt", help="Stage a receipt photo/document")
    p_receipt.add_argument("--file", required=True, help="Path to receipt image/pdf")
    p_receipt.add_argument("--caption", default="", help="User caption or receipt notes")
    p_receipt.add_argument("--user", default="telegram_user", help="Telegram user handle or ID")

    # Task/Ideation subcommand
    p_task = subparsers.add_parser("task", help="Create an ideation/operational task")
    p_task.add_argument("--text", required=True, help="Description of task or idea")
    p_task.add_argument("--user", default="telegram_user", help="Telegram user handle or ID")
    p_task.add_argument("--category", default="Ideation", help="Category prefix (e.g. Sound, Bar, Door, Art)")

    args = parser.parse_args()

    try:
        if args.subcommand == "receipt":
            result = stage_receipt(args.file, args.caption, args.user)
        elif args.subcommand == "task":
            result = create_task(args.text, args.user, args.category)
        else:
            parser.print_help()
            sys.exit(1)
        print(json.dumps(result, indent=2))
    except Exception as e:
        err = {"status": "error", "message": str(e)}
        print(json.dumps(err, indent=2), file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
