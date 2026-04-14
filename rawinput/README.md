# rawinput/ — Zone de staging

Ce dossier est la **zone d'entrée** pour toutes les nouvelles sources. C'est ici que tu déposes les fichiers avant ingestion.

## Workflow

1. **Dépose ici** : articles clippés, PDFs, notes, transcripts, datasets
2. **Dis à Claude** : `"Ingère les nouvelles sources"` ou `"Traite rawinput/"`
3. **Claude s'occupe du reste** :
   - Lit et analyse chaque fichier
   - Crée les pages wiki correspondantes
   - Déplace le fichier vers `raw/` (archive permanente)
   - Met à jour `wiki/index.md` et `wiki/log.md`

## Pourquoi ce dossier existe

Sans `rawinput/`, détecter les "nouvelles" sources nécessiterait de scanner tout `raw/` à chaque session — un scan dont le coût croît avec la taille de la collection. Avec `rawinput/`, le LLM ne scanne que ce petit dossier. La performance est indépendante du nombre total de sources.

## Convention de nommage

```
YYYY-MM-DD-titre-source.md
YYYY-MM-DD-titre-source.pdf
```

## Ce dossier devrait toujours être vide (ou presque)

Si `rawinput/` contient des fichiers, c'est qu'une ingestion est en attente. Après chaque ingest réussi, ce dossier doit être vide — les fichiers ont migré dans `raw/`.

## Images

Les images sont déplacées vers `raw/assets/` lors de l'ingest.

