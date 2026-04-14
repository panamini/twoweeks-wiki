---
title: "Timeline — twoweeks"
category: overview
tags: [timeline, chronologie, projet]
created: 2026-04-09
updated: 2026-04-14
---

# Timeline du projet twoweeks

Chronologie des événements-clés du projet : décisions prises, pivots, sorties de versions, changements d'orientation. Ce n'est pas un log d'opérations wiki (voir `log.md`) — c'est l'histoire du **projet lui-même**.

Utilisé par le LLM pour répondre à des questions temporelles : "qu'avions-nous décidé avant X ?" ou "quel était l'état en v1 ?".

---

## Format d'une entrée

```text
## [YYYY-MM-DD] type | Titre de l'événement
**Type** : decision | pivot | release | discovery | deprecation | milestone
**Version** : v1 | v2 | ...
**Impact** : pages wiki affectées
Description courte de l'événement et de son contexte.
```

---

## Événements

## [2026-04-09] milestone | Initialisation du wiki twoweeks
**Type** : milestone
**Version** : v0
**Impact** : Création de l'ensemble de la structure wiki (CLAUDE.md, index, log, overview, rawinput, archive)

Création de l'espace Obsidian LLM Wiki pour le projet twoweeks. Architecture v2 adoptée d'emblée : staging `rawinput/`, gestion temporelle avec statuts et archive.

## [2026-04-10] decision | Refonte du système de tones : 4 tones avec Auto
**Type** : decision
**Version** : v1
**Impact** : [[concepts/ai-product-model]], [[concepts/product-roadmap]], [[concepts/gap-analysis]]

Remplacement des 3 tones initiaux par 4 tones : **Auto**, **Natural**, **Formal**, **Warm**. Le mode Auto devient le point d'entrée recommandé.

## [2026-04-12] decision | Renommage entité principale : CV Forge -> twoweeks
**Type** : update
**Version** : v1
**Impact** : [[archive/entities/cv-forge]] -> [[entities/twoweeks]]

Le produit s'appelle **twoweeks** (twoweeks.ai), pas **CV Forge**. CVForge et ProposalForge restent des modules internes. La brand bible 2026 fixe le tagline "Finish. Faster." et le positionnement Anti-Work tool.

## [2026-04-14] decision | `sections[*].structuredContent` devient la vérité canonique produit
**Type** : decision
**Version** : v1
**Impact** : [[concepts/cv-parsing-pipeline]], [[concepts/cv-families]], [[tech/import-ocr-pipeline]], [[entities/twoweeks]]

Le pipeline parsing est désormais documenté comme architecture structurée par familles. Quand elles existent et sont valides, les sections structurées priment sur les tableaux top-level de compatibilité ou d'export.

## [2026-04-14] discovery | Clarification des modes local vs cloud pour le parser
**Type** : discovery
**Version** : v1
**Impact** : [[tech/local-vs-remote-parser-architecture]], [[howto/local-parser-operations]], [[tech/import-ocr-pipeline]]

Le debug parser/OCR doit passer par la boucle locale complète `frontend local + Convex local + parser local`. En preview/prod, le parser doit rester une URL publique configurée par env ; le localhost ne doit jamais fuiter hors du mode dev.
