---
title: "Verbati Style Pipeline Scratchpad"
category: source
tags: [verbati, style, proposal, tokens, render]
created: 2026-04-16
updated: 2026-04-16
status: current
valid_from: 2026-04-16
valid_until:
superseded_by:
horizon: present
version: v1
type: spec
sources: []
related: [[design/document-token-contract]], [[tech/preview-to-print-pipeline]], [[tech/export-pipeline]]
---

# Verbati Style Pipeline Scratchpad
**Type** : spec  
**Date** : 2026-04-16  
**URL** : rawinput/Verbati Style Pipeline Scratchpad.md

## Résumé

Cartographie rapide du pipeline actif `verbati` pour clarifier ce qui fait autorité dans le rendu visuel proposal et ce qui ne doit pas être considéré comme source de vérité.

## Points clés

- `metadata.verbatiStyle` est la source de vérité persistée pour l'identité visuelle proposal.
- `templateId` décrit surtout la géométrie, le template et certains defaults structurels, mais ne doit pas devenir une autorité de style concurrente.
- Le style runtime peut hériter du CV tant que la proposal n'est pas détachée, mais le rendu doit toujours se faire depuis un snapshot résolu de `verbatiStyle`.
- Les vrais points d'autorité passent par `style.ts`, `documentAppearance.ts`, `ProposalForge.tsx`, `ProposalDisplay.tsx`, `ProposalDocumentRenderer.tsx`, `styleState.ts`, `useBoundVerbatiCvStyle.ts`, `proposal-render-state.ts` et `proposal-output-draft.ts`.
- Les zones non autoritatives incluent `pdf-ingest/`, les backups, `ProposalForgeNext.tsx` et les tokens de thème génériques qui n'entrent pas dans le pipeline document.

## Implications pour twoweeks

- Le contrat des tokens doit distinguer plus clairement le rôle de l'apparence résolue par rapport au template structurel.
- Le pipeline preview-to-print doit transporter le snapshot visuel résolu, pas seulement un identifiant de template.
- Les audits de régression proposal doivent couvrir l'héritage initial, le détachement, la sauvegarde, la réouverture et l'export.

## Extraits notables

- Le renderer ne devrait jamais devoir deviner le style final à partir d'une simple clé de template.
- Un thème shell ou app-wide n'est pas, par lui-même, une preuve que le document exporté recevra les mêmes tokens.

## Pages wiki mises à jour

- [[design/document-token-contract]]
- [[tech/preview-to-print-pipeline]]
- [[tech/export-pipeline]]
