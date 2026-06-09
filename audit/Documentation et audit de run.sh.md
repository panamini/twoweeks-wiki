Prompts utilisés :
1. En tant que développeur bash, rédige une documentation expliquant ce que fait le script run.sh Procède à un audit du script et propose en fin de la documentation des améliorations. En plus de ces améliorations, explique comment améliorer la production de logs et l'ajout de commentaires dans ce script. Je veux que le document généré soit précis, détaillé, accessible à un novice et professionnel. Ne modifie aucun fichier existant.
2. Ok, le document généré m'a l'air pas mal mais on va l'améliorer pour que run.sh soit apte à aller en exploitation (environnement de Prod) :
	- considères-tu qu'il serait envisageable de modulariser ce script ? Si oui, inclue cela comme amélioration dans le document existant en donnant les avantages à faire ça.
	- Même question mais pour la mise en fichier de properties de certaines variables.
	- toutes les améliorations proposées doivent être précises, détaillées étape par étape et très accessibles.
	- y a-t-il des tests avant/après les actions ? L'idée derrière cette question est l'idempotence. Propose les améliorations adéquates pour rendre le script idempotent.
	Le seul fichier à modifier est 2026-06-08-run-sh-documentation-audit.md

  

Date: 2026-06-08

Portée: ce document décrit le script `run.sh` à la racine du dépôt. Le script est du code actif: il sert de point d'entrée local pour lancer, arrêter, diagnostiquer et reconstruire la pile de développement autour du parser CV, de Vite, de Convex local et du tunnel Cloudflare.

Vérification réalisée: lecture du script et vérification syntaxique avec `bash -n run.sh`. Aucun lancement de Docker, Vite, Convex ou tunnel n'a été exécuté pour cet audit.

## 1. Résumé pour débutant

`run.sh` est un script Bash d'orchestration. Son rôle est de simplifier des commandes longues et répétitives en une interface unique:

```bash
./run.sh local-fast

./run.sh tunnel

./run.sh down

./run.sh status
```

En pratique, il peut
* construire ou réutiliser une image Docker du service de parsing de CV;
- démarrer le parser local sur `http://127.0.0.1:8001`;
- démarrer l'application frontend Vite dans `my-app`;
- démarrer un backend Convex local pour le mode de développement rapide;
- démarrer un tunnel Cloudflare avec `cloudflared`;
- suivre les processus lancés dans un fichier d'état;
- arrêter ou nettoyer les processus et conteneurs qu'il connaît;
- vérifier rapidement si les services répondent.

Pour un novice, il faut comprendre que ce script n'est pas seulement un "run". C'est un petit superviseur de pile locale. Il choisit quoi lancer selon la commande et les options passées.

## 2. Principes Bash utilisés

Le script commence par:

```bash
#!/usr/bin/env bash
set -euo pipefail
```

Cela signifie
- `bash`: le script doit être exécuté avec Bash, pas avec `sh`.
- `set -e`: le script s'arrête quand une commande échoue, sauf exceptions gérées.
- `set -u`: utiliser une variable non définie provoque une erreur.
- `set -o pipefail`: dans un pipeline, une erreur intermédiaire est prise en compte.

Ces options rendent le script plus strict et évitent beaucoup de comportements silencieux. En contrepartie, chaque commande qui peut échouer normalement doit être explicitement protégée avec `|| true` ou un test.

## 3. Chargement de l'environnement

Au démarrage, le script:
1. lit la commande demandée dans le premier argument;
2. place le répertoire courant à la racine du dépôt;
3. charge des variables depuis `.env`, `.env.local` et `my-app/.env`;
4. définit des valeurs par défaut si certaines variables ne sont pas déjà présentes.

Variables importantes:
- `PARSER_ORIGIN`: origine distante du parser, par défaut `https://parser.dasti.ai`.
- `OPEN_BROWSER`: ouvre ou non le navigateur quand Vite démarre.
- `TUNNEL_NETWORK`: réseau Docker partagé entre parser et tunnel.
- `PARSER_NAME`: nom du conteneur Docker du parser.
- `CLOUDFLARED_NAME`: nom du conteneur Cloudflare.
- `IMAGE_NAME`: image Docker runtime du parser.
- `PARSER_RUNTIME_MODE`: mode `image` ou `workspace`.
- `VITE_PORT`: port Vite souhaité, par défaut `5173`.
- `TUNNEL_TOKEN`: token requis pour le mode tunnel.

Le script crée aussi des dossiers de travail:
- `tmp/dev-stack`: état des processus;
- `tmp`: logs Vite, Convex et autres fichiers temporaires;
- `tmp/convex-tmp`: fichiers temporaires Convex;
- `.buildx-cache`: cache Docker Buildx;
- `.docker`: petites informations d'état liées aux builds Docker.

Il peut aussi charger automatiquement `MISTRAL_API_KEY` depuis `~/.mistral_key` si la variable n'est pas déjà définie.

## 4. Fichier d'état

Le script écrit son état dans:

```text
tmp/dev-stack/pids.env
```

Ce fichier contient notamment:
- PID Vite;
- indicateur de parser démarré;
- PID Convex;
- URL Convex;
- indicateur de tunnel démarré;
- mode de pile actif;
- origine parser utilisée par le frontend;
- mode runtime parser;
- mode OCR;
- hash des fichiers d'environnement.

Ce fichier permet à `down`, `reload-env`, `status` et aux relances de savoir ce qui a été lancé précédemment.

Point important: le script ne supervise pas tout le système. Il supervise surtout ce qu'il a lancé et ce qu'il peut retrouver par nom de conteneur, PID ou port.

## 5. Construction de l'image parser

Le bloc Docker construit l'image runtime du parser à partir de `cv_parser_service/Dockerfile`.

Le script calcule une signature basée sur:
- `cv_parser_service/Dockerfile`;
- `package.json`;
- `package-lock.json`;
- `my-app/package.json`;
- `my-app/package-lock.json`;
- `.dockerignore`;
- la plateforme CPU détectée.

