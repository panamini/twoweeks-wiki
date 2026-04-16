---
title: "Export Pipeline — OCR to ATS / Styled Output"
category: tech
tags: [export, pdf, docx, ats, renderer, worker, preview, stylePreset]
created: 2026-04-14
updated: 2026-04-16
status: current
valid_from: 2026-04-14
valid_until:
superseded_by:
horizon: present
version: v1
sources: [2026-04-14-export-pipeline-brief-ocr-to-ats-styled-output, 2026-04-15-a4-grid-canon-spec-writer, 2026-04-15-typography-mode, 2026-04-15-french-typography-scratch-pad, 2026-04-15-english-typography-scratch-pad, 2026-04-15-conversation-locale-typography-rules, 2026-04-16-live-proposal-preview-to-print-pipeline-scratchpad, 2026-04-16-live-resume-preview-to-print-pipeline-scratchpad, 2026-04-16-pdf-pipeline, 2026-04-16-token-classes-for-the-layout]
related: [[tech/import-ocr-pipeline]], [[concepts/cv-parsing-pipeline]], [[design/ats-safety]], [[design/a4-layout-systems]], [[design/locale-typography-rules]], [[design/document-token-contract]], [[tech/preview-to-print-pipeline]], [[entities/twoweeks]]
---

# Export Pipeline — OCR to ATS / Styled Output

Référence technique du pipeline document final, de la donnée normalisée jusqu'au fichier téléchargé.

## Architecture en un coup d'œil

```text
OCR / parsing / state document normalisé
  -> export source builders
  -> unified export client
  -> parser export endpoints
  -> Node export worker
  -> export-only renderers
  -> PDF ou DOCX
  -> direct browser download
```

## Deux mondes de rendu

### Monde preview

Utilisé pour :

- édition à l'écran
- preview CvForge / ProposalForge
- zoom
- viewport fit
- preview shell UI

### Monde export

Utilisé pour :

- Resume ATS PDF
- Resume Styled PDF
- Proposal ATS PDF
- Proposal Styled PDF
- Proposal DOCX

Ces deux mondes peuvent partager :

- contenu normalisé
- style tokens
- layout intent
- `stylePreset`

Ils ne doivent pas partager :

- preview DOM monté comme source d'export
- wrappers de zoom / viewport
- screenshot export
- logique géométrique purement preview

## Source de vérité export

Les exports sont construits depuis des objets normalisés :

- `ResumePrintSource`
- `ProposalPrintSource`

Pour le styled export preview-driven, la chaîne active passe ensuite par des payloads print-route (`ResumePreviewPrintSource`, `ProposalPreviewPrintSource`) avant la route print Playwright.

La source visuelle est gouvernée par :

- `stylePreset`
- les style/layout tokens partagés
- le contrat de géométrie Robial grid

Pour les templates résumé A4, le wiki distingue désormais explicitement :

- `Canon 12` comme option classique dense et pratique
- `Canon 9` comme option éditoriale plus généreuse
- `Robial 17/18` comme système modulaire moderne recommandé

La typographie locale forme une couche distincte :

- conventions FR/EN de ponctuation et citations
- dates, décimales, nombre-unité
- normalisation textuelle dépendante de la locale

Elle ne doit pas modifier implicitement la géométrie ou les flow tokens.

## Couches principales

### Frontend trigger layer

Entrées UI typiques :

- `ResumeExportControl.tsx`
- `ProposalExportActions.tsx`
- `CvForge.tsx`
- `ProposalForge.tsx`

### Unified export client

Fichier principal :

- `my-app/src/lib/exportDocumentFile.ts`

Rôle :

- reçoit l'intention d'export depuis l'UI
- envoie un payload normalisé au parser service
- reçoit un blob fichier
- déclenche le téléchargement direct navigateur

### Export source builders

Fichier principal :

- `my-app/src/lib/document-export-models.ts`

Builders principaux :

- `buildResumeExportSource(...)`
- `buildProposalExportSource(...)`

### Backend export endpoints

Fichiers principaux :

- `cv_parser_service/main.py`
- `cv_parser_service/document_export.py`

### Worker layer

Fichier principal :

- `my-app/scripts/document-export-worker.ts`

### Renderer layer

Fichier principal :

- `my-app/src/lib/export-renderers.ts`

Renderers principaux :

- `ResumeAtsExportDocument`
- `ResumeStyledExportDocument`
- `ProposalAtsExportDocument`
- `ProposalStyledExportDocument`

## Règles d'architecture

- Le fichier final doit être généré hors preview DOM.
- Le PDF doit rester text-based, searchable et selectable.
- Le téléchargement final doit être direct-download.
- L'ancien helper raster `my-app/src/lib/document-export.ts` est legacy.
- La normalisation typographique locale doit être validée contre wrap et page-break tests.
- Preview et styled PDF doivent rester des jumeaux à travers la route print, pas deux systèmes concurrents.
- Le contrat canonique des tokens document doit séparer `geometry`, `flow`, `appearance` et `runtime`.

## Voir aussi

- [[tech/import-ocr-pipeline]] — chemin OCR/import jusqu'à la donnée normalisée
- [[concepts/cv-parsing-pipeline]] — stratégie parser et vérité canonique
- [[design/ats-safety]] — contraintes ATS sur les outputs
- [[design/a4-layout-systems]] — géométries A4 recommandées
- [[design/locale-typography-rules]] — règles FR/EN de typographie locale
- [[design/document-token-contract]] — classes de tokens et ownership
- [[tech/preview-to-print-pipeline]] — parité preview -> print -> PDF
