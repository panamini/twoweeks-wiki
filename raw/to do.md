-

the page im in is name weirdly this instead of adapting to the new parsing cv name when i import a cv name shoudl change not keep the same old one
-modifier le add ur own section pour qu'il fasse partie du vrai blockrenderer comme summary ou EXPERIENCE, d'ailleur le add ur own permettra de choisir d'ajouter un section type skill , experience, summary. 
pour l'instant il a une legacy section nested , verifier que les autrees sections n'ont pas le meme probleme, hobbies should be like skill section remove exsitaning and replce,projects(become experience sections tye) ,additional information(become section summary style) ,hobbies(become skill style)

achivment is present still in manage section eventhough its already loaded

**asking Codex to make synthetic CVs**



make the resume is one page, add a mod e cv multipage, or froce one page. 



pdf export react 

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