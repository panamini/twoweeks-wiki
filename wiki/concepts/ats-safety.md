---
title: "ATS Safety — Parser-safe output rules"
category: concept
tags: [ats, parsing, quality, templates, typography, layout, audit]
created: 2026-04-14
updated: 2026-04-14
status: current
valid_from: 2026-04-14
valid_until:
superseded_by:
horizon: present
version: v1
sources: [2026-04-14-ats-compliant-score, 2026-04-14-export-pipeline-brief-ocr-to-ats-styled-output]
related: [[concepts/benchmark-matrix]], [[concepts/ai-product-model]], [[entities/twoweeks]], [[tech/export-pipeline]]
---

# ATS Safety — Parser-safe output rules

Axe qualité produit dédié à la sûreté ATS. L'objectif n'est pas seulement de générer un beau CV, mais un document qui reste lisible par les parsers, aligné sur le poste, et rapide à scanner par un recruteur.

---

## Blockers absolus

Si l'un de ces défauts est présent, le document ne doit pas être considéré comme ATS-safe :

- scan ou image PDF non textuelle
- tables, text boxes, sidebars, multi-colonnes
- headers/footers contenant des informations importantes
- icônes, photos, charts, progress bars, logos porteurs de sens
- headings créatifs ou non standards
- fautes graves sur noms, titres, skills, certifications ou dates

---

## Rubrique de référence

| Catégorie                                | Poids | Ce qui compte                                                  |
| ---------------------------------------- | ----- | -------------------------------------------------------------- |
| File format and parse integrity          | 20    | format accepté, texte sélectionnable, ordre de lecture correct |
| Layout and graphic design safety         | 20    | single-column, pas de blocs graphiques, hiérarchie simple      |
| Typography and readability               | 15    | polices standard, tailles stables, pas de style décoratif      |
| Section structure and extraction clarity | 20    | headings standards, dates/titres/écoles clairs                 |
| Keyword alignment                        | 15    | skills/titres/certifications exacts et naturels                |
| Content quality                          | 10    | bullets concis, résultats mesurables, langue propre            |

---

## Règles produit pour twoweeks

1. Les templates premium ne doivent jamais compromettre la lecture machine.
2. Les sections custom doivent rester mappables vers des headings standards.
3. Les exports doivent privilégier DOCX ou PDF text-based et éviter toute mise en page ambigüe.
4. Les réécritures IA ne doivent pas sacrifier la structure pour "faire plus design".
5. Une future document health layer peut exposer ce rubric comme score ATS interne.
6. Le pipeline final doit produire un téléchargement direct depuis des payloads normalisés, pas une capture du preview DOM.

---

## Ce que cela change dans le benchmark

Le benchmark produit mesure déjà la confiance et la sécurité professionnelle. ATS Safety précise ce sous-ensemble avec des règles actionnables pour :

- layout/template
- export
- nettoyage typographique
- headings de sections
- audits automatiques

---

## Voir aussi

- [[concepts/benchmark-matrix]] — scorecard produit globale
- [[concepts/ai-product-model]] — réécritures IA et alignement ATS
- [[entities/twoweeks]] — produit principal
