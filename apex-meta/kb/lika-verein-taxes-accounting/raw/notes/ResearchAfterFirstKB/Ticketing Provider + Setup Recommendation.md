# LIKA / Safer Space e.V. — Ticketing Provider + Setup Recommendation

## 0. Context basis

Safer Space / LIKA should treat this as a **non-charitable e.V. ticketing setup**, not as donation/fundraising tax relief. The project index defines the organisation as an eingetragener Verein in Hamburg, **nicht gemeinnützig**, without donation receipts, using EÜR, with VAT on invoices and KUR not as default assumption. It also warns not to silently apply Gemeinnützigkeit, Zweckbetrieb, Spendenbescheinigung, Übungsleiterpauschale, or Ehrenamtspauschale assumptions.

The concrete event file says Equinox has a venue capacity of **300–350**, with a recommended cap of **310–320**, venue-run bar/admission/security/cleaning, a **€7,500 minimum bar revenue**, and open clarifications around written capacity, security/cleaning inclusion, and exact minimum-bar-revenue calculation.

---

# 1. Recommendation

## 1.1 Best provider: **pretix**

**Recommendation status:** `recommended`

pretix is the best fit for LIKA because it has the clearest Germany-specific fiscal documentation, supports German invoice and e-invoice workflows, explicitly addresses GoBD/procedure documentation, logs configuration and transaction changes, and recommends offline exports because pretix itself should not be treated as the long-term archive. pretix also supports tax-rule configuration, invoices, payment provider integration, order/payment/refund lifecycle modelling, and data exporters.

**Why this matters for LIKA:**  
You need a ticketing system that behaves like an accounting source system, not only a sales page. pretix is the strongest option for “ticket as receipt / invoice field control + GoBD archive + refund trace + export discipline”.

**Main caveat:** pretix documentation is excellent operationally, but it does **not** decide LIKA’s tax law questions. VAT rate, support-tier wording, and whether any ticket PDF is sufficient as a Kleinbetragsrechnung must still be validation-gated.

---

## 1.2 Second-best option: **ticket.io**

**Recommendation status:** `acceptable / second-best`

ticket.io has good German event-ticketing fit and useful operational functions: DATEV export from Backstage, CSV order/sales reports, PDF invoices/payouts/credit notes, guest list tickets, buyer/ticket data fields, scan statistics, offline scanning, and payout after the event within 2–3 business days according to its FAQ.

**Why it is second-best:**  
It appears practical for German event organizers, but the public documentation I found is weaker than pretix for German fiscal requirements, GoBD/procedure documentation, and tax-rule/invoice setup depth.

---

## 1.3 Weak / avoid unless there is a strong non-accounting reason

|Provider|Status|Reason|
|---|---|---|
|**Eventbrite**|`weak for this case`|Good reporting and refund tools, but weaker Germany-specific GoBD/ticket-as-invoice documentation; more marketplace/provider-flow complexity.|
|**Rausgegangen / Event Zentrale**|`weak / only if discovery value matters`|Useful German cultural-event ecosystem and payout docs, but insufficient public evidence for detailed VAT/invoice/GoBD setup compared with pretix.|
|**TicketPAY**|`weak / needs demo confirmation`|Has organizer help categories and payout timing, but public docs found were not enough for invoice/VAT/GoBD/export confidence.|

---

# 2. Provider scores

```
provider_scores:  - provider: pretix    score_0_100: 89    best_for: "German VAT/invoice-aware ticketing, GoBD workflow documentation, export/archive discipline, tax-rule setup, refund lifecycle"    weakest_point: "Requires disciplined external archive; provider docs do not decide tax classification"    evidence_quality: "high"    recommendation_status: "recommended"  - provider: ticket.io    score_0_100: 73    best_for: "German event ticketing with DATEV export, CSV reports, post-event settlement, guest list and scan operations"    weakest_point: "Public docs weaker on German fiscal/GoBD/tax-rule setup than pretix"    evidence_quality: "medium"    recommendation_status: "acceptable"  - provider: Eventbrite    score_0_100: 62    best_for: "Broad event marketplace, simple setup, payout and sales reports"    weakest_point: "Weaker German-specific GoBD/invoice documentation; no clear DATEV path found"    evidence_quality: "medium"    recommendation_status: "weak"  - provider: Rausgegangen / Event Zentrale    score_0_100: 54    best_for: "Local culture-event reach and simple ticketing"    weakest_point: "Insufficient public documentation for tax-rule, invoice, GoBD and accounting-export confidence"    evidence_quality: "low-medium"    recommendation_status: "weak"  - provider: TicketPAY    score_0_100: 50    best_for: "German ticketing alternative if demo confirms export/invoice details"    weakest_point: "Public documentation found is not enough for implementation-ready accounting decision"    evidence_quality: "low-medium"    recommendation_status: "weak"
```

