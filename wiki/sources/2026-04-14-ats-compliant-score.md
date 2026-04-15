---
title: "ATS Compliant Score — Resume Audit Rubric"
category: source
tags: [ats, audit, score, parsing, resume, benchmark, typography, layout]
created: 2026-04-14
updated: 2026-04-14
status: current
valid_from: 2026-04-14
valid_until:
superseded_by:
horizon: present
version: v1
type: spec
sources: []
related: [[design/ats-safety]], [[strategy/benchmark-matrix]], [[entities/twoweeks]]
---

# ATS Compliant Score — Resume Audit Rubric
**Type** : Spec d'audit ATS  
**Date** : 2026-04-14  
**URL** : source locale `rawinput/ATS COMPLIANT SCORE.md`

## Résumé

Rubric détaillé pour auditer un CV au prisme ATS. Le document fixe des blockers absolus, une grille pondérée sur 100 points, et un format de verdict strict qui privilégie la sûreté de parsing avant l'optimisation copy.

## Points clés

1. **Blockers automatiques** : scan/image PDF, tables, text boxes, header/footer porteurs d'information, layout multi-colonnes, design graphique porteur de sens, headings non standard, fautes graves.
2. **Rubric pondéré** : 6 catégories couvrent parse integrity, layout safety, typography, section structure, keyword alignment et content quality.
3. **ATS-safe = simple, pas pauvre** : single-column, texte sélectionnable, hiérarchie visuelle simple, typographies standard, sections canoniques.
4. **Le score doit rester dur** : si un blocker est présent, le score total est capé à 69 tant que le défaut n'est pas corrigé.
5. **Le verdict final sépare 3 niveaux** : parser safety, keyword match, recruiter readability.

## Implications pour twoweeks

- Le produit doit traiter l'ATS-safety comme un axe qualité distinct du simple benchmark UX.
- Les templates, exports PDF/DOCX et sections custom ne doivent jamais casser les invariants ATS.
- Les audits automatiques futurs peuvent réutiliser cette grille comme scorecard produit et document health layer.
- Les modes IA orientés rewrite doivent préserver les headings standards et la structure machine-safe.

## Extraits notables

> "Prioritize parser safety first, then keyword match, then recruiter readability."

> "Single-column only. No sidebars."

## Pages wiki mises à jour

- [[design/ats-safety]] — nouvelle page design qualité produit
- [[overview]] — synthèse projet enrichie avec l'axe ATS
- [[index]] — source ajoutée
