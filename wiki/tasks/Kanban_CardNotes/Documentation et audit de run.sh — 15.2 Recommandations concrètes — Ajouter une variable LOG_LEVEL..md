# Documentation et audit de run.sh — 15.2 Recommandations concrètes — Ajouter une variable `LOG_LEVEL`.

Source: `audit/Documentation et audit de run.sh.md`

Paragraphe: 15.2 Recommandations concrètes

Amélioration proposée: Ajouter une variable `LOG_LEVEL`.

Exemple:
	```bash
	LOG_LEVEL=debug ./run.sh local-fast
	```
	Niveaux possibles:
	- `error`;
	- `warn`;
	- `info`;
	- `debug`.
