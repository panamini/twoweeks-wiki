# Documentation et audit de run.sh — 14.2 Améliorations d'idempotence proposées — Ajouter un mode de comparaison d'état avant/après.

Source: `audit/Documentation et audit de run.sh.md`

Paragraphe: 14.2 Améliorations d'idempotence proposées

Amélioration proposée: Ajouter un mode de comparaison d'état avant/après.

Etapes :
	1. Capturer l'état avant action: conteneurs, PID, ports, hashes de config.
	2. Exécuter l'action.
	3. Capturer l'état après action.
	4. Afficher les différences utiles.
	5. En mode test, échouer si une différence non attendue apparait.
