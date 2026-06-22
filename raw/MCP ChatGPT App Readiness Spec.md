---
aliases:
  - MCP / ChatGPT App Readiness Spec
---


## Status

This PR is documentation-only.  
PR16 Local MCP Beta exists and is the current local foundation.  
No Remote MCP server, ChatGPT App, network transport, OAuth, deployment, or real tool execution is implemented here.

## Source inspection notes

Files inspected:

- `AGENTS.md`
- `docs/decisions/2026-06-08-application-os-master-plan.md`
- `docs/decisions/2026-06-11-local-mcp-beta.md`
- `docs/decisions/2026-06-11-controlled-ats-public-endpoint-resolver.md`
- `my-app/src/modules/internal-tool-contracts/schema.ts`
- `my-app/src/modules/internal-tool-contracts/contracts.ts`
- `my-app/src/modules/internal-tool-contracts/contractRules.ts`
- `my-app/src/modules/local-mcp/schema.ts`
- `my-app/src/modules/local-mcp/toolRegistry.ts`
- `my-app/src/modules/local-mcp/authz.ts`
- `my-app/src/modules/local-mcp/localMcpAdapter.ts`
- `my-app/src/modules/local-mcp/__tests__/localMcp.test.ts`

Current authority classification:

- Internal Tool Contracts: active code. The contracts define the V1 internal tool catalog, allowed effects, risk levels, input kinds, output kinds, active/blocked status, and metadata safety checks.
- Local MCP schema: active code. It defines the local-only request, approval, authorization result, dry-run result, response, and tool-definition shapes.
- Local MCP registry: active code. It builds a deterministic static registry from existing Internal Tool Contracts and exposes only four mapped local tools.
- Local MCP authz: active code. It parses requests, rejects malformed or unauthorized requests with structured reasons, requires user identity, checks the allowlist, and requires approval for exposed medium-risk tools.
- Local MCP dry-run adapter: active code. It returns stable success or refusal responses and echoes cloned arguments into a `local_mcp_dry_run` result without invoking real product handlers.
- Local MCP tests: active tests. They cover deterministic registry output, exact four-tool exposure, internal-contract mapping, approval requirements, stable refusal/success responses, defensive cloning, no product/UI imports, and no remote-host markers.
- PR16 decision doc: active decision record. It explicitly says PR16 is local MCP-shaped only and excludes transport, ChatGPT, OAuth, persistence, UI, routes, Convex functions, external API calls, and real product action execution.
- Controlled ATS public endpoint resolver decision: active decision record. It preserves a narrow known-ATS, public, no-auth, no-scraping distribution boundary and keeps LinkedIn, Upwork, and Indeed forbidden.

No expected decision doc was missing.

## Current local architecture

The PR16 local flow is:

`LocalMcpRequestV1`  
-> `parseLocalMcpRequest`  
-> build or receive `LocalMcpToolRegistryV1`  
-> `getLocalMcpTool`  
-> `authorizeParsedLocalMcpRequest`  
-> `executeLocalMcpRequest`  
-> `LocalMcpResponseV1`

The current local tool allowlist is exactly:

- `application_package.summarize`
- `evidence_graph.summarize`
- `resume_variant_plan.summarize`
- `review_cockpit.summarize`

The local-facing IDs use the `local_mcp.*` prefix and map to those existing Internal Tool Contract IDs. All exposed tools remain dry-run only. The adapter does not execute product mutations, export flows, network calls, persistence writes, or UI route behavior.

## Current invariants from PR16

- read/dry-run only
- explicit allowlist
- approval required
- structured refusal reasons
- no network
- no real actions
- no persistence
- no routes
- no product-module mutation
- rollback by deletion

## Official MCP / Apps SDK surface

Source-grounded notes from official docs:

- MCP tools are server-exposed capabilities that can be discovered and invoked by clients through the protocol.
- Servers with tool support declare a tools capability and respond to `tools/list` with the tools currently available.
- Tool invocation is represented by `tools/call` in MCP. Tool errors that are visible to the model should usually be returned inside the tool result with `isError: true`, not only as protocol-level errors.
- Tool descriptors include names, descriptions, and input schemas. Current OpenAI Apps SDK guidance also expects JSON Schema input and output contracts for well-shaped tools.
- Tool results include `content`; they may also include `structuredContent` for machine-readable results.
- MCP trust and safety guidance expects a human-in-the-loop path, including clear UI around exposed tools and confirmation prompts for operations.
- MCP transport is not just a function call boundary. Standard transports include stdio and Streamable HTTP. Streamable HTTP introduces HTTP method, session, protocol-version, SSE, and resumability concerns.
- MCP Streamable HTTP guidance requires origin validation for incoming connections, recommends localhost binding for local servers, and recommends authentication for all connections.
- MCP authorization for HTTP transports is a transport-level concern and uses OAuth-oriented discovery/protected-resource metadata when a restricted remote server is exposed.
- ChatGPT Apps SDK builds on an MCP server. It expects the server to list tools, accept tool calls, return structured content, and optionally bind returned data to UI components rendered in ChatGPT.