Si l'image existe déjà et que cette signature n'a pas changé, le script évite de reconstruire. Sinon, il utilise Docker Buildx avec cache local.

Le mode par défaut est `image`, ce qui veut dire que le parser tourne dans une image Docker construite. Le mode `workspace` monte le dépôt dans le conteneur pour itérer plus vite sur le code local.

## 6. Parser CV

Le parser est lancé dans Docker sous le nom `cv-parser-service-dev` par défaut. Il expose:

```text
http://127.0.0.1:8001
```

Le script démarre Uvicorn avec l'application:

```text
cv_parser_service.main:app
```

Il vérifie ensuite:

```text
http://127.0.0.1:8001/ready
```

Modes OCR possibles:
- `auto`: mode par défaut;
- `doctr`: force Doctr;
- `paddle`: force Paddle;
- `disabled`: désactive l'OCR.

Si `MISTRAL_API_KEY` est disponible et que la synchronisation de secrets est active, le script active aussi Mistral OCR côté conteneur.

## 7. Convex local

Le mode `local-fast` démarre un backend Convex local. Avant de le faire, le script cherche les informations de binding:
- `CONVEX_TEAM`;
- `CONVEX_TEAM_SLUG`;
- `CONVEX_PROJECT`;
- `CONVEX_PROJECT_SLUG`;
- `CONVEX_LOCAL_DEPLOYMENT_NAME`;
- `CONVEX_LOCAL_DEPLOYMENT`;
- `CONVEX_DEPLOYMENT`.

Il cherche ces valeurs dans:
- `.env.local`;
- `.env`;
- `my-app/.env.local`;
- `my-app/.env`.

Il vérifie aussi que les ports Convex attendus ne sont pas occupés par un autre service. Par défaut:
- cloud local Convex: `3210`;
- site local Convex: `3211`.

Le log Convex est écrit dans:

```text
tmp/convex-dev.log
```

Après le démarrage, le script synchronise certaines variables d'environnement dans Convex local. Cela inclut des variables applicatives, des URLs et potentiellement des secrets si `LOCAL_CONVEX_SYNC_SECRETS` est actif.

## 8. Frontend Vite

Quand l'option `--ui` est utilisée, le script démarre Vite depuis `my-app`.

Il configure plusieurs variables côté frontend:
- `CONVEX_PARSER_URL`;
- `VITE_PARSER_URL`;
- `VITE_CONVEX_PARSER_URL`;
- `VITE_CONVEX_URL` si Convex local est utilisé;
- `NEXT_PUBLIC_CONVEX_URL` si Convex local est utilisé.

Le log Vite est écrit dans:

```text
tmp/vite-dev.log
```

Avant de démarrer Vite, le script tue les processus qui écoutent sur les ports `5173` à `5215`.

## 9. Tunnel Cloudflare

Le mode tunnel démarre un conteneur `cloudflare/cloudflared:latest`. Il nécessite:

```bash
TUNNEL_TOKEN=...
```

Le tunnel est connecté au réseau Docker défini par `TUNNEL_NETWORK`, par défaut `parsernet`. Ce réseau sert à rendre le parser accessible depuis le connecteur Cloudflare.

## 10. Commandes disponibles

### 10.1 Commande `./run.sh local-fast`

Commande recommandée pour un développement rapide complet.

Elle lance:
- parser local;
- runtime parser en mode `workspace`;
- autoreload Uvicorn;
- Convex local;
- Vite;
- frontend pointé vers le parser local.

Usage typique:

```bash
./run.sh local-fast

./run.sh local-fast --ocr disabled
```

### 10.2 Commande `./run.sh local`

Lance:
- parser local en runtime image;
- Vite;
- Convex dans son mode configuré par l'environnement, généralement cloud.

C'est utile pour tester le frontend avec un parser local tout en conservant le backend Convex existant.

### 10.3 Commande `./run.sh local-convex`

Alias legacy. Le script affiche que `local-convex` est remplacé par `local-fast`, puis appelle `local-fast`.

### 10.4 Commande `./run.sh tunnel`

Mode de validation stable avec:
- frontend Vite;
- origine parser edge;
- Convex cloud ou environnement existant;
- tunnel Cloudflare démarré par le script.

Ce mode dépend d'un `TUNNEL_TOKEN`.

### 10.5 Commande `./run.sh parser-dev`

Mode avancé pour travailler seulement sur le parser.

Il lance:
- parser Docker;
- montage du workspace;
- autoreload Uvicorn;
- pas de Vite;
- pas de Convex local.

Ce mode est rapide pour modifier du Python, mais le script indique lui-même que ce n'est pas le meilleur mode pour valider la parité runtime/export.

### 10.6 Commande `./run.sh reload-env`

Recharge la pile courante après changement de `.env`, `.env.local`, `my-app/.env.local` ou `my-app/.env`.

Le script compare des hashes d'environnement et redémarre seulement ce qui est nécessaire:
- parser si l'environnement a changé;
- Convex local si le binding Convex local a changé;
- tunnel si nécessaire;
- Vite si l'UI était active.

### 10.7 Commande `./run.sh rebuild-docker`

Force la reconstruction de l'image runtime du parser, arrête la pile courante, reconstruit, relance le mode précédent quand c'est possible, puis vérifie `/ready`.

### 10.8 Commande `./run.sh down`

Arrêt normal. Il arrête les processus suivis par le fichier d'état:
- Vite;
- Convex local;
- parser;
- tunnel si lancé par la pile.

Il supprime ensuite le fichier d'état.

### 10.9 Commande `./run.sh reset`

Nettoyage plus fort que `down`.

Il:
- appelle `down`;
- supprime les conteneurs parser et cloudflared par nom;
- tue des processus Convex considérés comme stale;
- tue les processus sur les ports Vite `5173-5215`;
- supprime certains fichiers d'état et logs temporaires.

Cette commande est utile quand une pile locale est bloquée, mais elle est plus intrusive que `down`.

### 10.10 Commande `./run.sh status`

