# Documentation et audit de run.sh — 13.2 Priorité moyenne — Ajouter une commande `doctor`.

Source: `audit/Documentation et audit de run.sh.md`

Paragraphe: 13.2 Priorité moyenne

Amélioration proposée: Ajouter une commande `doctor`.

Elle pourrait vérifier:
	- Docker disponible;
	- Buildx disponible;
	- Node disponible;
	- `my-app/node_modules` présent;
	- Convex CLI présent;
	- `jq`, `curl`, `lsof`, `pgrep` disponibles;
	- ports attendus disponibles;
	- fichiers `.env` essentiels présents.
	Etapes proposées:
	1. Créer une fonction `doctor`.
	2. Ajouter des checks indépendants, chacun avec un nom clair.
	3. Pour chaque check, afficher `OK`, `WARN` ou `FAIL`.
	4. Retourner un code non nul si au moins un check critique est en échec.
	5. Ajouter `doctor --env dev`, `doctor --env staging`, `doctor --env prod`.
	6. Ajouter `doctor --json` pour une intégration CI/CD.
