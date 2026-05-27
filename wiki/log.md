---
title: "Log — twoweeks Wiki"
category: overview
updated: 2026-05-27
---

# Log du Wiki · twoweeks

Journal chronologique append-only de toutes les opérations sur le wiki.

```bash
grep "^## \[" wiki/log.md | tail -5   # Dernières 5 entrées
grep "^## \[" wiki/log.md | grep "ingest"  # Tous les ingests
```

---

## [2026-05-27] direct-update | docx layout parity follow-up backlog entry

**Agent** : Codex
**Mode** : direct-update
**Pages créées** :
- `wiki/tasks/docx-layout-parity-follow-up.md`
**Pages mises à jour** :
- `wiki/tasks/kanban.md`
- `wiki/index.md`
- `wiki/hot.md`
- `wiki/log.md`
**Points notables** :
- Recorded the merged DOCX document-language metadata work as complete.
- Added a deferred follow-up page for Arabic RTL layout parity, bullets, tables, and font strategy so the next work item is discoverable without reopening the completed metadata slice.
- Updated the hot cache and index/task catalog to point at the deferred follow-up rather than the merged metadata work.

## [2026-05-26] direct-update | proposal language hardening final state

**Agent** : Codex
**Mode** : direct-update
**Pages créées** :
- aucune
**Pages mises à jour** :
- `wiki/strategy/language-localization.md`
- `wiki/tech/proposal-ai-routing-and-inline-diff.md`
- `wiki/outputs/2026-05-26-proposal-language-generation-hardening.md`
- `wiki/hot.md`
- `wiki/log.md`
**Points notables** :
- Recorded final merged status for PR #58/#59/#60 in the proposal language hardening chain.
- Added explicit policy: unsupported exact numeric/duration/credential/ownership/operational claims remain hard-blocks in production, while vague timeline claims stay repair-first.
- Recorded that job title/job description are not candidate-proof sources for numeric/duration authorization.
- Preserved the `en`/`fr`/`es` UI scope and document-first rollout for additional language support (`de`, `ru`, `pl`, `ar`).
- Confirmed no page creation and no index reclassification was required in this pass.

---

## [2026-05-26] direct-update | proposal language pipeline hardening checkpoint

**Agent** : Codex
**Mode** : direct-update
**Pages créées** :
- `wiki/outputs/2026-05-26-proposal-language-generation-hardening.md`
**Pages mises à jour** :
- `wiki/index.md`
- `wiki/hot.md`
- `wiki/strategy/language-localization.md`
- `wiki/log.md`
**Points notables** :
- Captured the current language-generation state: UI layer still `en`/`fr`/`es`; document languages broader and independent (`de`, `ru`, `ar`, `pl`).
- Recorded that deterministic English fallback prose is blocked for non-`en`/`fr` document languages in proposal helper paths under the hardening pass.
- Added a forward-looking note for optional future document candidates (`zh`, `ta`) after QA evidence threshold is met.
- Confirmed hot/index/log consistency after this mutation.

---

## [2026-05-26] direct-update | proposal planner chain-of-thought documentation

**Agent** : Codex
**Mode** : direct-update
**Pages mises à jour** :
- `wiki/product/ai-product-model.md`
- `wiki/index.md`
- `wiki/hot.md`
**Points notables** :
- Added the Planner Agent chain-of-thought text verbatim to product documentation as the canonical shadow planner reasoning order.
- Added cross-references in wiki hot cache and retrieval index so the Planner Agent chain is discoverable.
- Linked [[product/ai-product-model]] to the existing source evidence: `sources/2026-05-25-proposal-generation-truth-planner`.

---

## [2026-05-26] ingest | language localization strategy reference

**Agent** : Codex
**Mode** : ingest
**Fichiers traités** :
- `rawinput/Two Weeks Language Map — Reference Note.md`
**Fichiers non traités** :
- `rawinput/emojis library .md` (intentionnellement ignoré)
**Pages créées** :
- `wiki/sources/2026-05-26-two-weeks-language-map-reference-note.md`
- `wiki/strategy/language-localization.md`
**Pages mises à jour** :
- `wiki/index.md`
- `wiki/hot.md`
- `wiki/log.md`
**Pages archivées** :
- aucune
**Points notables** :
- La note de langage est ingérée comme source de stratégie et déployée dans `wiki/strategy/language-localization.md`.
- Le fichier traité a été déplacé vers `raw/2026-05-26-two-weeks-language-map-reference-note.md` pour immutabilité `raw/`.
- La bibliothèque d’emojis n’a pas été ingérée par demande.

---

## [2026-05-25] ingest | proposal truth and theme palette ingest

**Agent** : Codex
**Mode** : ingest
**Fichiers traités** :
- `rawinput/Proposal Generation Truth Planner.md`
- `rawinput/light and dark theme two weeks .md`
**Pages créées** :
- `wiki/sources/2026-05-25-proposal-generation-truth-planner.md`
- `wiki/sources/2026-05-25-two-weeks-theme-palette.md`
**Mise à jour des pages** :
- `wiki/index.md`
- `wiki/hot.md`
- `wiki/log.md`
**Points notables** :
- Les nouvelles entrées de `rawinput/` ont été ingérées en tant que sources.
- Dédoublonnage vérifié : aucun duplicate exact n’a été trouvé dans `wiki/sources/`.
- Les fichiers ont été déplacés vers `raw/` avec conservation de l’original.
- `rawinput/` repasse à vide (hors `README.md`).
**Référence ingest** : `raw/` immuable.

---

## [2026-05-21] direct-update | shared command-layer parity for CV/Proposal toolbar + Ask

