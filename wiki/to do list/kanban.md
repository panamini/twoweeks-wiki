---
title: "Kanban — CV Forge Sprint"
category: todo
tags: [kanban, sprint, todo, bugs, parsing, cleanup]
created: 2026-04-12
updated: 2026-04-12
---

# Kanban · CV Forge

> Mise à jour via conversation. Déplacer les tâches de colonne en colonne au fil du sprint.

---

## 🔵 Backlog

### Parsing — familles restantes
- [ ] **EDUCATION enrichissement** — enrichir les champs parsés (dates, diplômes, institutions)
- [ ] **SUMMARY family** — schema-first ou heuristique selon résultat IDENTITY POC
- [ ] **ACHIEVEMENTS family** — extraction des accomplissements chiffrés

### Features produit
- [ ] **Warning navigation pendant import** — quand l'utilisateur tente de changer de page pendant l'import, warning ou import background. Décision : friction minimale vs background (best practice UX 2026)
- [ ] **AI rewrite suggestions** — 2–3 suggestions par section (Suggestion AI mode)

### Cleanup technique
- [ ] **Paddle cleanup** — supprimer les références Paddle (runtime/build/test, Docker, env/config). Ne pas toucher : `./run.sh up --ui`, Mistral OCR, Convex `cloud/default`, `https://parser.dasti.ai`, parser behavior, entrypoints runtime.

---

## 🟡 En cours

- [ ] **IDENTITY/CONTACT POC hybride** — schema-first. Fixes acceptés : Jessica address/location recovery, Anne title-as-location guard, Linda location pass-through, Helen name fix, Helen desired-position fix. **Ne pas rouvrir ces slices sans nouvelle contradiction live.**

---

## 🔴 Bugs ouverts

- [ ] **Scroll/zoom dans la preview CV** — scroll bloqué en mode zoom, pas de pan à 100% fit. À vérifier manuellement sur `./run.sh up --ui`.

---

## ✅ Done

| Tâche | Complété |
|-------|----------|
| POC EXPERIENCE — Jessica 3 entries, pas de faux row, pas de blob | 2026-04-11 |
| POC EDUCATION — Jessica 2 entrées cohérentes | 2026-04-11 |
| POC LANGUAGES — Robert languagesRaw collapse | 2026-04-11 |
| POC SKILLS — Anne markdown-table cleanup, Jake grouped technical-skills | 2026-04-11 |
| Convex investigation — CVs dans `userProfiles.cvDocument` confirmé | 2026-04-11 |
| Tones — Auto / Natural / Formal / Warm | 2026-04-10 |

---

## Notes

- Live path : `./run.sh up --ui` + Convex `cloud/default` + `https://parser.dasti.ai`
- Règle parsing : ne jamais rouvrir un slice accepté sans contradiction live
