# Documentation et audit de run.sh — 14.2 Améliorations d'idempotence proposées — Rendre `down` totalement idempotent.

Source: `audit/Documentation et audit de run.sh.md`

Paragraphe: 14.2 Améliorations d'idempotence proposées

Amélioration proposée: Rendre `down` totalement idempotent.

Etapes:
	1. Si le fichier d'état est absent, afficher `nothing to stop`.
	2. Pour chaque PID lu, vérifier qu'il existe encore.
	3. Si le PID n'existe plus, ne pas échouer.
	4. Pour chaque conteneur, vérifier son existence avant stop.
	5. Supprimer le fichier d'état seulement après les stops.
	6. Relancer `down` doit retourner `0`.
