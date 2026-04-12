---
title: "Notion Roadmap — CV Forge (document de référence)"
category: source
tags: [roadmap, product, kpi, decision-log, notion, stratégie]
created: 2026-04-10
updated: 2026-04-10
status: current
valid_from: 2026-04-10
valid_until:
superseded_by:
horizon: present
version: v1
type: document
sources: []
related: [[cv-forge]], [[product-roadmap]], [[kpis]]
---

# Notion Roadmap — CV Forge (document de référence)

**Type** : Document de référence produit
**Auteur** : Inconnu (partagé par l'utilisateur)
**Date** : 2026-04-10

## Résumé

Document complet de roadmap produit pour CV Forge, structuré pour import dans Notion. Couvre 16 initiatives sur 4 phases de priorité (P0→P3), 16 KPIs de suivi, 8 décisions stratégiques, les schémas des 3 bases Notion, et un rituel opérationnel hebdomadaire.

## Points clés

1. **Stratégie en 4 axes** : Gagner la confiance au premier usage → Gagner la supériorité d'édition → Gagner l'usage récurrent → Gagner commercialement

2. **P0 (priorité maximale)** : 4 initiatives critiques — Import recovery layer, Quick-start guided path, AI interaction rulebook, Editor↔preview linking. Toutes en lien avec la confiance utilisateur au premier run.

3. **Le parsing n'est pas seulement un problème technique** : Décision clé — "Treat import trust as a product UX problem, not only a parser problem". La solution passe par une UX de recovery (confidence scoring, uncertain-block review), pas seulement l'amélioration du parser.

4. **Structure Notion recommandée** : 3 bases de données — Product Roadmap (16 propriétés), KPI Tracker (8 propriétés), Decision Log (10 propriétés). Schemas complets documentés dans la source.

5. **16 KPIs définis** par catégorie : Activation (Visitor→First Draft, Time to First Draft, Proposal Draft Completion), Import (Import Completion, Review Completion, Parser Error Rate), AI (Accept Rate, Undo Rate), Trust (Export Readiness), Conversion (Export Initiation, Paywall Conversion), Retention (Documents/User, Jobs/User, Duplicate Usage, D7/D30).

6. **8 décisions de produit formalisées** : structured editor comme source de vérité, 3 tones seulement en UI, pas de gallery de templates, quick-start path, onboarding progressif, import trust = UX problem, AI standardization, framing "Cover letter / Proposal".

7. **Modèle d'ownership lean** : Product/Founder (quick-start, roadmap, packaging), Product Design (import recovery UX, editor-preview, onboarding, templates), Engineering (parser, confidence scoring, extension handoff), AI/Prompt (rulebook, quality), Growth (landing page, pricing).

## Implications pour twoweeks

- La roadmap confirme que la **priorité absolue** est de résoudre la confiance au premier run via l'import recovery — le parser doit être entouré d'une UX de transparence et de récupération.
- Le **structured skeleton editor** est une décision validée : ne pas pivoter vers preview-first sauf échec flagrant en tests utilisateurs.
- Les **3 tones** (Balanced/Warm/Formal) sont figés en UI ; la nuance se passe sous le capot.
- La **Jobs layer** (P2) est identifiée comme un "moat builder" — à préserver dans la vision même si différée.
- L'**extension Chrome** vers app est stratégiquement importante (P1) — à soigner dès Phase 2.

## Pages wiki mises à jour

- [[product-roadmap]] — créé depuis ce document
- [[kpis]] — créé depuis ce document
- [[cv-forge]] — enrichi avec la vision roadmap et les décisions
