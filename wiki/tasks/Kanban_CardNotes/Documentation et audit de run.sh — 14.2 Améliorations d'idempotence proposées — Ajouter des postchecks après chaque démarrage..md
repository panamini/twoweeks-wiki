# Documentation et audit de run.sh — 14.2 Améliorations d'idempotence proposées — Ajouter des postchecks après chaque démarrage.

Source: `audit/Documentation et audit de run.sh.md`

Paragraphe: 14.2 Améliorations d'idempotence proposées

Amélioration proposée: Ajouter des postchecks après chaque démarrage.

Etapes:
	1. Apres Docker parser: vérifier `/ready`, nom du conteneur, image, port.
	2. Apres Convex: vérifier `/instance_name` et URL attendue.
	3. Apres Vite: vérifier que le PID existe et que le port répond.
	4. Apres tunnel: vérifier que le conteneur tourne et que l'edge `/ready` répond si accessible.
	5. Apres `reload-env`: vérifier que les nouveaux hashes sont écrits dans l'état.
