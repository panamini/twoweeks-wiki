---
title: "CV Hydration and Style System"
category: source
tags: [cv-forge, persistence, style, decoration]
created: 2026-06-11
updated: 2026-06-11
status: current
type: analysis
---

# CV Hydration and Style System

**Type** : Technical source note
**Date** : 2026-06-11
**URL** : source locale `raw/cv persistence .md`

## Résumé

Note de frontière d’intégrité CV autour de la décoration et de la synchronisation style.

## Points clés

- La restauration de décoration après refresh dépend de trois couches: `profilesPublic.getByProfileId`, `StorageAdapter.mapPersistedProfileToCvDocument`, et overlay runtime dans `CvLibraryContext`.
- Le renderer doit consommer `documentDecoration.resolvedUrl`; l’`assetId` seul est insuffisant.
- La persistance est stratifiée: état local durable (document + style metadata), état remote canonical (`cvDocument`), champs runtime (`documentDecoration.resolvedUrl`).
- Un garde d’actualisation doit préserver les champs de style locaux plus récents quand le contenu est similaire.

## Risque restant

- Des rafraîchissements remote peuvent encore forcer des régressions de style si la règle de fraîcheur/égalité n’est pas stable.

## Touched pages

- none
