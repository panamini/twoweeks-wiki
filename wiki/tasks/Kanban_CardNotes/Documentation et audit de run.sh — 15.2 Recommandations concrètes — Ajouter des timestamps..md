# Documentation et audit de run.sh — 15.2 Recommandations concrètes — Ajouter des timestamps.

Source: `audit/Documentation et audit de run.sh.md`

Paragraphe: 15.2 Recommandations concrètes

Amélioration proposée: Ajouter des timestamps.

Format recommandé:
	```text
	2026-06-08T15:42:10+02:00 [run][INFO] starting parser
	```
	En Bash:
	```bash
	timestamp() { date '+%Y-%m-%dT%H:%M:%S%z'; }
	```
