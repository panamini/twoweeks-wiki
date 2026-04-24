---
title: "Pass 3B Structured Scoring Decisions"
category: source
tags: [jobs-v2, structured-scoring, calibration, beta-review]
created: 2026-04-24
updated: 2026-04-24
status: current
valid_from: 2026-04-24
type: analysis
---

# Pass 3B Structured Scoring Decisions
**Type** : Decision note
**Date** : 2026-04-24
**URL** : source locale `raw/Pass 3B Structured Scoring Decisions.md`

## Resume

Note de décision pour la review interne beta du structured shadow output. La position centrale est simple: le score production reste l'autorité, le structured match reste shadow-only, et aucune promotion user-facing ou rollout production ne doit partir avant la revue de 30-50 paires job/profile et le readout de calibration.

## Points cles

1. La revue vise 30-50 paires réelles avec couverture obligatoire sur security/licensed, retail/service, admin/office, technical, healthcare/regulated, multilingual, short noisy scrape, long duplicated scrape et negative controls.
2. Le prochain passage doit juger la correction sémantique et la calibration de tier, pas la validité schema.
3. Le rubric demande de vérifier extraction, evidence quality, outcome quality et tier calibration sur structured shadow output uniquement.
4. Les labels de review sont: good, acceptable but conservative, overmatched, undermatched, metadata leak, evidence missing, language issue, hard-gate issue.
5. Les blockers de broad rollout sont overmatched, metadata leak, language issue et hard-gate issue.
6. Le readout doit lister les cas reviewed, la couverture, les counts de labels, des exemples de false strong / false weak / overconfident partial, et une next action explicite.
7. Le rollout gate exige au moins 30 cas, la couverture complète, zero fuite de metadata/langue récurrente, negative controls weak, strong tiers avec evidence réelle, et high unknown sans surconfiance.

## Implications pour twoweeks

- Cette note sert de contrat de beta review pour le structured match shadow path.
- `computeMatchRead` et le score production ne changent pas dans ce pass.
- `unknown` doit rester une information de coverage / confidence, pas une preuve positive.
- Le beta review readout doit guider add fixtures, tune extraction semantics, tune evidence matching, tune tier gates, ou hold rollout.

## Pages wiki mises à jour

- `wiki/index.md`
- `wiki/log.md`

