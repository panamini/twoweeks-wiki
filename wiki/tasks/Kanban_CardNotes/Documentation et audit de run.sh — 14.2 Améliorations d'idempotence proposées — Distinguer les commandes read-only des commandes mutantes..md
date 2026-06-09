# Documentation et audit de run.sh — 14.2 Améliorations d'idempotence proposées — Distinguer les commandes read-only des commandes mutantes.

Source: `audit/Documentation et audit de run.sh.md`

Paragraphe: 14.2 Améliorations d'idempotence proposées

Amélioration proposée: Distinguer les commandes read-only des commandes mutantes.

Commandes read-only attendues:
	- `help`;
	- `status`;
	- `logs`;
	- `smoke`;
	- `probe-edge` sauf POST de fichier.
	Commandes mutantes:
	- `up`;
	- `local-fast`;
	- `local`;
	- `tunnel`;
	- `parser-dev`;
	- `reload-env`;
	- `rebuild-docker`;
	- `down`;
	- `reset`;
	- `kill-vite-ports`.
	Etapes:
	1. Documenter cette classification dans `help`.
	2. Garantir que les commandes read-only n'écrivent pas dans `tmp/dev-stack`.
	3. Ajouter un test qui compare l'arborescence avant/après une commande read-only.
	4. En production, limiter les commandes mutantes autorisées.