---

# 3. Provider comparison table

|Provider|German VAT / invoice support|Receipt customization|Refund / storno flow|Exports|Payout reporting|GoBD / audit support|Fees|Main risk|Citation|
|---|---|---|---|---|---|---|---|---|---|
|**pretix**|Strongest: Germany fiscal page, §14/§33 context, ZUGFeRD plugin support|Strong; invoice/tax settings and ticket/product configuration|Strong order lifecycle documentation covers orders, fees, payments, refunds, invoices|Strong; data exporters and API exporters|Depends on chosen payment provider / setup|Strongest: GoBD procedure docs, change logs, archive guidance|Hosted: 2.5% excl. tax, max €15/ticket + payment provider fees|Must export/archive externally; tax classification still external||
|**ticket.io**|Medium: German provider; docs show invoices, credit notes, payouts|Medium: custom ticket design front side; data fields configurable|Medium: refunds/cancellations via support, not fully self-service|Good: CSV order/sales reports; DATEV export|Good: sales overview + invoice; payout via Hyperwallet|Weak-medium: no strong GoBD docs found|Individual offer; system + payment fees|Less transparent fiscal documentation; refund process support-dependent||
|**Eventbrite**|Medium: tax setup and tax invoices supported where applicable|Medium|Good: organizer can issue full/partial refund; refund requests within 5 business days|Good: sales, payout, audit, channel/payment reports|Good: gross/net/refunds/fees/tax payout reports|Weak: no Germany-specific GoBD source found|Organizer pricing/fees; can pass fees to attendees|German audit/ticket-as-invoice uncertainty; provider-role complexity||
|**Rausgegangen**|Low-medium from public docs|Unknown / demo needed|AGB mentions ticket reversal fees|Payout/billing area mentioned|Payout by 7 working days / Stripe flow mentioned|Not enough public evidence|Ticketing fee calculated in setup|Good marketing fit may hide weak accounting evidence||
|**TicketPAY**|Unknown / demo needed|Unknown / demo needed|Unknown / demo needed|Unknown / demo needed|Payout 5 bank days after event initiated|Not enough public evidence|Unknown / demo needed|Insufficient public docs for this decision||

---

# 4. Required ticketing setup checklist

## 4.1 Before creating tickets

|Setup item|Required LIKA decision|
|---|---|
|**Organizer legal name**|`Safer Space e.V.`|
|**Organizer address**|Use registered Hamburg address from confirmed Stammdaten / tax setup.|
|**Seller role**|Confirm whether provider is agent/platform, merchant of record, or payment processor interface. Do **not** assume.|
|**VAT status**|Configure VAT as active; KUR should not be default.|
|**VAT rate**|Do not decide 7% vs 19% inside ticketing. Use finance/tax validation gate first.|
|**Ticket product names**|Use taxable product wording: e.g. `Eintritt Equinox`, `Eintritt Equinox Support Tier 1`, not “Donation Ticket”.|
|**Support tiers**|Model as taxable price tiers by default unless finance creates a legally separated voluntary contribution model.|
|**Capacity cap**|Set hard online cap at **310–320 max** until written venue confirmation allows more.|
|**Buyer fields**|Minimum: buyer name, email, order ID, ticket type, payment status; optional: invoice address for B2B/full invoice requests.|
|**Refund policy**|Define in the shop before launch: refund allowed/until date/manual approval/no refund.|
|**Archive owner**|Name one person responsible for exports, PDFs, screenshots and logs.|
|**Test order**|Required before launch. No public sale without acceptance test.|

The project KB already identifies ticketing setup, tax-rule configuration, payout reconciliation, refund/cancellation mapping and export requirements as the correct source cluster, while warning that provider docs are operational rather than legal authority.

---

## 4.2 Ticket receipt / Kleinbetragsrechnung fields

