---
title: "ChatGPT MCP Private Beta Tunnel Connector Runbook"
category: howto
tags: [chatgpt-app, mcp, cloudflare, tunnel, oauth, private-beta]
created: 2026-07-04
updated: 2026-07-13
status: current
type: runbook
sources: [2026-07-13-pr313-pr317-mcp-private-beta-live-reproof-checkpoint, 2026-07-13-pr311-runsh-doctor-regression-closure-checkpoint, 2026-07-13-pr309-mcp-protocol-compatibility-checkpoint, 2026-07-12-pr308-mcp-private-beta-operational-smoke-checkpoint, 2026-07-12-pr307-runsh-collaborator-portability-checkpoint, 2026-07-05-pr305-durable-mcp-connector-proof-checkpoint, 2026-07-04-pr304-live-mcp-connector-smoke-checkpoint]
related: [[product/chatgpt-app-sdk-roadmap]]
---

# ChatGPT MCP Private Beta Tunnel Connector Runbook

Procedure reproductible pour demarrer le serveur MCP prive twoweeks, exposer son origine locale par le tunnel Cloudflare nomme, connecter ChatGPT avec un client OAuth confidentiel, puis prouver `tools/list` et un `tools/call` read-only.

## Etat verifie

- PR305 est mergee dans `application-os-foundation` par `f9dd477b116c48f1b223b17e1636876edf3c939f`.
- PR306 est mergee par `23c2cca9c09ba22c522242305545390dbc1bbea1`; `mcp-secret-sync` reste value-silent sous `bash -x`.
- PR307 est mergee par `736c6193966006e91a7bbbad5ff4b60898dd45fb`; `run.sh doctor` couvre le demarrage collaborateur macOS/Linux/WSL2 sans elargir MCP/OAuth.
- PR308 est mergee par `b101a75a1b625f7b0f3a62f677f474b4a030bff6`; `run.sh mcp-smoke` verifie la frontiere publique sans charger de dotenv, secret, token ou donnee privee.
- PR309 est mergee par `b2090fd71e643120d2d695704536d1a45f690b57`; le serveur accepte exactement MCP `2025-06-18` et `2025-11-25` et negocie la version supportee demandee.
- PR311 est mergee par `c61c9945e33f9208f4e3cb28dfd9e48d6fcfae50`; `run.sh doctor` detecte les collisions de ports, refuse un daemon Docker distant, verifie WSL2/Docker Desktop et impose le port Vite valide.
- PR313 est mergee par `d091c066edceaa60ba4e92dd0e215a913aa1d2a3` depuis le head relu `894ee870c24433b3636f9cfe6841a29a694e085b`.
- PR314 est mergee par `ccbba0a4a655af942b21c8e9144c432df79cbb38` depuis le head relu `85b8b201f2cae99b09007013398d3c7983220b03`.
- PR315 est mergee par `14e5abcdc880ef9ed020fe34e3d5f586819381c4` depuis le head relu `8f58c4637b81e45c6d5d8dec75bd9a2b7ff142e3`.
- PR316 est mergee par `bbd96b5cbaa3f7a24908ed51b001183b62119001` depuis le head relu `0c63c234f004ac4fbd853eb6aebf328ebf6bc758`.
- PR317 est la cible courante, mergee par `0ddcfeccef1a0f803c12b227692b85e848e1561b` depuis le head relu `e18e74f40d0ceb9e90f56596374f713f5d6b756f`; elle garde la projection exacte de six tools sous test CI.
- Endpoint MCP : `https://mcp.twoweeks.ai/mcp`.
- Redirect URI exact : `https://chatgpt.com/connector/oauth/b7v_6OncLEsg`.
- Client ID : `local-chatgpt-client`.
- Methode token : `client_secret_post` uniquement.
- Scope : `twoweeks:applications:read`.
- Rotation du secret dans Infisical, synchronisation value-silent et nouveau connecteur `twoweeks-mcp-final-v2-0713` prouves.
- Le connecteur est connecte; les actions read-only `search` et `fetch` sont visibles.
- Des appels read-only `search` et `fetch` ont reussi sans mutation ni erreur de reconnexion.
- Un connecteur frais a affiche exactement six Actions et un appel `twoweeks.application_package.summarize` a reussi avec le resultat sur `no_data_available`, sans contenu prive capture.
- La preuve d'echange OAuth est directe au niveau stockage : le nombre d'enregistrements de token est passe de 7 a 8 pendant la connexion V2. Aucune valeur de token n'a ete capturee ou documentee.

