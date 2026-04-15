---
title: "Parsing POC Progress — État par famille"
category: concept
tags: [parsing, poc, familles, fixtures, experience, education, languages, skills, identity, contact]
created: 2026-04-11
updated: 2026-04-15
status: archived
valid_from: 2026-04-11
valid_until: 2026-04-15
superseded_by: [[concepts/cv-parsing-pipeline]]
horizon: present
version: v1
sources: [2026-04-11-cv-parsing-poc-state, 2026-04-14-run-sh-quick-note, 2026-04-15-mistral-resume-v3-section-recovery-scratchpad, 2026-04-15-section-detection-future-note]
related: [[concepts/cv-parsing-pipeline]], [[concepts/cv-families]], [[entities/twoweeks]]
---

# Parsing POC Progress — Snapshot archivé

> Cette page est conservée comme snapshot d'une phase POC terminée. L'état courant du parser est désormais porté par [[concepts/cv-parsing-pipeline]] et par les pages tech/howto actives autour de `run.sh`.

État du POC parsing hybride sur le live path : `./run.sh tunnel` + Convex `cloud/default` + `https://parser.dasti.ai` + route `/mistral-ocr/parse`.

**Règle absolue : ne pas rouvrir un slice accepté sans nouvelle contradiction live.**

---

## État par famille

| Famille              | État          | Fixtures acceptées                                                                                                                            |
| -------------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **EXPERIENCE**       | ✅ Complète    | Jessica WORK HISTORY (3 entries, pas de faux row "Spring Education Group", pas de blob merged responsibilities, `desiredPosition` non pollué) |
| **EDUCATION**        | ✅ Complète    | Jessica (2 entrées cohérentes, plus de fragmentation institution-only/degree-only)                                                            |
| **LANGUAGES**        | ✅ Complète    | Robert : `languagesRaw` collapse → `["English","Spanish","Italian"]`                                                                          |
| **SKILLS**           | ✅ Complète    | Anne markdown-table cleanup, Jake grouped technical-skills recovery                                                                           |
| **IDENTITY/CONTACT** | 🟡 En cours   | Jessica address/location, Anne title-as-location guard, Linda location pass-through, Helen name fix, Helen desired-position fix               |
| **SUMMARY**          | ⬜ Pas démarré | —                                                                                                                                             |
| **ACHIEVEMENTS**     | ⬜ Pas démarré | —                                                                                                                                             |

---

## Roadmap POC (historique)

1. ✅ Finir Experience
2. 🟡 POC hybride IDENTITY/CONTACT (schema-first) — en cours
3. ⬜ EDUCATION enrichissement
4. ⬜ SUMMARY
5. ⬜ ACHIEVEMENTS

EXPERIENCE n'est pas la première famille schema-first — trop instable. Décision figée.

---

## Incohérence non-bloquante documentée

L'UI peut afficher la localisation Jessica alors que `contact.location` / `contact.addressNormalized` ne sont pas remplis dans les champs normalisés. Incohérence de contrat profile/materialization, **pas un échec de parsing** dans les slices fermés.

---

## Déférés

Jessica contact-location normalized-contract, Helen `New York` location recovery, website/linkedin, Robert experience oddities, Jake non-skills regressions.

---

## Clôture

Au 2026-04-15, ce POC de stabilisation est considéré comme terminé sur son périmètre initial. Les suites relèvent de la stabilisation continue, de l'observabilité et des choix de modes locaux/cloud, pas d'un backlog POC séparé.

## Voir aussi

- [[concepts/cv-parsing-pipeline]] — stratégie et état courant
- [[tech/import-ocr-pipeline]] — chemin de code complet
