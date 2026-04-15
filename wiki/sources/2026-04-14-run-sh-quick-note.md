---
title: "run.sh Quick Note — Main Dev Entrypoint"
category: source
tags: [runbook, parser, local, convex, run.sh, dev, entrypoint]
created: 2026-04-14
updated: 2026-04-14
status: current
valid_from: 2026-04-14
valid_until:
superseded_by:
horizon: present
version: v1
type: runbook
sources: []
related: [[APP-launcher-command]], [[tech/local-vs-remote-parser-architecture]], [[tech/import-ocr-pipeline]], [[entities/twoweeks]]
---

# run.sh Quick Note — Main Dev Entrypoint
**Type** : Note opératoire
**Date** : 2026-04-14
**URL** : source locale `rawinput/RUN.SH QUICK NOTE.md`

## Résumé

Cette note fixe `run.sh` comme point d'entrée principal du stack de dev. Elle remplace les longues variantes `up --ui ...` comme langage opérationnel courant par un petit ensemble de commandes courtes : `local`, `local-convex`, `tunnel`, `down`, `reset`, `status`, `logs`, et éventuellement `build-parser`.

## Points clés

1. `./run.sh local` devient le workflow quotidien recommandé : parser local, frontend pointé sur `http://127.0.0.1:8001`, Convex online/default, runtime parser export-capable.
2. `./run.sh local-convex` est un mode avancé réservé au debug backend Convex local.
3. `./run.sh tunnel` devient le raccourci nominal pour le workflow tunnel/edge historique via `PARSER_ORIGIN` / `https://parser.dasti.ai`.
4. `./run.sh down` et `./run.sh reset` sont explicitement non destructifs : arrêt normal puis cleanup de reprise, sans suppression d'images Docker ni de `node_modules`.
5. Les anti-patterns documentés incluent : rebuild parser à chaque boot, workspace mount par défaut, export depuis le preview DOM, et dépendance à de longues commandes `up --ui --local-origin --local-convex`.

## Implications pour twoweeks

- La documentation active doit parler d'abord en termes de `./run.sh local`, `./run.sh local-convex` et `./run.sh tunnel`.
- Les longues variantes `up --ui ...` restent une couche d'implémentation du script, pas l'interface opérateur recommandée.
- `run.sh` doit être traité comme la source de vérité opérationnelle pour le lancement local, le tunnel, l'arrêt et la remise à zéro.

## Extraits notables

- "`run.sh` is the main dev entrypoint for the app stack."
- "should replace long boot commands and make normal startup simple"
- "needing long commands like `--ui --local-origin --local-convex` for normal usage"

## Pages wiki mises à jour

- [[run.sh` LLM Scratchpad]]
- [[tech/local-vs-remote-parser-architecture]]
- [[tech/import-ocr-pipeline]]
- [[entities/twoweeks]]
