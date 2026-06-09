# Documentation et audit de run.sh — 14.2 Améliorations d'idempotence proposées — Formaliser une fonction `ensure_*` par ressource.

Source: `audit/Documentation et audit de run.sh.md`

Paragraphe: 14.2 Améliorations d'idempotence proposées

Amélioration proposée: Formaliser une fonction `ensure_*` par ressource.

Exemples:
	- `ensure_network`;
	- `ensure_runtime_image`;
	- `ensure_parser_running`;
	- `ensure_tunnel_running`;
	- `ensure_vite_running`;
	- `ensure_convex_running`;
	- `ensure_state_file`.
	Etapes:
	1. Pour chaque ressource, créer une fonction qui observe d'abord l'état.
	2. Si l'état est conforme, afficher `already ok` et retourner `0`.
	3. Si l'état est absent, créer la ressource.
	4. Si l'état est incompatible, remplacer uniquement la ressource concernée.
	5. Vérifier l'état final.
	6. Retourner une erreur claire si le postcheck échoue.
