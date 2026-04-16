---
title: "Token Classes for the Layout"
category: source
tags: [tokens, layout, geometry, flow, appearance, runtime, adr]
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
related: [[design/document-token-contract]], [[tech/export-pipeline]], [[design/a4-layout-systems]]
---

# Token Classes for the Layout
**Type** : ADR / spec
**Date** : 2026-04-16
**URL** : source locale `rawinput/token classes for the layout.md`

## Résumé

ADR qui fixe un contrat canonique de tokens document avec quatre classes d'ownership : `geometry`, `flow`, `appearance`, `runtime`. Le but est d'avoir une seule source de vérité entre preview, export CSS et DOCX, sans laisser les helpers runtime contaminer les snapshots exportés.

## Points clés

1. Le contrat interne officiel repose sur quatre classes : geometry, flow, appearance, runtime.
2. `appearance.decor` est explicitement non-structurel et ne peut pas piloter pagination, sizing ou reading measure.
3. `style.ts` doit déléguer au resolver canonique d'apparence, pas devenir une seconde autorité de thème.
4. Le choix primaire de police vient de `appearance.font.*`; les fallbacks sérialiseur sont autorisés uniquement comme littéraux de compatibilité plateforme.

## Implications pour twoweeks

- Le système de layout doit séparer plus proprement ce qui change la page, ce qui change le texte, et ce qui n'est qu'un helper runtime.
- Cette classification devient la base pour la convergence preview/export/DOCX.

## Extraits notables

- "Adopt a single internal token contract with four ownership classes"
- "appearance.decor is non-structural"

## Pages wiki mises à jour

- [[design/document-token-contract]]
- [[tech/export-pipeline]]
