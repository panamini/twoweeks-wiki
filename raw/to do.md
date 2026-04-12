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

`CvForge.tsx` currently exports by calling `printFirstMatchingNodeAsPdf(...)` against the preview container, which means the export source is the rendered preview, not a canonical export serializer built from `CvDocument.sections`.

For your requirements, that should be inverted:

- **canonical structured CV model first**
- then **PDF / DOCX / Markdown / JSON renderers** from that model
- never user-facing export directly from preview DOM
- never user-facing export from raw parser JSON