---
title: "Export Pipeline Brief — OCR to ATS / Styled Output"
category: source
tags: [export, ocr, pdf, docx, ats, preview, renderer]
created: 2026-04-14
updated: 2026-04-14
status: current
valid_from: 2026-04-14
valid_until:
superseded_by:
horizon: present
version: v1
type: spec
sources: []
related: [[tech/export-pipeline]], [[tech/import-ocr-pipeline]], [[concepts/cv-parsing-pipeline]], [[design/ats-safety]], [[entities/twoweeks]]
---

# Export Pipeline Brief — OCR to ATS / Styled Output
**Type** : Brief technique
**Date** : 2026-04-14
**URL** : source locale `rawinput/Export Pipeline Brief  OCR to ATS Styled Output.md`

## Résumé

Cette note documente le pipeline document de bout en bout : OCR/parsing, normalisation des données, construction des sources d'export, client d'export unifié, endpoints parser, worker Node, renderers d'export, puis téléchargement direct du PDF ou DOCX. Elle formalise aussi une séparation forte entre le monde preview et le monde export.

## Points clés

1. Le système supporte désormais : Resume ATS PDF, Resume Styled PDF, Proposal ATS PDF, Proposal Styled PDF et Proposal DOCX.
2. L'export part de **normalized data objects** via `ResumePrintSource` et `ProposalPrintSource`, jamais du DOM preview monté.
3. Le pipeline d'export reste séparé du preview DOM, tout en partageant contenu normalisé, style tokens, layout intent et `stylePreset`.
4. Le parser service reçoit les payloads normalisés via des endpoints d'export, puis un worker Node rend le document final en PDF ou DOCX avec téléchargement direct navigateur.
5. L'ancien helper raster `my-app/src/lib/document-export.ts` est explicitement legacy ; la voie cible est text-based, direct-download, searchable/selectable et gouvernée par le contrat Robial grid.

## Implications pour twoweeks

- Il faut une page technique dédiée au pipeline d'export, distincte du call path OCR/import.
- La doc active doit expliciter que preview et export sont deux mondes de rendu différents.
- ATS safety doit intégrer la contrainte "real text PDF / direct-download / pas de screenshot export".

## Extraits notables

- "There are two different rendering worlds"
- "Exports are built from normalized data objects, not from the visible preview DOM."
- "The browser does not use `window.print()` for the final UX."

## Pages wiki mises à jour

- [[tech/export-pipeline]]
- [[tech/import-ocr-pipeline]]
- [[concepts/cv-parsing-pipeline]]
- [[design/ats-safety]]
- [[entities/twoweeks]]
