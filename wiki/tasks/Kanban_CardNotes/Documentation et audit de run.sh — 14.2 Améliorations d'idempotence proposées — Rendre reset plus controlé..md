# Documentation et audit de run.sh — 14.2 Améliorations d'idempotence proposées — Rendre `reset` plus controlé.

Source: `audit/Documentation et audit de run.sh.md`

Paragraphe: 14.2 Améliorations d'idempotence proposées

Amélioration proposée: Rendre `reset` plus controlé.

Etapes:
	1. Ajouter un précheck qui liste ce que `reset` va supprimer ou tuer.
	2. En mode interactif, demander confirmation.
	3. En CI ou production, exiger `--yes` ou `--confirm-maintenance`.
	4. Tuer seulement les ressources appartenant au projet.
	5. Produire un résumé final: supprimé, déjà absent, échec.
