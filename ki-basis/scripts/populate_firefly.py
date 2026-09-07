"""
Populate Firefly III with Equinox Hamburg Fundraiser Financial Data
Creates GLS Bank Asset Account for Safer Space e.V., expense & revenue accounts,
categories, and complete transaction ledger reflecting Pretix ticket sales and vendor invoices.
"""

import argparse
import os
from typing import Any, Dict
import httpx

INSTANCE_PORTS = {
    "private": 8086,
    "community": 9086,
}

DEFAULT_FIREFLY_TOKEN = (
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIwMWEwNWU2Yy1lYTliLTcyZTMtOTNjMS02OTE3OTcyZjgwNjEiLCJqdGkiOiI2"
    "Yjg5ZWE4MWYyN2EyM2I2YjQwZGFhYmJkZjE3OWExMWM5ZTU1YzQ2ZjMwMjRhYzIxNTYwNGJkZWZiZGI3ZTRmMWFjODIzMmVhZmM3YWNkYSIsIm"
    "lhdCI6MTc4ODU5MjA5Ni43Mzk2MDQsIm5iZiI6MTc4ODU5MjA5Ni43Mzk2MDYsImV4cCI6MTgyMDEyODA5Ni42NTQ2MjIsInN1YiI6IjEiLCJ"
    "zY29wZXMiOltdfQ.pEwRwpTIXJjCyPniAnRSiFut5VsO7X3CcITXqvq-uY5mojtu7y3lEo_lFoSPH3dwaHsOqczx57QzMRHg5M87FybHNzjBCY"
    "rRCa0XdyX3P8azyzW_a-tEzzi-Gj3sBTKKA6ipNuV5yZ8wzN18BksQny0hXIAc84Y9V2ydWztRUBQxPMPMXwC7ZukFSGrmmLt8nqb_yCFoHxE7"
    "WklxivZVyJaEl_ZplXrjcNjH2_Tn9C1_9g-EnDTXteMFLOFIBsIPv3D2dj3eOh6Kfi1utCBuqnGted7BVRyDJ6SQzgOVv8kBkft5tGdVFvqVTZi"
    "j7bMXnlWhIUeLSZTf-oqZ94DwvZXFh135-2JBE7QBDIVNZ43WgQp04NBa_onqVJLE0EPkA1oJClkGVxjzqnX8cx-MED3hKfHrb7eBz2eFmvzez"
    "lnpFwtkTbbStojlT9r9Vswmht6n1c6gmB3GrpEhOV9gUs0ThMDVP7VieF9LC6AB14A_AGkaqUUf6OPxqZ4qBvrCKQcwghEINxmDUWKoMZ7BWPcY"
    "R4e29GokXbANBktE-GC27gBoaQpHQY3YVoRK0GRMz1DbyxngbQk-aWVZUBtrYks4KOcfI1s1mb_IWE9Nt8WoDhxsWQJvcFqqPWXlfflwNNb-Wb"
    "min9p__lL3Rxnv3fHqod8hlZ_FoZ_bKuLLraM"
)

FIREFLY_URL = os.environ.get(
    "FIREFLY_URL",
    f"http://127.0.0.1:{INSTANCE_PORTS.get(os.environ.get('KI_INSTANCE', 'private'), 8086)}"
)
FIREFLY_TOKEN = os.environ.get("FIREFLY_TOKEN", DEFAULT_FIREFLY_TOKEN)

HEADERS = {
    "Authorization": f"Bearer {FIREFLY_TOKEN}",
    "Accept": "application/vnd.api+json",
    "Content-Type": "application/json",
}


def get_or_create_account(client: httpx.Client, name: str, account_type: str, currency_code: str = "EUR", opening_balance: str = None) -> str:
    r = client.get(f"{FIREFLY_URL}/api/v1/accounts?type={account_type}", headers=HEADERS)
    for acc in r.json().get("data", []):
        if acc["attributes"]["name"] == name:
            return acc["id"]

    payload: Dict[str, Any] = {
        "name": name,
        "type": account_type,
        "currency_code": currency_code,
    }
    if account_type == "asset":
        payload["account_role"] = "defaultAsset"
        if opening_balance:
            payload["opening_balance"] = opening_balance
            payload["opening_balance_date"] = "2026-10-01"

    r_post = client.post(f"{FIREFLY_URL}/api/v1/accounts", headers=HEADERS, json=payload)
    if r_post.status_code in (200, 201):
        return r_post.json()["data"]["id"]
    raise RuntimeError(f"Failed creating account {name}: {r_post.status_code} {r_post.text}")


