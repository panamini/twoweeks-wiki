Objectif: supprimer des secrets de l'historique Git avec un risque minimal de perte de dépôt ou de publication incomplète.

# 1. Pré-requis et règles de sécurité

- Travailler sur un clone dédié (ex: `neyssan-rewrite-clean`), pas sur le workspace principal.
- Vérifier que les secrets ont déjà été rotatés/révoqués côté fournisseurs.
- Préparer un fichier `replacements.txt` validé.
- Ne pas utiliser `--path` pour ce cas: `--path` filtre l'arbre et peut retirer des fichiers hors cible.

# 2. Préparation du clone de travail
Commandes :
```bash
cd ..

git clone https://github.com/panamini/neyssan.git neyssan-rewrite-clean

cd neyssan-rewrite-clean
```

Vérifications:
```bash
git status

git branch --show-current

git remote -v
```

Résultat attendu:
- `working tree clean`
- branche `main`
- remote `origin` présent

# 3. Préparer `replacements.txt`
Exemple de contenu de fichier validé:
```txt
regex:(?m)^OPENAI_API_KEY=.*$==>OPENAI_API_KEY=<OPENAI_API_KEY>

regex:(?m)^MISTRAL_API_KEY=.*(?:\r?\nMISTRAL_API_KEY=.*)?$==>MISTRAL_API_KEY=<MISTRAL_API_KEY>

regex:(?m)^\s*-\s*`MISTRAL_API_KEY`:\s*.*$==> - `MISTRAL_API_KEY`: Your Mistral API key.

regex:(?m)^[ \t]*<!--[ \t]*old key disabled: MISTRAL_API_KEY=<plain_text_api_key> -->\r?\n?==>
```

Note : <plain_text_api_key> est à remplacer par la chaine de caractère que l'on cherche à remplacer.

# 4. Positionnement correct
Il s'agit de s'assurer que l'on est bien placé dans le workspace adéquat et surtout que les commandes de réécriture se feront bien sur le repo local associé :
```bash
cd /Users/aurelienprivileggio/Workspace/neyssan-rewrite-clean

pwd

git rev-parse --show-toplevel
```

Si `git rev-parse --show-toplevel` affiche :
```txt
<absolute_path_workspace>/neyssan-rewrite-clean
```
alors les commandes concerneront bien ce repo.

# 4. Contrôle avant réécriture (preuve de présence)
Commandes :
```bash
git rev-list --all | while read c; do
git show "$c:my-app/env.md" 2>/dev/null
git show "$c:my-app/mistral_integration_backend.md" 2>/dev/null
done | grep -nE 'sk-[A-Za-z0-9_-]{20,}|<plain_text_api_key>|^[[:space:]]*<!--[[:space:]]*old key disabled: MISTRAL_API_KEY='
```

Résultat attendu: des lignes (avant nettoyage).

# 5. Réécriture d'historique
Commande :
```bash
git filter-repo --force --replace-text replacements.txt
```

Notes:
- `git-filter-repo` peut supprimer `origin` automatiquement: c'est normal. C'est fait volontairement pour éviter un push accidentel après réécriture d’historique.
- Pour vérifier, lancer les commandes ci-dessous :
	```bash
	git remote -v
	```
	Si `origin` a été supprimé, il n'y aura pas de lignes `origin...`.
	Une vérification plus directe est :
	```bash
	git remote get-url origin
	```
	Si `origin` existe, Git affiche son URL
	Si `origin` a été supprimé, Git renvoie une erreur du type `No such remote 'origin'`
- Si `origin` disparaît, le recréer:
```bash
git remote add origin https://github.com/panamini/neyssan.git
```

# 6. Contrôle après réécriture (preuve d'absence)
Commande de contrôle sur le `main` local :
```bash
git rev-list main | while read c; do
git show "$c:my-app/env.md" 2>/dev/null
git show "$c:my-app/mistral_integration_backend.md" 2>/dev/null
done | grep -nE 'sk-[A-Za-z0-9_-]{20,}|<plain_text_api_key>|^[[:space:]]*<!--[[:space:]]*old key disabled: MISTRAL_API_KEY='
```
Résultat attendu: aucune sortie.

Contrôle positif (formes désensibilisées présentes) sur le `main` local:
```bash
git rev-list main | while read c; do
git show "$c:my-app/env.md" 2>/dev/null
git show "$c:my-app/mistral_integration_backend.md" 2>/dev/null
done | grep -nE 'OPENAI_API_KEY=<OPENAI_API_KEY>|MISTRAL_API_KEY=<MISTRAL_API_KEY>|`MISTRAL_API_KEY`: Your Mistral API key\.'
```
Résultat attendu: pleins de lignes

Commande de contrôle sur `origin/main` (remote) :
```bash
git rev-list origin/main | while read c; do
git show "$c:my-app/env.md" 2>/dev/null
git show "$c:my-app/mistral_integration_backend.md" 2>/dev/null
done | grep -nE 'sk-[A-Za-z0-9_-]{20,}|<plain_text_api_key>|^[[:space:]]*<!--[[:space:]]*old key disabled: MISTRAL_API_KEY='
```
Résultat attendu: pleins de lignes

# 7. Publication de la réécriture
Avant push:
```bash
git remote -v

git fetch origin --prune
```

Push de toutes les branches et tags réécrits:
```bash
git push --force --all origin

git push --force --tags origin
```

Pourquoi `--all` + `--tags`:
- `main` seule ne suffit pas si d'autres branches/tags contiennent encore l'ancien historique.

# 8. Vérification post-publication

```bash
git fetch origin --prune

git rev-list --all | while read c; do

git show "$c:my-app/env.md" 2>/dev/null

git show "$c:my-app/mistral_integration_backend.md" 2>/dev/null

done | grep -nE 'sk-[A-Za-z0-9_-]{20,}|KvmzGFNnY0UjleuXu1HD8sRaajsyA1SX|^[[:space:]]*<!--[[:space:]]*old key disabled: MISTRAL_API_KEY='
```

Résultat attendu: aucune sortie.

# 9. Instructions aux autres contributeurs

- Reclone recommandé (option la plus sûre).
- Sinon:
```bash
git fetch origin --prune

git checkout main

git reset --hard origin/main
```

Puis recréer les branches de travail depuis `origin/main`.

# 10. Pièges rencontrés (retour d'expérience)

- `git filter-repo --path ...` peut supprimer des fichiers hors cible: éviter pour ce cas.
- En `zsh`, un pattern contenant `<!--` peut casser avec `event not found` si mal quoté: utiliser des quotes simples autour du regex dans les commandes `grep`.
- Après `fetch`, un contrôle sur `--all` inclut aussi les refs distantes: faire les contrôles au bon moment (avant/après push) et interpréter selon contexte.
- Ne jamais pousser avant d'avoir une preuve d'absence de secrets dans l'historique local.