Affiche:
- statut `/ready` local du parser;
- statut `/ready` edge du parser;
- statut Convex local;
- runtime parser;
- image parser;
- statut tunnel;
- mode de pile enregistré;
- chemin du log Vite.

### 10.11 Commande `./run.sh logs`

Affiche les logs Docker du conteneur parser:

```bash
docker logs -f --tail=200 cv-parser-service-dev
```

Cette commande ne suit pas les logs Vite ni Convex.

### 10.12 Commande `./run.sh smoke`

Appelle le endpoint local:

```text
http://127.0.0.1:8001/ready
```

et formate la réponse avec `jq`.

### 10.13 Commande `./run.sh assert-ocr FILE.pdf`

Envoie un PDF au parser local en mode OCR et affiche quelques diagnostics avec `jq`.

### 10.14 Commande `./run.sh probe-edge [FILE.pdf]`

Teste l'origine edge configurée par `PARSER_ORIGIN`.

Il vérifie:
- `GET /ready`;
- `GET /mistral-ocr/parse`;
- éventuellement un `POST /mistral-ocr/parse` avec service token Cloudflare Access si `CF_ACCESS_CLIENT_ID` et `CF_ACCESS_CLIENT_SECRET` sont configurés.

### 10.15 Commande `./run.sh kill-vite-ports`

Tue les processus qui écoutent sur les ports `5173` à `5215`.

## 11. Audit technique

### 11.1 Points solides

- Le script utilise `set -euo pipefail`, ce qui réduit les erreurs silencieuses.
- Les variables sont majoritairement citées avec des guillemets, ce qui limite les problèmes d'espaces dans les chemins.
- Les commandes longues sont encapsulées dans des fonctions.
- L'état est centralisé dans `tmp/dev-stack/pids.env`.
- Les modes principaux sont explicites: `local-fast`, `local`, `tunnel`, `parser-dev`.
- La reconstruction Docker évite des rebuilds inutiles via une signature locale.
- Le script vérifie les health checks parser et Convex avant de considérer le démarrage comme réussi.
- Les dépendances runtime du mode `workspace` sont vérifiées après démarrage.
- `reload-env` évite un rebuild Docker quand seuls les fichiers d'environnement changent.

### 11.2 Risques et limites confirmés

1. `my-app/.env.local` est pris en compte dans les hashes mais n'est pas sourcé au démarrage.
	Le script source `.env`, `.env.local` et `my-app/.env`, mais pas `my-app/.env.local`. Pourtant `env_reload_hash` et plusieurs fonctions Convex lisent `my-app/.env.local`. Cela peut créer une différence entre les fichiers observés pour détecter un changement et les variables réellement chargées dans le shell.

2. `kill_vite_ports` tue brutalement tous les listeners entre `5173` et `5215`.
	La fonction utilise `kill -9` sur tout processus écoutant sur cette plage. C'est efficace, mais potentiellement dangereux si un autre projet utilise un port dans cette plage. Le comportement est particulièrement intrusif pour `reset`, mais il est aussi appelé au démarrage et à l'arrêt de Vite.

3. Les logs sont fragmentés.
	Le parser est principalement consulté via `docker logs`, Vite écrit dans `tmp/vite-dev.log`, Convex écrit dans `tmp/convex-dev.log`, et `status` n'affiche que le chemin du log Vite. Il n'y a pas de commande unique pour voir toute la pile.

4. Les messages ne portent pas tous un niveau de gravité structuré.
	Le préfixe `[run]` est utile, mais il ne distingue pas systématiquement `INFO`, `WARN`, `ERROR`, `DEBUG`. Cela complique la recherche rapide dans les logs.

5. Les secrets peuvent apparaître dans des contextes de processus ou de logs indirects.
	Le script passe `MISTRAL_API_KEY` à Docker via `-e "MISTRAL_API_KEY=..."`. C'est courant en développement, mais cela reste sensible. La synchronisation Convex locale peut aussi pousser des secrets quand `LOCAL_CONVEX_SYNC_SECRETS` est actif.

6. Le conteneur `cloudflare/cloudflared:latest` n'est pas pinne.
	Utiliser `latest` rend les exécutions moins reproductibles. Une mise à jour amont peut modifier le comportement du tunnel sans changement dans le dépôt.

7. Le script mélange orchestration Bash et petits programmes Node inline.
	Les blocs `node -e` sont fonctionnels, mais ils rendent la maintenance plus difficile pour un développeur qui lit seulement Bash. Ils sont utilisés pour lancer des processus détachés et lire du JSON.

8. Certains parseurs de fichiers `.env` sont simplifiés.
	Le script utilise `source` pour charger certains fichiers, puis `grep`, `cut`, `xargs` et des regex pour en lire d'autres. C'est suffisant pour des lignes simples `KEY=value`, mais plus fragile avec des valeurs contenant `#`, des guillemets complexes ou des espaces significatifs.

9. `down` dépend fortement de l'état enregistré.
	`down` arrête principalement ce que `pids.env` décrit. Si le fichier d'état est absent, corrompu ou ancien, certains processus peuvent rester actifs. `reset` compense partiellement avec des recherches par nom et port.

10. Le trap `INT TERM` appelle `down`.
	C'est utile pour nettoyer après `Ctrl+C`, mais cela peut aussi arrêter une pile déjà lancée si l'utilisateur interrompt une sous-commande qui ne faisait qu'observer ou diagnostiquer.

## 12. Aptitude actuelle pour une exploitation production

En l'état, `run.sh` est adapte a un environnement de développement local avancé. Il n'est pas encore prêt tel quel pour devenir un script d'exploitation production.

