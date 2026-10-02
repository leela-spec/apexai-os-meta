„Preflight DONE“ ist zu optimistisch

Die Seite behauptet:



„Preflight — DONE, proved exactly what’s broken“

Das würde ich deutlich abschwächen. Ein vollständiger Preflight wäre erst abgeschlossen, wenn mindestens nachweisbar dokumentiert ist:

1. Welcher Windows-Prozess führt opCall.js tatsächlich aus?
2. Welches node.exe wird verwendet?
3. Welche Base URL verwendet die Skill-Konfiguration?
4. Welcher Docker-Kontext / welche Docker Engine betreibt OpenProject?
5. Wie lautet das reale Docker-Portmapping?
6. Auf welchen WSL-Adressen lauscht der Host-Port?
7. Ist Windows localhost:8083 per TCP erreichbar?
8. Liefert Windows localhost:8083 eine OpenProject-HTTP-Antwort?
9. Kann der echte opCall.js-Skill einen read-only API-Aufruf ausführen?
10. Welche Typen meldet OpenProject für Projekt 3 über API?
11. Ist ein Preview ohne Write möglich?
12. Wird ein Write ohne explizites Confirmation-Token technisch blockiert?

Solange Punkt 9 bis 12 fehlen, ist nicht der Skill-Preflight abgeschlossen. Allenfalls ist eine Teil-Diagnose des Netzwerkproblems erfolgt.

Bessere Formulierung:



P0 · Evidence collection — partially complete
Der Fehler wurde aus dem Agent-Kontext reproduziert. Docker-/WSL-Netzmodus, Windows-Listener und der echte Skill-Read-Test werden jetzt als verbindlicher, read-only Preflight dokumentiert.



Option C wird zu Unrecht als Zielabweichung dargestellt

Der Satz:



„Install Node inside WSL … deviates from all agents run the identical skill“

ist nicht zwingend richtig. Das hängt davon ab, was „identisch“ bedeutet.

Wenn alle Agenten auf Windows dieselbe Wrapper-Schnittstelle verwenden, etwa:

openproject-skill project get --id 3
openproject-skill work-package preview-create ...
openproject-skill work-package apply --confirmation ...

und dieser Wrapper intern kontrolliert ausführt:

wsl.exe -d Ubuntu -- node /opt/openproject-skill/opCall.js ...

dann verwenden weiterhin alle Agenten:





dieselbe Skill-Version,



denselben Code,



dieselben API-Guards,



dieselben Policies,



dieselbe Konfiguration,



dieselben Audit-Mechanismen.

Der Transport ist dann nur ein Implementierungsdetail.

Für dein Setup hat C sogar wichtige Vorzüge:





OpenProject und Skill-CLI laufen im selben Linux-/WSL-Netzraum.



OpenProject kann auf Loopback beschränkt bleiben.



Kein breiteres Container-Port-Publishing notwendig.



Kein globaler Wechsel zu mirrored networking.



Die Netzwerkgrenze ist nicht Teil jedes einzelnen Agent-Requests.



Die Einheitlichkeit lässt sich besser über Git, Versionspinning und einen Windows-Wrapper erzwingen.

Die Kosten sind real:





Zweite Node-Installation bzw. Runtime-Verwaltung.



Ein sauberer wsl.exe-Wrapper ist nötig.



Secrets und Konfiguration müssen eindeutig verwaltet werden.



Der WSL-Start/Idle-Zustand muss zuverlässig abgefangen werden.

Aber bei einem privacy-/self-hosting-orientierten System würde ich diese Variante nicht als bloß „konservativ“ behandeln, sondern als ernstzunehmende Sicherheits- und Wartungsoption.

Meine überarbeitete Empfehlung

Ich würde die drei Optionen nicht schon als A > B > C bewerten, bevor die Architekturfrage beantwortet ist. Stattdessen:







Priorität



Entscheidung



Empfehlung





1



Soll der Skill ein Windows-nativer Prozess bleiben?



Falls ja: kontrolliertes Container-Publishing prüfen





2



Soll OpenProject ausschließlich im WSL-Innenraum erreichbar bleiben?



Falls ja: Node + Skill in WSL, Windows-Wrapper davor





3



Braucht ihr ohnehin breites bidirektionales Windows↔WSL-Netz?



Falls ja: mirrored networking als eigenes, getestetes Infrastrukturprojekt





4



Soll das Ziel minimaler Änderungsumfang sein?



Erst Windows↔WSL-Test durchführen; dann punktuell Portfreigabe oder WSL-Wrapper

Für deine konkrete Umgebung wäre mein bevorzugter Zielzustand wahrscheinlich:

Windows-Agenten
    │
    │ Einheitlicher, versionierter Windows-Launcher
    ▼
wsl.exe -d <Distro> -- node /opt/openproject-skill/opCall.js
    │
    │ localhost innerhalb derselben WSL-Distribution
    ▼
