---
title: "Preview-to-Print Pipeline"
category: tech
tags: [preview, print, pdf, export, resume, proposal, playwright]
created: 2026-04-16
updated: 2026-04-27
status: current
valid_from: 2026-04-16
version: v1
sources: [2026-04-16-live-proposal-preview-to-print-pipeline-scratchpad, 2026-04-16-live-resume-preview-to-print-pipeline-scratchpad, 2026-04-16-pdf-pipeline, 2026-04-16-proposal-style-persistence-quickmap-scratchpad, 2026-04-16-verbati-style-pipeline-scratchpad, 2026-04-27-workshop-pagination]
related: [[tech/export-pipeline]], [[design/document-token-contract]], [[entities/twoweeks]], [[tech/workshop-pagination]]
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
- même snapshot visuel résolu (`stylePreset` ou `metadata.verbatiStyle`)
- même `templateId` ou `rendererVariantId` quand la structure le requiert
- même renderer de page
- mêmes vars/theme document
- mêmes fonts réellement matérialisées
- aucune seconde logique de layout export-only

Pour proposal, il faut distinguer explicitement :

- `templateId` : structure, disposition, géométrie
- `verbatiStyle` : identité visuelle persistée

Si le payload print ne transporte que le template et laisse le style être reconstruit depuis un default de liste, la parité preview -> print est déjà perdue avant `page.pdf()`.

## Boundaries de debug

Quand preview et PDF divergent, inspecter dans cet ordre :

1. état sélectionné dans l'UI
2. merge saved proposal / draft local / hydratation saved-view
3. payload export envoyé
4. bootstrap worker
5. route print prête
6. screenshot pre-`page.pdf()`
7. PDF final

Les écarts de typography fidelity peuvent venir du chargement réel des fonts, de wrappers différents, du timing print ou de la génération PDF elle-même.

Les écarts de style proposal peuvent aussi venir plus tôt :

- override optimiste sur le même id
- bundle par défaut réinjecté côté `ProposalsList`
- héritage CV rejoué au lieu d'un snapshot proposal détaché

## Workshop resume path

Pour `workshop_resume_onecol_ats`, la parité preview -> print -> export passe par `committedPages`.

Le planner calcule les frontières; le preview, la print route et l'export doivent lire ces pages engagées sans refaire une pagination locale. Si les surfaces divergent, vérifier d'abord qu'elles reçoivent le même payload `committedPages`, puis seulement ensuite inspecter les tokens, fonts et wrappers.

## Conséquence

Le bon diagnostic ne consiste pas à comparer seulement des types ou des snapshots JSON. Il faut comparer un même run de preview, route print et PDF final.

## Voir aussi

- [[tech/export-pipeline]]
- [[design/document-token-contract]]
- [[entities/twoweeks]]
- [[tech/workshop-pagination]]
