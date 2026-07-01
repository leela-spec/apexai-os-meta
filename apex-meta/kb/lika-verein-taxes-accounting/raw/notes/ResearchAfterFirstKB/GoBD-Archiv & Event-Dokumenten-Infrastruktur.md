# GoBD-Archiv & Event-Dokumenten-Infrastruktur

**Ziel:** ein schlankes, freiwilligen-taugliches Archivsystem für **Equinox / Fundraiser Hamburg**, bevor Ticketverkäufe starten.  
**Grenze:** keine finale Steuer- oder Rechtsberatung. USt-Satz, Support-Wording, Venue-Settlement, KSK/§50a/Reverse-Charge bleiben Validierungsfragen.

Safer Space ist im Projektkontext als **nicht gemeinnütziger e.V.**, mit **EÜR**, **USt auf Rechnungen**, **Istversteuerung** und **ohne Spendenbescheinigungen** geführt. Der Vereinssitz, das Kalenderjahr als Geschäftsjahr und der Kultur-/Veranstaltungszweck ergeben sich zusätzlich aus Satzung und Stammdaten. Die vorhandene KB warnt ausdrücklich davor, Gemeinnützigkeit, Zweckbetrieb, Spendenbescheinigungen, Übungsleiterpauschale oder Ehrenamtspauschale stillschweigend zu übernehmen.

---

## 1. Plain-language explanation

### Warum gibt es dieses Archiv?

Das Archiv ist kein Bürokratie-Projekt. Es beantwortet später einfache Fragen:

- **Welche Einnahmen gab es?**
- **Welche Gebühren, Refunds und Auszahlungen gehören dazu?**
- **Welche Rechnungen und Ausgaben gab es?**
- **Warum wurde etwas so entschieden?**
- **Kann jede Bankbewegung mit einem Beleg erklärt werden?**

Die GoBD betreffen die ordnungsmäßige Führung und Aufbewahrung elektronischer Bücher, Aufzeichnungen und Unterlagen sowie den Datenzugriff. Das BMF hat die GoBD zuletzt wegen gesetzlicher Änderungen angepasst; 2025 kam zusätzlicher Änderungsbedarf durch die verpflichtende E-Rechnung im inländischen B2B-Bereich hinzu.

### Warum vor Ticketverkauf?

Weil ab dem ersten Testticket Daten entstehen:

- Ticketprodukt
- Steuereinstellung
- Beleg-/Ticket-PDF
- Zahlungsanbieter- und Ticketing-Export
- Storno-/Refund-Logik
- Gebühren
- Bankauszahlung

Wenn ihr erst nach dem Event sortiert, fehlen oft Screenshots, Rohdaten oder Entscheidungsnotizen.

### Was bedeutet „GoBD-ish“ praktisch?

Für LIKA heißt das nicht: teures DMS kaufen.  
Es heißt:

|Begriff|Praktische Bedeutung|
|---|---|
|**vollständig**|Jede Einnahme, Auszahlung, Erstattung, Rechnung und relevante Entscheidung ist auffindbar.|
|**unverändert**|Roh-Exports, Rechnungen, XML-Dateien und Belege werden nicht überschrieben oder nachträglich „schön bearbeitet“.|
|**nachvollziehbar**|Eine fremde Person kann sehen: Bestellung → Zahlung → Auszahlung → Bank → Buchhaltung.|
|**lesbar**|Dateien sind später noch öffnbar; E-Rechnungen werden nicht nur als Screenshot abgelegt.|
|**geordnet**|Gleiche Dokumenttypen liegen immer am gleichen Ort.|

Die AWV stellt genau für solche geordneten Belegablagen eine kostenlose Muster-Verfahrensdokumentation mit PDF- und Word-Vorlage bereit; dort geht es insbesondere um Vollständigkeit, Ordnung, Unveränderbarkeit und Schutz gegen Verlust.

### Arbeitsordner vs. Archivordner vs. Handoff

