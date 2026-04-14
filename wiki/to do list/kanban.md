---
title: "Kanban — twoweeks Sprint"
category: todo
tags: [kanban, sprint, todo, bugs, parsing, cleanup, extension, sections]
created: 2026-04-12
updated: 2026-04-14
status: current
valid_from: 2026-04-12
valid_until:
superseded_by:
horizon: present
version: v1
sources: [2026-04-11-todo-sprint, 2026-04-14-kanban-sprint-notes, 2026-04-14-clerk-chrome-extension-addon, 2026-04-14-run-sh-quick-note]
related: [[entities/twoweeks]], [[concepts/cv-parsing-pipeline]], [[concepts/cv-families]]
---

# Kanban · twoweeks

> Sprint actif : fiabilité parser live, vérité canonique sections, normalisation des sections custom, polish du path extension.

---

## Backlog

- [ ] **Warning navigation pendant import** — friction minimale ou import background, décision UX à trancher.
- [ ] **AI rewrite suggestions** — 2 à 3 suggestions par section.
- [ ] **Save to twoweeks dans l'extension** — capsule hover sur offre d'emploi ouvrant le modal `send to twoweeks`.
- [ ] **Add your own section -> vrai block renderer** — choix explicite `skill`, `experience`, `summary`.
- [ ] **Mapper les sections legacy** — `projects` -> experience style, `additional information` -> summary style, `hobbies` -> skill style.
- [ ] **Observabilité + régression parser** — métriques, vrais CVs, derniers durcissements bruit template/liens/contact.
- [ ] **Paddle cleanup** — supprimer les références Paddle sans toucher au workflow actif parser/Convex.

---

## En cours

- [x] **Stabiliser la vérité canonique** — aligner rendus, JSON copiés/exports et vues dérivées sur `sections[*].structuredContent`.
- [x] **IDENTITY/CONTACT POC hybride** — fixs acceptés déjà documentés, ne pas rouvrir sans contradiction live.

---

## Bugs ouverts

- [ ] **Scroll/zoom preview CV** — scroll bloqué en mode zoom, pas de pan à 100% fit.
- [ ] **Achievements encore visible dans Manage Section** — incohérence alors que la section est déjà chargée.
- [ ] verify if proposal are saved in the library. and persistent. in convex. make autosave default for generated proposal. 
- [ ] export ats and exportpd  style and docx should be accesible from the library proposal
- [ ] ./run.sh local-convex  is not working fix it
---

## Déférés

- [ ] **CVs synthétiques** — à relancer seulement après les durcissements qualité live et les tests de régression utiles.
- [ ] Export UX feedback
- Add loading state to export actions for Resume ATS PDF, Resume Styled PDF, Proposal ATS PDF, Proposal Styled PDF, and Proposal DOCX
- On click:
  - disable the clicked action
  - show spinner or subtle indeterminate fill animation
  - change label to “Generating PDF…” / “Generating DOCX…”
- Do not use fake determinate progress unless real progress events exist
- Re-enable on success/failure
- Show error toast/message on failure
Reason:
PDF export can take ~5–10s through the current backend render pipeline, so users need immediate visual feedback that the action is processing.

---

## Done

| Tâche | Complété |
|-------|----------|
| POC EXPERIENCE — Jessica 3 entries, pas de faux row, pas de blob | 2026-04-11 |
| POC EDUCATION — Jessica 2 entrées cohérentes | 2026-04-11 |
| POC LANGUAGES — Robert languagesRaw collapse | 2026-04-11 |
| POC SKILLS — Anne markdown-table cleanup, Jake grouped technical-skills recovery | 2026-04-11 |
| Convex investigation — CVs dans `userProfiles.cvDocument` confirmé | 2026-04-11 |
| Tones — Auto / Natural / Formal / Warm | 2026-04-10 |

---

## Notes

- Live path : `./run.sh tunnel`
- Debug parser local : `./run.sh local-convex`
- Règle parsing : ne jamais rouvrir un slice accepté sans contradiction live nouvelle
