---
tool: " "
llm: " "
test: " "
fixture: " "
install: " "
playwright: " "
---


1. Install Chromium for Playwright:
   npx playwright@latest install chromium

2. If the local app server is not already running, start it on:
   http://127.0.0.1:5173

3. Run a headless Playwright script against the live `/cv` route.
   The script should:
   - seed localStorage before navigation
   - set `dasti:cv-forge-workspace-mode:v1=preview`
   - set `cvActiveId=<fixture-id>`
   - set `cvDocuments=[<doc>]`
   - set `cv:<fixture-id>=<doc>`
   - navigate to `/cv?id=<fixture-id>`
   - wait for `[data-testid="resume-template-page"]`
   - capture screenshot(s)
   - read page count from:
     - `[data-document-page="true"]`
     - `.dasti-doc-page-count`

4. For the probe fixture pass, I used three cases:
   - experience continuation
   - selected projects
   - normal prose

5. The browser check is headless Chromium via Playwright.
   No repo code changes are needed for the browser install itself.
Exact install command I used:

npx playwright@latest install chromium