**Agent** : Codex
**Mode** : direct-update
**Pages créées** :
- `wiki/sources/2026-05-21-cv-proposal-command-layer-unification-note.md`
**Pages mises à jour** :
- `my-app/src/hooks/use-document-command-layer-position.ts`
- `my-app/src/lib/document-command-layer-layout.ts`
- `my-app/src/pages/CvForge.tsx`
- `my-app/src/pages/ProposalForge.tsx`
- `my-app/src/styles/product-cv.css`
- `my-app/src/styles/product-proposal.css`
- `my-app/src/styles/foundation.css`
- `my-app/src/styles/product.css`
- `my-app/src/components/__tests__/CvForgeToolbar.css.test.ts`
- `my-app/src/components/__tests__/ProposalDisplay.css.test.ts`
- `my-app/src/hooks/__tests__/use-document-command-layer-position.test.tsx`
- `my-app/src/lib/__tests__/document-command-layer-layout.test.ts`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`
**Points notables** :
- Unifie la logique de positionnement/densité du command-layer (toolbar + Ask) entre CV Forge et Proposal Forge via logique partagée (`use-document-command-layer-position` / `document-command-layer-layout`).
- Supprime les déviations CV-only qui causaient labels persistants à faible zoom, offsets Ask séparés et sauts de handle.
- Préserve les garde-fous de qualité: même comportement de mode compact/ultra et de sticky `commandLayerY` pour les deux surfaces.
- Garde la sémantique zoom CV intouchée (valeur utilisateur inchangée), en appliquant le rétrécissement uniquement par tokens de densité partagée.

---

## [2026-05-20] direct-update | topbar tokenized chrome alignment

**Agent** : Codex
**Mode** : direct-update
**Pages créées** :
- Aucune
**Pages mises à jour** :
- `my-app/src/styles/foundation.css`
- `my-app/src/styles/product.css`
- `my-app/src/components/__tests__/SidebarVisual.css.test.ts`
- `my-app/src/components/__tests__/ProposalDisplay.css.test.ts`
- `wiki/design/document-token-contract.md`
- `wiki/tech/proposal-forge-document-geometry.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`
**Points notables** :
- Définition explicite de la tokenisation topbar dans le contrat design pour stabiliser les métriques des contrôles (hauteur, gap, padding, alignement).
- Ajout de la règle “topbar commune” dans `proposal-forge-document-geometry` : les contrôles de toolbar sont gouvernés par les tokens app-topbar de `foundation.css`, pas des literals locaux.
- Mise à jour de la page de focus/chaleur (`hot.md`) avec la règle d’alignement CV/Proposal des contrôles, pour mémoire opérationnelle partagée.

## [2026-05-11] direct-update | CV ATS audit heuristic note ingested

**Agent** : Codex
**Mode** : direct-update
**Pages créées** :
- `wiki/tech/cv-ats-audit-heuristic.md`
**Pages mises à jour** :
- `wiki/index.md`
- `wiki/hot.md`
- `wiki/log.md`
**Points notables** :
- Ajoute la note technique V1 sur l'évaluation ATS heuristique CV (`evaluateCvAtsAudit`) et ses contraintes (heuristique, non parser-compatible ATS réel).
- Documente : seuils (excellent/good/needs_review/blocked), catégories, poids, fallback sur `cv.sections` quand le modèle export normalisé de confiance manque, et cas bloquants (`missing-cv`, `unresolved-import-review`).

## [2026-05-08] direct-update | ui audit proposal-polish snapshot

**Agent** : Codex
**Mode** : direct-update
**Pages créées** :
- `wiki/outputs/2026-05-08-ui-audit-proposal-polish.md`
**Pages mises à jour** :
- `wiki/index.md`
- `wiki/hot.md`
- `wiki/log.md`
**Points notables** :
- Ingest du recap UI audit en output snapshot non canonique.
- Conserve les valeurs CSS vérifiées séparément et marque le reste comme subjectif / screenshots only.
- Classe le diagnostic comme utile pour la direction design, mais pas comme source de vérité absolue.

## [2026-05-08] direct-update | proposal signature legacy artefact note

**Agent** : Codex
**Mode** : direct-update
**Pages mises à jour** :
- `wiki/tech/proposal-signature-closing-layer.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`
**Mise à jour technique associée (repo)** :
- `commit 9ed81aa9`
**Points notables** :
- Documente le comportement cible en edit/preview pour la signature structurée (edit = corps texte uniquement, signature = métadonnée/rendu).
- Ajoute la liste des artefacts legacy encore observés (`Warm regards`, nom en signature textuel) et leurs impacts connus.
- Ajoute des recommandations de migration: nettoyage legacy au chargement, sanitization du draft chargé, et test e2e ciblé sur ancienne proposition.
- Note que le flux manuscrit/image doit rester une couche de rendu (preview/print/export), jamais éditable dans le texte.

## [2026-05-08] direct-update | shared custom style color pipeline

**Agent** : Codex
**Mode** : direct-update
**Pages mises à jour** :
- `wiki/tech/proposal-style-layer.md`
- `wiki/index.md`
- `wiki/hot.md`
- `wiki/log.md`
**Mise à jour technique associée (repo)** :
- `my-app/src/pages/SettingsPage.tsx`
- `my-app/src/components/cv/CvRail.tsx`
- `my-app/src/pages/CvForge.tsx`
**Points notables** :
- Documente Custom comme septième option d'accent dans Settings, CV Forge, et Proposal Forge.
- Clarifie que Custom n'est pas un `paletteOverride` nommé: il persiste via `palette: "custom"` et `accentHex`.
- Note que sélectionner une couleur nommée doit effacer l'accent custom, tandis que sélectionner Custom conserve le slot de style courant en état personnalisé.
- Ajoute la règle de reset: Settings restaure le slot aux defaults factory sans déplacer le default actif; CV Forge reset vers le slot Settings utilisateur quand il existe.

## [2026-05-08] direct-update | proposal style default-slot semantics note

**Agent** : Codex
**Mode** : direct-update
**Pages mises à jour** :
- `wiki/tech/proposal-style-layer.md`
- `wiki/index.md`
- `wiki/hot.md`
- `wiki/log.md`
**Mise à jour technique associée (repo)** :
- `my-app/src/pages/SettingsPage.tsx`
- `my-app/convex/proposalSettings.ts`
**Points notables** :
- Clarifie la différence entre slot content and active default: editing a style slot does not make it default.

## [2026-05-08] direct-update | proposal signature closing structured pipeline note

**Agent** : Codex
**Mode** : direct-update
**Pages créées** :
- `wiki/tech/proposal-signature-closing-layer.md`
**Pages mises à jour** :
- `wiki/index.md`
- `wiki/hot.md`
- `wiki/log.md`
**Mise à jour technique associée (repo)** :
- `my-app/src/lib/proposal-closing.ts`
- `my-app/src/lib/proposal-output-draft.ts`
- `my-app/src/lib/document-export-models.ts`
- `my-app/src/components/proposal-render/ProposalDocumentRenderer.tsx`
- `my-app/src/pages/ProposalForge.tsx`
- `my-app/src/pages/ProposalPrintPage.tsx`
- `my-app/src/components/ProposalDisplay.tsx`
- `my-app/src/components/ProposalsList.tsx`
- `my-app/convex/schema.ts`
- `my-app/convex/createProposalPublic.ts`
- `my-app/convex/updateProposalPublic.ts`
- `my-app/convex/proposalsPublic.ts`
**Points notables** :
- Note de plan ajoutée dans le wiki sur la frontière Signature/Closing (pas de pipeline Python dédié; le flux actif est TypeScript + Convex + renderers).
- Résumé du plan `plans/proposal-structured-closing.md` intégré en mode "started": métadonnée close structurée, fallback legacy, et propagation preview/print/export.
- Le contrôle UI avancé (toggle/override dédié) reste planifié après stabilisation de la persistance et des tests de parité.
- Records the explicit `Set as default` control as the only action that should move the active default badge.
- States the intended rule for new docs: start from the active default slot when no more specific document style exists.

## [2026-05-08] direct-update | proposal style layer live-boundary scratchpad

**Agent** : Codex
**Mode** : direct-update
**Pages mises à jour** :
- `wiki/tech/proposal-style-layer.md`
- `wiki/index.md`
- `wiki/hot.md`
- `wiki/log.md`
**Mise à jour technique associée (repo)** :
- `my-app/convex/proposalSettings.ts`
- `my-app/convex/schema.ts`
**Points notables** :
- Enregistre le vrai cause/résolution du bug live: `savePreset` faisait un fan-out sur tous les `userProfiles` du même Clerk, ce qui dépassait la limite de lecture Convex et empêchait la sauvegarde.
- Clarifie que le Style 2 natif reste `quiet-editorial` avec le template CV Workshop deux colonnes.
- Oriente le diagnostic vers les champs persistés `proposalPreset2`, `proposalFontPairId`, et `proposalVerbatiStyle.typography` si l'UI affiche encore Parisienne/Cormorant.

## [2026-05-08] direct-update | document style slot live-boundary trace

**Agent** : Codex
**Mode** : direct-update
**Pages mises à jour** :
- `wiki/tech/proposal-style-layer.md`
- `wiki/hot.md`
- `wiki/log.md`
**Mise à jour technique associée (repo)** :
- Style slot debugging in app worktree, uncommitted
**Points notables** :
- Documente que Style 1/2/3 traverse trois frontières gagnantes: factory slots, Settings/CV Forge presets, et Proposal Forge current settings.
- Note que `studio-grotesk` / Parisienne-Cormorant ne vient pas des factory slots actuels et pointe plutôt vers un preset Convex ou un champ current settings persisté.

## [2026-05-07] direct-update | workshop two-column resume pagination

**Agent** : Codex
**Mode** : direct-update
**Pages mises à jour** :
- `wiki/tech/workshop-pagination.md`
- `wiki/hot.md`
- `wiki/log.md`
**Mise à jour technique associée (repo)** :
- Branch app `new-layout`
**Points notables** :
- Étend la vérité Workshop pagination aux templates planner-backed `workshop_resume_onecol_ats` et `workshop_resume_twocol_ats`.
- Préserve `committedPages` comme autorité des page breaks preview/print/export.
- Documente que le placement des colonnes two-column reste local au renderer sauf preuve browser mesurée.

## [2026-05-07] direct-update | proposal forge document geometry canon

**Agent** : Codex
**Mode** : direct-update
**Pages créées** :
- `wiki/tech/proposal-forge-document-geometry.md`
**Pages mises à jour** :
- `wiki/index.md`
- `wiki/log.md`
- `wiki/hot.md`
**Mise à jour technique associée (repo)** :
- Commit app `f0e9208e fix(proposal): canonicalize workspace paper width`
- Commit app `93c093ae fix(proposal): align edit scrollbar with page edge`
**Points notables** :
- Documente le canon page-first Proposal Forge: `--proposal-paper-visual-inline-size` comme autorité de largeur visible.
- Clarifie l'alignement toolbar/panel/shell/stage/viewport autour du breakpoint 1420px.
- Définit la séparation page width vs reading measure et le placement des scrollbars preview/edit au bord de page.
- Ajoute un prompt guardrail réutilisable pour agents LLM travaillant sur cette surface.

## [2026-05-06] direct-update | proposal AI routing and inline diff overlay

**Agent** : Codex
**Mode** : direct-update
**Pages créées** :
- `wiki/tech/proposal-ai-routing-and-inline-diff.md`
**Pages mises à jour** :
- `wiki/index.md`
- `wiki/log.md`
- `wiki/hot.md`
**Mise à jour technique associée (repo)** :
- `docs/decisions/2026-05-06-proposal-ai-selector-and-inline-diff-overlay.md`
- `my-app/config/llmConfig.ts`
- `my-app/convex/lib/editorAi.ts`
- `my-app/convex/generateProposalMutation.ts`
- `my-app/convex/langchain/models/openai_responses_adapter.ts`
- `my-app/convex/lib/proposals/premiumCoverLetter.ts`
- `my-app/src/components/ProposalInputForm.tsx`
- `my-app/src/components/ProposalDisplay.tsx`
- `my-app/src/styles/product-proposal.css`
**Points notables** :
- Proposal generation remains on OpenAI `gpt-5.5`; the proposal form now honors env-driven default model overrides.
- Helper toolbar actions now route through Qwen first, with `fix_grammar` on `qwen-3.6-flash` and Mistral/DeepSeek fallbacks.
- Proposal text suggestions now render inline as an overlay diff rather than a detached suggestion card.
- Job summary and keyword match synthesis is on the Ministral/Mistral path, currently defaulting to `ministral-3-3b-instruct-2512`.

## [2026-05-06] direct-update | proposal style layer scratchpad

**Agent** : Codex
**Mode** : direct-update
**Pages créées** :
- `wiki/tech/proposal-style-layer.md`
**Pages mises à jour** :
- `wiki/index.md`
- `wiki/log.md`
- `wiki/hot.md`
**Mise à jour technique associée (repo)** :
- Commit app `ccbc4280 fix: stabilize proposal style customization`
**Points notables** :
- Documente le modèle Style 1/2/3 comme base durable avec état `Custom` pour les changements couleur/police/layout.
- Définit les palettes actives nommées `terre`, `cobalt`, `ink`, `sauge`, `plum`, `ochre`; les ids legacy restent lisibles seulement.
- Note les commandes de vérification Vitest/TypeScript à relancer pour cette couche.

## [2026-05-04] direct-update | CV Forge docs sync for paper width and AI routing

**Agent** : Codex
**Mode** : direct-update
**Pages mises à jour** :
- `wiki/sources/2026-04-30-cv-forge-pr4-remaining-tasks.md`
- `wiki/tasks/kanban.md`
- `wiki/hot.md`
- `wiki/index.md`
**Mise à jour technique associée (repo)** :
- `docs/plans/2026-03-21-ui-next-steps-todo.md`
- `docs/audits/2026-05-04-cv-forge-paper-width-and-ai-routing.md`
**Points notables** :
- Synchronisation de la doc active avec l’état live du CV Forge: edit et preview partagent maintenant le même paper width canonique (860px), sans stage compact.
- Alignement du helper AI CV Forge sur `mistral-small-latest` pour summary/custom et suggestion actions.
- Parité rich-summary conservée dans le renderer partagé; la paper editing complète reste partiellement différée.

## [2026-05-04] direct-update | e2e modal selector hardening for cvforge preview linking

**Agent** : Codex
**Mode** : direct-update
**Pages mises à jour** :
- `wiki/hot.md`
- `wiki/tasks/kanban.md`
- `wiki/sources/2026-04-30-cv-forge-pr4-remaining-tasks.md`
**Mise à jour technique associée (repo)** :
- `e2e/cvforge-preview-linking.spec.ts`
- `docs/plans/2026-03-21-ui-next-steps-todo.md`
- `docs/audits/2026-05-04-verbati-style-metadata-persistence-hardening.md`
**Points notables** :
- Résolution de fragilité Playwright: remplacement des assertions de nom exact de dialogue par assertions sur le heading (`Profile`, `Projects`, `Experience`, etc.) + fermeture via `button[aria-label="Close panel."]`.
- Fixe du seed test en forçant explicitement le mode preview via `dasti:cv-forge-workspace-mode:v1=preview`.
- Vérification: `rtk npx playwright test e2e/cvforge-preview-linking.spec.ts --project=chromium --grep "keeps modal targets in preview mode and routes aliases correctly"`.

## [2026-05-04] direct-update | CV style persistence hardening and guardrail documentation

**Agent** : Codex
**Mode** : direct-update
**Pages mises à jour** :
- `wiki/tasks/kanban.md`
- `wiki/sources/2026-04-30-cv-forge-pr4-remaining-tasks.md`
- `wiki/hot.md`
**Mise à jour technique associée (repo)** :
- `docs/audits/2026-05-04-verbati-style-metadata-persistence-hardening.md` (repo)
**Points notables** :
- Les sauvegardes style-only CV sont désormais routées vers une mutation Convex de métadonnées (`metadata.verbatiStyle`) sans `cvDocument`.
- Un garde-fou backend évite la création de ligne `userProfiles` quand le patch style est `metadata` only.
- Les tests de vérification incluent :
  - `my-app/convex/__tests__/profiles.patch.test.ts`
  - `my-app/src/adapters/__tests__/StorageAdapter.test.ts`
  - `src/features/verbati/__tests__/useBoundVerbatiCvStyle.test.tsx`
  - `src/features/verbati/__tests__/VerbatiCvPreviewPanel.test.tsx`
  - `src/features/verbati/__tests__/VerbatiCvPreviewPanel.workspace-style-cycle.test.tsx`

## [2026-05-04] ingest | rawinput ingest + task sync

**Agent** : Codex
**Fichiers traités** :
- `rawinput/2026-04-30-cv-forge-pr4-remaining-tasks 1.md`
- `rawinput/2026-04-30-cv-forge-pr4-remaining-tasks.md`
- `rawinput/2026-04-30-jobs-language-localization-scratchpad.md`
- `rawinput/refonte wiki claude-obsidian.md`
- `rawinput/two-weeks app skeleton -skill.md`
**Pages créées** :
- `wiki/sources/2026-04-30-cv-forge-pr4-remaining-tasks.md`
- `wiki/sources/2026-04-30-jobs-language-localization-scratchpad.md`
- `wiki/sources/2026-04-30-refonte-wiki-claude-obsidian.md`
- `wiki/sources/2026-04-30-two-weeks-app-skeleton-skill.md`
**Pages mises à jour** :
- `wiki/tasks/kanban.md`
- `wiki/index.md`
- `wiki/log.md`
**Points notables** :
- Toutes les entrées de `rawinput/` ont été ingérées et déplacées vers `raw/`.
- Dédoublonnage `cv-forge-pr4-remaining-tasks` : la version `... 1.md` (plus récente) a été conservée comme source principale.
- `wiki/tasks/kanban.md` a reçu un suivi PR4 plus explicite (actions en cours de confirmation).
- `wiki/index.md` mis à jour avec 4 nouvelles sources `2026-04-30-*`.

## [2026-05-02] direct-update | active memory gateway for LLM retrieval

**Agent** : Codex
**Pages créées** :
- `wiki/hot.md`
- `wiki/howto/wiki-commands-and-llm-export.md`
**Pages mises à jour** :
- `AGENTS.md`
- `WIKI_SCHEMA.md`
- `CLAUDE.md`
- `README.md`
- `SKILL.md`
- `skills/ingest-wiki/SKILL.md`
- `/Users/pana/.codex/skills/ingest-wiki/SKILL.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`
- `wiki/tasks/coffee talk.md`
**Points notables** :
- `wiki/hot.md` devient le cache actif non canonique pour retrieval LLM rapide
- `wiki/index.md` garde la carte canonique et reçoit une Retrieval Map courte
- les workflows doivent lire `hot.md` avant d'élargir vers `index.md` et pages durables
- `AGENTS.md`, `README.md` et le howto donnent un prompt court pour les agents futurs
- `README.md` pointe maintenant vers `hot.md` dans le démarrage wiki
- `coffee talk.md` contient la commande courte pour synchroniser la skill Codex collaborateur
- `wiki/howto/wiki-commands-and-llm-export.md` sauvegarde les commandes wiki et le plan `wiki/llms.txt`

## [2026-04-28] direct-update | AI Consistency P0 closure audit note

**Agent** : Codex
**Pages créées** :
- `wiki/product/ai-consistency-p0-editor-ai.md`
**Pages mises à jour** :
- `wiki/index.md`
- `wiki/log.md`
**Points notables** :
- closure audit snapshot for PRs #42 to #45
- status updated to implemented / audited / follow-up hardening pending
- dev docs mention added for `./run.sh local-fast`, `./run.sh tunnel`, and `./run.sh reload-env`

## [2026-04-12] ingest | Brand Bible twoweeks.ai 2026

**Agent** : Claude
**Fichiers traités** : `rawinput/twoweeks-brand-bible.md`
**Pages créées** :
- `wiki/sources/2026-04-12-twoweeks-brand-bible.md`
- `wiki/entities/twoweeks.md` — entité principale corrigée (nom réel du produit)
- `wiki/concepts/brand-voice.md` — voix staccato, Corporate Noir, règles copie UI
**Pages archivées** :
- `wiki/entities/cv-forge.md` → `wiki/archive/entities/cv-forge.md` (supersédée par twoweeks)
**Mises à jour** :
- `CLAUDE.md` — description app mise à jour : twoweeks.ai, tagline, positionnement, modules
- `wiki/timeline.md` — event Supersede cv-forge → twoweeks
- `wiki/index.md` — section Archive ajoutée, stats mises à jour

---

## [2026-04-12] ingest | Runbook tunnel Cloudflare + note pipeline import OCR

**Agent** : Claude
**Fichiers traités** : `rawinput/howto_tunnel.md`, `rawinput/pipeline note.md`
**Pages créées** :
- `wiki/howto/cloudflare-zero-trust-tunnel.md`
- `wiki/tech/import-ocr-pipeline.md`

---

## [2026-04-12] structure | Nouveaux répertoires tech/ howto/ kanban + récupération pages manquantes

**Agent** : Claude
**Pages créées** :
- `wiki/to do list/kanban.md`
- `wiki/concepts/parsing-poc-progress.md`
- `wiki/sources/2026-04-11-cv-parsing-poc-state.md`
- `wiki/sources/2026-04-11-todo-sprint.md`
- `wiki/sources/2026-04-11-jessica-helen-poc-state.md`
**Mises à jour** : `wiki/index.md`, `CLAUDE.md`

---

## [2026-04-11] decision | Finding stockage Convex — cvDocument est la source de vérité

**Agent** : Claude
**Pages mises à jour** : `wiki/entities/cv-forge.md` (archivé depuis) — architecture de stockage Convex documentée. `userProfiles.cvDocument` est la source de vérité. Les champs top-level `experience[]`, `education[]`, `skills[]` sont legacy et vides.

---

## [2026-04-11] ingest | CV Parsing POC State + Sprint Notes

**Agent** : Claude
**Fichiers traités** : `rawinput/2026-04-11-cv-parsing-poc-state.md`, `rawinput/to do.md`
**Pages créées** : sources/2026-04-11-cv-parsing-poc-state.md, sources/2026-04-11-todo-sprint.md, concepts/parsing-poc-progress.md
**Pages mises à jour** : concepts/cv-parsing-pipeline.md, entities/cv-forge.md (archivé depuis)

---

## [2026-04-10] decision | Refonte système de tones — 4 tones avec Auto

**Agent** : Claude
**Décision** : Remplacer Balanced/Warm/Formal par Auto/Natural/Formal/Warm. Auto = mode recommandé par défaut, analyse l'offre d'emploi et choisit le tone automatiquement.
**Pages mises à jour** : concepts/ai-product-model.md, entities/cv-forge.md (archivé depuis), concepts/product-vision.md, wiki/timeline.md

---

## [2026-04-10] ingest | Gap Analysis — diagnostic vs ResumeLab, priorités, 3 cycles

**Agent** : Claude
**Fichiers traités** : `rawinput/3_gap_analysis.md`
**Pages créées** : concepts/gap-analysis.md, sources/2026-04-10-gap-analysis.md

---

## [2026-04-10] ingest | Benchmark Matrix + Success Blueprint — scoring, vision, IA

**Agent** : Claude
**Fichiers traités** : `rawinput/1_ideal_benchmark_matrix.md`, `rawinput/2_success_blueprint.md`
**Pages créées** : concepts/benchmark-matrix.md, concepts/product-vision.md, concepts/ai-product-model.md, concepts/kpis.md, sources/2026-04-10-benchmark-matrix.md, sources/2026-04-10-success-blueprint.md

---

## [2026-04-10] ingest | Notion Roadmap CV Forge — phases, KPIs, décisions produit

**Agent** : Claude
**Fichiers traités** : `rawinput/6_NOTION_ROADMAP.MD`
**Pages créées** : concepts/product-roadmap.md, sources/2026-04-10-notion-roadmap-cvforge.md

---

## [2026-04-09] ingest | Décisions sprint CV Forge — parser, features, bugs

**Agent** : Claude
**Fichiers traités** : `rawinput/`
**Pages créées** : entities/cv-forge.md (archivé depuis), concepts/cv-parsing-pipeline.md, concepts/cv-families.md, sources/2026-04-09-decisions-cvforge-sprint.md, sources/2026-04-09-tweet-karpathy-llm-wiki.md, sources/2026-04-09-wiki-paste-llm-wiki.md

---

## [2026-04-09] init | Création du vault twoweeks

Initialisation du vault Obsidian + schema LLM wiki v1.

---

## [2026-04-09] architecture | Migration v1 → v2 : rawinput/ + gestion temporelle

Migration vers schema v2 : ajout rawinput/ (staging), gestion temporelle (status/horizon/version/superseded_by), wiki/archive/, wiki/timeline.md.

## [2026-04-14] ingest | ATS, parser canonical truth, local/cloud modes, extension, kanban

**Agent** : Codex
**Fichiers traités** : `rawinput/ATS COMPLIANT SCORE.md`, `rawinput/Local dev server vs Remote dev server Architecture.md`, `rawinput/run.sh launching commands for the app.md`, `rawinput/clerk chrome extension specs addon.md`, `rawinput/ARCHITECTURE PARSIN MISTRAL.md`, `rawinput/Docker commands.md`, `rawinput/kanban.md`
**Pages créées** :
- `wiki/sources/2026-04-14-ats-compliant-score.md`
- `wiki/sources/2026-04-14-local-dev-vs-remote-parser-architecture.md`
- `wiki/sources/2026-04-14-run-sh-modes.md`
- `wiki/sources/2026-04-14-clerk-chrome-extension-addon.md`
- `wiki/sources/2026-04-14-structured-parsing-canonical-truth.md`
- `wiki/sources/2026-04-14-docker-commands.md`
- `wiki/sources/2026-04-14-kanban-sprint-notes.md`
- `wiki/concepts/ats-safety.md`
- `wiki/concepts/cv-parsing-pipeline.md`
- `wiki/concepts/cv-families.md`
- `wiki/tech/local-vs-remote-parser-architecture.md`
- `wiki/howto/local-parser-operations.md`
**Pages mises à jour** :
- `wiki/overview.md`
- `wiki/entities/twoweeks.md`
- `wiki/tech/import-ocr-pipeline.md`
- `wiki/to do list/kanban.md`
- `wiki/timeline.md`
- `wiki/index.md`
**Pages archivées** :
- aucune

## [2026-04-14] ingest | run.sh quick note — main dev entrypoint

**Agent** : Codex
**Fichiers traités** : `rawinput/RUN.SH QUICK NOTE.md`
**Pages créées** :
- `wiki/sources/2026-04-14-run-sh-quick-note.md`
**Pages mises à jour** :
- `wiki/howto/APP-launcher-command.md`
- `wiki/tech/local-vs-remote-parser-architecture.md`
- `wiki/tech/import-ocr-pipeline.md`
- `wiki/entities/twoweeks.md`
- `wiki/concepts/parsing-poc-progress.md`
- `wiki/to do list/kanban.md`
- `wiki/howto/cloudflare-zero-trust-tunnel.md`
- `wiki/overview.md`
- `wiki/timeline.md`
- `wiki/index.md`
**Pages archivées** : aucune

## [2026-04-15] ingest | locale typography rules + French/English scratch pads

**Agent** : Codex
**Fichiers traités** : `rawinput/TYPOGRAPHY MODE.md`, `rawinput/FRENCH TYPOGRAPHY SCRATCH PAD.md`, `rawinput/ENGLISH TYPOGRAPHY SCRATCH PAD.md`
**Pages créées** :
- `wiki/sources/2026-04-15-typography-mode.md`
- `wiki/sources/2026-04-15-french-typography-scratch-pad.md`
- `wiki/sources/2026-04-15-english-typography-scratch-pad.md`
- `wiki/sources/2026-04-15-conversation-locale-typography-rules.md`
- `wiki/design/locale-typography-rules.md`
**Pages mises à jour** :
- `wiki/design/a4-layout-systems.md`
- `wiki/design/brand-voice.md`
- `wiki/tech/export-pipeline.md`
- `wiki/index.md`
- `wiki/log.md`
**Pages archivées** :
- aucune

## [2026-04-18] direct-update | Mistral Resume V3 section recovery refresh

**Agent** : Codex
**Références revues** : `cv_parser_service/mistral_resume_v3/section_headings.py`, `cv_parser_service/mistral_resume_v3/pipeline.py`, `cv_parser_service/mistral_resume_v3/post_validation.py`, `cv_parser_service/tests/test_mistral_resume_v3_pipeline.py`
**Pages mises à jour** :
- `wiki/sources/2026-04-15-mistral-resume-v3-section-recovery-scratchpad.md`
- `wiki/tech/import-ocr-pipeline.md`
- `wiki/concepts/cv-parsing-pipeline.md`
- `wiki/index.md`
- `wiki/log.md`
**Points notables** :
- alias `experience` multilingues maintenus explicitement
- split des headings composés borné aux séparateurs sûrs
- validation post-recovery et retry unique conservés via `section_evidence_contradiction`

## [2026-04-18] ingest | Quick Start module hierarchy

**Agent** : Codex
**Fichiers traités** : `rawinput/Quick Start Module Hierarchy.md`
**Pages créées** :
- `wiki/sources/2026-04-18-quick-start-module-hierarchy.md`
- `wiki/tech/quick-start-module-hierarchy.md`
**Pages mises à jour** :
- `wiki/product/product-roadmap.md`
- `wiki/strategy/gap-analysis.md`
- `wiki/overview.md`
- `wiki/index.md`
- `wiki/log.md`
**Pages archivées** :
- aucune
**Points notables** :
- Quick Start est un état d'app-shell content-pane, pas une modale
- le cold start cover-letter reste un état d'entrée intentionnel dans `/proposal`
- la primitive de carte partagée reste commune aux chemins resume et cover-letter
- l'onboarding de première session demeure le reliquat principal

## [2026-04-14] ingest | export pipeline brief — OCR to ATS / styled output

**Agent** : Codex
**Fichiers traités** : `rawinput/Export Pipeline Brief  OCR to ATS Styled Output.md`
**Pages créées** :
- `wiki/sources/2026-04-14-export-pipeline-brief-ocr-to-ats-styled-output.md`
- `wiki/tech/export-pipeline.md`
**Pages mises à jour** :
- `wiki/tech/import-ocr-pipeline.md`
- `wiki/concepts/cv-parsing-pipeline.md`
- `wiki/concepts/ats-safety.md`
- `wiki/entities/twoweeks.md`
- `wiki/overview.md`
- `wiki/index.md`
**Pages archivées** : aucune

## [2026-04-15] ingest | parser recovery scratchpad + run.sh workspace modes + section detection note

**Agent** : Codex
**Fichiers traités** : `rawinput/Mistral Resume V3 Section-Recovery Scratchpad.md`, `rawinput/run.sh\` LLM Scratchpad.md`, `rawinput/section detection.md`
**Pages créées** :
- `wiki/sources/2026-04-15-mistral-resume-v3-section-recovery-scratchpad.md`
- `wiki/sources/2026-04-15-run-sh-workspace-modes.md`
- `wiki/sources/2026-04-15-section-detection-future-note.md`
- `wiki/howto/local-parser-operations.md`
**Pages mises à jour** :
- `wiki/concepts/cv-parsing-pipeline.md`
- `wiki/tech/import-ocr-pipeline.md`
- `wiki/tech/local-vs-remote-parser-architecture.md`
- `wiki/entities/twoweeks.md`
- `wiki/overview.md`
- `wiki/to do list/kanban.md`

