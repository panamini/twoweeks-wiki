# 

Date: 2026-06-12  
Status: docs-only exploration plan  
Scope: non-production planning only

## 1. Objective

PR35 explores the official OpenAI Apps SDK path and maps it to the current Twoweeks Local MCP safety chain.

PR35 answers one question:

What is the smallest safe next step toward an Apps SDK prototype without starting runtime integration?

PR35 does not approve build work, runtime integration, ChatGPT connection, production exposure, or user-data access.

## 2. Explicit non-permissions

PR35 does not allow:

- Apps SDK install
- MCP SDK install
- OpenAI SDK install
- `/mcp` endpoint
- `tools/list` runtime
- `tools/call` runtime
- `call_tool` runtime
- Streamable HTTP transport
- SSE transport
- public tunnel
- ChatGPT connector setup
- Developer Mode setup
- auth implementation
- OAuth
- UI components
- widget resources
- iframe rendering
- Convex changes
- real handlers
- real user data
- export/download/send/submit/apply
- production behavior

## 3. Sources reviewed

Repository sources:

- `AGENTS.md` - repo rules, `v1` baseline, docs placement, and verification expectations.
- `docs/audits/2026-06-12-chatgpt-app-prototype-readiness-checkpoint.md` - PR34 readiness checkpoint and non-permissions.
- `docs/plans/2026-06-11-chatgpt-app-non-production-prototype-plan.md` - PR28 Plan/Build/Deploy boundary.
- `docs/plans/2026-06-11-chatgpt-app-local-only-manifest-draft.md` - PR29 static manifest rules and future tool metadata policy.
- `docs/audits/2026-06-11-chatgpt-app-end-to-end-safety-audit.md` - PR30 safety audit and execution-path blockers.
- `docs/decisions/2026-06-11-mcp-schema-projection.md` - PR18 descriptor projection and read-only/non-destructive/closed-world annotations.
- `docs/decisions/2026-06-11-mcp-call-envelope-error-contract.md` - PR19 non-executable call envelope.
- `docs/decisions/2026-06-11-mcp-approval-audit-boundary.md` - PR20 approval and audit shell boundary.
- `docs/decisions/2026-06-11-mcp-real-handler-boundary-design.md` - PR21 design-only real handler boundary.
- `docs/decisions/2026-06-11-mcp-remote-transport-spike.md` - PR22 disabled/reference-only transport model.
- `docs/plans/2026-06-11-chatgpt-app-ux-privacy-spec.md` - PR23 UX, consent, privacy, refusal, rollback, and review gates.
- `docs/decisions/2026-06-11-mcp-privacy-redaction-fixtures.md` - PR24 sentinel fixture scope and limitation.
- `docs/decisions/2026-06-11-mcp-tool-visibility-policy.md` - PR25 hidden-by-default visibility policy.
- `docs/decisions/2026-06-11-mcp-approval-ux-copy-fixtures.md` - PR26 fixed safe copy catalog.
- `docs/decisions/2026-06-11-mcp-privacy-review-gate.md` - PR27 privacy gate semantics.
- `my-app/src/modules/local-mcp/chatGptAppPrototypeScaffold.ts` - PR31 active fixture-only scaffold.
- `my-app/src/modules/local-mcp/chatGptAppPrototypeScaffoldGoldenFixtures.ts` - PR33 golden fixture scenarios.
- `my-app/src/modules/local-mcp/mcpPrivacyReviewGate.ts` - PR27.1 fail-closed review gate implementation.
- `my-app/src/modules/local-mcp/privacyRedactionFixtures.ts` - PR24 fixture-level privacy sentinel checks.
- `my-app/src/modules/local-mcp/mcpApprovalUxCopyFixtures.ts` - PR26 copy fixtures and action-word guards.
- `my-app/src/modules/local-mcp/__tests__/chatGptAppPrototypeScaffold.test.ts` - PR31/PR32 scaffold guard coverage.
- `my-app/src/modules/local-mcp/__tests__/chatGptAppPrototypeScaffoldGoldenFixtures.test.ts` - PR33 golden fixture guard coverage.

