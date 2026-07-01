Executed. Below is the implementation memo for **Task 106 — purchase, reimbursement, invoice-intake and expense archive infrastructure**.

# LIKA / Safer Space e.V. — Purchase, Reimbursement & Expense Archive Memo

**Scope:** Equinox / Fundraiser Hamburg.  
**Status:** workflow design, not final tax/legal advice.  
**Core assumption:** Safer Space e.V. is treated as a non-charitable e.V. with event-related economic activity, EÜR, VAT on invoices, and no donation receipts. The Satzung also requires Vereinsmittel to be used only for statutory purposes, prohibits member benefits from association funds, and prohibits purpose-foreign or disproportionately high payments.

The existing KB already ranks **invoice requirements, Kleinbetragsrechnung, GoBD archive, E-Rechnung, KSK, and reverse-charge checks** as core source clusters, while warning that generic Vereins-/Ehrenamts templates are often contaminated by Gemeinnützigkeit assumptions. The previous APEX packet also identifies GoBD/archive, invoice/receipt fields, E-Rechnung intake, ticketing exports, and foreign-services checks as strong workflow domains.

---

# 1. Executive recommendation

## 1.1 Minimum viable purchase policy

Safer Space should run **all Equinox expenses through one controlled expense lane**:

|Layer|Rule|
|---|---|
|**Before purchase**|Every expense needs a purchase request ID before money is spent.|
|**Preferred payment**|Supplier invoice to Safer Space e.V. or association bank/card payment.|
|**Private outlay**|Allowed only as Ausnahme, with prior approval and reimbursement form.|
|**Cash**|Strongly discouraged; emergency-only and capped.|
|**Receipt standard**|Original receipt/invoice + payment proof + event allocation.|
|**Archive**|Store original file format, link every log row to file path, freeze closeout packet.|
|**Foreign/digital services**|Meta Ads, Canva, Google, Eventbrite, Stripe, foreign SaaS: always reverse-charge / §13b validation flag.|

## 1.2 Recommended approval thresholds

These are internal governance thresholds, not statutory thresholds.

