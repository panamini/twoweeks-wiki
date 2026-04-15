---
title: "Local vs Remote Parser Architecture"
category: tech
tags: [parser, local, remote, convex, run.sh, environment, production]
created: 2026-04-14
updated: 2026-04-15
status: current
valid_from: 2026-04-14
valid_until:
superseded_by:
horizon: present
version: v1
sources: [2026-04-14-local-dev-vs-remote-parser-architecture, 2026-04-14-run-sh-modes, 2026-04-14-run-sh-quick-note, 2026-04-15-run-sh-workspace-modes]
related: [[tech/import-ocr-pipeline]], [[howto/local-parser-operations]], [[entities/twoweeks]]
---

# Local vs Remote Parser Architecture

Référence technique pour distinguer le chemin local de debug du chemin cloud/public utilisé en preview et en production.

---

## Mode local full-stack recommandé

**Stack** : frontend local + Convex local + parser local workspace

**Usage** :
- travail local quotidien sur le parser
- import structuré end-to-end réellement local
- export avec runtime image préservé

**Commande de référence** : `./run.sh local-fast`

---

## Alias legacy

**Commande** : `./run.sh local-convex`

Doit être lu comme alias documentaire/transitoire de `local-fast`, pas comme un quatrième modèle mental distinct.

---

## Mode local partiel

**Stack** : frontend local + parser local, sans garantie d'alignement backend local complet

**Usage** :
- cas simples
- tests partiels UI/parser
- pas recommandé pour valider le structured upload complet

**Commande de référence** : `./run.sh local`

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

- [[howto/local-parser-operations]] — commandes à lancer
- [[tech/import-ocr-pipeline]] — call path actif
