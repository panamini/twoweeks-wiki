
## `run.sh` modes

### 1. Normal local UI, but still **remote/cloud Convex + edge parser**

./run.sh up --ui

Use this when:

- you want the normal app behavior
- you are okay with the **cloud/default Convex path**
- you are okay with the **edge parser / tunnel path**

What it does:

- starts the local parser container anyway
- but frontend origin defaults to `PARSER_ORIGIN`, which defaults to `https://parser.dasti.ai`
- and without `--local-convex`, Convex stays on env/default, typically cloud

Meaning:

- **yes, this still launches the remote/tunnel-oriented flow**
- **yes, it can work**, but only if the remote parser/tunnel path is healthy

---

### 2. Local parser in the browser, but **cloud/default Convex actions**

./run.sh up --ui --local-origin

Use this when:

- you want the frontend/Vite parser origin set local
- but you are **not** switching the app to local Convex

Important:

- `run.sh` explicitly warns this is **not enough** for structured upload actions
- actions still follow the configured Convex backend/env unless you also use `--local-convex`

Meaning:

- good for some frontend-local checks
- **not reliable for true local end-to-end OCR debugging**

---

### 3. Full local stack: **local parser + local Convex + local UI**

./run.sh up --ui --local-origin --local-convex

Use this when:

- you want the real local debugging stack
- you need to test the parser on your machine
- you want structured upload actions to hit the **local parser path**

What it does:

- local parser on `127.0.0.1:8001`
- local Convex from `npx convex dev --local --verbose`
- Vite gets local parser + local Convex URLs injected

Meaning:

- this is the **correct command for local OCR/parser debugging**

---

### 4. Force edge parser explicitly

./run.sh up --ui --edge-origin

Use this when:

- you want to be explicit that the frontend should use the edge origin
- useful for reproducing tunnel/cloud behavior

---

### 5. Stop everything

./run.sh down

---

## Simple rule

### Use this for normal app/dev behavior

./run.sh up --ui

### Use this for real local parser debugging

./run.sh up --ui --local-origin --local-convex

## Direct answer to your question