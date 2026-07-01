# Executed — Research Memo v0.1

**LIKA / Safer Space e.V. — Supporter-Tickets, freiwillige Zusatzbeträge, „Spenden“-Wording, Ticketshop/Buchhaltung**

## 0. Ausgangspunkt aus der Projekt-KB

Safer Space / LIKA ist in der KB als **eingetragener Verein in Hamburg**, **nicht gemeinnützig**, **ohne Spendenbescheinigungen**, mit **EÜR**, **USt auf Rechnungen** und noch zu bestätigender **Istversteuerung** angelegt. Die KB warnt ausdrücklich davor, Gemeinnützigkeit, Zweckbetrieb, Spendenbescheinigung oder Ehrenamtspauschale stillschweigend zu übernehmen; Provider-Dokumentation darf technische Workflows erklären, aber keine Steuerentscheidung ersetzen.

Die bisherige Quellenbasis benennt **Support-/Donation-Wording**, **7 % vs. 19 % Ticket-USt** und Ticket-/Belegprozesse als offene Validierungsfelder; zugleich sind Rechnung, GoBD, KSK und pretix/Provider-Exporte bereits gut abgedeckt.

---

# 1. Executive Summary

## Wahrscheinlich sicherste Variante

**Steuerlich konservativ am saubersten:**  
**Supporter Ticket als normale steuerpflichtige Preisstufe**.

Beispiel:

|Produkt|Checkout|Behandlung|
|---|---|---|
|Regular Ticket|300 €|Eintrittsentgelt|
|Supporter Ticket|350 €|vollständiger Betrag als Eintrittsentgelt|
|Wording|„Support-Ticket / Solidaritäts-Ticket“|keine „Spende“, keine steuerliche Abzugsfähigkeit behaupten|

Warum: Umsatzsteuerlich unterliegen Lieferungen und sonstige Leistungen eines Unternehmers im Inland gegen Entgelt der USt; die Bemessungsgrundlage richtet sich nach dem Entgelt. Der UStAE stellt zudem klar, dass ein Leistungsaustausch eine Gegenleistung voraussetzt und **auch freiwillig erbrachte Gegenleistungen** Leistungsaustausch sein können.

## Steuerlich offen / advisor_required

**Ticket + freiwilliger Zusatzbetrag** kann nur dann steuerlich defensiv argumentiert werden, wenn der Zusatzbetrag **nicht Bedingung für Eintritt**, **nicht mit Zusatzleistung verbunden**, **separat ausgewiesen**, **klar freiwillig** und **ohne Gegenleistung** dokumentiert ist. Selbst dann bleibt die Frage offen, ob der enge Checkout-Zusammenhang ihn faktisch als weiteres Eintrittsentgelt erscheinen lässt. Der UStAE ist hier das Kernrisiko, weil Freiwilligkeit allein den Leistungsaustausch nicht ausschließt.

## „Spende/Donation“ vermeiden

Ich habe keine belastbare Quelle gefunden, die sagt, dass ein nicht gemeinnütziger e.V. das Wort „Spende“ umgangssprachlich **nie** verwenden darf. Aber die Quellenlage macht das Wording klar riskant: Steuerlich abzugsfähige Spenden setzen freiwillige Zahlung **ohne Gegenleistung** und einen **steuerlich begünstigten Empfänger** voraus; Zuwendungsbestätigungen können von steuerbegünstigten Einrichtungen ausgestellt werden.

**Defensiver Begriff:**  
„freiwilliger Unterstützungsbeitrag ohne Gegenleistung — nicht steuerlich abzugsfähig — keine Spendenbescheinigung“.

## Technisch beste Ticketshop-Option

**pretix** ist aktuell die beste technische Option für LIKA, weil es getrennte Produkte/Add-ons/Cross-Selling, produktspezifische Umsatzsteuer, Banküberweisung, manuelle Zahlungsabgleiche, Overpayment-Status, Rechnungs-/Exportlogik und GoBD-nahe Dokumentationshinweise besser öffentlich dokumentiert als die Alternativen.

---

# 2. Source Library — priorisiert

