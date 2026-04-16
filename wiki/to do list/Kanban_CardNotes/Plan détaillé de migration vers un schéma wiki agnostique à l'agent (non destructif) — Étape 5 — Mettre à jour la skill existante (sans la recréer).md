# Plan détaillé de migration vers un schéma wiki agnostique à l'agent (non destructif) — Étape 5 — Mettre à jour la skill existante (sans la recréer)


Mettre à jour `skills/twoweeks-wiki-operator` pour pointer vers `WIKI_SCHEMA.md`.

Contrôle:

```bash
rg -n "CLAUDE.md|WIKI_SCHEMA.md" skills/twoweeks-wiki-operator
```

Résultat attendu:
- Références principales vers `WIKI_SCHEMA.md`.
- `CLAUDE.md` mentionné uniquement comme shim transitoire.

