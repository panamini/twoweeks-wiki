the import ocr pdf txt button

- Mistral button path: `StructuredUploadButton.tsx` → `api.actions.structuredUpload.structuredUpload` → `my-app/convex/actions/structuredUpload.ts` → `canonicalizeParserResult(...)` → `my-app/convex/lib/parsing/canonicalize.ts` / `canonicalizeExperience(...)` → parser target `/mistral-ocr/parse`
- Source of truth: frontend local, Convex cloud/default, parser base `https://parser.dasti.ai`, launch path `./run.sh up --ui`
- Current active diagnostic boundary: `canonicalizeExperience(...)`
- Warning: `structuredUpload.ts` is the wrapper/action path, not the source-selection decision point