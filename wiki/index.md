---
title: Index du Wiki — twoweeks
category: overview
sticker: emoji//1f9c6
updated: 2026-06-27
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
| Planning IA shadow | [[product/ai-product-model]] | [[tech/proposal-ai-routing-and-inline-diff]], [[sources/2026-05-25-proposal-generation-truth-planner]] |
| Cover-letter quality | [[tasks/2026-06-22-cover-letter-quality-production-roadmap]] | [[sources/2026-06-24-cover-letter-mistral-v2-staging-green]], [[sources/2026-06-23-cover-letter-quality-pr249-staged-internal-gate]], [[sources/2026-06-23-release-orchestration-staging-pr87-8-checkpoint]], [[sources/2026-06-23-cover-letter-quality-pr248-merge-checkpoint]], [[sources/2026-06-23-cover-letter-quality-pr246-merge-checkpoint]] |
| ChatGPT App roadmap | [[product/chatgpt-app-sdk-roadmap]] | [[product/manual-application-handoff]], [[sources/2026-06-27-pr87-17d-mcp-oauth-local-dev-route-adapter-checkpoint]], [[sources/2026-06-26-pr87-17c1-mcp-oauth-login-return-continuation-checkpoint]], [[sources/2026-06-26-pr87-17c0-mcp-oauth-login-return-convention-checkpoint]], [[sources/2026-06-26-pr87-17b-mcp-oauth-authorization-intent-checkpoint]], [[sources/2026-06-26-pr87-17a-mcp-oauth-authorization-request-boundary-checkpoint]], [[sources/2026-06-25-pr87-16-mcp-account-link-lifecycle-checkpoint]], [[sources/2026-06-25-pr87-15d-mcp-auth-local-runtime-wiring-checkpoint]], [[sources/2026-06-25-pr87-15c-mcp-auth-composition-checkpoint]], [[sources/2026-06-25-pr87-15b1-mcp-account-link-lookup-adapter-checkpoint]], [[sources/2026-06-25-pr87-15b0-mcp-account-link-canonical-storage-checkpoint]], [[sources/2026-06-25-pr87-15a-mcp-stytch-bearer-verifier-checkpoint]], [[sources/2026-06-24-pr87-14b-mcp-auth-dev-endpoint-wiring-checkpoint]], [[sources/2026-06-24-pr87-14a-mcp-auth-request-orchestrator-checkpoint]], [[sources/2026-06-24-pr87-13-mcp-auth-policy-boundary-checkpoint]], [[sources/2026-06-24-pr87-12-mcp-dev-fixture-demo-checkpoint]], [[sources/2026-06-24-pr87-10-mcp-dev-endpoint-blocked-reachability-checkpoint]], [[sources/2026-06-23-release-orchestration-staging-pr87-8-checkpoint]], [[sources/2026-06-23-twoweeks-mcp-chatgpt-app-sdk-roadmap-checkpoint]], [[sources/2026-06-19-pr80b-safe-application-handoff-while-ats-access-pending]] |
| Manual application handoff | [[product/manual-application-handoff]] | [[product/chatgpt-app-sdk-roadmap]], [[sources/2026-06-23-twoweeks-mcp-chatgpt-app-sdk-roadmap-checkpoint]] |
| Parser / vérité CV | [[concepts/cv-parsing-pipeline]] | [[concepts/cv-families]], [[tech/import-ocr-pipeline]] |
| Jobs / match | [[product/job-library]] | [[product/job-match-review]] |
| Export / pagination | [[tech/export-pipeline]] | [[tech/preview-to-print-pipeline]], [[tech/workshop-pagination]] |
| Proposal Forge geometry | [[tech/proposal-forge-document-geometry]] | [[tech/proposal-style-layer]], [[design/document-token-contract]] |
| Proposal signature/closing | [[tech/proposal-signature-closing-layer]] | [[tech/proposal-style-layer]], [[tech/proposal-forge-document-geometry]], [[tech/export-pipeline]] |
| Design / ATS / motion | [[design/ats-safety]] | [[design/document-token-contract]], [[design/motion-system]], [[design/brand-voice]] |
| ATS scoring / health | [[tech/cv-ats-audit-heuristic]] | [[design/ats-safety]], [[concepts/cv-parsing-pipeline]] |
| Langue / localisation | [[strategy/language-localization]] | [[design/locale-typography-rules]], [[product/product-roadmap]] |
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
| [[product/ai-product-model\|AI Product Model]] | 3 modes IA, rulebook, qualité writing, and Planner Agent shadow chain | current | ai, ux, modes |
| [[product/ai-consistency-p0-editor-ai\|AI Consistency P0 — Closure Audit]] | Closure audit snapshot du rulebook AI editor, preview, telemetry et tailoring | current | ai, editor, rulebook |
| [[product/chatgpt-app-sdk-roadmap\|ChatGPT/App SDK Roadmap]] | MCP/App SDK PR94 merged production `/oauth/authorize` ownerless pre-auth intent creation behind PR89 activation, PR90 status, PR92 preflight, and PR93 shells; `/oauth/callback` and `/mcp` remain inert, next slice is production login-return owner binding | current | chatgpt-app, apps-sdk |
| [[product/job-library\|Job Library]] | Jobs sauvegardés, Job Brief editable et documents liés | current | jobs, library |
| [[product/job-match-review\|Job Match Review]] | Match comme indicateur d'attention utilisateur et dogfood interne | current | jobs, match |
| [[product/kpis\|KPIs]] | Métriques de succès produit | current | kpi, métriques |
| [[product/manual-application-handoff\|Manual Application Handoff]] | PR80B manual handoff implemented/tested on the MCP/App SDK track; live submit/apply still blocked | current | ats, handoff, safety |
| [[product/product-roadmap\|Product Roadmap]] | Initiatives par phase, items implémentés et reliquat de raffinement | current | roadmap, product |
| [[product/product-vision\|Product Vision]] | Blueprint produit complet | current | vision, architecture |