## [2026-04-16] ingest | proposal style persistence + verbati style pipeline

**Agent** : Codex
**Fichiers traités** : `rawinput/Proposal Style Persistence Quickmap Scratchpad.md`, `rawinput/Verbati Style Pipeline Scratchpad.md`
**Pages créées** :
- `wiki/sources/2026-04-16-proposal-style-persistence-quickmap-scratchpad.md`
- `wiki/sources/2026-04-16-verbati-style-pipeline-scratchpad.md`
**Pages mises à jour** :
- `wiki/design/document-token-contract.md`
- `wiki/tech/preview-to-print-pipeline.md`
- `wiki/tech/export-pipeline.md`
- `wiki/index.md`
- `wiki/log.md`
**Pages archivées** :
- aucune
- `wiki/sources/2026-04-14-run-sh-quick-note.md`
- `wiki/timeline.md`
- `wiki/index.md`
- `wiki/log.md`
**Pages archivées** :
- `wiki/archive/concepts/parsing-poc-progress.md`

## [2026-04-15] ingest | A4 grid canon spec writer

**Agent** : Codex
**Fichiers traités** : `rawinput/A4 Grid Canon Spec Writer.md`
**Pages créées** :
- `wiki/sources/2026-04-15-a4-grid-canon-spec-writer.md`
- `wiki/design/a4-layout-systems.md`
**Pages mises à jour** :
- `wiki/concepts/ats-safety.md`
- `wiki/tech/export-pipeline.md`
- `wiki/index.md`
- `wiki/log.md`
**Pages archivées** :
- aucune