Cette preuve est privee. Elle n'autorise ni lancement public, ni provider calls, ni write tools, ni refresh tokens, ni billing, ni expansion du cycle account-link, ni mutation de base production/shared.

## Configuration canonique

Le fichier serveur canonique est la racine `.env.local`, ignoree par Git et en mode `600`. Les valeurs serveur y sont chargees sans etre affichees dans les logs. Les cles de configuration pertinentes incluent :

```dotenv
MCP_OAUTH_PRODUCTION_RUNTIME=1
MCP_OAUTH_PRODUCTION_APPROVED=1
MCP_OAUTH_PRODUCTION_ROUTE_WIRING=1
MCP_OAUTH_PRODUCTION_CLIENT_IDS=local-chatgpt-client
MCP_OAUTH_PRODUCTION_PRIVATE_BETA_ENABLED=1
MCP_OAUTH_PRODUCTION_PRIVATE_BETA_CLIENT_IDS=local-chatgpt-client
MCP_OAUTH_PRODUCTION_PRIVATE_BETA_RESOURCES=https://mcp.twoweeks.ai/mcp
MCP_OAUTH_PRODUCTION_PRIVATE_BETA_SUBJECT_DIGESTS=<digests-sha256-minuscules-non-documentes>
MCP_OAUTH_PRODUCTION_RESOURCE=https://mcp.twoweeks.ai/mcp
MCP_OAUTH_PRODUCTION_AUTHORIZATION_ORIGIN=https://mcp.twoweeks.ai
MCP_OAUTH_PRODUCTION_REDIRECT_URIS=https://chatgpt.com/connector/oauth/b7v_6OncLEsg
MCP_OAUTH_PRODUCTION_ISSUER=<issuer-serveur>
MCP_OAUTH_PRODUCTION_PROVIDER_ENVIRONMENT=<environnement>
MCP_OAUTH_PRODUCTION_CLIENT_SECRET_SHA256=<digest-non-documente>
CLERK_JWT_ISSUER_DOMAIN=<issuer-clerk>
CONVEX_URL=http://127.0.0.1:3210
CONVEX_AUTH_TOKEN=<admin-local>
MCP_PRIVATE_BETA_TUNNEL_CREDENTIALS_FILE=<chemin-absolu-du-fichier-credentials>
```

Regles :

- la racine `.env.local` est la seule source canonique des cles serveur; ne pas les placer dans `.env`, `my-app/.env` ou `my-app/.env.local`;
- `my-app/.env.local` reste reserve aux valeurs client `VITE_*`;
- `run.sh` derive en memoire la cle publique Clerk depuis l'issuer et ne l'affiche ni ne la persiste;
- `MCP_OAUTH_PRODUCTION_PRIVATE_BETA_SUBJECT_DIGESTS` est la seule cle canonique d'eligibilite par sujet; ses valeurs sont des digests SHA-256 minuscules et la configuration legacy avec sujets bruts ne doit pas etre recommandee;
- le digest SHA-256 ne permet pas de retrouver le secret brut;
- tous les fichiers `.env*` restent exclus du contexte Docker;
- ne jamais stocker le secret brut, son digest ou un token de tunnel dans Git, le wiki, une PR ou des logs.

Etat du checkpoint : la migration de l'environnement private-beta vers la cle de digests est deployee et a ete re-prouvee avec le connecteur V2. Le `mcp-smoke` public reste une preuve distincte, sans credential.

## Source Infisical du secret

Le secret partage est gere dans Infisical EU Cloud :

```text
project: twoweeks
environment: dev
shared key: MCP_OAUTH_PRODUCTION_CLIENT_SECRET
```

Le fichier `.infisical.json` contient uniquement le binding non-secret du projet et de l'environnement; il ne contient aucune valeur de secret. Chaque collaborateur se connecte individuellement a Infisical avec son propre compte. Ne jamais mettre la valeur dans le wiki, une commande shell, un log, une PR ou un fichier de configuration suivi par Git.

La rotation one-shot PR305 a ete executee depuis la source Infisical et synchronisee vers la racine `.env.local` avec `./run.sh mcp-secret-sync`. Cette commande refuse un fichier qui n'est pas deja en mode `600`, ne persiste que le digest SHA-256 lors du remplacement atomique et n'imprime aucune valeur. PR306, mergee par `23c2cca9c09ba22c522242305545390dbc1bbea1`, suspend aussi `xtrace` avant le chargement des fichiers env et pendant la recuperation, le hachage et le remplacement atomique; elle restaure ensuite l'etat initial sur les sorties controlees. Ainsi, meme `bash -x ./run.sh mcp-secret-sync` ne doit afficher ni secret brut, ni ancien ou nouveau digest. Une rotation ulterieure doit remplacer la valeur Infisical et recreer le connecteur dans la meme operation controlee.

