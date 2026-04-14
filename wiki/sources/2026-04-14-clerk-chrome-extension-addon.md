---
title: "Clerk Chrome Extension Addon — Save to twoweeks"
category: source
tags: [extension, chrome, jobs, save, modal, ux, twoweeks]
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
related: [[entities/twoweeks]], [[to do list/kanban]], [[concepts/product-roadmap]]
---

# Clerk Chrome Extension Addon — Save to twoweeks
**Type** : Micro-spec UX extension  
**Date** : 2026-04-14  
**URL** : source locale `rawinput/clerk chrome extension specs addon.md`

## Résumé

Ajout UX pour l'extension Chrome : au hover d'une offre d'emploi, afficher une capsule "Save" qui ouvre le modal "send to twoweeks". Le pattern de référence cité est Pinterest.

## Points clés

1. **Trigger** : hover sur une offre d'emploi.
2. **Affordance** : capsule save légère, visible sans surcharger la carte.
3. **Action** : ouverture du modal `send to twoweeks`.
4. **Valeur produit** : raccourcir le chemin Job import path sans quitter la page source.

## Implications pour twoweeks

- Renforce le path extension-to-app déjà identifié comme moat potentiel.
- Doit être priorisé comme polish UX plutôt que comme refonte fonctionnelle lourde.
- Mérite une ligne claire dans le kanban sprint.

## Pages wiki mises à jour

- [[to do list/kanban]] — backlog enrichi côté extension
- [[entities/twoweeks]] — rappel du rôle de l'extension dans le produit
