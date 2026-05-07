---
title: Index du Wiki — twoweeks
category: overview
sticker: emoji//1f9c6
updated: 2026-05-07
---

# Index du Wiki · twoweeks (v2)

Catalogue complet de toutes les pages **actives** du wiki (status: current ou planned). Les pages archivées sont dans `wiki/archive/`.
Le contrôle opératoire du repo reste défini par `WIKI_SCHEMA.md` puis `CLAUDE.md` / `AGENTS.md`; ce catalogue demeure la surface active des pages wiki.

---

## Retrieval Map

| Sujet | Page canonique | Lire aussi |
|-------|----------------|------------|
| Mémoire active LLM | [[hot]] | [[overview]], [[meta/llm-wiki-pattern]] |
| État produit | [[overview]] | [[entities/twoweeks]], [[product/product-roadmap]], [[product/product-vision]] |
| Parser / vérité CV | [[concepts/cv-parsing-pipeline]] | [[concepts/cv-families]], [[tech/import-ocr-pipeline]] |
| Jobs / match | [[product/job-library]] | [[product/job-match-review]] |
| Export / pagination | [[tech/export-pipeline]] | [[tech/preview-to-print-pipeline]], [[tech/workshop-pagination]] |
| Proposal Forge geometry | [[tech/proposal-forge-document-geometry]] | [[tech/proposal-style-layer]], [[design/document-token-contract]] |
| Design / ATS / motion | [[design/ats-safety]] | [[design/document-token-contract]], [[design/motion-system]], [[design/brand-voice]] |
| Opérations locales | [[howto/local-parser-operations]] | [[tech/local-vs-remote-parser-architecture]] |
| Règles wiki | [[meta/llm-wiki-pattern]] | [[meta/temporal-management]], [[meta/codex-prompting-standards]] |

Cette carte est un routeur de lecture pour agents LLM. Elle ne remplace pas les pages durables.

---

## Vue d'ensemble

| Fichier | Description | Status |
|---------|-------------|--------|
| [[hot]] | Cache actif non canonique pour retrieval LLM rapide | current |
| [[overview]] | Synthèse générale — produit, architecture active, priorités | current |
| [[log]] | Journal chronologique des opérations wiki | — |
| [[timeline]] | Chronologie des décisions et pivots projet | — |

---

## Entités

| Page | Résumé | Status | Version |
|------|--------|--------|---------|
| [[entities/twoweeks\|twoweeks]] | Produit principal — ingestion CV, données canoniques, génération de documents | current | v2 |

---

## Concepts

| Page | Résumé | Status | Tags |
|------|--------|--------|------|
| [[concepts/cv-families\|CV Families]] | Familles first-class, familles secondaires, mappings de sections | current | parser, sections |
| [[concepts/cv-parsing-pipeline\|CV Parsing Pipeline]] | Architecture structurée par familles et vérité canonique par sections | current | parser, architecture |

---

## Design

| Page | Résumé | Status | Tags |
|------|--------|--------|------|
| [[design/a4-layout-systems\|A4 Layout Systems]] | Canons A4 et grille Robial pour templates résumé/export | current | layout, a4 |
| [[design/ats-safety\|ATS Safety]] | Règles parser-safe pour layouts, headings, exports et audits | current | ats, quality |
| [[design/brand-voice\|Brand Voice]] | Voix staccato, Corporate Noir, règles de copie | current | brand, voice |
| [[design/document-token-contract\|Document Token Contract]] | Classes geometry/flow/appearance/runtime pour preview/export/DOCX | current | tokens, layout |
| [[design/elite-design-system\|Elite Design System]] | Boundary chrome/document, tokens UI, exports et risques design-system | current | design-system, tokens |
| [[design/locale-typography-rules\|Locale Typography Rules]] | Règles FR/EN de ponctuation, citations, dates et wrap-safe export | current | typography, locale |
| [[design/logo-system\|Logo System]] | Wordmark `two weeks.`, compact `tw.` et période terracotta | current | logo, brand |
| [[design/motion-system\|Motion System]] | Motion causal, breathing period, stages IA et settle | current | motion, ai |

---

## Product

