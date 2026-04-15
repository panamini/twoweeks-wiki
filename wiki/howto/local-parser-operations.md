---
title: "Local Parser Operations"
category: howto
tags: [parser, local, convex, run.sh, workspace, export]
created: 2026-04-15
updated: 2026-04-15
status: current
valid_from: 2026-04-15
valid_until:
superseded_by:
horizon: present
version: v1
sources: [2026-04-14-run-sh-quick-note, 2026-04-15-run-sh-workspace-modes]
related: [[tech/local-vs-remote-parser-architecture]], [[tech/import-ocr-pipeline]], [[entities/twoweeks]]
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

## Voir aussi

- [[tech/local-vs-remote-parser-architecture]]
- [[tech/import-ocr-pipeline]]
- [[entities/twoweeks]]
