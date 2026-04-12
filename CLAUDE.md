# CLAUDE.md — Schema LLM Wiki · twoweeks (v2)

> Ce fichier est la configuration principale du wiki. L'agent LLM le lit en premier à chaque session pour comprendre la structure, les conventions et les workflows à suivre. Ne pas modifier sans intention claire.

---

## Projet : twoweeks

**twoweeks** (twoweeks.ai) est un outil haute performance de gestion de candidatures. Tagline : "Finish. Faster." Positionnement : "Anti-Work tool for people who do great work." Modules internes : CVForge (génération CV) et ProposalForge (cover letters & proposals). Ce wiki sert à accumuler et organiser les connaissances nécessaires à sa création et son entretien : décisions de design, recherches utilisateurs, patterns techniques, sources d'inspiration, compétiteurs, et tout autre contexte pertinent.

---

## Structure du vault (v2)

```
twoweeks/
├── CLAUDE.md                  ← ce fichier (schema LLM v2)
├── PLUGINS.md                 ← guide d'installation des plugins Obsidian
│
├── rawinput/                  ← STAGING : nouvelles sources à ingérer
│   └── README.md
│
├── raw/                       ← BIBLIOTHÈQUE : sources ingérées, IMMUABLES
│   └── assets/                ← images téléchargées localement
│
└── wiki/                      ← wiki maintenu par le LLM
    ├── index.md               ← catalogue de toutes les pages actives
    ├── log.md                 ← journal chronologique des opérations wiki
    ├── timeline.md            ← chronologie des événements du PROJET
    ├── overview.md            ← synthèse générale
    │
    ├── entities/              ← personnes, organisations, produits, outils (actifs)
    ├── concepts/              ← idées, patterns, techniques, décisions (actifs)
    ├── sources/               ← résumés des sources ingérées
    ├── tech/                  ← référence technique : call paths, architecture code, infra
    ├── howto/                 ← runbooks opérationnels (procédures step-by-step)
    ├── to do list/            ← kanban de sprint et backlog de tâches
    ├── outputs/               ← analyses, Q&A, slides filés en retour
    │
    └── archive/               ← pages supersédées (historique)
        ├── entities/
        ├── concepts/
        └── sources/
```

---

## Conventions de pages wiki

### Frontmatter YAML (obligatoire sur chaque page wiki)

```yaml
---
title: "Titre de la page"
category: entity | concept | source | output | overview
tags: [tag1, tag2]
created: YYYY-MM-DD
updated: YYYY-MM-DD

# Champs temporels (v2 — obligatoires)
status: current           # current | archived | planned | deprecated
valid_from: YYYY-MM-DD    # date depuis laquelle cette info est valide
valid_until:              # vide si encore valide ; sinon YYYY-MM-DD
superseded_by:            # [[nom-nouvelle-page]] si remplacée
horizon: present          # past | present | future
version: v1               # version du projet concernée

sources: [nom-source-1]   # sources qui ont alimenté cette page
related: [[Page liée]]
---
```

### Valeurs de `status`
- `current` — information valide et active aujourd'hui → **priorité maximale pour les réponses**
- `archived` — valide en son temps, plus applicable → dans `wiki/archive/`
- `planned` — décision ou spec pour une version/date future
- `deprecated` — abandonné

### Règle de priorité LLM pour les réponses

Par défaut, lire en priorité :
1. Pages `status: current` + `horizon: present`
2. Pages `status: current` + `horizon: future`
3. Pages `status: planned`
4. **Ignorer** : pages `status: archived` ou `deprecated` — sauf query explicitement historique

### Règles de nommage des fichiers
- **Entités** : `wiki/entities/nom-entite.md` (kebab-case)
- **Concepts** : `wiki/concepts/nom-concept.md`
- **Sources** : `wiki/sources/YYYY-MM-DD-titre-source.md`
- **Outputs** : `wiki/outputs/YYYY-MM-DD-titre-output.md`
- **Archivés** : même nom, déplacé dans `wiki/archive/[catégorie]/`

---

## Workflows

### Workflow : Ingest v2

Quand l'utilisateur dit "ingère les nouvelles sources" ou "traite rawinput/" :

1. **Scanner `rawinput/`** (pas `raw/`) pour trouver les nouveaux fichiers
2. Pour chaque fichier trouvé :
   a. **Lire** le fichier
   b. **Discuter** brièvement des points clés avec l'utilisateur
   c. **Créer** une page résumé dans `wiki/sources/YYYY-MM-DD-titre.md`
   d. **Mettre à jour** les pages d'entités et concepts existantes affectées
   e. **Créer** de nouvelles pages entité/concept si nécessaire
   f. **Appliquer le workflow Supersede** si la source contredit des pages existantes
   g. **Déplacer** le fichier de `rawinput/` vers `raw/` (ou `raw/assets/` pour les images)
