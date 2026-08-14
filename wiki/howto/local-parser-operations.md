---
title: "Local Parser Operations"
category: howto
tags: [parser, local, convex, infisical, run.sh, workspace, export]
created: 2026-04-15
updated: 2026-08-12
status: current
valid_from: 2026-04-15
version: v1
sources: [2026-04-14-run-sh-quick-note, 2026-04-15-run-sh-workspace-modes]
related: [[tech/local-vs-remote-parser-architecture]], [[tech/import-ocr-pipeline]], [[howto/chatgpt-mcp-private-beta-tunnel-connector]], [[entities/twoweeks]]
---

# Local Parser Operations

Howto opératoire pour lancer et diagnostiquer la stack parser locale sans retomber sur les anciennes longues commandes `up --ui ...`.

## Modes de référence

- `./run.sh tunnel` : validation stable sur le path edge/public.
- `./run.sh local-fast` : développement parser full-stack recommandé.
- `./run.sh parser-dev` : parser-only avec autoreload.
- `./run.sh rebuild-docker` : reconstruire le runtime image export-capable.
- `./run.sh reset` : nettoyage de reprise si Convex/Vite sont incohérents.
- `./run.sh status` : état rapide des services.
- `./run.sh logs` : suivi des logs parser.

## Quand utiliser quel mode

- Si tu modifies le parser Python et veux que l'app réelle l'utilise, lance `./run.sh local-fast`.
- Si tu veux valider le chemin production-like, lance `./run.sh tunnel`.
- Si tu modifies les dépendances runtime/export ou le Dockerfile, lance `./run.sh rebuild-docker` avant de faire confiance à `local-fast`.
- Si l'UI est locale mais que l'import continue de router vers le cloud, vérifie que tu n'es pas resté en `local` et passe en `local-fast`.

## Détails runtime importants

- `local-fast` aligne les trois couches : parser local, frontend local, Convex local.
- Le mode workspace doit préserver les dépendances Linux embarquées via des volumes `node_modules`, sinon l'export casse.
- `local-convex` doit être lu comme alias legacy de `local-fast`.

## Bindings Convex dans Infisical

La source partagée est le projet Infisical `twoweeks`, environnement `dev`, chemin CLI `/twoweeks`. Les noms disponibles sont `CONVEX_TEAM`, `CONVEX_PROJECT`, `CONVEX_DEPLOYMENT`, `CONVEX_URL`, `CONVEX_AUTH_TOKEN` et `CONVEX_DEPLOY_KEY`; aucune valeur ne doit être copiée dans le wiki.

Pour `local-fast`, le binding requis est `CONVEX_TEAM` + `CONVEX_PROJECT`; `CONVEX_DEPLOYMENT` est optionnel pour réutiliser un déploiement local nommé. Le `run.sh` actif lit ces bindings depuis l'environnement ou les fichiers dotenv locaux, mais `./run.sh bootstrap` ne les matérialise pas automatiquement depuis Infisical : il récupère aujourd'hui uniquement la configuration Clerk nécessaire au frontend.

`CONVEX_DEPLOY_KEY` est un credential de déploiement cloud et n'est pas le binding local : `local-fast` l'unset avant de démarrer Convex local. `CONVEX_AUTH_TOKEN` est un credential serveur pour le runtime local autorisé; il ne doit pas être remplacé par un JWT navigateur, un token Clerk ou un token personnel de CLI Convex.

## Proxy OpenAI pour les agents locaux

Le service Agent Proxy d'Infisical expose `OPENAI_API_KEY_INFISICAL` comme placeholder au processus qu'il lance, puis remplace ce placeholder sur le trafic destiné à OpenAI par le secret source `OPENAI_API_KEY`. Il ne faut ni lire, ni copier, ni exporter la valeur source. `MISTRAL_API_KEY` reste un secret et un chemin provider séparés.

La connexion locale recommandée est une session utilisateur stockée dans le trousseau macOS :

```sh
infisical login --domain=https://eu.infisical.com --silent
infisical login status
```

Une session navigateur Infisical ne suffit pas : le CLI doit être connecté séparément. La session CLI persiste dans le trousseau jusqu'à son expiration; elle évite un `INFISICAL_TOKEN` copié dans le shell, mais un environnement sandboxé doit encore être autorisé à consulter le trousseau.

Depuis un checkout lié au projet `twoweeks`, lancer un agent derrière le proxy avec :

```sh
infisical secrets agent-proxy run --silent --env=dev --path=/twoweeks -- codex
```

Le 2026-08-12, le contrat a été vérifié sans afficher de valeur : le placeholder était présent dans le processus proxifié et un `GET https://api.openai.com/v1/models` authentifié via ce placeholder a retourné HTTP 200. Ce proxy concerne uniquement les processus lancés par `agent-proxy run`; il n'est pas le mécanisme d'authentification interne de Codex Desktop et il ne fournit pas automatiquement les bindings Convex ou Clerk à un processus ordinaire.

Pour une automatisation totalement non interactive au-delà de l'expiration de la session utilisateur, utiliser ultérieurement une machine identity Infisical à droits minimaux. Ne jamais stocker un token longue durée dans le repo; cette création reste une décision d'accès séparée.

## Voir aussi

- [[tech/local-vs-remote-parser-architecture]]
- [[tech/import-ocr-pipeline]]
- [[howto/chatgpt-mcp-private-beta-tunnel-connector]]
- [[entities/twoweeks]]