Official sources inspected:

- Model Context Protocol tools spec: [https://modelcontextprotocol.io/specification/2025-06-18/server/tools](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)
- Model Context Protocol transports spec: [https://modelcontextprotocol.io/specification/2025-06-18/basic/transports](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports)
- Model Context Protocol authorization spec: [https://modelcontextprotocol.io/specification/draft/basic/authorization](https://modelcontextprotocol.io/specification/draft/basic/authorization)
- Model Context Protocol schema reference: [https://modelcontextprotocol.io/specification/2025-11-25/schema](https://modelcontextprotocol.io/specification/2025-11-25/schema)
- OpenAI Apps SDK MCP server docs: [https://developers.openai.com/apps-sdk/concepts/mcp-server](https://developers.openai.com/apps-sdk/concepts/mcp-server)
- OpenAI Apps SDK quickstart: [https://developers.openai.com/apps-sdk/quickstart](https://developers.openai.com/apps-sdk/quickstart)
- OpenAI Apps SDK tool planning docs: [https://developers.openai.com/apps-sdk/plan/tools](https://developers.openai.com/apps-sdk/plan/tools)

## Gap analysis

| Area                               | Current PR16 state                                                          | Required before Remote MCP / ChatGPT App                                                                                               | Risk if skipped                                                           | Future PR |
| ---------------------------------- | --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- | --------- |
| MCP tool descriptor projection     | `LocalMcpToolDefinitionV1` exists but is not an MCP descriptor.             | Pure mapper to MCP-compatible names, descriptions, annotations, and schemas.                                                           | Model sees incorrect or unstable tool surface.                            | PR18      |
| JSON Schema for inputs             | Local input kinds exist; no JSON Schema contract exists.                    | Deterministic JSON Schema per tool argument shape.                                                                                     | Invalid or overbroad model arguments reach handlers.                      | PR18      |
| JSON Schema for structured outputs | Output kinds exist; no structured output schema exists.                     | JSON Schema for each `structuredContent` shape.                                                                                        | ChatGPT/UI cannot validate returned machine-readable data.                | PR18      |
| `tools/list`                       | No MCP protocol method exists.                                              | List response projection with stable ordering and allowlist filtering.                                                                 | Remote clients cannot safely discover tools.                              | PR18      |
| `tools/call`                       | Local adapter accepts local request objects only.                           | Protocol envelope that validates tool name, arguments, user/session context, approval, and result shape.                               | Tool calls bypass local safety assumptions.                               | PR19      |
| Error taxonomy                     | Local refusal reasons exist for authz and parsing.                          | MCP-visible error contract covering validation, auth, approval, timeout, rate limit, size limit, privacy filter, and handler failures. | Model and UI cannot recover predictably.                                  | PR19      |
| Approval UX                        | Approval metadata is accepted; no UI or durable approval event exists.      | User-visible confirmation surface and explicit denial/approval states.                                                                 | Model-controlled calls may look user-approved when they are not.          | PR20      |
| Identity propagation               | `userId` string is required locally.                                        | Authenticated user/session identity passed through every envelope and audit event.                                                     | Cross-user data exposure or unverifiable actions.                         | PR20      |
| User/session auth                  | No auth provider or session validation.                                     | Explicit auth boundary before remote access.                                                                                           | Anyone with endpoint access could invoke tools.                           | PR22      |
| Audit logging                      | No persistence or audit log.                                                | Append-only audit event shape for list/call/approval/result/refusal.                                                                   | No investigation trail for sensitive invocations.                         | PR20      |
| Rate limits                        | No limiters.                                                                | Per-user, per-session, per-tool, and global rate limits.                                                                               | Cost, abuse, or availability failures.                                    | PR22      |
| Timeout handling                   | No async handler or timeout policy.                                         | Bounded call duration with cancellation/refusal semantics.                                                                             | Remote calls can hang or exhaust resources.                               | PR22      |
| Tool output size limits            | Dry-run output is small by construction.                                    | Hard limits and truncation/redaction strategy for content and structured output.                                                       | Private or oversized data leaks into model context.                       | PR19      |
| Privacy filtering                  | Local metadata forbids some unsafe terms; no runtime privacy filter exists. | Output sanitizer for private facts, source docs, and public-safe summaries.                                                            | Sensitive profile or source data may be exposed.                          | PR23      |
| `never_use` fact protection        | Not represented in PR16 local MCP.                                          | Enforce canonical fact policy before any tool output can include profile facts.                                                        | Facts explicitly marked unusable could leak.                              | PR23      |
| Private fact protection            | Not represented in PR16 local MCP.                                          | Classify and filter private facts by audience and destination.                                                                         | Private CV/profile details could be exposed to ChatGPT or remote clients. | PR23      |
| Source document redaction          | No source document access in PR16.                                          | Redaction boundary before exposing raw CV, job, proposal, or provenance snippets.                                                      | Raw source documents may leak.                                            | PR23      |
| Real handler boundary              | Adapter returns dry-run result only.                                        | Separate, reviewed handler interface with allowed effects, idempotency, approval, and rollback rules.                                  | Dry-run safety may be lost by direct product-module calls.                | PR21      |
| Rollback/deactivation              | PR16 rollback is deletion-only.                                             | Runtime kill switch and tool deactivation path.                                                                                        | Unsafe remote tool remains callable after incident.                       | PR20      |
| Transport                          | None.                                                                       | Isolated stdio or Streamable HTTP spike after schema, call envelope, approval, and audit contracts exist.                              | Network trust boundary is introduced before local safety is complete.     | PR22      |
| Origin validation                  | None.                                                                       | Validate `Origin` for HTTP transport and define allowed hosts.                                                                         | DNS rebinding or untrusted web-origin access.                             | PR22      |
| OAuth / auth discovery             | None.                                                                       | OAuth/protected-resource metadata and authorization-server discovery plan for restricted remote use.                                   | Remote clients cannot authenticate or consent safely.                     | PR22      |
| Deployment                         | None.                                                                       | Non-production deployment plan, secrets boundary, endpoint exposure policy, and rollback.                                              | Accidental public exposure of unfinished tool server.                     | PR22      |
| Observability                      | None.                                                                       | Structured logs, metrics, alerting, and trace IDs across list/call/approval/result.                                                    | Failures and abuse are invisible.                                         | PR22      |
| Review policy                      | PR16 has tests and decision docs only.                                      | Security, privacy, product, and UX review gates before remote exposure or ChatGPT submission.                                          | Remote integration ships without consent and privacy review.              | PR23      |

## Non-goals

Future work must not include:

- auto-apply
- auto-submit
- auto-send
- LinkedIn scraping
- Upwork scraping
- Indeed scraping
- browser automation
- generic web crawling
- unaudited real action execution
- exporting before approval
- tracking before approval
- broad rewrite of current product flows

## Readiness decision

The system is not ready for Remote MCP or ChatGPT App implementation yet.

The next safe step is MCP schema projection from `LocalMcpToolDefinitionV1` to MCP-compatible descriptors. That step should be pure TypeScript only and must not add transport, deployment, ChatGPT App code, OAuth, persistence, UI, routes, or real handlers.

## Recommended future PR sequence

PR18 - MCP Schema Projection  
Pure TypeScript mapper from `LocalMcpToolDefinitionV1` to MCP-compatible tool descriptors.  
No transport.

PR19 - MCP Call Envelope / Error Contract  
Pure TypeScript request/response envelope and structured error taxonomy.  
No transport.  
No real handlers.

PR20 - Approval + Audit Boundary  
Approval event shell and audit event shape for tool invocation.  
No remote server.  
No deployment.

PR21 - Real Handler Boundary Design  
Define how a local dry-run tool can become a real action safely.  
Docs and pure types only unless explicitly approved.  
No send/apply/submit/export.

PR22 - Remote Transport Spike  
Isolated non-production exploration only.  
No deployment.  
No ChatGPT App submission.

PR23 - ChatGPT App UX / Privacy Spec  
Docs-only UX, consent, privacy, and review policy.

## Security checklist

- every tool is allowlisted
- every real action requires human approval
- no model-controlled send/apply/submit/export
- no raw private source document exposure
- no private facts in public outputs
- no `never_use` facts in outputs
- tool arguments are validated
- tool results are bounded
- output is sanitized
- audit logs are append-only
- users can revoke/deactivate tools
- transport validates origin
- auth is explicit before remote use
- rollback disables tools quickly

## Rollback

This PR is docs-only.

Rollback:

- delete `docs/plans/2026-06-11-mcp-readiness.md`

## Verification

Run:

```
rtk git diff --name-only application-os-foundation...HEAD
rtk git diff --check
rtk git status --short
```

Expected changed files:

```
docs/plans/2026-06-11-mcp-readiness.md
```

No Vitest or TypeScript run is required because this PR is docs-only and must not touch code.