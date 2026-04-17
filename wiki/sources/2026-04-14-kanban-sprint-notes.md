---
title: "Kanban Sprint Notes — 2026-04-14"
category: source
tags: [kanban, sprint, backlog, sections, extension, parser, tests]
created: 2026-04-14
updated: 2026-04-17
status: current
valid_from: 2026-04-14
valid_until:
superseded_by:
horizon: present
version: v1
type: conversation
sources: []
related: [[tasks/kanban]], [[concepts/cv-parsing-pipeline]], [[entities/twoweeks]]
---

# Kanban Sprint Notes — 2026-04-14
**Type** : Notes de backlog  
**Date** : 2026-04-14  
**URL** : source locale `rawinput/kanban.md`

## Résumé

Lot de priorités sprint : durcissement qualité sur de vrais CVs, observabilité/régression, normalisation des sections custom dans le block renderer, nettoyage de familles legacy, bug Achievements dans Manage Section, et idée d'extension Chrome "Save to twoweeks".

## Points clés

1. **Priorité de fond** : fiabilité sur vrais CVs, métriques/observabilité, tests de régression, derniers durcissements sur bruit template/liens/contact.
2. **Sections custom** : `add your own section` doit devenir une vraie entrée du block renderer et permettre de choisir skill / experience / summary.
3. **Legacy nested sections à corriger** : hobbies → style skills, projects → style experience, additional information → style summary.
4. **Bug UI** : `achievement` apparaît encore dans Manage Section alors que la section est déjà chargée.
5. **Tests synthétiques** : idée à relancer plus tard, pas avant les durcissements qualité live.

## Implications pour twoweeks

- Le backlog parsing doit privilégier la stabilité live et la régression avant l'expansion POC.
- Les sections custom deviennent un vrai sujet de modèle produit, pas un bricolage UI isolé.
- Le bug Achievements signale une incohérence de source de vérité côté gestion de sections.

## Pages wiki mises à jour

- [[tasks/kanban]] — backlog enrichi
- [[concepts/cv-families]] — familles custom et mappings documentés
