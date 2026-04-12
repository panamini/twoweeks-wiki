---
title: "CV Families — Familles de sections"
category: concept
tags: [parser, families, sections, cv, structure]
created: 2026-04-09
updated: 2026-04-09
status: current
valid_from: 2026-04-09
valid_until:
superseded_by:
horizon: present
version: v0
sources: [2026-04-09-decisions-cvforge-sprint]
related: [[cv-forge]], [[cv-parsing-pipeline]]
---

# CV Families — Familles de sections

Une **famille** est une catégorie de section de CV. Le pipeline de CV Forge classe chaque bloc de texte parsé dans une famille. La qualité du parsing se mesure famille par famille.

## Familles identifiées

| Famille                | Stabilité | Notes                                                   |
| ---------------------- | --------- | ------------------------------------------------------- |
| IDENTITY / CONTACT     | Haute     | Bonne candidate pour POC JSON structuré                 |
| EDUCATION              | Haute     | Structure prévisible, bon candidat POC                  |
| EXPERIENCE             | Basse     | La plus instable — pas la première à traiter en JSON    |
| LANGUAGES              | Haute     | Courte, bien délimitée                                  |
| HOBBIES                | Moyenne   | Sous-représentée dans les fixtures réelles              |
| CERTIFICATIONS         | Moyenne   | Sous-représentée dans les fixtures réelles              |
| PROJECTS               | Moyenne   | Sous-représentée dans les fixtures réelles              |
| AFFILIATIONS           | Moyenne   | Sous-représentée dans les fixtures réelles              |
| ADDITIONAL INFORMATION | Basse     | Fourre-tout, difficile à structurer                     |
| SUMMARY / BODY         | Variable  | Contamination identifiée — tranche en cours d'isolation |

## Notion de contamination par famille

Chaque famille peut être affectée par de la **contamination** — du contenu d'une autre famille qui se glisse dans les sections parsées. La stratégie consiste à isoler et corriger les contaminations famille par famille, dans l'ordre de stabilité décroissante.

## Familles sous-représentées dans les fixtures

Les familles suivantes manquent de données réelles pour les tests et sont candidates à la génération de fixtures synthétiques :
- Hobbies
- Certifications
- Projects
- Affiliations
- Additional information

## Voir aussi

- [[cv-parsing-pipeline]] — la stratégie d'évolution du parser
- [[cv-forge]] — l'application
