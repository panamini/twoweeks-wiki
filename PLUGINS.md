# Plugins Obsidian recommandés — twoweeks Wiki

Plugins à installer manuellement via Settings → Community plugins.

## Essentiels

| Plugin | Usage | Installation |
|--------|-------|-------------|
| **Dataview** | Requêtes dynamiques sur le frontmatter YAML des pages wiki (tableaux, listes auto-générées) | Community plugins → Browse → "Dataview" |
| **Marp Slides** | Générer des présentations depuis le wiki en format Marp markdown | Community plugins → Browse → "Marp" |
| **Obsidian Web Clipper** | Convertir des articles web en markdown dans `raw/` (extension navigateur) | [obsidian.md/plugins/web-clipper](https://obsidian.md/plugins) |

## Recommandés

| Plugin | Usage | Installation |
|--------|-------|-------------|
| **Templater** | Templates pour créer rapidement des nouvelles pages source, entité, concept | Community plugins → "Templater" |
| **Various Completes** | Autocomplétion des liens `[[...]]` | Community plugins → "Various Completes" |
| **Kanban** | Suivre les sources à ingérer et les questions à investiguer | Community plugins → "Kanban" |

## Configuration post-installation

### Obsidian Web Clipper
Configurer pour sauvegarder dans `raw/` par défaut.

### Images locales
Dans Settings → Files and links :
- **Default location for new attachments** → `In the folder specified below`
- **Attachment folder path** → `raw/assets`

Dans Settings → Hotkeys :
- Chercher "Download attachments for current file"
- Assigner `Ctrl+Shift+D` (ou `Cmd+Shift+D` sur Mac)

Après avoir clipé un article, appuyer sur ce raccourci pour télécharger toutes les images localement.

### Dataview
Exemples de requêtes utiles dans le wiki :

```dataview
TABLE updated, tags FROM "wiki/concepts" SORT updated DESC
```

```dataview
TABLE type, date FROM "wiki/sources" SORT date DESC
```

```dataview
LIST FROM "wiki" WHERE !contains(file.outlinks, [[index]])
```
