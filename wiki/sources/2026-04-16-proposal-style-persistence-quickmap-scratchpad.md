---
title: "Proposal Style Persistence Quickmap Scratchpad"
category: source
tags: [proposal, style, persistence, render, convex]
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
related: [[tech/preview-to-print-pipeline]], [[tech/export-pipeline]], [[design/document-token-contract]]
---

# Proposal Style Persistence Quickmap Scratchpad
**Type** : spec  
**Date** : 2026-04-16  
**URL** : rawinput/Proposal Style Persistence Quickmap Scratchpad.md

## Résumé

Scratchpad de debug sur la persistance du style proposal et les dérives entre draft local, saved proposal, liste de proposals et rendu final.

## Points clés

- La vérité de persistance passe par les métadonnées proposal stockées dans Convex et par le draft browser local tant qu'il n'est pas commité.
- La vérité de rendu est le bundle résolu `verbatiStyle` + `templateId` effectivement transmis à `ProposalDisplay`.
- Deux frontières de bug sont identifiées : override optimiste/local sur le même id lors du merge des proposals sauvegardées, puis override bundle/default côté `ProposalsList.tsx`.
- La route saved-view peut se réhydrater avec un mauvais bundle visuel si la sélection ou l'hydratation locale rejoue un état plus récent que le record sauvegardé.
- Les fichiers critiques sont `ProposalForge.tsx`, `ProposalsList.tsx`, `ProposalDisplay.tsx`, `proposal-render-state.ts`, `proposal-output-draft.ts` et les mutations/queries Convex publiques.

## Implications pour twoweeks

- La doc doit distinguer plus fermement l'autorité de persistance et l'autorité de rendu.
- Le debug export/preview ne suffit pas si le saved-view résout déjà un mauvais style avant l'étape print.
- Le contrat document doit expliciter la différence entre sélection structurelle (`templateId`) et identité visuelle résolue (`verbatiStyle`).

## Extraits notables

- Le style sauvegardé peut être correct en base et pourtant être masqué au moment du merge local ou de l'hydratation saved-view.
- La bonne inspection se fait à la jonction `saved proposal -> draft local -> render state`, pas seulement sur le PDF final.

## Pages wiki mises à jour

- [[design/document-token-contract]]
- [[tech/preview-to-print-pipeline]]
- [[tech/export-pipeline]]
