---
title: "Local Parser Operations"
category: howto
tags: [parser, local, docker, run.sh, convex, debug]
created: 2026-04-14
updated: 2026-04-14
status: current
valid_from: 2026-04-14
valid_until:
superseded_by:
horizon: present
version: v1
sources: [2026-04-14-run-sh-modes, 2026-04-14-docker-commands]
related: [[tech/local-vs-remote-parser-architecture]], [[tech/import-ocr-pipeline]]
---

# Local Parser Operations

Runbook court pour lancer, arrêter et redémarrer la stack parser locale selon l'objectif de debug.

---

## Dev normal

UI locale avec chemin cloud/tunnel par défaut :

```bash
./run.sh up --ui
```

À utiliser pour le comportement app habituel quand le parser edge et Convex cloud sont la référence.

---

## Debug parser local end-to-end

Boucle locale complète :

```bash
./run.sh up --ui --local-origin --local-convex
```

À utiliser pour :
- diagnostiquer OCR/parsing
- vérifier le chemin `structured upload`
- éviter le bruit Cloudflare/tunnel

---

## Forcer explicitement le chemin edge

```bash
./run.sh up --ui --edge-origin
```

---

## Arrêter la stack

```bash
./run.sh down
```

---

## Redémarrer le conteneur parser

```bash
docker restart cv-parser-service-dev
```

---

## Important

`./run.sh up --ui --local-origin` seul ne suffit pas pour un vrai debug parser end-to-end si Convex reste sur le backend cloud/default.