OpenProject API via 127.0.0.1:8083
    │
    ▼
OpenProject-Container

Das ist nicht deshalb besser, weil Windows→WSL-Portweiterleitung „schlecht“ wäre. Es ist besser, weil es eure Vertrauensgrenze sauber hält:





Agenten erhalten nur eine kontrollierte CLI.



Der Skill muss nicht nach außen publiziert werden.



OpenProject bleibt loopback-nah.



Netzwerkverhalten bleibt einfach.



Der Skill kann unabhängig von Windows-Portweiterleitung getestet werden.



Der Windows-Launcher kann für alle fünf Agenten exakt gleich sein.

Wenn dagegen die Agenten unbedingt direkt und ohne Wrapper eine Node-CLI auf Windows ausführen sollen, ist die kontrollierte Publish-Variante legitim — aber sie benötigt bewusstes Hardening.

Sichere Reihenfolge

Ich würde den Ablauf in der Grafik so ändern:

P0  Read-only evidence capture
    └─ Runtime, Node, Skill config, WSL mode, Docker mode, ports, listener

P1  Decide trust boundary
    ├─ Skill runs in WSL: WSL-wrapper architecture
    └─ Skill runs natively in Windows: minimal Windows↔WSL transport change

P2  Implement skill doctor
    ├─ API reachability
    ├─ authentication
    ├─ correct OpenProject instance
    ├─ expected project access
    ├─ project-specific allowed types
    └─ write gate verification

P3  Configure Leela work-package types
    ├─ Enable only required types
    ├─ Prefer project-specific activation
    └─ Read back effective types through API

P4  Dry run
    ├─ Read project
    ├─ Resolve types by name
    ├─ Build preview
    └─ No mutation

P5  Controlled creation
    ├─ Explicit confirmation
    ├─ Exact approved payload
    ├─ Create once
    └─ Re-read and log result

Die Typen würde ich erst nach dem Netzwerk-/Skill-Entscheid durchführen, aber noch vor dem ersten echten Preview. OpenProject erlaubt, Work-Package-Typen pro Projekt zu aktivieren und zu deaktivieren; eine Aktivierung in Leela ist damit die passende, eng begrenzte Konfiguration — nicht zwingend eine globale Aktivierung für alle Projekte.[openproject][openproject]

Konkrete Textkorrekturen

Ich würde diese Sätze direkt ersetzen:







Aktuelle Aussage



Bessere Aussage





„Windows automatically forwards to.“



„WSL kann diese Bindung für Windows-localhost weiterleiten; das wird in dieser Installation unmittelbar getestet.“





„We proved this live.“



„Der Fehler wurde aus dem vorgesehenen Agent-Kontext reproduziert. Die zugrunde liegende Weiterleitungsursache wird mit Listener- und HTTP-Tests bestätigt.“





„P0 — DONE.“



„P0 — Netzwerkfehler reproduziert; vollständiger Skill-Preflight noch offen.“





„C deviates from identical skill.“



„C verwendet denselben Skill-Code, benötigt aber einen einheitlichen Windows→WSL-Launcher und eine zweite Node-Runtime.“





„0.0.0.0 (the building).“



„0.0.0.0 (alle WSL-Netzwerkschnittstellen).“





„Leela currently only has three switched on.“



„Die API-/UI-Prüfung zeigte aktuell nur diese Typen als verfügbar: …“ — nur mit tatsächlicher Liste und Zeitstempel.





„OpenProject knows seven types.“



„In dieser Instanz sind derzeit folgende globalen Typen angelegt: …“ — niemals als allgemeine OpenProject-Tatsache formulieren.

Der letzte Punkt ist wichtig: OpenProject hat keine weltweit feste, unveränderliche Liste von sieben Typen. Instanzadministratoren können Typen anlegen, ändern oder entfernen. Die Liste muss daher als Beobachtung eurer Instanz ausgewiesen werden, nicht als Produktgesetz. Die projektweise Aktivierung ist hingegen explizit vorgesehen.[openproject][openproject]

Fazit

Die Seite ist ein guter Versuch, Transparenz herzustellen, und sie adressiert berechtigt den vorherigen Vertrauensbruch. Sie sollte aber erst nach vier Korrekturen als verbindlicher Plan gelten:





Keine absolute Behauptung, dass die Ursache vollständig bewiesen ist.



0.0.0.0 nicht als automatisch sichere bzw. garantierte Weiterleitung verkaufen.



Die WSL-Variante als gleichwertige Architekturentscheidung behandeln, nicht als Abweichung vom gemeinsamen Skill.



„Preflight completed“ erst sagen, wenn der echte Skill aus dem realen Agent-Kontext mindestens read-only durchläuft und die erlaubten Typen für Leela selbst abfragt.