| Page | Résumé | Status | Tags |
|------|--------|--------|------|
| [[product/ai-product-model\|AI Product Model]] | 3 modes IA, rulebook et qualité writing | current | ai, ux, modes |
| [[product/ai-consistency-p0-editor-ai\|AI Consistency P0 — Closure Audit]] | Closure audit snapshot du rulebook AI editor, preview, telemetry et tailoring | current | ai, editor, rulebook |
| [[product/job-library\|Job Library]] | Jobs sauvegardés, Job Brief editable et documents liés | current | jobs, library |
| [[product/job-match-review\|Job Match Review]] | Match comme indicateur d'attention utilisateur et dogfood interne | current | jobs, match |
| [[product/kpis\|KPIs]] | Métriques de succès produit | current | kpi, métriques |
| [[product/product-roadmap\|Product Roadmap]] | Initiatives par phase, items implémentés et reliquat de raffinement | current | roadmap, product |
| [[product/product-vision\|Product Vision]] | Blueprint produit complet | current | vision, architecture |

---

## Strategy

| Page | Résumé | Status | Tags |
|------|--------|--------|------|
| [[strategy/benchmark-matrix\|Benchmark Matrix]] | Scorecard concurrentielle pondérée | current | benchmark, scoring |
| [[strategy/gap-analysis\|Gap Analysis]] | Diagnostic concurrentiel avec gaps restants vs items déjà implémentés | current | gap, diagnostic |

---

## Meta

| Page | Résumé | Status | Tags |
|------|--------|--------|------|
| [[meta/llm-wiki-pattern\|LLM Wiki Pattern]] | Pattern de base de connaissance persistante | current | meta, workflow |
| [[meta/codex-prompting-standards\|Codex Prompting Standards]] | Prompts d'exécution stricts, locaux, testables et bornés | current | codex, prompts |
| [[meta/temporal-management\|Gestion temporelle]] | Distinction passé/présent/futur dans le wiki | current | temporal, architecture |

---

## Sources

CV Forge PR4 Remaining Tasks now reflects the 860px paper-width sync, rich summary parity, and `mistral-small-latest` helper routing.