---

## Strategy

| Page | Résumé | Status | Tags |
|------|--------|--------|------|
| [[strategy/benchmark-matrix\|Benchmark Matrix]] | Scorecard concurrentielle pondérée | current | benchmark, scoring |
| [[strategy/gap-analysis\|Gap Analysis]] | Diagnostic concurrentiel avec gaps restants vs items déjà implémentés | current | gap, diagnostic |
| [[strategy/language-localization\|Language Localization]] | Rollout language strategy: UI vs document vs market, promotion gates, RTL and release rules | current | i18n, localization |

---

## Meta

| Page | Résumé | Status | Tags |
|------|--------|--------|------|
| [[meta/llm-wiki-pattern\|LLM Wiki Pattern]] | Pattern de base de connaissance persistante | current | meta, workflow |
| [[meta/codex-prompting-standards\|Codex Prompting Standards]] | Prompts d'exécution stricts, locaux, testables et bornés | current | codex, prompts |
| [[meta/temporal-management\|Gestion temporelle]] | Distinction passé/présent/futur dans le wiki | current | temporal, architecture |

---

## Sources

Cover-letter quality has a merged PR249 staged internal Mistral V2 gate and a green Convex staging checkpoint on `dev:neat-starfish-33`; production full GO and quality repair remain separate/not approved. The MCP/App SDK track now has PR87.10 reachability, PR87.11 auth architecture, PR87.12 local/dev fixture demo, PR87.13 pure auth-policy boundary, PR87.14A auth request orchestrator boundary, PR87.14B local/dev auth endpoint wiring, PR87.15A server-only Stytch bearer verifier boundary, PR87.15B0 canonical account-link storage/index, PR87.15B1 server-only account-link lookup adapter, PR87.15C non-production auth composition boundary, PR87.15D local/dev runtime auth composition wiring, PR87.16 authoritative server-only account-link lifecycle, PR87.17A OAuth authorization request boundary, PR87.17B OAuth authorization-intent storage, PR87.17C0 OAuth login-return convention, PR87.17C1 OAuth login-return continuation boundary, and PR87.17D local/dev-only OAuth route adapter merged, while production MCP/OAuth/token/account-link runtime remains blocked with PR80B implemented and PR88/PR89 blocked.

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
| [[sources/2026-05-25-proposal-generation-truth-planner\|Proposal Generation Truth Planner]] | source | 2026-05-25 | current |
| [[sources/2026-05-25-two-weeks-theme-palette\|Two Weeks Theme Palette]] | source | 2026-05-25 | current |
| [[sources/2026-05-21-cv-proposal-command-layer-unification-note|Command Layer Unification Note — CV & Proposal Toolbars]] | source | 2026-05-21 | current |
| [[sources/2026-05-26-two-weeks-language-map-reference-note\|Two Weeks Language Map Reference Note]] | source | 2026-05-26 | current |
| [[sources/2026-06-11-audit-architecture-application-os-pr1-pr17\|Audit architecture — Application OS PR1 à PR17]] | analysis | 2026-06-11 | current |
| [[sources/2026-06-11-cv-forge-save-restore-pipeline-fix\|CV Forge Save / Restore Pipeline Fix]] | scratchpad | 2026-06-11 | current |
| [[sources/2026-06-11-future-two-weeks-agents-ready\|Future Two Weeks Agents Ready]] | analysis | 2026-06-11 | current |
| [[sources/2026-06-11-mcp-chatgpt-app-readiness-spec\|MCP and ChatGPT App Readiness Spec]] | analysis | 2026-06-11 | current |
| [[sources/2026-06-11-chatgpt-app-end-to-end-safety-audit\|ChatGPT App End-to-end Safety Audit]] | analysis | 2026-06-11 | current |
| [[sources/2026-06-11-chatgpt-app-local-only-manifest-draft\|Local-only ChatGPT App Manifest Draft]] | analysis | 2026-06-11 | current |
| [[sources/2026-06-11-chatgpt-app-non-production-prototype-plan\|Non-production ChatGPT App Prototype Plan]] | analysis | 2026-06-11 | current |
| [[sources/2026-06-12-chatgpt-apps-sdk-roadmap-pr35\|ChatGPT Apps SDK Roadmap PR33-PR40]] | analysis | 2026-06-12 | current |
| [[sources/2026-06-12-non-production-apps-sdk-exploration-plan\|Non-production Apps SDK Exploration Plan]] | analysis | 2026-06-12 | current |
| [[sources/2026-06-11-cv-hydration-and-style-system\|CV Hydration And Style System]] | analysis | 2026-06-11 | current |
| [[sources/2026-06-11-emojis-library\|Emojis Library References]] | other | 2026-06-11 | current |
| [[sources/2026-06-11-master-architecture-decision-doc-v1\|Twoweeks Application OS Execution Starter Pack]] | draft | 2026-06-11 | current |
| [[sources/2026-06-11-oddyseo-pietro-schirano-writing-tool\|Oddyseo Writing Tool Note]] | other | 2026-06-11 | current |
| [[sources/2026-06-12-chatgpt-app-sdk-roadmap-pr41-pr89\|ChatGPT/App SDK Roadmap PR41-PR89]] | roadmap | 2026-06-12 | current |
| [[sources/2026-06-19-pr80b-safe-application-handoff-while-ats-access-pending\|PR80B - Safe Application Handoff While ATS Authorization Is Pending]] | implementation-plan | 2026-06-19 | current |
| [[sources/2026-06-23-cover-letter-quality-production-roadmap-updated-checklist\|Cover Letter Quality Production Roadmap - Updated Checklist]] | analysis | 2026-06-23 | current |
| [[sources/2026-06-23-cover-letter-quality-pr246-merge-checkpoint\|Cover Letter Quality PR246 Merge Checkpoint]] | analysis | 2026-06-23 | current |
| [[sources/2026-06-23-cover-letter-quality-pr249-staged-internal-gate\|Cover Letter Quality PR249 Staged Internal Gate]] | analysis | 2026-06-23 | current |
| [[sources/2026-06-23-release-orchestration-staging-pr87-8-checkpoint\|Release Orchestration Checkpoint - Staging and PR87.8]] | analysis | 2026-06-23 | current |
| [[sources/2026-06-24-pr87-10-mcp-dev-endpoint-blocked-reachability-checkpoint\|MCP Dev Endpoint Test-Only Reachability Checkpoint - PR87.10]] | analysis | 2026-06-24 | current |
| [[sources/2026-06-24-pr87-11-mcp-auth-account-linking-architecture-checkpoint\|ChatGPT App MCP Auth And Account-Linking Architecture Checkpoint - PR87.11]] | analysis | 2026-06-24 | current |
| [[sources/2026-06-24-pr87-12-mcp-dev-fixture-demo-checkpoint\|MCP Dev Fixture Demo Checkpoint - PR87.12]] | analysis | 2026-06-24 | current |
| [[sources/2026-06-24-pr87-13-mcp-auth-policy-boundary-checkpoint\|MCP Auth Metadata And Policy Boundary Checkpoint - PR87.13]] | analysis | 2026-06-24 | current |
| [[sources/2026-06-24-pr87-14a-mcp-auth-request-orchestrator-checkpoint\|MCP Auth Request Orchestrator Boundary Checkpoint - PR87.14A]] | analysis | 2026-06-24 | current |
| [[sources/2026-06-24-pr87-14b-mcp-auth-dev-endpoint-wiring-checkpoint\|MCP Local Dev Auth Discovery And Challenge Wiring Checkpoint - PR87.14B]] | analysis | 2026-06-24 | current |
| [[sources/2026-06-25-pr87-15a-mcp-stytch-bearer-verifier-checkpoint\|MCP Stytch Bearer Verifier Boundary Checkpoint - PR87.15A]] | analysis | 2026-06-25 | current |
| [[sources/2026-06-25-pr87-15b0-mcp-account-link-canonical-storage-checkpoint\|MCP Account-Link Canonical Storage Checkpoint - PR87.15B0]] | analysis | 2026-06-25 | current |
| [[sources/2026-06-25-pr87-15b1-mcp-account-link-lookup-adapter-checkpoint\|MCP Account-Link Lookup Adapter Checkpoint - PR87.15B1]] | analysis | 2026-06-25 | current |
| [[sources/2026-06-25-pr87-15c-mcp-auth-composition-checkpoint\|MCP Auth Composition Checkpoint - PR87.15C]] | analysis | 2026-06-25 | current |
| [[sources/2026-06-25-pr87-15d-mcp-auth-local-runtime-wiring-checkpoint\|MCP Local Dev Auth Runtime Wiring Checkpoint - PR87.15D]] | analysis | 2026-06-25 | current |
| [[sources/2026-06-26-pr87-17a-mcp-oauth-authorization-request-boundary-checkpoint\|MCP OAuth Authorization Request Boundary Checkpoint - PR87.17A]] | analysis | 2026-06-26 | current |
| [[sources/2026-06-26-pr87-17b-mcp-oauth-authorization-intent-checkpoint\|MCP OAuth Authorization Intent Storage Checkpoint - PR87.17B]] | analysis | 2026-06-26 | current |
| [[sources/2026-06-26-pr87-17c0-mcp-oauth-login-return-convention-checkpoint\|MCP OAuth Login Return Convention Checkpoint - PR87.17C0]] | analysis | 2026-06-26 | current |
| [[sources/2026-06-27-pr87-17d-mcp-oauth-local-dev-route-adapter-checkpoint\|MCP OAuth Local Dev Route Adapter Checkpoint - PR87.17D]] | analysis | 2026-06-27 | current |
| [[sources/2026-06-26-pr87-17c1-mcp-oauth-login-return-continuation-checkpoint\|MCP OAuth Login Return Continuation Boundary Checkpoint - PR87.17C1]] | analysis | 2026-06-26 | current |
| [[sources/2026-06-25-pr87-16-mcp-account-link-lifecycle-checkpoint\|MCP Account-Link Lifecycle Checkpoint - PR87.16]] | analysis | 2026-06-25 | current |
| [[sources/2026-06-24-cover-letter-mistral-v2-staging-green\|Cover Letter Mistral V2 Staging Green Checkpoint]] | analysis | 2026-06-24 | current |
| [[sources/2026-06-23-twoweeks-mcp-chatgpt-app-sdk-roadmap-checkpoint\|Twoweeks MCP / ChatGPT App SDK Roadmap Checkpoint]] | analysis | 2026-06-23 | current |
---

