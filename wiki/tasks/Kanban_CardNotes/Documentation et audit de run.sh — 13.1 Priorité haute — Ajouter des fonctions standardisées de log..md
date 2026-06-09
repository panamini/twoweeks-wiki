# Documentation et audit de run.sh — 13.1 Priorité haute — Ajouter des fonctions standardisées de log.

Source: `audit/Documentation et audit de run.sh.md`

Paragraphe: 13.1 Priorité haute

Amélioration proposée: Ajouter des fonctions standardisées de log.

Exemple:
	```bash
	log_info() { printf '[run][INFO] %s\n' "$*"; }
	
	log_warn() { printf '[run][WARN] %s\n' "$*" >&2; }
	
	log_error() { printf '[run][ERROR] %s\n' "$*" >&2; }
	```
	Cela rendrait les messages homogènes et faciles à filtrer.
	Etapes proposées:
	1. Ajouter `timestamp`, `log_info`, `log_warn`, `log_error`, `log_debug`.
	2. Ajouter `RUN_LOG_FILE="${LOG_DIR}/run-dev-stack.log"`.
	3. Faire écrire les logs à la fois sur la sortie standard et dans ce fichier.
	4. Remplacer progressivement les `echo "[run] ..."` par ces fonctions.
	5. Ajouter `LOG_LEVEL=info` par défaut.
	6. Vérifier qu'une erreur critique apparait bien dans la console et dans le fichier principal.
