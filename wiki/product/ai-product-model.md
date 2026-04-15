---
title: "AI Product Model — Modes, règles et qualité"
category: product
tags: [ai, ux, modes, toolbar, rulebook, qualité, writing, suggestion]
created: 2026-04-10
updated: 2026-04-10
status: current
valid_from: 2026-04-10
valid_until:
superseded_by:
horizon: present
version: v1
sources: [2026-04-10-success-blueprint, 2026-04-10-notion-roadmap-cvforge]
related: [[product/product-vision]], [[product/product-roadmap]], [[archive/entities/cv-forge]]
---

# AI Product Model — Modes, règles et qualité

Architecture IA complète pour CV Forge : 3 modes distincts, 5 règles d'interaction, cadre de qualité writing, et le pattern de suggestion idéal.

---

## 3 modes IA

### Mode 1 — Draft AI

**Usage** : Créer les blocks initiaux du document.

**Exigences** :
- Guardrails forts
- Job awareness (utiliser le Job Record pour contextualiser)
- Anti-generic writing
- Structure awareness (respecter les familles CV)
- Tone consistency

**Surface** : Génération initiale dans le funnel (Step 5 Quick-start path) + génération de cover letter/proposal.

---

### Mode 2 — Assist AI

**Usage** : Dans le workflow, sur du contenu existant.

**Actions** :
- rewrite
- shorten
- clarify
- fix grammar
- improve ATS alignment
- make more formal / warmer
- extract bullets
- convert paragraph → bullets
- convert bullets → paragraph

**Surface** : La **floating selection toolbar** est l'outil principal de ce mode. C'est un vrai asset UX identifié comme "excellent embedded writing assistant feel."

> Important : la toolbar actuelle est moins curé que l'IA de proposal — cette asymétrie est dangereuse car "users judge AI by the worst interaction, not the best one."

---

### Mode 3 — Suggestion AI

**Usage** : Quand le choix aide l'utilisateur.

**Pattern** :
- **Default** : 1 strong rewrite (pas de choix forcé)
- **Option** : "show alternatives" → max 2-3 variants
- Variants doivent être **ranked + visiblement distincts** (pas superficiels)

**Anti-pattern à éviter** :
- 10 options de mauvaise qualité
- 1 réécriture opaque sans contrôle
- Suggestions non différenciées

**Exemples de suggestion sets idéaux** :
- "Pick 1 of 3 stronger summaries"
- "Pick 1 of 2 opening lines"
- "Choose compact / persuasive / formal rewrite"
- "Choose better verb set"

> "If the AI can only produce one version and user must trust it blindly, that can feel efficient at first, but it creates hidden distrust."

---

## 5 règles d'interaction IA

**Règle 1** : Ne jamais demander de prompt quand un bouton peut faire le job.

**Règle 2** : Chaque action IA a un intent obvieux :
rewrite · shorten · strengthen · humanize · formalize · fix grammar · align to job · extract keywords

**Règle 3** : Chaque output IA est replaceable, pas destructif. Options : replace · insert below · keep both · compare versions

**Règle 4** : L'IA se souvient du contexte automatiquement : job · tone · user profile · target role · section type

**Règle 5** : L'IA est la plus forte sur : summary · experience bullets · cover letter opening · call to action · ATS keyword adaptation. Tout n'a pas besoin d'une égale intensité IA.

---

## Système de tones

### UI (visible utilisateur)
4 tones :
- **Auto** : l'IA analyse l'offre d'emploi (secteur, culture d'entreprise, formulation de l'annonce) et choisit le tone le plus adapté automatiquement. Mode recommandé par défaut.
- **Natural** : ton humain et authentique, conversationnel, accessible — sans être informel
- **Formal** : conservateur, structuré, traditionnel — adapté aux secteurs institutionnels, juridiques, corporate
- **Warm** : chaleureux, orienté relation, humain — adapté aux secteurs créatifs, startup, RH

**Logique du système** :
- **Auto** est la porte d'entrée — il réduit la charge de choix et personnalise selon l'offre
- Les 3 autres tones restent disponibles pour les utilisateurs qui veulent contrôler explicitement
- L'IA enrichit chaque tone avec des modifiers contextuels sous le capot (voir ci-dessous)
- Critère d'un bon système de tone : légible, distinct, stable, facile à choisir — pas de pseudo-tones vagues

### Modifiers cachés (sous le capot)
Ne pas exposer en premier niveau mais utiliser en interne ou en contrôles avancés :
- concise
- assertive
- plain language
- executive
- beginner-friendly
- achievement-heavy
- ATS-focused

---

## Cadre de qualité — Writing généré

**Chaque block généré doit être vérifié pour** :
- Role specificity (pas générique)
- Company specificity quand disponible
- Anti-fluff
- Concrete responsibilities
- Tone consistency
- Sentence simplicity
- Non-répétition
- No hallucinated claims
- No cringe phrases
- No "I am excited to apply…" cliché overload

**Le writing fort doit se sentir** : grounded · clear · confident · human · employable

**Éviter** : poetic · overenthusiastic · "AI polished" · generic HR spam

---

## AI Rulebook (P0 priorité)

Le **AI interaction rulebook** est une initiative P0 Phase 1 dans la roadmap. C'est un **product spec**, pas une feature.

Il doit définir :
- Quand l'IA retourne 1 résultat vs 2-3 options
- Quand elle ouvre une modale
- Comportement diff
- Contrôles replace/insert/keep
- Comportement par surface (toolbar vs proposal vs import)

Sans ce rulebook, le comportement IA reste incohérent entre surfaces — ce qui damage la confiance de l'utilisateur même si chaque surface prise seule est correcte.

---

## Zones IA prioritaires

En ordre d'importance pour l'impact utilisateur :
1. **Summary** — la section la plus lue, la plus influente
2. **Experience bullets** — volume le plus important, plus grand risque de généricité
3. **Cover letter opening** — premier impression critique
4. **Call to action** — clôture de la lettre
5. **ATS keyword adaptation** — valeur différenciatrice vs concurrents

---

## Voir aussi

- [[product/product-vision]] — architecture produit complète (5 objets, parcours utilisateur, éditeur)
- [[product/product-roadmap]] — AI interaction rulebook (P0) et advanced tone modifiers (P2)
- [[product/kpis]] — AI Accept Rate et AI Undo Rate comme métriques de succès
