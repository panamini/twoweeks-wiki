---
title: "CV Parsing Pipeline"
category: concept
tags: [parser, cv, mistral, structured, canonical, sections, architecture]
created: 2026-04-09
updated: 2026-04-15
status: current
valid_from: 2026-04-09
valid_until:
superseded_by:
horizon: present
version: v1
sources: [2026-04-09-decisions-cvforge-sprint, 2026-04-11-cv-parsing-poc-state, 2026-04-14-structured-parsing-canonical-truth, 2026-04-14-export-pipeline-brief-ocr-to-ats-styled-output, 2026-04-15-mistral-resume-v3-section-recovery-scratchpad, 2026-04-15-section-detection-future-note]
related: [[concepts/cv-families]], [[tech/import-ocr-pipeline]], [[tech/export-pipeline]], [[entities/twoweeks]]
---

# CV Parsing Pipeline

Stratégie active d'évolution du parser CV. Le cap n'est ni un retour à un pipeline purement heuristique, ni un pivot brutal full-JSON. Le modèle retenu est un pipeline structuré par familles, avec fallbacks limités, gates explicites, recovery bornée et vérité canonique portée par les sections.

---

## Architecture cible

1. OCR / ingest brut
2. Extraction structurée guidée par schéma, famille par famille
3. Post-validation et normalisation
4. Mapping vers `currentCv.sections[*].structuredContent`
5. Vues dérivées pour exports, compatibilité et affichages secondaires

Quand les sections structurées existent et sont valides, elles constituent la vérité canonique produit.

Les exports finaux doivent donc dériver de cette donnée normalisée via des builders d'export, et non du preview DOM monté.

---

## Décisions actives

- **Approche hybride** : faire progresser le parser famille par famille, pas par réécriture globale.
- **Vérité canonique** : `sections[*].structuredContent` > tableaux top-level recalculés.
- **Fallbacks** : utiles pour la transition et la robustesse, jamais comme vérité durable.
- **Recovery bornée** : la reconstruction déterministe depuis le markdown OCR reste limitée aux sections locales et peu ambiguës (`languages`, `skills`, path `achievements` existant).
- **Retry unique** : un seul refetch OCR est autorisé quand le pipeline échoue sur une contradiction d'évidence de section.
- **Debug path** : reproduire d'abord sur la boucle locale complète quand il faut diagnostiquer un problème parser.

---

## Ce qu'il faut éviter

- revenir à un parsing majoritairement text-only
- laisser frontend et backend dériver des vérités séparées
- recalculer les top-level arrays indépendamment alors que `sections` est déjà fiable
- rouvrir des slices parsing validés sans contradiction live nouvelle

---

## État actuel

Le POC de stabilisation initiale est considéré comme terminé sur son périmètre étroit. Les familles `experience`, `education`, `languages` et `skills` ont un socle accepté; le travail restant relève surtout de stabilisation continue, d'observabilité et d'alignement des couches locales/cloud plutôt que d'un POC ouvert famille par famille.

Le parser actif s'appuie désormais explicitement sur :

1. evidence OCR markdown par heading
2. gate d'acceptation contre cette evidence
3. recovery déterministe locale à la section quand elle est autorisée
4. seconde validation post-recovery
5. retry OCR unique si contradiction persistante

---

## Horizon de travail

1. stabiliser la vérité canonique autour des sections
2. réduire la duplication top-level
3. décider explicitement quelles familles méritent un rendu first-class vs générique
4. renforcer les tests de régression sur vrais CVs avant tout élargissement de recovery

---

## Voir aussi

- [[concepts/cv-families]] — familles first-class vs secondaires
- [[tech/import-ocr-pipeline]] — call path OCR/import