|Bereich|Zweck|Darf bearbeitet werden?|
|---|---|---|
|**Working folder**|Rechnen, Abstimmen, Entwürfe, offene Klärungen|Ja|
|**Raw archive / no-edit**|Originale: Exporte, Rechnungen, PDFs, XML, Bankauszüge, Screenshots|Nein|
|**Accounting handoff**|Paket für Steuerberatung/Buchhaltung: final, sortiert, erklärt|Nur kontrolliert|

### Was passiert, wenn Belege fehlen?

Nicht sofort Panik. Aber es kostet Zeit und erzeugt Risiko:

- Bankbewegungen sind schwer erklärbar.
- Vorsteuer kann gefährdet sein, wenn Eingangsrechnungen nicht korrekt vorliegen.
- Refunds oder Gebühren werden falsch zugeordnet.
- USt- und KSK-Fragen werden schwerer prüfbar.
- Das Team muss Wochen später aus Chats, E-Mails und Screenshots rekonstruieren.

---

# 2. Minimum viable archive

## Minimal, aber defensibel

Für einen kleinen, ehrenamtlichen e.V. reicht erstmal:

```
minimum_viable_archive:  tool:    - Cloud-Drive oder lokaler Ordner mit Backup    - klare Schreibrechte    - ein Archiv-Owner    - wöchentlicher Export- und Abgleichtermin  no_edit_rule:    - Rohdaten nach Ablage nicht mehr verändern    - Korrekturen nur in Arbeitskopien oder Reconciliation Workbook  core_files:    - README_archive_rules.md    - decision_log.md    - payout_reconciliation.xlsx    - exception_log.xlsx    - tax_advisor_handoff.md  routine:    - vor Ticketlaunch Setup testen    - während Sales wöchentlich Exporte ziehen    - nach Event Closeout-Paket bauen
```

**Wichtig:** Die Verfahrensdokumentation muss nicht riesig sein. DATEV beschreibt sie als Überblick über die buchführungsrelevanten Abläufe; gerade externe Personen kennen die internen Abläufe meist nicht gut genug, deshalb sollte das Team selbst die tatsächlichen Schritte dokumentieren.

---

# 3. Event archive folder template

## Folder tree mit Ordner-Typen

Legt vor Ticketverkauf diesen Ordner an:

```
LIKA_Equinox_YYYY-MM-DD_EventArchive/  00_README_AND_PROCESS/                         [decision/evidence folder]    README_archive_rules.md    verfahrensdokumentation_mini.md    owner_roles.md    decision_log.md  01_EVENT_BASE/                                 [decision/evidence folder]    venue_agreement/    capacity_and_schedule/    event_budget/    permits_or_confirmations_if_any/  02_TICKETING_SETUP/                            [decision/evidence folder]    ticket_products/    tax_configuration/    receipt_ticket_samples/    test_orders/    screenshots/  03_TICKETING_EXPORTS_RAW/                      [raw archive / no-edit]    orders/    attendees/    invoices_or_receipts/    refunds/    fees/    payouts/    raw_provider_exports_do_not_edit/  04_RECONCILIATION_WORKING/                     [working folder]    payout_reconciliation_workbook/    bank_matching/    exception_log/    closeout_calculations/  05_BANK_AND_PAYMENT/                           [raw archive / no-edit]    bank_statements/    payment_processor_reports/    payout_confirmations/  06_INCOMING_INVOICES/                          [raw archive / no-edit]    venue/    artists/    contractors/    marketing/    decoration/    technical/    software_and_ticketing/    other/  07_E_RECHNUNGEN/                               [raw archive / no-edit]    xrechnung_xml/    zugferd_pdf_xml/    visual_copies/    validation_notes/  08_EXPENSES_AND_REIMBURSEMENTS/                [handoff + evidence folder]    private_purchases/    reimbursement_forms/    approvals/    payment_proofs/  09_ARTISTS_KSK_CONTRACTORS/                    [handoff + evidence folder]    artist_register/    contracts/    invoices/    ksk_check/    foreign_service_checks/    payment_proofs/  10_VENUE_SETTLEMENT/                           [handoff + evidence folder]    venue_invoice_or_settlement/    bar_revenue_or_minimum_revenue_evidence/    security_cleaning_evidence/    settlement_approval/  11_EVENT_DAY_EVIDENCE/                         [raw archive + evidence folder]    final_guest_list_or_admission_report/    door_sales_if_any/    incident_or_exception_notes/    photos_of_signage_or_box_office_if_relevant/  12_CLOSEOUT_PACKET/                            [handoff folder]    final_reconciliation/    tax_advisor_handoff/    accounting_handoff/    unresolved_questions/    archive_lock_confirmation/
```