## Demarrage et controle

Depuis le repo app :

```bash
chmod 600 .env.local
./run.sh doctor mcp-private-beta
./run.sh mcp-check
./run.sh mcp-secret-sync
./run.sh mcp-private-beta
./run.sh mcp-smoke
```

`doctor mcp-private-beta` est un preflight read-only : il ne source pas les fichiers dotenv, ne recupere pas le secret Infisical et ne demarre ni n'arrete de service. Il doit finir en `PASS` avant le premier demarrage collaborateur. PR311 aligne ce diagnostic avec le demarrage reel pour les ports Convex/Vite/parser, le daemon Docker local, WSL2 et les variables Bash speciales. Vite utilise `--strictPort` et ne doit jamais migrer silencieusement vers un autre port. `mcp-check` doit afficher seulement `PASS` et les noms de cles en cas d'erreur, jamais leurs valeurs. `mcp-private-beta` demarre Convex local, Vite sur `127.0.0.1:5196`, le runtime parser image et le tunnel nomme. Une fois l'origine publique disponible, `mcp-smoke` verifie les metadata OAuth/MCP, le lifecycle `initialize`/`initialized`, le challenge Bearer et l'erreur token fail-closed; il ne source aucun dotenv et n'envoie aucun credential.

Le smoke credential-free frais apres PR317 est `PASS` pour les metadata, les metadata protected-resource, les deux versions MCP supportees, l'inventaire exact de six tools, `tools/call` non authentifie fail-closed et le token malforme fail-closed. La preuve authentifiee est separee : connexion V2, token-record count 7 vers 8, six tools listes et un appel read-only reussi.

Apres une modification de configuration :

```bash
./run.sh reload-env
```

Pour un stack `mcp-private-beta` suivi, `reload-env` rejoue d'abord `mcp-check`, recree la cle Clerk publique en memoire, puis seulement redemarre Vite si l'environnement a change.

Verifier les surfaces publiques :

```bash
curl -sS https://mcp.twoweeks.ai/.well-known/oauth-authorization-server
curl -sS https://mcp.twoweeks.ai/.well-known/oauth-protected-resource/mcp
```

Attendu : metadata `200`, `token_endpoint_auth_methods_supported` vaut exactement `client_secret_post`, et la ressource vaut exactement `https://mcp.twoweeks.ai/mcp`.

## Tunnel Cloudflare nomme

```text
name: neyssan-mcp-pr305-twoweeks-ai
id: 935a2064-9473-41bc-bd73-174660892847
hostname: mcp.twoweeks.ai
Docker Desktop / WSL2 origin: http://host.docker.internal:5196
native Linux Docker Engine origin: http://127.0.0.1:5196 through --network host
```

`run.sh` monte le fichier de credentials du tunnel en lecture seule. Sur Linux natif, cloudflared utilise le reseau hote pour joindre Vite qui reste lie a loopback; Docker Desktop et WSL2 utilisent `host.docker.internal`. Le tunnel transporte le trafic; les valeurs OAuth restent dans le processus Vite local, pas dans Workers, Pages ou le dashboard Cloudflare.

`Bot Fight Mode` et `AI Labyrinth` sont restes desactives apres la preuve. Cette session ne prouve pas qu'ils etaient la cause du blocage; utiliser un A/B separe avant toute reactivation sur ce hostname.

## Configuration ChatGPT

| Champ | Valeur |
| --- | --- |
| Connexion | URL du serveur |
| URL MCP | `https://mcp.twoweeks.ai/mcp` |
| Authentification | OAuth |
| Enregistrement client | Client OAuth defini par l'utilisateur |
| Client ID | `local-chatgpt-client` |
| Client secret | secret brut correspondant exactement au digest local |
| Methode token | `client_secret_post` |
| Scope par defaut | `twoweeks:applications:read` |
| Authorization URL | `https://mcp.twoweeks.ai/oauth/authorize` |
| Token URL | `https://mcp.twoweeks.ai/oauth/token` |
| Authorization server | `https://mcp.twoweeks.ai/` |
| Resource | `https://mcp.twoweeks.ai/mcp` |

Utiliser `URL du serveur`, pas `Tunnel`. L'identifiant OAuth n'est pas un email et le secret OAuth n'est pas le mot de passe du compte twoweeks. Le compte utilisateur est choisi plus tard par Clerk pendant le login.

