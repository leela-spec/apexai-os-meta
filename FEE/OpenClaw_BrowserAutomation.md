Ja. **OpenClaw kann genau solche Workflows umsetzen** – inklusive echten Chrome-Tabs, Login-Sessions und dem automatischen Absenden vordefinierter Prompts.

Wichtig ist nur die OpenClaw-Terminologie: Der **`browser`-Tool** führt Aktionen tatsächlich aus; ein **Skill** (`SKILL.md`) beschreibt den wiederholbaren Workflow, also z. B. „öffne ChatGPT → wähle bestehenden Chat → füge Prompt X ein → absenden → Antwort auslesen“. OpenClaw selbst beschreibt Skills ausdrücklich als Instruktionspakete über vorhandenen Tools. ([OpenClaw](https://docs.openclaw.ai/tools "Overview - OpenClaw"))

|Anforderung|OpenClaw|Umsetzung|
|---|---|---|
|Chrome öffnen/steuern|**Ja**|eingebautes `browser`-Tool|
|Klicken, tippen, Formulare ausfüllen|**Ja**|Browser Actions / Playwright|
|Bestehende eingeloggte Chrome-Session verwenden|**Ja**|offizielle Chrome Extension|
|ChatGPT.com bedienen|**Ja**|Browser oder spezielle ClawHub Skills|
|Vordefinierte Prompts einfügen + absenden|**Ja**|eigener Skill oder vorhandener ChatGPT-Skill|
|Antwort auslesen|**Ja**|Browser Snapshot/Text Extraction|
|Gleichen Ablauf regelmäßig wiederholen|**Ja**|OpenClaw Automations/Cron|
|Mehrstufige Browser-Automation|**Ja**|eingebauter `browser-automation` Skill / Community Skills|

### 1. Offizielle Chrome-Steuerung ist bereits eingebaut

OpenClaw hat inzwischen eine **offizielle Chrome Extension**. Damit kann der Agent deine bereits eingeloggten Chrome-Tabs kontrollieren – also nicht nur einen separaten Headless-Browser. Die Extension kann je nach Berechtigung entweder alle normalen Tabs oder nur explizit freigegebene Tabs sehen und steuern. ([OpenClaw](https://docs.openclaw.ai/tools/chrome-extension "Chrome Extension - OpenClaw"))

Der Browser kann u. a. **Tabs öffnen, fokussieren und schließen sowie klicken, tippen, ziehen, auswählen, Screenshots erstellen und Seiteninhalte auslesen**. Zusätzlich liefert OpenClaw selbst einen gebündelten `browser-automation` Skill für robuste mehrstufige Abläufe mit. ([OpenClaw](https://docs.openclaw.ai/tools/browser "Browser (OpenClaw-managed) - OpenClaw"))

Für dein Beispiel könnte ein Workflow also konzeptionell so aussehen:

```text
OpenClaw
    ↓
browser tool
    ↓
Chrome Extension
    ↓
bereits eingeloggter Chrome
    ↓
chatgpt.com
    ↓
Promptfeld finden
    ↓
vordefinierten Prompt einsetzen
    ↓
abschicken
    ↓
Antwort abwarten
    ↓
Antwort extrahieren
    ↓
nächster Verarbeitungsschritt
```

### 2. Es existieren sogar spezielle ChatGPT-Web-Skills

Auf **ClawHub** gibt es bereits Skills, die genau diesen Spezialfall implementieren.

**`@placidusaxalarak/chatgpt-skill` – ChatGPT Web Skill**

Der Skill ist explizit dafür vorgesehen, ChatGPT über die **Weboberfläche statt über die OpenAI API** zu bedienen. Er unterstützt persistente Login-Sessions, einzelne Prompts und länger laufende Multi-Turn-Unterhaltungen. ([ClawHub](https://clawhub.ai/placidusaxalarak/skills/chatgpt-skill "ChatGPT Web Skill — ClawHub"))

Installation:

```bash
openclaw skills install @placidusaxalarak/chatgpt-skill
```

Intern kann beispielsweise eine Frage direkt als Browser-Workflow gestartet werden:

```bash
python3 scripts/run.py ask_chatgpt.py --question "Mein vordefinierter Prompt"
```

Noch direkter ist:

**`@lainxxx/gpt-web-chat-skill` – GPT Web Chat Skill**

Dieser Skill ist ausdrücklich für **Chrome-Automation von chatgpt.com** gebaut: Login prüfen, vorhandenen Tab wiederverwenden, Prompt senden, Antwort abwarten und strukturiert zurückgeben. ([ClawHub](https://clawhub.ai/lainxxx/skills/gpt-web-chat-skill "GPT Web Chat Skill — ClawHub"))

```bash
openclaw skills install @lainxxx/gpt-web-chat-skill
```

Sein Ablauf ist im Wesentlichen:

```text
Chrome vorhanden?
    ↓
ChatGPT Tab vorhanden?
    ↓
Login vorhanden?
    ↓
Prompt senden
    ↓
Antwort abwarten
    ↓
Antwort als strukturiertes Ergebnis zurückgeben
```

Das kommt deinem beschriebenen Szenario sehr nahe. ([ClawHub](https://clawhub.ai/lainxxx/skills/gpt-web-chat-skill "GPT Web Chat Skill — ClawHub"))

### 3. Für beliebige Websites gibt es allgemeinere Browser-Skills

Falls es nicht nur um ChatGPT geht, gibt es beispielsweise **`openclaw-skill-browser-use`**. Dieser kombiniert `agent-browser` und `browser-use` und kann selbstständig Websites öffnen, Elemente finden, Textfelder befüllen, Buttons anklicken, Sessions erhalten und komplexe Multi-Step-Workflows durchführen. ([ClawHub](https://clawhub.ai/yinj0012/skills/openclaw-skill-browser-use "Openclaw Skill Browser Use — ClawHub"))

Beispielsweise technisch:

```bash
agent-browser open "https://example.com"
agent-browser snapshot -i
agent-browser fill @e2 "Mein gespeicherter Prompt"
agent-browser press Enter
```

Das heißt: **„Gehe zu Seite X und setze Prompt Y in Feld Z ab“ ist ein ziemlich normaler OpenClaw-Use-Case.**

### 4. Für deine Anwendung würde ich aber einen eigenen kleinen Skill bauen

Statt einen generischen Browser-Agent jedes Mal neu überlegen zu lassen, was er tun soll, würde ich für wiederkehrende Prompts einen Skill etwa dieser Art bauen:

```text
skill: send-research-prompt

input:
  - topic

workflow:
  - use Chrome profile "chrome"
  - open/focus chatgpt.com
  - start new conversation
  - load prompt template "deep-research"
  - substitute {{topic}}
  - enter prompt
  - submit
  - wait until generation completes
  - extract response
  - return response
```

Dann wäre die Bedienung beispielsweise nur noch:

```text
/research "OpenClaw Browser Automation"
```

und der Skill setzt intern deinen vollständigen Prompt ab.

Das entspricht genau der vorgesehenen OpenClaw-Architektur: **Tool = Fähigkeit; Skill = reproduzierbarer Prozess.** ([OpenClaw](https://docs.openclaw.ai/tools "Overview - OpenClaw"))

### 5. Das lässt sich sogar zeitgesteuert ausführen

OpenClaw besitzt zusätzlich einen eingebauten Scheduler namens **Automations** (`openclaw automations`, früher/alternativ `cron`). Ein gespeicherter Agent-Prompt kann damit einmalig oder nach Cron-Zeitplan ausgeführt werden. ([OpenClaw](https://docs.openclaw.ai/cli/cron "Automations (cron) - OpenClaw"))

Damit wäre beispielsweise möglich:

```text
jeden Morgen 07:00
        ↓
Research-Skill starten
        ↓
Chrome → ChatGPT
        ↓
Prompt A senden
        ↓
Antwort speichern/verarbeiten
        ↓
Prompt B senden
        ↓
Resultat über Telegram senden
```

Das heißt, du könntest nicht nur manuell sagen „führe Prompt X aus“, sondern komplette **Prompt-Pipelines über Web-UIs automatisieren**.

### Meine Einschätzung für FusionAi2

Für deinen Anwendungsfall würde ich **nicht primär auf einen fremden ChatGPT-ClawHub-Skill setzen**. Die sauberste Architektur wäre:

```text
OpenClaw
├── offizielles browser plugin
├── offizielle Chrome Extension
│
└── eigener FusionAi2 Skill
    ├── Prompt Templates
    ├── Website/URL
    ├── Browser Workflow
    ├── Session-Regeln
    ├── Output Extraction
    └── optional Automations/Cron
```

Damit kontrollierst du selbst die Prompts und den Ablauf und bist nicht davon abhängig, wie ein Community-Skill gebaut wurde. Das ist besonders relevant, weil OpenClaw selbst ausdrücklich empfiehlt, **Third-Party-Skills als nicht vertrauenswürdigen Code zu behandeln und vor Aktivierung zu prüfen**; ClawHub bietet dafür inzwischen Verifikation und Security-Scans. ([OpenClaw](https://docs.openclaw.ai/tools/skills "Skills - OpenClaw"))

**Kurz: Ja – OpenClaw ist für genau diesen Typ „Browser als ausführende Oberfläche“-Automation bereits ziemlich gut aufgestellt.** Die entscheidende Komponente ist inzwischen sogar offiziell: Chrome Extension + `browser` Tool + `browser-automation` Skill. Für deine vordefinierten Prompt-Sequenzen würde man darauf einen sehr kleinen eigenen Skill setzen.