|ID|Thema|Quelle|Typ|Score|Archive|Key Finding|
|---|---|---|---|---|---|---|
|S01|USt-Leistungsaustausch|UStG §1|Gesetz|95|HTML snapshot|Steuerbar sind Leistungen gegen Entgelt.|
|S02|Bemessungsgrundlage|UStG §10|Gesetz|95|HTML snapshot|Entgelt ist Basis der USt-Bemessung.|
|S03|Leistungsaustausch / Freiwilligkeit|UStAE 1.1 / UStH|Verwaltung|98|HTML/PDF|Freiwillige Gegenleistung kann trotzdem Leistungsaustausch sein.|
|S04|Spendenabzug|EStG §10b|Gesetz|95|HTML snapshot|Abziehbar sind Zuwendungen zu steuerbegünstigten Zwecken.|
|S05|Zuwendungsbestätigung|EStDV §50 / BMF Muster|Gesetz/BMF|90|HTML/PDF|Amtliche Muster für Zuwendungsbestätigungen.|
|S06|Spenden / Gegenleistung|BMF Broschüre|BMF|86|PDF|Spende: freiwillig, ohne Gegenleistung; steuerlich begünstigter Empfänger nötig.|
|S07|Zuwendungsbestätigung|Finanzverwaltung NRW|Verwaltung|88|HTML snapshot|Zuwendungsbestätigung durch steuerbegünstigte Einrichtungen.|
|S08|Sponsoring vs. Spende|BMF Sponsoring-Erlass|BMF|84|HTML snapshot|Sponsoring beruht oft auf Vertrag/Gegenleistung; andere Einordnung als Spende.|
|S09|Rechnung > 250 €|UStG §14|Gesetz|90|HTML snapshot|Rechnungsanforderungen für vollständige Rechnungen.|
|S10|Kleinbetragsrechnung|UStDV §33|Gesetz|92|HTML snapshot|Rechnungen bis 250 € brauchen reduzierte Pflichtangaben.|
|S11|Rechnung aufbewahren|UStG §14b|Gesetz|88|HTML snapshot|Aufbewahrung von Rechnungen.|
|S12|GoBD|BMF GoBD 2024|BMF|92|PDF|Elektronische Unterlagen / Datenzugriff / Aufbewahrung.|
|S13|pretix Tax Rules|pretix|Provider|82|HTML snapshot|Tax rules pro Produkt konfigurierbar; keine Steuerberatung.|
|S14|pretix Products/Add-ons|pretix|Provider|85|HTML snapshot|Add-on/Cross-Selling-Produkte und Produktsteuer.|
|S15|pretix Bank Transfer|pretix|Provider|82|HTML snapshot|Banktransfer, Import, manuelle Freigabe, manuelle Refunds.|
|S16|pretix Overpayment/API|pretix|Provider|78|HTML snapshot|Orders können „overpaid“ sein; Transactions sind für Accounting belastbarer als aktueller Order-State.|
|S17|pretix GoBD/Archive|pretix|Provider|86|HTML snapshot|Verfahrensdoku, Logs, Export/Archivhinweise.|
|S18|Eventbrite Donations|Eventbrite|Provider|65|HTML snapshot|Donation ticket type vorhanden, Gebühren auch auf Donations.|
|S19|Eventbrite Tax/Reports|Eventbrite|Provider|68|HTML snapshot|Tax paid in reports, payout summary, order report.|
|S20|Eventfrog VAT receipts|Eventfrog|Provider|64|HTML snapshot|USt-Nummer/Steuersatz hinterlegen, MwSt.-konformer Beleg.|

---

# 3. Tax Analysis

## 3.1 Eintrittsentgelt vs. freiwilliger Zusatzbetrag

**Kernregel:** Sobald Zahlung und Eintritt in einem wirtschaftlichen Zusammenhang stehen, ist das Risiko hoch, dass der Betrag als Entgelt für Eintritt behandelt wird. Der UStAE verlangt keinen „inneren“ synallagmatischen Zusammenhang; ein unmittelbarer Zusammenhang genügt, und auch freiwillige Gegenleistungen können Leistungsaustausch sein.

