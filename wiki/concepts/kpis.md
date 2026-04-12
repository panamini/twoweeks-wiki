---
title: "KPIs — CV Forge"
category: concept
tags: [kpi, métriques, activation, rétention, conversion, import, ai]
created: 2026-04-10
updated: 2026-04-10
status: current
valid_from: 2026-04-10
valid_until:
superseded_by:
horizon: present
version: v1
sources: [2026-04-10-notion-roadmap-cvforge]
related: [[cv-forge]], [[product-roadmap]]
---

# KPIs — CV Forge

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

---

## Notes d'implémentation

- Le **AI Undo Rate** est un proxy fort mais indirect — à surveiller en complement du Accept Rate.
- La **Resume Import Review Completion Rate** est distincte de l'Import Completion Rate : elle mesure si les utilisateurs terminent le flow de review des blocs incertains, pas juste l'import initial.
- Les **métriques Retention mensuelles** (Documents/User, Jobs/User) nécessitent un workspace stable — dépendent de la Phase 2-3.

---

## Voir aussi

- [[product-roadmap]] — initiatives liées à chaque KPI
- [[cv-forge]] — entité produit
