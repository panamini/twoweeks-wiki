---
title: "Document Token Contract"
category: design
tags: [tokens, geometry, flow, appearance, runtime, layout, export]
created: 2026-04-16
updated: 2026-04-16
status: current
valid_from: 2026-04-16
valid_until:
superseded_by:
horizon: present
version: v1
sources: [2026-04-16-token-classes-for-the-layout]
related: [[design/a4-layout-systems]], [[design/locale-typography-rules]], [[tech/export-pipeline]], [[tech/preview-to-print-pipeline]]
---

# Document Token Contract

Contrat canonique des classes de tokens document pour aligner preview, export CSS et DOCX.

## Classes officielles

- `geometry`
- `flow`
- `appearance`
- `runtime`

## Règles d'ownership

- `geometry` porte la page, la live area et les dimensions structurelles
- `flow` porte les comportements typographiques/layout qui affectent la lecture et potentiellement la pagination
- `appearance` porte le décor et les choix visuels non structurels
- `runtime` porte les helpers locaux de fit, mesure et instrumentation preview

## Règles figées

- `appearance.decor` est non-structurel
- `style.ts` n'est pas une autorité de thème indépendante
- le choix primaire de police vient de `appearance.font.*`
- les littéraux fallback plateforme sont tolérés uniquement pour compatibilité sérialiseur
- les helpers `runtime` ne doivent pas fuiter dans les snapshots exportés

## Pourquoi ça compte

Sans ce contrat, preview, export HTML/CSS et DOCX dérivent facilement vers plusieurs systèmes concurrents. Avec lui, chaque classe sait ce qu'elle a le droit d'influencer.

## Voir aussi

- [[design/a4-layout-systems]]
- [[design/locale-typography-rules]]
- [[tech/export-pipeline]]
- [[tech/preview-to-print-pipeline]]
