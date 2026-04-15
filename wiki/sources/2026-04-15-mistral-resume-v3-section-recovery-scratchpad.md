---
title: "Mistral Resume V3 — Section Recovery Scratchpad"
category: source
tags: [parser, mistral, recovery, sections, telemetry, retry]
created: 2026-04-15
updated: 2026-04-15
status: current
valid_from: 2026-04-15
valid_until:
superseded_by:
horizon: present
version: v1
type: spec
sources: []
related: [[concepts/cv-parsing-pipeline]], [[tech/import-ocr-pipeline]], [[entities/twoweeks]]
---

# Mistral Resume V3 — Section Recovery Scratchpad
**Type** : Spec technique
**Date** : 2026-04-15
**URL** : source locale `rawinput/Mistral Resume V3 Section-Recovery Scratchpad.md`

## Résumé

Note technique sur le comportement actuel du pipeline Mistral Resume V3 pour la détection de sections explicites, la recovery déterministe locale à une section, la validation post-recovery, le retry OCR unique et la télémétrie légère de qualité parser.

## Points clés

1. Le pipeline actif s'appuie sur l'évidence de section extraite du markdown OCR, pas sur l'annotation brute, pour décider quand rejeter, récupérer ou retenter.
2. La recovery déterministe reste volontairement étroite : `languages`, `skills`, et le path existant `achievements`.
3. La recovery est locale à la section détectée; il n'y a pas de mining document-wide pour reconstruire `skills` ou `languages`.
4. Une seconde passe de validation après recovery empêche d'accepter silencieusement des valeurs polluées ou non préservées.
5. La télémétrie `diagnostics.parsingQuality` et le marker de logs `[mistral-quality]` servent de boundary de debug prioritaire avant toute investigation UI.

## Implications pour twoweeks

- Le parser actif doit être documenté comme pipeline structuré avec gates, recovery bornée et retry unique.
- Le debug live doit partir des diagnostics parser et des logs request-level, pas des symptômes UI uniquement.
- Le chantier "POC parsing" initial peut être considéré comme clos sur ce périmètre étroit; les travaux restants sont de la stabilisation continue, pas un POC ouvert.

## Extraits notables

- "The parser does not blindly trust the annotation when OCR markdown shows explicit section evidence."
- "There is exactly one allowed retry."
- "The earliest useful boundary is almost always: OCR markdown section evidence."

## Pages wiki mises à jour

- [[concepts/cv-parsing-pipeline]]
- [[tech/import-ocr-pipeline]]
- [[overview]]
- [[entities/twoweeks]]
