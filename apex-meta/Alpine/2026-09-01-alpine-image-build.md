# Runbook: Alpine-Images bauen

Stand: 2026-09-01  
Zielgruppe: Entwickler am lokalen Mac (Apple Silicon oder amd64)  
Gültigkeit: projektübergreifend unter `~/dev/development`

---

## Zweck

Dieses Runbook beschreibt den **standardisierten Workflow** zum Bauen schlanker Container-Images auf Basis von **Alpine Linux**. Es ergänzt den Skill `docker-compose-deploy` (vollständiges Stack-Deployment) und fokussiert auf **Dockerfile-Design, Build, Validierung und Compose-Anbindung**.

---

## Wann Alpine — wann nicht

| Alpine sinnvoll | Alpine vermeiden |
|-----------------|------------------|
| Kleine Runtime-Images, explizite `apk`-Deps | Vorgefertigte **glibc-only** Binaries ohne musl-Build |
| Multi-Stage: kompilieren in `builder`, Artefakte kopieren | Schwere ML-Runtime (PyTorch, CUDA, große Wheels) |
| Go-Rust-C-Projekte mit musl/static build | Viele Python-Pakete ohne musl/manylinux-Wheels |
| Edge-Proxies, Sidecars, CLI-Tools | Wenn offizielles `python:3.x-slim` / `node:slim` weniger Reibung hat |

