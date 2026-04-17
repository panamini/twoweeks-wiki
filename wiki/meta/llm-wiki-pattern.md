---
title: "LLM Wiki Pattern"
category: meta
tags: [meta, workflow, knowledge-management, llm]
created: 2026-04-09
updated: 2026-04-17
sources: [tweet-andrej-karpathy, wiki-paste]
related: [[overview]], [[index]]
---

# LLM Wiki Pattern

Le pattern fondateur de ce vault. Un LLM construit et maintient une base de connaissance persistante et structurée — un wiki en markdown — au lieu de simplement répondre à des questions depuis des sources brutes à chaque fois.

## Définition

Au lieu de faire du RAG classique, le système compile incrémentalement un wiki qui s'enrichit à chaque nouvelle source et chaque nouvelle question. La connaissance s'accumule au lieu d'être re-dérivée à chaque fois.

## Les trois couches

1. **Raw sources** (`raw/`) — documents bruts immuables. Articles, papers, images, données. Source de vérité.
2. **Wiki** (`wiki/`) — markdown généré et maintenu comme surface de connaissance durable. Pages durables, index, log, outputs.
3. **Schema** (`WIKI_SCHEMA.md` + `CLAUDE.md`) — découverte neutre puis contrat opérationnel d'écriture.

## Pourquoi ça marche

Le travail ingrat de maintenance d'une base de connaissance — mettre à jour les cross-références, noter les contradictions, maintenir la cohérence — est précisément ce que les humains abandonnent mais que les LLMs exécutent bien quand la structure est simple et stable.

## Les opérations principales

| Opération | Déclencheur | Résultat |
|-----------|-------------|----------|
| **Ingest** | Nouvelle source dans `rawinput/` | Page source + mise à jour des pages existantes |
| **Direct update** | Demande explicite d'éditer le wiki | Correction, fusion, reclassification, ou nouvelle page durable |
| **Lint** | Health check demandé | Rapport de contradictions, orphelins, drift |
| **Save output** | Demande de préserver une analyse | Page dans `wiki/outputs/` |

## Application dans twoweeks

Ce vault utilise ce pattern pour accumuler toute la connaissance nécessaire à la création et l'entretien de twoweeks : décisions design, recherche utilisateur, patterns techniques, compétiteurs, inspirations, et règles opératoires du wiki lui-même.

## Voir aussi

- [[index]] — catalogue du wiki
- [[overview]] — synthèse du projet twoweeks
- `WIKI_SCHEMA.md` — contrat neutre de découverte
- `CLAUDE.md` — contrat opérationnel d'écriture
