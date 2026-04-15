---
title: "A4 Layout Systems"
category: design
tags: [layout, a4, grid, canon, robial, typography, resume]
created: 2026-04-15
updated: 2026-04-15
status: current
valid_from: 2026-04-15
valid_until:
superseded_by:
horizon: present
version: v1
sources: [2026-04-15-a4-grid-canon-spec-writer]
related: [[design/ats-safety]], [[tech/export-pipeline]], [[entities/twoweeks]]
---

# A4 Layout Systems

Référence active pour les systèmes de grille A4 utilisés ou réutilisables dans les templates CV twoweeks.

## Format de base

- largeur : `210 mm`
- hauteur : `297 mm`

## Système 1 — Van de Graaf adapté à l'A4

Logique classique asymétrique :

- marge intérieure : `1 division`
- marge haute : `1 division`
- marge extérieure : `2 divisions`
- marge basse : `2 divisions`

### Canon 12

- divisions : `17.5 mm` horizontal, `24.75 mm` vertical
- marges : `top 24.75 mm`, `right 35 mm`, `bottom 49.5 mm`, `left 17.5 mm`
- live area : `157.5 mm x 222.75 mm`

Usage recommandé :
- meilleur canon classique pour un résumé A4 dense
- compromis pratique entre élégance et surface utile

### Canon 9

- divisions : `23.3 mm` horizontal, `33 mm` vertical
- marges : `top 33 mm`, `right 46.7 mm`, `bottom 66 mm`, `left 23.3 mm`
- live area : `140 mm x 198 mm`

Usage recommandé :
- rendu plus luxueux et plus éditorial
- moins adapté aux CVs chargés

## Système 2 — Grille modulaire Robial 17/18

Logique modulaire alternée :

- rythme horizontal : `17, 18, 17, 18...`
- rythme vertical : `17, 18, 17, 18...`

Setup résumé recommandé :

- marges : `top 17 mm`, `right 35 mm`, `bottom 35 mm`, `left 17 mm`
- layout : `header full-width`, `sidebar 35 mm`, `gutter 18 mm`, `main 105 mm`

Usage recommandé :
- layout résumé asymétrique moderne
- système flexible pour templates premium et éditoriaux

## Recommandation active pour twoweeks

- option classique A4 : `Canon 12`
- option modulaire moderne : `Robial 17/18`

Le choix dépend du template, mais la géométrie doit rester explicite, mesurée en mm, et compatible avec les contraintes de lisibilité/export du pipeline document final.

## Voir aussi

- [[design/ats-safety]]
- [[tech/export-pipeline]]
- [[entities/twoweeks]]