|Fall|USt-Risiko|Bewertung|
|---|---|---|
|350 € Supporter Ticket mit Eintritt|niedriges Streitrisiko, aber voll USt-pflichtig|konservativ|
|300 € Ticket + 50 € freiwillige Checkout-Position|mittel/hoch|advisor_required|
|300 € Ticket + getrennte spätere Überweisung|niedriger als gleicher Checkout|nur mit klarer Erklärung|
|Überzahlung 350 € auf 300 € Rechnung|hoch|nicht automatisch umwidmen|
|Nachträglicher Support-Link ohne Gegenleistung|am saubersten für Trennung|trotzdem dokumentieren|

## 3.2 Nicht gemeinnütziger e.V. und „Spende“

**Spendenabzug:** EStG §10b knüpft den Sonderausgabenabzug an steuerbegünstigte Zwecke; BMF formuliert, dass die Organisation steuerlich begünstigt sein muss, damit der Zahlende absetzen kann.

**Zuwendungsbestätigung:** Finanzverwaltung NRW sagt, dass Zuwendungsbestätigungen von steuerbegünstigten Einrichtungen ausgestellt werden können; BMF/EStH verweist auf verbindliche Muster nach §50 EStDV.

**Praktisches Ergebnis für LIKA:**  
Das Wort „Spende“ ist nicht der beste operative Begriff. Besser:

> „freiwilliger Unterstützungsbeitrag ohne Gegenleistung — keine steuerliche Abzugsfähigkeit — keine Spendenbescheinigung“.

## 3.3 Überzahlung bei Banküberweisung

Bei einer Bestellung über 300 € und Zahlungseingang 350 € sollte die Differenz **nicht automatisch** als „Spende“ oder nicht steuerbarer Beitrag gebucht werden. pretix kennt technisch „overpaid“-Situationen, aber das löst nicht die steuerliche Willenserklärungsfrage.

**Prozesspflicht:**  
Käufer:in muss bestätigen:

> „Der Mehrbetrag von X € ist freiwillig, ohne Gegenleistung, nicht Bedingung für den Eintritt und nicht steuerlich abzugsfähig. Ich wünsche keine Rückzahlung.“

Ohne Bestätigung: Rückzahlung anbieten oder Rechnung/Ticketbetrag korrigieren lassen.

---

# 4. Provider Comparison

|Provider|Variable Zusatzbeträge|Separate Produktzeile|Eigene Tax Rule|Banküberweisung|Overpayment|Export/Buchhaltung|Risiko|
|---|---|---|---|---|---|---|---|
|**pretix**|ja, technisch wahrscheinlich über variable Preise / Produktstruktur; Quelle spricht von Preis erhöhen nach Wunsch|ja, Add-on/Cross-Selling|ja, Produkt mit Sales Tax|ja|ja, „overpaid“ im Transaktionsmodell|stark; Logs, Verfahrensdoku, Rechnungen, Export|**niedrig-mittel**|
|**Eventbrite**|Donation tickets möglich|ja als Tickettyp/Add-on-nahe Struktur|Tax reports vorhanden|eher Payment-Processing-orientiert|unklar|Umsatzübersicht, Order/Payout reports|mittel; Donation-Wording stark NPO-orientiert|
|**Eventfrog**|unklar|unklar|USt-Steuersatz/Nummer möglich|Anbieterabhängig|unklar|Eventabrechnung als PDF, MwSt.-Beleg möglich|mittel|
|**ticket.io**|nicht belastbar öffentlich gefunden|unklar|unklar|unklar|unklar|Reporting/Backend vorhanden, aber Quellen dünn|mittel-hoch|
|**vivenu**|API/flexibel, aber Donation-Nachweis nicht gefunden|wahrscheinlich custom|wahrscheinlich custom|unklar|unklar|Finance/API-Fokus|mittel; Sales-Demo nötig|
|**Rausgegangen**|nicht öffentlich belastbar|unklar|unklar|unklar|unklar|Marketing-/Ticketing-Plattform|hoch bis Anbieterklärung|
|**ticketbro / TixforGigs**|nicht öffentlich belastbar|unklar|unklar|unklar|unklar|wenig öffentliche Buchhaltungsdetails|hoch bis Anbieterklärung|

