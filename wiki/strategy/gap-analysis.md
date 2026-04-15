---
title: "Gap Analysis — TwoWeeks vs ResumeLab"
category: strategy
tags: [gap, compétiteurs, resumelab, diagnostic, priorités, forces, faiblesses]
created: 2026-04-10
updated: 2026-04-10
status: current
valid_from: 2026-04-10
valid_until:
superseded_by:
horizon: present
version: v1
sources: [2026-04-10-gap-analysis]
related: [[strategy/benchmark-matrix]], [[product/product-vision]], [[product/product-roadmap]], [[product/ai-product-model]]
---

# Gap Analysis — TwoWeeks vs ResumeLab

## Diagnostic en une phrase

> **"TwoWeeks is currently closer to the better product, but it is still missing the conversion scaffolding and import trust layer needed to beat a simpler commercial funnel like ResumeLab."**

---

## Ce que TwoWeeks fait déjà mieux

| Avantage | Détail |
|----------|--------|
| Core architecture | Workspace persistant : documents, resumes + proposals, recents, editing as a system, live preview, reusable structure |
| Long-term editing model | Skeleton + live preview scale mieux que le modèle popup de ResumeLab (plus de templates, plus de doc types, repeat users, AI avancé) |
| Proposal / cover letter | Job-aware proposal flow > questionnaire-heavy cover letter de ResumeLab — potentiel de moat |
| Visual taste | Design premium → impact sur trust, perceived employability, willingness to pay, emotional pride |
| AI embedding potential | Floating toolbar + AI contextuel = direction plus moderne que wizard-only AI |
| Retention potential | "Job search companion" possible — ResumeLab est plus transactionnel |

> "You are starting from a better product foundation."

---

## Ce qui nuit activement (blockers)

### A. Weak first-run activation (risque marché principal)

Le produit a plus de sens après compréhension. ResumeLab a plus de sens immédiatement. Cette différence détruit la conversion.

Un nouvel utilisateur peut ne pas savoir :
- quoi faire en premier
- si créer un resume ou une proposal en premier
- à quel point le système l'aidera automatiquement
- quel est le payoff après l'import
- pourquoi c'est mieux qu'un autre outil AI

> "A better system that is slower to understand often loses to a worse system that is immediately legible."

### B. Import / parser trust gap (sérieux)

Si l'import est désordonné (mauvaises sections, mauvais splits de paragraphes, glyphes bizarres) :

> "If it can't understand my resume, I can't trust its AI."

C'est dévastateur car l'import est le **premier moment où l'app prouve son intelligence**. ResumeLab ne parse peut-être pas mieux mais paraît plus fiable car la charge de correction est plus faible ou mieux cachée.

### C. AI consistency gap (dangereux)

Proposal AI avec guardrails vs floating-toolbar AI moins curé = problème de confiance produit.

> "Users score AI by the worst visible output, not the average."

### D. Lack of beginner path

Le produit est "good tool" mais pas "good entry experience." ResumeLab ne gagne pas parce qu'il est plus intelligent — il gagne parce qu'il réduit la peur du débutant : obvious next steps, progress feeling, low-cognitive entry, fast completion.

### E. Value communication underdeveloped

L'utilisateur doit comprendre rapidement pourquoi c'est vaut le coup d'essayer, de payer, et ce qui le différencie de ChatGPT + Canva + Docs.

### F. "Beauty without reassurance"

Le risque n'est pas que le design soit trop bon. C'est que le design signale sophistication sans signaler également simplicity + friendliness + approachability + guidance.

---

## Gaps manquants (pour battre ResumeLab)

**1. Quick-start funnel** — Le plus urgent. Pas un wizard géant. Un short, smart activation funnel : what to create → import resume/job → calibrate → generate → editor avec quelque chose de réel.

**2. Import recovery layer** — Pas juste un meilleur parser, une meilleure **parser UX** : confidence scoring, review queue, "3 uncertain blocks found", fix-this-first interface, encoding cleanup. "The product must never pretend messy imports are fine."

**3. AI interaction rulebook** — Règles explicites pour : quand 1 réponse vs variants, quand rewrite inline vs modal, quand silencieux vs proactif, quand preserve job tone, quand deterministic. "This is not polish. This is product coherence."