## File naming rules

Use one consistent pattern:

```
YYYY-MM-DD__LIKA_Equinox__DOC-TYPE__SOURCE__VERSION.ext
```

Beispiele:

```
2026-08-01__LIKA_Equinox__ticket_products__pretix__v01.pdf2026-08-01__LIKA_Equinox__tax_config_screenshot__pretix__raw.png2026-08-08__LIKA_Equinox__orders_export__pretix__raw.csv2026-08-08__LIKA_Equinox__payout_report__pretix__raw.pdf2026-08-09__LIKA_Equinox__bank_statement__GLS__raw.pdf2026-08-10__LIKA_Equinox__refund_export__pretix__raw.csv2026-09-01__LIKA_Equinox__reconciliation_workbook__finance__v03.xlsx
```

## No-edit rule

**Rohdateien niemals umbenennen, wenn sie schon archiviert und referenziert sind.**  
Besser:

```
raw_original_filename/  original_export.csv  2026-08-08__archive_note.md
```

Oder: Dateiname beim Speichern direkt sauber wählen und danach nicht mehr anfassen.

---

# 4. Process by phase

## A. Before ticket sales

**Ziel:** Ticketverkauf erst starten, wenn Belege später erklärbar sind.

Checklist:

- Archivordner anlegen.
- Archiv-Owner benennen.
- Ticketing-Owner benennen.
- Finance-Owner benennen.
- Ticketproduktliste erstellen.
- Steuer-/Support-Wording als Entscheidungsmemo vorbereiten.
- Testbestellung durchführen.
- Ticket-/Receipt-PDF prüfen.
- Screenshot der Tax-Konfiguration sichern.
- Exportfunktion testen.
- Mini-Verfahrensdokumentation schreiben.

**Besonders wichtig:** Tickets bis 250 € brutto können grundsätzlich als Kleinbetragsrechnung gedacht werden, wenn die Pflichtangaben erfüllt sind: vollständiger Name und Anschrift des Leistenden, Ausstellungsdatum, Art/Umfang der Leistung sowie Bruttobetrag mit Steuerbetrag/Steuersatz. Das ist aber kein Freifahrtschein: Der Ticketing-Anbieter und die konkrete Konfiguration müssen geprüft werden.

## B. Weekly during sales

**Ziel:** Nicht erst nach dem Event alles zusammensuchen.

Wöchentlich:

- Order export herunterladen.
- Attendee export herunterladen.
- Refund export herunterladen.
- Fees / payout reports sichern.
- Bankauszahlungen gegen Ticketing-Payouts matchen.
- Exception Log aktualisieren.
- Raw exports unverändert in `03_TICKETING_EXPORTS_RAW/` ablegen.
- Arbeitskopien nur in `04_RECONCILIATION_WORKING/` bearbeiten.

## C. Event day

**Ziel:** Event-Fakten sichern, die später nicht mehr rekonstruierbar sind.

Sichern:

- finale Gästeliste / Admission Report
- finaler Scan-/Check-in-Report
- Door-sales-Unterlagen, falls vorhanden
- Refund-/Exception-Notizen
- Venue-Settlement-Nachweise
- Sicherheits-/Cleaning-Inclusion-Nachweis
- Barumsatz-/Mindestumsatz-Bestätigung, falls vom Venue bereitgestellt

Die Projektfindings nennen für Equinox bereits: Venue Capacity 300–350, Empfehlung 310–320, Mindestbarumsatz 7.500 €, Venue handles bar/admission/security/cleaning, Organizer handles greeting/DJs/performers/crew/program. Genau diese Punkte gehören schriftlich bestätigt und archiviert.

## D. Closeout

**Ziel:** fertiges Paket für Steuerberatung/Buchhaltung.

Closeout-Paket:

- finaler Order Export
- finaler Attendee Export
- finaler Refund Export
- Payout Report
- Provider Fee Report
- Bank Matching
- Reconciliation Workbook
- Venue Settlement Packet
- Artist/KSK Register
- Foreign-Service Checks
- Expense/Reimbursement Evidence
- Tax Advisor Handoff Memo
- unresolved questions
- archive lock confirmation

---

# 5. Evidence by transaction type

## Tickets

Benötigt:

- Ticket product list
- Steuereinstellung / Tax Configuration Screenshot
- Sample Ticket / Receipt PDF
- Test Order
- Order Export
- Attendee Export
- VAT/support wording decision memo

**Warum:** Ticketumsätze sind die Hauptquelle der Einnahmen. Provider-Dokumentation darf aber nur die technische Umsetzung erklären, nicht die steuerliche Bewertung entscheiden. Die KB nennt Ticketing, E-Rechnung, GoBD, Ticketing-Exports und Payout-Reconciliation als besonders relevante Quellcluster.

## Payouts

Benötigt:

- Ticketing payout report
- bank statement line
- provider fee report
- reconciliation workbook

**Regel:** Bankeingang ist meist netto nach Gebühren; Buchhaltung muss trotzdem Bruttoverkauf, Gebühren, Refunds und Auszahlung auseinanderhalten.

## Refunds

Benötigt:

- Refund Export
- cancellation / credit note record, falls generiert
- payment processor refund evidence
- reason / approval note bei manuellen Refunds

## Venue settlement

Benötigt:

- signed venue agreement
- minimum bar revenue wording
- venue invoice / settlement
- bar revenue confirmation, falls vorhanden
- security/cleaning inclusion evidence

**Offen:** Die vorhandene APEX-Auswertung markiert Venue-Settlement und Mindestbarumsatz als schwach belegte bzw. validierungspflichtige Bereiche.

## Purchases and reimbursements

Benötigt:

- supplier invoice or receipt
- proof of payment
- business purpose
- approval
- reimbursement form, wenn privat bezahlt

## Artists and contractors

Benötigt:

- contract / booking confirmation
- invoice
- payment proof
- KSK relevance check
- foreign-service / §50a / reverse-charge trigger check, falls relevant

Die Quellenbewertung stuft KSK-Quellen als starke Pflichtquellen ein; KSK-Veranstalterthemen und DRV-Künstlersozialabgabe sind wiederholt als P0/Pflichtbereich markiert.

---

# 6. E-Rechnung intake

## Was muss Safer Space wissen?

Seit 2025 ist bei Umsätzen zwischen inländischen Unternehmern regelmäßig eine E-Rechnung zu verwenden; private Endverbraucher sind laut BMF davon nicht betroffen. Für LIKA betrifft das vor allem **eingehende B2B-Rechnungen** von Venue, Dienstleistern, Agenturen, Software-/Ticketing-Anbietern oder sonstigen Unternehmen.

## E-Rechnung vs. PDF

|Format|Praktische Bedeutung|
|---|---|
|**PDF-Rechnung**|Menschlich lesbar, aber nach neuer Definition nicht automatisch E-Rechnung.|
|**XRechnung XML**|Strukturierte maschinenlesbare E-Rechnung.|
|**ZUGFeRD**|Hybrides Format: PDF + eingebettete strukturierte Daten.|
|**Screenshot**|Kein Ersatz für Rechnung oder E-Rechnung.|

Das BMF-Schreiben zur E-Rechnung beschreibt, dass E-Rechnungen rein strukturiert oder hybrid sein können; zulässige Formate müssen gewährleisten, dass Rechnungsangaben elektronisch übermittelt und ausgelesen werden können. EN-16931-konforme strukturierte Formate sind zulässig.

## Wie speichern?

```
07_E_RECHNUNGEN/  xrechnung_xml/    original.xml  zugferd_pdf_xml/    original_zugferd.pdf  visual_copies/    lesbare_ansicht.pdf  validation_notes/    2026-08-01__viewer_note.md
```

## XML und PDF beide speichern?

**Ja, wenn vorhanden.**

