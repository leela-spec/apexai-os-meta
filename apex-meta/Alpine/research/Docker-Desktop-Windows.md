# Docker Desktop Windows — Research Input and Current Disposition

> **Status:** NON-AUTHORITATIVE RESEARCH INPUT / provenance preserved.  
> **Runtime authority:** `ki-basis/compose.yaml`, live runtime behavior, `ARCHITEKTUR-BASIS.md`, and `04A-DOCKER-BACKGROUND-RUNTIME.md`.

## Current disposition

The supplied analysis correctly motivates avoiding unnecessary Docker Desktop Dashboard/UI use and measuring host overhead before per-service tuning.

Technical clarification:

- Current supported target: Docker Desktop **background runtime** + Hyper-V Linux VM + Docker Engine, Dashboard closed.
- Not equivalent: fully quit/stop Docker Desktop and expect its Linux Docker Engine to continue independently.
- True no-Desktop Linux Engine: separate Linux VM + independently managed Docker Engine, which would be a runtime migration.

Adopted now:

- CLI-first/background operation;
- Dashboard closed/not auto-opened;
- control-plane restart guard after sleep/resume failures;
- measure before service-level tuning;
- no `.wslconfig` on the Hyper-V target.

Not adopted now:

- manual Linux-VM migration solely to remove the Dashboard;
- Windows-native `dockerd.exe` for the Linux stack;
- speculative worker/memory/Postgres/Valkey tuning.

---

## Original supplied analysis

