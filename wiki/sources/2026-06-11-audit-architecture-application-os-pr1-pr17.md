---
title: "Audit architecture — Application OS PR1 à PR17"
category: source
tags: [application-os, architecture, audit]
created: 2026-06-11
updated: 2026-06-11
status: current
type: analysis
---

# Audit architecture — Application OS PR1 à PR17

**Type** : Architecture audit note
**Date** : 2026-06-11
**URL** : source locale `raw/Audit architecture — Application OS PR1 à PR17.md`

## Résumé

Audit documentaire de `application-os-foundation` couvrant PR1 à PR17 dans le socle "Application OS".

## Points clés

- L’audit a été réalisé à partir de la documentation de décision, des plans et des fichiers inspectés dans les modules Application OS, avec comparaison adaptée `main...application-os-foundation`.
- Une matrice module par module a été reconstituée pour `application-harness`, `candidate-evidence`, `career-knowledge`, `evidence-graph`, `resume-variants`, `review-cockpit`, `cover-letter-artifact`, `application-package`, `internal-tool-contracts` et `controlled-ats-scout`.
- Des écarts de sécurité, de provenance de données et de limites de portée ont été repérés pour prioriser la suite sans élargir le scope de manière non nécessaire.
- Le document fixe des **interdictions opérationnelles** pour le travail courant (pas de remote MCP, pas de ChatGPT App, pas d’OAuth, pas de scraping LinkedIn/Upwork/Indeed, pas de mutation CV canonical, pas de mutation sémantique des `CandidateFacts` dans cette phase).
- La suite recommandée garde le rail local: `controlled-ats-scout`, `internal-tool-contracts` purement locaux, projection MCP/handler en étapes.

## Recommandations d’action

- Exécuter d’abord les vérifications ciblées sur les modules auditables (CV/facts/candidat/ATS) avec tests locaux ciblés.
- Mettre en séquence les prochaines PR de sûreté d’abord, puis passer progressivement aux couches API/agent.
- Réserver les changements infra/UX plus larges à une fenêtre dédiée pour éviter les confusions de source de vérité.

## Touched pages

- none
