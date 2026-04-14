---
title: "Docker Commands — Local Parser"
category: source
tags: [docker, parser, local, restart, runbook]
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

# Docker Commands — Local Parser
**Type** : Note opératoire  
**Date** : 2026-04-14  
**URL** : source locale `rawinput/Docker commands.md`

## Résumé

Rappel minimal : pour redémarrer le conteneur parser de dev, utiliser `docker restart cv-parser-service-dev`.

## Points clés

1. Le nom du conteneur local de référence est `cv-parser-service-dev`.
2. Le redémarrage suffit pour la plupart des incidents de dev parser sans relancer toute la stack.

## Implications pour twoweeks

- Cette commande doit vivre dans un howto court dédié aux opérations locales du parser.
- Réduit le coût de reprise pendant le débogage OCR/parsing.

## Pages wiki mises à jour

- [[howto/local-parser-operations]] — commande ajoutée
