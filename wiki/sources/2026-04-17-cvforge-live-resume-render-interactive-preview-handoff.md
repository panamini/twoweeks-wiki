---
title: "CVForge Live Resume Render / Interactive Preview Handoff"
category: source
tags: [cvforge, resume, preview, renderer, linking, runtime]
created: 2026-04-17
updated: 2026-04-17
status: current
valid_from: 2026-04-17
valid_until:
superseded_by:
horizon: present
version: v1
type: spec
sources: []
related: [[tech/live-resume-preview-runtime]], [[tech/preview-to-print-pipeline]], [[product/product-roadmap]]
---

# CVForge Live Resume Render / Interactive Preview Handoff
**Type** : Handoff technique
**Date** : 2026-04-17
**URL** : source locale `raw/CVForge Live Resume Render  Interactive Preview Handoff.md`

## Resume

Note d'architecture sur le runtime actif du preview resume CVForge. Elle couvre la chaine `CvForge -> VerbatiCvPreviewPanel -> VerbatiResumePreview -> ResumePage`, le mapping `CvDocument -> ResumeData`, les alias canoniques de `resumeLinking.ts`, et le routage preview -> editor -> modal/inline pour les sections resume.

## Points cles

1. La source de verite active du preview est `currentCv`, mappee en `ResumeData`; le sample fallback ne doit pas etre confondu avec le chemin vivant.
2. Le rendu visible est gouverne par `VerbatiResumePreview.tsx` et `ResumePage.tsx`, avec le choix du renderer porte par `style.ts`.
3. Les clics preview deviennent des `ResumeLinkIntent` resolus par `CvForge`, `ProfileReviewCard` et `SectionEditor` vers des surfaces modales ou inline.
4. Les alias `contact`, `notes` et `selected_projects` doivent etre normalises vers des surfaces editoriales canoniques au lieu d'etre traites comme des sections autonomes.
5. Le hidden editor host en workspace preview est un pont vers les surfaces d'edition canoniques, pas un second arbre de preview a debugger comme source visible.

## Implications pour twoweeks

- Le runtime preview resume doit etre documente comme une architecture distincte du pipeline preview-to-print.
- Les bugs visibles dans le preview doivent etre localises par couche : mapping, renderer, linking, ou surface editoriale.
- Le debug des presets non-Swiss doit commencer par `ClassicResumePage` quand `style.ts` route vers `robial`.

## Extraits notables

- "The live resume preview system is the CVForge runtime"
- "data-live-resume-preview="true" is the best runtime marker for the visible preview tree."
- "The hidden editor host exists so modal-capable preview clicks can still resolve into canonical editor surfaces."

## Pages wiki mises a jour

- [[tech/live-resume-preview-runtime]]
