
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