Les raisons principales sont:
- il mélange des modes de développement (`local-fast`, `parser-dev`, `workspace`, autoreload) et des modes plus stables (`tunnel`, runtime image);
- il contient des actions destructives pratiques en local, comme tuer des ports ou supprimer des conteneurs par nom;
- il dépend de fichiers `.env` locaux et de conventions de poste développeur;
- il ne sépare pas clairement configuration, orchestration, vérification, logs et nettoyage;
- il ne fournit pas encore de contrat d'idempotence strict pour chaque action;
- il ne trace pas toutes les opérations avec un niveau de détail suffisant pour une investigation production;
- il utilise `cloudflare/cloudflared:latest`, ce qui n'est pas reproductible;
- il ne distingue pas encore clairement secrets, configuration non sensible et état runtime.

Pour viser une exploitation, le script devrait être traité comme un outil opérationnel avec des garanties explicites:
- une action peut être relancée sans casser l'état courant;
- les préconditions sont vérifiées avant chaque changement;
- les postconditions prouvent que l'action a réussi;
- les logs permettent de comprendre l'ordre exact des opérations;
- la configuration est versionnée ou injectée proprement;
- les secrets ne sont jamais affichés;
- les commandes dangereuses demandent une confirmation ou sont reservées à un mode maintenance.

## 13. Améliorations proposées

### 13.1 Priorité haute

1. Charger explicitement `my-app/.env.local` au démarrage.
	Le script l'utilise déjà pour les hashes et la résolution Convex. Le sourcer rendrait le comportement plus cohérent.
	Etapes proposées:
	1. Ajouter `my-app/.env.local` dans le bloc de chargement initial.
	2. Définir l'ordre de priorite attendu: fichier global, fichier local, fichier app, fichier app local.
	3. Documenter cet ordre dans l'aide.
	4. Ajouter une commande `config-print --redacted` pour afficher les valeurs effectives sans secrets.
	5. Vérifier avant/après avec une variable non sensible définie uniquement dans `my-app/.env.local`.

2. Remplacer `kill -9` par une stratégie progressive.
	Proposition:
	- envoyer d'abord `TERM`;
	- attendre brièvement;
	- vérifier si le processus écoute encore;
	- utiliser `KILL` seulement en dernier recours;
	- afficher la commande/processus propriétaire avant suppression.
	Etapes proposées:
	1. Créer une fonction `stop_pid_gracefully PID SERVICE_NAME`.
	2. Dans cette fonction, vérifier que le PID existe avec `kill -0`.
	3. Envoyer `TERM`.
	4. Attendre une courte période configurable, par exemple `STOP_TIMEOUT_SECONDS=10`.
	5. Recontroler si le PID existe.
	6. Envoyer `KILL` seulement si le processus est encore vivant.
	7. Journaliser chaque étape avec le service concerné.
	8. Pour les ports Vite, vérifier que le processus correspond bien au projet courant avant de le tuer.

3. Ajouter une commande `logs-all`.
	Elle pourrait afficher ou suivre:
	- logs parser Docker;
	- `tmp/vite-dev.log`;
	- `tmp/convex-dev.log`;
	- derniers messages d'état `run.sh`.
	Etapes proposées:
	1. Créer une commande `logs all`.
	2. Créer aussi `logs parser`, `logs vite`, `logs convex`, `logs run`.
	3. Pour chaque source, afficher clairement son origine avant les lignes de logs.
	4. Ajouter une option `--tail N`.
	5. Ajouter une option `--follow`.
	6. Masquer les secrets au moment de l'affichage si le log principal peut contenir de la configuration.

4. Ajouter des fonctions standardisées de log.
	Exemple:
	```bash
	log_info() { printf '[run][INFO] %s\n' "$*"; }
	
	log_warn() { printf '[run][WARN] %s\n' "$*" >&2; }
	
	log_error() { printf '[run][ERROR] %s\n' "$*" >&2; }
	```
	Cela rendrait les messages homogènes et faciles à filtrer.
	Etapes proposées:
	1. Ajouter `timestamp`, `log_info`, `log_warn`, `log_error`, `log_debug`.
	2. Ajouter `RUN_LOG_FILE="${LOG_DIR}/run-dev-stack.log"`.
	3. Faire écrire les logs à la fois sur la sortie standard et dans ce fichier.
	4. Remplacer progressivement les `echo "[run] ..."` par ces fonctions.
	5. Ajouter `LOG_LEVEL=info` par défaut.
	6. Vérifier qu'une erreur critique apparait bien dans la console et dans le fichier principal.

5. Pinner l'image `cloudflare/cloudflared`.
	Remplacer `cloudflare/cloudflared:latest` par une version ou un digest documenté améliore la reproductibilité du mode tunnel.
	Etapes proposées:
	1. Introduire une variable `CLOUDFLARED_IMAGE`.
	2. Définir une valeur par défaut versionnée, par exemple `cloudflare/cloudflared:<version>`.
	3. Documenter la procédure de mise à jour de cette version.
	4. Ajouter la valeur effective dans `status`.
	5. En production, préférer un digest immuable si la politique de déploiement l'exige.

6. Séparer clairement les modes développement et production.
	Le script contient aujourd'hui des comportements très utiles en local mais inappropriés en production, par exemple `workspace`, `--reload`, ouverture de navigateur, nettoyage agressif de ports et alias legacy.
	Etapes proposées:
	1. Ajouter une variable `RUN_ENV=dev|staging|prod`, avec `dev` par défaut.
	2. Interdire `workspace`, `parser-dev`, `local-fast`, `--parser-reload` et `OPEN_BROWSER=1` quand `RUN_ENV=prod`.
	3. Interdire `reset` en production sauf option explicite `--confirm-maintenance`.
	4. Remplacer les messages d'erreur par des explications courtes et actionnables.
	5. Ajouter `./run.sh doctor --env prod` pour vérifier que le mode prod respecte les contraintes.
	6. Documenter les commandes autorisées en production, par exemple `up`, `down`, `status`, `logs`, `smoke`, `reload-env` si valide.

7. Ajouter des préchecks bloquants pour la production.
	Etapes proposées:
	1. Vérifier que Docker est disponible.
	2. Vérifier que l'image runtime attendue existe ou que la stratégie de build est autorisée.
	3. Vérifier que les ports requis sont libres ou déjà détenus par le bon service.
	4. Vérifier que les variables obligatoires sont présentes.
	5. Vérifier que les secrets ne sont pas vides.
	6. Vérifier que `cloudflared` est pinné si le tunnel est utilise.
	7. Refuser de continuer si une précondition critique échoue.

