# Plan détaillé de migration vers un schéma wiki agnostique à l'agent (non destructif) — Étape 1 — Ajouter une spec neutre sans supprimer l'existant


Créer une copie de travail agnostique.

```bash
cp CLAUDE.md WIKI_SCHEMA.md
```

Résultat attendu:
- `CLAUDE.md` existe toujours.
- `WIKI_SCHEMA.md` est créé.

Vérification:

```bash
ls -1 CLAUDE.md WIKI_SCHEMA.md
```