- XML/strukturierte Datei = maßgeblicher maschinenlesbarer Beleg.
- PDF/Visual Copy = Lesekopie für Menschen.
- ZUGFeRD-PDF nicht in „normale PDFs“ verschieben; es gehört in den E-Rechnungsordner.

## Was Volunteers nicht tun sollen

- XML-Dateien nicht in Word öffnen und neu speichern.
- Rechnungsdateien nicht umbenennen, nachdem sie im Archive Log referenziert sind.
- E-Rechnung nicht nur als Screenshot speichern.
- Rechnungs-PDF nicht bearbeiten.
- Rechnungen nicht in privaten Chats liegen lassen.
- Dateien nicht aus dem E-Mail-Anhang löschen, bevor sie archiviert sind.

---

# 7. Document matrix

|Document|Why needed|When captured|Owner|Folder|Retention / archive note|Source basis|
|---|---|---|---|---|---|---|
|Ticket product list|Belegt, was verkauft wurde|Vor Launch + bei Änderung|Ticketing Owner|`02_TICKETING_SETUP/ticket_products/`|Versionieren|Ticketing setup / Provider docs|
|Ticket tax configuration screenshots|Nachweis der USt-Konfiguration|Vor Launch + bei Änderung|Ticketing + Finance|`02_TICKETING_SETUP/tax_configuration/`|Raw Screenshot nicht bearbeiten|GoBD / Tax validation|
|Sample ticket / receipt|Prüft Pflichtangaben|Testorder vor Launch|Finance|`02_TICKETING_SETUP/receipt_ticket_samples/`|PDF + Screenshot sichern|§33 UStDV / IHK|
|Test order|End-to-end-Test|Vor Launch|Ticketing Owner|`02_TICKETING_SETUP/test_orders/`|Mit Export referenzieren|Provider lifecycle|
|Order export|Hauptumsatzdaten|Wöchentlich + final|Ticketing Owner|`03_TICKETING_EXPORTS_RAW/orders/`|Raw CSV/XLSX unverändert|GoBD / Provider docs|
|Attendee export|Check-in/Leistungsnachweis|Wöchentlich/final/Eventday|Ticketing Owner|`03_TICKETING_EXPORTS_RAW/attendees/`|DSGVO-minimal teilen|Provider docs|
|Refund export|Stornos/Erstattungen|Wöchentlich + final|Finance|`03_TICKETING_EXPORTS_RAW/refunds/`|Raw + Refund Register|Provider lifecycle|
|Payout report|Zahlungsfluss Provider → Bank|Pro Auszahlung|Finance|`03_TICKETING_EXPORTS_RAW/payouts/`|Mit Bankzeile matchen|Payout reconciliation|
|Provider fee report|Gebühren getrennt erfassen|Pro Export/Monat|Finance|`03_TICKETING_EXPORTS_RAW/fees/`|Nicht nur Nettoauszahlung buchen|Provider docs|
|Bank statement|Zahlungsnachweis|Pro Auszug|Finance|`05_BANK_AND_PAYMENT/bank_statements/`|PDF/CSV sichern|AO/GoBD|
|Reconciliation workbook|Verbindung Order → Payout → Bank|Wöchentlich|Finance|`04_RECONCILIATION_WORKING/`|Arbeitsdatei versionieren|GoBD-ish workflow|
|Venue agreement|Vertragsgrundlage|Vor Launch|Event Lead|`01_EVENT_BASE/venue_agreement/`|Signierte Fassung archivieren|Venue risk|
|Venue invoice / settlement|Ausgabe/Abrechnung|Nach Event / nach Rechnung|Finance|`10_VENUE_SETTLEMENT/`|Original unverändert|Venue settlement|
|Bar minimum revenue evidence|Klärt 7.500 € Mindestumsatz|Vor Vertrag + Eventday|Event Lead|`10_VENUE_SETTLEMENT/`|Steuerberater-Frage markieren|Project risk|
|Artist contract|Grundlage Zahlung/KSK|Vor Leistung|Booking Owner|`09_ARTISTS_KSK_CONTRACTORS/contracts/`|Pro Person|KSK|
|Artist invoice|Zahlungs-/Vorsteuerbeleg|Vor Zahlung|Finance|`09_ARTISTS_KSK_CONTRACTORS/invoices/`|Eingangsrechnung prüfen|Rechnungspflicht|
|KSK check|Künstlersozialabgabe prüfen|Vor Zahlung + Closeout|Finance|`09_ARTISTS_KSK_CONTRACTORS/ksk_check/`|Register behalten|KSK/DRV|
|Foreign-service check|§50a/Reverse Charge Trigger|Vor Vertrag|Finance + Booking|`09_ARTISTS_KSK_CONTRACTORS/foreign_service_checks/`|Steuerberater-Gate|BZSt/IHK|
|Supplier invoice|Vorsteuer/Ausgabe|Bei Eingang|Finance|`06_INCOMING_INVOICES/`|Originaldatei speichern|IHK/BMF|
|E-Rechnung XML|Strukturierte Rechnung|Bei Eingang|Finance|`07_E_RECHNUNGEN/xrechnung_xml/`|XML nicht verändern|BMF E-Rechnung|
|ZUGFeRD file|Hybridrechnung|Bei Eingang|Finance|`07_E_RECHNUNGEN/zugferd_pdf_xml/`|PDF mit XML behalten|BMF E-Rechnung|
|Normal PDF invoice|Sonstige Rechnung|Bei Eingang|Finance|`06_INCOMING_INVOICES/`|Nicht bearbeiten|IHK/BMF|
|Reimbursement form|Private Auslagen erklären|Vor Erstattung|Ops + Finance|`08_EXPENSES_AND_REIMBURSEMENTS/`|Mit Beleg + Zahlung|Expense workflow|
|Private purchase receipt|Nachweis Ausgabe|Sofort nach Kauf|Käufer:in + Finance|`08_EXPENSES_AND_REIMBURSEMENTS/private_purchases/`|Originalfoto/PDF sichern|GoBD-ish|
|Approval note|Warum bezahlt/erstattet|Vor Zahlung|Event Lead/Finance|`08_EXPENSES_AND_REIMBURSEMENTS/approvals/`|Kurznotiz reicht|Internal control|
|Final closeout packet|Abschluss für Buchhaltung|Nach Event|Finance|`12_CLOSEOUT_PACKET/`|Final PDF + Workbook|Handoff|
|Tax advisor handoff memo|Validierungsfragen bündeln|Vor/ nach Event|Finance|`12_CLOSEOUT_PACKET/tax_advisor_handoff/`|Keine finale Steuerbehauptung|Validation gates|

