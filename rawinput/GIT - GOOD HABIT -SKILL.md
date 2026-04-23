## For a new task: update main from git  first

For a new task:
Switches to `main`, updates it safely from `origin/main`, then creates and moves to a new branch from that updated `main`.

git switch main  
git pull --ff-only origin main  
git switch -c short-descriptive-branch-name