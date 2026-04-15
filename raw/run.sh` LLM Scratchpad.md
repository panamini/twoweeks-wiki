
## What `run.sh` is

  

`./run.sh` is the single local dev entrypoint for the app stack:

  

- parser container

- local Convex dev backend when needed

- Vite frontend when needed

- optional Cloudflare tunnel validation path

  

It chooses between two parser runtime styles:

  

- `image` runtime: uses the built Docker image exactly as installed

- `workspace` runtime: bind-mounts the repo for fast Python edits with `uvicorn --reload`

  

## Commands That Matter

  

- `./run.sh tunnel`

Stable full workflow.

Uses image runtime and the edge parser path (`parser.dasti.ai`).

Use this for end-to-end validation.

  

- `./run.sh local-fast`

Fast full-app parser development.

Starts:

- parser in workspace mode with autoreload

- local Convex

- Vite

Frontend and server-side structured upload both resolve the local parser at `http://127.0.0.1:8001`.

Export works here too.

  

- `./run.sh parser-dev`

Parser-only / advanced mode.

Workspace-mounted parser with autoreload, no full app stack.

  

- `./run.sh rebuild-docker`

Explicit rebuild of the parser/export runtime image, then restart.

Use this after Dockerfile or runtime dependency changes.

  

- `./run.sh down`

Stop tracked local processes and containers.

  

- `./run.sh reset`

Stronger cleanup.

Use this if local Convex or Vite state is stale or untracked.

  

- `./run.sh status`

Quick health summary for parser, Convex, tunnel, runtime mode, and logs.

  

- `./run.sh logs`

Follow parser container logs.

  

## Recommended Mental Model

  

- `tunnel` = stable validation mode

- `local-fast` = daily parser development mode

- `parser-dev` = parser-only hacking

- `rebuild-docker` = refresh runtime image

  

If the task is “I changed Python parser code and want the real app to use it now”, use `local-fast`.

  

If the task is “I need the validated production-like path”, use `tunnel`.

  

If the task is “I changed runtime deps, Node export deps, Dockerfile, or Playwright install surface”, run `rebuild-docker` before trusting `local-fast`.

  

## Why `local-fast` Exists

  

Without local Convex, the browser can be local while server-side `structuredUpload` still talks to cloud/env parser config.

  

`local-fast` fixes that by aligning all three layers:

  

- parser is local

- frontend points at local parser

- local Convex actions also point at local parser

  

That is why CV import works end-to-end locally instead of silently routing through `parser.dasti.ai`.

  

## Runtime Details That Matter

  

In `local-fast`, the parser container uses:

  

- repo bind mount at `/app`

- anonymous volume at `/app/node_modules`

- anonymous volume at `/app/my-app/node_modules`

  

This is important because it preserves image-installed Linux export dependencies while still allowing live Python source edits.

  

Why:

  

- export worker boot uses `tsx` from `/app/my-app/node_modules`

- worker imports `playwright` via `/app/node_modules`

- if host macOS `node_modules` leak into the Linux container, export fails with platform-mismatch errors

  

`run.sh` now preflights this runtime surface in workspace mode and tells you to run `./run.sh rebuild-docker` if it is missing.

  

## Mode Selection Rules

  

- `local-fast`

- parser runtime: `workspace`

- parser reload: on

- Convex: local

- frontend parser URL: local

- structured upload parser target: local

- export: expected to work

  

- `tunnel`

- parser runtime: `image`

- Convex: env/default path

- parser URL: edge/tunnel

- use for stable validation

  

- `local`

- local parser + Vite only

- not the recommended full local structured-upload path

  

- `local-convex`

- legacy alias for `local-fast`

  

## Common Failure Cases

  

- `local-fast` fails early telling you export/runtime deps are missing

Cause: workspace mode cannot see the image-installed export runtime surface.

Fix: `./run.sh rebuild-docker`

  

- `local-fast` says local Convex is already running but untracked

Cause: stale or interrupted previous session.

Fix: `./run.sh reset`

  

- browser UI is local but import still hits cloud

Cause: wrong mode, usually not using `local-fast`

Fix: use `./run.sh local-fast`

  

- parser Python edits are not reflected

Cause: not in workspace reload mode

Fix: use `./run.sh local-fast` or `./run.sh parser-dev`

  

## Fast Usage Recipes

  

Daily parser work:

  

```bash

OPEN_BROWSER=0 ./run.sh local-fast

```

  

Stable validation:

  

```bash

./run.sh tunnel

```

  

After runtime dependency changes:

  

```bash

./run.sh rebuild-docker

./run.sh local-fast

```

  

If the stack is confused:

  

```bash

./run.sh reset

./run.sh local-fast

```