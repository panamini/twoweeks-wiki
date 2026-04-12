---
title: "LLM Wiki Pattern"
category: concept
tags: [meta, workflow, knowledge-management, llm]
created: 2026-04-09
updated: 2026-04-09
sources: [tweet-andrej-karpathy, wiki-paste]
related: [[overview]], [[index]]
---

# LLM Wiki Pattern

Le pattern fondateur de ce vault. Un LLM construit et maintient une base de connaissance persistante et structurée — un wiki en markdown — au lieu de simplement répondre à des questions depuis des sources brutes à chaque fois.

## Définition

Au lieu de faire du RAG classique (récupérer des chunks de documents bruts à chaque requête), le LLM **compile incrémentalement un wiki** qui s'enrichit à chaque nouvelle source et chaque nouvelle question. La connaissance s'accumule au lieu d'être re-dérivée à chaque fois.

## Les trois couches

1. **Raw sources** (`raw/`) — documents bruts immuables. Articles, papers, images, données. Source de vérité.
2. **Wiki** (`wiki/`) — markdown généré et maintenu par le LLM. Résumés, pages entités, pages concepts, index, log. Le LLM en est l'unique auteur.
3. **Schema** (`CLAUDE.md`) — instructions pour le LLM : structure, conventions, workflows. Co-évolue avec l'utilisateur.

## Pourquoi ça marche

Le travail ingrat de maintenance d'une base de connaissance (mettre à jour les cross-références, noter les contradictions, maintenir la cohérence) est précisément ce que les humains abandonnent mais les LLMs font sans se lasser. Le coût de maintenance est quasi nul.

## Les trois opérations principales

| Opération | Déclencheur | Résultat |
|-----------|-------------|----------|
| **Ingest** | Nouvelle source dans `raw/` | Page source + mise à jour des pages existantes |
| **Query** | Question de l'utilisateur | Réponse synthétisée + option de filer dans `outputs/` |
| **Lint** | Health check demandé | Rapport de contradictions, orphelins, gaps |

## Application dans twoweeks

Ce vault utilise ce pattern pour accumuler toute la connaissance nécessaire à la création et l'entretien de l'app twoweeks : design decisions, recherche utilisateur, patterns techniques, compétiteurs, inspirations.

## Analogie

Proche du Memex de Vannevar Bush (1945) — une mémoire personnelle et curative avec des liens associatifs entre documents. La partie que Bush n'avait pas résolue : qui fait la maintenance ? Le LLM s'en charge.

## Voir aussi

- [[index]] — catalogue du wiki
- [[overview]] — synthèse du projet twoweeks
- Obsidian Web Clipper — pour alimenter `raw/` facilement
- Marp — pour générer des slides depuis le wiki
- Dataview — pour des vues dynamiques sur le frontmatter

## Sources

- Tweet d'Andrej Karpathy sur les LLM Knowledge Bases (2026)
- Wiki paste : document de référence sur le pattern
