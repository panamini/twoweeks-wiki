---
title: "Preview-to-Print Pipeline"
category: tech
tags: [preview, print, pdf, export, resume, proposal, playwright]
created: 2026-04-16
updated: 2026-04-16
status: current
valid_from: 2026-04-16
valid_until:
superseded_by:
horizon: present
version: v1
sources: [2026-04-16-live-proposal-preview-to-print-pipeline-scratchpad, 2026-04-16-live-resume-preview-to-print-pipeline-scratchpad, 2026-04-16-pdf-pipeline]
related: [[tech/export-pipeline]], [[design/document-token-contract]], [[entities/twoweeks]]
---

# Preview-to-Print Pipeline

Référence technique du chemin styled preview -> print route -> PDF, pour résumé et proposal.

## Thèse

Preview et styled PDF doivent être des jumeaux. Le pipeline actif n'est pas un export HTML séparé inventé après coup, mais une réhydratation du même intent de preview sur une print route dédiée avant `page.pdf()`.

## Chaîne active

1. état preview vivant dans `CvForge` ou `ProposalForge`
2. payload preview-export (`ResumePreviewPrintSource` ou `ProposalPreviewPrintSource`)
3. requête client vers endpoint export
4. worker Node + Playwright
5. route `/print/resume` ou `/print/proposal`
6. screenshot pre-`page.pdf()`
7. bytes PDF finaux

## Contrat de parité

Les invariants critiques sont :

- même contenu/document state
- même `stylePreset`
- même `templateId` ou `rendererVariantId`
- même renderer de page
- mêmes vars/theme document
- mêmes fonts réellement matérialisées
- aucune seconde logique de layout export-only

## Boundaries de debug

Quand preview et PDF divergent, inspecter dans cet ordre :

1. état sélectionné dans l'UI
2. payload export envoyé
3. bootstrap worker
4. route print prête
5. screenshot pre-`page.pdf()`
6. PDF final

Les écarts de typography fidelity peuvent venir du chargement réel des fonts, de wrappers différents, du timing print ou de la génération PDF elle-même.

## Conséquence

Le bon diagnostic ne consiste pas à comparer seulement des types ou des snapshots JSON. Il faut comparer un même run de preview, route print et PDF final.

## Voir aussi

- [[tech/export-pipeline]]
- [[design/document-token-contract]]
- [[entities/twoweeks]]
