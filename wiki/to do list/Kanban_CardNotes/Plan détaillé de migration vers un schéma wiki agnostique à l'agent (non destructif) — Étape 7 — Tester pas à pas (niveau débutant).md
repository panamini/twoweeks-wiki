# Plan détaillé de migration vers un schéma wiki agnostique à l'agent (non destructif) — Étape 7 — Tester pas à pas (niveau débutant)


Objectif: vérifier que le système marche après migration sans toucher aux pages métier existantes.

### 7.1 Test A — Bootstrap (lecture des bons fichiers)

Action:
- Ouvrir `WIKI_SCHEMA.md`.
- Ouvrir `wiki/index.md`.
- Ouvrir `wiki/log.md` (10 dernières entrées).
- Ouvrir `wiki/overview.md`.
- Lister `rawinput/`.

Commandes:

```bash
sed -n '1,80p' WIKI_SCHEMA.md
sed -n '1,80p' wiki/index.md
tail -n 120 wiki/log.md
sed -n '1,80p' wiki/overview.md
ls -la rawinput/
```

Résultat attendu:
- Tous les fichiers sont lisibles.
- Tu vois clairement le nombre de sources en attente dans `rawinput/`.

### 7.2 Test B — Query simple (sans écriture)

Action:
- Poser une question simple: "Quel est l'état actuel du projet ?"
- Vérifier que la réponse est basée sur des pages `status: current`.

Vérification manuelle:

```bash
rg -n "status:\s*current" wiki/overview.md wiki/concepts/*.md wiki/entities/*.md | head -n 20
```

Résultat attendu:
- Les réponses s'appuient d'abord sur les contenus `current`.

### 7.3 Test C — Lint léger (sans créer de rapport)

Action:
- Contrôler frontmatter et liens cassés de base.

Commandes:

```bash
rg -n "^status:" wiki/**/*.md
rg -n "\[\[[^\]]+\]\]" wiki/**/*.md | head -n 40
```

Résultat attendu:
- Les pages importantes ont un `status`.
- Les liens internes sont présents.

### 7.4 Test D — Ingest de test contrôlé (avec rollback facile)

Action:
1. Créer un mini fichier de test dans `rawinput/`.
2. Simuler l'ingestion (création d'une page source).
3. Vérifier le déplacement vers `raw/`.
4. Supprimer les artefacts de test (rollback manuel).

Commandes:

```bash
cat > rawinput/2099-01-01-test-ingest.md <<'EOT'
# Test ingest
Ceci est un test temporaire.
EOT

ls -la rawinput/2099-01-01-test-ingest.md
```

Résultat attendu:
- Le fichier test est créé.

Ensuite, exécuter l'ingestion via ton agent puis vérifier:

```bash
ls -la raw/2099-01-01-test-ingest.md
rg -n "2099-01-01-test-ingest" wiki/sources/*.md
```

Résultat attendu:
- Le fichier test est dans `raw/`.
- Une page source de test existe dans `wiki/sources/`.

Rollback test:

```bash
rm -f raw/2099-01-01-test-ingest.md
rm -f wiki/sources/2099-01-01-test-ingest.md
```

Résultat attendu:
- Plus de trace des artefacts de test.

### 7.5 Test E — Vérification Git finale

```bash
git status --short
```

Résultat attendu:
- Tu vois uniquement les changements attendus de migration.
- Pas de fichiers de test oubliés.

