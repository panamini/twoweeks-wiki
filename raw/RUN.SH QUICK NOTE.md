
RUN.SH QUICK NOTE

Purpose
`run.sh` is the main dev entrypoint for the app stack.
It should replace long boot commands and make normal startup simple.

Core commands
- `./run.sh local`
- `./run.sh local-convex`
- `./run.sh tunnel`
- `./run.sh down`
- `./run.sh reset`
- `./run.sh status`
- `./run.sh logs`
- `./run.sh build-parser`   # only if rebuild is implemented

Command meaning

1. `./run.sh local`
Use this for normal local app work.
Expected behavior:
- starts Vite
- frontend talks to local parser at `http://127.0.0.1:8001`
- uses the validated export-capable parser runtime
- should NOT use parser workspace mount by default
- should NOT start local Convex by default
- should use normal online/default Convex
- should support working exports:
  - Resume ATS PDF
  - Resume Styled PDF
  - Proposal ATS PDF
  - Proposal Styled PDF
  - Proposal DOCX

2. `./run.sh local-convex`
Use this only when debugging Convex locally.
Expected behavior:
- same as `local`
- also starts local Convex
- advanced mode, not the default daily workflow

3. `./run.sh tunnel`
Use this for the old tunnel/edge workflow.
Expected behavior:
- starts Vite
- frontend talks to `PARSER_ORIGIN` / `https://parser.dasti.ai`
- starts cloudflared if needed
- should still use the correct export-capable parser runtime
- exports must work through the tunnel

4. `./run.sh down`
Normal stop command.
Expected behavior:
- stops Vite
- stops local Convex if run.sh started it
- stops parser if run.sh started it
- stops cloudflared if tunnel mode started it
- does NOT delete images or caches

5. `./run.sh reset`
Recovery cleanup.
Expected behavior:
- does everything `down` does
- removes stale parser/cloudflared containers
- kills stale Vite/Convex processes
- clears stale tmp/dev-stack state and temp logs
- does NOT delete Docker images
- does NOT delete node_modules
- does NOT do destructive cleanup

6. `./run.sh status`
Quick health/status summary.
Should show:
- parser status
- parser origin
- Vite status
- Convex mode
- tunnel status if relevant

7. `./run.sh logs`
Shows parser logs quickly.

8. `./run.sh build-parser`
Explicit rebuild command.
This should be the only normal rebuild path.
`local` and `tunnel` should NOT rebuild every time by default.

Important runtime rules
- Normal boot must be fast.
- `local` and `tunnel` must not rebuild the parser image every run.
- Normal modes must not use the bad parser workspace-mount default.
- If workspace-mount mode still exists, it must be explicit only.
- Parser/export runtime must support:
  - Node
  - npm
  - tsx loader
  - Playwright
  - Chromium
  - DOCX generation

Architecture summary
- parser service handles export endpoints
- final exports are direct-download
- export source of truth is normalized data, not preview DOM
- Robial grid governs export geometry
- stylePreset governs typography, palette, emphasis, ornament
- old raster DOM export helper is legacy, not final architecture

Practical default workflow
- normal work: `./run.sh local`
- Convex backend debugging: `./run.sh local-convex`
- tunnel workflow: `./run.sh tunnel`
- stop stack: `./run.sh down`
- recover weird state: `./run.sh reset`

Known anti-patterns
- rebuilding parser image on every `local`/`tunnel` boot
- using preview DOM as export source
- using parser workspace mount by default in export-capable modes
- needing long commands like `--ui --local-origin --local-convex` for normal usage

What “green” means
All of these should work in the intended mode:
- Resume ATS PDF
- Resume Styled PDF
- Proposal ATS PDF
- Proposal Styled PDF
- Proposal DOCX