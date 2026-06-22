# CV Hydration And Style System

## Purpose

This note captures the working boundary that restored the CV decoration image after refresh, and the broader persistence system we are building around CV style, template, and decoration state.

## What Fixed The Image

The image started winning after we proved the live boundary between three layers:

1. profilesPublic.getByProfileId must return a runtime documentDecoration.resolvedUrl for the current assetId.
2. StorageAdapter.mapPersistedProfileToCvDocument must preserve the top-level decoration metadata even when an embedded cvDocument snapshot is stale or invalid.
3. CvLibraryContext must overlay runtime decoration metadata onto the active document when a background refresh is skipped.

The important implementation detail was not rendering assetId directly. The renderer still rejects asset-id-only decorations. The fix was to hydrate resolvedUrl before render state wins.

## What The System Is Doing

The current system is a layered CV persistence model:

1. Durable local state stores the CV document, style metadata, and decoration metadata.
2. Remote Convex state stores the canonical user profile row and the embedded cvDocument snapshot.
3. Public profile reads hydrate runtime-only fields such as documentDecoration.resolvedUrl.
4. The client merges remote state into local state only when the remote version is actually the winning source.
5. Runtime-only image URLs are not persisted back into durable storage.

The style stack is meant to keep these fields synchronized:

- resumeTemplateId
- verbatiStyle
- verbatiStyleBaseSnapshot
- documentStyleVersion
- documentIcons
- documentIconOverrides
- documentDecoration runtime fields

## Why Template And Font Needed A Separate Fix

Image persistence and style persistence are adjacent but not identical.

The image fix solved the decoration boundary, but template and font can still regress if refresh logic compares only document content and not style freshness. If a remote refresh is older for style metadata, it can overwrite the newer local resumeTemplateId or typography choice and make the font drawer feel frozen.

That means the real refresh rule is:

- preserve newer local style metadata when remote content is otherwise equivalent
- only accept remote style state when it is actually fresher or materially different

## Current Remaining Risk

There is still room for a stale remote refresh to interfere with style state if the equality and freshness checks are ordered incorrectly.

The audit boundary to watch is:

- local updatedAt
- remote updatedAt
- remote resumeTemplateId
- remote verbatiStyle.typography
- whether shouldApplyBackgroundRefresh chooses local or remote

## Reusable Proposal Summary

The proposal-safe description is:

“We built a CV persistence pipeline that separates durable document state from runtime hydration. Images are restored by hydrating runtime decoration URLs from Convex before render, while style/template state is preserved by treating local freshness as authoritative when remote content is not actually newer. The system keeps the UI responsive without persisting blob URLs or destabilizing the document model.”