# Documentation et audit de run.sh — 13.1 Priorité haute — Séparer clairement les modes développement et production.

Source: `audit/Documentation et audit de run.sh.md`

Paragraphe: 13.1 Priorité haute

Amélioration proposée: Séparer clairement les modes développement et production.

Le script contient aujourd'hui des comportements très utiles en local mais inappropriés en production, par exemple `workspace`, `--reload`, ouverture de navigateur, nettoyage agressif de ports et alias legacy.
	Etapes proposées:
	1. Ajouter une variable `RUN_ENV=dev|staging|prod`, avec `dev` par défaut.
	2. Interdire `workspace`, `parser-dev`, `local-fast`, `--parser-reload` et `OPEN_BROWSER=1` quand `RUN_ENV=prod`.
	3. Interdire `reset` en production sauf option explicite `--confirm-maintenance`.
	4. Remplacer les messages d'erreur par des explications courtes et actionnables.
	5. Ajouter `./run.sh doctor --env prod` pour vérifier que le mode prod respecte les contraintes.
	6. Documenter les commandes autorisées en production, par exemple `up`, `down`, `status`, `logs`, `smoke`, `reload-env` si valide.