Official and high-trust sources reviewed on 2026-06-12:

- OpenAI Apps SDK overview/navigation - confirms Plan, Build, Deploy, Security & Privacy, and App submission surfaces: [https://developers.openai.com/apps-sdk](https://developers.openai.com/apps-sdk)
- OpenAI Apps SDK Quickstart - confirms Apps SDK uses MCP, requires an MCP server, and optionally uses a web component rendered in ChatGPT: [https://developers.openai.com/apps-sdk/quickstart](https://developers.openai.com/apps-sdk/quickstart)
- OpenAI Apps SDK MCP Server concept - confirms minimal Apps SDK MCP capabilities: list tools, call tools, and return UI metadata/resources: [https://developers.openai.com/apps-sdk/concepts/mcp-server](https://developers.openai.com/apps-sdk/concepts/mcp-server)
- OpenAI Apps SDK Research use cases - confirms use-case research, prompt sampling, direct/indirect/negative evaluation prompts, component intent, state needs, and legal/compliance review before implementation: [https://developers.openai.com/apps-sdk/plan/use-case](https://developers.openai.com/apps-sdk/plan/use-case)
- OpenAI Apps SDK Define tools - confirms tool-first contract design, explicit inputs, predictable outputs, separate read/write tools, and structured content planning: [https://developers.openai.com/apps-sdk/plan/tools](https://developers.openai.com/apps-sdk/plan/tools)
- OpenAI Apps SDK Design components - confirms component intent, data requirements, iframe/responsive planning, auth context, and state contract planning: [https://developers.openai.com/apps-sdk/plan/components](https://developers.openai.com/apps-sdk/plan/components)
- OpenAI Apps SDK Build your MCP server - reviewed only to identify future blockers around server, tools, templates, widget runtime, HTTP reachability, and UI bundle prerequisites: [https://developers.openai.com/apps-sdk/build/mcp-server](https://developers.openai.com/apps-sdk/build/mcp-server)
- OpenAI Apps SDK Build your ChatGPT UI - reviewed only to identify future blockers around iframe UI, MCP Apps bridge, `tools/call`, and component runtime: [https://developers.openai.com/apps-sdk/build/chatgpt-ui](https://developers.openai.com/apps-sdk/build/chatgpt-ui)
- OpenAI Apps SDK Authenticate users - reviewed only to identify future OAuth 2.1 and customer-data blockers: [https://developers.openai.com/apps-sdk/build/auth](https://developers.openai.com/apps-sdk/build/auth)
- OpenAI Apps SDK Manage state - reviewed only to identify business/UI/cross-session state blockers: [https://developers.openai.com/apps-sdk/build/state-management](https://developers.openai.com/apps-sdk/build/state-management)
- OpenAI Apps SDK Deploy your app - reviewed only to identify future tunnel, HTTPS `/mcp`, TLS, streaming, logs, and metrics blockers: [https://developers.openai.com/apps-sdk/deploy](https://developers.openai.com/apps-sdk/deploy)
- OpenAI Apps SDK Connect from ChatGPT - reviewed only to identify Developer Mode, connector, public `/mcp`, tunnel, and metadata-refresh blockers: [https://developers.openai.com/apps-sdk/deploy/connect-chatgpt](https://developers.openai.com/apps-sdk/deploy/connect-chatgpt)
- OpenAI Apps SDK Test your integration - reviewed only to identify MCP Inspector, `tools/list`, `tools/call`, direct/indirect/negative golden prompt, auth, structured content, and component verification blockers: [https://developers.openai.com/apps-sdk/deploy/testing](https://developers.openai.com/apps-sdk/deploy/testing)
- OpenAI Apps SDK Submit your app - reviewed only to identify public distribution and dashboard review blockers: [https://developers.openai.com/apps-sdk/deploy/submission](https://developers.openai.com/apps-sdk/deploy/submission)
- OpenAI Apps SDK Security & Privacy - confirms least privilege, explicit consent, prompt-injection assumptions, server-side validation, audit logs, data retention, deletion, and logging/redaction requirements: [https://developers.openai.com/apps-sdk/guides/security-privacy](https://developers.openai.com/apps-sdk/guides/security-privacy)
- OpenAI Apps SDK App submission guidelines - confirms accurate tool definitions, correct `readOnlyHint`, `destructiveHint`, `openWorldHint`, minimal inputs, auditable behavior, and transparent auth requirements: [https://developers.openai.com/apps-sdk/app-submission-guidelines](https://developers.openai.com/apps-sdk/app-submission-guidelines)
- OpenAI official `openai-apps-sdk-examples` repository - reviewed only as future architecture/blocker reference; no code copied and no dependencies installed: [https://github.com/openai/openai-apps-sdk-examples](https://github.com/openai/openai-apps-sdk-examples)
- Model Context Protocol official specification, version 2025-11-25 latest - confirms JSON-RPC, host/client/server architecture, capability negotiation, tools/resources/prompts, and security/trust principles: [https://modelcontextprotocol.io/specification/2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25)
- Model Context Protocol tools specification, version 2025-11-25 latest - confirms `tools/list`, `tools/call`, tool schemas, structured content, output schema, annotations, and human-in-the-loop guidance: [https://modelcontextprotocol.io/specification/2025-11-25/server/tools](https://modelcontextprotocol.io/specification/2025-11-25/server/tools)
- Model Context Protocol transport specification, version 2025-11-25 latest - confirms stdio and Streamable HTTP, single MCP endpoint path for Streamable HTTP, SSE behavior, origin/auth warnings, session IDs, and protocol-version headers: [https://modelcontextprotocol.io/specification/2025-11-25/basic/transports](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports)
- Model Context Protocol authorization specification, version 2025-11-25 latest - confirms HTTP auth expectations and OAuth 2.1 requirements when auth is supported: [https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

## 4. cur Twoweeks baseline after PR34

After PR34, Twoweeks is conditionally ready for planning-only Apps SDK exploration.

The current baseline is:

- local-only
- fixture-only
- review-only
- non-runnable
- non-callable
- no real handlers
- no real user data
- no runtime transport
- no OAuth
- no UI
- no ChatGPT connector
- no production path

This is active code for the fixture scaffold only.  
It is not Apps SDK runtime code.  
It is not ChatGPT App readiness.

## 5. Official Apps SDK path summary

Official path, summarized:

- Apps SDK apps use MCP to connect to ChatGPT.
- An Apps SDK app normally requires an MCP server that exposes tools to ChatGPT.
- The MCP server advertises tools and schemas, accepts tool calls, and returns structured results.
- Apps can optionally provide UI components/resources that render inside ChatGPT.
- UI components run in an iframe and communicate through the MCP Apps bridge.
- ChatGPT needs access to the MCP endpoint before a connector can be created or tested.
- Customer-specific data or write actions introduce authentication/OAuth requirements.
- State must be deliberately split between backend business data, ephemeral widget state, and durable cross-session state.
- Deployment and submission require a reachable HTTPS MCP endpoint, TLS, logs/metrics, Developer Mode testing, app review, and policy compliance.
- Security and privacy review is mandatory for any real-data or write-action path.

Planning-only requirements extracted from official sources:

- Use-case research: define the user persona, scenario, data sources, compliance constraints, and success sentence before tool or UI design.
- Prompt sampling: collect direct prompts, indirect prompts, and negative prompts to tune discovery precision and recall.
- Evaluation prompts: build a golden prompt set and later record tool selection, arguments, and confirmation behavior.
- Tool contract design: one job per tool, explicit inputs, predictable structured outputs, separate read and write tools, safe parameter annotations, and machine-readable IDs.
- Tool annotations: classify tools with `readOnlyHint`, `destructiveHint`, and `openWorldHint` correctly before review.
- Component intent: decide viewer/editor, single-shot/multiturn, inline/fullscreen, empty states, structured payload, auth context, and state contract before UI implementation.
- Security/privacy: apply least privilege, explicit consent, input validation, prompt-injection testing, audit logs, data minimization, retention, deletion, redaction, and safe logging.
- Authentication/OAuth blockers: customer-specific data and write actions require an OAuth 2.1-compliant MCP auth model before runtime exposure.
- State-management blockers: authoritative business data, UI state, and cross-session state need separate ownership and lifetime decisions.
- Deployment/submission blockers: public HTTPS `/mcp`, TLS, streaming, logs/metrics, Developer Mode connector, MCP Inspector testing, screenshots/artifacts, app review, and submission metadata remain unresolved.

Implementation-only requirements that remain forbidden in PR35:

- package dependency installation
- MCP server creation
- `/mcp` endpoint
- `tools/list`
- `tools/call`
- public tunnel/ngrok
- Developer Mode setup
- ChatGPT connector creation
- OAuth
- UI/widget implementation
- state persistence
- deployment
- app submission

## 6. Requirement map against Twoweeks

|Requirement|Official requirement summary|cur Twoweeks status|Covered by PR18-PR34?|Gap|Allowed in PR35 impl?|Notes|
|---|---|---|---|---|---|---|
|Tool listing|MCP servers expose tools through `tools/list` with schemas and metadata.|PR18 projects local descriptor shapes only.|Partially, as static projection.|No runtime MCP server or `tools/list`.|No|PR18 is not protocol runtime.|
|Tool calling|MCP clients invoke tools through `tools/call` / call_tool semantics.|PR19 has a non-executable local envelope.|Partially, as local call shape.|No handler execution, JSON-RPC, or protocol call path.|No|PR19 intentionally omits `method` and `params`.|
|Structured content|Tool results can return `structuredContent` and may declare `outputSchema`.|PR18/PR31 use bounded fixture output and safe summaries.|Partially, for shape planning.|No approved real output schema or runtime result validation.|No|Full generated artifacts remain blocked in generic tool output.|
|Tool metadata|Tool names, descriptions, inputs, outputs, and annotations guide model discovery and review.|PR18/PR29 define candidate names and metadata policy.|Partially.|Need official Apps SDK descriptor mapping and review copy.|No|Avoid executable wording.|
|Component/resource metadata|Apps can return UI/resource metadata so ChatGPT renders components.|PR29 discusses placeholders only.|No runtime coverage.|No `ui://` resource, template, iframe, bridge, or resource registration.|No|Component intent must stay planning-only.|
|opt UI component|UI is optional; if used, it renders in ChatGPT iframe and uses MCP Apps bridge.|Current scaffold sets `noUiComponent: true`.|Covered as forbidden.|No UI model, component state contract, or accessibility review.|No|Future may choose no UI.|
|Transport|MCP supports stdio and Streamable HTTP; Apps deployment needs HTTP reachability.|PR22 models disabled/non-production preflight only.|Partially, as disabled reference.|No approved transport, listener, Streamable HTTP, SSE, session, origin/auth enforcement.|No|PR22 is not a server.|
|Public accessibility for ChatGPT|Connector needs reachable HTTPS MCP endpoint, commonly `/mcp`.|None.|No.|No public endpoint, TLS, tunnel, deployment, logs, or metrics.|No|Official docs make this a deploy/connect blocker.|
|Connector setup in ChatGPT|Developer Mode connector requires metadata and public `/mcp` endpoint.|None.|No.|No Developer Mode setup or connector metadata flow.|No|Explicitly forbidden in PR35.|
|auth/OAuth|Customer-specific data or write actions should authenticate users; HTTP auth follows MCP OAuth expectations.|PR22 says future auth required; no implementation.|Only as blocker.|No OAuth 2.1 flow, tokens, client registration, scope model, account linking, or auth tests.|No|This blocks real user data.|
|Security/privacy review|Apps SDK requires least privilege, explicit consent, validation, prompt-injection defense, logging/audit, retention, deletion, and redaction.|PR23-PR27.1 define local review and fixture checks.|Partially.|No semantic privacy review, threat model update, real-data policy, or production security checklist.|No|PR24 sentinel absence is not semantic privacy.|
|Submission/deployment|Public app submission requires tested app, public MCP server, CSP, screenshots, metadata, review, and policy compliance.|None.|No.|No deployment, submission materials, org/app review readiness, or public distribution decision.|No|PR35 does not approve public/private submission.|

## 7. PR18-PR34 safety-chain mapping

|Safety-chain item|Contribution|What it does not solve|Can be reused for future Apps SDK work?|Risk if misinterpreted|
|---|---|---|---|---|
|PR18 schema projection|Projects local tools to stable `twoweeks.*` descriptors with closed schemas and read-only/non-destructive/closed-world annotations.|No `tools/list`, server, protocol, or runtime metadata review.|Yes, as descriptor input for future mapping.|Static descriptors may be mistaken for advertised MCP tools.|
|PR19 call envelope|Defines safe local call shape and error taxonomy without JSON-RPC runtime.|No `tools/call`, handler execution, transport, or model-invoked call path.|Yes, as a future internal adapter boundary.|Envelope may be mistaken for a protocol request.|
|PR20 approval/audit shell|Defines approval requests, decisions, audit event shells, and safe argument summaries.|No approval UI, persistent audit, real consent, or action execution.|Yes, as design input for future approval/audit policy.|Shell presence may be mistaken for enforceable audit.|
|PR21 handler boundary|Describes future real handler gates: approval, audit, idempotency, rollback, and privacy.|No real handler, registry, execution, or product side effect.|Yes, as a future implementation checklist.|Design-only boundary may be mistaken for handler readiness.|
|PR22 disabled/ref transport spike|Models disabled/non-production transport preflight, origin/host/auth expectations, limits, and blocking reasons.|No listener, route, network call, Streamable HTTP, SSE, OAuth, or production transport.|Yes, as threat-model input.|`allowed_for_non_production_spike` may be mistaken for runtime permission.|
|PR23 UX/privacy spec|Documents consent, refusal, redaction, rollback, visibility, and submission review gates.|No UI, code, legal approval, or production privacy review.|Yes, as policy input.|Spec may be mistaken for approved user-facing UX.|
|PR24 privacy redaction fixtures|Adds sentinel fixtures and checks for forbidden material in safe output-like objects.|Not a semantic privacy system, runtime sanitizer, or global product artifact policy.|Yes, as fixture-level regression support.|PR24 sentinel fixtures are not semantic privacy.|
|PR25 visibility policy|Defines hidden-by-default states and deterministic visibility decisions.|No UI listing, no ChatGPT exposure, no callable listing.|Yes, as policy input.|`listed_ready_for_review` may be mistaken for callable.|
|PR26 approval UX copy fixtures|Pins short safe copy and maps errors/transport/visibility states to copy keys.|No UI, no consent screen, no real approval workflow.|Yes, as future copy fixture source.|Copy may be mistaken for a working approval path.|
|PR27/27.1 privacy review gate|Combines visibility, privacy, approval, audit, handler, transport, and copy inputs into fail-closed review statuses.|No runtime permission, no exec approval, no production or ChatGPT approval.|Yes, as one review input.|PR27.1 `ready_for_internal_review` is not exec approval.|
|PR28 non-production prototype plan|Locks Plan-only boundary and forbids Build/Deploy surfaces.|No implementation, SDK, server, UI, auth, or transport.|Yes, as scope guard.|Plan may be mistaken for prototype approval.|
|PR29 local-only manifest draft|Defines static placeholder manifest/tool metadata rules.|No real manifest, resource, OAuth config, endpoint, or Apps SDK descriptor.|Yes, as future metadata draft input.|Static draft may be mistaken for machine-consumed config.|
|PR30 end-to-end safety audit|Confirms no approved execution path across PR18-PR29 and gates PR31.|No runtime, no server, no auth, no UI, no production readiness.|Yes, as audit baseline.|Passing audit may be mistaken for production readiness.|
|PR31 prototype scaffold|Adds local-only, fixture-only scaffold cards with non-runnable constraints.|No Apps SDK app, no ChatGPT connection, no real handler, no data, no UI.|Yes, as mock review artifact only.|PR31 scaffold is not app readiness.|
|PR32 scaffold fixtureOutput hardening|Asserts fixture output status/summary consistency against card state.|No runtime safety, no protocol safety, no privacy proof.|Yes, as fixture drift guard.|Shape hardening may be mistaken for integration hardening.|
|PR33 golden fixtures|Freezes default, blocked, review-required, ready, and mixed scaffold scenarios.|No runtime safety, no semantic privacy, no ChatGPT test.|Yes, as planning regression evidence.|PR33 golden fixtures prove shape stability, not runtime safety.|
|PR34 readiness checkpoint|Confirms conditional readiness for PR35 planning only.|No Apps SDK build approval, no package install, no server, no connection, no production.|Yes, as PR35 entry checkpoint.|Conditional planning readiness may be mistaken for integration approval.|

## 8. Gap analysis

Confirmed gaps:

- No approved MCP server architecture.
- No approved runtime transport.
- No approved public endpoint.
- No approved OAuth/auth model.
- No approved real handler boundary.
- No approved tool execution semantics.
- No approved user-data minimization contract for real data.
- No approved semantic privacy review beyond sentinel fixtures.
- No approved UI/widget component model.
- No approved connector setup flow.
- No approved state management model.
- No approved deployment model.
- No approved production security checklist.
- No approved dependency policy for Apps SDK/MCP SDK.

Planning-only gaps extracted from official sources:

- Use-case research is not complete: Twoweeks has candidate tools, but no Apps SDK-specific persona, scenario, compliance, rate-limit, or user-success sentence.
- Prompt sampling is not complete: no direct, indirect, and negative Apps SDK discovery prompt set exists yet.
- Evaluation prompts are not complete: no official-style golden prompt set records model selection, arguments, and confirmation behavior because no connector exists.
- Tool contract design is incomplete: current descriptor projection does not yet define official Apps SDK-ready tool descriptions, output schemas, write/read split, annotation justifications, or minimal input rationale.
- Read-only/destructive/open-world annotations need a written justification for every candidate tool before submission-grade work.
- Component intent is not decided: viewer/editor, single-shot/multiturn, inline/fullscreen, structured payload, auth context, and empty states remain undefined.
- Security/privacy remains planning-only: prompt injection, least privilege, consent, retention, deletion, redaction, and logs/audit are not production-reviewed.
- Authentication/OAuth remains a blocker for customer-specific data or write actions.
- State management remains a blocker because authoritative business data, UI state, and durable cross-session state have no approved Apps SDK ownership model.
- Deployment/submission remains blocked because no public HTTPS `/mcp`, TLS, tunnel, logs, metrics, Developer Mode connector, CSP, screenshots, test credentials, or submission metadata exists.

## 9. Security and privacy implications

Apps SDK work may expose user data, third-party API access, and write actions in future.

Any future implementation must:

- follow least privilege;
- require explicit user consent;
- validate all inputs server-side;
- treat prompt injection as expected, not exceptional;
- define human confirmation for irreversible or write operations;
- keep approval and audit boundaries before any write action;
- define minimization, retention, deletion, redaction, logging, and audit rules for real-data paths;
- separate user-visible data, model-visible data, and component-only data;
- avoid raw prompt text, raw source documents, secrets, tokens, session identifiers, stack traces, private facts, and `never_use` facts in logs or generic tool output;
- prove that write or open-world tools cannot hide side effects;
- provide clear rollback, disable, and incident-response paths.

Strict interpretation:

- Fixture safety is not runtime safety.
- Golden fixture stability is not privacy proof.
- PR24 sentinel absence is not semantic privacy.
- PR27.1 `ready_for_internal_review` is only review evidence.
- PR31 scaffold output is not Apps SDK, MCP, ChatGPT, OAuth, UI, or production readiness.

## 10. Runtime blockers

Runtime implementation remains blocked until these boundaries are resolved:

- server boundary
- transport boundary
- auth boundary
- handler boundary
- data boundary
- privacy boundary
- approval boundary
- audit boundary
- UI/resource boundary
- state boundary
- deployment boundary
- dependency boundary

Implementation-only requirements remain forbidden in PR35:

- package dependency installation
- MCP server creation
- `/mcp` endpoint
- `tools/list`
- `tools/call`
- public tunnel/ngrok
- Developer Mode setup
- ChatGPT connector creation
- OAuth
- UI/widget implementation
- state persistence
- deployment
- app submission

## 11. Smallest safe next step

The smallest safe next step is a docs-only MCP server architecture decision record.

That ADR should define, without code:

- future MCP server boundary;
- future transport boundary;
- future tool exposure model;
- no-real-data mode;
- official Apps SDK/MCP descriptor mapping;
- read-only/destructive/open-world annotation policy;
- structured content and output schema policy;
- security/privacy gates;
- approval and audit gates;
- forbidden runtime surfaces;
- dependency approval checkpoint.

This is safer than installing the SDK or building `/mcp` because the current gap is architectural permission, not implementation skill.

PR35 should not recommend installing the SDK, building an endpoint, creating a tunnel, using Developer Mode, connecting to ChatGPT, implementing OAuth, adding UI, persisting state, deploying, or submitting an app.

## 12. min gates before any impl PR

Any implementation PR requires all of:

- Written MCP server architecture decision.
- Written transport/public endpoint decision.
- Written auth/OAuth decision.
- Written real-user-data policy.
- Written handler execution policy.
- Written approval/audit policy for real tool calls.
- Written UI/widget resource policy.
- Written state management policy.
- Updated threat model.
- Updated privacy review.
- Explicit maintainer approval to install dependencies.
- Explicit maintainer approval to touch package files.
- Explicit maintainer approval to add runtime code.
- Explicit maintainer approval to expose any endpoint.
- Explicit maintainer approval to connect anything to ChatGPT.

No missing gate may be treated as implied approval.

## 13. Recommended future PR sequence

Conservative future sequence:

- PR36: MCP server architecture decision record - docs only.
- PR37: Real-data, privacy, consent, retention, and audit policy - docs only.
- PR38: Tool contract mapping from local fixtures to future MCP descriptors - docs-only or tests-only.
- PR39: Runtime threat model for Apps SDK integration - docs only.
- PR40: Dependency, package, and server skeleton approval checkpoint - docs only.
- PR41 or later: first possible code PR, only if explicitly approved.

Do not create these future PRs from PR35.

## 14. PR35 verdict

PR35 allows continued planning only.

PR35 identifies the smallest safe next step toward a future Apps SDK prototype.

PR35 does not approve implementation.

PR35 does not approve package installation.

PR35 does not approve MCP server creation.

PR35 does not approve ChatGPT connection.

PR35 does not approve runtime integration.

PR35 does not approve production.

## 15. Rollback

Rollback is deletion-only:

```
docs/plans/2026-06-12-chatgpt-apps-sdk-non-production-exploration-plan.md
```

To pick up a draggable item, press the space bar. While dragging, use the arrow keys to move the item. Press space again to drop the item in its new position, or press escape to cancel.