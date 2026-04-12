---
title: "Jessica/Helen Identity-Experience-Education POC State"
category: source
tags: [parsing, poc, jessica, helen, identity, experience, education, fixtures]
created: 2026-04-11
updated: 2026-04-11
status: current
valid_from: 2026-04-11
valid_until:
superseded_by:
horizon: present
version: v1
type: document
sources: []
related: [[concepts/parsing-poc-progress]], [[concepts/cv-parsing-pipeline]]
---

# Jessica/Helen Identity-Experience-Education POC State

Checkpoint fixes Jessica et Helen sur les familles IDENTITY/CONTACT, EXPERIENCE, EDUCATION.

## Fixes IDENTITY/CONTACT acceptés

- Jessica address/location recovery
- Anne title-as-location guard
- Linda normalized location pass-through/materialization
- Helen name fix
- Helen desired-position fix

## EXPERIENCE — POC complet

Jessica WORK HISTORY : 3 entries, pas de faux row "Spring Education Group", pas de blob responsibilities, pas de pollution desiredPosition. Fermé.

## EDUCATION — POC complet

Jessica : 2 entrées cohérentes. Pas encore fully enrichi (dates/diplômes/institutions). Fermé pour ce sprint.

## Incohérence documentée (non-bloquante)

UI affiche localisation Jessica mais `contact.location` / `contact.addressNormalized` peuvent ne pas être remplis → incohérence profile/materialization, pas un échec parsing.
