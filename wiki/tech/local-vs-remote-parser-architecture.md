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
sources: [2026-04-14-local-dev-vs-remote-parser-architecture, 2026-04-14-run-sh-modes, 2026-04-14-run-sh-quick-note]
related: [[tech/import-ocr-pipeline]], [[howto/local-parser-operations]], [[entities/twoweeks]]
---

# Local vs Remote Parser Architecture

Référence technique pour distinguer le chemin local de debug du chemin cloud/public utilisé en preview et en production.

---

## Mode local quotidien

**Stack** : frontend local + Convex cloud/default + parser local

**Usage** :
- travail local normal
- vérification rapide du parser/export sans tunnel
- boucle courte côté app + parser

**Commande de référence** : `./run.sh local`

---

## Mode local complet

**Stack** : frontend local + Convex local + parser local

**Usage** :
- debug parser/OCR end-to-end
- debug backend Convex local
- reproduction locale complète d'un flux structuré

**Commande de référence** : `./run.sh local-convex`

---

## Mode cloud / preview / production

**Stack** : frontend hébergé ou local + Convex cloud + parser public

**Usage** :
- usage réel
- previews Vercel / frontends hébergés
- actions Convex cloud parlant à un serveur parser accessible publiquement

**Variable clé** : `CONVEX_PARSER_URL=https://your-parser.example.com`

**Commande de référence côté dev** : `./run.sh tunnel`

---

## Garde-fou essentiel

La préférence localhost doit rester strictement dev-only. Elle peut être activée par un flag comme `STRUCTURED_UPLOAD_PREFER_LOOPBACK=1`, par le mode local Convex, ou par un flow repo local explicite. Elle ne doit jamais s'appliquer par défaut dans le cloud.

---

## Conséquence produit

Le passage du mode local au mode prod doit rester un changement d'environnement, pas un fork d'architecture. Le code doit donc rester compatible avec un parser public et avec une boucle locale complète.

---

## Voir aussi

- [[run.sh` LLM Scratchpad]] — commandes à lancer
- [[tech/import-ocr-pipeline]] — call path actif
