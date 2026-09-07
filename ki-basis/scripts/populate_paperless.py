"""
Populate Paperless-ngx with Equinox Hamburg Fundraiser Documents
Uploads all 7 generated PDF documents into Paperless-ngx, tagging them
with KI-BASIS-TEST, LIKA, SAFER-SPACE-EV, HAMBURG-FUNDRAISER-2026, and PRETIX.
"""

import argparse
import os
from pathlib import Path
import httpx

INSTANCE_PORTS = {
    "private": 8010,
    "community": 9010,
}

DEFAULT_PAPERLESS_TOKEN = "c0b591378103b3328b1bb3269fcf581191864a06"

PAPERLESS_URL = os.environ.get(
    "PAPERLESS_URL",
    f"http://127.0.0.1:{INSTANCE_PORTS.get(os.environ.get('KI_INSTANCE', 'private'), 8010)}"
)
PAPERLESS_TOKEN = os.environ.get("PAPERLESS_TOKEN", DEFAULT_PAPERLESS_TOKEN)
STAGING_DIR = Path(os.environ.get("STAGING_DIR", "C:/GitDev/apexai-os-meta/ki-basis/fixtures/fundraiser_hamburg"))

HEADERS = {
    "Authorization": f"Token {PAPERLESS_TOKEN}",
}


def get_or_create_tag(client: httpx.Client, tag_name: str) -> int:
    r = client.get(f"{PAPERLESS_URL}/api/tags/?name__iexact={tag_name}", headers=HEADERS)
    results = r.json().get("results", [])
    if results:
        return results[0]["id"]
    r_create = client.post(f"{PAPERLESS_URL}/api/tags/", headers=HEADERS, json={"name": tag_name})
    return r_create.json()["id"]


def get_or_create_correspondent(client: httpx.Client, name: str) -> int:
    r = client.get(f"{PAPERLESS_URL}/api/correspondents/?name__iexact={name}", headers=HEADERS)
    results = r.json().get("results", [])
    if results:
        return results[0]["id"]
    r_create = client.post(f"{PAPERLESS_URL}/api/correspondents/", headers=HEADERS, json={"name": name})
    return r_create.json()["id"]


def get_or_create_doc_type(client: httpx.Client, name: str) -> int:
    r = client.get(f"{PAPERLESS_URL}/api/document_types/?name__iexact={name}", headers=HEADERS)
    results = r.json().get("results", [])
    if results:
        return results[0]["id"]
    r_create = client.post(f"{PAPERLESS_URL}/api/document_types/", headers=HEADERS, json={"name": name})
    return r_create.json()["id"]


