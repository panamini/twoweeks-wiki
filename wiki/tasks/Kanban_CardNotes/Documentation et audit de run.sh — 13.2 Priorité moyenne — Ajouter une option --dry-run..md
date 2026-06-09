# Documentation et audit de run.sh — 13.2 Priorité moyenne — Ajouter une option `--dry-run`.

Source: `audit/Documentation et audit de run.sh.md`

Paragraphe: 13.2 Priorité moyenne

Amélioration proposée: Ajouter une option `--dry-run`.

Elle permettrait de comprendre ce que le script va lancer ou tuer sans exécuter les actions. C'est utile pour les novices et pour les revues.
	Etapes proposées:
	1. Ajouter une variable globale `DRY_RUN=0`.
	2. Ajouter un helper `run_cmd` qui affiche puis exécute une commande.
	3. Si `DRY_RUN=1`, `run_cmd` affiche seulement l'action.
	4. Remplacer progressivement les appels sensibles par `run_cmd`.
	5. Commencer par Docker, kill, rm et build.
	6. Ajouter `./run.sh up --dry-run` et `./run.sh reset --dry-run`.
	7. Vérifier que `--dry-run` ne modifie aucun fichier d'état.
