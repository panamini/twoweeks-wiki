---
title: "Proposal AI Routing and Inline Diff"
category: tech
tags: [proposal, ai, routing, qwen, deepseek, mistral, openai, overlay, diff]
created: 2026-05-06
updated: 2026-05-06
status: current
valid_from: 2026-05-06
version: v1
related: [[product/ai-product-model]], [[product/ai-consistency-p0-editor-ai]], [[tech/proposal-style-layer]], [[design/document-token-contract]]
---

# Proposal AI Routing and Inline Diff

This page records the active routing contract for ProposalForge AI and the inline diff overlay used when reviewing selected text in the proposal editor.

## Current Routing

### Proposal generation

- Proposal generation uses OpenAI Responses.
- The default proposal writer model is `gpt-5.5`.
- The writer request uses low reasoning effort and medium text verbosity.
- The proposal form can still be overridden through environment variables, but the visible default remains `chatgpt` when no override is present.
- The request path includes `outputLanguage` from the proposal payload and does not force English-then-translate behavior.

### Editor helper actions

Primary routes:

- `rewrite` -> `qwen-3.6-plus`
- `shorten` -> `qwen-3.6-plus`
- `clarify` -> `qwen-3.6-plus`
- `strengthen` -> `qwen-3.6-plus`
- `expand` -> `qwen-3.6-plus`
- `tailor_to_job` -> `qwen-3.6-plus`
- `custom` -> `qwen-3.6-plus`
- `fix_grammar` -> `qwen-3.6-flash`

Fallback order:

1. Mistral `mistral-small-latest`
2. DeepSeek `DeepSeek V4 Flash`

Provider credentials:

- OpenAI: `OPENAI_API_KEY`
- Qwen: `QWEN_API_KEY` plus `QWEN_CHAT_COMPLETIONS_URL` or `QWEN_BASE_URL`
- DeepSeek: `DEEPSEEK_API_KEY` plus `DEEPSEEK_CHAT_COMPLETIONS_URL` or `DEEPSEEK_BASE_URL`
- Mistral: `MISTRAL_API_KEY`

Match-read synthesis:

- Job summary and keyword match synthesis uses the Ministral/Mistral family.
- The current default model is `ministral-3-3b-instruct-2512`.
- This is separate from proposal generation and editor helper actions.

### Language hardening on proposal output

- Proposal language quality is enforced in two layers:
  - benchmark/eval hardening validates language-specific leakage and unsupported claim patterns in synthetic test runs.
  - production enforcement enforces unsupported exact numeric, duration, credential, ownership, and operational-history claims at runtime.
- The production layer keeps vague timeline language as repair-first (`vague_timeline_claim`) so strong writing is not flattened.
- Source-authorized proof checks use candidate facts only; job-description requirements do not authorize unsupported numeric proof in generated copy.
- This split preserves production behavior while keeping QA coverage for `de`, `ru`, `ar`, and `pl`.

## Inline Diff Overlay

`ProposalDisplay` now renders inline suggestion state inside the active document area instead of using a detached suggestion card for text edits.

Behavior:

- preview state shows struck-through old text and inserted replacement text
- preview actions are `Accept` and `Discard`
- applied state shows `Applied`, `Undo`, and `Close`
- the textarea selection highlight is hidden while the overlay is active
- the overlay text uses the proposal document typography contract
- the action controls stay on the app UI font path

This means the user reviews the edit in the same place where the selection was made.

## Implementation Pointers

- `my-app/config/llmConfig.ts` owns provider defaults, helper routes, and env fallbacks.
- `my-app/convex/lib/editorAi.ts` resolves the helper action policy and provider fallback chain.
- `my-app/convex/generateProposalMutation.ts` handles the proposal writer path.
- `my-app/convex/langchain/models/openai_responses_adapter.ts` wraps OpenAI Responses for proposal generation.
- `my-app/convex/lib/proposals/premiumCoverLetter.ts` keeps the premium writer model resolver on the OpenAI writer contract.
- `my-app/src/components/ProposalInputForm.tsx` reads the env-driven proposal model default.
- `my-app/src/components/ProposalDisplay.tsx` owns the inline proofing overlay and selection lifecycle.
- `my-app/src/styles/product-proposal.css` holds the overlay layout and proofing spans.

## Notes

- `fix_grammar` is not using `qwen-3.6-plus`.
- `fix_grammar` uses `qwen-3.6-flash` first, then Mistral, then DeepSeek.
- Job summary and keyword matching stay on the Ministral/Mistral match-read path.
- Proposal writing still resolves to `gpt-5.5` by default.
