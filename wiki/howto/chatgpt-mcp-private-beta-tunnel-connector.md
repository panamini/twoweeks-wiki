---
title: "ChatGPT MCP Private Beta Tunnel Connector Runbook"
category: howto
tags: [chatgpt-app, mcp, cloudflare, tunnel, oauth, private-beta]
created: 2026-07-04
updated: 2026-07-06
status: current
type: runbook
sources: [2026-07-04-pr304-live-mcp-connector-smoke-checkpoint, 2026-07-05-pr305-durable-mcp-connector-proof-checkpoint]
related: [[product/chatgpt-app-sdk-roadmap]]
---

# ChatGPT MCP Private Beta Tunnel Connector Runbook

Runbook manuel pour exposer l'app locale twoweeks via un tunnel Cloudflare quick tunnel, creer un connecteur ChatGPT prive, connecter OAuth/Clerk, puis verifier que ChatGPT appelle le serveur MCP local avec des donnees read-only reelles.

## Etat actuel

Le smoke PR304 a utilise un tunnel ephemere Cloudflare vers Vite local, puis un connecteur ChatGPT prive. Le tunnel cree pendant la preuve etait :

```text
https://are-effort-skirts-hints.trycloudflare.com
```

Ce domaine `trycloudflare.com` est temporaire. Il ne doit pas etre hardcode comme URL stable. Il sert seulement a prouver la frontiere locale/private-beta.

PR305 ajoute une preuve durable limitee avec un tunnel nomme Cloudflare :

```text
https://mcp.twoweeks.ai/mcp
```

Tunnel PR305 :

```text
name: neyssan-mcp-pr305-twoweeks-ai
id: 935a2064-9473-41bc-bd73-174660892847
hostname: mcp.twoweeks.ai
origin local: http://127.0.0.1:5187
```

Etat PR305 : la preuve route/OAuth/token/MCP/read-side directe passe par `mcp.twoweeks.ai`. Le blocage local Clerk `VITE_CLERK_PUBLISHABLE_KEY` a ete corrige pendant la reprise du 2026-07-06. Un second blocage local, cause par un cookie Clerk `__session` stale sur `/oauth/continue`, a ete corrige cote app par `fb17e6cc6171f3e54baa805c39eb5e34728f5b0a` sans elargir le comportement runtime.

Dernier point de preuve ChatGPT UI : le navigateur a fini la connexion twoweeks, la continuation OAuth a renvoye ChatGPT vers son callback avec les cles de requete attendues `code` et `state`, puis ChatGPT a affiche une erreur generique de connexion. Aucun appel `/oauth/token` n'a atteint `mcp.twoweeks.ai` pendant cette tentative. Classer ce point comme `BLOCKED_CHATGPT_UI` / callback ChatGPT avant echange token, pas comme une action manuelle restante dans la configuration du connecteur.

## Pre-requis

- Avoir le checkout twoweeks/neyssan contenant le patch PR304, ou une branche equivalente basee sur `application-os-foundation` apres PR303.
- Avoir les dependances locales deja installees. Ne pas lancer d'installation pendant une preuve si le contrat l'interdit.
- Avoir Convex local demarre sur `127.0.0.1:3210`.
- Avoir Vite local demarre sur un port connu. La preuve PR304 a utilise `http://localhost:5187`.
- Avoir `cloudflared` disponible localement.
- Avoir un compte ChatGPT qui peut creer un connecteur prive / private beta.
- Avoir un compte twoweeks/Clerk valide. Si le compte twoweeks utilise Google, il faut se connecter avec Google ; ne pas inventer un mot de passe twoweeks.
- Avoir `VITE_CLERK_PUBLISHABLE_KEY` disponible dans l'environnement Vite local. Sans cette cle publique, `/sign-in` affiche l'erreur Clerk `Missing publishableKey` et le flux OAuth ChatGPT ne peut pas finir.

## 1. Demarrer la stack locale

Dans le repo app, utiliser le workflow local existant du projet pour demarrer Convex et Vite. La preuve PR304 attendait :

```text
Convex local: http://127.0.0.1:3210
Vite local:   http://localhost:5187
```

Verifier que Vite sert l'app avant de creer le tunnel.

## 2. Creer le tunnel Cloudflare

Lancer un quick tunnel depuis la machine locale :

```bash
cloudflared tunnel --config /dev/null --no-autoupdate --loglevel info --protocol http2 --url http://localhost:5187
```

Pourquoi `--config /dev/null` est important : sur la machine de preuve, le fichier `~/.cloudflared/config.yml` local redirigeait les quick tunnels vers `http_status:404`. En forcant une config vide, le tunnel pointe vraiment vers Vite.

Copier l'URL `https://...trycloudflare.com` affichee par `cloudflared`. Dans la preuve PR304, l'URL etait :

```text
https://are-effort-skirts-hints.trycloudflare.com
```

Pour un nouveau run, remplacer partout cette URL par la nouvelle URL generee.