| Page | Type | Date | Status |
|------|------|------|--------|
| [[sources/2026-04-03-workspace-security-rgpd-audit\|Workspace Security / RGPD Audit]] | analysis | 2026-04-03 | current |
| [[sources/2026-04-09-decisions-cvforge-sprint\|Décisions sprint — parsing & features]] | conversation | 2026-04-09 | current |
| [[sources/2026-04-09-tweet-karpathy-llm-wiki\|Tweet Karpathy — LLM Knowledge Bases]] | tweet | 2026-04-09 | current |
| [[sources/2026-04-09-wiki-paste-llm-wiki\|Wiki Paste — LLM Wiki]] | document | 2026-04-09 | current |
| [[sources/2026-04-10-notion-roadmap-cvforge\|Notion Roadmap — CVForge]] | document | 2026-04-10 | current |
| [[sources/2026-04-10-benchmark-matrix\|Ideal Benchmark Matrix — Path A]] | document | 2026-04-10 | current |
| [[sources/2026-04-10-success-blueprint\|Success Blueprint — Path B]] | document | 2026-04-10 | current |
| [[sources/2026-04-10-gap-analysis\|Gap Analysis — Path C]] | document | 2026-04-10 | current |
| [[sources/2026-04-11-cv-parsing-poc-state\|CV Parsing POC State — Checkpoint]] | spec | 2026-04-11 | current |
| [[sources/2026-04-11-todo-sprint\|Sprint Notes — 2026-04-11]] | conversation | 2026-04-11 | current |
| [[sources/2026-04-11-jessica-helen-poc-state\|Jessica/Helen POC State]] | document | 2026-04-11 | current |
| [[sources/2026-04-12-twoweeks-brand-bible\|Brand Bible 2026 — twoweeks.ai]] | spec | 2026-04-12 | current |
| [[sources/2026-04-14-ats-compliant-score\|ATS Compliant Score — Resume Audit Rubric]] | spec | 2026-04-14 | current |
| [[sources/2026-04-14-local-dev-vs-remote-parser-architecture\|Local Dev vs Remote Parser Architecture]] | spec | 2026-04-14 | current |
| [[sources/2026-04-14-run-sh-modes\|run.sh — Local/Cloud Modes]] | runbook | 2026-04-14 | current |
| [[sources/2026-04-14-run-sh-quick-note\|run.sh Quick Note — Main Dev Entrypoint]] | runbook | 2026-04-14 | current |
| [[sources/2026-04-14-export-pipeline-brief-ocr-to-ats-styled-output\|Export Pipeline Brief — OCR to ATS / Styled Output]] | spec | 2026-04-14 | current |
| [[sources/2026-04-14-clerk-chrome-extension-addon\|Clerk Chrome Extension Addon — Save to twoweeks]] | spec | 2026-04-14 | current |
| [[sources/2026-04-14-structured-parsing-canonical-truth\|Structured Parsing Canonical Truth]] | spec | 2026-04-14 | current |
| [[sources/2026-04-14-docker-commands\|Docker Commands — Local Parser]] | runbook | 2026-04-14 | current |
| [[sources/2026-04-14-kanban-sprint-notes\|Kanban Sprint Notes — 2026-04-14]] | conversation | 2026-04-14 | current |
| [[sources/2026-04-15-mistral-resume-v3-section-recovery-scratchpad\|Mistral Resume V3 — Section Recovery Scratchpad]] | spec | 2026-04-15 | current |
| [[sources/2026-04-15-run-sh-workspace-modes\|run.sh Workspace Modes — Local Fast and Parser Dev]] | runbook | 2026-04-15 | current |
| [[sources/2026-04-15-section-detection-future-note\|Section Detection Future Note — Narrow Recovery Scope]] | spec | 2026-04-15 | current |
| [[sources/2026-04-15-a4-grid-canon-spec-writer\|A4 Grid Canon Spec Writer]] | spec | 2026-04-15 | current |
| [[sources/2026-04-15-typography-mode\|Typography Mode]] | spec | 2026-04-15 | current |
| [[sources/2026-04-15-french-typography-scratch-pad\|French Typography Scratch Pad]] | spec | 2026-04-15 | current |
| [[sources/2026-04-15-english-typography-scratch-pad\|English Typography Scratch Pad]] | spec | 2026-04-15 | current |
| [[sources/2026-04-15-conversation-locale-typography-rules\|Conversation — Locale Typography Rules]] | conversation | 2026-04-15 | current |
| [[sources/2026-04-16-live-proposal-preview-to-print-pipeline-scratchpad\|Live Proposal Preview-to-Print Pipeline Scratchpad]] | spec | 2026-04-16 | current |
| [[sources/2026-04-16-live-resume-preview-to-print-pipeline-scratchpad\|Live Resume Preview-to-Print Pipeline Scratchpad]] | spec | 2026-04-16 | current |
| [[sources/2026-04-16-plan-onboarding-activation-interactive-preview\|Plan Onboarding, Activation & Interactive Preview — twoweeks.ai]] | spec | 2026-04-16 | current |
| [[sources/2026-04-16-pdf-pipeline\|PDF Pipeline]] | note | 2026-04-16 | current |
| [[sources/2026-04-16-token-classes-for-the-layout\|Token Classes for the Layout]] | spec | 2026-04-16 | current |
| [[sources/2026-04-16-proposal-style-persistence-quickmap-scratchpad\|Proposal Style Persistence Quickmap Scratchpad]] | spec | 2026-04-16 | current |
| [[sources/2026-04-16-verbati-style-pipeline-scratchpad\|Verbati Style Pipeline Scratchpad]] | spec | 2026-04-16 | current |

