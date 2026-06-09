# Documentation et audit de run.sh — 13.2 Priorité moyenne — Modulariser le script.

Source: `audit/Documentation et audit de run.sh.md`

Paragraphe: 13.2 Priorité moyenne

Amélioration proposée: Modulariser le script.

Oui, il est envisageable et recommandé de modulariser `run.sh`, surtout si l'objectif est une exploitation production.
	Aujourd'hui, le script fait 1677 lignes et contient plusieurs responsabilités:
	- chargement de configuration;
	- fonctions utilitaires;
	- build Docker;
	- orchestration parser;
	- orchestration Convex;
	- orchestration Vite;
	- orchestration tunnel;
	- gestion de l'état;
	- logs;
	- diagnostics;
	- nettoyage;
	- dispatch des commandes.
	Ces responsabilités peuvent rester en Bash, mais elles devraient être séparées en fichiers plus courts.
	Structure cible possible:
	```text
	scripts/run/
	main.sh # point d'entree et dispatch des commandes
	config.sh # chargement et validation de configuration
	logging.sh # fonctions de logs
	state.sh # lecture/ecriture de pids.env
	docker.sh # build image, buildx, image id
	parser.sh # start/stop/status parser
	convex.sh # start/stop/status Convex local
	vite.sh # start/stop/status Vite
	tunnel.sh # start/stop/status cloudflared
	checks.sh # prechecks, postchecks, doctor
	cleanup.sh # down/reset/maintenance
	```
	Le fichier `run.sh` racine peut rester comme wrapper stable:
	```bash
	#!/usr/bin/env bash
	set -euo pipefail
	source "$(dirname "${BASH_SOURCE[0]}")/scripts/run/main.sh"
	main "$@"
	```
	Avantages:
	- lecture plus simple pour un nouveau contributeur;
	- tests plus faciles, car chaque module a une responsabilité claire;
	- risque réduit de casser Convex en modifiant Docker, ou Vite en modifiant le tunnel;
	- réutilisation possible de fonctions communes comme logs, checks et état;
	- meilleure séparation entre développement et production;
	- meilleure revue de code, car les diffs sont plus petits;
	- possibilité de remplacer progressivement certaines parties par des scripts plus robustes sans tout réécrire.
	Etapes proposées:
	1. Ne pas tout découper en une seule fois.
	2. Extraire d'abord `logging.sh`, car il a peu de dépendances.
	3. Extraire ensuite `state.sh`, car la lecture/écriture d'état est centrale.
	4. Extraire `config.sh`, avec validation et affichage redacted.
	5. Extraire `checks.sh`, pour préparer l'idempotence.
	6. Extraire les modules service par service: parser, Vite, Convex, tunnel.
	7. Garder `run.sh` compatible avec les commandes actuelles.
	8. Apres chaque extraction, exécuter `bash -n` et un test de non-regression sur `help`, `status`, puis un mode de démarrage.
	9. Documenter le contrat de chaque module en haut du fichier.
	10. Eviter les dépendances circulaires: les modules service peuvent utiliser `logging`, `state`, `config`, `checks`, mais pas l'inverse.
