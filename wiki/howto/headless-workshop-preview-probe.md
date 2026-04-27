---
title: "Headless Workshop Preview Probe"
category: howto
tags: [playwright, workshop, preview, browser, qa]
created: 2026-04-27
updated: 2026-04-27
status: current
version: v1
sources: [2026-04-27-test-headless-browser-setup-workshop-preview-probe]
related: [[tech/workshop-pagination]], [[tech/repo-testing-system]]
---

# Headless Workshop Preview Probe

Use this procedure to inspect the live `/cv` workshop preview with headless Chromium and seeded local storage.

## Procedure

1. Install Chromium for Playwright if missing:

```bash
npx playwright@latest install chromium
```

2. Start the local app at `http://127.0.0.1:5173`.

3. Run a headless Playwright script that seeds local storage before navigation:

- `dasti:cv-forge-workspace-mode:v1=preview`
- `cvActiveId=<fixture-id>`
- `cvDocuments=[<doc>]`
- `cv:<fixture-id>=<doc>`

4. Navigate to `/cv?id=<fixture-id>`.

5. Wait for `[data-testid="resume-template-page"]`.

6. Capture screenshots and read page count from `[data-document-page="true"]` and `.dasti-doc-page-count`.

## Probe fixtures

The known probe pass used:

- experience continuation
- selected projects
- normal prose

## Sources

- [[sources/2026-04-27-test-headless-browser-setup-workshop-preview-probe]]

## Related

- [[tech/workshop-pagination]]

