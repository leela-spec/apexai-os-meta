---
type: Operator Feedback
title: Feedback zu INFRASTRUCTURE.md + InstallationInsights.md — was als Nächstes zu tun ist
description: >
  Priorisierte Einschätzung auf Basis des aktuellen Infrastruktur-Ist-Zustands und der
  Installations-Fehlerhistorie auf der Windows/WSL2-Maschine (ki-basis / ki-büro).
created: 2026-09-29
sources:
  - INFRASTRUCTURE.md
  - InstallationInsights.md
status: opinion / action plan
---

# Feedback: Was als Nächstes zu tun ist

**Kurzfassung.** Die Architektur ist im Wesentlichen **fertig und grün** (Health 29/29, ADR-002, ein Engine, ein Postgres). Das Problem ist nicht „noch einmal neu installieren“, sondern **einen offenen Transport-Bug schließen**, die gleichen Annahmen bei den anderen Host-Ports prüfen, und dann **Prozess + Install-Skript** so härten, dass die letzten drei Monate Detours nicht wiederholt werden.

---

## 1. Lagebild (meine Lesart)

| Schicht | Zustand | Konsequenz |
|---|---|---|
| Engine / Compose / Shared DB | laut `INFRASTRUCTURE.md` live und verifiziert | **Nicht** noch einmal Engine oder Dual-Postgres diskutieren |
| Private + Community Stacks | getrennt, Portbänder 808x / 908x | Asymmetrie Hermes (Bind vs. Named Volume) **bewusst lassen** |
| Doku-Wahrheit | `INFRASTRUCTURE.md` als Hub | Konkurrierende „current“-Docs nicht neu füttern |
| Nutzbarkeit von Windows aus | **R11 offen** (`ECONNREFUSED 127.0.0.1:8083`) | Ohne Fix bleibt OpenProject-Skill / Windows-Agent tot |
| Prozess | „geschrieben = wahr“, Patch-Bundles nie applied | Größeres Risiko als fehlende Features |

Die Insights-Datei ist die richtige Diagnose: Die teuren Fehler waren **fehlende Entscheidungen**, **falsche Defaults** (Docker Desktop, `/mnt/c`, VM-RAM) und **Status vor Evidence**. Der Stack nach dem Pivot ist dagegen die richtige Zielrichtung — daran festhalten.

---

## 2. Priorisierte To-dos

### P0 — Sofort (ohne Architekturänderung)

1. **R11 schließen (OpenProject von Windows erreichbar machen)**  
   Empfohlene Variante aus den Insights: Ports für Windows-Agent-relevante Services in WSL2 auf `0.0.0.0` publishen (nicht `127.0.0.1` im Compose).  
   Danach **von Windows** (nicht aus WSL) prüfen:
   - `curl http://127.0.0.1:8083` (OpenProject / leela-op178)
   - analog Firefly / Paperless / Hermes-Gateway / Nginx der privaten und Community-Bande  
   Ohne diesen Windows-seitigen Beweis gilt nichts als „reachable“.

2. **Operator-Blocker auflösen**  
   Docker-Gruppenzugriff freigeben, damit der Fix wirklich applied werden kann — nicht nur diskutiert. Ohne Schreibzugriff auf Compose/Engine bleibt R11 dauerhaft „vorgeschlagen“.

3. **Gleichen Loopback-Bug bei Firefly, Paperless, Hermes, Nginx auditieren**  
   R11 sagt explizit: die wurden nie gegen denselben WSL2-NAT-Fall geprüft. Einmalige Port-Publish-Matrix + Windows-`curl`-Checks, Ergebnis in `INFRASTRUCTURE.md` §6 nachziehen.

### P1 — Stabilität sichern (kurze Session, kein Redesign)

4. **Pre-`up`-Guard für Hermes-Volumes (R5)**  
   Vor jedem `compose up` prüfen: deklarierter Mount-Typ == live Mount-Typ. Sonst fail-closed. Das ist der einzige Weg, einen erneuten Near-Data-Loss (~7.9 GB) zu verhindern.

5. **Alias-/Identitäts-Check vor Stack-Änderungen (R4)**  
   Kein zweites `postgres`-Alias auf demselben Netz; OpenProject nur als `leela-op178-openproject` referenzieren; alte Compose-Blöcke nicht copy-paste ohne Identity-Check.

6. **Health-Test als Definition of Done**  
   `infra-health-test.sh` nach jedem Infra-Eingriff grün — und dasselbe Prinzip für Skill-/App-„Preflight DONE“ (R9). Kein Status ohne Live-Check.

