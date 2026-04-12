---
title: "CV Parsing Pipeline"
category: concept
tags: [parser, architecture, ocr, heuristics, json, pipeline]
created: 2026-04-09
updated: 2026-04-09
status: current
valid_from: 2026-04-09
valid_until:
superseded_by:
horizon: present
version: v0
sources: [2026-04-09-decisions-cvforge-sprint]
related: [[cv-forge]], [[cv-families]]
---

# CV Parsing Pipeline

Le pipeline de parsing est le cœur technique de CV Forge. Il transforme du texte OCR brut en données structurées, organisées par [[cv-families|famille de section]].

## Approches en présence

### 1. Heuristiques (approche actuelle)

Règles explicites pour détecter et classer les sections d'un CV : patterns regex, détection de titres, alignement spatial, etc. Rapide à itérer, fragile sur les CVs atypiques.

### 2. Extraction JSON structurée (approche cible)

Schéma JSON défini par famille → LLM ou modèle structuré extrait directement les champs. Plus robuste sur les variantes, plus coûteux à implémenter, meilleure maintenabilité long terme.

### 3. Hybride (reco actuelle)

Garder les heuristiques pour les familles stables, introduire l'extraction structurée famille par famille via un POC. Permet de valider sans réécrire tout le pipeline.

## Décision en cours : POC hybride

**Reco** : ne pas pivoter tout de suite. Lancer un POC schema-first sur une seule famille, comparer avec le pipeline heuristique existant, puis décider.

**Familles candidates pour le POC :**
- IDENTITY / CONTACT — la plus simple, la plus stable
- EDUCATION — bonne structure prévisible
- LANGUAGES — courte, bien délimitée
- ❌ EXPERIENCE — trop instable pour commencer

**Critères de comparaison :**
- Coût d'implémentation
- Stabilité sur les fixtures réelles
- Taux de duplication
- Support multilingue

## Notion de contamination

Une **contamination** désigne une section mal parsée ou mal classée — par exemple, du contenu d'une famille qui se retrouve dans une autre, ou un bloc de texte non assigné. La gestion des contaminations est un travail continu par famille.

## CVs synthétiques

Des fixtures synthétiques (générées par LLM/Codex) complètent les fixtures réelles pour tester les familles sous-représentées : hobbies, certifications, projects, affiliations, additional information.

**Timing** : à utiliser après le patch actuel et l'isolation de la prochaine contamination family.

## Voir aussi

- [[cv-forge]] — l'application
- [[cv-families]] — les familles de sections