---

# 8. SOP — Event archive daily / weekly / closeout SOP

## SOP 1 — Before ticket launch

```
title: "Before ticket launch archive SOP"trigger: "Ticketing-Testsystem ist bereit oder Ticketverkauf soll starten."responsible_owner: "Archive Owner + Ticketing Owner + Finance Owner"inputs:  - Ticketproduktliste  - geplante Preise  - USt-/Support-Wording-Entwurf  - Ticketing-Backend-Zugang  - Vereinsdatensteps:  - Archivordner nach Template anlegen.  - README_archive_rules.md ausfüllen.  - owner_roles.md ausfüllen.  - Ticketprodukte als PDF/Screenshot sichern.  - Tax-Konfiguration als Screenshot sichern.  - Testorder durchführen.  - Ticket/Receipt PDF sichern.  - Exportfunktion testen: orders, attendees, refunds, fees, payouts.  - Reconciliation Workbook anlegen.  - decision_log.md mit offenen Validierungsfragen füllen.done_when:  - Testorder liegt im Archiv.  - Ticketbeleg wurde gegen Pflichtfelder geprüft.  - Tax/support wording ist entweder validiert oder klar als Gate markiert.  - Archive Owner bestätigt: Ordnerstruktur funktioniert.exceptions:  - Ticketbeleg zeigt keine vollständigen Vereinsdaten.  - USt-Satz unklar.  - Support-Begriff klingt nach Spende.  - Exportformate unklar.escalation:  - Finance Owner stoppt Launch bis Tax-/Receipt-Gate geklärt ist.
```

## SOP 2 — Weekly during ticket sales