## Tech

| Page | Résumé | Tags |
|------|--------|------|
| [[tech/import-ocr-pipeline\|Import OCR Pipeline]] | Call path OCR/import et vérité canonique par sections | import, ocr, convex |
| [[tech/export-pipeline\|Export Pipeline]] | Pipeline document final PDF/DOCX séparé du preview DOM | export, pdf, docx |
| [[tech/local-vs-remote-parser-architecture\|Local vs Remote Parser Architecture]] | Séparation debug local / cloud / prod pour le parser | parser, env, production |
| [[tech/preview-to-print-pipeline\|Preview-to-Print Pipeline]] | Parité preview -> print route -> PDF pour resume et proposal | preview, print, pdf |
| [[tech/proposal-ai-routing-and-inline-diff\|Proposal AI Routing and Inline Diff]] | Routing proposal AI, selector models, and inline proofing overlay | proposal, ai, routing |
| [[tech/cv-ats-audit-heuristic\|CV ATS Audit Heuristic]] | Heuristique de santé CV (score/verdict/issue bundle) pour signalements document-level | ats, scoring, quality |
| [[tech/proposal-forge-document-geometry|Proposal Forge Document Geometry]] | Canon page-first: paper width, toolbar/panel alignment, breakpoint stability, preview/edit scrollbars | proposal, forge, geometry |
| [[tech/proposal-signature-closing-layer\|Proposal Signature & Closing Layer]] | Signature/closing comme état structuré + fallback legacy + propagation preview/print/export | proposal, signature |
| [[tech/proposal-style-layer|Proposal Style Layer]] | Base Style 1/2/3, default-slot model, Custom color token path, live boundary note, et reset des personnalisations proposal | proposal, style, tokens |
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
| [[tasks/docx-layout-parity-follow-up\|DOCX Layout Parity Follow-up]] | Deferred DOCX RTL layout, bullets, tables, and font strategy follow-up |
| [[tasks/coffee talk\|Coffee Talk]] | Note courte pour synchroniser la skill Codex collaborateur |
| [[tasks/Audit Workspace — Bonnes Pratiques, Sécurité, RGPD\|Audit Workspace — Bonnes Pratiques, Sécurité, RGPD]] | Audit sauvegardé du workspace |
| [[tasks/2026-06-22-cover-letter-quality-production-roadmap|Cover Letter Quality Production Roadmap]] | Cover-letter generation quality only; Mistral V2 is green on Convex staging `dev:neat-starfish-33`; production and quality repair remain separate/not approved |

