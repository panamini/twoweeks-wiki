
  
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