## [2026-04-15] doc-update | design bucket pour specs visuelles durables

**Agent** : Codex
**Source** : explicit user instruction
**Pages créées** : aucune
**Pages mises à jour** :
- `CLAUDE.md`
- `wiki/design/a4-layout-systems.md` (déplacée depuis `wiki/concepts/`)
- `wiki/sources/2026-04-15-a4-grid-canon-spec-writer.md`
- `wiki/concepts/ats-safety.md`
- `wiki/tech/export-pipeline.md`
- `wiki/index.md`
- `wiki/log.md`
**Pages archivées** : aucune

## [2026-04-15] doc-update | buckets product strategy meta et rangement des concepts

**Agent** : Codex
**Source** : explicit user instruction
**Pages créées** : aucune
**Pages mises à jour** :
- `CLAUDE.md`
- `wiki/index.md`
- `wiki/entities/twoweeks.md`
- `wiki/overview.md`
- `wiki/tech/export-pipeline.md`
- `wiki/design/a4-layout-systems.md`
- `wiki/sources/2026-04-12-twoweeks-brand-bible.md`
- `wiki/sources/2026-04-14-ats-compliant-score.md`
- `wiki/sources/2026-04-14-export-pipeline-brief-ocr-to-ats-styled-output.md`
- `wiki/sources/2026-04-14-clerk-chrome-extension-addon.md`
- `wiki/sources/2026-04-15-a4-grid-canon-spec-writer.md`
- `wiki/timeline.md`
- `wiki/log.md`
**Pages archivées** : aucune

