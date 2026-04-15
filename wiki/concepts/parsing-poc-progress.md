---
title: "Parsing POC Progress — État par famille"
category: concept
tags: [parsing, poc, familles, fixtures, experience, education, languages, skills, identity, contact]
created: 2026-04-11
updated: 2026-04-14
status: current
valid_from: 2026-04-11
valid_until:
superseded_by:
horizon: present
version: v1
sources: [2026-04-11-cv-parsing-poc-state, 2026-04-14-run-sh-quick-note]
related: [[cv-parsing-pipeline]], [[cv-families]], [[cv-forge]]
---

# Parsing POC Progress — État par famille

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

## Roadmap (ordre validé)

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

## Voir aussi

- [[cv-parsing-pipeline]] — stratégie et décision hybride
- [[tech/import-ocr-pipeline]] — chemin de code complet
