Use `./run.sh up --ui` when you are doing UI work or reproducing the shared-cloud path intentionally.

  

Use `./run.sh up --ui --local-origin --local-convex` when you are debugging parser selection, local OCR behavior, or any end-to-end resume import issue where local parser changes must be exercised.



kill les ports actifs convex

pkill -f 'convex dev'
pkill -f 'convex-local-backend|convex-local|convex-lo' || true
lsof -nP -iTCP:3210 -sTCP:LISTEN

run
./run.sh up --ui --local-origin --local-convex

cd /Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan

pkill -f "convex dev" || true
pkill -f "convex-local-backend" || true
pkill -f "vite --host localhost --port 5173" || true

sleep 2

lsof -nP -iTCP:3210 -sTCP:LISTEN
lsof -nP -iTCP:5173 -sTCP:LISTEN
lsof -nP -iTCP:8001 -sTCP:LISTEN