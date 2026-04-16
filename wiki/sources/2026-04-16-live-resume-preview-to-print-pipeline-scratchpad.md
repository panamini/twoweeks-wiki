---
title: "Live Resume Preview-to-Print Pipeline Scratchpad"
category: source
tags: [resume, preview, print, pdf, export, pipeline, typography]
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

# Live Resume Preview-to-Print Pipeline Scratchpad
**Type** : Scratch pad technique
**Date** : 2026-04-16
**URL** : source locale `rawinput/Live Resume Preview-to-Print Pipeline Scratchpad.md`

## Résumé

Note opératoire sur le pipeline styled resume export. Elle décrit la chaîne active entre `CvForge`, `VerbatiResumePreview`, `ResumePage`, `exportDocumentFile`, le worker Playwright, la route `/print/resume` et le PDF final.

## Points clés

1. La parité preview/PDF styled repose sur `ResumePreviewPrintSource`, `stylePreset`, `rendererVariantId`, `ResumePage` et les mêmes theme vars.
2. Le print route `/print/resume` n'est pas un renderer spécial, mais une surface jumelle de `ResumePage`.
3. Les divergences typographiques peuvent venir de plusieurs boundaries : font materialization, wrapper surface, role styling, timing `page.pdf()`.
4. Le screenshot pre-`page.pdf()` est un checkpoint obligatoire si l'on veut distinguer un problème de route print d'un problème de génération PDF.

## Implications pour twoweeks

- Le pipeline styled resume doit être documenté comme une chaîne de parité explicite.
- Les bugs de typography fidelity doivent être localisés par boundary et non résolus à l'aveugle.

## Extraits notables

- "styled preview and styled PDF are supposed to be twins"
- "The print route is meant to be a twin rendering surface"

## Pages wiki mises à jour

- [[tech/preview-to-print-pipeline]]
- [[tech/export-pipeline]]
