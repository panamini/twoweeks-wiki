# Plan détaillé de migration vers un schéma wiki agnostique à l'agent (non destructif) — Étape 4 — Transformer `CLAUDE.md` en shim de compatibilité (contenu exact en français + emplacement)


### 4.1 Où modifier

- Fichier à modifier: `CLAUDE.md` à la racine du vault.
- Action: remplacer tout le contenu actuel par un shim court.

### 4.2 Contenu exact à mettre dans `CLAUDE.md`

```md
# CLAUDE.md — Shim de compatibilité

Ce fichier est conservé temporairement pour compatibilité.

Source canonique:
- `WIKI_SCHEMA.md`

Adaptation Claude:
- `adapters/claude.md`

Procédure:
1. Lire `WIKI_SCHEMA.md`.
2. Appliquer `adapters/claude.md`.
3. Exécuter les workflows selon `WIKI_SCHEMA.md`.

Notes:
- Ne plus maintenir de règles métier dans ce fichier.
- Toutes les évolutions de règles doivent être faites dans `WIKI_SCHEMA.md`.
```

### 4.3 Commande pratique pour écrire le shim

```bash
cat > CLAUDE.md <<'EOT'
# CLAUDE.md — Shim de compatibilité

Ce fichier est conservé temporairement pour compatibilité.

Source canonique:
- `WIKI_SCHEMA.md`

Adaptation Claude:
- `adapters/claude.md`

Procédure:
1. Lire `WIKI_SCHEMA.md`.
2. Appliquer `adapters/claude.md`.
3. Exécuter les workflows selon `WIKI_SCHEMA.md`.

Notes:
- Ne plus maintenir de règles métier dans ce fichier.
- Toutes les évolutions de règles doivent être faites dans `WIKI_SCHEMA.md`.
EOT
```

Résultat attendu:
- `CLAUDE.md` reste présent, mais ne contient plus de logique métier.
- `WIKI_SCHEMA.md` devient le seul document métier à maintenir.

