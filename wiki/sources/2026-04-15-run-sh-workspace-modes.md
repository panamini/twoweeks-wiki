---
title: "run.sh Workspace Modes — Local Fast and Parser Dev"
category: source
tags: [runbook, parser, local, convex, run.sh, workspace]
created: 2026-04-15
updated: 2026-04-15
status: current
valid_from: 2026-04-15
valid_until:
superseded_by:
horizon: present
version: v1
type: runbook
sources: []
related: [[howto/local-parser-operations]], [[tech/local-vs-remote-parser-architecture]], [[tech/import-ocr-pipeline]], [[entities/twoweeks]]
---

# run.sh Workspace Modes — Local Fast and Parser Dev
**Type** : Runbook
**Date** : 2026-04-15
**URL** : source locale `rawinput/run.sh\` LLM Scratchpad.md`

## Résumé

Cette note remplace la description trop courte des modes `run.sh` par un modèle opératoire plus précis : `tunnel` pour validation stable, `local-fast` pour le vrai développement parser full-stack, `parser-dev` pour hacking parser-only, et `rebuild-docker` quand le runtime image doit être régénéré.

## Points clés

1. `./run.sh local-fast` est le mode recommandé pour le développement parser full-app : parser workspace + autoreload, Convex local, Vite, structured upload local et export attendu fonctionnel.
2. `./run.sh local-convex` doit être traité comme alias legacy de `local-fast`, pas comme un mode conceptuellement distinct.
3. `./run.sh local` ne représente plus le chemin local complet recommandé pour le structured upload end-to-end.
4. Le runtime workspace doit préserver les dépendances Linux installées dans l'image via des volumes `node_modules`; sinon l'export casse par mismatch de plateforme.
5. `./run.sh rebuild-docker`, `./run.sh reset`, `./run.sh status` et `./run.sh logs` forment le kit opératoire minimal de diagnostic local.

## Implications pour twoweeks

- La doc active doit promouvoir `local-fast` comme boucle principale de dev parser, avec `tunnel` pour la validation edge.
- Les pages techniques doivent décrire explicitement le boundary "browser local vs local Convex vs parser local" pour éviter les faux positifs où l'UI est locale mais l'import route encore vers le cloud.
- Les anciens liens howto cassés autour de `run.sh` doivent être remplacés par une vraie page howto active.

## Extraits notables

- "`local-fast` fixes that by aligning all three layers."
- "`local-convex` - legacy alias for `local-fast`."
- "`tunnel` = stable validation mode"

## Pages wiki mises à jour

- [[howto/local-parser-operations]]
- [[tech/local-vs-remote-parser-architecture]]
- [[tech/import-ocr-pipeline]]
- [[entities/twoweeks]]
