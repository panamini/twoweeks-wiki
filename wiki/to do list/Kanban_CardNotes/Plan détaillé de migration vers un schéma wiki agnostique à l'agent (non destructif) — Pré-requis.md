# Plan détaillé de migration vers un schéma wiki agnostique à l'agent (non destructif) — Pré-requis


- Se placer à la racine du vault (dossier qui contient `CLAUDE.md`, `rawinput/`, `raw/`, `wiki/`).
- Vérifier l'état Git avant de commencer.

```bash
git status --short
```

Résultat attendu:
- Une liste de fichiers modifiés/non suivis déjà présents.
- Tu gardes cette sortie comme point de référence avant migration.

