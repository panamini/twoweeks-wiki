# Documentation et audit de run.sh — 13.1 Priorité haute — Ajouter une commande `logs-all`.

Source: `audit/Documentation et audit de run.sh.md`

Paragraphe: 13.1 Priorité haute

Amélioration proposée: Ajouter une commande `logs-all`.

Elle pourrait afficher ou suivre:
	- logs parser Docker;
	- `tmp/vite-dev.log`;
	- `tmp/convex-dev.log`;
	- derniers messages d'état `run.sh`.
	Etapes proposées:
	1. Créer une commande `logs all`.
	2. Créer aussi `logs parser`, `logs vite`, `logs convex`, `logs run`.
	3. Pour chaque source, afficher clairement son origine avant les lignes de logs.
	4. Ajouter une option `--tail N`.
	5. Ajouter une option `--follow`.
	6. Masquer les secrets au moment de l'affichage si le log principal peut contenir de la configuration.