**Empfehlung:** Für LIKA zuerst **pretix-Testshop** bauen, weil steuerliche Tax Rules, Produktzeilen, Banktransfer, Transaktionsmodell, GoBD-Dokumentation und Archivhinweise am besten prüfbar sind. pretix selbst sagt aber ausdrücklich, dass die Dokumentation nicht entscheidet, welche Steuer im Einzelfall korrekt ist.

---

# 5. Prozessvarianten

## Variante 1 — Supporter Ticket als steuerpflichtige Preisstufe

|Schritt|Prozess|
|---|---|
|Checkout|„Regular Ticket 300 €“, „Support Ticket 350 €“|
|Receipt|eine Position: „Support Ticket Equinox“|
|USt|gesamter Betrag mit Ticket-USt|
|Buchung|vollständiger Betrag Ticketumsatz|
|Vorteil|einfach, prüfbar, keine Spendenfiktion|
|Nachteil|kein echter getrennter freiwilliger Beitrag|

**Empfehlung:** Default, wenn Ticketverkauf schnell und robust starten soll.

---

## Variante 2 — Ticket + freiwilliger Zusatzbetrag im Checkout

|Schritt|Prozess|
|---|---|
|Checkout|Pflichtprodukt Ticket + optionale Position „freiwilliger Unterstützungsbeitrag“|
|Pflicht|separate Zeile, separater Produktname, keine Gegenleistung|
|USt|advisor_required|
|Buchung|getrennte Erlöskategorie, aber steuerlich noch zu validieren|
|Risiko|enger Zusammenhang mit Eintritt kann als Neben-/Zusatzentgelt wirken|

**Nur nutzen**, wenn Steuerberater:in bestätigt und Provider-Export die Trennung sauber zeigt.

---

## Variante 3 — Ticket + separate Überweisung

|Schritt|Prozess|
|---|---|
|Zahlung 1|exakt Ticketbetrag mit Order-ID|
|Zahlung 2|separater freiwilliger Unterstützungsbeitrag|
|Verwendungszweck|„Freiwilliger Unterstützungsbeitrag ohne Gegenleistung, keine Spendenbescheinigung“|
|Nachweis|separate Bestätigung / Mail / Formular|
|Risiko|deutlich niedriger als Überzahlung, aber advisor_required|

---

## Variante 4 — Überzahlung

|Schritt|Prozess|
|---|---|
|Erkennung|Bankbetrag > Orderbetrag|
|Sofortstatus|„Überzahlung ungeklärt“|
|Aktion|Käufer:in kontaktieren|
|Optionen|Rückzahlung oder schriftliche Bestätigung|
|Buchung|erst nach Klärung|
|Regel|keine automatische Spendenbehauptung|

---

## Variante 5 — Nachträglicher Support-Link

|Schritt|Prozess|
|---|---|
|Erstkauf|Ticket abgeschlossen und bezahlt|
|Danach|separater Link / separate Mail|
|Text|klar ohne Gegenleistung|
|Buchung|getrennt|
|Vorteil|sauberste Trennung|
|Nachteil|geringere Conversion, zusätzlicher Aufwand|

---

# 6. Buchungs- und Beleglogik

|Vorgang|Beleg|Exportfeld|Bankabgleich|GoBD-Ablage|
|---|---|---|---|---|
|Ticketverkauf|Ticket/Receipt/Rechnung|Order-ID, Produkt, Brutto, USt, Zahlungsstatus|Payout/Bank zu Orders|Ticketexport, Receipt, Payout|
|Supporter Ticket|Ticket/Receipt|Produkt „Support Ticket“|wie Ticket|wie Ticket|
|Freiwillige Checkout-Position|separate Line Item|Produkt „freiwilliger Unterstützungsbeitrag“|eigener Betrag|Checkout-Screenshot, Export, Wording-Memo|
|Separate Zahlung|Bestätigung + Kontoauszug|Referenz-ID|eigener Zahlungseingang|Zahlungsnachweis + Willenserklärung|
|Überzahlung|Exception-Log|Overpaid / Differenz|nicht buchen bis Klärung|Käuferkommunikation + Rückzahlung/Bestätigung|
|Refund|Storno/Refund-Beleg|Refund-ID, Status, Betrag|Bankausgang/Payout-Abzug|Refund-Register|

