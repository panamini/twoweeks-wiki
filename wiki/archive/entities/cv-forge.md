---
title: "CV Forge"
category: entity
tags: [cvforge, app, product, parser, cv, roadmap, vision, benchmark]
created: 2026-04-09
updated: 2026-04-10
status: archived
valid_from: 2026-04-09
valid_until: 2026-04-12
superseded_by: [[twoweeks]]
horizon: present
version: v2
sources: [2026-04-09-decisions-cvforge-sprint, 2026-04-10-notion-roadmap-cvforge, 2026-04-10-success-blueprint, 2026-04-10-benchmark-matrix]
related: [[cv-parsing-pipeline]], [[cv-families]], [[overview]], [[product-roadmap]], [[kpis]], [[product-vision]], [[benchmark-matrix]], [[ai-product-model]]
---

# CV Forge

CV Forge est l'application principale du projet twoweeks — un outil de parsing, normalisation et édition de CVs.

## Description

CV Forge ingère des CVs (via OCR/upload), les parse en sections structurées ([[cv-families]]), et permet à l'utilisateur de les éditer, reformater et exporter. Le cœur technique est un pipeline de parsing qui transforme du texte brut OCR en données structurées JSON par famille de section.

## Position sur le marché

**TwoWeeks est un job application operating system**, pas seulement un resume builder. Sa différenciation vs ResumeLab : meilleure architecture long terme, editing ergonomics supérieures, AI embeddée dans le workflow, direction multi-document/companion.

**Positionnement** : "The fastest way to turn your experience into premium, job-ready applications."

**Modèle hybride** : Guided activation funnel (convertir) + Structured editor workspace (retenir). Ne pas choisir l'un ou l'autre.

Voir [[benchmark-matrix]] pour l'évaluation comparative et [[product-vision]] pour le blueprint complet.

## Architecture actuelle (v0)

- **Pipeline** : OCR → heuristiques de parsing → sections normalisées → UI d'édition
- **Export** : prévu — Download Raw OCR Markdown + Download Normalized JSON
- **Editing** : Output shell + compose shell + card header line

## Composants UI principaux

| Composant | Rôle |
|-----------|------|
| Output shell | Affichage du CV parsé, mode preview et edit |
| Compose shell | Zone de saisie/édition de sections |
| Card header line | Toolbar de navigation/action sur les sections |
| Recovery drawer | Gestion des sections non parsées / fallback |

## État du développement

Sprint actuel : stabilisation du pipeline save, bugs d'alignement UI, décision architecture parser (heuristiques vs JSON structuré).

Features en attente : AI rewrite suggestions (2–3 par section), Destination Summary Pane.

## Décisions techniques ouvertes

- Architecture parser : continuer heuristiques vs hybride (POC JSON sur une famille) vs pivot complet — **reco actuelle : POC hybride**
- Timing CVs synthétiques pour tests : après patch actuel + isolation prochaine contamination family

## Roadmap produit

Voir [[product-roadmap]] pour le détail complet. Résumé des phases :

- **Phase 1 (P0)** : Import recovery layer, Quick-start guided path, AI interaction rulebook, Editor↔preview linking
- **Phase 2 (P1)** : Onboarding progressif, Document health/readiness, Template switcher, Extension handoff, Premium packaging, Proposal framing
- **Phase 3 (P2)** : Jobs as first-class object, Duplicate/retarget, Versioning, Advanced tone modifiers
- **Phase 4 (P3)** : Landing page + market story, Template expansion

## Stratégie

1. **Gagner la confiance au premier run** — import recovery, quick-start, AI cohérent
2. **Gagner la supériorité d'édition** — structured editor + preview linking + AI contextuel
3. **Gagner l'usage récurrent** — jobs, duplicate/retarget, versioning
4. **Gagner commercialement** — premium value clair, market story

## Décisions produit figées

| Décision | Statut |
|----------|--------|
| Structured skeleton editor = source de vérité | Approuvé |
| 3 tones en UI (Balanced/Warm/Formal) | Approuvé |
| Pas de gallery de templates | Approuvé |
| Quick-start path | Approuvé |
| Import trust = UX problem (pas seulement parser) | Approuvé |
| AI standardisation via rulebook | Approuvé |

## KPIs principaux

Voir [[kpis]] pour le détail. KPIs critiques : Visitor→First Draft Rate, Import Completion Rate, AI Accept Rate, Paywall Conversion, D7/D30 Retention.

## Architecture cible — 5 objets produit

L'évolution vers un "application system" passe par 5 objets distincts (voir [[product-vision]]) :
- **Profile** — identité core réutilisable
- **Experience Library** — bullet bank + achievement bank par rôle
- **Job Record** — objet normalisé avec keywords + tone cues
- **Resume Variant** — output spécifique lié à un ou plusieurs jobs
- **Cover Letter / Proposal Variant** — doc ciblé avec version history

## Voir aussi

- [[cv-parsing-pipeline]] — la stratégie d'évolution du parser
- [[cv-families]] — les familles de sections CV
- [[product-roadmap]] — roadmap complète par phase
- [[kpis]] — métriques de succès
- [[product-vision]] — blueprint complet (funnel+éditeur, objets, IA, import, onboarding)
- [[benchmark-matrix]] — système de scoring et positionnement vs ResumeLab
- [[ai-product-model]] — 3 modes IA, 5 règles, cadre de qualité writing