3. **Mettre à jour** `wiki/index.md`
4. **Ajouter** une entrée dans `wiki/log.md` : `## [YYYY-MM-DD] ingest | Titre`
5. **Signaler** à l'utilisateur quelles pages ont été touchées

### Workflow : Supersede

Quand une information contredit ou remplace une page existante :

1. **Identifier** la page à superseder dans `wiki/[catégorie]/`
2. **Créer** la nouvelle page : `status: current`, `valid_from: aujourd'hui`
3. **Mettre à jour** l'ancienne page :
   - `status: archived`
   - `valid_until: aujourd'hui`
   - `superseded_by: [[nom-nouvelle-page]]`
4. **Déplacer** l'ancienne page vers `wiki/archive/[catégorie]/`
5. **Ajouter** un événement dans `wiki/timeline.md`
6. **Mettre à jour** `wiki/index.md` et `wiki/log.md`

### Workflow : Query

Quand l'utilisateur pose une question sur le wiki :

1. **Lire** `wiki/index.md` pour identifier les pages pertinentes
2. **Appliquer la règle de priorité** (current > planned > archived)
3. **Lire** les pages pertinentes (actives en priorité)
4. **Synthétiser** une réponse avec citations vers les pages wiki
5. **Proposer** de filer la réponse dans `wiki/outputs/` si elle mérite d'être conservée
6. **Si oui** : créer `wiki/outputs/YYYY-MM-DD-titre.md`, mettre à jour index et log

**Queries temporelles** :
- "état actuel" → `status: current` uniquement
- "avant [date]" → consulter `timeline.md` + `archive/` + `valid_from`
- "planifié pour v3" → `status: planned` + `horizon: future` + `version: v3`
- "évolution de [concept]" → page actuelle + chaîne `superseded_by` dans archive

### Workflow : Lint v2

Quand l'utilisateur demande un health check :

1. **Lire** toutes les pages listées dans `wiki/index.md`
2. **Détecter** :
   - Contradictions entre pages `status: current`
   - Pages `status: current` qui mentionnent des données `archived`
   - Pages sans champ `status` (frontmatter incomplet)
   - Pages `planned` dont la `valid_from` est dépassée (à activer)
   - Pages orphelines (aucun lien entrant)
   - Concepts mentionnés mais sans leur propre page
   - Liens cassés ou manquants
   - Fichiers oubliés dans `rawinput/` (ingestion en attente)
3. **Produire** un rapport dans `wiki/outputs/YYYY-MM-DD-lint-report.md`
4. **Proposer** des questions à investiguer et des sources à chercher
5. **Mettre à jour** index et log

### Workflow : Nouvelle session

Au début de chaque session :
1. Lire ce fichier `CLAUDE.md`
2. Lire `wiki/index.md` (catalogue complet)
3. Lire les 10 dernières entrées de `wiki/log.md`
4. Lire `wiki/overview.md`
5. Vérifier si `rawinput/` contient des fichiers (ingestion en attente ?)
6. Annoncer à l'utilisateur : nb de pages, dernière activité, sources en attente

---

## Règles de maintenance

- **Le LLM est l'unique auteur du wiki.** L'utilisateur lit, dirige, questionne.
- **Jamais modifier les fichiers dans `raw/`.** Source de vérité immuable.
- **`rawinput/` doit être vide après chaque ingest.** Les fichiers migrent vers `raw/`.
- **Toujours mettre à jour `index.md` et `log.md`** après toute modification.
- **Maintenir la cohérence temporelle** : propager les supersessions dans `timeline.md`.
- **Liens Obsidian** : utiliser `[[Nom de la page]]` pour les liens internes.
- **Images** : référencer les images locales depuis `raw/assets/`.
- **Archive** : une page archivée n'est jamais supprimée, seulement déplacée.

---

## Formats de sortie disponibles

| Format | Usage | Stockage |
|--------|-------|----------|
| Page markdown | Réponses, analyses, synthèses | `wiki/outputs/` |
| Marp slide deck | Présentations | `wiki/outputs/` |
| Tableau comparatif | Comparaisons de features, compétiteurs | dans une page wiki |
| Image matplotlib | Visualisations de données | `wiki/outputs/` |

---

## Historique du schema

- `2026-04-09` : Création initiale du schema (v1)
- `2026-04-09` : **Migration vers v2** — ajout de `rawinput/` (staging), gestion temporelle (status/horizon/version/superseded_by), `wiki/archive/`, `wiki/timeline.md`. Voir `wiki/outputs/2026-04-09-architecture-v2.md` pour la documentation complète.
