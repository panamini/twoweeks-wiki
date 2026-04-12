# dasti.ai - how to

# 1. Lancement de l’application en local

1. Copy .env.local.example → .env.local and fill values (or put Mistral key in ~/.mistral_key).
2. Launch everything: ./run.sh up --ui
3. Probe server: cd my-app && CONVEX_DEPLOYMENT=dev:neat-starfish-33 npx --yes convex run --push actions/_probeMistral:probe
4. Grab last RID: ./scripts/convex-logs-last-rid.sh
5. Print slice: ./scripts/convex-logs-rid.sh <RID>

# parser.dasti.ai — Zero Trust + Tunnel + Convex runbook

## 0) What “good” looks like

Edge checks (from your laptop/CI):

```bash
# public health
curl --http1.1 -s -o /dev/null -w 'ready=%{http_code}\n' https://parser.dasti.ai/ready
# → 200

# protected GET (no token)
curl --http1.1 -s -o /dev/null -w 'get=%{http_code}\n' https://parser.dasti.ai/mistral-ocr/parse
# → 403 (or 405 if origin answers GET with 405; either is fine)

# protected POST (with service token)
curl --http1.1 -s -o /dev/null -w 'post=%{http_code}\n' \
  -H 'Accept: application/json' -H 'Expect:' \
  -H 'CF-Access-Client-Id: <SERVICE_TOKEN_CLIENT_ID>.access' \
  -H 'CF-Access-Client-Secret: <SERVICE_TOKEN_CLIENT_SECRET>' \
  -F "file=@./fixtures/cv_png.pdf;type=application/pdf" \
  https://parser.dasti.ai/mistral-ocr/parse
# → 200

```

Connector log should **show the POST**:

```bash
docker logs --since 120s cloudflared 2>&1 | grep -Ei ' /mistral-ocr/parse' || echo 'NO parse seen'

```

---

## 1) Cloudflare Zero Trust — Access apps (exactly two)

**Access → Applications**

Create/keep only these two for `parser.dasti.ai`. Delete/disable any other app that mentions this hostname/wildcards.

### A. Protected app (Service Auth)

- **Public hostnames (rows):**
    - `parser.dasti.ai` **/mistral-ocr/**
    - `parser.dasti.ai` **/parse-cv**
- **Policies (order matters):**
    1. **Service Auth** → Include → **Service Token** = `<your service token>`
        - No Bypass/Allow above it. No extra policies.
- Save.

### B. Health app (Bypass)

- **Public hostnames (row):**
    - `parser.dasti.ai` **/ready**
- **Policies:**
    1. **Bypass** → Include → **Everyone**
- Save.

> Tip: paths must have a leading slash.
> 

---

## 2) Cloudflare Tunnel — Published routes (single “good” tunnel)

**Zero Trust → Networks → Tunnels → `<your good tunnel>` → Published application routes**

Keep only these two rows (in this order):

1. `parser.dasti.ai` **/ready** → **`http_status:200`**
2. `parser.dasti.ai` */ → `http://cv-parser-service-dev:8001`*

Delete any other `parser.dasti.ai` routes in **other** tunnels so all traffic goes to this one.

You should see the connector log pull this config line after start:

```
Updated to new configuration … "path":"/ready","service":"http_status:200"}, {"path":"/*","service":"http://cv-parser-service-dev:8001"}

```

---

## 3) DNS for `parser.dasti.ai`

Two valid patterns — use **one**:

- **Managed by Tunnel**: when you created the route in the tunnel UI with “Manage DNS” enabled, CF auto-manages DNS (you’ll usually see A/AAAA on the hostname, proxied).
- **Manual CNAME** (if needed):
    
    Add **proxied** `CNAME parser.dasti.ai → <TUNNEL_ID>.cfargotunnel.com`
    

Do **not** keep duplicates (no second CNAME/A/AAAA with the same name from another tunnel/app).

---

## 4) Service Token (Access)

Create **one** service token (name it `parser`).

- You’ll get:
    - **Client ID**: looks like `xxxxxxxxxxxxxxx.access`
    - **Client Secret**: long hex
- These power the protected POSTs. Rotate if you ever get 403s and you’re sure policies are correct.

---

## 5) Optional WAF tweak (only if multipart POST ever gets blocked)

If you see POST 502 at the edge **without** hitting the connector, add **one** narrow Skip rule:

