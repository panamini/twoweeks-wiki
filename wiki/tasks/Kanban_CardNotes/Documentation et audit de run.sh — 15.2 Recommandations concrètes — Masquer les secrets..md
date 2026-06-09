# Documentation et audit de run.sh — 15.2 Recommandations concrètes — Masquer les secrets.

Source: `audit/Documentation et audit de run.sh.md`

Paragraphe: 15.2 Recommandations concrètes

Amélioration proposée: Masquer les secrets.

Toute valeur de variable contenant `KEY`, `SECRET`, `TOKEN`, `PASSWORD` ou `PRIVATE` doit être masquée dans les logs.
	Exemple:
	```text
	MISTRAL_API_KEY=***
	TUNNEL_TOKEN=***
	```
