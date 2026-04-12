---
title: "Index du Wiki — twoweeks / CV Forge"
category: overview
updated: 2026-04-12
---

# Index du Wiki · twoweeks / CV Forge (v2)

Catalogue complet de toutes les pages **actives** du wiki (status: current ou planned). Les pages archivées sont dans `wiki/archive/`.

---

## Vue d'ensemble

| Fichier | Description | Status |
|---------|-------------|--------|
| [[overview]] | Synthèse générale — CV Forge, état du projet, décisions actives | current |
| [[log]] | Journal chronologique des opérations wiki | — |
| [[timeline]] | Chronologie des événements du projet | — |

---

## Entités

| Page | Résumé | Status | Version |
|------|--------|--------|---------|
| [[entities/cv-forge\|CV Forge]] | L'application — parser, normalisation et édition de CVs | current | v2 |

---

## Concepts

| Page | Résumé | Status | Tags |
|------|--------|--------|------|
| [[concepts/cv-parsing-pipeline\|CV Parsing Pipeline]] | Stratégie d'évolution du parser : heuristiques vs JSON structuré, POC hybride | current | parser, architecture |
| [[concepts/cv-families\|CV Families]] | Familles de sections CV, stabilité, contamination, fixtures synthétiques | current | parser, sections |
| [[concepts/parsing-poc-progress\|Parsing POC Progress]] | État du POC parsing par famille (Experience/Education/Languages/Skills ✅, IDENTITY/CONTACT 🟡) | current | parsing, poc, familles |
| [[concepts/llm-wiki-pattern\|LLM Wiki Pattern]] | Pattern de base de connaissance persistante maintenue par un LLM | current | meta, workflow |
| [[concepts/temporal-management\|Gestion temporelle]] | Mécanisme de distinction passé/présent/futur dans le wiki | current | temporal, architecture |
| [[concepts/product-roadmap\|Product Roadmap]] | 16 initiatives sur 4 phases (P0→P3), décisions figées, stratégie produit | current | roadmap, product |
| [[concepts/kpis\|KPIs]] | 16 métriques de succès par catégorie | current | kpi, métriques |
| [[concepts/product-vision\|Product Vision]] | Modèle hybride funnel+éditeur, 5 objets produit, 3 parcours, IA, monétisation | current | vision, architecture |
| [[concepts/benchmark-matrix\|Benchmark Matrix]] | Scoring 12 catégories pondérées + seuils non-négociables | current | benchmark, scoring |
| [[concepts/ai-product-model\|AI Product Model]] | 3 modes IA, tones Auto/Natural/Formal/Warm, cadre qualité writing | current | ai, ux, modes |
| [[concepts/gap-analysis\|Gap Analysis]] | Diagnostic vs ResumeLab : 6 blockers, 10 gaps, 3 cycles | current | gap, diagnostic |

---

## Sources

| Page | Type | Date | Status |
|------|------|------|--------|
| [[sources/2026-04-09-decisions-cvforge-sprint\|Décisions sprint CV Forge]] | conversation | 2026-04-09 | current |
| [[sources/2026-04-09-tweet-karpathy-llm-wiki\|Tweet Karpathy — LLM Knowledge Bases]] | tweet | 2026-04-09 | current |
| [[sources/2026-04-09-wiki-paste-llm-wiki\|Wiki Paste — LLM Wiki]] | document | 2026-04-09 | current |
| [[sources/2026-04-10-notion-roadmap-cvforge\|Notion Roadmap — CV Forge]] | document | 2026-04-10 | current |
| [[sources/2026-04-10-benchmark-matrix\|Ideal Benchmark Matrix — Path A]] | document | 2026-04-10 | current |
| [[sources/2026-04-10-success-blueprint\|Success Blueprint — Path B]] | document | 2026-04-10 | current |
| [[sources/2026-04-10-gap-analysis\|Gap Analysis — Path C]] | document | 2026-04-10 | current |
| [[sources/2026-04-11-cv-parsing-poc-state\|CV Parsing POC State — Checkpoint]] | spec | 2026-04-11 | current |
| [[sources/2026-04-11-todo-sprint\|Sprint Notes — 2026-04-11]] | conversation | 2026-04-11 | current |
| [[sources/2026-04-11-jessica-helen-poc-state\|Jessica/Helen POC State]] | document | 2026-04-11 | current |

---

## Tech (référence technique — architecture, call paths, infra)

| Page | Résumé | Tags |
|------|--------|------|
| [[tech/import-ocr-pipeline\|Import OCR Pipeline]] | Chemin StructuredUploadButton → Convex → canonicalize → parser | import, ocr, convex |

---

## Howto (runbooks opérationnels)

| Page | Résumé | Tags |
|------|--------|------|
| [[howto/cloudflare-zero-trust-tunnel\|Cloudflare Zero Trust + Tunnel]] | Runbook parser.dasti.ai : CF Access, tunnel, DNS, token, WAF, connector, Convex env, smoke tests | cloudflare, devops |

---

## Todo List & Kanban

| Page | Résumé |
|------|--------|
| [[to do list/kanban\|Kanban Sprint]] | Backlog / En cours / Bugs ouverts / Done — sprint actuel CV Forge |

---

## Outputs

| Page | Type | Date | Sujet |
|------|------|------|-------|
| [[outputs/2026-04-09-architecture-v2\|Architecture v2]] | decision | 2026-04-09 | rawinput/ + gestion temporelle |

---

## Archive

*(vide — aucune page archivée pour l'instant)*

---

## Statistiques

- **Pages actives** : 27 (3 overview, 1 entité, 11 concepts, 10 sources, 1 tech, 1 howto, 1 kanban, 1 output)
- **Pages archivées** : 0
- **Sources dans `raw/`** : 9
- **Sources en attente dans `rawinput/`** : 0
- **Dernière mise à jour** : 2026-04-12
