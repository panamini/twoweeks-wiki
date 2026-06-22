---
title: "MCP and ChatGPT App Readiness Spec"
category: source
tags: [mcp, chatgpt-app, distribution, api]
created: 2026-06-11
updated: 2026-06-11
status: current
type: analysis
---

# MCP and ChatGPT App Readiness Spec

**Type** : Technical spec note
**Date** : 2026-06-11
**URL** : source locale `raw/MCP ChatGPT App Readiness Spec.md`

## Résumé

Spécification de préparation à l’activation MCP/ChatGPT App avec limite stricte de portée: cette PR est seulement locale et documentaire.

## Points clés

- L’implémentation actuelle est exclusivement PR16 local MCP beta; pas de transport remote, pas d’exécution produit réelle, pas d’UI/routes.
- Outils exposés localement: `application_package.summarize`, `evidence_graph.summarize`, `resume_variant_plan.summarize`, `review_cockpit.summarize`.
- Les prochaines étapes recommandées gardent la même contrainte de séparation: projection MCP en TS pur, enveloppe d’appel, audit/approbation, puis transport remote.
- Checklist de sécurité listée: allowlist, approbation humaine pour actions, sorties bornées, logs append-only, révocation d’outil.

## Risques et garde-fous

- Ne pas ouvrir `send/apply/submit/export` dans cette phase.
- Ne pas décloisonner la sécurité CV/CandidateFacts avant la couche d’approbation.
- Éviter la surcharge de portée dans les PR de distribution.

## Touched pages

- none
