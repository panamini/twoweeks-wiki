---
title: "CV Families"
category: concept
tags: [cv, sections, families, renderer, parsing, schema]
created: 2026-04-09
updated: 2026-04-17
status: current
valid_from: 2026-04-09
valid_until:
superseded_by:
horizon: present
version: v1
sources: [2026-04-09-decisions-cvforge-sprint, 2026-04-11-cv-parsing-poc-state, 2026-04-14-structured-parsing-canonical-truth, 2026-04-14-kanban-sprint-notes]
related: [[concepts/cv-parsing-pipeline]], [[concepts/parsing-poc-progress]], [[entities/twoweeks]]
---

# CV Families

Le produit raisonne en familles de sections CV. Chaque famille n'a pas le même niveau de maturité parser, de support UI, ni le même besoin d'être first-class dans le block renderer.

---

## Familles first-class aujourd'hui

- profile / contact
- summary
- experience
- education
- certifications
- skills
- languages
- projects

Ce sont les familles qui doivent guider la normalisation, les tests de régression et le rendu principal.

---

## Familles secondaires ou plus tardives

- awards
- publications
- volunteering
- additional information
- hobbies
- autres sections libres

Elles existent structurellement, mais ne sont pas encore traitées partout comme des sections produit de premier rang.

---

## Décisions de mapping actuelles

- `projects` doit converger vers un rendu de type experience quand c'est pertinent.
- `additional information` doit converger vers un rendu de type summary.
- `hobbies` doit converger vers un rendu de type skills.
- `add your own section` doit créer une vraie section du block renderer, pas une sous-structure legacy nested.

---

## Règle produit

Une famille peut rester générique temporairement, mais pas incohérente. Si une section est visible dans l'UI, son type, son renderer et sa source de vérité doivent rester alignés avec le modèle canonique `sections[*].structuredContent`.

---

## Voir aussi

- [[concepts/cv-parsing-pipeline]] — stratégie d'ensemble
- [[concepts/parsing-poc-progress]] — slices déjà stabilisés
- [[tasks/kanban]] — tâches ouvertes sur les sections custom