For tickets under €250 gross, the statutory small-invoice rule is the relevant working model: §33 UStDV requires at least the full name/address of the supplier, issue date, type/scope of service, and gross amount with tax rate or tax exemption note.

**Configure the ticket / receipt PDF to include:**

|Field|Example|
|---|---|
|Supplier|`Safer Space e.V.`|
|Address|`Spaldingstraße 43a, 20097 Hamburg`|
|Issue date|Purchase/order date|
|Service|`Eintritt Equinox / Fundraiser Hamburg am [Datum]`|
|Ticket tier|`Regular`, `Support Tier 1`, `Support Tier 2`|
|Gross amount|`xx,xx €`|
|VAT text|`inkl. [validierter Satz] % USt`|
|Order/ticket ID|Internal reconciliation ID|
|Payment status|Paid / pending / refunded / cancelled|
|Provider fee handling|Must be clear in export/reconciliation, not necessarily on public ticket|

For invoices above €250 or B2B cases, use a full invoice flow, not a simplified ticket receipt. IHK guidance distinguishes invoices above €250 from small-invoice simplifications.

---

# 5. Test order protocol

Run this **before public launch**.

```
test_order_protocol:  preconditions:    - "VAT rate placeholder replaced by finance-approved rate"    - "support tiers named as taxable ticket/product tiers"    - "capacity cap set to <= 310-320 unless written venue confirmation allows more"    - "refund policy published"    - "archive folder exists"  steps:    - step: 1      action: "Create one hidden/internal test ticket product."      evidence_to_archive:        - "screenshot of product settings"        - "screenshot of tax rule"        - "screenshot of capacity settings"    - step: 2      action: "Buy one test ticket with real or test-mode payment."      evidence_to_archive:        - "order confirmation PDF/email"        - "ticket PDF"        - "payment record"    - step: 3      action: "Inspect receipt/ticket fields."      acceptance_criteria:        - "Safer Space e.V. is the supplier shown"        - "address shown"        - "issue date shown"        - "event/service description shown"        - "gross amount shown"        - "VAT text shown"        - "order/ticket ID shown"    - step: 4      action: "Refund/cancel the test order."      acceptance_criteria:        - "original order remains traceable"        - "refund payment trace exists"        - "cancellation/storno/credit note trace exists if provider supports it"        - "order status changes are exportable"    - step: 5      action: "Export all relevant reports."      required_exports:        - "orders CSV"        - "tickets/attendees CSV"        - "payments CSV or payment provider export"        - "refunds/cancellations CSV"        - "invoice/receipt PDFs"        - "payout/settlement report if available"    - step: 6      action: "Archive everything."      required_archive_items:        - "PDFs"        - "CSV exports"        - "screenshots"        - "provider settings"        - "test result memo"
```

pretix is particularly strong here because it documents German audit readiness, procedure documentation, change logging, and the need to export invoices/order/payment data for long-term archive rather than treating pretix itself as the archive.

---

# 6. Accounting export minimum fields

|Field|Why needed|pretix|ticket.io|Eventbrite|
|---|---|---|---|---|
|Event ID / event name|Separate Equinox from future events|Yes|Yes|Yes|
|Order ID|Primary reconciliation key|Yes|Yes|Yes|
|Ticket ID|Door list and refund trace|Yes|Yes|Yes|
|Order date|Istversteuerung/payment timing check|Yes|Likely|Yes|
|Payment date|Bank/payout reconciliation|Yes|Likely|Yes|
|Buyer name/email|Order support, audit, B2B invoice follow-up|Yes|Yes|Yes|
|Ticket type/tier|Revenue by product, support-tier split|Yes|Yes|Yes|
|Quantity|Capacity and revenue reconciliation|Yes|Yes|Yes|
|Gross ticket price|Revenue basis|Yes|Yes|Yes|
|VAT rate|Tax calculation|Yes|Unclear from public docs|Yes, if tax enabled|
|VAT amount|USt reconciliation|Yes|Unclear from public docs|Yes, if tax enabled|
|Net amount|EÜR/accounting split|Yes|Unclear from public docs|Yes|
|Provider fee|Cost / fee invoice reconciliation|Yes, depending setup|Yes via settlement|Yes|
|Payment method|Stripe/PayPal/bank matching|Yes|Yes|Yes|
|Payment processor transaction ID|Bank/payment provider reconciliation|Yes, depending processor|Unclear|Yes/likely|
|Refund amount|Refund/storno accounting|Yes|Support-handled|Yes|
|Refund date|Correct period matching|Yes|Support-handled|Yes|
|Cancellation/storno status|Void/refund trace|Yes|Yes|Yes|
|Invoice/receipt number|Beleg chain|Yes|PDF docs mentioned|Tax invoice if enabled|
|Payout ID|Match provider payout to bank|Depends on processor|Yes/Hyperwallet flow|Yes|
|Payout date|Bank matching|Depends on processor|Yes|Yes|
|Net payout|Bank entry matching|Depends on processor|Yes|Yes|
|Export timestamp|GoBD/archive evidence|Yes if archived|Manual|Manual|

