---
title: "CV Parsing POC State — Checkpoint 2026-04-11"
category: source
tags: [parsing, poc, checkpoint, experience, education, languages, skills, identity, contact]
created: 2026-04-11
updated: 2026-04-11
status: current
valid_from: 2026-04-11
valid_until:
superseded_by:
horizon: present
version: v1
type: spec
sources: []
related: [[concepts/parsing-poc-progress]], [[concepts/cv-parsing-pipeline]]
---

# CV Parsing POC State — Checkpoint 2026-04-11

**Date** : 2026-04-11 | **Live path** : `./run.sh up --ui` + Convex `cloud/default` + `https://parser.dasti.ai`

## Familles closes

| Famille | Résultat |
|---------|----------|
| EXPERIENCE | Jessica WORK HISTORY : 3 entries, pas de faux row, pas de blob, desiredPosition non pollué |
| EDUCATION | Jessica : 2 entrées cohérentes, fin de fragmentation |
| LANGUAGES | Robert : languagesRaw collapse → `["English","Spanish","Italian"]` |
| SKILLS | Anne markdown-table clean, Jake grouped technical-skills OK |

## Slices acceptés (ne pas rouvrir)

Jessica experience recovery, Jessica education recovery, Jessica desired-position pollution fix, Helen name fix, Helen desired-position fix, Robert languages cleanup, Anne markdown-table skills cleanup, Jake grouped technical-skills recovery, Anne title-as-location guard, Linda normalized location pass-through/materialization, Jessica address/location recovery.

## Incohérence non-bloquante

UI peut afficher la localisation Jessica sans que `contact.location` / `contact.addressNormalized` soient remplis. Incohérence de contrat profile/materialization, pas un échec de parsing dans les slices fermés.

## Fichiers touchés

`cv_parser_service/mistral_ocr.py`, `cv_parser_service/tests/test_mistral_layout_sections.py`, `my-app/convex/lib/parsing/canonicalize.ts`, `my-app/convex/lib/parsing/__tests__/canonicalize.test.ts`
