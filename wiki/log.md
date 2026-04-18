---
title: "Log — twoweeks Wiki"
category: overview
updated: 2026-04-18
---

# Log du Wiki · twoweeks

Journal chronologique append-only de toutes les opérations sur le wiki.

```bash
grep "^## \[" wiki/log.md | tail -5   # Dernières 5 entrées
grep "^## \[" wiki/log.md | grep "ingest"  # Tous les ingests
```

---

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
