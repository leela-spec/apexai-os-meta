Title: SKR42 Branchenpaket Vereine, Stiftungen, gGmbHs einrichten - DATEV Hilfe-Center

URL Source: https://help-center.apps.datev.de/documents/1022996

Markdown Content:
Aktuelle Änderungen
24.11.2025 Das Dokument wurde aktualisiert.

## 1 Über dieses Dokument

In diesem Dokument erfahren Sie, wie Sie das Branchenpaket Vereine, Stiftungen, gGmbHs (SKR42) einrichten.

### 2.1 Buchführung

Sie können ein Branchenpaket bei einer Jahresübernahme mit Kontenrahmenwechsel oder bei Neuanlage eines Mandanten wählen.

#### 2.1.1 Kontenrahmen wechseln

![Image 1](https://help-center.apps.datev.de/api/amr/knowledge-common/v1/entities/st150122891_de.png) Hilfe-Video
[Jahresübernahme auf das Branchenpaket SKR42 durchführen](https://go.datev.de/sv-23576 "https://go.datev.de/sv-23576") (Dauer: 04:42, Stand: 12.12.2023)

Wählen Sie den Standardkontenrahmen SKR42 und das Branchenpaket Vereine, Stiftungen, gGmbHs.

Branchenpaket bei der Jahresübernahme wählen
Voraussetzung:
DFÜ-Verbindung zum DATEV-Rechenzentrum
Vorgehen:
1 Mandantenbestand öffnen.
2 Im Menü: Bestand | Jahresübernahme | Neues Wirtschaftsjahr anlegen wählen.
3 Wenn die Programm-Meldung REW92919 kommt: Auf OK klicken.
4 Im Fenster Neues Wirtschaftsjahr anlegen das Kontrollkästchen Kontenrahmen wechseln / Branchenpaket bzw. Lösung einstellen aktivieren.
5 Kontenrahmen: SKR42 (Vereine, Stiftungen, gGmbHs) wählen.
6 In der Programm-Meldung REW90598: Auf OK klicken.
7 Überleitung Kontenüberleitungstabelle: Auf den Link Auswahl klicken.
8 Im Fenster Auswahl der Vorlage: Auf OK klicken.
9 Im Fenster Überleitungstabelle importieren: Standard-Kontenüberleitung wählen.
10 Auf OK klicken.

Im Fenster Vorjahreskonten-Überleitung Kontenüberleitung auf Konto und Sphärenzuordnung prüfen und ggf. vervollständigen. Ordnen Sie folgende Konten zu:

*   Konten mit Inventaren (Anlagekonten)

*   Geldkonten

*   Sammelkonten für Forderungen aus Lieferungen und Leistungen und Verbindlichkeiten aus Lieferungen und Leistungen

Vorbelegung Sphäre 9 übernehmen.
11 Auf OK klicken.
12 Alle anderen Konten können Sie nach der Jahresübernahme in Ihrem DATEV-Rechnungswesen-Programm im neuen Wirtschaftsjahr zuordnen.
13 Im Fenster Neues Wirtschaftsjahr anlegen unter Kosten- und Leistungsrechnung unter Jahresübernahme durchführen alle Kontrollkästchen deaktivieren.
14 Auf OK klicken.
15 Auf Schließen klicken.

#### 2.1.2 Branchenpaket für neuen Mandanten einrichten

Wählen Sie den Standardkontenrahmen SKR42 und das Branchenpaket Vereine, Stiftungen, gGmbHs.

Branchenpaket für neuen Mandanten wählen
Vorgehen:
1 Leistung Buchführung ist angelegt.
2 Mandantenbestand im DATEV-Rechnungswesen-Programm öffnen.
3 Im Arbeitsblatt Grunddaten Rechnungswesen Wirtschaftsjahresbeginn und Wirtschaftsjahresende prüfen und ggf. ändern.

Der Wirtschaftsjahresbeginn kann nach dem Buchen nicht mehr geändert werden.
4 Basisdaten | DATEV-Standardkontenrahmen: Kontenrahmen wählen.
5 Im Feld Branchenpaket/Lösung: Branchenpaket wählen.
6 In der Programm-Meldung REW90598: Auf OK klicken.
7 Alle weiteren Stammdaten erfassen.
8 Auf Speichern und schließen klicken.

#### 2.1.3 Belege buchen

#### Buchungen mit Sphären erfassen

Das KOST-System Nr. 9 DATEV SKR42 mit Sphärenkostenstellen ist automatisch angelegt. Sie können Buchungen mit Sphären erfassen. [SKR42 Buchungen mit Sphären erfassen und aufteilen (Dok.-Nr. 1022900)](https://help-center.apps.datev.de/documents/1022900 "SKR42 Buchungen mit Sphären erfassen und aufteilen")

Für steuerbegünstigte Körperschaften ist eine Untergliederung nach Sphären / Bereichen erforderlich. Die Sphären werden über Kostenstellen untergliedert. Folgende Kostenstellen sind im Branchenpaket enthalten:

**Kostenstelle****Sphäre / Bereich**
1 Ideeller Bereich, optional Kostenstellen 11 – 19 für weitere Unterteilungen
2 Vermögensverwaltung, optional Kostenstellen 21 – 29 für weitere Unterteilungen
3 Zweckbetrieb; optional Kostenstellen 31-39 für weitere Unterteilungen
4 Wirtschaftlicher Geschäftsbetrieb; optional Kostenstellen 41-49 für weitere Unterteilungen
9 Sammelposten

(noch zu klärende oder die Gesamtkörperschaft betreffenden Positionen)

Erfassen Sie Kostenstellen im Feld KOST1 (Sphäre) des Buchungssatzes.

Blenden Sie in der Buchungszeile das Feld KOST1 ein.

KOST-Feld in Buchungszeile einblenden
Vorgehen:
1 Im Menü: Erfassen | Belege buchen wählen.
2 Buchungsstapel anlegen oder bestehenden Stapel öffnen.
3 Im Zusatzbereich Eigenschaften: Buchungssatz | Optionale Erfassungsfelder |Darstellung der Buchungszeile:Maximal (Gegenkonto-Konto) wählen.
4 Das Kontrollkästchen KOST1 aktivieren.

Nicht benötigte Kontrollkästchen deaktivieren.
5 In der Buchungszeile erscheint das Feld KOST1.

#### 2.1.4 Hinweise

### 2.2 Kostenrechnung

Sie können Kostenrechnung mit dem Feld KOST1 oder mit dem Feld KOST2 auswerten.

Weitere Informationen: [SKR42 Gegenüberstellung KOST1 oder KOST1 & KOST2 nutzen (Dok.-Nr. 1038388)](https://help-center.apps.datev.de/documents/1038388 "SKR42 Gegenüberstellung KOST1 oder KOST1 & KOST2 nutzen")

#### 2.2.1 Im Feld KOST1

Mustervorlage für SKR42 einspielen und anpassen. Sphäre und Kostenstelle werden verknüpft und im Feld KOST1 erfasst.

Nur mit dem Programm Kostenrechnung classic können Sie eine Mustervorlage für SKR42 einspielen und anpassen.

In der Mustervorlage können Sie Kostenstellen anlegen. Zum Beispiel für weitere Zweckbetriebe, Projekte, Abteilungen, Sparten.

Wie Sie eine Kostenrechnung mit SKR42 neu einrichten und im Feld KOST1 nutzen, lesen Sie hier [SKR42 Kostenrechnung einrichten (Dok.-Nr. 1023147)](https://help-center.apps.datev.de/documents/1023147 "SKR42 Kostenrechnung einrichten")

Wie Sie eine bestehende Kostenrechnung anpassen, lesen Sie im Dokument: [SKR42 Bestehende Kostenrechnung anpassen (Dok.-Nr. 1023368)](https://help-center.apps.datev.de/documents/1023368 "SKR42 Bestehende Kostenrechnung anpassen")

#### 2.2.2 Im Feld KOST2

Ein neues KOST-System anlegen und Kostenstellen im Feld KOST2 erfassen. So können Sie im Feld KOST1 die Sphäre und im Feld KOST2 die Kostenstelle erfassen und auswerten.

Wie Sie ein neues KOST-System für KOST2 anlegen, lesen Sie im Dokument: [Kostenrechnung einrichten (Dok.-Nr. 1035751)](https://help-center.apps.datev.de/documents/1035751 "Kostenrechnung einrichten").

Wie Sie eine bestehende Kostenrechnung anpassen, lesen Sie im Dokument: [SKR42 Bestehende Kostenrechnung anpassen (Dok.-Nr. 1023368)](https://help-center.apps.datev.de/documents/1023368 "SKR42 Bestehende Kostenrechnung anpassen")

### 2.3 Personalwirtschaft

LODAS:

[Kontenrahmen SKR42 in LODAS nutzen (Dok.-Nr. 1023730)](https://help-center.apps.datev.de/documents/1023730 "Kontenrahmen SKR42 in LODAS nutzen")

Lohn und Gehalt:

[SKR 42: Buchungen aus Lohn und Gehalt nach Rechnungswesen übergeben (Dok.-Nr. 1022896)](https://help-center.apps.datev.de/documents/1022896 "SKR 42: Buchungen aus Lohn und Gehalt nach Rechnungswesen übergeben")

### 2.4 Anlagenbuchführung

Mit dem Branchenpaket können Sie die Abschreibungen auf die verschiedenen Sphären aufteilen.

Dafür gibt es folgende Möglichkeiten:

*   Direkte Zuordnung der Sphäre im Inventar: [Inventar bearbeiten - Kostenstellen zuordnen (Dok.-Nr. 9211257)](https://help-center.apps.datev.de/documents/9211257 "Inventar bearbeiten - Kostenstellen zuordnen")

*   Prozentuelle Aufteilung eines Inventars auf verschiedene Sphären (Kostenstellen):[SKR42 Abschreibungen auf die verschiedenen Sphären aufteilen (Dok.-Nr. 1022967)](https://help-center.apps.datev.de/documents/1022967 "SKR42 Abschreibungen auf die verschiedenen Sphären aufteilen")

### 2.5 DATEV Unternehmen online

Wenn Sie oder Ihre Mandanten DATEV Unternehmen online nutzen, passen Sie direkt nach der Jahresübernahme die Stammdaten an. Weitere Informationen finden Sie im Dokument [SKR42: Anpassungen in DATEV Unternehmen online (Dok.-Nr. 1024038)](https://help-center.apps.datev.de/documents/1024038 "SKR42: Anpassungen in DATEV Unternehmen online")

### 2.6 Unterstützung bei DATEV buchen (kostenpflichtig)

#### Programmtechnische Umstellung auf SKR42 - ohne Einsatz Kostenrechnung classic

*   Für Steuerberater: [Information und Buchung](https://www.terminland.de/datev_beratung/default.aspx?m=7782&ll=KH9Sj&dpp=KH9Sj&dlgid=1710693591&step=1&dlg=4&a147517210=147517231&a1543578849=1846535784&a164870403=1902016975&a164907492=1903574366&css=1 "https://www.terminland.de/datev_beratung/default.aspx?m=7782&ll=KH9Sj&dpp=KH9Sj&dlgid=1710693591&step=1&dlg=4&a147517210=147517231&a1543578849=1846535784&a164870403=1902016975&a164907492=1903574366&css=1")

*   Für Unternehmer: [Information und Buchung](https://www.terminland.de/datev_beratung/default.aspx?m=7782&ll=KH9Sj&dpp=KH9Sj&dlgid=1710693591&step=1&dlg=4&a147517210=147517264&a1543578849=1846535699&a164870403=1902016975&a164907492=1903574366&css=1 "https://www.terminland.de/datev_beratung/default.aspx?m=7782&ll=KH9Sj&dpp=KH9Sj&dlgid=1710693591&step=1&dlg=4&a147517210=147517264&a1543578849=1846535699&a164870403=1902016975&a164907492=1903574366&css=1")

#### Programmtechnische Umstellung auf SKR42 - mit Einsatz Kostenrechnung classic

*   Für Steuerberater: [Information und Buchung](https://www.terminland.de/datev_beratung/default.aspx?m=7782&ll=KH9Sj&dpp=KH9Sj&dlgid=1710693591&step=1&dlg=4&a147517210=147517231&a1543578849=1846535982&a164870403=1902016975&a164907492=1903574366&css=1 "https://www.terminland.de/datev_beratung/default.aspx?m=7782&ll=KH9Sj&dpp=KH9Sj&dlgid=1710693591&step=1&dlg=4&a147517210=147517231&a1543578849=1846535982&a164870403=1902016975&a164907492=1903574366&css=1")

*   Für Unternehmer: [Information und Buchung](https://www.terminland.de/datev_beratung/default.aspx?m=7782&ll=KH9Sj&dpp=KH9Sj&dlgid=1710693591&step=1&dlg=4&a147517210=147517264&a1543578849=1846535806&a164870403=1902016975&a164907492=1903574366&css=1 "https://www.terminland.de/datev_beratung/default.aspx?m=7782&ll=KH9Sj&dpp=KH9Sj&dlgid=1710693591&step=1&dlg=4&a147517210=147517264&a1543578849=1846535806&a164870403=1902016975&a164907492=1903574366&css=1")

#### Individuelle Einstiegsberatung: Konzeption der Umstellung auf SKR42 bei größeren Bestandskunden mit Kostenrechnung classic

*   Für Steuerberater: [Information und Buchung](https://www.terminland.de/datev_beratung/default.aspx?m=7782&ll=KH9Sj&dpp=KH9Sj&dlgid=1710693591&step=1&dlg=4&a147517210=147517231&a1543578849=2232556583&a164870403=1902016975&a164907492=1903574366&css=1 "https://www.terminland.de/datev_beratung/default.aspx?m=7782&ll=KH9Sj&dpp=KH9Sj&dlgid=1710693591&step=1&dlg=4&a147517210=147517231&a1543578849=2232556583&a164870403=1902016975&a164907492=1903574366&css=1")

*   Für Unternehmer: [Information und Buchung](https://www.terminland.de/datev_beratung/default.aspx?m=7782&ll=KH9Sj&dpp=KH9Sj&dlgid=1710693591&step=1&dlg=4&a147517210=147517264&a1543578849=2232550122&a164870403=1902016975&a164907492=1903574366&css=1 "https://www.terminland.de/datev_beratung/default.aspx?m=7782&ll=KH9Sj&dpp=KH9Sj&dlgid=1710693591&step=1&dlg=4&a147517210=147517264&a1543578849=2232550122&a164870403=1902016975&a164907492=1903574366&css=1")