Deine Analyse ist technisch schlüssig und deckt sich mit bekannten Docker-Desktop-Problemen unter Windows: Der eigentliche Container-Stack ist mit ~1,4 GB tatsächlich „lean“, aber Docker Desktop als Electron-App plus Hyper‑V/WSL2-VM erzeugt Host-Overhead (DWM, Memory Compression, GPU-Hooks), der auf einem 32‑GB-Laptop trotzdem spürbare UI-Lags auslösen kann. [reddit](https://www.reddit.com/r/windows/comments/1ti3go0/every_windows_operating_system_ordered_by/)

## Kurze Einschätzung deiner Diagnose

- **Container-Messung (~1,4 GB)** ist plausibel und entspricht typischen Werten für Paperless + OpenProject + Postgres + Helper. [docs.opsramp](https://docs.opsramp.com/support/reference/agent-templates/g2-agent-template-details/)
- **Docker Desktop GUI + GPU-Hooks** können DWM (Desktop Window Manager) aufblähen und zu Maus-/Klick-Lags führen – das ist ein bekanntes Windows-Phänomen bei schweren Electron-Apps mit Grafikbeschleunigung. [reddit](https://www.reddit.com/r/windows/comments/1ti3go0/every_windows_operating_system_ordered_by/)
- **Memory Compression ~2 GB** deutet auf echten Host-Druck hin; Windows komprimiert dann aktiv Seiten, was spürbare Verzögerungen beim Fensterwechsel erzeugt. [news.ycombinator](https://news.ycombinator.com/item?id=46574707)
- **OpenProject als größter Einzelverbraucher (~890 MB)** passt zur Puma-Cluster-Architektur; weniger Worker = weniger RAM, dafür geringerer Durchsatz. [oneuptime](https://oneuptime.com/blog/post/2026-02-08-how-to-optimize-docker-for-memory-intensive-applications/view)

Alles in allem: Du hast die richtigen Hebel identifiziert.

## Konkrete, praxistaugliche Maßnahmen (priorisiert)

### 1. Docker Desktop GUI schließen / „headless“ betreiben (schnellster Gewinn)

Das bringt sofort Entlastung für DWM und GPU-Kontexte.

- **Manuell:** Docker Desktop App schließen, Engine aber laufen lassen (im Taskmanager prüfen, ob `Docker Desktop.exe` wirklich weg ist; `com.docker.backend` kann bleiben).
- **Optional:** Im Docker Desktop Settings „Start Docker Desktop when you log in“ deaktivieren und nur den Daemon (bzw. WSL2-Backend) nutzen. Viele Nutzer fahren den Stack per `docker compose up -d` aus dem Terminal und lassen die GUI komplett zu. [reddit](https://www.reddit.com/r/windows/comments/1ti3go0/every_windows_operating_system_ordered_by/)

Wenn du ohnehin meist per CLI arbeitest (was bei deinem Stack typisch ist), ist das die sauberste Lösung.

### 2. OpenProject Worker reduzieren

Das adressiert den größten Einzelblock im Stack.

- Umgebungsvariable setzen (je nach Setup im `docker-compose.yml` oder `.env`):

  ```yaml
  services:
    openproject:
      environment:
        - OPENPROJECT_WEB_WORKERS=1
        # ggf. auch:
        # - OPENPROJECT_BACKGROUND_WORKERS=1
  ```

- Erwartung: RAM von ~900 MB auf ~400–500 MB, dafür etwas weniger Parallelität bei Requests/Background-Jobs. Für lokale / KMU-Nutzung meist völlig ausreichend. [oneuptime](https://oneuptime.com/blog/post/2026-02-08-how-to-optimize-docker-for-memory-intensive-applications/view)

### 3. Harte Ressourcenlimits im Compose-File

Damit verhinderst du, dass einzelne Dienste bei Lastspitzen den Host in Memory-Compression treiben.

Beispiel (Auszug):

```yaml
services:
  openproject:
    deploy:
      resources:
        limits:
          memory: 1.5G
        reservations:
          memory: 512M

  paperless:
    deploy:
      resources:
        limits:
          memory: 768M
        reservations:
          memory: 256M

  hermes:
    deploy:
      resources:
        limits:
          memory: 512M
        reservations:
          memory: 128M
```

Hinweis: `deploy.resources` wirkt voll nur im Swarm-Modus; im reinen Compose-Betrieb sind `mem_limit` / `memory` (v2-Format) oft direkter:

```yaml
services:
  openproject:
    mem_limit: 1.5g
    mem_reservation: 512m
```

Das entspricht der Empfehlung, für produktive Container immer explizite Memory-Limits zu setzen, um OOM und Host-Thrashing zu vermeiden. [oneuptime](https://oneuptime.com/blog/post/2026-02-08-how-to-optimize-docker-for-memory-intensive-applications/view)

### 4. Optional: WSL2-VM global begrenzen (falls du WSL2-Backend nutzt)

Falls du Docker Desktop mit WSL2 betreibst, kannst du zusätzlich die gesamte WSL2-VM im Griff behalten:

- `%USERPROFILE%\.wslconfig` anlegen / bearbeiten:

  ```ini
  [wsl2]
  memory=6GB
  swap=2GB
  pageReporting=false
  ```

Das verhindert, dass die VM bei Last dynamisch zu viel Host-RAM frisst und die Memory Compression anwirft. [reddit](https://www.reddit.com/r/windows/comments/1ti3go0/every_windows_operating_system_ordered_by/)

## Empfohlener nächster Schritt (pragmatisch)

Ich würde in dieser Reihenfolge vorgehen:

1. **Stack stoppen, Docker Desktop GUI schließen**, dann kurz prüfen, ob Maus/Window-Responsiveness sofort besser wird. Das gibt dir ein klares „Ja/Nein“ zur DWM/GPU-Hypothese.
2. Wenn das hilft:  
   - **OpenProject auf 1 Worker** stellen  
   - **Memory-Limits** für OpenProject, Paperless, Hermes setzen  
   - Optional **`.wslconfig`** mit z. B. `memory=6GB` ergänzen  
   - Stack wieder starten und unter Last beobachten.

Wenn du magst, kann ich dir ein konkretes, minimales Diff für dein `docker-compose.yml` (und optional `.wslconfig`) vorschlagen, das genau diese drei Punkte (1 Worker + Limits + WSL2-Cap) umsetzt.