## [2026-04-16] ingest | preview-print pipelines, token contract, onboarding plan

**Agent** : Codex
**Fichiers traités** : `rawinput/Live Proposal Preview-to-Print Pipeline Scratchpad.md`, `rawinput/Live Resume Preview-to-Print Pipeline Scratchpad.md`, `rawinput/Plan Onboarding, Activation & Interactive Preview — twoweeks.ai.md`, `rawinput/pdf pipeline.md`, `rawinput/token classes for the layout.md`
**Pages créées** :
- `wiki/sources/2026-04-16-live-proposal-preview-to-print-pipeline-scratchpad.md`
- `wiki/sources/2026-04-16-live-resume-preview-to-print-pipeline-scratchpad.md`
- `wiki/sources/2026-04-16-plan-onboarding-activation-interactive-preview.md`
- `wiki/sources/2026-04-16-pdf-pipeline.md`
- `wiki/sources/2026-04-16-token-classes-for-the-layout.md`
- `wiki/tech/preview-to-print-pipeline.md`
- `wiki/design/document-token-contract.md`
**Pages mises à jour** :
- `wiki/tech/export-pipeline.md`
- `wiki/product/product-roadmap.md`
- `wiki/index.md`
- `wiki/log.md`
**Pages archivées** :
- aucune

