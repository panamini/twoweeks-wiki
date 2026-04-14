
---
title: "Local Parser Operations"
category: howto
tags: [run.sh, parser, local, convex, tunnel, devops]
created: 2026-04-14
updated: 2026-04-14
status: current
valid_from: 2026-04-14
valid_until:
superseded_by:
horizon: present
version: v1
sources: [2026-04-14-run-sh-modes, 2026-04-14-run-sh-quick-note, 2026-04-14-docker-commands]
related: [[tech/local-vs-remote-parser-architecture]], [[tech/import-ocr-pipeline]], [[entities/twoweeks]]
---

# Local Parser Operations

`run.sh` est le point d'entrée opérateur du stack de dev. Les commandes courtes `local`, `local-convex` et `tunnel` sont la référence documentaire ; les variantes longues `up --ui ...` restent des détails d'implémentation du script.

## Commandes de référence

```bash
./run.sh local
./run.sh local-convex
./run.sh tunnel
./run.sh down
./run.sh reset
./run.sh status
./run.sh logs
./run.sh build-parser
```

## Signification des modes

### `./run.sh local`

- workflow quotidien recommandé
- démarre Vite
- démarre le parser local en runtime image export-capable
- pointe le frontend sur `http://127.0.0.1:8001`
- garde Convex sur le déploiement online/default
- ne doit pas utiliser le workspace mount parser par défaut

### `./run.sh local-convex`

- même base que `local`
- démarre aussi Convex local
- mode avancé réservé au debug backend Convex

### `./run.sh tunnel`

- workflow edge/tunnel historique
- démarre Vite
- pointe le frontend sur `PARSER_ORIGIN` (`https://parser.dasti.ai` par défaut)
- démarre `cloudflared` si nécessaire
- garde Convex sur le déploiement online/default sauf changement explicite

## Commandes de cycle de vie

### `./run.sh down`

- arrêt normal
- stoppe Vite
- stoppe Convex local si `run.sh` l'a lancé
- stoppe le parser si `run.sh` l'a lancé
- stoppe `cloudflared` si le mode tunnel l'a lancé
- conserve images, caches et état du repo

### `./run.sh reset`

- cleanup de reprise, non destructif
- fait ce que `down` fait déjà
- supprime les conteneurs parser/cloudflared obsolètes
- tue les processus Vite/Convex résiduels
- nettoie `tmp/dev-stack` et les logs temporaires
- ne supprime ni images Docker, ni `node_modules`

### `./run.sh status`

Affiche rapidement :

- statut parser
- origine parser active
- statut Vite
- mode Convex
- statut tunnel si pertinent

### `./run.sh logs`

Affiche rapidement les logs parser.

### `./run.sh build-parser`

Chemin de rebuild explicite. `local` et `tunnel` ne doivent pas rebuild l'image parser à chaque lancement.

## Modèle mental

- **parser** = OCR / export / file-processing service
- **Convex** = backend applicatif / database / actions
- `local-convex` = besoin ponctuel de debug backend local, pas le workflow quotidien

## Règles runtime importantes

- Le boot normal doit rester rapide.
- `local` et `tunnel` utilisent le runtime image export-capable par défaut.
- Le workspace mount parser doit rester explicite uniquement.
- La source de vérité export reste la donnée normalisée, pas le preview DOM.

## Vérification rapide

Le script source de vérité actuel supporte bien :

- `./run.sh local`
- `./run.sh local-convex`
- `./run.sh tunnel`
- `./run.sh down`
- `./run.sh reset`
- `./run.sh status`
- `./run.sh logs`

Voir aussi : [[tech/local-vs-remote-parser-architecture]], [[tech/import-ocr-pipeline]]
