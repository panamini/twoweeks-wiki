---
title: "Product Vision — TwoWeeks / CV Forge"
category: product
tags: [vision, positioning, architecture, funnel, éditeur, objets, ia, import, onboarding]
created: 2026-04-10
updated: 2026-04-10
status: current
valid_from: 2026-04-10
valid_until:
superseded_by:
horizon: present
version: v1
sources: [2026-04-10-success-blueprint]
related: [[archive/entities/cv-forge]], [[product/product-roadmap]], [[strategy/benchmark-matrix]], [[product/ai-product-model]]
---

# Product Vision — TwoWeeks / CV Forge

## Thesis produit

**TwoWeeks est un job application operating system** — pas seulement un resume builder.

Pour les utilisateurs qui veulent :
- un CV fort
- des cover letters / proposals forts
- du tailoring rapide sur un poste
- des données personnelles réutilisables
- une IA qui aide sans les faire babysitter

## Positionnement

> **"The fastest way to turn your experience into premium, job-ready applications."**

Pas : "AI resume builder", "beautiful templates", "editor for power users" — ce sont des features, pas une promesse marché.

La promesse combine : **speed + quality + confidence + repeat use**

---

## Modèle stratégique : Funnel + Éditeur (ne pas choisir)

### La peur initiale

Un éditeur pur convertit moins qu'un funnel guidé car : plus de choix, blank-state anxiety, moins de momentum, plus faible engagement psychologique.

Un funnel pur a ses limites : shallow long-term utility, weak retention, repetitive workflows.

### La réponse

**Ne pas choisir. Construire un système hybride.**

**Layer 1 — Guided activation funnel** : pour cold traffic, one-shot users, low-confidence users, mobile. Crée le commitment.

**Layer 2 — Structured editor workspace** : pour refinement, applications répétées, imports, deeper control, long-term users. Crée la rétention et la supériorité.

> "The funnel creates commitment. The editor creates retention and superiority."

Réponse directe à la peur : "Will the editor convert less than the funnel?" → Oui si l'éditeur est la première expérience dominante. Non si l'éditeur est la couche de valeur retenue derrière un guided activation path.

---

## Architecture produit — 5 objets

### A. Profile
Identité core de l'utilisateur : nom, contact, location, role targets, years experience, industries, education, skills, certifications, languages, tone defaults.

### B. Experience Library
Entrées de travail structurées et réutilisables :
- company, title, location, dates
- **bullet bank** (bullets spécifiques à un rôle)
- **achievement bank**
- role summary
- source/import origin
- état AI-cleaned / manually edited

### C. Job Record
Objet job normalisé :
- title, company, source URL
- raw description + **parsed responsibilities**
- **keywords + must-have requirements**
- industry, location type, seniority
- tone cues, hiring language style

### D. Resume Variant
Output spécifique : template + ordering + chosen sections + selected bullets + summary + styling + export settings + lien vers target jobs

### E. Cover Letter / Proposal Variant
Doc ciblé job : target job + tone + section blocks + AI history + version history + export state

Cette architecture fait évoluer TwoWeeks de "document builder" vers **application system**.

---

## 3 parcours utilisateur

### Path 1 — Quick conversion path (cold traffic)
Land → Choose goal → Import job → Import resume/start from profile → Quick guided setup → Generate first draft → Show premium preview + trust signals → 1-3 easy edits → Soft paywall/export gate → Upgrade

**Rôle** : conversion engine

### Path 2 — Workspace path (utilisateurs de retour)
Dashboard → See resumes/proposals/jobs/profile → Start from existing/target job/duplicate → Refine in structured editor + live preview → Export/save/duplicate

**Rôle** : retention engine

### Path 3 — Job-import path via extension
LinkedIn → Click extension → Job importé dans TwoWeeks → User choisit (tailor resume / cover letter / both) → Draft ouvert déjà contextualisé → Edit → Export/pay

**Rôle** : acquisition and habit engine ("extremely strong if polished" — potentiel moat)

---

## Architecture de l'éditeur

**Principe** : "Edit the structure, watch the final result."

Layout idéal :
- **Left rail** : documents, jobs, proposals, navigation rapide
- **Main editor pane** : sections structurées (profile, summary, experience, education, skills…)
- **Right preview pane** : live page preview toujours visible
- **Top bar** : template, tone, document type, export, import, AI actions, version/duplicate

**Interactions** :
- Click section dans l'éditeur → preview highlight de la section correspondante
- Click section dans preview → éditeur scroll vers le block
- Select text dans l'éditeur → floating AI bar
- Preview = mostly read/inspect mode (pas complex edit mode)
- Document-level blocks (header, recipient) → focused sheets/modals

