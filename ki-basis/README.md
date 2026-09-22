# KI-Basis (Private Stack)

Independent Private configuration for the existing `ki-basis` Docker project. Persistent application data stays in its existing Docker volumes.

Start: `.\scripts\start-ki-basis.ps1` (Docker Desktop must be running).  
Stop: `.\scripts\stop-ki-basis.ps1` (leaves Community and Docker Desktop running).  
Hermes: `.\scripts\invoke-hermes.ps1 -Prompt "Your request"`.  

| Application | Local URL |
|---|---|
| Entry page | http://127.0.0.1:8084 |
| Paperless | http://127.0.0.1:8010 |
| OpenProject | http://127.0.0.1:8082 |
| Firefly III | http://127.0.0.1:8086 |
| Hermes dashboard | http://127.0.0.1:9119 |
| Hermes API | http://127.0.0.1:8642 |

Local credentials belong in ignored `.env.private`. The persona is in `SOUL.md` (`ExecutivePartner`); developer instructions are in `AGENTS.md`. Telegram is strictly disabled.