**Security → WAF → Custom Rules → “parserskip”**

Expression (choose **one**):

- By **path** (recommended):
    
    ```
    http.host eq "parser.dasti.ai" and starts_with(http.request.uri.path, "/mistral-ocr/")
    
    ```
    
- Or by **content-type**:
    
    ```
    http.host eq "parser.dasti.ai" and
    starts_with(lower(http.request.headers["content-type"][0]), "multipart/form-data")
    
    ```
    

Action: **Skip** → check **Managed rules**, **Rate limiting**, **Super Bot Fight Mode**, **remaining custom rules**.

Place near the top. Keep it narrow to our host/path only.

> If your current setup works without this, you can skip adding it. It’s a guardrail for Cloudflare products that sometimes block large multipart uploads.
> 

---

## 6) Connector (cloudflared) — run exactly one

We run **one** Docker connector on the `parsernet` network.

```bash
# kill any old ones (docker + host)
docker ps --filter ancestor=cloudflare/cloudflared:latest -q | xargs -r docker rm -f
sudo pkill -f 'cloudflared.*tunnel.*run' || true
pgrep -fal 'cloudflared.*tunnel.*run' || true   # should print nothing

# start one connector (use the token from the “good” tunnel above)
docker run -d --name cloudflared --restart=unless-stopped \
  --network parsernet cloudflare/cloudflared:latest \
  --loglevel debug tunnel --no-autoupdate run --protocol auto \
  --token "$TUNNEL_TOKEN"

# verify it registered & pulled ingress
sleep 2
docker logs --since 5s cloudflared 2>&1 | awk '/Updated to new configuration|Registered tunnel connection|Starting tunnel/{print}'

```

---

## 7) Convex / Frontend env

Ensure the Convex action points to the **edge** origin and carries the service token headers.

```bash
# set Convex env (project dir)
npx convex env set CONVEX_PARSER_URL https://parser.dasti.ai
npx convex env set CF_ACCESS_CLIENT_ID  <SERVICE_TOKEN_CLIENT_ID>.access
npx convex env set CF_ACCESS_CLIENT_SECRET <SERVICE_TOKEN_CLIENT_SECRET>

# verify
npx convex env get CONVEX_PARSER_URL
npx convex env get CF_ACCESS_CLIENT_ID
npx convex env get CF_ACCESS_CLIENT_SECRET

```

Restart your dev stack so the action picks these up:

```bash
./run.sh down || true
OPEN_BROWSER=0 ./run.sh up --ui
# or
cd my-app
pkill -f 'convex.*dev' || true
npx convex dev

```

---

## 8) Smoke test matrix (copy/paste)

```bash
# health
curl --http1.1 -s -o /dev/null -w 'ready=%{http_code}\n' https://parser.dasti.ai/ready

# protected GET (no token): expect 403/405
curl --http1.1 -s -o /dev/null -w 'get=%{http_code}\n' https://parser.dasti.ai/mistral-ocr/parse

# protected POST with token: expect 200
curl --http1.1 -s -o /dev/null -w 'post=%{http_code}\n' \
  -H 'Accept: application/json' -H 'Expect:' \
  -H 'CF-Access-Client-Id: <SERVICE_TOKEN_CLIENT_ID>.access' \
  -H 'CF-Access-Client-Secret: <SERVICE_TOKEN_CLIENT_SECRET>' \
  -F "file=@./fixtures/cv_png.pdf;type=application/pdf" \
  https://parser.dasti.ai/mistral-ocr/parse

# prove the POST hit your connector
docker logs --since 120s cloudflared 2>&1 | grep -Ei ' /mistral-ocr/parse' || echo 'NO parse seen'

```

---

## 9) Troubleshooting quick map

- `ready=502` and **no** `/ready` in connector log → wrong tunnel/DNS; fix the tunnel routes or token.
- `get=403/405` is OK (protected path / method not allowed).
- `post=403` → the service token is wrong or Access policy order is wrong.
    
    Fix: ensure Protected app has **only** “Service Auth → Include → `<token>`” on top; rotate token if needed.
    
- `post=502` and **no** `/mistral-ocr/parse` in connector log → edge blocked/redirected; add the narrow WAF Skip rule or remove conflicting Workers/Routes in other tunnels.
- POST succeeds via CLI but **UI fails** (502) and connector sees nothing → the UI didn’t send CF headers or used a different origin; fix Convex env (Section 7).