---

## Architecture de la proposal

**Left side** : job offer card + source + keywords + tone cues + extracted priorities + company info + role expectations

**Right side** : generated proposal/letter + long/short slider + paragraph actions + template controls

Valeur UX : "The AI is writing from the job, not from nowhere." → trust signal fort.

Amélioration future : explicit job alignment widgets (key job needs / matched strengths / missing info / suggested emphasis).

---

## Template strategy

Pendant la création : 1 template recommandé + 2 alternates max. Pas de gallery au départ.

Après le premier draft : controlled template switcher (6-12 curated max, groupés par purpose).

Catégories recommandées : Classic/conservative · Modern professional · Compact ATS · Executive · Creative restrained · Academic/structured

> "Templates should be a finishing decision, not an opening burden."

---

## Information architecture cible

Top-level nav : Dashboard · Resumes · Cover Letters/Proposals · Jobs · Profile · Templates · Settings

Dashboard modules : Continue editing · Recent jobs · Recent documents · Suggested next action · Import resume · Import job · Create from scratch

Principe : "I know where my stuff is. I know what this job is. I know which document belongs to which opportunity."

---

## Onboarding 2026

**Pas** de tooltip tour géant comme système principal.

Stack recommandé :
1. **Progressive checklist** : import resume → add job → generate first draft → improve one section → export
2. **Contextual nudges** : helpers one-line au bon moment ("click any section to edit", "select text to rewrite")
3. **First-time spotlight** : uniquement pour les actions les plus importantes (generate, import, edit preview, AI toolbar)
4. **Embedded empty-state education** : enseigner la prochaine action là où il n'y a pas de contenu
5. **Dismissible coach panel** : optionnel, pas forcé

---

## Pipeline import idéal (6 étapes)

1. **Raw ingest** : PDF / DOCX / pasted content / LinkedIn import
2. **Structural normalization** : détecter profile lines, summary, roles, dates, bullet blocks, education, skills, certifications, languages
3. **Confidence scoring** : chaque block extrait reçoit un score de confiance
4. **Review queue** : si confiance basse → surfer les blocs incertains ("Review 3 imported blocks"), ne pas les placer silencieusement
5. **Cleanup AI** : normaliser glyphes bizarres, lignes merged, fragments dupliqués, mauvais bullet formatting, dates, capitalisation
6. **User confirmation** : review layer très rapide

> "Never dump uncertain parse results directly into final sections without review."

---

## Modèle de monétisation recommandé

**Option A (strongest commercial)** : free draft creation + limited exports/watermark/preview → paid unlock pour export + unlimited edits + advanced AI + multiple templates + multi-doc management

**Option B (hybrid)** : free first resume preview → pay to export/duplicate/tailor across jobs/advanced AI

**Vendre le levier, pas juste l'export** : unlimited tailoring, better AI rewriting, premium templates, saved jobs, duplicate and retarget, document library, cover letters/proposals, extension use, import cleanup assistance → "job search productivity layer"

---

## UI philosophy : premium mais accessible

Le risque : premium peut aliéner quand ça signale fashion over usefulness, elite taste, creative-industry bias, "designer toy".

**La bonne balance** : documents premium + product language human and practical.

Garder : strong grid, typography quality, restrained palette, sophisticated spacing, curated templates.

Ajouter : friendly helper text, explicit benefits, clearer action labels, more reassurance, "why this matters" copy, stronger empty-state coaching.

**premium aesthetic + mass-market clarity**

---

## Messaging marketing (futur)

Thèmes forts :
- Tailor every application faster
- Premium resumes without design skills
- Import from LinkedIn and generate in minutes
- Stronger cover letters without generic AI fluff
- One workspace for resumes, proposals, and jobs

Direction hero : **"Create job-ready resumes and cover letters in minutes — then tailor them for every opportunity."**

Submessage : **"Import your job, reuse your experience, and let AI help where it actually matters."**

---

## Différenciation vs ResumeLab

| ResumeLab | TwoWeeks |
|-----------|----------|
| Guided, beginner-friendly | Premium mais pratique |
| Conversion-focused | Job-aware + reusable |
| Template/funnel heavy | AI-native + structured |
| Reassuring, somewhat rigid | Better for repeated applications |
| | Better design system + workbench feel |
| | Still accessible for quick users |

> "Do not try to become ResumeLab with better colors. That is not the lane."

---

## Voir aussi

- [[strategy/benchmark-matrix]] — système de scoring pour évaluer le produit
- [[product/ai-product-model]] — architecture IA détaillée (3 modes, 5 règles)
- [[product/product-roadmap]] — initiatives priorisées pour atteindre cette vision
- [[cv-forge]] — entité produit
