# wiki/archive/ — Pages supersédées

Ce dossier contient les pages wiki qui ont été **remplacées** par des informations plus récentes. Elles sont conservées pour la traçabilité historique du projet.

## Structure

```
archive/
├── entities/    ← entités supersédées
├── concepts/    ← concepts supersédés (décisions changées, pivots)
└── sources/     ← sources dont les conclusions ont été invalidées
```

## Comment une page atterrit ici

Quand une information est contredite ou remplacée :
1. La nouvelle page est créée dans `wiki/[catégorie]/` avec `status: current`
2. L'ancienne page est déplacée ici avec `status: archived`
3. L'ancienne page reçoit `valid_until: YYYY-MM-DD` et `superseded_by: [[nouvelle-page]]`
4. L'événement est tracé dans `wiki/timeline.md`

## Quand consulter ce dossier

- Questions historiques : "quelle était notre architecture technique en v1 ?"
- Comprendre pourquoi on a pivoté
- Éviter de répéter des erreurs passées
- Audits de cohérence (workflow Lint)

## Règle LLM

Par défaut, le LLM **ne lit pas** ce dossier sauf si la query est explicitement historique. Les pages archivées ne doivent jamais polluer des réponses sur l'état actuel.
