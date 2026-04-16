---
title: "Product Roadmap — CV Forge"
category: product
tags: [roadmap, product, initiatives, phases, stratégie]
created: 2026-04-10
updated: 2026-04-16
status: current
valid_from: 2026-04-10
valid_until:
superseded_by:
horizon: present
version: v1
sources: [2026-04-10-notion-roadmap-cvforge, 2026-04-10-gap-analysis, 2026-04-16-plan-onboarding-activation-interactive-preview]
related: [[archive/entities/cv-forge]], [[product/kpis]], [[strategy/gap-analysis]], [[product/product-vision]], [[design/brand-voice]]
---

# Product Roadmap — CV Forge

## Stratégie générale

Quatre axes séquencés :

1. **Win first-run trust** — import recovery, quick-start flow, AI cohérent
2. **Win editing superiority** — structured editor, preview linking, typographie premium, AI contextuel
3. **Win repeat usage** — jobs as first-class objects, duplicate/retarget, workspace, versioning
4. **Win commercially** — premium value clair, packaging honnête, market story

---

## Phase 1 — P0 : Confiance et fondations (priorité maximale)

### Import recovery layer
**Problème** : Les utilisateurs perdent confiance quand l'import PDF place du contenu au mauvais endroit ou affiche des glyphes incorrects.
**Solution** : UX de recovery autour du parsing — confidence scoring, interface de review des blocs incertains, nettoyage des glyphes, normalisation des bullets, flow de réassignation de sections.
**KPIs** : Import Completion Rate ↑, drop-off après import ↓, parse errors non résolus ↓

### Quick-start guided path
**Problème** : L'entrée directe dans l'éditeur peut sous-convertir les nouveaux utilisateurs froids.
**Solution** : Flow guidé court avant l'éditeur — "que veux-tu créer ?", import CV/job, choix de tone, génération du premier draft, puis ouverture de l'éditeur.
**KPIs** : Time to First Draft ↓, Paywall Conversion ↑

### AI interaction rulebook
**Problème** : Le comportement de l'IA semble incohérent selon les surfaces (génération de proposition, modales, toolbar, import).
**Solution** : Standardisation des comportements IA sur toutes les surfaces — spec définissant quand l'IA retourne 1 vs 2-3 options, quand elle ouvre une modale, comportement diff, contrôles replace/insert/keep.
**KPIs** : AI Accept Rate ↑, Undo Rate ↓

### Editor ↔ Preview linking
**Problème** : L'édition en skeleton peut sembler abstraite sans mapping fort vers l'output final.
**Solution** : Cliquer dans le preview → focus section dans l'éditeur. Hover section → highlight preview. Sync active section. Pas de pivot vers preview-first — renforcement du lien émotionnel.
**KPIs** : Edit Completion ↑, Session Depth ↑

**Priorité d'exécution actuelle** : à faire avant le quick-start et avant la couche d'onboarding, car c'est le signal premium le plus fort à l'intérieur de l'éditeur et le meilleur payoff perceptible du produit.

---

## Phase 2 — P1 : Confiance + Conversion

### First-run onboarding system
Remplacer les longs tutoriaux par un onboarding progressif : checklist première session, nudges contextuels, empty-state helpers, 1-2 spotlight moments. Pas de tooltip tour géant.
**Dépendance** : Quick-start path

**Clarification actuelle** : cette couche vient après `Editor ↔ Preview linking` puis `Quick-start guided path`. La brand voice est jugée suffisamment mature pour être appliquée directement aux microcopies, sans chantier préalable.

### Document health / readiness layer
Système de readiness pour CV + proposition : checklist avec infos manquantes, sections faibles, blocs d'import non résolus, placeholders, alignement keywords, export readiness.
**Dépendances** : Import recovery, AI rulebook

### Focused template switcher
Template courant toujours visible, drawer/modal "Changer de template", 6-12 templates curés avec labels par usage. Pas de gallery Canva-style.
**Dépendance** : Preview system stable

