# LIKA / Safer Space e.V. — Ticket VAT + Support Wording Memo

**Status:** Arbeitsmemo für Steuerberatung / Finance Owner. Keine finale Steuerberatung.

## 1. Executive Answer

### Konservativer Default

Für den Ticketshop sollte Safer Space zunächst mit **19 % USt auf alle Eintritts-/Support-Tickets** planen, bis ein Steuerberater schriftlich bestätigt, dass für das konkrete Equinox-Format 7 % tragfähig ist.

Grund: Das Projekt selbst markiert **7 % vs. 19 % Ticket-USt** und **Support-/Donation-Wording** als offene Schwachstellen. Der KB-Index warnt ausdrücklich, dass 7 %/19 %, Venue-Settlement und KSK/Contractor-Themen Validierungspunkte bleiben und dass Provider-Dokumentation keine Steuerrechtsentscheidung ersetzt.

### Validation required

|Thema|Warum offen|
|---|---|
|**7 % Kultur/Konzert**|Nur möglich, wenn das Event steuerlich als begünstigte kulturelle/konzertähnliche Veranstaltung einzuordnen ist. Bei Club-/Dance-/Bar-Kontext ist 19 % konservativer.|
|**Support / freiwilliger Beitrag**|Wenn der Betrag mit Eintritt verknüpft ist, spricht vieles für steuerbares Ticketentgelt, nicht für echte Spende.|
|**„Donation Ticket“**|Riskant, weil Safer Space laut Projektkontext **nicht gemeinnützig** ist und keine Spendenbescheinigungen ausstellt.|
|**Ticket als Rechnung**|Unter 250 € brutto gut über Kleinbetragsrechnung lösbar, wenn alle Pflichtfelder vorhanden sind. Über 250 € / B2B braucht es Full-Invoice-Prozess.|

### Sofort sicher implementierbar

- Ticketprodukte als **brutto bepreiste Eintrittsleistungen inkl. USt** anlegen.
    
- Support-Tickets nur als **höherer steuerpflichtiger Ticketpreis**, nicht als Spende.
    
- Ticket/Receipt mit Safer-Space-Name, Adresse, Ausstellungsdatum, Leistungsbeschreibung, Bruttobetrag und Steuersatz ausgeben. § 33 UStDV nennt genau diese Mindestangaben für Rechnungen bis 250 € brutto.
    
- Für B2B oder >250 € eine vollständige Rechnung nach § 14 UStG vorsehen. § 14 UStG definiert Rechnung als jedes Abrechnungsdokument und nennt die vollständigen Pflichtangaben.
    

---

## 2. Source Table