Tickets unter 250 € können als Kleinbetragsrechnung geprüft werden, wenn die Mindestangaben nach §33 UStDV enthalten sind; bei höheren Beträgen oder B2B-Konstellationen ist §14 UStG als vollständiger Rechnungsmaßstab zu prüfen.

pretix sollte nicht als Langzeitarchiv allein genutzt werden; die Unterlagen gehören regelmäßig exportiert und in einem GoBD-konformen Archiv gesichert.

---

# 7. Wording Drafts

## 7.1 Sicherer: steuerpflichtiges Supporter Ticket

**Deutsch**

> **Support Ticket — 350 € inkl. USt**  
> Dieses Ticket berechtigt wie das Regular Ticket zum Eintritt. Der höhere Preis unterstützt die Finanzierung des Events. Der gesamte Betrag ist Ticketentgelt. Es wird keine Spendenbescheinigung ausgestellt.

**English**

> **Support Ticket — €350 incl. VAT**  
> This ticket grants the same admission as a regular ticket. The higher price supports the event budget. The full amount is ticket consideration. No donation receipt will be issued.

## 7.2 Freiwilliger Zusatzbeitrag ohne Gegenleistung

**Deutsch**

> **Freiwilliger Unterstützungsbeitrag**  
> Dieser Betrag ist freiwillig, nicht Voraussetzung für den Eintritt und mit keiner Zusatzleistung verbunden. Er ist nicht steuerlich abzugsfähig. Safer Space e.V. ist nicht als gemeinnützig anerkannt und stellt keine Spendenbescheinigungen aus.

**English**

> **Voluntary support contribution**  
> This contribution is voluntary, not required for admission, and does not provide any additional benefit. It is not tax-deductible. Safer Space e.V. is not recognized as charitable and does not issue donation receipts.

## 7.3 Wording vermeiden

|Nicht verwenden|Warum|
|---|---|
|„Spendenticket“|suggeriert Spende trotz Eintritt|
|„Donation Ticket incl. entry“|vermischt Gegenleistung und Donation|
|„steuerlich absetzbar“|falsch ohne steuerbegünstigten Empfänger|
|„Spendenbescheinigung folgt“|unzulässig für nicht gemeinnützigen e.V.|
|„Pay what you want Eintrittsspende“|hohes Entgelt-/Spenden-Mischrisiko|

---

# 8. Decision Matrix

|Variante|Steuerliches Risiko|Machbarkeit|Buchhaltungsaufwand|Nachweisqualität|Empfehlung|
|---|---|---|---|---|---|
|Supporter Ticket als steuerpflichtige Preisstufe|niedrig|hoch|niedrig|hoch|**Default**|
|Ticket + separate freiwillige Checkout-Position|mittel/hoch|hoch in pretix|mittel|mittel|nur mit Steuerberater|
|Ticket + separate Überweisung|mittel|mittel|mittel|hoch, wenn bestätigt|gute Alternative|
|Überzahlung auf Ticketüberweisung|hoch|technisch möglich|hoch|niedrig bis bestätigt|vermeiden|
|Nachträglicher Support-Link|niedrig/mittel|mittel|mittel|hoch|sauberste Trennung|

---

# 9. Steuerberater-Fragen — copy/paste