**Faustregel:** Wenn du Build-Tools und Dev-Header brauchst, aber die Runtime minimal bleiben soll → Alpine Multi-Stage. Wenn du primär `pip install` mit komplexen nativen Extensions machst → eher `debian-slim` oder `python:3.x-slim` (siehe Abschnitt [Rezept-Karten](#6-rezept-karten)).

---

## Standard-Konventionen (verbindlich)

Abgestimmt auf `~/dev/ai-skills/docker-compose-deploy/SKILL.md`.

### Basis-Image

```dockerfile
ARG ALPINE_VERSION=3.21
```

Default-Version: **3.21**. In Compose als Build-Arg durchreichen, damit Upgrades zentral möglich sind.

### Multi-Stage

| Stage | Inhalt |
|-------|--------|
| `builder` | `build-base`, `git`, `*-dev`, Quellcode, Compile/Build |
| `runtime` | Nur Laufzeit-Libraries, App-Artefakte, Locale, non-root User |

Build-Tools **niemals** in die Runtime-Stage kopieren oder dort installieren.

### apk

- Immer `apk add --no-cache …` (kein separater Cache-Cleanup nötig)
- Runtime-Pakete explizit auflisten — kein blindes `apk add build-base` in Runtime
- Wo sinnvoll: Paketversionen pinnen (`package=1.2.3-r0`)

### Deutsche Lokalisierung (Runtime)

In der Runtime-Stage und in `docker-compose.yml` `environment`:

```dockerfile
RUN apk add --no-cache tzdata musl-locales musl-locales-lang \
    && ln -sf /usr/share/zoneinfo/Europe/Berlin /etc/localtime

ENV TZ=Europe/Berlin \
    LANG=de_DE.UTF-8 \
    LC_ALL=de_DE.UTF-8 \
    LC_TIME=de_DE.UTF-8 \
    LC_MONETARY=de_DE.UTF-8 \
    LC_NUMERIC=de_DE.UTF-8 \
    KEYMAP=de-latin1
```

`KEYMAP=de-latin1` ist nur relevant, wenn interaktive Shell/TTY genutzt wird.

### Sicherheit

- **Non-root User:** `addgroup -S app && adduser -S -G app app` → `USER app`
- **Keine Secrets** im Dockerfile (Passwörter, API-Keys über `.env` / Compose)
- `.env` in `.gitignore`, nur `.env.example` mit Platzhaltern committen

---

## Referenz: ki-basis nginx

Produktionsreifes Beispiel: `~/dev/ki-basis/docker/nginx/Dockerfile`

**Was daran gut ist:**

1. **BuildKit-Context** für externe Quellen (`COPY --from=nginx-src`)
2. **Builder:** nur Compile-Deps (`build-base`, `pcre2-dev`, …)
3. **Runtime:** nur Laufzeit-Libs (`pcre2`, `zlib`, `openssl`, `ca-certificates`, …)
4. **Build-Gate:** `nginx -t` in der Runtime-Stage vor dem finalen Image
5. **Non-root:** dedizierter `nginx`-User, Verzeichnisse mit korrekten Rechten
6. **Kein Locale-Block** — nginx braucht keine DE-Locale; für App-Services Locale ergänzen

Kurzüberblick:

```dockerfile
ARG ALPINE_VERSION=3.21

FROM alpine:${ALPINE_VERSION} AS build
RUN apk add --no-cache build-base pcre2-dev zlib-dev openssl-dev linux-headers
# … Quellcode kopieren, ./auto/configure && make …

FROM alpine:${ALPINE_VERSION} AS runtime
RUN apk add --no-cache pcre2 zlib openssl ca-certificates tzdata wget netcat-openbsd \
 && addgroup -S nginx && adduser -S -D -H … -G nginx nginx
COPY --from=build /usr/sbin/nginx /usr/sbin/nginx
COPY --from=build /etc/nginx/ /etc/nginx/
RUN nginx -t
USER nginx
CMD ["nginx", "-g", "daemon off;"]
```

---

## Schritt-für-Schritt: neues Image bauen

### 1. Projektstruktur

```text
myproject/
├── docker/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── .env.example
│   └── scripts/
│       └── find-free-port.sh          # optional
└── src/                               # App-Quellcode
```

Build-Context typisch **Repo-Root** (`context: ..`), Dockerfile unter `docker/Dockerfile`.

### 2. Minimal-Dockerfile (Template)

```dockerfile
# syntax=docker/dockerfile:1
ARG ALPINE_VERSION=3.21

# --- Builder ---
FROM alpine:${ALPINE_VERSION} AS builder

RUN apk add --no-cache build-base git

WORKDIR /build
COPY . .
RUN <build-commands>

# --- Runtime ---
FROM alpine:${ALPINE_VERSION} AS runtime

RUN apk add --no-cache \
    tzdata musl-locales musl-locales-lang \
    <runtime-deps-only> \
    && ln -sf /usr/share/zoneinfo/Europe/Berlin /etc/localtime

ENV TZ=Europe/Berlin \
    LANG=de_DE.UTF-8 \
    LC_ALL=de_DE.UTF-8 \
    LC_TIME=de_DE.UTF-8 \
    LC_MONETARY=de_DE.UTF-8 \
    LC_NUMERIC=de_DE.UTF-8 \
    KEYMAP=de-latin1

WORKDIR /app
COPY --from=builder /path/to/artifacts /app

RUN addgroup -S app && adduser -S -G app app \
    && chown -R app:app /app
USER app

EXPOSE 8080
HEALTHCHECK --interval=10s --timeout=5s --retries=5 --start-period=30s \
  CMD wget -qO- http://127.0.0.1:8080/health || exit 1
CMD ["./myapp"]
```

Platzhalter `<build-commands>`, `<runtime-deps-only>` und Pfade projektspezifisch ersetzen.

### 3. Bauen

```bash
cd ~/dev/myproject

# Direkt mit docker build
docker build \
  -f docker/Dockerfile \
  --build-arg ALPINE_VERSION=3.21 \
  -t myproject:latest \
  .

# Oder über Compose (bevorzugt im Stack)
cd docker
docker compose --env-file .env build --no-cache
```

### 4. Compose validieren (Pflicht vor Deploy)

```bash
cd ~/dev/myproject/docker
docker compose --env-file .env config
```

Syntax-Fehler, fehlende Env-Vars und falsche Volume-/Netzwerk-Referenzen werden hier sichtbar.

### 5. Smoke-Test

```bash
# Container starten und Logs prüfen
docker run --rm -p 127.0.0.1:8080:8080 myproject:latest

# Healthcheck (wenn in Compose definiert)
docker compose up -d
docker inspect --format='{{.State.Health.Status}}' myproject-app
```

### 6. Image-Größe prüfen

```bash
docker images myproject:latest
docker history myproject:latest --no-trunc | head -20
```

Wenn das Image trotz Alpine > 200 MB ist: prüfen, ob Build-Artefakte oder Dev-Pakete in der Runtime landen.

---

## Compose-Anbindung

Snippet für `docker/docker-compose.yml`:

```yaml
name: ${COMPOSE_PROJECT_NAME:-myproject}

services:
  app:
    image: ${APP_IMAGE:-myproject:latest}
    build:
      context: ..
      dockerfile: docker/Dockerfile
      args:
        ALPINE_VERSION: "3.21"
    container_name: ${COMPOSE_PROJECT_NAME:-myproject}
    restart: unless-stopped
    env_file:
      - .env
    environment:
      TZ: Europe/Berlin
      LANG: de_DE.UTF-8
      LC_ALL: de_DE.UTF-8
    ports:
      - "127.0.0.1:${APP_HOST_PORT:-8080}:8080"
    healthcheck:
      test: ["CMD-SHELL", "wget -qO- http://127.0.0.1:8080/health || exit 1"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 30s
```

Host-Binding bevorzugt **`127.0.0.1:<port>`** (nicht `0.0.0.0`), sofern kein LAN-Zugriff nötig ist.

`.env.example`:

```bash
COMPOSE_PROJECT_NAME=myproject
APP_HOST_PORT=8080
APP_IMAGE=myproject:latest
```

---

## Rezept-Karten

### Go (statisches Binary)

```dockerfile
ARG ALPINE_VERSION=3.21

FROM golang:1.23-alpine AS builder
WORKDIR /src
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-s -w" -o /out/myapp ./cmd/myapp

FROM alpine:${ALPINE_VERSION} AS runtime
RUN apk add --no-cache ca-certificates tzdata musl-locales musl-locales-lang \
    && ln -sf /usr/share/zoneinfo/Europe/Berlin /etc/localtime
ENV TZ=Europe/Berlin LANG=de_DE.UTF-8 LC_ALL=de_DE.UTF-8
COPY --from=builder /out/myapp /usr/local/bin/myapp
RUN addgroup -S app && adduser -S -G app app
USER app
ENTRYPOINT ["/usr/local/bin/myapp"]
```

Bei rein statischem Binary ohne TLS/Zeitzone reicht alternativ `FROM scratch` — dann `ca-certificates` und `tzdata` weglassen.

### Node.js

```dockerfile
ARG ALPINE_VERSION=3.21

FROM node:22-alpine AS builder
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build && npm prune --omit=dev

FROM alpine:${ALPINE_VERSION} AS runtime
RUN apk add --no-cache nodejs tzdata musl-locales musl-locales-lang \
    && ln -sf /usr/share/zoneinfo/Europe/Berlin /etc/localtime
ENV TZ=Europe/Berlin LANG=de_DE.UTF-8 LC_ALL=de_DE.UTF-8 NODE_ENV=production
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./
RUN addgroup -S app && adduser -S -G app app && chown -R app:app /app
USER app
EXPOSE 3000
CMD ["node", "dist/server.js"]
```

Alternative: Builder und Runtime beide auf `node:22-alpine`, Runtime ohne `npm`/Dev-Deps — einfacher, etwas größer.

### Python

Alpine + pip ist möglich, aber **musl** bricht oft native Wheels. Nur wählen, wenn alle Dependencies musl-kompatibel sind oder aus Source bauen.

```dockerfile
ARG ALPINE_VERSION=3.21

FROM python:3.12-alpine AS builder
RUN apk add --no-cache build-base libffi-dev
WORKDIR /app
COPY pyproject.toml ./
RUN pip install --no-cache-dir .

FROM alpine:${ALPINE_VERSION} AS runtime
RUN apk add --no-cache python3 py3-pip tzdata musl-locales musl-locales-lang \
    && ln -sf /usr/share/zoneinfo/Europe/Berlin /etc/localtime
ENV TZ=Europe/Berlin LANG=de_DE.UTF-8 LC_ALL=de_DE.UTF-8
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY app/ ./app/
RUN addgroup -S app && adduser -S -G app app && chown -R app:app /app
USER app
CMD ["python3", "-m", "app"]
```

**Empfehlung bei komplexen Stacks** (FastAPI + httpx + native Extensions): `python:3.12-slim` wie in `agent-orchestrator/docker/gliner-sidecar/Dockerfile` — kleiner Overhead, weniger musl-Reibung.

---

## Validierung & Review

### Checkliste vor Merge/Deploy

- [ ] `docker build` / `docker compose build` ohne Fehler
- [ ] `docker compose config` ok
- [ ] Runtime-Stage enthält **kein** `build-base`, `git`, `*-dev`
- [ ] Locale gesetzt (`TZ`, `LANG`, `LC_*`) — sofern App DE-Kontext braucht
- [ ] Container läuft als **non-root**
- [ ] Healthcheck definiert und grün
- [ ] Keine Secrets im Dockerfile oder Git
- [ ] Image-Größe plausibel (keine Build-Artefakte in Runtime)

### Stack-Review

Für bestehende Compose-Setups den Skill **`docker-compose-review`** nutzen (`~/dev/ai-skills/docker-compose-review/SKILL.md`): Ports, Secrets, Ressourcen-Wiederverwendung, Image-Hygiene.

---

## Troubleshooting

| Symptom | Ursache | Fix |
|---------|---------|-----|
| `exec format error` | Arch-Mismatch (arm64 vs amd64) | `--platform linux/arm64` setzen oder auf Zielarch bauen |
| `Error loading shared library …` | musl vs. glibc Binary | Für Alpine musl-kompilieren oder glibc-Base wählen |
| `pip install` schlägt fehl | Kein Wheel für musl | `build-base` + `-dev`-Header in Builder, oder `python:slim` |
| Paket in `apk` nicht gefunden | Paket in community/testing | `/etc/apk/repositories` prüfen; ggf. `@community` |
| Image > erwartet trotz Alpine | Build-Artefakte in Runtime | Multi-Stage prüfen; `.dockerignore` ergänzen |
| `nginx -t` / App-Start schlägt in Build fehl | Fehlende Runtime-Dateien | COPY-Pfade und Config-Platzhalter prüfen |
| Locale wirkt nicht | `musl-locales` fehlt | Paket + `LANG`/`LC_ALL` in Runtime und Compose |
| Permission denied auf Volume | User ohne Schreibrechte | `chown` im Dockerfile oder named Volume mit passendem User |

### Nützliche Debug-Befehle

```bash
# Shell in laufendem Container (nur lokal/debug)
docker run --rm -it --entrypoint /bin/sh myproject:latest

# Installierte Pakete in Runtime
docker run --rm --entrypoint /bin/sh myproject:latest -c "apk info -e"

# Welche Dateien Layer vergrößern
docker history myproject:latest --human --format "{{.Size}}\t{{.CreatedBy}}"
```

---

## Abgrenzung

| Thema | Wo dokumentiert |
|-------|-----------------|
| Volumes, Netzwerke, Homarr, OKF, AnythingLLM | Skill `docker-compose-deploy` |
| Stack-Review vor Merge | Skill `docker-compose-review` |
| Bestehende Images migrieren (z. B. slim → Alpine) | Projektentscheidung; dieses Runbook nur als Entscheidungshilfe |

---

## Referenzen

- Skill Deploy: `~/dev/ai-skills/docker-compose-deploy/SKILL.md`
- Templates: `~/dev/ai-skills/docker-compose-deploy/templates.md`
- Skill Review: `~/dev/ai-skills/docker-compose-review/SKILL.md`
- Referenz-Image: `~/dev/ki-basis/docker/nginx/Dockerfile`
- Gegenbeispiel Python-slim: `~/dev/development/agent-orchestrator/docker/gliner-sidecar/Dockerfile`