| [[sources/2026-04-17-cvforge-live-resume-render-interactive-preview-handoff|CVForge Live Resume Render / Interactive Preview Handoff]] | spec | 2026-04-17 | current |
| [[sources/2026-04-18-quick-start-module-hierarchy|Quick Start Module Hierarchy]] | spec | 2026-04-18 | current |
| [[sources/2026-04-24-pass-3b-structured-scoring-decisions|Pass 3B Structured Scoring Decisions]] | analysis | 2026-04-24 | current |
| [[sources/2026-04-21-2026-elite-design-system-implementation-handoff|2026 Elite Design System Implementation Handoff]] | other | 2026-04-21 | current |
| [[sources/2026-04-27-brand-logo-system|Brand Logo System]] | other | 2026-04-27 | current |
| [[sources/2026-04-27-brand-twoweeks-ai|Brand — Twoweeks.ai]] | other | 2026-04-27 | current |
| [[sources/2026-04-27-brand-voice-review-twoweeks|Brand Voice Review — Twoweeks.ai]] | analysis | 2026-04-27 | current |
| [[sources/2026-04-27-claude-light-mode-palette|Claude Light Mode Palette]] | other | 2026-04-27 | current |
| [[sources/2026-04-27-codex-prompt-master|Meta-prompt maître]] | other | 2026-04-27 | current |
| [[sources/2026-04-27-dev-only-advisory-beta-access|Dev-only Advisory Beta Access]] | spec | 2026-04-27 | current |
| [[sources/2026-04-27-empty-staged-md|Empty Staged Markdown File]] | other | 2026-04-27 | current |
| [[sources/2026-04-27-git-good-habit-skill|Git Good Habit Skill]] | runbook | 2026-04-27 | current |
| [[sources/2026-04-27-job-library-prd|Job Library PRD]] | spec | 2026-04-27 | current |
| [[sources/2026-04-27-job-match-validation-contract|Job Match Validation Contract]] | spec | 2026-04-27 | current |
| [[sources/2026-04-27-match-review-v1-dogfood-tool|Match Review V1 Dogfood Tool]] | runbook | 2026-04-27 | current |
| [[sources/2026-04-27-motion-system-implementation-hardening|Motion System Implementation Hardening]] | spec | 2026-04-27 | current |
| [[sources/2026-04-27-repo-test-system-note|Repo Test System Note]] | other | 2026-04-27 | current |
| [[sources/2026-04-27-test-headless-browser-setup-workshop-preview-probe|Headless Browser Setup for Workshop Preview Probe]] | runbook | 2026-04-27 | current |
| [[sources/2026-04-27-twoweeks-brand-voice-card|Twoweeks.ai Brand Voice Card]] | spec | 2026-04-27 | current |
| [[sources/2026-04-27-twoweeks-brand-voice-copy-refactor-prompt|Prompt for Twoweeks Brand-Voice Copy Refactor]] | other | 2026-04-27 | current |
| [[sources/2026-04-27-twoweeks-motion-system|Twoweeks.ai Motion System]] | spec | 2026-04-27 | current |
| [[sources/2026-04-27-typography-token-audit-table|Typography Token Audit Table]] | analysis | 2026-04-27 | current |
| [[sources/2026-04-27-ui-design-audit-prompt|UI Design Audit Prompt]] | other | 2026-04-27 | current |
| [[sources/2026-04-27-voice-card-ui-copy-audits|Voice Card and UI Copy Audits]] | analysis | 2026-04-27 | current |
| [[sources/2026-04-27-workshop-pagination|Workshop Pagination]] | spec | 2026-04-27 | current |
| [[sources/2026-04-27-workshop-token-audit|Workshop Token Audit]] | analysis | 2026-04-27 | current |
| [[sources/2026-04-30-cv-forge-pr4-remaining-tasks|CV Forge PR4 Remaining Tasks]] | scratchpad | 2026-04-30 | current |
| [[sources/2026-04-30-jobs-language-localization-scratchpad|Jobs Language Localization Scratchpad]] | scratchpad | 2026-04-30 | current |
| [[sources/2026-04-30-refonte-wiki-claude-obsidian|Revue: refonte wiki claude-obsidian]] | decision | 2026-04-30 | current |
| [[sources/2026-04-30-two-weeks-app-skeleton-skill|Twoweeks App Skeleton Skill Source]] | skill | 2026-04-30 | current |
---

## Tech

