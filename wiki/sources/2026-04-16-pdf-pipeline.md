---
title: "PDF Pipeline"
category: source
tags: [pdf, pipeline, export, html, playwright]
created: 2026-04-16
updated: 2026-04-16
status: current
valid_from: 2026-04-16
valid_until:
superseded_by:
horizon: present
version: v1
type: note
sources: []
related: [[tech/preview-to-print-pipeline]], [[tech/export-pipeline]]
---

# PDF Pipeline
**Type** : Note technique
**Date** : 2026-04-16
**URL** : source locale `rawinput/pdf pipeline.md`

## Résumé

Note ultra-courte qui fixe le vrai chemin PDF comme : client -> endpoint FastAPI -> worker Node -> HTML `export-renderers` -> Playwright PDF.

## Points clés

1. Le pipeline PDF réel est multi-surface et ne doit pas être résumé à un simple "frontend export".
2. Le worker Node et Playwright restent la frontière de génération PDF finale.
3. Le renderer HTML d'export est une étape explicite de la chaîne.

## Implications pour twoweeks

- Le wiki doit garder une représentation concise du chemin PDF réel pour éviter les diagnostics erronés.

## Extraits notables

- "the real PDF path: client -> FastAPI endpoint -> Node worker -> export-renderers HTML -> Playwright PDF"

## Pages wiki mises à jour

- [[tech/preview-to-print-pipeline]]
- [[tech/export-pipeline]]
