---
title: "ChatGPT MCP Private Beta Tunnel Connector Runbook"
category: howto
tags: [chatgpt-app, mcp, cloudflare, tunnel, oauth, private-beta]
created: 2026-07-04
updated: 2026-07-10
status: current
type: runbook
sources: [2026-07-04-pr304-live-mcp-connector-smoke-checkpoint, 2026-07-05-pr305-durable-mcp-connector-proof-checkpoint]
related: [[product/chatgpt-app-sdk-roadmap]]
---

# ChatGPT MCP Private Beta Tunnel Connector Runbook

Procedure reproductible pour demarrer le serveur MCP prive twoweeks, exposer son origine locale par le tunnel Cloudflare nomme, connecter ChatGPT avec un client OAuth confidentiel, puis prouver `tools/list` et un `tools/call` read-only.

## Etat verifie

- PR305 est mergee dans `application-os-foundation` par `f9dd477b116c48f1b223b17e1636876edf3c939f`.
- Endpoint MCP : `https://mcp.twoweeks.ai/mcp`.
- Redirect URI exact : `https://chatgpt.com/connector/oauth/b7v_6OncLEsg`.
- Client ID : `local-chatgpt-client`.
- Methode token : `client_secret_post` uniquement.
- Scope : `twoweeks:applications:read`.
- Connecteur final : `twoweeks-mcp-pr305-final-0710`, etat connecte.
- Les actions read-only `search` et `fetch` sont visibles.
- Un appel `search` read-only a termine avec succes dans ChatGPT, sans erreur de connexion ou reconnexion.
- Un diagnostic live anterieur a observe directement `POST /oauth/token` en `200`. La connexion du connecteur final prouve aussi l'echange token de facon comportementale, mais sa requete backend n'a pas ete capturee directement dans la trace navigateur finale.

Cette preuve est privee. Elle n'autorise ni lancement public, ni provider calls, ni write tools, ni refresh tokens, ni billing, ni expansion du cycle account-link, ni mutation de base production/shared.

## Configuration canonique

Le fichier serveur canonique est la racine `.env.local`, ignoree par Git et en mode `600`. Il contient les valeurs serveur suivantes sans les afficher dans les logs :

```dotenv
MCP_OAUTH_PRODUCTION_RUNTIME=1
MCP_OAUTH_PRODUCTION_APPROVED=1
MCP_OAUTH_PRODUCTION_ROUTE_WIRING=1
MCP_OAUTH_PRODUCTION_CLIENT_IDS=local-chatgpt-client
MCP_OAUTH_PRODUCTION_PRIVATE_BETA_ENABLED=1
MCP_OAUTH_PRODUCTION_PRIVATE_BETA_CLIENT_IDS=local-chatgpt-client
MCP_OAUTH_PRODUCTION_PRIVATE_BETA_RESOURCES=https://mcp.twoweeks.ai/mcp
MCP_OAUTH_PRODUCTION_RESOURCE=https://mcp.twoweeks.ai/mcp
MCP_OAUTH_PRODUCTION_AUTHORIZATION_ORIGIN=https://mcp.twoweeks.ai
MCP_OAUTH_PRODUCTION_REDIRECT_URIS=https://chatgpt.com/connector/oauth/b7v_6OncLEsg
MCP_OAUTH_PRODUCTION_ISSUER=<issuer-serveur>
MCP_OAUTH_PRODUCTION_PROVIDER_ENVIRONMENT=<environnement>
MCP_OAUTH_PRODUCTION_CLIENT_SECRET_SHA256=<sha256-minuscule-du-secret-brut>
CLERK_JWT_ISSUER_DOMAIN=<issuer-clerk>
CONVEX_URL=http://127.0.0.1:3210
CONVEX_AUTH_TOKEN=<admin-local>
MCP_PRIVATE_BETA_TUNNEL_CREDENTIALS_FILE=<chemin-absolu-du-fichier-credentials>
```

Regles :

- ne jamais mettre ces cles serveur dans `.env`, `my-app/.env` ou `my-app/.env.local`;
- `my-app/.env.local` reste reserve aux valeurs client `VITE_*`;
- `run.sh` derive en memoire la cle publique Clerk depuis l'issuer et ne l'affiche ni ne la persiste;
- le digest SHA-256 ne permet pas de retrouver le secret brut;
- tous les fichiers `.env*` restent exclus du contexte Docker;
- ne jamais stocker le secret brut, son digest ou un token de tunnel dans Git, le wiki, une PR ou des logs.

