---
title: "Benchmark Matrix — Évaluation produit"
category: concept
tags: [benchmark, scoring, compétiteurs, resumelab, stratégie, qualité]
created: 2026-04-10
updated: 2026-04-10
status: current
valid_from: 2026-04-10
valid_until:
superseded_by:
horizon: present
version: v1
sources: [2026-04-10-benchmark-matrix]
related: [[cv-forge]], [[product-roadmap]], [[product-vision]]
---

# Benchmark Matrix — Évaluation produit

Système de scoring pour évaluer TwoWeeks, ResumeLab, et tout concurrent ou redesign avant shipping. La vraie question : **"Which product gets more users to a credible result faster, while still making them want to stay?"**

---

## Méthode de scoring

Chaque catégorie reçoit un score 1–10 :
- 1–3 : weak / broken / market-losing
- 4–5 : usable but not competitive
- 6–7 : good enough to compete
- **8 : strong advantage**
- **9 : category-leading**
- **10 : exceptional / difficult to replicate**

**Weighted score = (score ÷ 10) × poids**
**Total = 100 points**

---

## Matrice complète

| Catégorie | Poids | Ce qu'elle mesure |
|-----------|-------|-------------------|
| UX / Flow | 18 | Clarté, progression, task completion, architecture d'édition, error recovery |
| AI Quality + AI UX | 16 | Output quality, control model, trust, latency, mode design |
| Conversion / Monetization | 12 | First-session conversion, offer clarity, paywall timing, funnel discipline |
| Import / Parsing / Data Reliability | 10 | Accuracy, glyph resilience, cleanup UX, job import quality |
| UI / Visual System | 10 | Readability, hierarchy, emotional polish, accessibility, consistency |
| Onboarding / Activation | 9 | First-run clarity, time to first value, contextual guidance, reassurance |
| Retention / Long-term Value | 9 | Multi-doc management, reusability, repeat-job workflow, companion value |
| Universality / Market Coverage | 6 | Beginner + advanced, international, career breadth |
| Marketing / Positioning | 5 | Category clarity, promise strength, differentiation, consistency |
| Defensibility | 5 | Proprietary workflow, design moat, data reuse, distribution edge |
| Performance / Ergonomics | 5 | Responsiveness, editing comfort, interaction predictability |
| Brand Trust / Professional Safety | 5 | Output credibility, product seriousness, template employability |
| **Total** | **100** | |

---

## Seuils non-négociables

**Un produit ne devrait pas être poussé commercialement si :**

| Catégorie | Seuil minimum |
|-----------|---------------|
| Import / Parsing | < 6 |
| UX / Flow | < 7 |
| AI Quality + AI UX | < 7 |
| Conversion / Monetization | < 6 |
| Brand Trust | < 7 |

> "One weak trust gateway can cancel all your design and AI effort."

---

## Tiers stratégiques pour TwoWeeks

**Tier 1 — must win** : UX/Flow, AI Quality+AI UX, Import/Parsing/Reliability, Conversion/Monetization, Retention/Long-term Value

**Tier 2 — strong differentiators** : UI/Visual System, Onboarding/Activation, Defensibility, Performance/Ergonomics

**Tier 3 — important mais pas suffisant seul** : Marketing/Positioning, Universality, Brand Trust/Safety

---

## Interprétation des scores finaux

| Score final | Signification |
|-------------|--------------|
| 85–100 | Category leader / very hard to beat |
| 75–84 | Strong product with clear market potential |
| 65–74 | Competitive but has obvious weaknesses |
| 55–64 | Usable, but likely loses to sharper competitors |
| < 55 | Product-market friction is too high |

Pour le marché de TwoWeeks : **< 70 = not ready to dominate · 75+ = strong contender · 80+ = serious market threat · 85+ = category-defining**

---

## Verdict actuel (avant gap analysis formelle)

### ResumeLab gagne aujourd'hui sur :
- Activation et beginner reassurance
- Guided conversion
- Perceived safety du first-run path
- Hiding complexity

### TwoWeeks peut gagner sur :
- Long-term product architecture
- Serious editing ergonomics
- Visual sophistication + AI embeddedness
- Multi-document utility
- Future defensibility et eventual retention

### Tension stratégique centrale :
> "You are building the better machine, but the market often rewards the product that feels easier in minute 1."

---

## Bons paris identifiés

- Structured editor (pas template-chaos editing) ✓
- Live preview ✓
- Chrome extension / direct job import ✓
- Embedded AI dans la selection toolbar ✓
- 3 tones (pas 6 pseudo-tones) ✓
- Forte typographie ✓
- Direction multi-document / companion ✓

## Paris risqués

- Editor-first power sans guided activation
- Weak parser/import trust
- AI quality inégale entre surfaces
- Trop de minimalism si les actions/états ne sont pas évidents
- Manque d'handholding au first-run
- Gap d'intimidation entre design élite et utilisateurs ordinaires

---

## Template de scorecard

À utiliser pour chaque audit de produit :

| Catégorie | Poids | Score (1–10) | Résultat pondéré | Notes |
|-----------|-------|--------------|-----------------|-------|
| UX / Flow | 18 | | | |
| UI / Visual System | 10 | | | |
| AI Quality + AI UX | 16 | | | |
| Import / Parsing / Reliability | 10 | | | |
| Onboarding / Activation | 9 | | | |
| Conversion / Monetization | 12 | | | |
| Retention / Long-term Value | 9 | | | |
| Universality / Market Coverage | 6 | | | |
| Marketing / Positioning | 5 | | | |
| Defensibility | 5 | | | |
| Performance / Ergonomics | 5 | | | |
| Brand Trust / Professional Safety | 5 | | | |
| **Total** | **100** | | | |

---

## Voir aussi

- [[product-vision]] — le blueprint du produit idéal
- [[product-roadmap]] — les initiatives pour combler les gaps
- [[kpis]] — métriques liées aux catégories du benchmark