| Page | Résumé | Tags |
|------|--------|------|
| [[tech/import-ocr-pipeline\|Import OCR Pipeline]] | Call path OCR/import et vérité canonique par sections | import, ocr, convex |
| [[tech/export-pipeline\|Export Pipeline]] | Pipeline document final PDF/DOCX séparé du preview DOM | export, pdf, docx |
| [[tech/local-vs-remote-parser-architecture\|Local vs Remote Parser Architecture]] | Séparation debug local / cloud / prod pour le parser | parser, env, production |
| [[tech/preview-to-print-pipeline\|Preview-to-Print Pipeline]] | Parité preview -> print route -> PDF pour resume et proposal | preview, print, pdf |
| [[tech/proposal-ai-routing-and-inline-diff\|Proposal AI Routing and Inline Diff]] | Routing proposal AI, selector models, and inline proofing overlay | proposal, ai, routing |
| [[tech/proposal-forge-document-geometry|Proposal Forge Document Geometry]] | Canon page-first: paper width, toolbar/panel alignment, breakpoint stability, preview/edit scrollbars | proposal, forge, geometry |
| [[tech/proposal-style-layer|Proposal Style Layer]] | Base Style 1/2/3, palettes tokenisées et reset des personnalisations proposal | proposal, style, tokens |
| [[tech/live-resume-preview-runtime|Live Resume Preview Runtime]] | Runtime du preview resume vivant, mapping canonique et linking preview -> editor | preview, renderer, editor |
| [[tech/quick-start-module-hierarchy|Quick Start Module Hierarchy]] | Shell Quick Start app-shell, route-state transitoire et cold start cover-letter | quick-start, onboarding, ui |
| [[tech/repo-testing-system|Repo Testing System]] | Vitest/JSDOM/Testing Library, mocks et gap E2E produit | tests, qa |
| [[tech/workshop-pagination|Workshop Pagination]] | `committedPages` comme vérité preview/print/export workshop | workshop, pagination |
| [[tech/workshop-token-parity|Workshop Token Parity]] | Drift preview/planner sur tokens, typo et constantes workshop | workshop, tokens |

---

## Howto

| Page | Résumé | Tags |
|------|--------|------|
| [[howto/cloudflare-zero-trust-tunnel\|Cloudflare Zero Trust + Tunnel]] | Runbook parser.dasti.ai, CF Access, tunnel, DNS, token, WAF | cloudflare, devops |
| [[howto/git-branch-hygiene|Git Branch Hygiene]] | Démarrer une tâche depuis `main` à jour avant branche courte | git, workflow |
| [[howto/headless-workshop-preview-probe|Headless Workshop Preview Probe]] | Probe Playwright headless pour `/cv` workshop preview | playwright, workshop |
| [[howto/local-parser-operations\|Local Parser Operations]] | Lancer, diagnostiquer et réaligner la stack parser locale | parser, local, run.sh |
| [[howto/wiki-commands-and-llm-export|Wiki Commands and LLM Export]] | Commandes wiki, modes de retrieval et plan `wiki/llms.txt` | wiki, codex, retrieval |

---

## Tasks

| Page | Résumé |
|------|--------|
| [[tasks/kanban\|Kanban Sprint]] | Backlog, en cours, bugs ouverts, déférés, done |
| [[tasks/coffee talk\|Coffee Talk]] | Note courte pour synchroniser la skill Codex collaborateur |
| [[tasks/Audit Workspace — Bonnes Pratiques, Sécurité, RGPD\|Audit Workspace — Bonnes Pratiques, Sécurité, RGPD]] | Audit sauvegardé du workspace |

---

## Outputs

| Page | Type | Date | Sujet |
|------|------|------|-------|
| — | — | — | Aucun output actif sur disque |

---

## Archive

| Page | Archivée le | Supersédée par |
|------|-------------|----------------|
| [[archive/concepts/parsing-poc-progress\|Parsing POC Progress]] | 2026-04-15 | [[concepts/cv-parsing-pipeline]] |
| [[archive/entities/cv-forge\|CV Forge (ancienne entité)]] | 2026-04-12 | [[entities/twoweeks]] |

---

## Statistiques

- **Pages actives** : 113 (5 overview, 1 entité, 2 concepts, 8 design, 7 product, 2 strategy, 3 meta, 66 sources, 11 tech, 5 howto, 3 tasks, 0 output)
- **Pages archivées** : 2
- **Sources dans `raw/`** : 68
- **Sources en attente dans `rawinput/`** : 0
- **Dernière mise à jour** : 2026-05-06