Ne jamais utiliser de wildcard redirect. La seule URI autorisee pour cette preuve est la valeur complete et exacte indiquee plus haut.

## Preuve ChatGPT minimale

Cette preuve a ete rejouee apres la migration et le deploiement de `MCP_OAUTH_PRODUCTION_PRIVATE_BETA_SUBJECT_DIGESTS`. Le connecteur V2 a atteint l'etat connecte, l'echange token a ete observe sans valeur sensible, exactement six tools ont ete listes et un appel read-only a reussi.

1. Recuperer le secret partage depuis Infisical et creer un connecteur frais avec le secret correspondant au digest local, sans documenter la valeur.
2. Terminer le login twoweeks/Clerk.
3. Verifier que ChatGPT affiche `Connecte`.
4. Actualiser les actions et verifier exactement six actions, dont une seule `twoweeks.application_package.summarize`.
5. Selectionner le connecteur dans un nouveau chat.
6. Demander un appel `twoweeks.application_package.summarize` read-only, sans mutation.
7. Verifier un succes explicite et l'absence d'erreur de reconnexion.
8. Supprimer l'ancien connecteur apres rotation afin qu'il ne conserve pas le credential remplace.

Ne pas documenter le resultat prive retourne par l'outil. Documenter uniquement la forme de preuve, les statuts et les noms de tools publics.

## Historique des blocages et diagnostic

| Symptome | Cause ou conclusion prouvee | Correction durable |
| --- | --- | --- |
| `invalid_authorization_request` | client, resource, scope ou redirect incoherent | utiliser les valeurs exactes ci-dessus; aucun wildcard |
| `pre_auth_create_failed` | dependance Convex locale/config runtime indisponible | demarrer la stack par `run.sh` et faire passer `mcp-check` |
| `owner_binding_failed` | retour Clerk incomplet ou session stale | correctifs login-return/StrictMode deja merges; cle Clerk derivee au demarrage |
| callback ChatGPT puis aucun `/oauth/token` | ancien client public `none` non viable sur ce chemin ChatGPT | client confidentiel avec secret et `client_secret_post` |
| metadata correcte mais secret rejete | secret Infisical et digest local ne correspondent pas, souvent apres rotation partielle | resynchroniser par `run.sh mcp-secret-sync` et recreer le connecteur frais |
| politique `invalidConfiguration` malgre des valeurs presentes | anciennes variables `MCP_PRODUCTION_PRIVATE_BETA_*` ou valeurs placees seulement dans l'env app | utiliser `MCP_OAUTH_PRODUCTION_PRIVATE_BETA_*` dans la racine `.env.local` |
| `Missing publishableKey` sur `/sign-in` | Vite n'a pas recu la cle Clerk publique | demarrer/recharger par `run.sh`, qui la derive en memoire depuis l'issuer |
| premier `tools/call` en `400`, puis retry en `200` | ChatGPT a reinitialise la session MCP | preuve finale valide, mais comportement a surveiller |
| connecteur OAuth valide mais Actions indisponibles | ChatGPT initialise avec MCP `2025-06-18`, anciennement refuse par le serveur limite a `2025-11-25` | PR309 accepte exactement les deux versions et negocie celle demandee |

## Comportement fail-closed

- liste de digests de sujets absente, malformee ou sans correspondance : eligibilite private-beta refusee;
- digest absent ou malforme : metadata reste `client_secret_post`, mais `/oauth/token` retourne `invalid_request` avant issuance;
- `client_secret_basic` : refuse;
- secret absent ou incorrect : `invalid_request` generique, sans echo;
- wildcard ou redirect malforme : configuration rejetee;
- `client_id`, redirect, resource, PKCE et authorization code restent verifies exactement;
- aucun refresh token n'est emis.

## Sources

- [[sources/2026-07-13-pr313-pr317-mcp-private-beta-live-reproof-checkpoint]]
- [[sources/2026-07-13-pr311-runsh-doctor-regression-closure-checkpoint]]
- [[sources/2026-07-13-pr309-mcp-protocol-compatibility-checkpoint]]
- [[sources/2026-07-12-pr307-runsh-collaborator-portability-checkpoint]]
- [[sources/2026-07-04-pr304-live-mcp-connector-smoke-checkpoint]]
- [[sources/2026-07-05-pr305-durable-mcp-connector-proof-checkpoint]]
- [[product/chatgpt-app-sdk-roadmap]]