|Topic|Source|Authority|Use|Risk / limitation|Citation|
|---|---|--:|---|---|---|
|Projektstatus|LIKA Source Index|Projekt-KB|Safer Space: e.V., nicht gemeinnützig, EÜR, USt auf Rechnungen, Istversteuerung zu bestätigen|Projektstatus muss ggf. mit Steuerberater/Finanzamt abgeglichen werden||
|Event facts|LIKA Findings|Projekt-KB|Equinox, Kapazität, Bar-Minimum, Aufgabenverteilung Venue/Organizer|Venue terms schriftlich bestätigen||
|Ticket-VAT risk|LIKA Source Index|Projekt-KB|7 % vs. 19 % als Validation Gate; UStAE/BFH/IHK als Quellencluster|Index ersetzt nicht die Rechtsentscheidung||
|Rechnung allgemein|§ 14 UStG Archiv|Gesetz / Repo-Snapshot|Full invoice fields, Rechnung auch bei beliebiger Bezeichnung|Für B2C-Kleinbetrag ggf. § 33 UStDV vorrangig praktisch||
|Kleinbetragsrechnung|§ 33 UStDV Archiv|Gesetz / Repo-Snapshot|Ticket ≤250 € brutto als Kleinbetragsrechnung, wenn Felder vorhanden|Gilt nicht bei §13b etc.||
|IHK invoice guide|IHK Berlin|IHK|Pflichtangaben, >250 € und Kleinbetragsrechnung, E-Rechnung|IHK-Hinweis, keine individuelle Beratung|([IHK](https://www.ihk.de/berlin/service-und-beratung/recht-und-steuern/steuern-und-finanzen/pflichtangaben-in-rechnungen-4400732 "https://www.ihk.de/berlin/service-und-beratung/recht-und-steuern/steuern-und-finanzen/pflichtangaben-in-rechnungen-4400732"))|
|Ticketing implementation|pretix Fiscal Germany|Provider|Steuerregeln, Rechnungsinfos, Archiv-Export|ausdrücklich keine Rechtsberatung|([docs.pretix.eu](https://docs.pretix.eu/de/trust/fiscal/germany/ "https://docs.pretix.eu/de/trust/fiscal/germany/"))|
|Tax-rule configuration|pretix Taxes|Provider|Produktweise Tax Rules, Brutto-/Netto-Handling|sagt ausdrücklich: Steuersatz mit Steuerberater klären|([docs.pretix.eu](https://docs.pretix.eu/de/guides/taxes/ "https://docs.pretix.eu/de/guides/taxes/"))|

---

## 3. Decision Matrix

|Option|Allowed?|Evidence|Risk|Required validation|Suggested wording|
|---|---|---|---|---|---|
|**19 % regular ticket**|Ja, konservativer Default|Regelbesteuerte Ticketleistung; Projekt-KB empfiehlt konservative Defaults bis Validierung.|Kann teurer wirken, aber geringeres Nachzahlungsrisiko|Steuerberater soll bestätigen, ob 19 % als Default korrekt ist|„Eintritt Equinox Hamburg — Preis inkl. 19 % USt.“|
|**7 % cultural/concert ticket**|Möglich, aber nicht ungeprüft|KB nennt §12 Abs. 2 Nr. 7 UStG / UStAE / BFH als relevante Quellen, aber ausdrücklich als Validierungspfad.|Nachzahlung + Zinsen, wenn Finanzamt Club-/Tanzveranstaltung annimmt|Programm, Line-up, Performance-Charakter, Zeitplan, Werbetexte, Venue-Kontext, Bar-/Dance-Fokus prüfen lassen|Nur nach Freigabe: „Eintritt zur Kultur-/Konzertveranstaltung … inkl. 7 % USt.“|
|**Support ticket as taxable price tier**|Ja, praktikabel|Wenn der höhere Betrag an die Eintrittsleistung gekoppelt ist, sicher als Brutto-Ticketpreis behandeln. Ticketing-Systeme können je Produkt Tax Rules abbilden. ([docs.pretix.eu](https://docs.pretix.eu/de/guides/taxes/ "https://docs.pretix.eu/de/guides/taxes/"))|Kein Spendencharakter; gesamte Zahlung als Ticketumsatz|Steuerberater soll bestätigen, dass alle tiers gleich behandelt werden|„Support Ticket — freiwillig höherer Ticketpreis zur Unterstützung der Veranstaltung, inkl. USt.“|
|**Separate voluntary contribution**|Nur mit sauberer Trennung|Muss getrennt vom Eintritt, ohne Zusatzleistung und ohne Zugangsvorteil erfolgen|Bei Kopplung an Einlass wohl Entgelt-Risiko|Ob nicht-gemeinnütziger e.V. solche Beiträge wie Schenkung/sonstige Einnahme/USt-relevant behandeln muss|„Freiwilliger zusätzlicher Unterstützungsbeitrag, kein Spendenbeleg, keine Gegenleistung, kein Einfluss auf Einlass.“|
|**Wording using “donation” / “Spende”**|Vermeiden|Projektstatus: nicht gemeinnützig, keine Spendenbescheinigungen.|Irreführung, Erwartung steuerlicher Abzugsfähigkeit, falsche USt-Behandlung|Nur mit Steuerberater, wenn überhaupt|Nicht verwenden: „Donation Ticket“, „Spendenticket“, „steuerlich absetzbar“, „Spendenquittung“|

---

## 4. Ticket Wording Drafts

### A. Normal Ticket — safe German wording

> **Eintrittsticket Equinox Hamburg**  
> Dieses Ticket berechtigt eine Person zum Eintritt zur Veranstaltung „Equinox Hamburg“ am [Datum].  
> Preis: [xx,xx €] brutto, inkl. 19 % Umsatzsteuer.  
> Veranstalter: Safer Space e.V., Spaldingstrasse 43a, 20097 Hamburg.

### B. Support Ticket treated as taxable ticket revenue

> **Support Ticket Equinox Hamburg**  
> Dieses Ticket berechtigt eine Person zum Eintritt zur Veranstaltung „Equinox Hamburg“ am [Datum].  
> Der höhere Preis ist ein freiwillig gewählter Unterstützungs-Ticketpreis zur Finanzierung der Veranstaltung.  
> Es handelt sich nicht um eine steuerlich abzugsfähige Spende. Es wird keine Spendenbescheinigung ausgestellt.  
> Preis: [xx,xx €] brutto, inkl. 19 % Umsatzsteuer.

### C. Separate voluntary contribution — only if technically separated

> **Freiwilliger Unterstützungsbeitrag**  
> Dieser Beitrag ist freiwillig, nicht Voraussetzung für den Eintritt und führt zu keiner zusätzlichen Gegenleistung.  
> Safer Space e.V. ist nicht als gemeinnützig anerkannt; es wird keine Spendenbescheinigung ausgestellt.

**Advisor required:** Bei direkter Anzeige im Ticket-Checkout bleibt zu prüfen, ob die Zahlung trotzdem als Nebenentgelt zum Eintritt gewertet wird.

### D. Wording to avoid

- „Donation Ticket“
    
- „Spendenticket“
    
- „Spende“
    
- „steuerlich absetzbar“
    
- „Spendenquittung folgt“
    
- „Pay what you want donation for entry“
    
- „Support-Spende inkl. Eintritt“
    
- „freiwillige Spende für dein Ticket“
    

### E. Receipt / tax text examples

Für Ticket ≤250 € brutto:

> Rechnung/Kleinbetragsrechnung gemäß § 33 UStDV  
> Leistung: Eintritt Equinox Hamburg am [Datum]  
> Gesamtbetrag: [xx,xx €] inkl. 19 % USt.

Für Full Invoice / B2B / >250 €:

> Vollständige Rechnung auf Anfrage / bei B2B-Buchung erforderlich. Bitte vollständige Rechnungsanschrift und ggf. USt-IdNr. angeben.

---

## 5. Tax Advisor Question Memo

**Betreff:** Bitte um steuerliche Validierung vor Ticketverkauf — Safer Space e.V. / Equinox Hamburg

Hallo [Name],

wir planen den Ticketverkauf für die Veranstaltung **Equinox / Fundraiser Hamburg** über Safer Space e.V.

**Kurzkontext:**

- Safer Space e.V., Hamburg
    
- nicht gemeinnützig anerkannt
    
- keine Spendenbescheinigungen
    
- EÜR
    
- Umsatzsteuer auf Rechnungen
    
- Istversteuerung laut Projektkontext, bitte bestätigen
    
- Veranstaltung: Club-/Kultur-/Performance-/DJ-Event in Hamburg
    
- Venue: Bar, Admission, Security, Cleaning durch Venue
    
- Organizer: Greeting, DJs, Performer:innen, Crew, Programm
    
- Venue-Modell: Mindest-Barumsatz 7.500 €, genaue vertragliche Definition noch zu bestätigen
    

**Bitte prüfen / bestätigen:**

1. **Ticket-USt-Satz:** Sollen wir für alle Eintrittstickets konservativ 19 % USt verwenden?
    
2. **7 %-Option:** Welche konkreten Voraussetzungen müssten erfüllt und dokumentiert sein, damit 7 % für Eintrittsberechtigungen tragfähig wäre?
    
3. **Programm-/Werbetexte:** Welche Fakten wären für die Abgrenzung Konzert/Kulturveranstaltung vs. Club-/Tanzveranstaltung entscheidend?
    
4. **Support Tickets:** Können wir Support-Tickets als höhere steuerpflichtige Ticketpreis-Stufen behandeln, vollständig inkl. USt?
    
5. **Wording:** Ist folgende Formulierung sauber: „freiwillig höherer Unterstützungs-Ticketpreis, keine steuerlich abzugsfähige Spende, keine Spendenbescheinigung“?
    
6. **Separate freiwillige Beiträge:** Falls wir freiwillige Zusatzbeiträge getrennt vom Eintritt anbieten: Sind diese umsatzsteuerlich trotzdem Entgelt/Nebenentgelt oder getrennt behandelbar?
    
7. **Ticket als Kleinbetragsrechnung:** Können Tickets unter 250 € brutto als Kleinbetragsrechnung dienen, wenn Safer Space e.V., Adresse, Datum, Leistungsbeschreibung, Bruttobetrag und USt-Satz enthalten sind?
    
8. **B2B / >250 €:** Welche Full-Invoice-Felder und ggf. E-Rechnungspflichten sollen wir im Ticketing-Prozess vorsehen?
    
9. **Istversteuerung:** Ist die Istversteuerung für uns bestätigt oder müssen wir noch eine explizite Bestätigung/Beantragung abwarten?
    
10. **Venue-Minimum:** Wie ist eine mögliche Zahlung an die Venue bei Nichterreichen des Mindest-Barumsatzes zu behandeln: Entgelt, Miete/Service, Schadensersatz oder anderes?
    
11. **KSK / Künstler:innen:** Müssen wir trotz „eigene Künstler:innen / keine Gagen aktuell geplant“ eine KSK-Prüfmatrix führen, falls später Honorare, Reisekosten oder Sachleistungen entstehen?
    
12. **Abschluss:** Welche konkrete Ticket-/Receipt-Formulierung würden Sie vor Livegang freigeben?
    

Unser gewünschter konservativer Start wäre: **alle Tickets inkl. 19 % USt; Support-Tickets als steuerpflichtige Preisstufen; keine Verwendung von „Spende/Donation“ im Checkout.**

Danke!

---

## 6. Open Gaps

|Gap|Markierung|Entscheidung|
|---|---|---|
|Finaler USt-Satz 7 % vs. 19 %|**advisor_required**|Vor Livegang klären; bis dahin 19 %|
|„Donation“ vs. Support-Wording|**advisor_required**|„Spende/Donation“ vermeiden|
|Separate freiwillige Beiträge|**evidence_gap + advisor_required**|Nur sauber getrennt testen, sonst taxable support tier|
|Ticketing Provider|**implementation_choice**|pretix geeignet, aber Steuersatzentscheidung extern|
|Ticket als Rechnung|**implementation_choice**|Unter 250 € als Kleinbetragsrechnung konfigurieren|
|B2B / >250 €|**implementation_choice**|Full-invoice flow bauen|
|Venue-Minimum 7.500 €|**evidence_gap + advisor_required**|Schriftliche Venue-Vereinbarung + steuerliche Einordnung|
|Istversteuerung|**advisor_required**|Bestätigung dokumentieren|

**Praktische Empfehlung:** Für den ersten Verkauf: **19 % USt, keine Donation-Sprache, Support als steuerpflichtige Ticketstufe, Ticket ≤250 € als Kleinbetragsrechnung, Full-Invoice-Prozess für B2B/>250 €.**