def get_or_create_category(client: httpx.Client, name: str) -> str:
    r = client.get(f"{FIREFLY_URL}/api/v1/categories", headers=HEADERS)
    for cat in r.json().get("data", []):
        if cat["attributes"]["name"] == name:
            return cat["id"]

    r_post = client.post(f"{FIREFLY_URL}/api/v1/categories", headers=HEADERS, json={"name": name})
    if r_post.status_code in (200, 201):
        return r_post.json()["data"]["id"]
    raise RuntimeError(f"Failed creating category {name}: {r_post.status_code} {r_post.text}")


def create_transaction(client: httpx.Client, tx_type: str, description: str, date: str, amount: str, source_id: str, dest_id: str, category_name: str, notes: str, tags: list):
    payload = {
        "error_if_duplicate_hash": False,
        "apply_rules": False,
        "fire_webhooks": True,
        "transactions": [
            {
                "type": tx_type,
                "date": date,
                "amount": amount,
                "description": description,
                "source_id": source_id,
                "destination_id": dest_id,
                "category_name": category_name,
                "notes": notes,
                "tags": tags,
            }
        ],
    }
    r = client.post(f"{FIREFLY_URL}/api/v1/transactions", headers=HEADERS, json=payload)
    if r.status_code in (200, 201):
        tx_id = r.json()["data"]["id"]
        print(f"[OK] Transaction created: #{tx_id} - {description} ({amount} EUR)")
        return tx_id
    print(f"[ERR] Transaction failed: {description} -> {r.status_code}: {r.text}")
    return None