Eventbrite’s payout report is useful as a minimum benchmark because it explicitly includes gross and net sales and accounts for refunds, charges, credits, and tax. ticket.io’s FAQ explicitly says order overviews and sales reports can be downloaded as CSV and invoices, payouts and credit notes are provided as PDFs.

---

# 7. Provider document capture

```
provider_doc_capture:  - provider: pretix    docs_checked:      - topic: "Germany fiscal requirements / GoBD / archive / e-invoice"        last_updated_or_access_date: "accessed 2026-07-01"        claim_supported: "German fiscal page covers ZUGFeRD e-invoice support, GoBD procedure documentation, change logging, archiving/export recommendations."        citation: ":contentReference[oaicite:17]{index=17}"      - topic: "Tax rules"        last_updated_or_access_date: "accessed 2026-07-01"        claim_supported: "pretix can configure tax rules, including tax included or added on top."        citation: ":contentReference[oaicite:18]{index=18}"      - topic: "Order lifecycle"        last_updated_or_access_date: "accessed 2026-07-01"        claim_supported: "Order lifecycle documentation maps orders, order positions, fees, payments, refunds and invoices."        citation: ":contentReference[oaicite:19]{index=19}"      - topic: "Pricing"        last_updated_or_access_date: "accessed 2026-07-01"        claim_supported: "Hosted paid-ticket fee listed as 2.5% excl. taxes, max €15/ticket, plus payment provider fees."        citation: ":contentReference[oaicite:20]{index=20}"    missing_docs:      - "Exact recommended export package for LIKA without API use"      - "Exact payment processor payout mapping after chosen Stripe/PayPal/Mollie setup"  - provider: ticket.io    docs_checked:      - topic: "DATEV export"        last_updated_or_access_date: "accessed 2026-07-01"        claim_supported: "DATEV export exists in Backstage under Controlling -> Auszahlungen."        citation: ":contentReference[oaicite:21]{index=21}"      - topic: "Reporting and payout"        last_updated_or_access_date: "accessed 2026-07-01"        claim_supported: "CSV order/sales reports and PDF invoices, payouts, credit notes; statement 2–3 business days after event."        citation: ":contentReference[oaicite:22]{index=22}"      - topic: "Refunds/cancellations"        last_updated_or_access_date: "accessed 2026-07-01"        claim_supported: "Ticket cancellations/refunds handled by customer support."        citation: ":contentReference[oaicite:23]{index=23}"    missing_docs:      - "German VAT/tax-rule setup documentation"      - "GoBD/procedure documentation guidance"      - "Exact ticket-as-invoice fields"  - provider: Eventbrite    docs_checked:      - topic: "Tax setup and tax invoices"        last_updated_or_access_date: "accessed 2026-07-01"        claim_supported: "Organizer can add tax and enable tax invoices."        citation: ":contentReference[oaicite:24]{index=24}"      - topic: "Sales report"        last_updated_or_access_date: "accessed 2026-07-01"        claim_supported: "Sales summary covers ticket revenue, fees and taxes."        citation: ":contentReference[oaicite:25]{index=25}"      - topic: "Payout reports"        last_updated_or_access_date: "accessed 2026-07-01"        claim_supported: "Payout reports help reconcile gross/net sales, refunds, charges, credits and tax."        citation: ":contentReference[oaicite:26]{index=26}"      - topic: "Refunds"        last_updated_or_access_date: "accessed 2026-07-01"        claim_supported: "Organizer can issue full or partial refund; refund requests should be handled within five business days."        citation: ":contentReference[oaicite:27]{index=27}"    missing_docs:      - "Germany-specific GoBD/procedure documentation"      - "DATEV export"      - "Clear German ticket-as-Kleinbetragsrechnung implementation"
```