### 13.2 Priorité moyenne

1. Extraire les blocs Node inline dans des scripts dédiés.
	Des fichiers comme `scripts/spawn-detached.cjs` ou `scripts/read-convex-config.cjs` seraient plus lisibles, testables et commentables.
	Etapes proposées:
	1. Identifier chaque bloc `node -e`.
	2. Donner un nom fonctionnel à chaque responsabilité : spawn détaché, lecture JSON Convex, vérification HTTP.
	3. Créer un fichier script dédié par responsabilité.
	4. Ajouter une aide courte dans chaque script Node.
	5. Remplacer l'appel inline par `node scripts/<nom>.cjs`.
	6. Tester chaque script séparément avant de modifier le flux principal.
	7. Garder une compatibilité des arguments pour éviter de changer le comportement.

2. Ajouter une option `--dry-run`.
	Elle permettrait de comprendre ce que le script va lancer ou tuer sans exécuter les actions. C'est utile pour les novices et pour les revues.
	Etapes proposées:
	1. Ajouter une variable globale `DRY_RUN=0`.
	2. Ajouter un helper `run_cmd` qui affiche puis exécute une commande.
	3. Si `DRY_RUN=1`, `run_cmd` affiche seulement l'action.
	4. Remplacer progressivement les appels sensibles par `run_cmd`.
	5. Commencer par Docker, kill, rm et build.
	6. Ajouter `./run.sh up --dry-run` et `./run.sh reset --dry-run`.
	7. Vérifier que `--dry-run` ne modifie aucun fichier d'état.

3. Renforcer le parsing `.env`.
	Idéalement, utiliser une seule stratégie pour charger et inspecter les fichiers d'environnement. Si Bash reste la seule option, documenter clairement que seules les lignes simples `KEY=value` sont supportées dans certains chemins de lecture.
	Etapes proposées:
	1. Choisir un format officiel pour la configuration non sensible.
	2. Pour Bash pur, limiter les properties a `KEY=value` sans expansion complexe.
	3. Refuser ou avertir sur les lignes ambiguës.
	4. Utiliser la même fonction pour lire, valider et hasher la configuration.
	5. Ajouter un mode `config-validate`.
	6. Ajouter des exemples de fichiers dans la documentation.

4. Rendre le nettoyage Vite plus ciblé.
	Au lieu de tuer toute la plage `5173-5215`, conserver le PID exact de Vite et ne tuer les ports que si le processus correspond au projet courant ou à une commande Vite.
	Etapes proposées:
	1. Lire d'abord `VITE_PID` depuis le fichier d'état.
	2. Vérifier que ce PID correspond à un processus Vite lancé depuis `my-app`.
	3. Arrêter ce PID proprement.
	4. Ne scanner les ports qu'en fallback.
	5. En fallback, afficher le processus trouvé et demander confirmation hors mode CI.
	6. En production, interdire le kill par plage de ports.

5. Ajouter une commande `doctor`.
	Elle pourrait vérifier:
	- Docker disponible;
	- Buildx disponible;
	- Node disponible;
	- `my-app/node_modules` présent;
	- Convex CLI présent;
	- `jq`, `curl`, `lsof`, `pgrep` disponibles;
	- ports attendus disponibles;
	- fichiers `.env` essentiels présents.
	Etapes proposées:
	1. Créer une fonction `doctor`.
	2. Ajouter des checks indépendants, chacun avec un nom clair.
	3. Pour chaque check, afficher `OK`, `WARN` ou `FAIL`.
	4. Retourner un code non nul si au moins un check critique est en échec.
	5. Ajouter `doctor --env dev`, `doctor --env staging`, `doctor --env prod`.
	6. Ajouter `doctor --json` pour une intégration CI/CD.

6. Modulariser le script.
	Oui, il est envisageable et recommandé de modulariser `run.sh`, surtout si l'objectif est une exploitation production.
	Aujourd'hui, le script fait 1677 lignes et contient plusieurs responsabilités:
	- chargement de configuration;
	- fonctions utilitaires;
	- build Docker;
	- orchestration parser;
	- orchestration Convex;
	- orchestration Vite;
	- orchestration tunnel;
	- gestion de l'état;
	- logs;
	- diagnostics;
	- nettoyage;
	- dispatch des commandes.
	Ces responsabilités peuvent rester en Bash, mais elles devraient être séparées en fichiers plus courts.
	Structure cible possible:
	```text
	scripts/run/
	main.sh # point d'entree et dispatch des commandes
	config.sh # chargement et validation de configuration
	logging.sh # fonctions de logs
	state.sh # lecture/ecriture de pids.env
	docker.sh # build image, buildx, image id
	parser.sh # start/stop/status parser
	convex.sh # start/stop/status Convex local
	vite.sh # start/stop/status Vite
	tunnel.sh # start/stop/status cloudflared
	checks.sh # prechecks, postchecks, doctor
	cleanup.sh # down/reset/maintenance
	```
	Le fichier `run.sh` racine peut rester comme wrapper stable:
	```bash
	#!/usr/bin/env bash
	set -euo pipefail
	source "$(dirname "${BASH_SOURCE[0]}")/scripts/run/main.sh"
	main "$@"
	```
	Avantages:
	- lecture plus simple pour un nouveau contributeur;
	- tests plus faciles, car chaque module a une responsabilité claire;
	- risque réduit de casser Convex en modifiant Docker, ou Vite en modifiant le tunnel;
	- réutilisation possible de fonctions communes comme logs, checks et état;
	- meilleure séparation entre développement et production;
	- meilleure revue de code, car les diffs sont plus petits;
	- possibilité de remplacer progressivement certaines parties par des scripts plus robustes sans tout réécrire.
	Etapes proposées:
	1. Ne pas tout découper en une seule fois.
	2. Extraire d'abord `logging.sh`, car il a peu de dépendances.
	3. Extraire ensuite `state.sh`, car la lecture/écriture d'état est centrale.
	4. Extraire `config.sh`, avec validation et affichage redacted.
	5. Extraire `checks.sh`, pour préparer l'idempotence.
	6. Extraire les modules service par service: parser, Vite, Convex, tunnel.
	7. Garder `run.sh` compatible avec les commandes actuelles.
	8. Apres chaque extraction, exécuter `bash -n` et un test de non-regression sur `help`, `status`, puis un mode de démarrage.
	9. Documenter le contrat de chaque module en haut du fichier.
	10. Eviter les dépendances circulaires: les modules service peuvent utiliser `logging`, `state`, `config`, `checks`, mais pas l'inverse.

