---
title: "KPIs — twoweeks"
category: product
tags: [kpi, métriques, activation, rétention, conversion, import, ai, jobs, match]
created: 2026-04-10
updated: 2026-04-27
status: current
valid_from: 2026-04-10
version: v1
sources: [2026-04-10-notion-roadmap-cvforge, 2026-04-27-job-library-prd, 2026-04-27-job-match-validation-contract]
related: [[entities/twoweeks]], [[product/product-roadmap]], [[product/job-library]], [[product/job-match-review]]
---

# KPIs — twoweeks

16 métriques clés organisées par catégorie. Toutes sans valeurs cibles définies pour l'instant (à remplir après mise en place de l'analytics).

---

## Activation

| KPI | Direction | Cadence | Contexte |
|-----|-----------|---------|----------|
| Visitor → First Draft Rate | ↑ | Weekly | KPI d'activation core |
| Time to First Draft | ↓ | Weekly | Doit baisser après le quick-start |
| Proposal Draft Completion Rate | ↑ | Weekly | KPI de valeur core |

---

## Import

| KPI | Direction | Cadence | Contexte |
|-----|-----------|---------|----------|
| Resume Import Completion Rate | ↑ | Weekly | Métrique de confiance sensible |
| Resume Import Review Completion Rate | ↑ | Weekly | Indique la qualité de l'UX de recovery |
| Parser Error / Uncertain Block Rate | ↓ | Weekly | Doit décliner avec le temps |

---

## AI

| KPI | Direction | Cadence | Contexte |
|-----|-----------|---------|----------|
| AI Rewrite Accept Rate | ↑ | Weekly | Signal clé d'utilité |
| AI Undo Rate | ↓ | Weekly | Proxy fort pour output de mauvaise qualité |

---

## Trust

| KPI | Direction | Cadence | Contexte |
|-----|-----------|---------|----------|
| Export Readiness Completion Rate | ↑ | Weekly | Mesure la confiance avant export |

---

## Conversion

| KPI | Direction | Cadence | Contexte |
|-----|-----------|---------|----------|
| Export Initiation Rate | ↑ | Weekly | Indique l'intention de compléter |
| Paywall Conversion Rate | ↑ | Weekly | KPI business core |

---

## Rétention

| KPI | Direction | Cadence | Contexte |
|-----|-----------|---------|----------|
| Documents per User | ↑ | Monthly | Indique l'usage en companion réel |
| Jobs Imported per User | ↑ | Monthly | Mesure l'usage job-centric |
| Duplicate / Retarget Usage Rate | ↑ | Monthly | Signal fort d'utilité récurrente |
| D7 Retention | ↑ | Weekly | Benchmark clé |
| D30 Retention | ↑ | Monthly | Signal long terme du produit |

---

## Jobs et Match Review

| KPI | Direction | Cadence | Contexte |
|-----|-----------|---------|----------|
| Job Saved Rate | ↑ | Weekly | Mesure la capacité extension/app à créer une bibliothèque utile |
| Job to First Document Time | ↓ | Weekly | Temps entre job sauvegardé et premier document lié |
| Cover Letter from Saved Job Rate | ↑ | Weekly | Conversion de Job Library vers génération de cover letter |
| Linked Documents per Job | ↑ | Monthly | Signal de réutilisation par opportunité |
| Match False-zero Rate | ↓ | Per dogfood batch | 0 sur les évidences positives obvious en beta interne |
| Match Contradiction Rate | ↓ | Per dogfood batch | 0 contradiction critique verdict/raisons |
| Match Copy Safety Incidents | ↓ | Per dogfood batch | 0 PII/raw evidence/debug phrase visible |
| Time to Match Decision | ↓ | Per dogfood batch | Comprendre pertinence, raison et next step en moins de 5 secondes |

---

## Sources de données

- Product analytics (activation, export, proposals)
- Import funnel events (import completion, review completion)
- Parsing logs (parser error rate)
- AI action events (accept rate, undo rate)
- Extension + app (jobs imported)
- Billing funnel (paywall conversion)
- Workspace analytics (documents/user)
- Document actions (duplicate/retarget)
- User analytics (D7/D30)
- Job Library events
- Match Review dogfood exports and labels

---

## Notes d'implémentation

- Le **AI Undo Rate** est un proxy fort mais indirect — à surveiller en complement du Accept Rate.
- La **Resume Import Review Completion Rate** est distincte de l'Import Completion Rate : elle mesure si les utilisateurs terminent le flow de review des blocs incertains, pas juste l'import initial.
- Les **métriques Retention mensuelles** (Documents/User, Jobs/User) nécessitent un workspace stable — dépendent de la Phase 2-3.

---

## Voir aussi

- [[product/product-roadmap]] — initiatives liées à chaque KPI
- [[product/job-library]] — couche jobs first-class
- [[product/job-match-review]] — review match user-facing