## [2026-04-17] migration | hybrid control plane + tasks taxonomy

**Agent** : Codex
**Fichiers traités** : `WIKI_SCHEMA.md`, `CLAUDE.md`, `README.md`, `SKILL.md`, `wiki/index.md`, `wiki/meta/llm-wiki-pattern.md`, `wiki/overview.md`, `wiki/entities/twoweeks.md`, `wiki/concepts/cv-families.md`, `wiki/sources/2026-04-14-kanban-sprint-notes.md`, `wiki/sources/2026-04-14-clerk-chrome-extension-addon.md`, `/Users/pana/.codex/skills/ingest-wiki/SKILL.md`
**Pages créées** : aucune
**Pages mises à jour** : `wiki/index.md`, `wiki/meta/llm-wiki-pattern.md`, `wiki/overview.md`, `wiki/entities/twoweeks.md`, `wiki/concepts/cv-families.md`, `wiki/sources/2026-04-14-kanban-sprint-notes.md`, `wiki/sources/2026-04-14-clerk-chrome-extension-addon.md`
**Pages archivées** : aucune
**Migrations** : `wiki/to do list/` → `wiki/tasks/`, archive directories backfilled, bootstrap contract aligned on `WIKI_SCHEMA.md` + `CLAUDE.md`

## [2026-04-17] migration | twoweeks-pagecraft hybrid repo overlay