---

# 8. Final provider setup decision packet

```
7_final_provider_setup_decision_packet:  recommended_provider: "pretix"  second_best_provider: "ticket.io"  do_not_use_as_default:    - provider: "Eventbrite"      reason: "Useful reports, but weaker German GoBD/accounting setup evidence."    - provider: "Rausgegangen / TicketPAY"      reason: "Could be useful, but public documentation was insufficient for audit-safe accounting decision."  exact_setup_steps_before_launch:    - "Create pretix organizer as Safer Space e.V."    - "Enter legal address and tax details."    - "Configure payment provider deliberately: Stripe/PayPal/bank transfer etc."    - "Create event: Equinox / Fundraiser Hamburg."    - "Set hard capacity cap <= 310-320 until written venue confirmation."    - "Create ticket products as taxable tickets/product tiers."    - "Avoid 'Donation Ticket' wording."    - "Configure VAT rule only after finance validation."    - "Configure receipt/invoice fields."    - "Enable invoice/receipt generation for every order where possible."    - "Set refund policy."    - "Create export/archive folder."    - "Run test order protocol."    - "Archive test-order packet."    - "Only then launch public sales."  test_order_acceptance_criteria:    - "Ticket PDF contains Safer Space e.V., address, issue date, service, gross amount, VAT text, order/ticket ID."    - "Order appears in order export."    - "Payment appears in payment/provider export."    - "Refund creates traceable status/payment/storno evidence."    - "Exports can reconcile gross sales, fees, VAT, refunds and net payout."    - "All test evidence archived as PDF/CSV/screenshots."  export_archive_sop:    during_sales:      - "Weekly export orders, payments, invoices/receipts, refunds/cancellations."      - "After every configuration change, save screenshot or settings export."    before_event:      - "Export final door list."      - "Export sold ticket count by ticket type."      - "Export unpaid/cancelled/refunded orders."    after_event:      - "Export final orders, attendee list, payments, refunds, invoices, payout reports."      - "Save payment processor statement."      - "Save bank statement matching payout."      - "Save archive index and reconciliation memo."  refund_storno_sop:    - "Never delete accounting evidence."    - "Keep original order/ticket record."    - "Record refund reason, approver, date, amount."    - "Export refund/cancellation report."    - "Archive original receipt/invoice, cancellation/storno evidence, payment refund trace."    - "Reconcile refund to payout/bank/payment processor."  finance_owner_validation_gates:    - "VAT rate: 7% vs 19%."    - "Support-tier wording: taxable product tier vs legally separated voluntary contribution."    - "Ticket PDF as Kleinbetragsrechnung acceptance."    - "B2B/full invoice path for tickets >250 EUR or business buyers."    - "Provider role: platform/agent vs merchant of record."    - "Payment processor fee invoice and reverse-charge risk."    - "Venue minimum-bar-revenue treatment."  provider_docs_still_missing:    - "Final pretix export package after exact payment provider choice."    - "Written provider/contract confirmation of seller/merchant role."    - "Exact payment processor payout timing and fee invoice flow."    - "Tax advisor acceptance of ticket receipt fields."  decision_confidence_0_100: 86
```

---

# 9. Open questions for finance owner

- [ ]  Which VAT rate should be configured for the ticket products?
- [ ]  Should all optional extra amounts be taxable support tiers by default?
- [ ]  Is any legally separated voluntary contribution planned at all?
- [ ]  Should ticket PDFs be intended as Kleinbetragsrechnungen for B2C buyers under €250?
- [ ]  What is the full invoice process for B2B buyers or tickets/orders above €250?
- [ ]  Who is the legal seller shown on the receipt: Safer Space e.V. or provider?
- [ ]  Which payment processor will be used?
- [ ]  Are provider fees invoiced separately or netted from payout?
- [ ]  Are provider/payment processor invoices domestic, EU reverse charge, or otherwise?
- [ ]  How often must exports be archived during sales?
- [ ]  Who signs off the first test order before launch?
- [ ]  What refund cutoff and refund approval rule should be published?
- [ ]  What written venue confirmation is still needed for capacity and minimum bar revenue?

**Bottom line:** Use **pretix**, configure support options as **taxable ticket tiers**, cap tickets at **310–320 until written capacity confirmation**, run a real test order/refund/export cycle, and launch only after the finance owner signs off VAT wording and receipt fields.