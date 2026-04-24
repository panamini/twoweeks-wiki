


Le repo teste surtout l’application via **Vitest** dans `my-app`, avec **JSDOM** et **Testing Library** (`@testing-library/react`, `jest-dom`, `user-event`) comme base du système de test .  
La commande principale est `npm run test`, qui lance `vitest --run --exclude pdf-ingest/*`, avec un mode watch séparé `npm run test:watch` .

Les tests sont répartis à la fois dans `src/__tests__` et au plus près des domaines, par exemple dans `src/hooks/__tests__`, `src/components/__tests__`, `src/pages/__tests__`, `src/contexts/__tests__`, ainsi que dans `convex/lib/.../__tests__` pour certaines logiques côté parsing .  
Il y a donc une vraie base de tests, mais l’organisation est un peu hybride entre centralisation et colocalisation.

Côté couverture, le repo teste surtout :

- la **logique métier CV** et la normalisation des données,
    
- les **hooks** et **providers**,
    
- les **flows UI** importants,
    
- les comportements asynchrones comme polling, persistance locale et handoff d’état.  
    On le voit par exemple dans `v1.normalize.dates.test.ts`, `canonicalize.test.ts`, `useCvParser.test.tsx`, `CvLibraryContext.test.tsx`, `SectionEditor.cv-ai.test.tsx` ou `ProposalForge.handoff-continuity.test.tsx` .
    

Le système repose beaucoup sur des **mocks ciblés**. Les dépendances les plus souvent simulées sont `convex/react`, `@clerk/clerk-react`, `fetch`, `localStorage`, ainsi que plusieurs éléments de runtime navigateur. Le fichier central pour ça est `src/setupTests.ts`, complété par `src/test/setup.ts` pour le nettoyage des timers .  
En pratique, ce setup global est un point clé à lire avant toute contribution, car il définit l’environnement réel d’exécution des tests.

Le style implicite des tests est assez clair : on teste surtout le **comportement observable**, on privilégie les requêtes accessibles (`getByRole`, `findByRole`, `getByLabelText`), et on nettoie explicitement mocks et timers pour garder une suite stable .  
Ce n’est pas une suite orientée “snapshot” ou simple structure DOM ; elle vise plutôt les vrais flux applicatifs.

Il existe aussi une infra **Playwright** à la racine avec `pw:test` et une config multi-navigateurs, mais dans l’état visible du dépôt, la partie E2E semble encore très légère : le test repéré est surtout un exemple standard Playwright, pas une vraie couverture métier du produit .

En résumé : le repo a une **bonne base de tests front et métier**, surtout sur la logique CV, les hooks, les providers et les flows UI critiques. Le point le plus faible visible aujourd’hui n’est pas la qualité des tests existants, mais plutôt la **faible couverture E2E produit** et une **organisation un peu hétérogène** des fichiers de test.