```
Betreff: Safer Space e.V. / LIKA – Ticketing, Support-Tickets und freiwillige ZusatzbeträgeKontext:Safer Space e.V. ist ein eingetragener Verein in Hamburg, aktuell nicht gemeinnützig anerkannt. Es werden keine Zuwendungsbestätigungen / Spendenbescheinigungen ausgestellt. Geplant ist ein Kultur-/Club-/Fundraiser-Event mit Online-Ticketverkauf. USt auf Rechnungen wird angenommen; KUR nicht als Standardannahme.Fragen:1. Wenn wir ein „Support Ticket“ zu einem höheren Preis verkaufen, behandeln wir den gesamten Betrag als Eintrittsentgelt. Ist diese konservative Behandlung aus Ihrer Sicht korrekt?2. Wenn wir zusätzlich zum Basisticket eine freiwillige Checkout-Position „freiwilliger Unterstützungsbeitrag ohne Gegenleistung“ anbieten:   - Ist der Zusatzbetrag dennoch als Nebenentgelt zum Eintritt zu behandeln?   - Reicht eine separate Produktzeile im gleichen Checkout?   - Oder empfehlen Sie zwingend getrennten Zahlungsweg / nachträglichen Support-Link?3. Darf oder sollte ein nicht gemeinnütziger e.V. im Checkout überhaupt das Wort „Spende/Donation“ verwenden, wenn klar steht:   - nicht steuerlich abzugsfähig,   - keine Spendenbescheinigung,   - keine Gegenleistung?4. Wie behandeln wir Überzahlungen bei Banküberweisung?   Beispiel: Order 300 €, Zahlungseingang 350 €.   - Müssen wir Rückzahlung anbieten?   - Reicht eine nachträgliche Erklärung des Zahlenden?   - Wie buchen wir die Differenz bis zur Klärung?5. Welche USt-Behandlung empfehlen Sie je Variante:   - Supporter Ticket als Preisstufe,   - freiwillige Checkout-Position,   - separate Überweisung,   - nachträglicher Support-Link?6. Welche Buchungskonten / Steuerschlüssel sollen wir in EÜR/SKR nutzen?7. Welche Formulierungen sollen auf Ticket, Receipt und Checkout stehen?8. Müssen freiwillige Zusatzbeträge in der USt-Voranmeldung auftauchen, falls sie als nicht steuerbar behandelt werden?9. Welche Exportfelder aus pretix/Eventbrite/Eventfrog brauchen Sie zwingend für Buchhaltung und USt-Abstimmung?
```

---

# 10. Download-/Archivplan für KB

## Sofort archivieren

|Quelle|Format|Grund|
|---|---|---|
|UStG §1, §10, §14, §14b|HTML snapshot|Normanker für Entgelt, Rechnung, Aufbewahrung|
|UStDV §33|HTML snapshot|Ticket/Kleinbetragsrechnung|
|UStAE aktuell / UStH 1.1|PDF/HTML|Leistungsaustausch, freiwillige Gegenleistung|
|EStG §10b, EStDV §50|HTML snapshot|Spendenabzug/Zuwendungsbestätigung|
|BMF Spenden/Ehrenamt Broschüre|PDF|verständliche Spendenlogik|
|BMF Sponsoring-Erlass|HTML snapshot|Spende vs. Sponsoring/Gegenleistung|
|Finanzverwaltung NRW Zuwendungsbestätigung|HTML snapshot|steuerbegünstigte Einrichtungen|
|BMF GoBD 2024|PDF|Archiv-Normanker|
|pretix Fiscal Germany / Taxes / Products / Bank Transfer / Transactions|HTML snapshot|beste technische Umsetzung|
|Eventbrite Donations / Tax Reports / Payout Reports|HTML snapshot|Vergleichsanbieter|
|Eventfrog VAT receipt / Event invoice|HTML snapshot|Vergleichsanbieter|

## Reference only / noisy

|Quelle|Entscheidung|
|---|---|
|ticket.io öffentliche FAQ|reference only, Anbieter direkt fragen|
|vivenu Marketing/API-Seiten|reference only, Sales-Demo nötig|
|Rausgegangen Zentrale|reference only, Anbieter direkt fragen|
|ticketbro / TixforGigs|reference only|
|allgemeine Vereinsblogs mit Gemeinnützigkeit|discard/core vermeiden|

---

# 11. Konkreter nächster Schritt

**Ich würde für LIKA jetzt nicht mit „Donation“ starten.**  
Startet mit:

1. **Regular Ticket**
2. **Support Ticket als steuerpflichtige Preisstufe**
3. optional später: **separater freiwilliger Support-Link**, erst nach Steuerberaterfreigabe

Für den Ticketshop ist **pretix** aktuell der beste Kandidat für einen Testlauf. Vor Livegang braucht ihr einen archivierten Testkauf mit Ticket-PDF, Rechnung/Receipt, Export, Tax Rule, Bankabgleich und Refund-Test.