7. Mettre certaines variables dans un fichier de properties.
	Oui, c'est envisageable et recommandé, à condition de séparer les variables non sensibles des secrets.
	Objectif: sortir du script les valeurs qui changent selon l'environnement, sans rendre le script plus fragile.
	Variables candidates non sensibles:
	- `PARSER_ORIGIN`;
	- `OPEN_BROWSER`;
	- `TUNNEL_NETWORK`;
	- `PARSER_NAME`;
	- `CLOUDFLARED_NAME`;
	- `IMAGE_NAME`;
	- `PARSER_RUNTIME_MODE`;
	- `VITE_PORT`;
	- `LOCAL_CONVEX_CLOUD_PORT`;
	- `LOCAL_CONVEX_SITE_PORT`;
	- `LOCAL_CONVEX_STARTUP_TIMEOUT`;
	- `LOCAL_CONVEX_SYNC_SECRETS`;
	- `CACHE_DIR`;
	- `DOCKER_STATE_DIR`;
	- `CLOUDFLARED_IMAGE`;
	- `LOG_LEVEL`;
	- `RUN_ENV`;
	- `STOP_TIMEOUT_SECONDS`.
	Variables a ne pas mettre dans un fichier properties versionné :
	- `TUNNEL_TOKEN`;
	- `MISTRAL_API_KEY`;
	- `OPENAI_API_KEY`;
	- `DEEPSEEK_API_KEY`;
	- `QWEN_API_KEY`;
	- `CF_ACCESS_CLIENT_SECRET`;
	- tout secret, token, mot de passe ou clé privée.
	Structure cible possible:
	```text
	config/
	run.defaults.properties # valeurs par défaut versionnées
	run.dev.properties # configuration dev non sensible
	run.staging.properties # configuration staging non sensible
	run.prod.properties # configuration prod non sensible
	run.local.properties # ignore git, overrides poste local
	```
	Ordre de priorité proposé :
	a. valeurs internes minimales du script;
	b. `config/run.defaults.properties`;
	c. `config/run.${RUN_ENV}.properties`;
	d. `config/run.local.properties`;
	e. variables d'environnement déjà exportées;
	f. options CLI.
	Cette priorité permet de garder une valeur par défaut, de la surcharger par environnement, puis de laisser l'opérateur surcharger temporairement via le shell ou la ligne de commande.
	Etapes proposées:
	1. Créer une fonction `load_properties FILE`.
	2. Accepter uniquement les lignes `KEY=value` simples.
	3. Ignorer les lignes vides et les commentaires commençant par `#`.
	4. Refuser les noms de variables non autorises.
	5. Masquer les valeurs sensibles dans tout affichage.
	6. Ajouter `config-validate` pour vérifier les fichiers properties.
	7. Ajouter `config-print --redacted` pour voir la configuration finale.
	8. Documenter quelles variables appartiennent aux properties et quelles variables doivent rester dans un gestionnaire de secrets.
	9. En production, charger les secrets depuis l'environnement d'exécution ou un secret manager, pas depuis le fichier properties versionné.
	10. Ajouter un test qui prouve qu'une option CLI gagne bien sur une property.

### 13.3 Priorité basse

1. Ajouter une table de compatibilité des modes.
	Exemple:

| Mode         | Parser                 | Convex    | Vite | Tunnel | Usage                   |
| ------------ | ---------------------- | --------- | ---- | ------ | ----------------------- |
| `local-fast` | local workspace reload | local     | oui  | non    | dev rapide              |
| `local`      | local image            | cloud/env | oui  | non    | validation parser local |
| `tunnel`     | local image + edge     | cloud/env | oui  | oui    | validation stable       |
| `parser-dev` | local workspace reload | non       | non  | non    | hacking parser          |

2. Ajouter des codes de sortie documentés.
	Exemple:
	- `0`: succès;
	- `1`: erreur runtime;
	- `2`: mauvaise option utilisateur;
	- `130`: interruption utilisateur.
	Etapes proposées:
	1. Définir une table officielle des codes.
	2. Remplacer les `exit 1` génériques par des constantes lisibles.
	3. Documenter les codes dans `help`.
	4. Ajouter ces codes dans les logs d'erreur.
	5. Utiliser ces codes dans les jobs CI/CD.

3. Ajouter une section `help` plus compacte et une option `help <commande>`.
	La commande `help` actuelle est utile mais longue. Une aide par commande serait plus accessible.
	Etapes proposées :
	1. Garder `./run.sh help` comme vue générale.
	2. Ajouter `./run.sh help local-fast`.
	3. Ajouter `./run.sh help prod`.
	4. Ajouter pour chaque commande: objectif, préconditions, effets de bord, exemples, logs à consulter.
	5. Afficher les commandes dangereuses dans une section séparée.

## 14. Idempotence: tests avant et après les actions

L'idempotence signifie qu'une commande peut être relancée plusieurs fois et aboutir au même état final sans casser ce qui existe déjà.

Exemple simple:
- lancer `./run.sh status` dix fois ne doit rien modifier;
- lancer `./run.sh up` deux fois doit détecter que les services sont déjà dans le bon état;
- lancer `./run.sh down` deux fois doit réussir, même si tout est déjà arrêté.

