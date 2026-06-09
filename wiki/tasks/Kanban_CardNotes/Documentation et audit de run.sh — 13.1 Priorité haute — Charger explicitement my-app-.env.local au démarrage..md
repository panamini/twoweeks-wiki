# Documentation et audit de run.sh — 13.1 Priorité haute — Charger explicitement `my-app/.env.local` au démarrage.

Source: `audit/Documentation et audit de run.sh.md`

Paragraphe: 13.1 Priorité haute

Amélioration proposée: Charger explicitement `my-app/.env.local` au démarrage.

Le script l'utilise déjà pour les hashes et la résolution Convex. Le sourcer rendrait le comportement plus cohérent.
	Etapes proposées:
	1. Ajouter `my-app/.env.local` dans le bloc de chargement initial.
	2. Définir l'ordre de priorite attendu: fichier global, fichier local, fichier app, fichier app local.
	3. Documenter cet ordre dans l'aide.
	4. Ajouter une commande `config-print --redacted` pour afficher les valeurs effectives sans secrets.
	5. Vérifier avant/après avec une variable non sensible définie uniquement dans `my-app/.env.local`.
