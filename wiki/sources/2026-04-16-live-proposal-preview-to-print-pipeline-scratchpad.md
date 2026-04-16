---
title: "Live Proposal Preview-to-Print Pipeline Scratchpad"
category: source
tags: [proposal, preview, print, pdf, export, pipeline, playwright]
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
related: [[tech/preview-to-print-pipeline]], [[tech/export-pipeline]]
---

# Live Proposal Preview-to-Print Pipeline Scratchpad
**Type** : Scratch pad technique
**Date** : 2026-04-16
**URL** : source locale `rawinput/Live Proposal Preview-to-Print Pipeline Scratchpad.md`

## Résumé

Note opératoire sur le pipeline styled proposal export. Elle documente la chaîne complète entre le preview visible dans `ProposalForge`, le clic `Export Styled PDF`, le worker Playwright, la route `/print/proposal` et les bytes PDF finaux retournés par `page.pdf()`.

## Points clés

1. Preview et styled PDF sont censés être jumeaux car ils partagent le même `ProposalDocumentRenderer`, le même `templateId`, le même `stylePreset` et la même `voicePreset`.
2. La frontière critique entre preview et export est `ProposalPreviewPrintSource`.
3. Le worker ne doit pas inventer une seconde logique de layout; il doit réhydrater le payload preview sur `/print/proposal`.
4. Le bon diagnostic d'un écart passe par la parité d'un même export run : preview visible, payload envoyé, bootstrap worker, screenshot pre-`page.pdf()`, bytes finaux.

## Implications pour twoweeks

- Le pipeline styled proposal doit être documenté comme preview-driven print route, pas comme ancien renderer HTML séparé.
- Les audits de fidélité doivent comparer preview et print-route ready state avant de blâmer Playwright ou les fonts.

## Extraits notables

- "preview and styled PDF are supposed to be twins"
- "The worker is not supposed to invent an export-only layout"

## Pages wiki mises à jour

- [[tech/preview-to-print-pipeline]]
- [[tech/export-pipeline]]
