---
title: "Gestion temporelle du wiki"
category: concept
tags: [temporal, architecture, workflow, meta, versioning]
created: 2026-04-09
updated: 2026-04-09
status: current
valid_from: 2026-04-09
horizon: present
version: v0
sources: [commentaire-utilisateur, architecture-v2]
related: [[llm-wiki-pattern]], [[architecture-v2]]
---

# Gestion temporelle du wiki

La gestion temporelle est le mécanisme qui permet au wiki de distinguer les informations passées, présentes et planifiées. Sans elle, un LLM interrogeant un wiki long terme risque de mélanger des données de différentes époques dans une même réponse.

## Définition

Un wiki sans notion temporelle traite toutes ses pages comme également valides et actuelles. Sur un projet évolutif (plusieurs mois, plusieurs versions), c'est une faille sérieuse : les décisions changent, les specs sont révisées, les architectures pivotent. Le wiki accumule des informations dont certaines se contredisent, sans que le LLM puisse savoir laquelle est "la bonne réponse aujourd'hui."

## Le problème concret

Exemple sur un projet de 9 mois :
- Avril : décision d'utiliser une architecture monolithique
- Juillet : pivot vers microservices
- Octobre : spec préliminaire d'une migration serverless pour la v3

Sans gestion temporelle, si on demande "quelle est notre architecture ?", le LLM peut répondre n'importe laquelle des trois, ou les mélanger.

## La solution : frontmatter temporel

Chaque page wiki porte six champs temporels :

```yaml
status: current          # current | archived | planned | deprecated
valid_from: YYYY-MM-DD   # depuis quand cette info est valide
valid_until: YYYY-MM-DD  # vide si encore valide
superseded_by: [[page]]  # lien vers la version plus récente
horizon: present         # past | present | future
version: v2              # version projet concernée
```

### `status` — l'état de vie d'une page

| Valeur | Signification |
|--------|---------------|
| `current` | Information valide et active aujourd'hui |
| `archived` | Valide en son temps, plus applicable maintenant |
| `planned` | Décision ou spec pour une version/date future |
| `deprecated` | Abandonné (ni actif, ni archivé proprement) |

### `horizon` — la perspective temporelle

| Valeur | Usage |
|--------|-------|
| `past` | Concerne une période ou version révolue |
| `present` | Concerne l'état actuel du projet |
| `future` | Concerne ce qui est planifié |

## Architecture de l'archive

Les pages supersédées migrent dans `wiki/archive/[catégorie]/`. Elles conservent leur frontmatter complet avec `status: archived` et `superseded_by`. Le LLM les consulte uniquement pour des queries historiques explicites.

## Règle de priorité LLM

Par défaut, pour toute query :
1. Priorité 1 → `status: current` + `horizon: present`
2. Priorité 2 → `status: current` + `horizon: future`
3. Priorité 3 → `status: planned`
4. Ignoré par défaut → `status: archived` ou `deprecated`

## Workflow Supersede

Quand une nouvelle info contredit une ancienne :
1. Créer la nouvelle page : `status: current`, `valid_from: aujourd'hui`
2. Ancienne page : `status: archived`, `valid_until: aujourd'hui`, `superseded_by: [[nouvelle]]`
3. Déplacer l'ancienne dans `wiki/archive/[catégorie]/`
4. Ajouter un événement dans `wiki/timeline.md`

## Queries temporelles typiques

- **"Quel est l'état actuel ?"** → filtrer `status: current`
- **"Qu'avions-nous décidé avant juillet 2026 ?"** → consulter `timeline.md` + `archive/` + `valid_from` avant la date
- **"Qu'est-ce qui est planifié pour la v3 ?"** → `status: planned` + `horizon: future` + `version: v3`
- **"Montre l'évolution de [concept]"** → page actuelle + chaîne de `superseded_by` dans l'archive

## Application dans twoweeks

Ce mécanisme est fondamental pour un projet applicatif sur plusieurs versions. Il permet de répondre aux questions de conduite de projet long terme sans risque de confusion temporelle.

## Voir aussi

- [[llm-wiki-pattern]] — pattern général du wiki
- [[architecture-v2]] — document de référence sur la v2
- `wiki/archive/` — pages supersédées
- `wiki/timeline.md` — chronologie du projet
