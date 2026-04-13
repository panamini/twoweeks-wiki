icon  warning is missing in toolbar after import 
i get this wheniclickexport :Trusted Mistral v3 export is unavailable for this CV.


Treat legacy/fallback parsing as non-product code.
Remove it from all normal import, editor, preview, export, and ATS-label flows.
If Mistral v3 non-fallback truth is absent, do not synthesize a fallback resume.
Fail clearly instead.
Legacy/fallback may remain only behind an explicit internal debug gate until deleted.