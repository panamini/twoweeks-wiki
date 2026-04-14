---
title: "twoweeks"
category: entity
tags: [twoweeks, app, product, parser, cv, roadmap, vision, brand, cvforge, proposalforge, extension]
created: 2026-04-12
updated: 2026-04-14
status: current
valid_from: 2026-04-12
valid_until:
superseded_by:
horizon: present
version: v2
sources: [2026-04-09-decisions-cvforge-sprint, 2026-04-10-notion-roadmap-cvforge, 2026-04-10-success-blueprint, 2026-04-10-benchmark-matrix, 2026-04-12-twoweeks-brand-bible, 2026-04-14-structured-parsing-canonical-truth, 2026-04-14-clerk-chrome-extension-addon, 2026-04-14-ats-compliant-score, 2026-04-14-run-sh-quick-note, 2026-04-14-export-pipeline-brief-ocr-to-ats-styled-output]
related: [[concepts/cv-parsing-pipeline]], [[concepts/cv-families]], [[overview]], [[concepts/product-roadmap]], [[concepts/kpis]], [[concepts/product-vision]], [[concepts/benchmark-matrix]], [[concepts/ai-product-model]], [[concepts/brand-voice]], [[concepts/ats-safety]]
---

# twoweeks

**twoweeks** (twoweeks.ai) est un outil haute performance de gestion de candidatures : parsing, normalisation, édition et génération de documents de candidature à partir d'un CV et d'un job context.

---

## Brand

**Tagline** : Finish. Faster.

**Positionnement** : outil "Anti-Work" pour les gens qui font un excellent travail et veulent aller plus vite sans subir la friction des outils RH mous.

Voir [[concepts/brand-voice]] pour la voix et les règles de copie.

---

## Modules internes

| Module | Rôle |
|--------|------|
| **CVForge** | génération et édition de CVs |
| **ProposalForge** | cover letters et proposals |
| **Extension Chrome** | capture de jobs et handoff vers twoweeks |

---

## Architecture produit actuelle

### Vérité canonique CV

Le cap actif est désormais :

`OCR -> extraction structurée par famille -> normalisation -> cvDocument.sections[*].structuredContent -> vues dérivées`

Les champs top-level legacy sont des vues de compatibilité ou des fallbacks, pas la vérité durable.

### Vérité export

Les exports finaux CV/proposal dérivent des données normalisées via des builders et renderers d'export dédiés. Le preview DOM n'est pas la source d'export finale.

### Architecture de stockage Convex

| Champ Convex | Rôle | Note |
|--------------|------|------|
| `userProfiles.cvDocument` | source de vérité CV | point de lecture/écriture principal |
| `cvDocument.sections` | sections structurées du CV | vérité active côté produit |
| `cvDocument.metadata.importRecoverySession.baseSectionsSnapshot` | snapshot d'import | base du recovery UI |
| `userProfiles.experience[]` | champ legacy | à dériver ou ignorer selon le contexte |
| `userProfiles.education[]` | champ legacy | à dériver ou ignorer selon le contexte |
| `userProfiles.skills[]` | champ legacy | à dériver ou ignorer selon le contexte |

---

## Environnements parser

- **Workflow local quotidien** : `./run.sh local`
- **Debug local complet** : `./run.sh local-convex`
- **Dev cloud / preview / tunnel** : `./run.sh tunnel`

`run.sh` est la source de vérité opératoire pour ces modes. Les longues variantes `up --ui ...` ne sont plus la doc de premier niveau. Le localhost doit rester derrière une condition dev-only. Voir [[tech/local-vs-remote-parser-architecture]].

---

## Axes de qualité prioritaires

- stabilité de parsing sur vrais CVs
- réduction des divergences entre sections et vues dérivées
- régression tests et observabilité
- ATS safety des outputs et templates
- polish du path extension -> save-to-twoweeks

---

## État du sprint

**En cours** : stabilité parser, block renderer des sections custom, polish extension, backlog UX import.

**Bugs ouverts** : zoom/scroll preview, `achievement` encore visible dans Manage Section alors que chargé.

**Backlog important** : Paddle cleanup, warning navigation pendant import, AI rewrite suggestions, mapping propre hobbies/projects/additional information.

Voir [[to do list/kanban]] pour le détail.

---

## Voir aussi

- [[concepts/cv-parsing-pipeline]] — stratégie d'évolution du parser
- [[concepts/cv-families]] — familles first-class vs secondaires
- [[concepts/ats-safety]] — règles parser-safe
- [[concepts/product-roadmap]] — roadmap complète
- [[concepts/product-vision]] — blueprint complet
- [[tech/import-ocr-pipeline]] — chemin de code import OCR
- [[tech/local-vs-remote-parser-architecture]] — séparation local/cloud
