---
title: "A4 Grid Canon Spec Writer"
category: source
tags: [layout, a4, grid, canon, robial, typography, resume]
created: 2026-04-15
updated: 2026-04-15
status: current
valid_from: 2026-04-15
valid_until:
superseded_by:
horizon: present
version: v1
type: spec
sources: []
related: [[design/a4-layout-systems]], [[design/ats-safety]], [[tech/export-pipeline]]
---

# A4 Grid Canon Spec Writer
**Type** : Spec design/layout
**Date** : 2026-04-15
**URL** : source locale `rawinput/A4 Grid Canon Spec Writer.md`

## Résumé

Spec de référence pour formaliser des systèmes de page A4 applicables aux résumés et layouts éditoriaux. La note compare deux familles principales : le canon classique de Van de Graaf adapté à l'A4 (`Canon 12` et `Canon 9`) et une grille modulaire alternée Robial `17/18`.

## Points clés

1. Le format cible reste l'A4 exact : `210 mm x 297 mm`.
2. `Canon 12` est la meilleure option classique pratique pour un résumé dense : marges `24.75 / 35 / 49.5 / 17.5 mm`, live area `157.5 x 222.75 mm`.
3. `Canon 9` est plus spacieux et plus éditorial, mais moins efficace pour des CVs riches en contenu : marges `33 / 46.7 / 66 / 23.3 mm`, live area `140 x 198 mm`.
4. La grille Robial `17/18` fournit une structure moderne plus flexible pour des layouts asymétriques, avec une configuration recommandée de résumé `17 / 35 / 35 / 17 mm` et un corps `sidebar 35 mm / gutter 18 mm / main 105 mm`.
5. La spec insiste sur des sorties exactes, implementation-ready, avec unités en mm, objets JSON/CSS tokens et distinction stricte entre marges, live area et logique de division.

## Implications pour twoweeks

- Le pipeline d'export peut s'appuyer sur une base de géométrie A4 plus explicite pour ses templates résumé.
- `ATS Safety` doit distinguer plus clairement les layouts single-column sûrs des systèmes modulaires qui restent lisibles mais ne doivent pas compromettre l'extraction.
- La doc produit peut recommander `Canon 12` comme option classique et Robial `17/18` comme option modulaire moderne pour les templates A4.

## Extraits notables

- "For a real résumé on A4: best classical option: Canon 12"
- "best modern modular option: Robial 17/18"
- "never be vague about dimensions"

## Pages wiki mises à jour

- [[design/a4-layout-systems]]
- [[design/ats-safety]]
- [[tech/export-pipeline]]
