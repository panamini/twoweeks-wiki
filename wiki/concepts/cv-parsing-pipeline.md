---
title: "CV Parsing Pipeline"
category: concept
tags: [parser, cv, mistral, structured, canonical, sections, architecture]
created: 2026-04-09
updated: 2026-04-14
status: current
valid_from: 2026-04-09
valid_until:
superseded_by:
horizon: present
version: v1
sources: [2026-04-09-decisions-cvforge-sprint, 2026-04-11-cv-parsing-poc-state, 2026-04-14-structured-parsing-canonical-truth]
related: [[concepts/cv-families]], [[concepts/parsing-poc-progress]], [[tech/import-ocr-pipeline]], [[entities/twoweeks]]
---

# CV Parsing Pipeline

Stratégie active d'évolution du parser CV. Le cap n'est ni un retour à un pipeline purement heuristique, ni un pivot brutal full-JSON. Le modèle retenu est un pipeline structuré par familles, avec fallbacks limités et vérité canonique portée par les sections.

---

## Architecture cible

1. OCR / ingest brut
2. Extraction structurée guidée par schéma, famille par famille
3. Post-validation et normalisation
4. Mapping vers `currentCv.sections[*].structuredContent`
5. Vues dérivées pour exports, compatibilité et affichages secondaires

Quand les sections structurées existent et sont valides, elles constituent la vérité canonique produit.

---

## Décisions actives

- **Approche hybride** : faire progresser le parser famille par famille, pas par réécriture globale.
- **Vérité canonique** : `sections[*].structuredContent` > tableaux top-level recalculés.
- **Fallbacks** : utiles pour la transition et la robustesse, jamais comme vérité durable.
- **Debug path** : reproduire d'abord sur la boucle locale complète quand il faut diagnostiquer un problème parser.

---

## Ce qu'il faut éviter

- revenir à un parsing majoritairement text-only
- laisser frontend et backend dériver des vérités séparées
- recalculer les top-level arrays indépendamment alors que `sections` est déjà fiable
- rouvrir des slices parsing validés sans contradiction live nouvelle

---

## État actuel des familles

Voir [[concepts/parsing-poc-progress]] pour le détail. À date, experience, education, languages et skills sont stabilisées, tandis que IDENTITY/CONTACT reste un chantier actif et les sections custom demandent encore un alignement block renderer.

---

## Horizon de travail

1. stabiliser la vérité canonique autour des sections
2. réduire la duplication top-level
3. décider explicitement quelles familles méritent un rendu first-class vs générique
4. renforcer les tests de régression sur vrais CVs avant d'élargir les POC

---

## Voir aussi

- [[concepts/cv-families]] — familles first-class vs secondaires
- [[concepts/parsing-poc-progress]] — progression du POC
- [[tech/import-ocr-pipeline]] — call path OCR/import
