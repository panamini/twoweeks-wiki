---
title: "Quick Start Module Hierarchy"
category: source
tags: [quick-start, onboarding, app-shell, route-state, proposal, ui]
created: 2026-04-18
updated: 2026-04-18
status: current
valid_from: 2026-04-18
valid_until:
superseded_by:
horizon: present
version: v1
type: spec
sources: []
related: [[tech/quick-start-module-hierarchy]], [[product/product-roadmap]], [[strategy/gap-analysis]]
---

# Quick Start Module Hierarchy
**Type** : Architecture note
**Date** : 2026-04-18
**URL** : source locale `raw/Quick Start Module Hierarchy.md`

## Resume

Note d'architecture sur le module Quick Start de twoweeks. Elle clarifie que le flow d'activation n'est pas une modale globale ni un overlay de page : c'est un état du content pane piloté par l'app-shell. Le cold start cover-letter vit dans `/proposal` comme un état d'entrée intentionnel, et les choix primaires utilisent une primitive de carte commune.

## Points cles

1. `src/App.tsx` possède l'ouverture et la fermeture de Quick Start via `readQuickStartRouteState(location.state)`.
2. Les états transitoires vivent dans `src/lib/quick-start-routing.ts` sans stockage persistant.
3. `QuickStartFlow.tsx` guide le démarrage Resume/Cover letter et garde le chemin d'import Mistral existant.
4. `ProposalForge.tsx` héberge le cold start cover-letter seulement dans les conditions explicites de départ.
5. `CoverLetterStartSurface.tsx` gère le sous-flux centré job/resume et le retour vers l'app-shell Quick Start.
6. `QuickStartChoiceCard.tsx` et `src/styles/product.css` forment la primitive commune et le système visuel partagé.

## Implications pour twoweeks

- Quick Start doit être pensé comme un état d'app-shell visible, pas comme une modale superposée.
- Le démarrage cover-letter ne doit pas polluer le shell principal tant qu'un cold start n'est pas activé.
- Le même composant de choix doit rester utilisé pour les chemins resume et proposal afin d'éviter la fragmentation de l'UI.
- Le vrai reliquat produit après ce shell est l'onboarding de première session, pas le routage primaire.

## Extraits notables

- "Quick Start as an app-shell content-pane state"
- "Cover-letter cold start as an intentional `/proposal` entry state"
- "one semantic choice-card primitive"

## Pages wiki mises à jour

- [[tech/quick-start-module-hierarchy]]