### Variante PR305 : tunnel nomme durable

Si le tunnel nomme PR305 existe deja, utiliser une config explicite pour eviter que `cloudflared` charge le vieux `~/.cloudflared/config.yml` du parser :

```yaml
tunnel: 935a2064-9473-41bc-bd73-174660892847
credentials-file: /Users/pana/.cloudflared/935a2064-9473-41bc-bd73-174660892847.json
ingress:
  - hostname: mcp.twoweeks.ai
    service: http://127.0.0.1:5187
  - service: http_status:404
```

Puis lancer :

```bash
cloudflared tunnel --config /tmp/pr305-cloudflared.yml run
```

Verifier ensuite :

```bash
curl -sS https://mcp.twoweeks.ai/.well-known/oauth-protected-resource/mcp
```

Le champ `resource` doit valoir `https://mcp.twoweeks.ai/mcp`.

## 3. Verifier les routes depuis le tunnel

Definir la variable locale :

```bash
BASE="https://<votre-sous-domaine>.trycloudflare.com"
```

Verifier les metadonnees OAuth/MCP :

```bash
curl -sS "$BASE/.well-known/oauth-protected-resource/mcp"
curl -sS "$BASE/.well-known/oauth-authorization-server"
```

Verifier `tools/list` avec un token local de preuve seulement si le script de smoke du repo le fournit. Ne jamais coller de secret reel dans le terminal ou dans le wiki.

Un `GET /mcp` qui retourne `unsupported_method` est normal : MCP attend un `POST` JSON-RPC, pas un GET navigateur.

## 4. Creer le connecteur dans ChatGPT

Ouvrir ChatGPT avec le compte qui possede l'acces aux connecteurs. Aller dans l'interface de creation de connecteur / app privee.

Creer un nouveau connecteur avec ces valeurs :

| Champ | Valeur |
| --- | --- |
| Nom | `twoweeks-mcp-pr304-<timestamp>` |
| URL MCP | `https://<votre-sous-domaine>.trycloudflare.com/mcp` |
| Auth | Mixte / OAuth |
| Client registration | User-defined / manuel |
| Client ID | `local-chatgpt-client` |
| Client secret | vide |
| Token endpoint auth | `none` |
| Scope par defaut | `twoweeks:applications:read` |
| Authorization URL | `https://<votre-sous-domaine>.trycloudflare.com/oauth/authorize` |
| Token URL | `https://<votre-sous-domaine>.trycloudflare.com/oauth/token` |
| Resource | `https://<votre-sous-domaine>.trycloudflare.com/mcp` |

Pour PR305 durable, remplacer toutes les valeurs `https://<votre-sous-domaine>.trycloudflare.com` par `https://mcp.twoweeks.ai`.

Le redirect URI ChatGPT observe pendant PR305 utilise la forme :

```text
https://chatgpt.com/connector/oauth/<id-runtime>
```

La config locale doit autoriser l'URI concrete et complete generee par ChatGPT, pas un wildcard. PR96.1 canonicalise les redirect URIs puis fait une comparaison exacte; une entree comme `https://chatgpt.com/connector/oauth/*` reste invalide et fail-closed. Copier donc l'URL exacte affichee par ChatGPT, par exemple la valeur complete qui remplace `<id-runtime>`.

`https://chatgpt.com/connector_platform_oauth_redirect` seul ne suffit pas pour le flux UI courant si ChatGPT envoie une URI concrete `https://chatgpt.com/connector/oauth/<id-runtime>`.

Attention au remplissage automatique du navigateur : Chrome peut remplir l'email dans `Client ID` et un mot de passe dans `Client secret`. Il faut les effacer. Le client ID attendu pour cette preuve est `local-chatgpt-client`, et le client secret doit rester vide.

## 5. Connecter OAuth

Cliquer sur connecter le connecteur dans ChatGPT. ChatGPT ouvre la route OAuth twoweeks.

Si twoweeks demande une connexion, utiliser la methode normale du compte :

- si le compte twoweeks utilise Google, cliquer Google ;
- si Google demande un code, un telephone, ou une validation, la personne doit le faire manuellement ;
- ne pas mettre le mot de passe Google dans la configuration OAuth du connecteur.

La continuation doit revenir vers ChatGPT avec un code OAuth, puis ChatGPT doit pouvoir appeler MCP.

## 6. Smoke ChatGPT attendu

Dans ChatGPT, demander un appel au tool :

```text
twoweeks.application_package.summarize
```

Avec les arguments :

```json
{
  "applicationPackageRef": {
    "id": "mcp-safe-ref:application-package:latest"
  }
}
```

Resultat attendu si Stage 3 a bien materialise des donnees read-side :

```text
status: available
count: 1
result: real_data
```

Si le resultat est `no_data_available`, le connecteur peut etre correct mais les donnees read-side ne sont pas materialisees pour cet utilisateur. Refaire une sauvegarde de proposition liee a un job/profile valide, puis relancer le smoke.

