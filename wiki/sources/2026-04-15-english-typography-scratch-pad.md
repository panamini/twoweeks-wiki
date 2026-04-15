---
title: "English Typography Scratch Pad"
category: source
tags: [typography, english, locale, punctuation, us, uk, quotes]
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
related: [[design/locale-typography-rules]], [[tech/export-pipeline]]
---

# English Typography Scratch Pad
**Type** : Scratch pad typographique
**Date** : 2026-04-15
**URL** : source locale `rawinput/ENGLISH TYPOGRAPHY SCRATCH PAD.md`

## Résumé

Référence détaillée de typographie anglaise pour des sorties propres et cohérentes, en séparant clairement le choix de variante US/UK, les guillemets, la ponctuation des citations, les dates, les nombres et les unités.

## Points clés

1. Il faut choisir US ou UK par document et rester cohérent sur guillemets, dates, ponctuation de citation et style des tirets.
2. Les sorties polies utilisent des guillemets courbes et évitent tout espacement de type français avant la ponctuation.
3. Les dates doivent employer le mois en toutes lettres pour éviter l'ambiguïté.
4. Les unités SI conservent un espace entre le nombre et le symbole.
5. La cohérence documentaire est plus importante que le micro-style choisi, dès lors qu'il est stable.

## Implications pour twoweeks

- Les exports EN doivent expliciter la variante typographique choisie quand la locale ou le style guide le permet.
- Les tests d'export doivent couvrir au minimum guillemets, dates, ponctuation des citations et format nombre-unité.

## Extraits notables

- "First choose one variant and stay consistent: US English or UK English."
- "Do not use French spacing before punctuation."

## Pages wiki mises à jour

- [[design/locale-typography-rules]]
- [[tech/export-pipeline]]