**Agent** : Codex
**Source** : explicit user instruction
**Pages créées** : aucune
**Pages mises à jour** :
- `README.md`
- `WIKI_SCHEMA.md`
- `CLAUDE.md`
- `AGENTS.md`
- `SKILL.md`
- `wiki/index.md`
- `wiki/log.md`
**Fichiers ajoutés** :
- `IMPLEMENTATION_RULES.md`
- `EXAMPLES.md`
- `skills/ingest-wiki/SKILL.md`
- `skills/apply-hybrid-code-layer/SKILL.md`
- `scripts/audit_code_repo.py`
- `scripts/score_code_repo.py`
- `scripts/validate_overlay.py`
- `audit/code-benchmark-criteria.csv`
**Pages archivées** : aucune
**Migrations** :
- `CLAUDE.md` devient le contrat canonique hybride wiki + code
- `AGENTS.md` devient un shim de compatibilité pour éviter une deuxième rulebook
- la skill ingest gagne un préflight explicite et des contrats de vérification
- les scripts d'audit ignorent les surfaces Obsidian/wiki/raw pour ne pas confondre outillage local et vrai code applicatif

## [2026-04-17] doc-update | skills howto

**Agent** : Codex
**Source** : explicit user instruction
**Pages créées** : aucune
**Pages mises à jour** :
- `README.md`
- `wiki/log.md`
**Fichiers ajoutés** :
- `SKILLS_HOWTO.md`
**Pages archivées** : aucune
**Migrations** :
- ajout d'un howto repo-level qui explique le rôle de `ingest-wiki` vs `apply-hybrid-code-layer`

