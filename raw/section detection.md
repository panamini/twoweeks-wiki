### Future implementation note

The current stabilization scope should remain intentionally narrow.

For the first implementation, deterministic OCR-markdown recovery should be limited to section types that are strongly section-local and low-risk to reconstruct from explicit markdown headings and list content, specifically:

- `languages`
- `skills`
- existing `achievements` repair path

This is appropriate because these fields are represented as relatively atomic values in the extraction schema and can be validated with bounded sanity checks.

Broader deterministic recovery for additional resume sections should be treated as a future enhancement, not part of the initial stabilization patch.

Potential future candidates include:

- `hobbies`
- `affiliations`
- `additionalInformation`

These sections may be recoverable from explicit OCR markdown headings with bounded list-oriented extraction, but should be added only after the initial stabilization work is validated in repeated audit runs.

Complex structured sections should not receive first-pass deterministic reconstruction in the initial rollout. This includes:

- `experience`
- `education`
- `projects`
- `certifications`
- `volunteering`
- `awards`
- `publications`

These sections contain richer semantics such as dates, nested bullets, descriptions, role metadata, and reclassification rules, and are therefore better handled by the existing annotation + normalization pipeline rather than by broad markdown heuristics in the first stabilization phase.

If future reliability work expands beyond `languages` and `skills`, the recommended order is:

1. add section-specific acceptance checks
2. add bounded deterministic recovery only for sections with explicit headings and low semantic ambiguity
3. validate with repeated fixture audits before expanding to additional section families

The goal of the first stabilization pass is to improve correctness without creating a second full parser alongside the annotation pipeline. Future expansion should preserve that constraint.