Le script possède déjà quelques éléments idempotents:
- `docker network create ... || true` ne casse pas si le réseau existe déjà;
- `handle_existing_stack_request` évite de relancer une pile identique;
- `build_runtime_image` évite un rebuild si la signature n'a pas changé;
- `remove_parser_container` boucle jusqu'à disparition du conteneur;
- certains stops ignorent les erreurs avec `|| true`.

Mais l'idempotence n'est pas encore formalisée comme contrat global.

### 14.1 Règle recommandée: précheck, action, postcheck

Chaque opération importante devrait suivre ce schéma :
1. Précheck : observer l'état actuel.
2. Décision: déterminer si une action est nécessaire.
3. Action: appliquer le changement seulement si nécessaire.
4. Postcheck: vérifier que l'état final attendu est atteint.
5. Log: expliquer ce qui a été fait ou pourquoi rien n'a été fait.

Exemple pour le parser:
```text
Précheck: le conteneur existe-t-il?

Précheck: son image correspond-elle a l'image attendue?

Précheck: son mode runtime est-il correct?

Decision: réutiliser, remplacer ou démarrer.

Action: démarrer ou remplacer si nécessaire.

Postcheck: /ready répond 200.

Postcheck: le conteneur porte le bon nom et expose le bon port.
```

### 14.2 Améliorations d'idempotence proposées

1. Formaliser une fonction `ensure_*` par ressource.
	Exemples:
	- `ensure_network`;
	- `ensure_runtime_image`;
	- `ensure_parser_running`;
	- `ensure_tunnel_running`;
	- `ensure_vite_running`;
	- `ensure_convex_running`;
	- `ensure_state_file`.
	Etapes:
	1. Pour chaque ressource, créer une fonction qui observe d'abord l'état.
	2. Si l'état est conforme, afficher `already ok` et retourner `0`.
	3. Si l'état est absent, créer la ressource.
	4. Si l'état est incompatible, remplacer uniquement la ressource concernée.
	5. Vérifier l'état final.
	6. Retourner une erreur claire si le postcheck échoue.

2. Rendre `down` totalement idempotent.
	Etapes:
	1. Si le fichier d'état est absent, afficher `nothing to stop`.
	2. Pour chaque PID lu, vérifier qu'il existe encore.
	3. Si le PID n'existe plus, ne pas échouer.
	4. Pour chaque conteneur, vérifier son existence avant stop.
	5. Supprimer le fichier d'état seulement après les stops.
	6. Relancer `down` doit retourner `0`.

3. Rendre `reset` plus controlé.
	Etapes:
	1. Ajouter un précheck qui liste ce que `reset` va supprimer ou tuer.
	2. En mode interactif, demander confirmation.
	3. En CI ou production, exiger `--yes` ou `--confirm-maintenance`.
	4. Tuer seulement les ressources appartenant au projet.
	5. Produire un résumé final: supprimé, déjà absent, échec.

4. Ajouter des postchecks après chaque démarrage.
	Etapes:
	1. Apres Docker parser: vérifier `/ready`, nom du conteneur, image, port.
	2. Apres Convex: vérifier `/instance_name` et URL attendue.
	3. Apres Vite: vérifier que le PID existe et que le port répond.
	4. Apres tunnel: vérifier que le conteneur tourne et que l'edge `/ready` répond si accessible.
	5. Apres `reload-env`: vérifier que les nouveaux hashes sont écrits dans l'état.

5. Ajouter des tests automatisés d'idempotence.
	Tests minimum recommandés:
	```text
	Test 1: ./run.sh help retourne 0 et ne crée pas d'état.
	Test 2: ./run.sh down retourne 0 si rien n'est lancé.
	Test 3: ./run.sh down peut être lancé deux fois.
	Test 4: ./run.sh status retourne 0 même si aucun service ne tourne.
	Test 5: ./run.sh up --dry-run ne modifie pas tmp/dev-stack.
	Test 6: ./run.sh config-validate échoue si une property inconnue est présente.
	Test 7: ./run.sh local-fast --dry-run affiche les actions attendues sans démarrer Docker.
	```
	Tests avec services réels, à exécuter dans un environnement d'intégration:
	```text
	Test 8: ./run.sh up --local-origin lance le parser puis /ready répond 200.
	Test 9: relancer la même commande ne recrée pas inutilement le conteneur.
	Test 10: ./run.sh reload-env sans changement ne redémarre rien.
	Test 11: modifier une variable d'env provoque seulement le redémarrage attendu.
	Test 12: ./run.sh down arrête la pile.
	Test 13: relancer ./run.sh down retourne encore 0.
	```

6. Ajouter un mode de comparaison d'état avant/après.
	Etapes :
	1. Capturer l'état avant action: conteneurs, PID, ports, hashes de config.
	2. Exécuter l'action.
	3. Capturer l'état après action.
	4. Afficher les différences utiles.
	5. En mode test, échouer si une différence non attendue apparait.

7. Distinguer les commandes read-only des commandes mutantes.
	Commandes read-only attendues:
	- `help`;
	- `status`;
	- `logs`;
	- `smoke`;
	- `probe-edge` sauf POST de fichier.
	Commandes mutantes:
	- `up`;
	- `local-fast`;
	- `local`;
	- `tunnel`;
	- `parser-dev`;
	- `reload-env`;
	- `rebuild-docker`;
	- `down`;
	- `reset`;
	- `kill-vite-ports`.
	Etapes:
	1. Documenter cette classification dans `help`.
	2. Garantir que les commandes read-only n'écrivent pas dans `tmp/dev-stack`.
	3. Ajouter un test qui compare l'arborescence avant/après une commande read-only.
	4. En production, limiter les commandes mutantes autorisées.

## 15. Améliorer la production de logs

La production de logs peut être améliorée sans changer la logique métier du script.

### 15.1 Objectifs

