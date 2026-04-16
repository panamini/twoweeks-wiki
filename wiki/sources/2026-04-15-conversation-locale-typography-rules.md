---
title: "Conversation — Locale Typography Rules"
category: source
tags: [conversation, typography, locale, export, wrapping, pagination]
created: 2026-04-15
updated: 2026-04-15
status: current
valid_from: 2026-04-15
valid_until:
superseded_by:
horizon: present
version: v1
type: conversation
sources: []
related: [[design/locale-typography-rules]], [[tech/export-pipeline]], [[design/a4-layout-systems]]
---

# Conversation — Locale Typography Rules
**Type** : Conversation
**Date** : 2026-04-15
**URL** : instruction utilisateur en session Codex

## Résumé

Clarification supplémentaire sur la manière de documenter et d'appliquer les règles typographiques locales : elles doivent être plus lisibles humainement pour le LLM, indépendantes des tokens de géométrie/flow/apparence, et validées contre les effets de wrap et de pagination.

## Points clés

1. Les règles de typographie locale doivent être formulées comme documentation humaine de compréhension, pas seulement comme scratch pads.
2. Elles s'appliquent aux textes générés/exportés, labels, dates, ponctuation, nombres et copie normalisée quand la locale est connue.
3. Elles sont indépendantes de la géométrie, du flow et de l'apparence.
4. Les espaces insécables et comportements non-breaking doivent être testés contre wrap, clipping, collisions et page breaks.
5. Il faut ajouter une couverture de fixtures FR/EN sur ponctuation, guillemets, dates, décimales et formatage nombre-unité.

## Implications pour twoweeks

- Le wiki doit porter une page design consolidée de référence, plus lisible qu'un simple scratch pad.
- Le pipeline d'export doit considérer la typographie locale comme une couche dédiée avec validation de fidélité PDF/DOCX.

## Extraits notables

- "These rules are independent from geometry, flow, and appearance tokens."
- "Locale typography normalization must be validated against export wrap and page-break tests."

## Pages wiki mises à jour

- [[design/locale-typography-rules]]
- [[tech/export-pipeline]]
- [[design/a4-layout-systems]]
