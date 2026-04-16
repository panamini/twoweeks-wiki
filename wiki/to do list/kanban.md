---
title: "Kanban — twoweeks Sprint"
category: todo
tags: [kanban, sprint, todo, bugs, parsing, cleanup, extension, sections]
created: 2026-04-12
updated: 2026-04-15
status: current
valid_from: 2026-04-12
valid_until:
superseded_by:
horizon: present
version: v1
sources: [2026-04-11-todo-sprint, 2026-04-14-kanban-sprint-notes, 2026-04-14-clerk-chrome-extension-addon, 2026-04-14-run-sh-quick-note, 2026-04-15-run-sh-workspace-modes, 2026-04-15-mistral-resume-v3-section-recovery-scratchpad]
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
- [ ] 

---

## En cours

- [x] **Stabiliser la vérité canonique** — aligner rendus, JSON copiés/exports et vues dérivées sur `sections[*].structuredContent`.
- [x] **IDENTITY/CONTACT POC hybride** — fixs acceptés déjà documentés, ne pas rouvrir sans contradiction live.
- [ ] ##add paper color

Use the existing token as the base and extend it instead of replacing it:

- `--paper` = current default sheet color
- later add optional named paper variants such as:
    - `--paper-frost`
    - `--paper-ivory`
    - `--paper-recycled`

Then:

- preview page background can use `var(--paper)`
- export can either keep `var(--paper)` for digital simulation or override page background to white while still keeping colored rails/cards

---

## Bugs ouverts

- [ ] **Scroll/zoom preview CV** — scroll bloqué en mode zoom, pas de pan à 100% fit.
- [ ] **Achievements encore visible dans Manage Section** — incohérence alors que la section est déjà chargée.
- [ ] verify if proposal are saved in the library. and persistent. in convex. make autosave default for generated proposal. 
- [ ] export ats and exportpd  style and docx should be accesible from the library proposal
- [ ] align `./run.sh local-convex` alias behavior with `local-fast`, or deprecate the alias explicitly in code and docs
- [ ] Structured upload routing consistency
- Investigate why CV import in `run.sh local` still routes through cloud Convex → parser.dasti.ai
- Decide the intended behavior:
  - either `local` should support fully local structured upload
  - or `local` should clearly not support import until `local-convex` is fixed
- Fix `local-convex` bootstrap or add a direct local parser path for structured upload
	- Goal: import CV, OCR parse, and export should all behave consistently in local mode
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
| Parsing stabilization POC — gates + section-local recovery + retry + telemetry documentés | 2026-04-15 |

---

## Notes

- Live path : `./run.sh tunnel`
- Debug parser local recommandé : `./run.sh local-fast`
- Alias legacy encore mentionné : `./run.sh local-convex`
- Règle parsing : ne jamais rouvrir un slice accepté sans contradiction live nouvelle