---

## Outputs

| Page | Type | Date | Sujet |
|------|------|------|-------|
| [[outputs/2026-05-08-ui-audit-proposal-polish|UI Audit — proposal-polish]] | analysis | 2026-05-08 | Screenshot-only audit of Proposal Forge polish |
| [[outputs/2026-05-26-proposal-language-generation-hardening|Language Pipeline Hardening Checkpoint]] | analysis | 2026-05-26 | Document-language hardening status, smoke checks, and expansion plan |

---

## Archive

| Page | Archivée le | Supersédée par |
|------|-------------|----------------|
| [[archive/concepts/parsing-poc-progress\|Parsing POC Progress]] | 2026-04-15 | [[concepts/cv-parsing-pipeline]] |
| [[archive/entities/cv-forge\|CV Forge (ancienne entité)]] | 2026-04-12 | [[entities/twoweeks]] |

---

## Statistiques

- **Pages actives** : 152 (5 overview, 1 entité, 2 concepts, 8 design, 9 product, 3 strategy, 3 meta, 92 sources, 14 tech, 7 howto, 6 tasks, 2 outputs)
- **Pages archivées** : 2
- **Sources dans `raw/`** : 91
- **Sources en attente dans `rawinput/`** : 0
- **Dernière mise à jour** : 2026-06-25
