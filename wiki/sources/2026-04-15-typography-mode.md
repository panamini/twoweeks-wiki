---
title: "Typography Mode"
category: source
tags: [typography, locale, french, english, export, punctuation]
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

# Typography Mode
**Type** : Spec typographique
**Date** : 2026-04-15
**URL** : source locale `rawinput/TYPOGRAPHY MODE.md`

## Résumé

Note courte qui pose les règles minimales de typographie locale pour le texte généré ou exporté, avec un découpage explicite entre conventions françaises, conventions anglaises et règle globale de non-mélange dans un même passage.

## Points clés

1. En français : pas d'espace avant virgule ou point, espace insécable avant `: ; ? !`, guillemets français `« »`, accents sur capitales, virgule décimale, espace entre nombre et unité.
2. En anglais : pas d'espacement français avant la ponctuation, guillemets courbes, cohérence US ou UK par document, mois écrits en toutes lettres, espace entre nombre et unité SI.
3. Règle globale : ne pas mélanger conventions françaises et anglaises dans un même passage sans demande explicite.

## Implications pour twoweeks

- Le pipeline d'export doit avoir une couche de normalisation typographique dépendante de la locale.
- Ces règles doivent être lisibles par le LLM comme référence simple avant de produire des documents plus polis.

## Extraits notables

- "Never mix French and English typographic conventions in the same passage unless explicitly requested."

## Pages wiki mises à jour

- [[design/locale-typography-rules]]
- [[tech/export-pipeline]]
