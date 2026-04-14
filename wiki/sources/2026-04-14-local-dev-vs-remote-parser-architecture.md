---
title: "Local Dev vs Remote Parser Architecture"
category: source
tags: [parser, architecture, local, production, convex, env, infrastructure]
created: 2026-04-14
updated: 2026-04-14
status: current
valid_from: 2026-04-14
valid_until:
superseded_by:
horizon: present
version: v1
type: spec
sources: []
related: [[tech/local-vs-remote-parser-architecture]], [[tech/import-ocr-pipeline]], [[entities/twoweeks]]
---

# Local Dev vs Remote Parser Architecture
**Type** : Note d'architecture d'environnement  
**Date** : 2026-04-14  
**URL** : source locale `rawinput/Local dev server vs Remote dev server Architecture.md`

## Résumé

Clarification de l'architecture cible entre dev local et production. Le mode local doit utiliser la boucle locale complète seulement dans un contexte explicitement dev ; tout environnement hébergé doit pointer vers une URL parser publique configurée par env.

## Points clés

1. **Local dev** : frontend local + Convex local + parser local pour déboguer le parsing sans bruit réseau/tunnel.
2. **Prod/preview/shared dev** : frontend hébergé + Convex cloud + parser public via `CONVEX_PARSER_URL`.
3. **Localhost ne doit jamais fuiter en prod** : la préférence loopback doit rester derrière une condition dev-only (`STRUCTURED_UPLOAD_PREFER_LOOPBACK=1` ou équivalent).
4. **Le retour en prod est un changement de config, pas un rewrite**.

## Implications pour twoweeks

- La documentation opératoire doit séparer clairement les modes local et hosted.
- Les décisions parser doivent rester compatibles avec un backend accessible publiquement en prod.
- Les bugs de parsing doivent être reproduits d'abord sur la boucle locale complète, puis validés sur le chemin cloud réel.

## Extraits notables

> "local dev = frontend local + Convex local + parser local"

> "production = frontend hosted + Convex cloud + parser public URL"

## Pages wiki mises à jour

- [[tech/local-vs-remote-parser-architecture]] — nouvelle référence technique
- [[tech/import-ocr-pipeline]] — précision des modes d'environnement
- [[timeline]] — clarification d'architecture datée