7. **Keepalive + `.wslconfig` nicht „nebenbei“ ändern**  
   Memory/Swap-Änderungen brauchen `wsl --shutdown` → stoppt alle Stacks. Operator-gated belassen; nicht in Agent-Sessions stillschweigend anfassen.

### P2 — Installierbarkeit für den nächsten Rechner / nächsten Operator

8. **Ein Install-Skript bauen, das Abschnitt 3 der Insights 1:1 abbildet**  
   Reihenfolge verbindlich:
   1. Engine-Gate (nur WSL2-native dockerd; Docker Desktop = Fail)
   2. Filesystem-Gate (kein State unter `/mnt/c`)
   3. `shared-db-net` + Shared Postgres + Roles + `REVOKE CONNECT` + `vector` als Superuser
   4. Private Stack (`ki-basis`, Hermes-Binds)
   5. Community Stack (Named Volumes, kein OneDrive)
   6. OpenProject `leela-op178` frisch, per Container-Name
   7. Ports `0.0.0.0` + Windows-`curl`-Proof
   8. Health-Test grün = fertig  

   Kein zweites Runbook parallel. `INFRASTRUCTURE.md` bleibt die Wahrheit; das Skript ist der einzige „How to get there“.

9. **Superseded Docs nur bannern, nicht pflegen**  
   Alles, was Docker Desktop, zwei Postgres-Cluster, Arch-3/Nested, OpenClaw/local-LLM oder alte v14-OP beschreibt, muss klar als Geschichte markiert bleiben (R10). Keine „Korrekturprogramme“, die konkurrierende Current-Docs erzeugen.

### P3 — Prozessregeln (sonst wiederholt sich die Timeline)

10. **Patch-Status explizit tracken** (R12): `proposed` / `applied` / `superseded`. Chat-Output ≠ Repo-Stand.  
11. **Keine Feature-Arbeit auf ungetesteten Transport-Annahmen.** Skill erst, wenn Windows-`curl` grün ist.  
12. **Keine lokalen LLM-/GPU-Pfade** in den Install (R8) — Hermes bleibt auf Hosted Models, bis Hardware bewusst validiert ist.

---

## 3. Was bewusst *nicht* zu tun ist

- **Nicht** Docker Desktop wieder einführen oder „Hybrid“-Engines bauen.
- **Nicht** einen zweiten Postgres-Cluster für Isolation aufsetzen (`REVOKE CONNECT` reicht).
- **Nicht** Hermes-Bind vs. Community-Named-Volumes „harmonisieren“.
- **Nicht** State oder Git unter `/mnt/c` oder OneDrive legen.
- **Nicht** `--remove-orphans` blind auf gemischten Engine-/Projektständen.
- **Nicht** die Architektur dokumentieren, bevor der Live-Stand geprüft ist — und nicht „DONE“ schreiben, bevor die eigenen Completion-Kriterien abgehakt sind.
- **Nicht** die letzten Monate an Korrektur-Bundles aus Downloads nachträglich „alle anwenden“. Stattdessen: nur das, was den **aktuellen** Ist-Stand (INFRASTRUCTURE) absichert oder R11/P1 schließt.

---

## 4. Empfohlene Reihenfolge für die nächste Arbeitssitzung

```text
[ ] Docker-Gruppenzugriff freigeben (Operator)
[ ] OpenProject (+ ggf. andere Agent-Ports) auf 0.0.0.0 umstellen
[ ] Von Windows: curl gegen 8083 / 8086 / 8010 / 8642 / 8084 (und Community-Bande)
[ ] Ergebnis in INFRASTRUCTURE.md Ports-Abschnitt nachziehen
[ ] Pre-up Mount-Guard für Hermes skizzieren/landen
[ ] infra-health-test.sh erneut grün
[ ] Erst dann: OpenProject-Skill (opCall.js) wieder testen
[ ] Parallel/danach: Install-Skript aus Insights §3, kein zweites Architektur-Dokument
```

---

## 5. Urteil

Du hast die **richtige Zielarchitektur** erreicht und teuer dafür bezahlt (Desktop-Detour, RAM-Freeze, Volume-Drift, Alias-Incidents). Der Hebel jetzt ist klein und konkret: **Windows↔WSL2-Port-Publish beweisen und fixen**, denselben Check auf alle Agent-Ports ausweiten, Guards gegen die bekannten Data-Loss-/Alias-Fallen setzen, und Install + Prozess so zuschneiden, dass „geschrieben“ und „gemessen“ nicht wieder auseinanderlaufen.

Alles andere (neue Stack-Ideen, Engine-Debatten, Skill-Features ohne Transport) erhöht nur wieder die Wahrscheinlichkeit, R1–R12 zu wiederholen.