```
title: "Weekly ticket sales archive SOP"trigger: "Einmal pro Woche während laufender Sales; zusätzlich nach großen Sales-Spikes."responsible_owner: "Ticketing Owner zieht Exporte; Finance Owner gleicht ab."inputs:  - Ticketing Backend  - Bankkonto  - Payment/Payout Reports  - Reconciliation Workbooksteps:  - Order Export herunterladen.  - Attendee Export herunterladen.  - Refund Export herunterladen.  - Fee Report herunterladen.  - Payout Report herunterladen.  - Dateien unverändert in RAW-Ordner ablegen.  - Bankeingänge prüfen.  - Payouts gegen Bank matchen.  - Refunds markieren.  - Exception Log aktualisieren.  - Kurznotiz in weekly_archive_log.md schreiben.done_when:  - Alle neuen Ticketing-Bewegungen sind exportiert.  - Jede Auszahlung hat eine Bankzeile oder ist als offen markiert.  - Refunds sind sichtbar.  - Keine Rohdatei wurde bearbeitet.exceptions:  - Payout fehlt.  - Refund nicht im Export.  - Bankbetrag weicht ab.  - Exportformat geändert.escalation:  - Ticketing Owner fragt Provider.  - Finance Owner markiert offene Punkte für Closeout/Steuerberatung.
```

## SOP 3 — Closeout after event

```
title: "Event closeout archive SOP"trigger: "Event beendet; finale Providerdaten und Venue Settlement verfügbar."responsible_owner: "Finance Owner"inputs:  - finale Ticketing Exporte  - finale Payout Reports  - Bankauszüge  - Venue Settlement  - Artist/Contractor-Invoices  - Reimbursement Evidencesteps:  - Finalen Order Export sichern.  - Finalen Attendee/Admission Report sichern.  - Finalen Refund Export sichern.  - Alle Payouts gegen Bank matchen.  - Provider Fees gesondert erfassen.  - Venue Settlement Packet erstellen.  - Artist/KSK Register finalisieren.  - Foreign-service checks finalisieren.  - Expense/Reimbursement Packet finalisieren.  - Unresolved Questions sammeln.  - Accounting Handoff erstellen.  - Archive Lock Confirmation schreiben.done_when:  - Jede Bankbewegung ist erklärt oder als Exception geloggt.  - Jede Ausgabe hat Beleg + Zahlungsnachweis + Zweck.  - Steuerberater-Handoff ist vollständig.  - Roharchive sind read-only oder als final snapshot gesichert.exceptions:  - fehlende Rechnung  - fehlende Bankzeile  - unklare Refunds  - unklare Venue-Kurzfallzahlung  - ungeklärte KSK/§50a/Reverse-Charge Triggerescalation:  - Finance Owner erstellt gezieltes Steuerberater-Fragenmemo.
```

---

# 9. Team explanation

## How to explain this to volunteers

**Kernmessage:**  
Wir bauen keine Bürokratie. Wir sorgen nur dafür, dass später jeder Euro erklärbar ist.

### 5-minute team briefing script

> Wir machen für Equinox einen einfachen Event-Archivordner.  
> Der Sinn ist nicht Kontrolle, sondern Entlastung: Niemand soll nach dem Event alte Chats, Screenshots oder Rechnungen suchen müssen.  
> Alles, was Geld betrifft, kommt in den Archivordner: Ticketexports, Rechnungen, Refunds, Banknachweise, Erstattungen und wichtige Entscheidungen.  
> Rohdateien werden nicht bearbeitet. Wenn wir rechnen oder sortieren, machen wir das in Arbeitskopien.  
> Wenn jemand privat etwas kauft, brauchen wir Beleg, Zahlungsnachweis, Zweck und kurze Freigabe.  
> Wenn etwas unklar ist, ist das okay — es kommt ins Exception Log.  
> Unser Ziel ist einfach: Jede Einnahme und Ausgabe kann später in zwei Minuten erklärt werden.

---

# 10. Open questions