### Extension-to-app handoff polish
Actions Save Job, Tailor Resume, Generate Proposal + landing state propre en app avec next action claire. Potentiel de moat si bien poli.
**Dépendance** : Extension disponible

### Premium value packaging
Clarifier la valeur free vs premium autour du tailoring, AI avancé, templates premium, workspace, proposals, réutilisation, export leverage. Vendre le levier, pas juste l'export.

### Proposal framing clarity
Utiliser "Cover letter / Proposal" ou "Application letter" dans les points d'entrée et l'onboarding pour réduire la confusion mainstream. Conserver la flexibilité stratégique du terme "Proposal".

---

## Phase 3 — P2 : Rétention et profondeur

### Jobs as first-class object
Construire une couche Jobs liée aux CVs/propositions : record avec titre, entreprise, URL source, responsabilités parsées, keywords, docs liés. **Moat builder** selon la stratégie.
**KPIs** : Documents/User ↑, Jobs/User ↑

### Duplicate / retarget workflow
Duplication et retargeting de CV/proposition pour un nouveau rôle — préserver la structure en mettant à jour le contexte. Fort levier de rétention.

### Versioning / compare states
Historique de versions léger avec comparaison, restauration, labels optionnels par date/job. Réduit la peur des modifications et de l'IA.

### Advanced tone modifiers under the hood
4 tones en UI : **Auto** (analyse l'offre + choisit automatiquement), **Natural**, **Formal**, **Warm**. Modifiers internes (concise, assertive, executive, ATS-focused, plain-language) injectés sous le capot. Ne pas exposer en premier niveau.
**Dépendance** : AI rulebook

---

## Phase 4 — P3 : Croissance

### Landing page + market story
Hero, positioning, story extension, message job-tailoring, design premium, proof. **Ne pas marketer avant que le produit soit honnête.**

### Template expansion
Catalogue étendu et curé, groupé par usage. Après résolution des problèmes core. Éviter le "Canva-izing" du produit.
**Dépendance** : Focused template switcher d'abord

---

## Décisions stratégiques figées

| Décision | Statut |
|----------|--------|
| Structured skeleton editor = source de vérité (pas preview-first) | Approuvé |
| 4 tones en UI : Auto / Natural / Formal / Warm | Approuvé |
| Pas de gallery de templates géante | Approuvé |
| Quick-start path avant entrée directe dans l'éditeur | Approuvé |
| Onboarding progressif (pas de tooltip tour) | Approuvé |
| Import trust = problème UX, pas seulement parser | Approuvé |
| AI standardisation via rulebook | Approuvé |
| "Cover letter / Proposal" framing (en discussion) | Proposé |

---

## Plan d'exécution en 3 cycles (gap analysis)

Croisement entre les phases P0→P3 et les priorités de la gap analysis. Voir [[strategy/gap-analysis]] pour le détail complet.

**Cycle 1** : parser cleanup + import review layer · quick-start guided path · first-run checklist · stronger preview/editor linking
→ *Mappe directement sur les 4 initiatives P0*

**Ordre d'exécution actuellement recommandé** :
1. interactive preview ↔ editor linking
2. quick-start guided path
3. first-run onboarding layer

**Cycle 2** : AI rulebook implementation · improved toolbar rewrite quality · template switcher · document health system
→ *Mappe sur les initiatives P1 prioritaires*

**Cycle 3** : stronger jobs object · better premium packaging · landing/value communication · clearer "proposal" framing
→ *Mappe sur P1 (packaging, proposal framing) + P2 (jobs object)*

## Voir aussi

- [[product/kpis]] — métriques associées à chaque phase
- [[cv-forge]] — entité produit
- [[cv-parsing-pipeline]] — architecture technique du parsing
- [[strategy/gap-analysis]] — diagnostic complet et priority order vs ResumeLab
- [[product/product-vision]] — blueprint du produit idéal
- [[design/brand-voice]] — microcopy à appliquer directement pendant l'implémentation
