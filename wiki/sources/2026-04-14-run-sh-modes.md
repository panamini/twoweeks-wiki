---
title: "run.sh — Local/Cloud Modes"
category: source
tags: [runbook, parser, local, convex, run.sh, dev]
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
related: [[howto/local-parser-operations]], [[tech/local-vs-remote-parser-architecture]]
---

# run.sh — Local/Cloud Modes
**Type** : Runbook de lancement local  
**Date** : 2026-04-14  
**URL** : source locale `rawinput/run.sh launching commands for the app.md`

## Résumé

Documente les différents modes de `./run.sh up --ui` selon que l'on veut rester sur le chemin cloud/tunnel, forcer une origine parser locale côté browser, ou lancer la boucle locale complète avec Convex local.

## Points clés

1. `./run.sh up --ui` = UI locale, mais Convex cloud/default et parser edge/tunnel par défaut.
2. `./run.sh up --ui --local-origin` = origine parser locale côté browser seulement ; insuffisant pour déboguer un upload structuré end-to-end.
3. `./run.sh up --ui --local-origin --local-convex` = vraie stack locale complète pour OCR/parser.
4. `./run.sh up --ui --edge-origin` = reproduction explicite du chemin edge.
5. `./run.sh down` = arrêt global.

## Implications pour twoweeks

- Il faut un howto minimal pour distinguer "dev normal" de "debug parser local".
- Les tests manuels de parsing doivent utiliser la commande full local stack, pas seulement `--local-origin`.

## Pages wiki mises à jour

- [[APP-launcher-command]] — nouvelle page howto
- [[tech/local-vs-remote-parser-architecture]] — lien entre modes de lancement et architecture cible
