---
title: "Vue d'ensemble — twoweeks / CV Forge"
category: overview
tags: [project, overview, cvforge, roadmap]
created: 2026-04-09
updated: 2026-04-10
sources: [2026-04-09-decisions-cvforge-sprint, 2026-04-10-notion-roadmap-cvforge, 2026-04-10-success-blueprint, 2026-04-10-benchmark-matrix, 2026-04-10-gap-analysis]
---

# twoweeks — Vue d'ensemble

## Diagnostic compétitif (gap analysis)

> **"TwoWeeks is currently closer to the better product, but it is still missing the conversion scaffolding and import trust layer needed to beat a simpler commercial funnel like ResumeLab."**

Voir [[gap-analysis]] pour le diagnostic complet, les 3 cycles d'exécution, et le détail keep/change/avoid/defer.

---

## Qu'est-ce que twoweeks / CV Forge ?

**CV Forge** (projet twoweeks) est une application de parsing, normalisation et édition de CVs, avec génération de propositions/cover letters adaptées à une offre d'emploi. Elle ingère des CVs bruts (via OCR/upload), les découpe en sections structurées par famille (identity, education, experience…), et permet à l'utilisateur de les éditer, reformater et exporter. Un export Chrome vers l'app est également en développement.

## Architecture technique

Le pipeline central : **OCR → heuristiques de parsing → sections normalisées par famille → UI d'édition skeleton**.

Décision d'architecture : **structured skeleton editor** comme source de vérité (pas preview-first). Le preview est un miroir interactif, pas l'éditeur principal. Le POC sur extraction JSON structurée (schema-first) reste en décision ouverte.

## Stratégie produit

Quatre axes séquencés (voir [[product-roadmap]]) :

1. **Gagner la confiance au premier run** — import recovery, quick-start flow, AI cohérent
2. **Gagner la supériorité d'édition** — structured editor + preview linking + typographie premium
3. **Gagner l'usage récurrent** — jobs first-class, duplicate/retarget, versioning
4. **Gagner commercialement** — premium value clair, market story

## État du projet

| Dimension | Statut |
|-----------|--------|
| Stade | 🟡 En développement actif |
| Phase produit | Phase 1 (P0) — confiance et fondations |
| Sprint actuel | Stabilisation pipeline save, bugs UI, décision architecture parser |
| Sources ingérées | 7 |
| Pages wiki | 19 |
| Dernière activité | 2026-04-10 |

## Décisions actives

- **Architecture parser** : POC hybride (heuristiques + JSON structuré sur une famille) avant tout pivot
- **Import trust** : traiter comme un problème UX (recovery UI, confidence scoring) — pas seulement améliorer le parser
- **AI behavior** : standardiser via rulebook (quand modal, quand 1 vs 3 options, contrôles replace/insert/keep)
- **CVs synthétiques** : après le patch actuel, pas avant
- **Features immédiates** : Download Raw OCR Markdown + Download Normalized JSON
- **Features déférées** : AI rewrite suggestions, Destination Summary Pane, Jobs layer

## Thèmes majeurs du wiki

- [[cv-parsing-pipeline]] — stratégie d'évolution du parser
- [[cv-families]] — les familles de sections CV et leur stabilité
- [[cv-forge]] — l'application et ses composants UI
- [[product-roadmap]] — roadmap complète par phase et priorité
- [[kpis]] — 16 métriques de succès par catégorie
- [[product-vision]] — blueprint complet : modèle hybride funnel+éditeur, 5 objets produit, parcours, IA, import
- [[benchmark-matrix]] — scoring 12 catégories vs ResumeLab + seuils non-négociables
- [[ai-product-model]] — 3 modes IA, 5 règles d'interaction, cadre qualité writing
- [[gap-analysis]] — diagnostic vs ResumeLab, priority order, 3 cycles, keep/change/avoid/defer

## Questions ouvertes

- [ ] Résultats du POC JSON structuré sur IDENTITY/CONTACT — meilleur que les heuristiques ?
- [ ] Quelles contaminations restent à isoler après le sprint actuel ?
- [ ] Framing "Cover letter / Proposal" vs "Application letter" — tests de compréhension à faire
- [ ] Timing pour l'Extension-to-app handoff polish (P1 Phase 2)
- [ ] Score benchmark actuel de TwoWeeks sur les 12 catégories — quelle est la baseline ?
- [ ] AI Undo Rate actuel — mesurable ? L'asymétrie toolbar vs proposal AI est-elle chiffrée ?
- [ ] Path C (gap analysis formelle vs ResumeLab) — à ingérer quand disponible

---

*Mise à jour automatique par le LLM · 2026-04-10*
