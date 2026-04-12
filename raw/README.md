# raw/ — Sources brutes

Ce dossier contient toutes les sources brutes du wiki twoweeks.

**Règle fondamentale : ce dossier est IMMUABLE.** Le LLM lit les fichiers ici mais ne les modifie jamais. C'est la source de vérité du projet.

## Comment alimenter ce dossier

1. **Obsidian Web Clipper** (recommandé) — extension navigateur qui convertit les articles web en markdown directement dans ce dossier
2. **Copier-coller manuel** — créer un `.md` avec le contenu de l'article/document
3. **Télécharger** des PDFs, papers, repos, datasets

## Images

Toutes les images sont dans `raw/assets/`. Dans Obsidian :
- Settings → Files and links → "Attachment folder path" → `raw/assets`
- Settings → Hotkeys → "Download attachments for current file" → `Ctrl+Shift+D`

## Convention de nommage

```
raw/YYYY-MM-DD-titre-source.md
raw/assets/nom-image.png
```

## Après avoir ajouté une source

Dire à Claude (dans Cowork ou Claude Code) :
> "Ingère la source `raw/YYYY-MM-DD-titre.md` dans le wiki"

Le LLM se chargera de tout : résumé, mise à jour des pages existantes, index et log.
