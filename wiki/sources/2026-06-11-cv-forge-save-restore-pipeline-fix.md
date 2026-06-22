---
title: "CV Forge Save / Restore Pipeline Fix"
category: source
tags: [cv-forge, persistence, bug-fix]
created: 2026-06-11
updated: 2026-06-11
status: current
type: scratchpad
related: [[tech/live-resume-preview-runtime]], [[tech/repo-testing-system]]
---

# CV Forge Save / Restore Pipeline Fix

**Type** : Bug-fix evidence and implementation note
**Date** : 2026-06-07
**URL** : source locale `raw/CV Forge Save Restore Pipeline Fix.md`

## Résumé

Capture de la correction de persistance CV où la visibilité UI sortait incohérente après imports, changements de CV et rafraîchissement.

## Points clés

- Les invariants corrigés couvrent la présence du CV courant dans le drawer, la création/import route alignment, et le chargement immédiat d’un CV cible.
- Le bug principal était une coordination entre `routeId`, `currentId`, `cvDocuments`, cache complet `cv:<id>` et sauvegarde asynchrone sortante.
- `buildWorkLibraryModel` intègre maintenant `currentCv` même quand la liste compacte reste en retard.
- Le chemin d’import aligne `/cv?id=<id>` pendant la période de save pending.
- `loadCv` démarre la sauvegarde sortante en arrière-plan puis charge immédiatement la cible.
- `performSave` ne met plus `lastSavedRef` à jour si le save ne concerne plus le CV actif.

## Vérifications

- Invariants de cas utilisateur documentés: création + rafraîchissement, import de PDF + rafraîchissement, clic Drawer + rafraîchissement.
- Tests ciblés passés sur `CvLibraryContext`, `CvForge.workspace-mode`, `application-library` et rails d’interface.

## Touched pages

- none