Un bon système de logs doit permettre de répondre vite à ces questions:
- quelle commande a été lancée?
- quel mode est actif?
- quel service a échoué?
- quelle commande externe a été appelée?
- où lire les détails?
- quel fichier d'environnement a changé?
- quel PID ou conteneur a été démarré ou arrêté?

### 15.2 Recommandations concrètes

1. Centraliser les fonctions de logs.
	Créer des fonctions `log_info`, `log_warn`, `log_error`, `log_debug`, puis remplacer progressivement les `echo "[run] ..."` par ces fonctions.

2. Ajouter des timestamps.
	Format recommandé:
	```text
	2026-06-08T15:42:10+02:00 [run][INFO] starting parser
	```
	En Bash:
	```bash
	timestamp() { date '+%Y-%m-%dT%H:%M:%S%z'; }
	```

3. Ajouter un fichier de log principal.
	Par exemple:
	```text
	tmp/run-dev-stack.log
	```
	Il contiendrait les actions du script lui-même, distinctes des logs applicatifs Vite et Convex.

4. Conserver les logs des sous-services.
	Garder:
	- `tmp/vite-dev.log`;
	- `tmp/convex-dev.log`;
	- `docker logs` pour le parser.
	Mais ajouter dans le log principal les chemins et commandes utiles pour les consulter.

5. Ajouter une variable `LOG_LEVEL`.
	Exemple:
	```bash
	LOG_LEVEL=debug ./run.sh local-fast
	```
	Niveaux possibles:
	- `error`;
	- `warn`;
	- `info`;
	- `debug`.

6. Masquer les secrets.
	Toute valeur de variable contenant `KEY`, `SECRET`, `TOKEN`, `PASSWORD` ou `PRIVATE` doit être masquée dans les logs.
	Exemple:
	```text
	MISTRAL_API_KEY=***
	TUNNEL_TOKEN=***
	```

7. Ajouter un résumé d'échec.
	Quand un service échoue, afficher:
	- service concerné;
	- endpoint testé;
	- fichier de log à lire;
	- dernière ligne significative du log si disponible;
	- commande de récupération possible.
	Exemple:
	```text
	[run][ERROR] local Convex did not become reachable
	[run][ERROR] checked: http://127.0.0.1:3210/instance_name
	[run][ERROR] log: tmp/convex-dev.log
	[run][ERROR] try: ./run.sh reset
	```

8. Ajouter une commande `logs <service>`.
	Exemples:
	```bash
	./run.sh logs parser
	./run.sh logs vite
	./run.sh logs convex
	./run.sh logs all
	```
	La commande actuelle `logs` ne couvre que le parser Docker.

## 16. Améliorer les commentaires

Le script contient déjà quelques commentaires utiles, notamment pour les grandes sections et certains comportements Convex. L'amélioration principale n'est pas d'ajouter beaucoup de commentaires, mais d'ajouter les bons commentaires aux endroits où le comportement est surprenant.

### 16.1 Règles recommandées

1. Commenter l'intention, pas la syntaxe.
	Mauvais commentaire:
	```bash
	# Set variable to 1
	START_UI=1
	```
	Bon commentaire:
	```bash
	# local-fast doit lancer l'UI pour reproduire le flux complet parser + Convex + frontend.
	START_UI=1
	```

2. Commenter les décisions dangereuses.
	Les zones à commenter davantage:
	- pourquoi tuer les ports `5173-5215`;
	- pourquoi `reset` supprime certains logs;
	- pourquoi `workspace` n'est pas la validation runtime stable;
	- pourquoi certaines variables Convex sont unset avant démarrage;
	- pourquoi `STRUCTURED_UPLOAD_SKIP_HEALTHCHECK=1` est défini côté Vite;
	- pourquoi le parser démarre même quand le frontend pointe vers l'edge.

3. Ajouter un commentaire d'en-tête par grande fonction complexe.
	Fonctions candidates:
	- `build_runtime_image`;
	- `handle_existing_stack_request`;
	- `resolve_convex_project_binding`;
	- `start_convex`;
	- `sync_local_convex_env`;
	- `reload_env_stack`;
	- `rebuild_docker_stack`.

4. Documenter les effets de bord.
	Chaque fonction qui tue, supprime, reconstruit ou modifie l'état devrait annoncer ses effets principaux en commentaire court.
	Exemple:
	```bash
	# Effets de bord: supprime le fichier d'état, efface les logs temporaires et vide CONVEX_TMPDIR.
	clear_dev_state() { ... }
	```

5. Ajouter un bloc "contrat" en haut du script.
	Ce bloc pourrait indiquer:
	- dépendances nécessaires;
	- fichiers lus;
	- fichiers écrits;
	- ports utilisés;
	- conteneurs créés;
	- commandes destructives potentielles;
	- modes recommandés.
	Pour un novice, ce bloc vaut plus que des commentaires dispersés.


## 17. Conclusion

`run.sh` est un script actif et central pour le développement local. Il orchestre plusieurs services avec une interface unique et couvre déjà beaucoup de cas réels: parser Docker, Vite, Convex local, tunnel Cloudflare, reload d'environnement, rebuild Docker et nettoyage.

Les principaux axes d'amélioration ne sont pas une réécriture complète. Les gains les plus pragmatiques seraient:
1. rendre le chargement `.env` cohérent avec les fichiers surveillés;
2. rendre les actions de nettoyage moins brutales;
3. standardiser les logs;
4. ajouter une commande de diagnostic globale;
5. modulariser progressivement le script pour isoler configuration, état, logs, services et checks;
6. déplacer la configuration non sensible vers des fichiers de properties valides et documentés;
7. traiter les secrets à part, via l'environnement d'exécution ou un gestionnaire de secrets;
8. définir un contrat d'idempotence avec préchecks, actions conditionnelles et postchecks;
9. commenter les décisions d'orchestration qui ne sont pas évidentes pour un nouveau contributeur.

Pour aller vers une exploitation production, la priorité n'est donc pas d'ajouter plus de commandes. La priorité est de rendre les commandes existantes prévisibles, relançables, observables et limitées à des effets de bord clairement documentés.