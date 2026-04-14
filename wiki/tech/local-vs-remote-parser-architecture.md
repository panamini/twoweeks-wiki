---
title: "Local vs Remote Parser Architecture"
category: tech
tags: [parser, local, remote, convex, run.sh, environment, production]
created: 2026-04-14
updated: 2026-04-14
status: current
valid_from: 2026-04-14
valid_until:
superseded_by:
horizon: present
version: v1
sources: [2026-04-14-local-dev-vs-remote-parser-architecture, 2026-04-14-run-sh-modes]
related: [[tech/import-ocr-pipeline]], [[howto/local-parser-operations]], [[entities/twoweeks]]
---

# Local vs Remote Parser Architecture

Référence technique pour distinguer le chemin local de debug du chemin cloud/public utilisé en preview et en production.

---

## Mode local complet

**Stack** : frontend local + Convex local + parser local

**Usage** :
- debug parser/OCR
- vérification du comportement Mistral sans bruit tunnel
- reproduction end-to-end locale

**Commande de référence** : `./run.sh up --ui --local-origin --local-convex`

---

## Mode cloud / preview / production

**Stack** : frontend hébergé ou local + Convex cloud + parser public

**Usage** :
- usage réel
- previews Vercel / frontends hébergés
- actions Convex cloud parlant à un serveur parser accessible publiquement

**Variable clé** : `CONVEX_PARSER_URL=https://your-parser.example.com`

---

## Garde-fou essentiel

La préférence localhost doit rester strictement dev-only. Elle peut être activée par un flag comme `STRUCTURED_UPLOAD_PREFER_LOOPBACK=1`, par le mode local Convex, ou par un flow repo local explicite. Elle ne doit jamais s'appliquer par défaut dans le cloud.

---

## Conséquence produit

Le passage du mode local au mode prod doit rester un changement d'environnement, pas un fork d'architecture. Le code doit donc rester compatible avec un parser public et avec une boucle locale complète.

---

## Voir aussi

- [[howto/local-parser-operations]] — commandes à lancer
- [[tech/import-ocr-pipeline]] — call path actif
