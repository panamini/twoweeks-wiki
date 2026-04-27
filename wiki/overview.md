---
title: "Vue d'ensemble — twoweeks"
category: overview
tags: [project, overview, twoweeks, roadmap, parser, ats]
created: 2026-04-09
updated: 2026-04-27
status: current
valid_from: 2026-04-09
version: v1
sources: [2026-04-09-decisions-cvforge-sprint, 2026-04-10-notion-roadmap-cvforge, 2026-04-10-success-blueprint, 2026-04-10-benchmark-matrix, 2026-04-10-gap-analysis, 2026-04-14-structured-parsing-canonical-truth, 2026-04-14-ats-compliant-score, 2026-04-14-kanban-sprint-notes, 2026-04-14-run-sh-quick-note, 2026-04-14-export-pipeline-brief-ocr-to-ats-styled-output, 2026-04-15-mistral-resume-v3-section-recovery-scratchpad, 2026-04-15-run-sh-workspace-modes, 2026-04-18-quick-start-module-hierarchy, 2026-04-27-job-library-prd, 2026-04-27-job-match-validation-contract, 2026-04-27-twoweeks-motion-system, 2026-04-27-workshop-pagination]
related: [[entities/twoweeks]], [[product/product-roadmap]], [[concepts/cv-parsing-pipeline]], [[design/ats-safety]], [[howto/local-parser-operations]], [[product/job-library]], [[product/job-match-review]], [[design/motion-system]], [[tech/workshop-pagination]]
---

# twoweeks — Vue d'ensemble

## Ce qu'est twoweeks aujourd'hui

**twoweeks** est un job application operating system centré sur trois couches :
- ingestion/parsing de CV
- normalisation en données canoniques éditables
- génération de CV, cover letters et proposals contextualisés à un job

Le produit garde CVForge et ProposalForge comme modules internes, mais la vérité produit et marque est `twoweeks`.

---

## Architecture active

### Vérité produit

La vérité canonique visée pour le CV est :

`OCR -> extraction structurée par famille -> normalisation -> currentCv.sections[*].structuredContent -> vues dérivées`

Les top-level arrays legacy (`experience[]`, `education[]`, `skills[]`, etc.) ne doivent plus être traités comme la vérité produit quand les sections structurées sont disponibles.

La vérité d'export suit la même logique : fichiers PDF/DOCX finaux dérivés des données normalisées, pas du preview DOM.

### Environnements

- **Workflow local quotidien** : `./run.sh local-fast`
- **Alias legacy** : `./run.sh local-convex`
- **Usage local partiel** : `./run.sh local`
- **Usage cloud/tunnel** : `./run.sh tunnel`

`run.sh` est la source de vérité opératoire pour ces modes. `local-fast` est désormais la boucle locale complète recommandée pour le parser; `local` ne suffit pas à garantir le même call path que le structured upload backend. La préférence localhost doit rester strictement dev-only.

---

## État du projet

| Dimension | Statut |
|-----------|--------|
| Stade | Développement actif |
| Phase produit | P0-P1 : confiance import, vérité canonique, stabilité éditeur |
| Priorité parser | stabiliser `sections[*].structuredContent` comme source de vérité |
| Priorité qualité | fiabilité sur vrais CVs, observabilité, régression |
| Priorité UX | quick-start onboarding, extension save-to-twoweeks, sections custom alignées sur le block renderer |
| Dernière activité | 2026-04-18 |

---

## Décisions actives

- **Pipeline parsing** : architecture structurée par familles, pas de pivot heuristique-only ni full rewrite brutal.
- **Source de vérité** : quand elles sont valides, les sections structurées deviennent la vérité canonique produit.
- **ATS safety** : nouvel axe qualité explicite pour les templates, exports et headings.
- **Extension path** : le chemin browser -> save-to-twoweeks reste un moat UX fort à polir.
- **Quick Start shell** : l'activation vit dans l'app-shell via `App.tsx`; `/proposal` ne sert le cold start cover-letter que comme état d'entrée intentionnel, et la primitive de choix partagée reste commune.
- **Sections custom** : `add your own section` doit rejoindre le vrai block renderer et non un legacy nested model.
- **Jobs first-class** : Job Library devient la couche durable des offres sauvegardées, avec Job Brief editable et documents liés.
- **Match Review** : le match est un indicateur d'attention utilisateur, pas un ATS; structured read reste advisory/shadow tant que la dogfood review ne valide pas les seuils.
- **Motion** : la période terracotta est le seul loop ambient autorisé; l'IA doit prouver son travail par stages, diffs et settle.
- **Workshop pagination** : `committedPages` est la source de vérité pour preview, print et export sur `workshop_resume_onecol_ats`.

---

## Thèmes majeurs du wiki

- [[concepts/cv-parsing-pipeline]] — stratégie d'évolution du parser
- [[concepts/cv-families]] — familles first-class vs secondaires
- [[design/ats-safety]] — règles parser-safe pour les outputs
- [[product/product-roadmap]] — initiatives par phase
- [[product/product-vision]] — blueprint produit complet
- [[product/job-library]] — couche Jobs sauvegardés
- [[product/job-match-review]] — dogfood et validation du match
- [[strategy/benchmark-matrix]] — scorecard concurrentielle globale
- [[tech/import-ocr-pipeline]] — call path OCR/import actuel
- [[tech/export-pipeline]] — pipeline document final
- [[tech/workshop-pagination]] — committed pages pour preview/print/export workshop
- [[tech/local-vs-remote-parser-architecture]] — séparation local/cloud
- [[howto/local-parser-operations]] — modes run.sh et debug local
- [[design/motion-system]] — règles motion et IA visible
- [[tasks/kanban]] — backlog sprint actif

---

## Questions ouvertes

- Quelle part du JSON export/copié dérive encore de tableaux top-level au lieu des sections structurées ?
- Quels slices parser nécessitent encore des fixtures synthétiques après les durcissements live ?
- Quel score ATS interne voulons-nous exposer dans une future document health layer ?
- Quand l'extension Save to twoweeks devient-elle assez polie pour être un vrai moteur d'acquisition ?
- Quels seuils dogfood Match Review suffisent avant de promouvoir le structured read au-delà du shadow/advisory ?
- Quel premier slice motion doit être livré sans perturber les surfaces document existantes ?

---

*Mise à jour automatique par le LLM · 2026-04-27*