|Frage|Label|Warum wichtig|
|---|---|---|
|Welcher USt-Satz gilt für Tickets: 19 % oder validiert 7 %?|needs Steuerberater|Höchstes Nachzahlungsrisiko|
|Darf es Support-Tickets geben und wie dürfen sie heißen?|needs Steuerberater|Nicht gemeinnützig; „Spende“ vermeiden|
|Sind Tickets als Kleinbetragsrechnung ausreichend?|needs Steuerberater|Nur wenn Preis ≤ 250 € und Pflichtangaben erfüllt|
|Welcher Ticketing Provider wird gewählt?|needs tool decision|Export-/Refund-/Payout-Logik hängt daran|
|Welche Exportformate liefert der Provider?|needs ticketing owner|CSV/XLSX/PDF/API für Reconciliation|
|Wie ist Venue Settlement / Mindestbarumsatz genau geregelt?|needs venue confirmation|7.500 € Risiko; Shortfall-Behandlung offen|
|Wer bestätigt Capacity schriftlich?|needs venue confirmation|Ticketcap 310–320 bis Bestätigung|
|Wie werden E-Rechnungen empfangen und gelesen?|needs archive owner|XML/ZUGFeRD darf nicht verloren gehen|
|Wer macht die wöchentliche Archivroutine?|needs archive owner|Sonst entsteht Rückstau|
|Gibt es Door Sales oder Cash?|needs event lead decision|Zusätzliche Kassen-/Beleglogik|
|Gibt es bezahlte Artists/DJs/Performer?|needs event lead decision|KSK/Vertrag/Rechnung|
|Gibt es ausländische Artists oder Dienstleister?|needs Steuerberater|§50a / Reverse Charge Trigger|
|Wer führt KSK-Register?|needs archive owner|Pflicht-/Prüfrisiko|
|Wie lange wird das finale Archiv aufbewahrt?|needs event lead decision|§147 AO / steuerliche Aufbewahrung|
|Wer darf Rohdateien verändern?|needs archive owner|Antwort sollte sein: niemand|

§147 AO enthält die zentralen Aufbewahrungsvorschriften für steuerlich relevante Unterlagen; die Frist läuft nicht ab, solange die Unterlagen noch für Steuern von Bedeutung sind, deren Festsetzungsfrist nicht abgelaufen ist.

---

# Minimum viable setup in one page

## Setup

```
1 Archivordner1 Archive Owner1 Finance Owner1 Ticketing Owner1 Reconciliation Workbook1 Decision Log1 Exception Log1 wöchentlicher Exporttermin1 finaler Closeout-Termin
```

## Grundregel

```
Rohdaten bleiben roh.Gearbeitet wird nur in Arbeitskopien.Jede Bankbewegung braucht Erklärung.Jede Ausgabe braucht Beleg + Zahlung + Zweck.Jede Steuerfrage wird als Gate markiert, nicht geraten.
```

## Minimalordner

```
00_README_AND_PROCESS/02_TICKETING_SETUP/03_TICKETING_EXPORTS_RAW/04_RECONCILIATION_WORKING/05_BANK_AND_PAYMENT/06_INCOMING_INVOICES/07_E_RECHNUNGEN/08_EXPENSES_AND_REIMBURSEMENTS/09_ARTISTS_KSK_CONTRACTORS/10_VENUE_SETTLEMENT/12_CLOSEOUT_PACKET/
```

## Wöchentlicher Ablauf

```
Download exportsSave rawMatch payouts to bankTrack refundsLog exceptionsUpdate reconciliation workbook
```

## Closeout

```
Final exportsFinal bank matchRefund registerVenue settlement packetArtist/KSK packetExpense packetTax advisor handoffArchive lock snapshot
```

---

# First 10 actions before ticket sales

1. **Archive Owner benennen.**
2. **Finance Owner benennen.**
3. **Ticketing Owner benennen.**
4. **Ordnerstruktur anlegen.**
5. **README_archive_rules.md schreiben.**
6. **Ticketproduktliste erstellen.**
7. **USt-Satz und Support-Wording als Steuerberater-Gate markieren.**
8. **Testorder im Ticketing-System durchführen.**
9. **Ticket-/Receipt-PDF, Tax-Screenshots und erste Exporte archivieren.**
10. **Venue schriftlich um Capacity, Mindestbarumsatz-Definition, Shortfall-Regel und inkludierte Security/Cleaning-Leistungen bitten.**