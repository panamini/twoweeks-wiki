---
title: "Section Detection Future Note — Narrow Recovery Scope"
category: source
tags: [parser, section-detection, recovery, scope, guardrails]
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
related: [[concepts/cv-parsing-pipeline]], [[tech/import-ocr-pipeline]]
---

# Section Detection Future Note — Narrow Recovery Scope
**Type** : Spec technique
**Date** : 2026-04-15
**URL** : source locale `rawinput/section detection.md`

## Résumé

La note fixe une garde de scope : la première vague de recovery déterministe doit rester limitée aux sections locales et peu ambiguës, sans dériver vers une seconde implémentation complète du parser.

## Points clés

1. Le périmètre initial validé couvre `languages`, `skills` et le path `achievements` existant.
2. Les sections riches comme `experience`, `education`, `projects`, `certifications` ou `publications` ne doivent pas recevoir de reconstruction markdown heuristique dans cette phase.
3. L'ordre recommandé pour de futurs élargissements reste : gates de validation, recovery bornée par section, puis validation sur audits répétés.
4. L'objectif explicite est d'améliorer la correction sans créer un second parser concurrent à la pipeline annotation + normalization.

## Implications pour twoweeks

- Le travail parser en cours doit être décrit comme stabilisation incrémentale avec garde-fous, pas comme expansion opportuniste de heuristiques.
- Le wiki doit marquer le POC de base comme terminé et distinguer clairement les futures extensions optionnelles.

## Extraits notables

- "The current stabilization scope should remain intentionally narrow."
- "The goal of the first stabilization pass is to improve correctness without creating a second full parser."

## Pages wiki mises à jour

- [[concepts/cv-parsing-pipeline]]
- [[tech/import-ocr-pipeline]]
