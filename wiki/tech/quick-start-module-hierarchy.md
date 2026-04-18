---
title: "Quick Start Module Hierarchy"
category: tech
tags: [quick-start, onboarding, route-state, proposal, app-shell, ui]
created: 2026-04-18
updated: 2026-04-18
status: current
valid_from: 2026-04-18
valid_until:
superseded_by:
horizon: present
version: v1
sources: [2026-04-18-quick-start-module-hierarchy]
related: [[product/product-roadmap]], [[strategy/gap-analysis]], [[entities/twoweeks]]
---

# Quick Start Module Hierarchy

Le module Quick Start est un flow d'activation a l'echelle de l'app-shell. Il n'existe pas comme modal overlay generique. Le shell, l'entree cover-letter et le composant de cartes partagees sont separes par couche.

## These

- Quick Start = etat de content pane controle par `App.tsx`, pas route/page dediee
- `/proposal` peut entrer en cold start cover-letter via `proposalEntryIntent`
- une primitive `QuickStartChoiceCard` est partagee entre Resume et Cover letter
- les etats de route sont transitoires et ne passent pas par un stockage durable

## Architecture active

1. `src/App.tsx` lit `readQuickStartRouteState(location.state)` et remplace le routed content pane quand `quickStartRouteState.isOpen`
2. `src/lib/quick-start-routing.ts` encode `createType`, `resumeMode`, `returnTarget` via `createQuickStartLocationState(...)` et `clearQuickStartLocationState(...)`
3. `src/components/onboarding/QuickStartFlow.tsx` gere l'etat `What are you starting?` puis le sous-flux Resume
4. `src/pages/ProposalForge.tsx` n'active le cold start cover-letter que si compose view + intent `cover-letter-start` + pas de handoff/CV/draft
5. `src/components/CoverLetterStartSurface.tsx` gere le flux centre `Bring in the job` / `Bring in your resume`
6. `src/components/onboarding/QuickStartChoiceCard.tsx` et `src/styles/product.css` donnent la primitive partagee et les tokens visuels
7. `--quick-start-sheet-inline-size` fixe la largeur commune de la surface
8. les cartes restent `width: 100%` a l'interieur du sheet pour maintenir la coherence de mise en page

## Invariants critiques

- no new storage
- no new parser path
- no modal/backdrop system for Quick Start
- resume import retains trusted Mistral path and existing `importCv` semantics
- cover-letter flow must rewind into app-shell Quick Start when entered from `cover-letter-start`

## Boundaries de debug

1. route state creation/clearance in `quick-start-routing.ts`
2. shell visibility in `App.tsx`
3. resume starter flow in `QuickStartFlow.tsx`
4. cold start gating in `ProposalForge.tsx`
5. centered sheet / width tokens in `product.css`
6. back navigation between cover-letter root and app-shell Quick Start

## Consequences produit

This architecture makes onboarding less confusing and keeps the editor shell visible, while preserving the proposal cold start as a narrow, intentional activation path. It also keeps the final remaining gap centered on first-run onboarding and visual refinement, not on core routing.

## Voir aussi

- [[product/product-roadmap]]
- [[strategy/gap-analysis]]
- [[entities/twoweeks]]
