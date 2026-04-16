---
title: "French Typography Scratch Pad"
category: source
tags: [typography, french, locale, punctuation, numbers, spacing]
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

# French Typography Scratch Pad
**Type** : Scratch pad typographique
**Date** : 2026-04-15
**URL** : source locale `rawinput/FRENCH TYPOGRAPHY SCRATCH PAD.md`

## Résumé

Référence détaillée de typographie française moderne pour la ponctuation, les guillemets, les capitales accentuées, les nombres, les dates, les heures et les unités.

## Points clés

1. La ponctuation française impose des espaces insécables avant `: ; ? !`, mais jamais avant virgule ni point.
2. Les guillemets français `« »` doivent être accompagnés d'espaces insécables internes.
3. Les capitales conservent accents et cédille; les décimales utilisent la virgule.
4. Les dates, heures et unités suivent des conventions explicites : `15 avril 2026`, `14 h 30`, `8 kg`, `20 °C`.
5. La cohérence typographique sur tout le passage est traitée comme règle absolue.

## Implications pour twoweeks

- Les exports FR doivent être validés sur ponctuation, dates, nombres et unités, pas seulement sur le choix des guillemets.
- Une normalisation trop agressive doit être testée contre le wrapping et la pagination PDF.

## Extraits notables

- "Keep accents and cedilla on capitals."
- "Use a comma as the decimal separator."

## Pages wiki mises à jour

- [[design/locale-typography-rules]]
- [[tech/export-pipeline]]