## [2026-04-17] ingest | live resume preview runtime handoff

**Agent** : Codex
**Fichiers traites** : `rawinput/CVForge Live Resume Render  Interactive Preview Handoff.md`
**Pages creees** :
- `wiki/sources/2026-04-17-cvforge-live-resume-render-interactive-preview-handoff.md`
- `wiki/tech/live-resume-preview-runtime.md`
**Pages mises a jour** :
- `wiki/index.md`
- `wiki/log.md`
**Pages archivees** :
- aucune

## [2026-04-17] doc-update | roadmap and gap status refresh

**Agent** : Codex
**Source** : explicit user instruction
**Pages créées** : aucune
**Pages mises à jour** :
- `wiki/product/product-roadmap.md`
- `wiki/strategy/gap-analysis.md`
- `wiki/index.md`
- `wiki/log.md`
**Pages archivées** : aucune
**Migrations** :
- `Editor ↔ Preview linking` marqué comme implémenté avec reliquat UI/frontend
- `Import recovery layer` marqué comme implémenté avec reliquat de styling CSS et harmonisation des tokens
- `Document health / readiness layer` marqué comme implémenté avec reliquat de tests et validation

## [2026-04-24] ingest | Pass 3B Structured Scoring Decisions

**Agent** : Codex
**Fichiers traités** : `rawinput/Pass 3B Structured Scoring Decisions.md`
**Pages créées** :
- `wiki/sources/2026-04-24-pass-3b-structured-scoring-decisions.md`
**Pages mises à jour** :
- `wiki/index.md`
- `wiki/log.md`
**Pages archivées** :
- aucune
**Points notables** :
- contrat de beta review interne pour structured shadow output
- production score laissé inchangé
- rawinput déplacé vers `raw/` après ingest

## [2026-04-27] ingest | jobs, match review, brand voice, motion, workshop pagination

**Agent** : Codex
**Fichiers traités** :
- `rawinput/.md`
- `rawinput/ Prompt for ChatGPT — Twoweeks brand-voice copy refactor.md`
- `rawinput/Brand Voice Review — Twoweeks.ai.md`
- `rawinput/Contrat complet de validation  Job match kpi benchmark.md`
- `rawinput/Dev-only advisory beta access for everyone.md`
- `rawinput/GIT - GOOD HABIT -SKILL.md`
- `rawinput/Implementation Handoff — 2026 Elite Design System (Phases 1–4) (DONE VERIFIER SI VRAIMENT PLEINEMENT IMPLEMENTÉ SANS DRIFT).md`
- `rawinput/Job Library PRD.md`
- `rawinput/Match Review V1 Dogfood Tool — Developer  LLM Note.md`
- `rawinput/Meta-prompt maître.md`
- `rawinput/Note — système de tests du repo.md`
- `rawinput/TEST Headless browser setup for workshop preview probe.md`
- `rawinput/Twoweeks.ai Motion System — Implementation Hardening Pass -PR1 ,PR2,PR3.md`
- `rawinput/Twoweeks.ai — Brand Voice Card.md`
- `rawinput/Twoweeks.ai — Motion System.md`
- `rawinput/Typography Token Audit Table.md`
- `rawinput/UI design audit - prompt.md`
- `rawinput/VOICE CARD.md`
- `rawinput/Workshop Pagination.md`
- `rawinput/audit token workspace -en cours.md`
- `rawinput/brand Twoweeks.ai.md`
- `rawinput/brand logo system.md`
- `rawinput/claude light mode .md`
**Pages créées** :
- `wiki/product/job-library.md`
- `wiki/product/job-match-review.md`
- `wiki/design/motion-system.md`
- `wiki/design/logo-system.md`
- `wiki/design/elite-design-system.md`
- `wiki/tech/workshop-pagination.md`
- `wiki/tech/workshop-token-parity.md`
- `wiki/tech/repo-testing-system.md`
- `wiki/howto/headless-workshop-preview-probe.md`
- `wiki/howto/git-branch-hygiene.md`
- `wiki/meta/codex-prompting-standards.md`
- 23 pages source dans `wiki/sources/`
**Pages mises à jour** :
- `wiki/overview.md`
- `wiki/index.md`
- `wiki/log.md`
- `wiki/design/brand-voice.md`
- `wiki/design/document-token-contract.md`
- `wiki/product/kpis.md`
- `wiki/product/product-roadmap.md`
- `wiki/tech/export-pipeline.md`
- `wiki/tech/preview-to-print-pipeline.md`
**Pages archivées** :
- aucune
**Points notables** :
- `rawinput/` vidé sauf `README.md`
- fichiers source déplacés vers `raw/`
- les sources brand voice ont été dédupliquées vers une seule page durable `wiki/design/brand-voice.md`
- le fichier vide `rawinput/.md` a été conservé comme source vide sans page durable
