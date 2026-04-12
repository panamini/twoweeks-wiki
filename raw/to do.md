-modifier le add ur own section pour qu'il fasse partie du vrai blockrenderer comme summary ou EXPERIENCE, d'ailleur le add ur own permettra de choisir d'ajouter un section type skill , experience, summary. 
pour l'instant il a une legacy section nested , verifier que les autrees sections n'ont pas le meme probleme, hobbies should be like skill section remove exsitaning and replce,projects(become experience sections tye) ,additional information(become section summary style) ,hobbies(become skill style)

achivment is present still in manage section eventhough its already loaded

**asking Codex to make synthetic CVs**


bouton import pdf txt qui branche depuis structureupload, est ce qu'on en fait un fallback si mistral marche pas ? ou on le surprpime ? en tout cas je veux le supprimer de l'ui


—  
Ajoutez **Download raw** **.md** et **Download normalized** **.json**.  
make the resume and cv ATS compliants, the resume is onoe page, add a mod e cv multipage, or froce one page. 





pdf export react 
### ) The current export entrypoint is still preview-driven
The biggest blocker is the PDF path:

- current PDF = preview DOM → `html2canvas` → PNG slices → `jsPDF`
- required PDF = canonical model → text-first PDF renderer
`CvForge.tsx` currently exports by calling `printFirstMatchingNodeAsPdf(...)` against the preview container, which means the export source is the rendered preview, not a canonical export serializer built from `CvDocument.sections`.

For your requirements, that should be inverted:

- **canonical structured CV model first**
- then **PDF / DOCX / Markdown / JSON renderers** from that model
- never user-facing export directly from preview DOM
- never user-facing export from raw parser JSON
  
  Assuming you want this branch truly clean and reviewable, the intentional scope should be roughly:

- `my-app/package.json`
- lockfile
- one new canonical export serialization module
- one PDF renderer from canonical export model
- one DOCX renderer from canonical export model
- one Markdown renderer from canonical export model
- one normalized JSON exporter
- `my-app/src/components/ProfileReviewCard.tsx`
- `my-app/src/pages/CvForge.tsx`
- focused export tests

And **not** unrelated parser/import behavior or unrelated toolbar/UI cleanups.

---

## ATS rules I would enforce in code/templates

These should be hardcoded in the export layer, not left to preview styling:

- single-column only
- no tables
- no sidebars
- no icons, graphics, charts, skill bars, timelines, decorative widgets
- no essential info in headers/footers
- standard section headings only
- deterministic section/text order
- simple bullets only
- no duplicate bullets / repeated sentences
- ATS-safe date formatting like `MMM YYYY – MMM YYYY` and `Present`
- DOCX default font: **Arial**
- PDF default font: **Helvetica** or equivalent sans-serif
- body: **11 pt**
- contact line: **10.5–11 pt**
- section headings: **15–16 pt bold**
- candidate name: **24–28 pt bold**
- restrained spacing, black/dark neutral text only
- recruiter-safe filenames
- no preview palette / accent inheritance in ATS export mode