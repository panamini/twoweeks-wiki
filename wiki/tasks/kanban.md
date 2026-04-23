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
- [x] **Add your own section -> vrai block renderer** — choix explicite `skill`, `experience`, `summary`. ✅ 2026-04-19
- [x] **Mapper les sections legacy** — `projects` -> experience style, `additional information` -> summary style, `hobbies` -> skill style. ✅ 2026-04-19
- [x] **Observabilité + régression parser** — métriques, vrais CVs, derniers durcissements bruit template/liens/contact. ✅ 2026-04-19
- [ ] **Paddle cleanup** — supprimer les références Paddle sans toucher au workflow actif parser/Convex.
- [ ] check if propsoal is autosaved and resume is autosaved
- [ ] remove the modal name ur resume at start
- [ ] see how we deall withs save and autosave 
- [ ] remove the all cap namee in proposal 
- [ ] 

( ) 


() le edit responsabilites n'est pas update, ni edit skill dans la page jobs
concevoir la page job comme une colonne obsidienne
que fait tailor cv ? dans job?rediger le summary, chosir les skills a partir du job ? faut il creer un profil utilisateur de base pour le comparer au cv ingeres? et l'adapter en fonction , l'ia peut aller piocher dans la database de l'user et en fonction sortir les bons mots pour compelter les cv 
que fait do both?
dans quick start ajouter pull a job from library
pour l'instant les job c des gros paves de texte degueu lasse. soit on a un truc qui les resume  pour que l'user comprenen tres vite ce que, avec des info standart, salaire demande nombre de mois disponibilité enfin tous les trucs classique , et comme le tableau de bord il peut naviguer dans les offre
le parsing est degueu il cool e trois fois le meme texte full de l''offre dans lse trois sectin responsabilities skill keywords.
je ne vois pas de button qui selectionne le job dans la rubrique neda attention je ne vois aps comment ni pourquoi un doc job peut etre dans need attention. 
j'ai besoin d'un audit sur le potentiel de cet page tout en respectant les kpi e. le benchmark matrix et mes observation , rien n'est une regle immuable mais je veux comrend la direction je supervis c qui est impletent je teste je critique tu dois faire pareil 
---

## En cours

- [x] **Stabiliser la vérité canonique** — aligner rendus, JSON copiés/exports et vues dérivées sur `sections[*].structuredContent`.
- [x] **IDENTITY/CONTACT POC hybride** — fixs acceptés déjà documentés, ne pas rouvrir sans contradiction live.
- [ ] ##add paper color
- [ ] add @TYPOGRAPHY MODE dans les instruction FIX du menu ai de reecriture, ajouter aussi a workspace si c'est possible
- [ ] replace all resume, all proposal par show more, ou show all. 

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

- [x] **Scroll/zoom preview CV** — scroll bloqué en mode zoom, pas de pan à 100% fit. ✅ 2026-04-18
- [ ] desired position is not being parsed correctly is pretty much all the time absent
- [ ] when website is loaded i get a pop up card renam this cv imported cv, this modal is a symptom of a bug taht shoud be fixed its loading everytime import cv is refreshed or somthing
- [x] HOBBBIE SHOWING ONLY 2 ENTRIES, EVEN WHE THERE IS MORE ✅ 2026-04-22
- [ ] HIGHLIGHT SELECTED TEXT HAS NO STYLE ITS INVISIBLE IN LIGHT AND DARK MODE
- [ ] replace teh plus add icon in skill section in cv forge with a pen
- [ ] WHEN ENTERING NO DESIRED POSITION, saving keep. last sate entry
      jessica claire still show in desired position 
- [ ] 
- [x] **Achievements encore visible dans Manage Section** — incohérence alors que la section est déjà chargée. ✅ 2026-04-18
- [ ] quickstart jump of one line between start and cover letter slides, button is wider in start,cv than in covver letter
- [ ] assign 3default style for new users it should never be empty
- [ ] verify if proposal are saved in the library. and persistent. in convex. make autosave default for generated proposal. 
- [ ] export ats and exportpd  style and docx should be accesible from the library proposal
- [ ] align `./run.sh local-convex` alias behavior with `local-fast`, or deprecate the alias explicitly in code and docs
- [ ] update title in the toolbar browser title when cv is imported/uploaded, or manual cv when u enter name is profile
- [ ] on refresh cv prview the mock up cv iappear flikcering with the real imported cv , when u hit refresh page
- [x] les gros texte dans les section type experience des entry ne sont pas affiché apres un certain seuil(hardcodé?) le saut de la page a section suivante laisse enorme marge bottom, valbale pour autre section too.. ✅ 2026-04-22
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

- revoir le copywrite, changer le nom de quickstart, ameliorer brandvoice, relire quickstart rubrique, creer landing page
- - Show error toast/message on failure
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