def upload_documents():
    with httpx.Client(timeout=30.0) as client:
        # Create Tags
        tags = [
            get_or_create_tag(client, "KI-BASIS-TEST"),
            get_or_create_tag(client, "LIKA"),
            get_or_create_tag(client, "SAFER-SPACE-EV"),
            get_or_create_tag(client, "HAMBURG-FUNDRAISER-2026"),
            get_or_create_tag(client, "PRETIX"),
        ]

        # Correspondents
        corr_safer_space = get_or_create_correspondent(client, "Safer Space e.V.")
        corr_equinox = get_or_create_correspondent(client, "Equinox Club Hamburg")
        corr_sound = get_or_create_correspondent(client, "Nordic Sound & Light GmbH")
        corr_pretix = get_or_create_correspondent(client, "pretix.eu")
        corr_sixt = get_or_create_correspondent(client, "Sixt Rent-a-Car")
        corr_biomarkt = get_or_create_correspondent(client, "Bio-Großmarkt Hamburg")

        # Document Types
        dt_contract = get_or_create_doc_type(client, "Vertrag")
        dt_invoice = get_or_create_doc_type(client, "Rechnung")
        dt_receipt = get_or_create_doc_type(client, "Beleg")
        dt_guidelines = get_or_create_doc_type(client, "Richtlinie")
        dt_settlement = get_or_create_doc_type(client, "Abrechnung")

        documents_to_upload = [
            {
                "file": "Equinox_Hamburg_Venue_Lease_Contract.pdf",
                "title": "Mietvertrag Equinox Hamburg & Mindestumsatzgarantie 7.500 EUR",
                "correspondent": corr_equinox,
                "document_type": dt_contract,
                "created": "2026-10-15",
            },
            {
                "file": "Lika_Awareness_Care_Consent_Guidelines.pdf",
                "title": "Lika Care Team — Awareness & Consent Guidelines SOP",
                "correspondent": corr_safer_space,
                "document_type": dt_guidelines,
                "created": "2026-10-20",
            },
            {
                "file": "Sound_Visual_Rental_Invoice_Hamburg.pdf",
                "title": "Rechnung Nordic Sound & Light (12kW L-Acoustics & Licht)",
                "correspondent": corr_sound,
                "document_type": dt_invoice,
                "created": "2026-11-18",
            },
            {
                "file": "DJ_Booking_Agreements_Lineup.pdf",
                "title": "Künstlerverträge & Lineup-Vereinbarungen (4 Acts)",
                "correspondent": corr_safer_space,
                "document_type": dt_contract,
                "created": "2026-11-10",
            },
            {
                "file": "Catering_Bar_Snacks_Receipt.pdf",
                "title": "Quittung Bio-Großmarkt Hamburg (Care Station Versorgung)",
                "correspondent": corr_biomarkt,
                "document_type": dt_receipt,
                "created": "2026-11-19",
            },
            {
                "file": "Sixt_Transporter_Rental_Invoice.pdf",
                "title": "Rechnung Sixt Transporter IVECO Daily 3.5t",
                "correspondent": corr_sixt,
                "document_type": dt_invoice,
                "created": "2026-11-21",
            },
            {
                "file": "Pretix_Ticketing_Payout_Settlement.pdf",
                "title": "Pretix Auszahlungsabrechnung & Quotenbericht (320 Tickets)",
                "correspondent": corr_pretix,
                "document_type": dt_settlement,
                "created": "2026-11-21",
            },
        ]

        uploaded = []
        for doc_info in documents_to_upload:
            file_path = STAGING_DIR / doc_info["file"]
            if not file_path.exists():
                print(f"[SKIP] File not found: {file_path}")
                continue

            with open(file_path, "rb") as f:
                data = {
                    "title": doc_info["title"],
                    "created": doc_info["created"],
                    "correspondent": doc_info["correspondent"],
                    "document_type": doc_info["document_type"],
                }
                # Form data for multiple tags
                tag_data = [("tags", t) for t in tags]
                files = {"document": (doc_info["file"], f, "application/pdf")}

                r = client.post(
                    f"{PAPERLESS_URL}/api/documents/post_document/",
                    headers=HEADERS,
                    data=data,
                    files=files,
                )
                if r.status_code in (200, 201, 202):
                    print(f"[OK] Uploaded {doc_info['file']} -> {r.status_code}: {r.text}")
                    uploaded.append(doc_info["file"])
                else:
                    print(f"[ERR] Failed {doc_info['file']} -> {r.status_code}: {r.text}")

        print(f"Total documents successfully queued in Paperless-ngx: {len(uploaded)}/7")


def parse_args():
    parser = argparse.ArgumentParser(description="Populate Paperless-ngx with Equinox Hamburg Fundraiser Documents")
    parser.add_argument("-i", "--instance", choices=["private", "community"], default=os.environ.get("KI_INSTANCE", "private"),
                        help="Target instance: private (port 8010) or community (port 9010). Default: private")
    parser.add_argument("-u", "--url", default=None, help="Explicit Paperless base URL (overrides --instance and PAPERLESS_URL)")
    parser.add_argument("-t", "--token", default=None, help="Explicit Paperless API token")
    parser.add_argument("-s", "--staging-dir", default=None, help="Path to PDF documents directory")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    if args.url:
        PAPERLESS_URL = args.url
    elif "PAPERLESS_URL" in os.environ:
        PAPERLESS_URL = os.environ["PAPERLESS_URL"]
    else:
        PAPERLESS_URL = f"http://127.0.0.1:{INSTANCE_PORTS[args.instance]}"

    if args.token:
        PAPERLESS_TOKEN = args.token
    HEADERS["Authorization"] = f"Token {PAPERLESS_TOKEN}"

    if args.staging_dir:
        STAGING_DIR = Path(args.staging_dir)

    print(f"==> Connecting to Paperless-ngx at: {PAPERLESS_URL} (Staging: {STAGING_DIR})")
    upload_documents()
