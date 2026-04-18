---
title: "Live Resume Preview Runtime"
category: tech
tags: [resume, preview, renderer, linking, editor, runtime]
created: 2026-04-17
updated: 2026-04-17
status: current
valid_from: 2026-04-17
valid_until:
superseded_by:
horizon: present
version: v1
sources: [2026-04-17-cvforge-live-resume-render-interactive-preview-handoff]
related: [[tech/preview-to-print-pipeline]], [[tech/export-pipeline]], [[product/product-roadmap]], [[entities/twoweeks]]
---

# Live Resume Preview Runtime

Reference technique du runtime actif du preview resume dans CVForge, depuis `currentCv` jusqu'aux intents d'edition retournes vers les surfaces canoniques.

## These

Le preview resume vivant n'est ni un sample renderer autonome ni une simple previsualisation statique. C'est une chaine de rendu interactive qui mappe le document canonique vers `ResumeData`, choisit un renderer depuis le style preset, expose des zones cliquables et reroute ces intents vers les vraies surfaces d'edition sans reload.

## Chaine active

1. `CvForge.tsx` porte l'etat page, `workspaceMode`, `resumeLinkIntent` et `resumeActiveTarget`
2. `VerbatiCvPreviewPanel.tsx` choisit la source active et mappe `currentCv` vers `ResumeData`
3. `VerbatiResumePreview.tsx` monte le viewport interactif, intercepte les clics et fabrique les `ResumeLinkIntent`
4. `style.ts` route le style preset vers un `rendererVariantId`
5. `ResumePage.tsx` resolve le vrai renderer visuel (`ClassicResumePage`, `SwissMinimaPage`, etc.)
6. `ProfileReviewCard.tsx` et `SectionEditor.tsx` renvoient l'intent vers une surface modale ou inline canonique
7. la mutation du `currentCv` remappe le preview sans reload de page

## Sources d'autorite

Les fichiers pivots de ce runtime sont :

- `my-app/src/pages/CvForge.tsx`
- `my-app/src/features/verbati/VerbatiCvPreviewPanel.tsx`
- `my-app/src/features/verbati/VerbatiResumePreview.tsx`
- `my-app/src/features/verbati/style.ts`
- `my-app/src/features/verbati/resumeLinking.ts`
- `my-app/src/features/verbati/cvDocumentToResumeData.ts`
- `my-app/src/features/verbati/resume/ResumePage.tsx`
- `my-app/src/components/ProfileReviewCard.tsx`
- `my-app/src/components/SectionEditor.tsx`

## Invariants critiques

- le preview vivant doit partir de `currentCv` quand il existe; le sample fallback reste une roue de secours
- `cvDocumentToResumeData.ts` normalise la presence des sections; si une section vide reste visible, le bug est probablement dans le renderer ou l'etat UI, pas dans le mapping
- `style.ts` ne suffit pas a identifier le composant final; plusieurs presets non-Swiss finissent dans `ClassicResumePage`
- `resumeLinking.ts` est l'autorite canonique pour les alias preview et les surfaces editoriales cibles
- `data-live-resume-preview="true"` est le meilleur marqueur pour l'arbre preview visible
- le hidden host editor de `CvForge` supporte les clics preview en mode workspace preview, mais n'est pas un deuxieme renderer visible

## Boundaries de debug

Quand le preview visible se comporte mal, inspecter dans cet ordre :

1. `currentCv` et le choix `active` vs sample fallback
2. mapping `CvDocument -> ResumeData`
3. routing `stylePreset -> rendererVariantId`
4. branche renderer active dans `ResumePage.tsx`
5. metadata DOM preview et `ResumeLinkIntent`
6. normalisation des alias dans `resumeLinking.ts`
7. resolution editoriale dans `ProfileReviewCard.tsx` et `SectionEditor.tsx`

## Consequences produit

Cette architecture soutient l'initiative `Editor ↔ Preview linking` de la roadmap sans pivoter vers un produit preview-first. Le preview garde sa valeur emotionnelle et perceptible, mais l'edition canonique reste possedee par les surfaces modales et inline existantes.

## Voir aussi

- [[tech/preview-to-print-pipeline]]
- [[tech/export-pipeline]]
- [[product/product-roadmap]]
- [[entities/twoweeks]]