## Gestion du secret brut

Le secret brut doit exister a deux endroits seulement : le champ securise du connecteur ChatGPT et un gestionnaire de secrets personnel. Reference conseillee :

```text
service: twoweeks ChatGPT MCP OAuth
account: local-chatgpt-client
endpoint: https://mcp.twoweeks.ai/mcp
```

Ne jamais mettre la valeur dans le nom, les notes du wiki ou une commande shell. Si cette entree n'existe pas, le digest local ne permet aucune recuperation : generer un nouveau secret, remplacer son digest dans la racine `.env.local`, puis remplacer le champ securise du connecteur dans la meme rotation.

## Demarrage et controle

Depuis le repo app :

```bash
chmod 600 .env.local
./run.sh mcp-check
./run.sh mcp-private-beta
```

`mcp-check` doit afficher seulement `PASS` et les noms de cles en cas d'erreur, jamais leurs valeurs. `mcp-private-beta` demarre Convex local, Vite sur `127.0.0.1:5196`, le runtime parser image et le tunnel nomme.

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
origin: http://host.docker.internal:5196
```

`run.sh` monte le fichier de credentials du tunnel en lecture seule. Le tunnel transporte le trafic; les valeurs OAuth restent dans le processus Vite local, pas dans Workers, Pages ou le dashboard Cloudflare.

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

1. Creer un connecteur frais avec le meme couple secret brut/digest.
2. Terminer le login twoweeks/Clerk.
3. Verifier que ChatGPT affiche `Connecte`.
4. Actualiser les actions et verifier `search` et `fetch`.
5. Selectionner le connecteur dans un nouveau chat.
6. Demander un seul appel `search` read-only, sans mutation.
7. Verifier un succes explicite et l'absence d'erreur de reconnexion.

Ne pas documenter le resultat prive retourne par l'outil. Documenter uniquement la forme de preuve, les statuts et les noms de tools publics.

## Historique des blocages et diagnostic

| Symptome | Cause ou conclusion prouvee | Correction durable |
| --- | --- | --- |
| `invalid_authorization_request` | client, resource, scope ou redirect incoherent | utiliser les valeurs exactes ci-dessus; aucun wildcard |
| `pre_auth_create_failed` | dependance Convex locale/config runtime indisponible | demarrer la stack par `run.sh` et faire passer `mcp-check` |
| `owner_binding_failed` | retour Clerk incomplet ou session stale | correctifs login-return/StrictMode deja merges; cle Clerk derivee au demarrage |
| callback ChatGPT puis aucun `/oauth/token` | ancien client public `none` non viable sur ce chemin ChatGPT | client confidentiel avec secret et `client_secret_post` |
| metadata correcte mais secret rejete | secret ChatGPT et digest local ne correspondent pas, souvent apres rotation partielle | rotation atomique des deux cotes et connecteur frais |
| politique `invalidConfiguration` malgre des valeurs presentes | anciennes variables `MCP_PRODUCTION_PRIVATE_BETA_*` ou valeurs placees seulement dans l'env app | utiliser `MCP_OAUTH_PRODUCTION_PRIVATE_BETA_*` dans la racine `.env.local` |
| `Missing publishableKey` sur `/sign-in` | Vite n'a pas recu la cle Clerk publique | demarrer/recharger par `run.sh`, qui la derive en memoire depuis l'issuer |
| premier `tools/call` en `400`, puis retry en `200` | ChatGPT a reinitialise la session MCP | preuve finale valide, mais comportement a surveiller |

## Comportement fail-closed

- digest absent ou malforme : metadata reste `client_secret_post`, mais `/oauth/token` retourne `invalid_request` avant issuance;
- `client_secret_basic` : refuse;
- secret absent ou incorrect : `invalid_request` generique, sans echo;
- wildcard ou redirect malforme : configuration rejetee;
- `client_id`, redirect, resource, PKCE et authorization code restent verifies exactement;
- aucun refresh token n'est emis.

## Sources

- [[sources/2026-07-04-pr304-live-mcp-connector-smoke-checkpoint]]
- [[sources/2026-07-05-pr305-durable-mcp-connector-proof-checkpoint]]
- [[product/chatgpt-app-sdk-roadmap]]
