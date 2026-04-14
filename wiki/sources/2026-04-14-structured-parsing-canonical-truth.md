---
title: "Structured Parsing Canonical Truth"
category: source
tags: [parsing, mistral, structured, sections, canonical, cv, architecture]
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
related: [[concepts/cv-parsing-pipeline]], [[concepts/cv-families]], [[tech/import-ocr-pipeline]], [[entities/twoweeks]]
---

# Structured Parsing Canonical Truth
**Type** : Note d'architecture parsing  
**Date** : 2026-04-14  
**URL** : source locale `rawinput/ARCHITECTURE PARSIN MISTRAL.md`

## Résumé

Clarifie la vérité canonique du produit côté parsing CV. La cible active est désormais : extraction structurée par famille, normalisation, puis rendu/exports dérivés de `currentCv.sections[*].structuredContent` quand ces sections existent et sont valides.

## Points clés

1. **Le backend suit déjà la bonne direction** : OCR → extraction structurée guidée par schéma → post-validation/normalisation → mapping en sections applicatives.
2. **La vérité UI actuelle** : `currentCv.sections[*].structuredContent` est ce que l'éditeur consomme réellement.
3. **Le vrai problème** : coexistence entre sections structurées et tableaux top-level de compat/export qui peuvent diverger.
4. **Décision cible** : `sections` devient la vérité canonique produit ; les top-level arrays deviennent des vues dérivées ou des fallbacks.
5. **Familles solides aujourd'hui** : profile/contact, summary, experience, education, certifications, skills, languages, projects.
6. **Familles moins first-class** : awards, publications, volunteering, sections libres.

## Implications pour twoweeks

- Le pipeline parsing doit être documenté comme architecture structurée, pas comme heuristique-first.
- Les exports et copies JSON doivent dériver des sections lorsqu'elles existent.
- Les fallbacks heuristiques restent utiles pour la robustesse de transition, pas comme vérité durable.
- La roadmap des sections custom doit aligner `add your own section` avec le vrai block renderer.

## Extraits notables

> "quand `sections` existe et est valide, `sections[*].structuredContent` devient la vérité canonique produit"

> "ne pas laisser frontend et backend fabriquer chacun leur propre vérité durablement"

## Pages wiki mises à jour

- [[concepts/cv-parsing-pipeline]] — concept recréé et mis à jour
- [[concepts/cv-families]] — familles stabilisées vs secondaires
- [[tech/import-ocr-pipeline]] — chemin de vérité clarifié
- [[timeline]] — décision d'architecture datée
