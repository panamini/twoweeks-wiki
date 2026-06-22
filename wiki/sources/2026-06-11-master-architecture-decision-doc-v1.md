---
title: "Twoweeks Application OS Execution Starter Pack"
category: source
tags: [architecture, planning, application-os]
created: 2026-06-11
updated: 2026-06-11
status: current
type: draft
---

# Twoweeks Application OS Execution Starter Pack

**Type** : Master planning source
**Date** : 2026-06-11
**URL** : source locale `raw/master architecture decision doc v1.md`

## Résumé

Pack exécutable de transition vers l’Application OS, orienté PR par PR avec scope strict et garde-fous.

## Points clés

- Décrit la séparation des couches métier (harness, evidence, review cockpit, artifact, distribution) et la préférence pour un noyau réduit.
- Met en place une série PR ordonnée avec limites explicites pour éviter le "tout refaire".
- Insiste sur les contrats de preuve: checklists, rollback rules, points de stop, preuves de test.
- Introduit un format de prompts Codex structuré pour réduire l’ambiguïté d’exécution.

## Règles fortes

- Les documents de plan restent documentation de pilotage et ne doivent pas être convertis en implémentation brute.
- Aucune suppression non nécessaire de faits existants; prioriser les tâches minimales et vérifiables.

## Touched pages

- none
