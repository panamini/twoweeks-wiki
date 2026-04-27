---
title: "Brand Voice — twoweeks"
category: design
tags: [brand, voice, tone, copy, marketing, staccato, corporate-noir, twoweeks]
created: 2026-04-12
updated: 2026-04-27
status: current
valid_from: 2026-04-12
version: v1
sources: [2026-04-12-twoweeks-brand-bible, 2026-04-15-conversation-locale-typography-rules, 2026-04-27-twoweeks-brand-voice-card, 2026-04-27-brand-voice-review-twoweeks, 2026-04-27-brand-twoweeks-ai, 2026-04-27-voice-card-ui-copy-audits, 2026-04-27-twoweeks-brand-voice-copy-refactor-prompt]
related: [[entities/twoweeks]], [[product/ai-product-model]], [[design/locale-typography-rules]], [[design/logo-system]]
---

# Brand Voice — twoweeks

Guidelines de voix, tone et copie pour twoweeks.ai. À appliquer sur : copie UI, onboarding, marketing, microtextes, états vides, messages d'erreur.

La voix de marque ne remplace pas les règles de typographie locale. Le wording et la personnalité appartiennent à cette page; la ponctuation, les citations, les dates et les conventions FR/EN appartiennent à [[design/locale-typography-rules]].

---

## La personnalité de marque

> Imagine a creative director who is brilliant but ready to quit. They don't use buzzwords. They use results.

**Archétype** : "Le coolest person in the room" — brillant, efficace, prêt à partir. Pas de bullshit, juste des résultats.

---

## La voix

**Staccato** : phrases courtes. Impact fort. Pas de virgules en cascade.

**Corporate Noir** : humour sec, légèrement cynique sur le monde du travail, jamais amer.

**Anti-corporate productivity coach** : déclaratif, compressé, leisure-forward. La thèse est : le travail est fini; le temps vaut plus que l'ambition.

**Mots piliers** :
- "Finish. Faster."
- "Act your wage."
- "Go play outside."
- "The work is done. Just quit."

---

## Règles de copie

| Do ✅ | Don't ❌ |
|-------|---------|
| Phrases courtes (< 10 mots) | Phrases subordonnées longues |
| Verbes d'action directs | Substantifs abstraits ("optimisation", "synergie") |
| "Your Friday afternoon" | "Work-life balance" |
| Humour sec, corporate noir | Blagues forcées ou naïves |
| Laisser l'IA invisible | Préfixer avec "AI-powered", "AI-driven" |
| Parler des résultats | Parler du processus |

**Règle anti-AI** : en 2026, tout le monde sait que c'est de l'IA. Ne jamais l'annoncer comme un feature. L'IA est dans le produit, pas dans la copie.

---

## Application dans l'UI

- **Boutons** : 1-3 mots, verbe d'abord, pas de point. Exemples : `Save job`, `Attach resume`, `Draft cover letter`.
- **Section headers** : 1-2 mots, Title Case. Exemples : `Jobs`, `Brief`, `Match`, `Resumes`.
- **États vides** : 2 lignes max. Ligne 1 fait; ligne 2 action. Exemple : `No jobs. Import one.`
- **Tooltips** : 4 mots max, pas de point.
- **Placeholders** : miroir du champ, pas de hint ni `e.g.`. Exemple : `Paste job URL`.
- **Toasts** : succès = un mot avec point (`Saved.`); échec = 2-3 mots avec point (`Import failed.`).
- **Erreurs** : fait puis action, pas d'excuse. Exemple : `Something broke. Try again.`

## Noms user-facing

- `resume` est le nom visible canonique; `CV` reste acceptable dans les noms internes ou historiques.
- `cover letter` est le nom visible canonique pour le document mainstream; `proposal` peut survivre dans les identifiants internes ou surfaces stratégiques où la flexibilité est voulue.
- La marque visible est `Twoweeks`.

## Interdictions actives

- Hype : `seamlessly`, `effortlessly`, `powerful`, `leverage`, `unlock`, `elevate`, `empower`, `robust`, `comprehensive`, `intuitive`, `AI-powered`.
- Coach voice : `let's`, `hey`, `oops`, `you got this`, `we get you`.
- Corporate filler : `please`, `kindly`, `sorry` sauf vraie excuse pour vraie faute.
- Constructions : `not X, just Y`, `Zero fluff`, `Real impact`, `Powerful under the hood`.
- Questions sauf confirmations destructives (`Delete this job?`).

---

## Relation avec le système de tones IA

Le système de tones (Auto/Natural/Formal/Warm) dans le module CVForge s'applique au **contenu généré pour le CV** — pas à la voix de l'interface. La voix de l'interface reste toujours staccato/corporate-noir.

Voir [[product/ai-product-model]] pour le détail du système de tones IA.

---

## Voir aussi

- [[entities/twoweeks]] — entité principale et positionnement produit
- [[product/ai-product-model]] — système de tones pour la génération de contenu CV
- [[design/locale-typography-rules]] — conventions typographiques locales
- [[design/logo-system]] — wordmark, compact logo et période terracotta