def run():
    with httpx.Client(timeout=30.0) as client:
        # 1. Accounts
        gls_account_id = get_or_create_account(
            client, "GLS Bank — Safer Space e.V. (Girokonto)", "asset", "EUR", "5000.00"
        )
        print(f"Asset Account ready: ID {gls_account_id}")

        rev_pretix_early = get_or_create_account(client, "Pretix Ticketing (Early Bird)", "revenue")
        rev_pretix_reg = get_or_create_account(client, "Pretix Ticketing (Regular Tier)", "revenue")
        rev_pretix_supp = get_or_create_account(client, "Pretix Ticketing (Supporter Tier)", "revenue")

        exp_equinox = get_or_create_account(client, "Equinox Event GmbH (Kaution)", "expense")
        exp_sound = get_or_create_account(client, "Nordic Sound & Light GmbH", "expense")
        exp_lineup = get_or_create_account(client, "Lika DJ Collective (4 Acts)", "expense")
        exp_sixt = get_or_create_account(client, "Sixt Rent-a-Car Altona", "expense")
        exp_catering = get_or_create_account(client, "Bio-Großmarkt Hamburg", "expense")
        exp_pretix_fees = get_or_create_account(client, "pretix.eu (Servicegebühren)", "expense")

        # 2. Categories
        get_or_create_category(client, "Fundraiser: Ticketing Revenue")
        get_or_create_category(client, "Fundraiser: Sound & Lighting")
        get_or_create_category(client, "Fundraiser: Artist Honorariums")
        get_or_create_category(client, "Fundraiser: Logistics & Transport")
        get_or_create_category(client, "Fundraiser: Care & Awareness")
        get_or_create_category(client, "Fundraiser: Venue Deposit & Turnover Guarantee")

        tags = ["fundraiser-hamburg-2026", "lika", "safer-space-ev", "pretix"]

        # 3. Transactions
        # Ticket revenues from Pretix
        create_transaction(
            client, "deposit", "Pretix Ticket Batch: Early Bird (80x 25€)", "2026-10-25", "2000.00",
            rev_pretix_early, gls_account_id, "Fundraiser: Ticketing Revenue",
            "Pretix Order Batch 1: Early Bird sold out. Mandatory consent confirmed for 80 attendees.", tags
        )
        create_transaction(
            client, "deposit", "Pretix Ticket Batch: Regular Tier (180x 35€)", "2026-11-05", "6300.00",
            rev_pretix_reg, gls_account_id, "Fundraiser: Ticketing Revenue",
            "Pretix Order Batch 2: Standard admission tier sold out. Mandatory consent confirmed for 180 attendees.", tags
        )
        create_transaction(
            client, "deposit", "Pretix Ticket Batch: Supporter Tier (60x 50€)", "2026-11-12", "3000.00",
            rev_pretix_supp, gls_account_id, "Fundraiser: Ticketing Revenue",
            "Pretix Order Batch 3: Community solidarity tier. Total capacity 320 reached.", tags
        )

        # Pretix fees deduction
        create_transaction(
            client, "withdrawal", "Pretix Platform & Payment Gateway Fees", "2026-11-21", "466.10",
            gls_account_id, exp_pretix_fees, "Fundraiser: Ticketing Revenue",
            "Pretix Service fee 2.5% + SEPA/Stripe gateway processing. Net disbursement was 10,833.90 EUR. Paperless: Pretix_Ticketing_Payout_Settlement.pdf", tags
        )

        # Equinox venue security deposit & turnover clause
        create_transaction(
            client, "withdrawal", "Equinox Club Hamburg — Sicherheitskaution (§ 3 Mietvertrag)", "2026-10-28", "1500.00",
            gls_account_id, exp_equinox, "Fundraiser: Venue Deposit & Turnover Guarantee",
            "Mietvertrag § 2: Mindestumsatzgarantie 7.500 EUR brutto an der Bar. Bei Erreichen sind Security (4 Kräfte) und Endreinigung inkludiert. Kaution 1.500 EUR wird nach Endabnahme erstattet. Paperless: Equinox_Hamburg_Venue_Lease_Contract.pdf", tags
        )

        # Nordic Sound & Light 12kW System
        create_transaction(
            client, "withdrawal", "Nordic Sound & Light — 12kW L-Acoustics & Lichtrigg", "2026-11-18", "2915.50",
            gls_account_id, exp_sound, "Fundraiser: Sound & Lighting",
            "Rechnung R-2026-8812. L-Acoustics PA, RoboWash Moving Heads, DJ Set, Traversen-Rigging und Techniker. Paperless: Sound_Visual_Rental_Invoice_Hamburg.pdf", tags
        )

        # DJ Honorariums
        create_transaction(
            client, "withdrawal", "Künstlergagen Lineup (Mira Luna, Klangtherapie, Soma, Aura)", "2026-11-20", "1750.00",
            gls_account_id, exp_lineup, "Fundraiser: Artist Honorariums",
            "Honorare für 4 DJ Acts (21:00-05:30 Uhr) gemäß Künstlervereinbarungen. Paperless: DJ_Booking_Agreements_Lineup.pdf", tags
        )

        # Sixt Transporter
        create_transaction(
            client, "withdrawal", "Sixt Transporter Altona (IVECO Daily 3.5t 48h)", "2026-11-19", "215.80",
            gls_account_id, exp_sixt, "Fundraiser: Logistics & Transport",
            "Mietvertragsnr. 948271014. Transport PA, Deko, Lichttraversen und Lika-Bühnenaufbauten. Paperless: Sixt_Transporter_Rental_Invoice.pdf", tags
        )

        # Bio-Großmarkt Hamburg
        create_transaction(
            client, "withdrawal", "Bio-Großmarkt Hamburg — Care Station Versorgung", "2026-11-19", "284.60",
            gls_account_id, exp_catering, "Fundraiser: Care & Awareness",
            "Beleg BG-89124. Bananen, Äpfel, Elektrolyte, vegane Snacks, Tee für Awareness Station & Cuddle Puddle. Paperless: Catering_Bar_Snacks_Receipt.pdf", tags
        )

        # Verify Account Balance
        r_acc = client.get(f"{FIREFLY_URL}/api/v1/accounts/{gls_account_id}", headers=HEADERS)
        bal = r_acc.json()["data"]["attributes"]["current_balance"]
        print(f"GLS Bank Account Current Balance: €{bal}")


def parse_args():
    parser = argparse.ArgumentParser(description="Populate Firefly III with Equinox Hamburg Fundraiser Financial Data")
    parser.add_argument("-i", "--instance", choices=["private", "community"], default=os.environ.get("KI_INSTANCE", "private"),
                        help="Target instance: private (port 8086) or community (port 9086). Default: private")
    parser.add_argument("-u", "--url", default=None, help="Explicit Firefly base URL (overrides --instance and FIREFLY_URL)")
    parser.add_argument("-t", "--token", default=None, help="Explicit Firefly API Bearer token")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    if args.url:
        FIREFLY_URL = args.url
    elif "FIREFLY_URL" in os.environ:
        FIREFLY_URL = os.environ["FIREFLY_URL"]
    else:
        FIREFLY_URL = f"http://127.0.0.1:{INSTANCE_PORTS[args.instance]}"

    if args.token:
        FIREFLY_TOKEN = args.token

    HEADERS["Authorization"] = f"Bearer {FIREFLY_TOKEN}"
    print(f"==> Connecting to Firefly III at: {FIREFLY_URL}")
    run()
