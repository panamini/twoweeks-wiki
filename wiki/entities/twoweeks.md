---
title: "twoweeks"
category: entity
tags: [twoweeks, app, product, parser, cv, roadmap, vision, brand, cvforge, proposalforge]
created: 2026-04-12
updated: 2026-04-12
status: current
valid_from: 2026-04-12
valid_until:
superseded_by:
horizon: present
version: v2
sources: [2026-04-09-decisions-cvforge-sprint, 2026-04-10-notion-roadmap-cvforge, 2026-04-10-success-blueprint, 2026-04-10-benchmark-matrix, 2026-04-12-twoweeks-brand-bible]
related: [[cv-parsing-pipeline]], [[cv-families]], [[overview]], [[product-roadmap]], [[kpis]], [[product-vision]], [[benchmark-matrix]], [[ai-product-model]], [[concepts/brand-voice]]
---

# twoweeks

**twoweeks** (twoweeks.ai) est un outil haute performance de gestion de candidatures — parsing, normalisation et édition de CVs, cover letters et proposals. Le nom vient du préavis de deux semaines que l'on donne quand on quitte un poste.

---

## Brand

**Tagline** : Finish. Faster.

**Positionnement** : The "Anti-Work" tool for people who do great work. Le pont entre "The Grind" et "The Exit." En 2026, l'efficacité est une commodité ; le time-freedom est le luxe.

**Core values** :
- **Unrivaled Velocity** — la vitesse est la seule métrique qui compte
- **Invisible Tech** — l'IA est puissante, mais elle reste en retrait
- **Elite Indifference** — on s'en fiche de la "synergie corporate", on pense à ton vendredi après-midi

**Voix** : Staccato — phrases courtes, impact fort. Humor "Corporate Noir". Phrases piliers : "Act your wage." "Go play outside." "The work is done. Just quit."

Voir [[concepts/brand-voice]] pour les guidelines complètes de voix et de copie.

---

## Modules internes

| Module | Rôle |
|--------|------|
| **CVForge** | Génération et édition de CVs |
| **ProposalForge** | Génération de cover letters et proposals |

Ces noms sont des noms techniques internes — le produit s'appelle **twoweeks**.

---

## Position sur le marché

**twoweeks est un job application operating system**, pas seulement un resume builder. Sa différenciation vs ResumeLab : meilleure architecture long terme, editing ergonomics supérieures, AI embeddée dans le workflow, direction multi-document/companion.

**Modèle hybride** : Guided activation funnel (convertir) + Structured editor workspace (retenir).

Voir [[benchmark-matrix]] pour l'évaluation comparative et [[product-vision]] pour le blueprint complet.

---

## Architecture actuelle (v0)

- **Pipeline** : OCR → heuristiques de parsing → sections normalisées → UI d'édition
- **Export** : Download Raw OCR Markdown + Download Normalized JSON (prévu)
- **Editing** : Output shell + compose shell + card header line

## Architecture de stockage Convex

| Champ Convex | Rôle | Note |
|--------------|------|------|
| `userProfiles.cvDocument` | **Source de vérité** — CV parsé complet | À utiliser pour lire/écrire les CVs |
| `cvDocument.sections` | Sections actuelles du CV | État courant de l'édition |
| `cvDocument.metadata.importRecoverySession.baseSectionsSnapshot` | Snapshot au moment de l'import | Base pour le recovery UI |
| `userProfiles.experience[]` | Champ legacy — **vide** | Ne pas utiliser |
| `userProfiles.education[]` | Champ legacy — **vide** | Ne pas utiliser |
| `userProfiles.skills[]` | Champ legacy — **vide** | Ne pas utiliser |

## Composants UI principaux

| Composant | Rôle |
|-----------|------|
| Output shell | Affichage du CV parsé, mode preview et edit |
| Compose shell | Zone de saisie/édition de sections |
| Card header line | Toolbar de navigation/action sur les sections |
| Recovery drawer | Gestion des sections non parsées / fallback |
| StructuredUploadButton | Bouton import Mistral OCR (déclenche le pipeline de parsing) |

---

## État du sprint actuel

**Bugs ouverts** :
- Scroll/zoom bloqué dans la preview CV (pan impossible à 100% fit)

**En cours** :
- IDENTITY/CONTACT POC hybride (schema-first)

**Backlog** :
- Paddle cleanup (supprimer références runtime/build/test — ne pas toucher au workflow actif)
- Warning UX navigation pendant import
- AI rewrite suggestions (2–3 par section)

Voir [[to do list/kanban]] pour le kanban complet.

---

## Roadmap produit

Voir [[product-roadmap]] pour le détail. Résumé des phases :

- **Phase 1 (P0)** : Import recovery layer, Quick-start guided path, AI interaction rulebook, Editor↔preview linking
- **Phase 2 (P1)** : Onboarding progressif, Document health/readiness, Template switcher, Premium packaging, Proposal framing
- **Phase 3 (P2)** : Jobs as first-class object, Duplicate/retarget, Versioning, Advanced tone modifiers
- **Phase 4 (P3)** : Landing page + market story, Template expansion

## Décisions produit figées

| Décision | Statut |
|----------|--------|
| Structured skeleton editor = source de vérité | Approuvé |
| 4 tones : Auto / Natural / Formal / Warm | Approuvé |
| Pas de gallery de templates | Approuvé |
| Quick-start path | Approuvé |
| Import trust = UX problem (pas seulement parser) | Approuvé |
| AI standardisation via rulebook | Approuvé |
| Hybrid parser POC famille par famille | Approuvé |

## Architecture cible — 5 objets produit

- **Profile** — identité core réutilisable
- **Experience Library** — bullet bank + achievement bank par rôle
- **Job Record** — objet normalisé avec keywords + tone cues
- **Resume Variant** — output spécifique lié à un ou plusieurs jobs
- **Cover Letter / Proposal Variant** — doc ciblé avec version history

---

## KPIs principaux

Voir [[kpis]]. KPIs critiques : Visitor→First Draft Rate, Import Completion Rate, AI Accept Rate, Paywall Conversion, D7/D30 Retention.

## Voir aussi

- [[cv-parsing-pipeline]] — stratégie d'évolution du parser
- [[concepts/parsing-poc-progress]] — état POC par famille
- [[cv-families]] — familles de sections CV
- [[product-roadmap]] — roadmap complète
- [[product-vision]] — blueprint complet
- [[benchmark-matrix]] — scoring et positionnement vs ResumeLab
- [[ai-product-model]] — 3 modes IA, tones, cadre qualité writing
- [[concepts/brand-voice]] — voice & tone guidelines
- [[tech/import-ocr-pipeline]] — chemin de code import OCR