**4. Better editor-preview linking** — Click preview → jump to structured section. Hover section → highlight preview block. Stronger live status. "Better you-are-editing-this feeling."

**5. Focused template switching** — Small curated set + purpose labels + quick compare + easy swap. Pas une gallery géante, pas invisible non plus.

**6. Document health / quality layer** — Missing info, weak summary, unverified import blocks, low keyword alignment, export readiness. "Not just AI wrote it, but the system helps me know if it's ready." Opportunité de battre ResumeLab clairement.

**7. Better commercial packaging** — Clarifier free vs premium + pourquoi vs ChatGPT + Canva + Docs. Messaging : faster tailoring, premium layouts sans design skills, better letters from real job context, reusable workspace.

**8. Empty states + first-use education** — Pas un tour. Un guided first-use environment : smart empty states, suggested first action, progressive checklist, just-in-time coaching.

**9. Stronger Job entity** — Pas juste du texte importé. Un objet Job réel : title + company + URL + extracted requirements + keywords + location + tone + linked proposal + linked resume variant.

**10. Clearer "proposal" naming** — "Cover Letter / Proposal" ou "Application Letter" + copy qui explique. Sans framing clair, les utilisateurs grand public peuvent penser : freelance proposal, sales proposal, consulting proposal.

---

## Priority order

| Priorité | Workstream |
|----------|-----------|
| 1 — Import trust | Parser cleanup, glyph normalization, confidence scoring, uncertain-block review UI, section placement review |
| 2 — Quick-start path | "Create quickly" path, one-shot onboarding, import job+resume, fast first draft, guided refinement, export/pay point |
| 3 — AI quality unification | AI action taxonomy, standardize rewrite behaviors, improve toolbar outputs, undo/diff/replace patterns consistent |
| 4 — Editor-preview linking | Click preview → focus section, hover link states, section highlighting, active edit mapping |
| 5 — First-use coaching | Progressive checklist, contextual nudges, empty-state guidance, first-run spotlight |
| 6 — Document health/readiness | Quality checklist, missing info warnings, keyword alignment, proposal completeness, ready-to-export status |
| 7 — Premium value/offer | Only after trust issues above are improved — pricing logic, free vs premium boundary, why upgrade |

---

## Plan d'exécution — 3 cycles

### Cycle 1 (priorité absolue)
- Parser cleanup + import review layer
- Quick-start guided path
- First-run checklist
- Stronger preview/editor linking

### Cycle 2
- AI rulebook implementation
- Improved toolbar rewrite quality
- Template switcher
- Document health system

### Cycle 3
- Stronger jobs object
- Better premium packaging
- Landing / value communication
- Clearer "proposal" framing

---

## Keep / Change / Avoid / Defer

**Garder** : skeleton editor · live preview · tone system (4 tones : Auto/Natural/Formal/Warm) · forte direction graphique · extension job import · proposition/job-context direction · AI embedded dans le writing flow

**Changer** : entrée produit (pas workspace first) · AI rewrite UX (1 recommended + opt. 2-3 alternatives) · template access (focused browser) · onboarding (contextual guidance, pas tour) · import recovery (transparency + correction flow)

**Éviter** : copier le modèle popup de ResumeLab · expand les tone labels · giant template gallery · hidden AI magic sans contrôle · over-designed ambiguity · long generic product tour

**Déférer** : huge template catalog · collaboration features · heavy social proof · analytics dashboards · trop de niche tones · complex account areas · brand storytelling flourishes

---

## L'équation pour battre ResumeLab

```
ResumeLab's activation discipline
+ TwoWeeks' superior workspace architecture
+ TwoWeeks' superior design system
+ TwoWeeks' job-aware proposal engine
+ Reliable import
+ Coherent AI
= Category leader
```

---

## Voir aussi

- [[strategy/benchmark-matrix]] — scoring et seuils non-négociables
- [[product/product-vision]] — blueprint complet du produit idéal
- [[product/product-roadmap]] — roadmap priorisée (P0→P3)
- [[product/ai-product-model]] — 3 modes IA et rulebook