|Amount / case|Approval before purchase|Required document standard|Notes|
|--:|---|---|---|
|**0–50 €**|Category owner approval|Receipt or Kleinbetragsrechnung + purpose note|Only within pre-approved budget category.|
|**50–150 €**|Finance owner approval|Receipt/invoice + payment proof|Private card allowed only if pre-approved.|
|**150–250 €**|Finance + event lead approval|Proper receipt/invoice; check VAT data|250 € is important because simplified Kleinbetragsrechnung rules end there. §33 UStDV applies only up to 250 € gross. ([gesetze.co](https://gesetze.co/DE/UStDV/33 "§ 33 UStDV – Rechnungen über Kleinbeträge \| Gesetze.co"))|
|**>250 €**|Finance + board/treasurer approval|Full invoice to Safer Space e.V.|Full invoice fields under §14 UStG should be required. ([Buzer](https://www.buzer.de/14_UStG.htm "§ 14 UStG Ausstellung von Rechnungen Umsatzsteuergesetz"))|
|**>500 €**|Board/treasurer approval|Quote/order confirmation + full invoice + payment proof|No private card unless explicitly approved.|
|**Recurring/subscription**|Finance owner + board approval|Contract/account screenshot + invoice + cancellation owner|Includes Canva, Google Workspace, Meta tools, ticketing tools.|
|**Foreign supplier / no German VAT**|Finance owner + accountant gate|Invoice + country + VAT ID + reverse-charge flag|§13b / reverse charge must be checked. ([Buzer](https://www.buzer.de/13b_UStG.htm "§ 13b UStG Leistungsempfänger als Steuerschuldner Umsatzsteuergesetz"))|
|**Merch/sales items**|Board/finance approval|Purchase invoice + inventory/sales log|Extra VAT/inventory risk.|
|**Cash purchase**|Emergency only, max 50 € regular / 100 € absolute event-night emergency|Receipt + emergency reason + two-person signoff|No repeated cash workarounds.|

## 1.3 What to ban or avoid

|Ban / avoid|Reason|
|---|---|
|**No undocumented reimbursements**|Reimbursement without proof can look like hidden compensation.|
|**No “Spende” wording for reimbursements or ticket support tiers**|Safer Space is not operating on donation-receipt logic.|
|**No private Meta/Canva/Eventbrite accounts for event spending**|Invoice recipient, VAT country, payment proof and account ownership become messy.|
|**No cash purchases without receipt**|Eigenbeleg only as emergency fallback; it does not safely support Vorsteuer.|
|**No personal reward/benefit purchases**|Satzung risk: Vereinsmittel must serve statutory purposes.|
|**No foreign SaaS/ads without reverse-charge flag**|Foreign B2B services can shift VAT liability to Safer Space. ([IHK](https://www.ihk.de/stuttgart/fuer-unternehmen/recht-und-steuern/steuerrecht/umsatzsteuer-international/dienstleistungen/steuerschuldnerschaft-684826 "Steuerschuldumkehr beim Bezug von Leistungen / Werklieferungen<br>- IHK Region Stuttgart"))|
|**No paper-only archive**|GoBD/document access requires structured, traceable digital archive logic. ([Bundesministerium der Finanzen](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Weitere_Steuerthemen/Abgabenordnung/AO-Anwendungserlass/2024-03-11-aenderung-gobd.html "Bundesfinanzministerium  - Grundsätze zur ordnungsmäßigen Führung und Aufbewahrung von Büchern, Aufzeichnungen und Unterlagen in elektronischer Form sowie zum Datenzugriff (GoBD); Änderung aufgrund verschiedener gesetzlicher Änderungen"))|

## 1.4 Validate with accountant before spending starts

|Validation gate|Why|
|---|---|
|**Vorsteuer eligibility by category**|Vorsteuer requires proper invoice and business use; §15 UStG requires a compliant invoice under §§14/14a UStG. ([Gesetze im Internet](https://www.gesetze-im-internet.de/ustg_1980/__15.html?utm_source=chatgpt.com "§ 15 UStG - Einzelnorm - Gesetze im Internet"))|
|**Reverse charge for Meta Ads / Canva / Google / Eventbrite / Stripe**|Foreign supplier services may trigger §13b. ([Buzer](https://www.buzer.de/13b_UStG.htm "§ 13b UStG Leistungsempfänger als Steuerschuldner Umsatzsteuergesetz"))|
|**Food/drinks/welcome materials**|Risk of private benefit, hospitality, mixed-use, or non-deductible treatment.|
|**Merchandise/sales items**|Inventory, sales VAT, price display, cash/card collection and stock loss need a separate mini-process.|
|**E-Rechnung intake**|Entrepreneurial Vereins activity must be able to receive E-Rechnungen; BMF explicitly says this applies to Vereine where they act entrepreneurially. ([Bundesministerium der Finanzen](https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html "Bundesfinanzministerium  - Fragen und Antworten zur Einführung der obligatorischen (verpflichtenden) E-Rechnung zum 1. Januar 2025"))|

## 1.5 Minimum owner roles

|Role|Person/function|
|---|---|
|**Finance owner**|Owns purchase approvals, reimbursement review, invoice log, accountant handoff.|
|**Archive owner**|Owns folder tree, file naming, original preservation, closeout packet.|
|**Event ops owner**|Confirms operational need and emergency purchases.|
|**Budget owner**|Maintains category budget and remaining spend.|
|**Tool/account owner**|Owns Meta/Canva/Google/ticketing account access, invoices, payment methods.|
|**Board/treasurer gate**|Approves >250 €, recurring, foreign, merch, and high-risk spending.|

---

# 2. Purchase policy

## 2.1 Before-purchase workflow

```yaml
before_purchase_workflow:
  trigger: "Any team member wants to buy something for Equinox"
  steps:
    - "Open purchase request row."
    - "Assign PR-ID."
    - "Choose category: decoration, printing, ads, software, transport, props, merch, food/drink, other."
    - "Enter supplier, amount estimate, VAT shown or unknown, payment method."
    - "State event purpose in one sentence."
    - "Mark flags: foreign supplier, subscription, cash, private card, merch, food/drink, >250 EUR."
    - "Get approval according to threshold."
    - "Only then purchase."
  done_when:
    - "PR-ID exists."
    - "Approval is recorded."
    - "Archive folder placeholder exists."
```

## 2.2 After-purchase workflow

```yaml
after_purchase_workflow:
  deadline: "48 hours after purchase; 24 hours after event-night emergency purchase"
  steps:
    - "Upload original receipt/invoice."
    - "Upload payment proof: bank/card/PayPal/Stripe/Meta transaction."
    - "Rename file using convention."
    - "Attach file path to purchase log."
    - "If private payment: submit reimbursement claim."
    - "Finance owner checks invoice fields and VAT."
    - "Finance owner approves reimbursement or requests correction."
    - "Payment made only by bank transfer, not cash."
    - "Archive owner marks row as complete."
  done_when:
    - "Receipt/invoice, payment proof, approval and event allocation are linked in the log."
```

## 2.3 Emergency purchase rule

```yaml
emergency_purchase_rule:
  allowed_only_if:
    - "Needed for event safety, setup, operations or promised guest experience."
    - "Waiting for normal approval would materially harm the event."
  cap:
    normal_cash_or_private_emergency: "50 EUR"
    absolute_event_night_exception: "100 EUR"
  approval:
    - "Two-person approval in chat: event ops owner + finance owner or board member."
  documentation:
    - "Photo of receipt immediately."
    - "Reason for emergency."
    - "Reimbursement claim within 24 hours."
  not_allowed:
    - "Alcohol/private consumption"
    - "crew rewards"
    - "unplanned artist/crew fees"
    - "foreign SaaS/subscription purchases"
```

## 2.4 Forbidden purchase cases

|Case|Rule|
|---|---|
|Personal clothing, private cosmetics, private meals|Not reimbursable unless explicitly event-material and pre-approved.|
|Alcohol for internal team|Ban unless part of a documented sales/welcome concept and accountant-approved.|
|Tips without receipt/context|Ban except minor documented Eigenbeleg edge case; no Vorsteuer.|
|Foreign online ads bought from private account|Ban. Use Verein-controlled account only.|
|“Thanks for helping” flat payments|Ban as reimbursement; this is compensation/payroll/fee classification.|
|Repeated lost receipts|Escalate; reimbursement can be refused.|
|Purchases outside event purpose|Refuse under Satzung governance.|

---

# 3. Reimbursement SOP — Auslagenersatz

## SOP block

```yaml
sop_reimbursement:
  purpose: "Reimburse only actual, necessary, documented event expenses."
  legal_baseline: "Aufwendungsersatz logic: necessary expenses made for an assigned purpose can be reimbursed; §670 BGB states that necessary expenses made to execute an Auftrag must be reimbursed by the Auftraggeber."
  source: "§670 BGB"
```

§670 BGB is the legal anchor for Aufwendungsersatz logic: necessary expenses made for executing an assignment are reimbursable by the principal. ([Buzer](https://www.buzer.de/670_BGB.htm "§ 670 BGB Ersatz von Aufwendungen Bürgerliches Gesetzbuch")) For Safer Space, this should be operationalized narrowly: reimbursement is for **actual costs**, not time, labor, appreciation, or hidden compensation.

## 3.1 Who can claim

|Claimant|Allowed?|Conditions|
|---|---|---|
|Vereinsmitglied|Yes|Pre-approved purchase or emergency rule.|
|Internal volunteer/team member|Yes|Same evidence standard; no compensation hidden as reimbursement.|
|Board member|Yes|Same evidence standard; avoid self-approval.|
|External supplier|No reimbursement form|Supplier invoice route, not Auslagenersatz.|
|Paid helper/contractor|Separate classification|Must not mix invoice/fee and volunteer reimbursement without review.|

## 3.2 Required documents

|Required|Detail|
|---|---|
|Reimbursement form|Claimant, PR-ID, amount, category, bank details, declaration.|
|Original receipt/invoice|Photo/PDF/XML, readable, complete.|
|Payment proof|Card statement, bank transfer, PayPal/Stripe/Meta transaction, cash note.|
|Event purpose|Short purpose line: “Decoration material for Equinox stage entrance.”|
|Approval evidence|Screenshot/chat/approval field.|
|File links|Archive path for every document.|

## 3.3 Receipt/invoice quality

|Amount|Minimum requirement|
|--:|---|
|**Up to 250 € gross**|Kleinbetragsrechnung can be sufficient if it includes supplier name/address, date, type/scope of supply/service, gross amount with VAT amount/rate or exemption note. ([gesetze.co](https://gesetze.co/DE/UStDV/33 "§ 33 UStDV – Rechnungen über Kleinbeträge \| Gesetze.co"))|
|**Above 250 € gross**|Full invoice under §14 UStG with supplier and recipient name/address, tax number or VAT ID, invoice date, invoice number, performance description, delivery/service date, net/VAT/gross and VAT rate. ([Buzer](https://www.buzer.de/14_UStG.htm "§ 14 UStG Ausstellung von Rechnungen Umsatzsteuergesetz"))|
|**Vorsteuer intended**|Check invoice is formally correct and the purchase is for the entrepreneurial/event activity; §15 UStG requires a compliant invoice for Vorsteuer. ([Gesetze im Internet](https://www.gesetze-im-internet.de/ustg_1980/__15.html?utm_source=chatgpt.com "§ 15 UStG - Einzelnorm - Gesetze im Internet"))|
|**Foreign supplier**|No reimbursement until reverse-charge/accountant flag is cleared.|

## 3.4 Deadline

|Situation|Deadline|
|---|--:|
|Normal purchase|Submit within 7 days.|
|Event-week purchase|Submit within 48 hours.|
|Event-night emergency|Submit within 24 hours.|
|Final cutoff|No later than 7 days after event closeout start.|

## 3.5 Approval and payment

```yaml
approval_payment:
  reviewer_1: "category/event ops owner confirms event purpose"
  reviewer_2: "finance owner checks receipt, VAT, payment proof, threshold"
  payment_method: "bank transfer only"
  payment_reference: "EQX-REIMB-[claim_id]-[claimant]"
  no_cash_reimbursement: true
  self_approval_forbidden: true
```

## 3.6 Archive

```yaml
archive_done_when:
  - "Claim form saved."
  - "Receipt/invoice saved."
  - "Payment proof saved."
  - "Bank transfer proof saved."
  - "Expense log row links all files."
  - "Status = reimbursed / rejected / correction needed."
```

---

# 4. Incoming invoice checklist

## 4.1 Standard invoice check

|Check item|Required?|Notes|
|---|--:|---|
|Supplier name/address|Yes|Full legal supplier identity.|
|Safer Space legal name/address|Yes for full invoice|Use “Safer Space e.V.” and current address.|
|Invoice date|Yes|Required.|
|Invoice number|Yes for full invoice|Fortlaufende/eindeutige number under §14.|
|Supplier tax number or VAT ID|Yes for full invoice|Required under §14.|
|Leistungsdatum / service date|Yes for full invoice|Or period.|
|Description|Yes|Must clearly identify service/material.|
|Net amount|Yes for full invoice|Needed for VAT check.|
|VAT amount and VAT rate|Yes if German VAT charged|Check rate and calculation.|
|Gross amount|Yes|Match payment.|
|Kleinbetragsrechnung rule|Only ≤250 €|Reduced fields allowed under §33 UStDV. ([gesetze.co](https://gesetze.co/DE/UStDV/33 "§ 33 UStDV – Rechnungen über Kleinbeträge \| Gesetze.co"))|
|E-Rechnung format|If German B2B and no exception/transition applies|XML/structured part must be preserved. BMF says PDF alone is no longer an E-Rechnung from 2025. ([Bundesministerium der Finanzen](https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html "Bundesfinanzministerium  - Fragen und Antworten zur Einführung der obligatorischen (verpflichtenden) E-Rechnung zum 1. Januar 2025"))|
|Payment proof|Always|Bank/card/processor proof.|
|Event allocation|Always|Equinox / category / cost center.|
|Reverse-charge flag|If foreign/no German VAT/digital service|Check §13b. ([Buzer](https://www.buzer.de/13b_UStG.htm "§ 13b UStG Leistungsempfänger als Steuerschuldner Umsatzsteuergesetz"))|
|Approval before payment|Always|Finance owner approves payment.|

## 4.2 Minimum invoice-intake workflow before payment

```yaml
invoice_intake_before_payment:
  steps:
    - "Receive invoice only via finance mailbox or upload form."
    - "Assign INV-ID."
    - "Save original PDF/XML/email attachment unchanged."
    - "Log supplier, amount, VAT, due date, category, event allocation."
    - "Run invoice checklist."
    - "If German B2B E-Rechnung: store XML/ZUGFeRD/XRechnung structured part."
    - "If foreign supplier: set reverse-charge/accountant flag."
    - "Approval by finance owner."
    - "Payment by bank transfer from Verein account."
    - "Save payment proof and mark paid."
```

For E-Rechnung, BMF states that entrepreneurial Vereins activity falls under the general E-Rechnung rules; the Verein must then be able to receive E-Rechnungen and may need to issue them unless exceptions or transition rules apply. ([Bundesministerium der Finanzen](https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html "Bundesfinanzministerium  - Fragen und Antworten zur Einführung der obligatorischen (verpflichtenden) E-Rechnung zum 1. Januar 2025")) E-Rechnung archives must preserve at least the structured part in its original form. ([Bundesministerium der Finanzen](https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html "Bundesfinanzministerium  - Fragen und Antworten zur Einführung der obligatorischen (verpflichtenden) E-Rechnung zum 1. Januar 2025"))

---

# 5. Expense category matrix

|Category|Allowed?|Approval needed?|Required receipt/invoice|VAT/Vorsteuer note|Archive folder|Risk|
|---|---|---|---|---|---|---|
|**Decoration**|Yes|≤50 category owner; >50 finance; >250 board/finance|Receipt ≤250; full invoice >250|Vorsteuer only with proper invoice and event use|`03_expenses/decoration`|Medium: private benefit / vague purpose|
|**Printing/flyers/posters**|Yes|Finance approval; >250 board/finance|Supplier invoice preferred|Usually clean if invoice to Verein|`03_expenses/printing`|Low/medium|
|**Online ads**|Yes, controlled account only|Finance + tool owner; foreign flag always|Platform invoice + payment proof + campaign screenshot|Meta/foreign platforms may trigger reverse charge|`03_expenses/ads`|High|
|**Software/tools**|Yes if event/business purpose|Finance + board if recurring|Invoice + contract/account screenshot|Foreign SaaS reverse-charge check|`03_expenses/software`|High if private account|
|**Transport**|Yes if event-related|≤50 category owner; >50 finance|Ticket/receipt; mileage form if private car|Parking/taxi receipts often Kleinbetragsrechnung; private mileage no Vorsteuer|`03_expenses/transport`|Medium|
|**Food/drinks**|Restricted|Finance + event lead; accountant if material|Invoice/receipt + purpose + recipients/usage|Hospitality/private benefit risk; no casual team meals|`03_expenses/food_drinks`|High|
|**Props/materials**|Yes|Same as decoration|Receipt/invoice + event purpose|Vorsteuer if proper invoice and business use|`03_expenses/props_materials`|Medium|
|**Merchandise/sales items**|Only with separate sales workflow|Board/finance before purchase|Full invoice preferred + inventory log|Sales VAT/inventory needed|`03_expenses/merch_sales`|High|
|**Cash purchases**|Emergency-only|Event ops + finance; max 50/100|Receipt mandatory; Eigenbeleg only fallback|No Vorsteuer from Eigenbeleg as default|`03_expenses/cash_emergency`|High|

---

# 6. Form templates — field lists

## 6.1 Purchase request form

```yaml
purchase_request_form:
  fields:
    - PR-ID
    - request_date
    - requester_name
    - requester_role
    - category
    - supplier_name
    - supplier_country
    - supplier_website
    - expected_amount_gross
    - expected_vat_rate
    - foreign_supplier_flag
    - reverse_charge_flag
    - subscription_or_recurring_flag
    - cash_or_private_card_flag
    - merch_or_sales_item_flag
    - food_drink_flag
    - event_purpose
    - budget_line
    - payment_method
    - approval_required_level
    - approver_1
    - approver_2
    - approval_timestamp
    - archive_folder_link
    - status
```

## 6.2 Reimbursement claim form

```yaml
reimbursement_claim_form:
  fields:
    - claim_id
    - linked_PR-ID
    - claimant_name
    - claimant_role
    - claimant_email
    - claimant_IBAN
    - purchase_date
    - supplier
    - amount_gross
    - currency
    - payment_method_used
    - category
    - event_purpose
    - receipt_file_link
    - payment_proof_link
    - VAT_shown_yes_no
    - VAT_rate
    - foreign_supplier_flag
    - cash_purchase_flag
    - emergency_purchase_reason
    - claimant_declaration_actual_expense_no_compensation
    - reviewer_ops
    - reviewer_finance
    - approval_status
    - reimbursement_payment_date
    - bank_transfer_reference
```

## 6.3 Lost receipt declaration / Eigenbeleg

```yaml
lost_receipt_declaration:
  allowed_only_as: "emergency fallback"
  fields:
    - eigenbeleg_id
    - claimant_name
    - date_of_expense
    - supplier_or_payee
    - place
    - amount
    - currency
    - category
    - exact_business_event_purpose
    - why_original_receipt_missing
    - attempts_to_get_duplicate
    - payment_proof_link
    - supporting_evidence_links
    - no_Vorsteuer_claim_default
    - claimant_signature
    - finance_owner_decision
```

Eigenbelege should be treated only as exceptions. Secondary practice sources consistently describe them as emergency fallback when no external receipt exists; they also warn that Vorsteuer generally requires a proper invoice, not a self-made receipt. ([rechnungswesen-portal.de](https://www.rechnungswesen-portal.de/Fachinfo/Steuern/Der-Eigenbeleg-Letzte-Rettung-fuer-den-Steuerabzug.html?utm_source=chatgpt.com "Der Eigenbeleg - Letzte Rettung für den Steuerabzug"))

## 6.4 Invoice intake log

```yaml
invoice_intake_log:
  fields:
    - INV-ID
    - received_date
    - supplier_name
    - supplier_country
    - supplier_tax_id_or_vat_id
    - invoice_number
    - invoice_date
    - service_date_or_period
    - category
    - event_allocation
    - amount_net
    - vat_rate
    - vat_amount
    - amount_gross
    - currency
    - reverse_charge_flag
    - e_rechnung_flag
    - file_original_link
    - xml_structured_part_link
    - visual_pdf_link
    - approval_status
    - due_date
    - payment_date
    - payment_proof_link
    - accounting_notes
    - accountant_validation_needed
```

## 6.5 Expense closeout checklist

```yaml
expense_closeout_checklist:
  fields:
    - all_PRs_closed
    - all_reimbursements_paid_or_rejected
    - all_invoices_paid_or_accrued
    - all_payment_proofs_linked
    - all_foreign_supplier_flags_reviewed
    - all_cash_expenses_reviewed
    - all_E-Rechnung_XML_files_preserved
    - all_original_receipts_preserved
    - missing_documents_list
    - exception_approvals
    - category_totals
    - VAT_input_tax_summary
    - accountant_question_log
    - archive_locked_date
```

---

# 7. Archive integration

## 7.1 Folder structure

```text
/equinox_fundraiser_hamburg/
  00_admin/
    approvals/
    board_decisions/
    policies/
  01_budget_purchase_requests/
  02_incoming_invoices/
    german_suppliers/
    foreign_suppliers_reverse_charge_review/
    e_rechnung_xml/
  03_reimbursements/
    submitted/
    approved_paid/
    rejected_or_correction_needed/
  04_receipts_by_category/
    decoration/
    printing/
    ads/
    software/
    transport/
    food_drinks/
    props_materials/
    merch_sales/
    cash_emergency/
  05_payment_proof/
    bank/
    card/
    paypal_stripe_meta/
  06_ticketing_exports/
  07_venue_settlement/
  08_inventory_merch_sales/
  09_accountant_validation/
  10_closeout_packet/
  99_originals_locked/
```

## 7.2 File naming convention

```text
YYYYMMDD_EQX_[DOC-TYPE]_[CATEGORY]_[SUPPLIER]_[GROSS-EUR]_[PR-or-INV-or-CLAIM-ID]_[v01].ext
```

Examples:

```text
20261105_EQX_RECEIPT_DECORATION_Bauhaus_48-37_PR-004.pdf
20261107_EQX_INVOICE_PRINTING_Flyeralarm_312-90_INV-009.pdf
20261108_EQX_PAYMENTPROOF_ADS_Meta_150-00_INV-014.png
20261110_EQX_ERECHNUNG_SOFTWARE_GoogleWorkspace_29-75_INV-016.xml
```

## 7.3 Original preservation

Electronic records should be kept in their original format and backed up; IHK’s GoBD guidance explicitly recommends saving electronic receipts in the original format and maintaining current Verfahrensdokumentation and backups. ([ihk-muenchen.de](https://www.ihk-muenchen.de/ratgeber/steuern/finanzverwaltung/grundsaetze-elektronische-buchfuehrung-gobd/ "Ordnungsgemäße Buchführung: GoBD | IHK München")) BMF’s GoBD page is the primary official anchor for electronic records and data access; the updated GoBD were published as a BMF letter dated 11 March 2024. ([Bundesministerium der Finanzen](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Weitere_Steuerthemen/Abgabenordnung/AO-Anwendungserlass/2024-03-11-aenderung-gobd.html "Bundesfinanzministerium  - Grundsätze zur ordnungsmäßigen Führung und Aufbewahrung von Büchern, Aufzeichnungen und Unterlagen in elektronischer Form sowie zum Datenzugriff (GoBD); Änderung aufgrund verschiedener gesetzlicher Änderungen"))

## 7.4 Paper receipts

```yaml
paper_receipt_handling:
  steps:
    - "Photograph or scan immediately."
    - "Upload scan/photo within 48 hours."
    - "Store physical original in event envelope by claim ID."
    - "Do not destroy paper originals unless a documented ersetzendes-Scannen process exists."
    - "At closeout, reconcile physical envelope against digital log."
```

## 7.5 E-Rechnung / ZUGFeRD / XRechnung

```yaml
e_rechnung_handling:
  receive:
    - "Use finance mailbox capable of receiving XML/PDF attachments."
  store:
    - "Save original XML or ZUGFeRD PDF unchanged."
    - "If visualized, store viewer PDF separately as convenience copy."
  validate:
    - "Check supplier, amount, VAT, performance date, buyer data."
  archive:
    - "Structured part is authoritative for hybrid invoices."
```

BMF explains that since 2025 a simple PDF is no longer an E-Rechnung because it is not structured; typical compliant German formats include XRechnung and ZUGFeRD from version 2.0.1, and validation can help catch missing or illogical invoice data. ([Bundesministerium der Finanzen](https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html "Bundesfinanzministerium  - Fragen und Antworten zur Einführung der obligatorischen (verpflichtenden) E-Rechnung zum 1. Januar 2025"))

## 7.6 Event closeout packet

```yaml
event_closeout_packet:
  contents:
    - purchase_request_log_final.csv
    - reimbursement_log_final.csv
    - invoice_intake_log_final.csv
    - category_summary.xlsx_or_csv
    - missing_documents_exception_log.md
    - foreign_supplier_reverse_charge_review.md
    - cash_emergency_review.md
    - all_bank_payment_proofs
    - all_E-Rechnung_XML_files
    - all_original_receipts_or_scans
    - accountant_validation_questions.md
    - finance_owner_signoff.md
```

---

# 8. Source table

|Topic|Source|Authority|Use|Citation|
|---|---|--:|---|---|
|Safer Space purpose / no member benefits|Vereinssatzung|Internal governing document|Purchase policy boundary||
|Existing KB source ranking|Quellenanalyse Safer Space|Internal KB synthesis|Source priority and risk filters||
|APEX event operating model|LIKA APEX report|Internal execution packet|Archive/ticketing/settlement task dependencies||
|Aufwendungsersatz|§670 BGB|Legal text|Reimbursement baseline|([Buzer](https://www.buzer.de/670_BGB.htm "§ 670 BGB Ersatz von Aufwendungen Bürgerliches Gesetzbuch"))|
|Full invoices|§14 UStG|Legal text|Incoming invoice checklist >250 €|([Buzer](https://www.buzer.de/14_UStG.htm "§ 14 UStG Ausstellung von Rechnungen Umsatzsteuergesetz"))|
|Kleinbetragsrechnung|§33 UStDV|Legal text|Receipts up to 250 €|([gesetze.co](https://gesetze.co/DE/UStDV/33 "§ 33 UStDV – Rechnungen über Kleinbeträge \| Gesetze.co"))|
|Vorsteuer requirement|§15 UStG|Legal text|Proper invoice needed for input VAT|([Gesetze im Internet](https://www.gesetze-im-internet.de/ustg_1980/__15.html?utm_source=chatgpt.com "§ 15 UStG - Einzelnorm - Gesetze im Internet"))|
|E-Rechnung for Vereine|BMF FAQ E-Rechnung|Official tax source|B2B invoice intake and structured formats|([Bundesministerium der Finanzen](https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html "Bundesfinanzministerium  - Fragen und Antworten zur Einführung der obligatorischen (verpflichtenden) E-Rechnung zum 1. Januar 2025"))|
|E-Rechnung archive|BMF FAQ E-Rechnung|Official tax source|Preserve structured part/original|([Bundesministerium der Finanzen](https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html "Bundesfinanzministerium  - Fragen und Antworten zur Einführung der obligatorischen (verpflichtenden) E-Rechnung zum 1. Januar 2025"))|
|GoBD|BMF GoBD 2024|Official tax source|Archive and Verfahrensdokumentation anchor|([Bundesministerium der Finanzen](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Weitere_Steuerthemen/Abgabenordnung/AO-Anwendungserlass/2024-03-11-aenderung-gobd.html "Bundesfinanzministerium  - Grundsätze zur ordnungsmäßigen Führung und Aufbewahrung von Büchern, Aufzeichnungen und Unterlagen in elektronischer Form sowie zum Datenzugriff (GoBD); Änderung aufgrund verschiedener gesetzlicher Änderungen"))|
|Practical GoBD archive|IHK München GoBD|IHK guide|Original formats, backups, machine readability|([ihk-muenchen.de](https://www.ihk-muenchen.de/ratgeber/steuern/finanzverwaltung/grundsaetze-elektronische-buchfuehrung-gobd/ "Ordnungsgemäße Buchführung: GoBD \| IHK München"))|
|Reverse charge|§13b UStG|Legal text|Foreign supplier flag|([Buzer](https://www.buzer.de/13b_UStG.htm "§ 13b UStG Leistungsempfänger als Steuerschuldner Umsatzsteuergesetz"))|
|Reverse charge workflow|IHK Stuttgart|IHK guide|Foreign services, reporting split|([IHK](https://www.ihk.de/stuttgart/fuer-unternehmen/recht-und-steuern/steuerrecht/umsatzsteuer-international/dienstleistungen/steuerschuldnerschaft-684826 "Steuerschuldumkehr beim Bezug von Leistungen / Werklieferungen<br>- IHK Region Stuttgart"))|
|Eigenbeleg fallback|BVBC/Rechnungswesen-Portal + Taxfix|Secondary|Emergency lost receipt process|([rechnungswesen-portal.de](https://www.rechnungswesen-portal.de/Fachinfo/Steuern/Der-Eigenbeleg-Letzte-Rettung-fuer-den-Steuerabzug.html?utm_source=chatgpt.com "Der Eigenbeleg - Letzte Rettung für den Steuerabzug"))|

---

# 9. Open validation questions

## 9.1 Tax advisor

1. **Vorsteuer:** Which expense categories should Safer Space treat as Vorsteuer-eligible for this event, and which should be excluded or flagged?
    
2. **Food/drinks:** How should welcome materials, non-sale drinks, team snacks or hospitality be treated?
    
3. **Reverse charge:** How should Meta Ads, Canva, Google Workspace, Eventbrite/Stripe/foreign SaaS invoices be handled in UStVA and accounting?
    
4. **E-Rechnung:** What exact tool/mailbox/archive process is acceptable for receiving and preserving XRechnung/ZUGFeRD?
    
5. **Eigenbeleg:** Under what internal threshold will the accountant accept Eigenbelege as Betriebsausgabe, and should Vorsteuer always be disallowed?
    
6. **Merchandise:** If merch/sales items are used, what VAT, stock and sales log is required?
    
7. **Reimbursements:** Does the proposed Auslagenersatz form sufficiently separate reimbursement from compensation?
    

## 9.2 Board / event lead

1. **Owner roles:** Who is finance owner, archive owner, ops owner, tool owner?
    
2. **Thresholds:** Are the approval thresholds accepted as board/event policy?
    
3. **Budget:** Which categories are pre-approved and capped?
    
4. **Cash:** Does the board approve the cash-emergency cap and no-cash-reimbursement rule?
    
5. **Private cards:** Should private card spending above 150 € be fully banned unless board-approved?
    
6. **Merch:** Will there be sales items or only free/welcome materials?
    

## 9.3 Accounting tool decision

1. **Log tool:** Google Sheet, Excel, sevdesk, lexoffice, DATEV Unternehmen Online, or another tool?
    
2. **E-Rechnung viewer:** Which viewer will be used for XRechnung/ZUGFeRD?
    
3. **Archive lock:** Which system can preserve originals and avoid accidental edits?
    
4. **Export format:** CSV/XLSX/PDF/XML expectations for accountant handoff?
    
5. **File links:** Will log rows use Drive links, local paths, or repo paths?
    

## 9.4 Ticketing / provider setup

1. **Provider invoices:** Which provider issues fee invoices, from which country, with what VAT treatment?
    
2. **Payment processor:** Stripe/PayPal/provider payout: who is merchant of record?
    
3. **Exports:** Can the provider export gross ticket revenue, VAT, fees, refunds, payout IDs and invoice numbers?
    
4. **Refunds:** Are cancellation invoices/credit notes generated?
    
5. **Support tiers:** Can voluntary support be separated from ticket price, or is it just a taxable price tier?
    

---

# 10. Implementation next steps

```yaml
implementation_next_steps:
  create_immediately:
    - "One purchase policy PDF/MD for the team."
    - "Approval threshold table."
    - "Purchase request spreadsheet."
    - "Reimbursement claim form."
    - "Lost receipt / Eigenbeleg fallback form."
    - "Invoice intake log."
    - "Archive folder tree."
    - "File naming convention."
    - "No-private-ads-account rule."
    - "No undocumented cash rule."

  can_wait_until_provider_tool_decision:
    - "Provider-specific ticketing export mapping."
    - "Stripe/PayPal/Eventbrite/pretix fee invoice workflow."
    - "E-Rechnung viewer/tool choice."
    - "Accounting software field mapping."
    - "Automated closeout workbook."

  must_validate_before_spending_starts:
    - "Vorsteuer category treatment."
    - "Reverse charge workflow for Meta/Canva/foreign SaaS."
    - "Food/drink/welcome material treatment."
    - "Merchandise/sales workflow if used."
    - "E-Rechnung intake and storage process."
    - "Final board-approved spending thresholds."
```

**Practical next action:** create a single shared spreadsheet with four tabs: `purchase_requests`, `reimbursement_claims`, `invoice_intake`, and `closeout_checklist`, then open the archive folders before anyone buys anything.