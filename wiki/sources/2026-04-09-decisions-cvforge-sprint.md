---
title: "Décisions sprint CV Forge — parser, features, bugs"
category: source
tags: [cvforge, parser, sprint, decisions, bugs, architecture]
created: 2026-04-09
updated: 2026-04-09
status: current
valid_from: 2026-04-09
valid_until:
superseded_by:
horizon: present
version: v0
type: conversation
sources: []
related: [[cv-forge]], [[cv-parsing-pipeline]], [[cv-families]]
---

# Décisions sprint CV Forge — parser, features, bugs

**Type** : Note de décisions (conversation avec LLM)
**Date** : 2026-04-09

## Résumé

Note dense de décisions produit/tech pour CV Forge : stratégie d'évolution du parser CV (heuristiques vs JSON structuré), timing des CVs synthétiques pour les tests, features immédiates à ajouter, liste de bugs UI en cours, et features déféréées au sprint suivant.

## Points clés

1. **Ne pas pivoter tout de suite vers JSON structuré** — finir le sprint actuel en heuristiques, puis faire un POC schema-first sur une seule famille (identity/contact ou education) avant de décider
2. **CVs synthétiques** : utiles mais pas maintenant — attendre après le patch actuel et l'isolation de la prochaine contamination family
3. **Features à ajouter maintenant** : Download Raw OCR Markdown + Download Normalized JSON
4. **AI rewrite suggestions** (2–3 suggestions dans CV Forge) : future enhancement, pas ce sprint
5. **Destination Summary Pane** : potentiellement bon pour l'orientation utilisateur, mais après stabilisation du pipeline save

## Décision architecture parser (3 options)

| Option | Description |
|--------|-------------|
| 1. Continuer heuristiques | Rester sur le pipeline actuel, finir les bugs |
| 2. Hybride heuristiques + JSON structuré | POC sur une famille, comparer puis décider |
| 3. Pivot quasi complet vers JSON structuré | Réécriture plus profonde |

**Reco retenue : Option 2 — hybride** après un POC. Familles candidates pour le POC : IDENTITY/CONTACT, EDUCATION, ou LANGUAGES. Pas EXPERIENCE (trop instable).

Critères de comparaison du POC :
- Coût d'implémentation
- Stabilité
- Taux de duplication
- Facilité à supporter le multilingue

## CVs synthétiques — timing

À utiliser quand :
- Familles sous-représentées dans les fixtures réelles : hobbies, certifications, projects, affiliations, additional information
- Layouts de contamination spécifiques absents des fixtures existantes

**Ne pas lancer avant** : fin du patch actuel + isolation de la prochaine contamination family.

## Features décidées

- ✅ **Download Raw OCR Markdown** — à ajouter
- ✅ **Download Normalized JSON** — à ajouter
- ⏳ AI rewrite suggestions (2–3 par section dans CV Forge) — future enhancement
- ⏳ Destination Summary Pane (dans/adjacent au recovery drawer) — après stabilisation sprint

## Bugs UI listés

1. Card header line doit se superposer à l'output shell (pas à l'intérieur)
2. Mode edit de l'output shell mal aligné — 1-2px trop bas vs border de l'input shell
3. Character count à aligner avec les icônes du compose shell (marges égales haut/bas)
4. Toolbar from/to dans header line card peu claire — pas de feedback on click, manque un bouton delete/trash
5. Changer Biorhyme (police)
6. Virer Parisienne (police)
7. "Bricolage" — ne marche pas avec sa paire (police ?)
8. Enlever le X de suppression de photo quand il n'y a pas de photo
9. Styles définis dans Settings non activés dans la palette — pas d'indication claire du style actif, pas de "reset to default"

## Implications pour twoweeks

- Le parser est le cœur du produit — sa robustesse détermine la qualité de tout le reste
- La décision hybride (POC d'abord) est la bonne : elle préserve la vélocité à court terme tout en ouvrant la voie vers une architecture plus solide
- Les bugs listés sont tous des problèmes d'alignement/cohérence UI — aucun blocking, mais impactent la perception de qualité

## Pages wiki mises à jour

- [[cv-forge]] — entité créée
- [[cv-parsing-pipeline]] — concept créé
- [[cv-families]] — concept créé
- [[overview]] — projet décrit pour la première fois correctement