## 7. Depannage

| Symptome | Cause probable | Correction |
| --- | --- | --- |
| Le navigateur affiche `unsupported_method` sur `/mcp` | Normal : GET navigateur au lieu de POST JSON-RPC | Tester avec ChatGPT ou le harness MCP, pas avec un simple GET |
| Le tunnel retourne 404 | `cloudflared` a charge une ancienne config locale | Relancer avec `--config /dev/null` |
| ChatGPT refuse le connecteur ou voit 403/404 | L'URL ne pointe pas vers Vite ou le tunnel est mort | Refaire un quick tunnel et mettre a jour l'URL MCP |
| `client_id` vaut un email | Autofill navigateur dans le champ OAuth | Recreer ou corriger le connecteur avec `local-chatgpt-client` |
| Un mot de passe est dans `Client secret` | Autofill navigateur | Vider le champ secret et mettre token endpoint auth a `none` |
| Login twoweeks demande un mot de passe inconnu | Le compte utilise Google/Clerk | Utiliser le bouton Google, pas un mot de passe invente |
| `/sign-in` affiche `Missing publishableKey` | `VITE_CLERK_PUBLISHABLE_KEY` absent de l'env Vite | Charger la cle publique Clerk locale avant de relancer Vite |
| `/oauth/authorize` renvoie `invalid_authorization_request` avec ChatGPT | Redirect URI ChatGPT courant non allowliste | Ajouter l'URI concrete complete envoyee par ChatGPT a `MCP_OAUTH_PRODUCTION_REDIRECT_URIS`; ne pas utiliser `https://chatgpt.com/connector/oauth/*`, car PR96.1 compare exactement les URIs canonicalisees |
| Tunnel nomme connecte mais `mcp.twoweeks.ai` retourne 404 | `cloudflared` a charge la config globale parser | Relancer avec `--config /tmp/pr305-cloudflared.yml` pointant vers le credential PR305 |
| `/oauth/continue` renvoie `owner_binding_failed` alors que l'utilisateur est signe | Cookie Clerk `__session` stale ou mauvais jeton de session lu avant le bridge React | Utiliser le patch app `fb17e6cc6171f3e54baa805c39eb5e34728f5b0a` ou equivalent : les documents navigateur `/oauth/continue` passent par le bridge React et les fetchs `owner_binding_failed` retentent avec un bearer Clerk |
| ChatGPT affiche une erreur generique apres que l'onglet twoweeks s'est connecte puis ferme | ChatGPT a recu le callback OAuth mais a abandonne avant d'appeler `/oauth/token` | Ne pas recreer en boucle le connecteur. Conserver les preuves safe : callback avec cles `code,state`, absence d'appel `/oauth/token`, nom du connecteur, URL MCP. Demander les logs cote ChatGPT/OpenAI; classer `BLOCKED_CHATGPT_UI` tant que le token endpoint n'est jamais appele |
| Le bouton ChatGPT `Connecter` ne lance aucun nouvel onglet OAuth | Etat UI/navigateur ChatGPT bloque ou onglets `/oauth/continue` perimes | Fermer les anciens onglets `mcp.twoweeks.ai/oauth/continue`, rouvrir les reglages ChatGPT Applications dans une session propre, puis relancer le connecteur; ne pas classer cela comme un probleme Clerk si `/sign-in` rend deja l'app connectee |
| `invalid_continuation_request` avec nonce/intention | Code avant PR304 ou URL OAuth mal conservee | Appliquer PR304 et recreer le connecteur |
| `Invalid tools/call metadata` | Code avant PR304 rejetant `_meta` ChatGPT | Appliquer PR304 |
| `-32602` sur tool call | Arguments invalides ou safe-ref mal copiee | Utiliser exactement `mcp-safe-ref:application-package:latest` |
| `no_data_available` | Pas de package Stage 3 materialise pour cet owner | Sauvegarder une proposition valide puis retester |

## 8. Frontieres de securite

Cette procedure ne doit pas ouvrir :

- lancement public ;
- appels provider ;
- actions write ;
- refresh tokens ;
- billing ;
- expansion du cycle account-link ;
- mutation de base de donnees production/shared ;
- logs contenant secrets, texte CV/proposition/job brut, provider output, prompts, ou fichiers.

## 9. Nettoyage

Quand la preuve est terminee :

1. Arreter `cloudflared`.
2. Arreter Vite si le serveur local n'est plus necessaire.
3. Supprimer ou ignorer les connecteurs ChatGPT temporaires mal configures.
4. Garder uniquement le connecteur qui pointe vers le tunnel actif du moment.

## Sources

- [[sources/2026-07-04-pr304-live-mcp-connector-smoke-checkpoint]]
- [[sources/2026-07-05-pr305-durable-mcp-connector-proof-checkpoint]]
- [[product/chatgpt-app-sdk-roadmap]]
