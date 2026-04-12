---
title: "Cloudflare Zero Trust + Tunnel — Runbook parser.dasti.ai"
category: howto
tags: [cloudflare, zero-trust, tunnel, parser, devops, infrastructure, dasti]
created: 2026-04-12
updated: 2026-04-12
status: current
valid_from: 2026-04-12
valid_until:
superseded_by:
horizon: present
version: v1
sources: [howto-tunnel-2026-04-12]
related: [[tech/import-ocr-pipeline]], [[entities/cv-forge]]
---

# Cloudflare Zero Trust + Tunnel — Runbook `parser.dasti.ai`

Runbook opérationnel pour configurer et maintenir la protection Cloudflare Zero Trust + le tunnel cloudflared qui expose `parser.dasti.ai`.

---

## 0) Lancement local

```bash
cp .env.local.example .env.local   # remplir les valeurs
./run.sh up --ui
cd my-app && CONVEX_DEPLOYMENT=dev:neat-starfish-33 npx --yes convex run --push actions/_probeMistral:probe
./scripts/convex-logs-last-rid.sh
./scripts/convex-logs-rid.sh <RID>
```

## 0b) À quoi ressemble "tout va bien"

```bash
# Santé — doit retourner 200
curl --http1.1 -s -o /dev/null -w 'ready=%{http_code}\n' https://parser.dasti.ai/ready

# GET protégé sans token — doit retourner 403/405
curl --http1.1 -s -o /dev/null -w 'get=%{http_code}\n' https://parser.dasti.ai/mistral-ocr/parse

# POST avec service token — doit retourner 200
curl --http1.1 -s -o /dev/null -w 'post=%{http_code}\n' \
  -H 'Accept: application/json' -H 'Expect:' \
  -H 'CF-Access-Client-Id: <SERVICE_TOKEN_CLIENT_ID>.access' \
  -H 'CF-Access-Client-Secret: <SERVICE_TOKEN_CLIENT_SECRET>' \
  -F "file=@./fixtures/cv_png.pdf;type=application/pdf" \
  https://parser.dasti.ai/mistral-ocr/parse

# Prouver que le POST a atteint le connector
docker logs --since 120s cloudflared 2>&1 | grep -Ei ' /mistral-ocr/parse' || echo 'NO parse seen'
```

---

## 1) Cloudflare Zero Trust — deux Access Apps exactement

### A. Protected app (Service Auth)
- **Hostnames** : `parser.dasti.ai /mistral-ocr/` et `parser.dasti.ai /parse-cv`
- **Policies** : Service Auth → Include → Service Token `<votre token>`
- Pas de Bypass/Allow au-dessus. Pas de politiques supplémentaires.

### B. Health app (Bypass)
- **Hostname** : `parser.dasti.ai /ready`
- **Policies** : Bypass → Include → Everyone

> Les chemins doivent avoir un `/` initial.

---

## 2) Tunnel — routes publiées (ordre important)

| Ordre | Hostname | Path | Service |
|-------|----------|------|---------|
| 1 | `parser.dasti.ai` | `/ready` | `http_status:200` |
| 2 | `parser.dasti.ai` | `/*` | `http://cv-parser-service-dev:8001` |

Supprimer toute autre route `parser.dasti.ai` dans d'autres tunnels.

---

## 3) DNS

- **Managed by Tunnel** (recommandé) — CF gère automatiquement
- **CNAME manuel** : `CNAME proxied parser.dasti.ai → <TUNNEL_ID>.cfargotunnel.com`

---

## 4) Service Token

Un seul token (nommé `parser`). Donne : Client ID (`xxx.access`) + Client Secret (hex). Rotation si 403 persistants avec politiques correctes.

---

## 5) WAF Skip Rule (optionnel — si POST 502 sans atteindre le connector)

```
http.host eq "parser.dasti.ai" and starts_with(http.request.uri.path, "/mistral-ocr/")
```

Action : **Skip** → Managed rules + Rate limiting + Super Bot Fight Mode.

---

## 6) Connector cloudflared — un seul

```bash
docker ps --filter ancestor=cloudflare/cloudflared:latest -q | xargs -r docker rm -f
sudo pkill -f 'cloudflared.*tunnel.*run' || true

docker run -d --name cloudflared --restart=unless-stopped \
  --network parsernet cloudflare/cloudflared:latest \
  --loglevel debug tunnel --no-autoupdate run --protocol auto \
  --token "$TUNNEL_TOKEN"

sleep 2
docker logs --since 5s cloudflared 2>&1 | awk '/Updated to new configuration|Registered tunnel connection|Starting tunnel/{print}'
```

---

## 7) Variables Convex

```bash
npx convex env set CONVEX_PARSER_URL https://parser.dasti.ai
npx convex env set CF_ACCESS_CLIENT_ID  <CLIENT_ID>.access
npx convex env set CF_ACCESS_CLIENT_SECRET <CLIENT_SECRET>

./run.sh down || true && OPEN_BROWSER=0 ./run.sh up --ui
```

---

## 8) Troubleshooting

| Symptôme | Cause | Fix |
|----------|-------|-----|
| `ready=502`, rien dans les logs connector | Mauvais tunnel/DNS | Corriger routes tunnel ou token |
| `get=403` ou `get=405` | Normal — chemin protégé | Rien |
| `post=403` | Service token wrong ou ordre politiques wrong | Protected app → seule la politique Service Auth en premier ; rotation si besoin |
| `post=502`, rien dans les logs | Edge bloqué | Ajouter WAF Skip rule |
| POST OK en CLI mais UI échoue | UI ne transmet pas les headers CF | Corriger les env Convex (section 7) |

---

## Voir aussi

- [[tech/import-ocr-pipeline]] — chemin de code frontend → Convex → parser
