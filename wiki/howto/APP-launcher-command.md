
  
## `./run.sh local`  
- starts the app in true local mode  
- frontend points to `http://127.0.0.1:8001`  
- starts the parser locally in the validated image-runtime mode  
- does **not** use the workspace bind mount by default  
- should boot in the mode where PDF/DOCX export actually works  
- cloud Convex by default unless there is a clearly separate advanced mode  
  
## `./run.sh tunnel`  
- starts the app in the old tunnel/edge mode like before  
- frontend points to `https://parser.dasti.ai`  
- should not force me into the long flag version  
- should behave like the previous normal remote/dev workflow  
  
## ./run.sh down`

Normal close/stop command.  
It should:

- stop Vite
- stop local Convex if started by `run.sh`
- stop parser container started by `run.sh`
- stop cloudflared if `run.sh tunnel` started it
- keep images, caches, and repo state intact
  
## `./run.sh reset`  
- cleans up stale local dev state safely  
- stop/remove stale parser container if needed  
- stop stale cloudflared if needed  
- clear stale vite/convex processes if needed  
- this should make the next `local` or `tunnel` boot clean


`./run.sh help


`local-convex` just means:

- instead of talking to your usual remote Convex deployment,
- the app starts a **local Convex dev backend** on your machine.

## In simple terms

### `./run.sh local`

- local parser
- app points to local parser
- **Convex stays on the normal online/default deployment**

### `./run.sh local-convex`

- local parser
- app points to local parser
- **Convex also runs locally on your machine**

### `./run.sh tunnel`

- app uses the tunnel/edge parser flow like before
- Convex stays on the normal online/default deployment unless explicitly changed

## So do you need `local-convex`?

Probably **no**, unless you are actively developing/debugging Convex backend functions locally.

For your normal use, the right command is likely:

./run.sh local

or

./run.sh tunnel

## Good mental model

- **parser** = OCR / export / file-processing service
- **Convex** = app backend/database/actions
- `local-convex` is only for backend dev work on Convex itself

- `./run.sh local` → fast start, no rebuild by default
- `./run.sh local-convex` → same, plus local Convex
- `./run.sh tunnel` → fast start, no rebuild by default
- `./run.sh build-parser` → explicit rebuild
- `./run.sh down` → normal stop
- `./run.sh reset` → stronger cleanup, non-destructive
- `./run.sh status` → quick state
- `./run.sh logs` → parser logs

### Runtime behavior

- `local` and `tunnel` should use the **validated export-capable image**
- if the image is missing, build once
- if the image looks stale, show a clear warning:
    - “parser image may be stale, run `./run.sh build-parser`”
- optional:
    - `./run.sh local --rebuild`
    - `./run.sh tunnel --rebuild`