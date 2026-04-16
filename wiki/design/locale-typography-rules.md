---
title: "Locale Typography Rules"
category: design
tags: [typography, locale, french, english, export, punctuation, wrapping]
created: 2026-04-15
updated: 2026-04-15
status: current
valid_from: 2026-04-15
valid_until:
superseded_by:
horizon: present
version: v1
sources: [2026-04-15-typography-mode, 2026-04-15-french-typography-scratch-pad, 2026-04-15-english-typography-scratch-pad, 2026-04-15-conversation-locale-typography-rules]
related: [[design/a4-layout-systems]], [[design/brand-voice]], [[tech/export-pipeline]], [[design/ats-safety]]
---

# Locale Typography Rules

Référence humaine de typographie locale pour les sorties générées et exportées. Cette page consolide les scratch pads FR/EN en règles plus lisibles pour le LLM et pour les humains qui maintiennent les exports.

## Portée

Ces règles s'appliquent à :

- texte généré ou exporté
- labels et copie UI quand la locale est connue
- dates, ponctuation, citations, nombres, unités
- texte normalisé dans les documents finaux

Elles sont **indépendantes** de la géométrie, du flow et des tokens d'apparence.

## Règles françaises

- pas d'espace avant virgule ni point
- espace insécable avant `: ; ? !`
- préférer une espace fine insécable avant `; ? !` quand le rendu le permet
- utiliser les guillemets français `« »`
- garder les accents sur les capitales
- utiliser la virgule pour les décimales
- garder un espace entre un nombre et son unité
- dates en style `15 avril 2026`
- heures en style soigné `14 h 30`
- rester cohérent sur toute la séquence française

## Règles anglaises

- ne jamais utiliser l'espacement français avant la ponctuation
- utiliser des guillemets courbes
- choisir US ou UK par document et rester cohérent
- appliquer les conventions de ponctuation de citation du variant choisi
- écrire le mois en toutes lettres dans les dates
- garder un espace entre un nombre et son unité SI
- rester cohérent sur toute la séquence anglaise

## Règles globales

- ne jamais mélanger conventions françaises et anglaises dans le même passage sans demande explicite
- ne pas laisser les règles de locale modifier implicitement la géométrie ou les flow tokens
- traiter la normalisation typographique comme une couche de sortie, pas comme un remplacement des systèmes de grille

## Caveat d'export

Les espaces insécables et autres comportements non-breaking peuvent changer le wrapping.

La règle active est donc :

> Locale typography normalization must be validated against export wrap and page-break tests so punctuation and unit spacing do not introduce clipping, collisions, or unstable pagination.

## Conséquences produit

- Les templates et exports doivent séparer nettement géométrie A4, tokens visuels et règles typographiques locales.
- Les tests d'export FR/EN doivent couvrir ponctuation, guillemets, dates, décimales et formatage nombre-unité.
- La typographie locale doit améliorer la qualité perçue sans dégrader la fidélité PDF/DOCX.

## Voir aussi

- [[design/a4-layout-systems]]
- [[design/brand-voice]]
- [[design/ats-safety]]
- [[tech/export-pipeline]]
