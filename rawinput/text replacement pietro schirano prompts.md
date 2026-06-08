
absorb this code deeply , truly understand how it works, soak in the code and the features

-------

actually imaginge you're writing an instruction msg for a junior developer to go work  on this, can  you wwrite somthing extremly clear and specific (including what files to look at for the change and what ones need to be fixed) for them ? 

---------------------------------

Remember, you are an agent - please keep going until the user's query is completely resolved, before ending your turn and yielding back to the user. Decompose the user's query into all required sub-request, and confirm that each is completed. Do not stop after completing only part of the request. Only terminate your turn when you are sure that the problem is solved. You must be prepared to answer multiple queries and only finish the call once the user has confirmed they're done. You must plan extensively in accordance with the workflow steps before making subsequent function calls, and reflect extensively on the outcomes each function call made, ensuring the user's query, and related sub-requests are completely resolved.

-------
Spawn multiple agents in parallel — as many as you need to accomplish this task better and faster. Break the work into independent pieces, dispatch them concurrently, and synthesize the results when they return.

----
I'm working on branch A and want to bring in changes from branch B without regressions. Don't merge B directly into A. Instead: (1) create a new branch off A, (2) cherry-pick or port only the changes from B that we actually want, (3) verify nothing in A regressed (run tests, review the diff), (4) then open a PR from that new branch into A. Keep A clean — only the diff from B should land on the new branch, and only push that new branch

----

Explain what this code does, why it's structured this way, and any non-obvious behavior. Be concise.

----
Review the recent code we wrote for potential bugs, regressions, edge cases, and side effects on functionality. List everything risky and explain the impact before we move on — don't fix anything.

--
## Version finale que je te conseille

```
scope 
Before editing anything, restate the exact scope, likely files involved, what must not change, and acceptance criteria. Do not broaden the task.
```

```
review
Review this like a senior engineer. Inspect the current diff and relevant source. Findings first, ordered by severity. Focus on regressions, edge cases, missing tests, unrelated changes, and architecture drift. Do not rewrite unless needed.
```

```
boundary
Debug the live boundary. State the contradiction, list likely boundaries, choose one, add one narrow temporary diagnostic, run the real workflow, prove which path wins, patch only that boundary, verify again, then remove the diagnostic.
```

```
patch
Implement the smallest safe patch for the confirmed issue. Do not refactor, redesign, rename, or touch adjacent features unless strictly required. Preserve behavior outside the target issue.
```

```
verify
Verify the real result, not just the implementation. Run relevant build/typecheck/lint/tests and inspect the actual UI/output when relevant. Report commands, pass/fail, before/after behavior, diff summary, and remaining risks.
```

```
source
Before coding, inspect the real source files, SDK, package, or upstream repo that defines this behavior. Do not guess API names or install replacement packages. Report the files/functions/examples used as reference.
```

```
diff
Inspect the current diff. Explain what changed, what risk it introduces, what looks unrelated, whether it should be split, and what checks are missing.
```

```
testfix
Add or update the smallest focused regression test that would fail before this fix and pass after it. Keep it local to the changed behavior. Avoid broad snapshots or unrelated coverage.
```

```
handoff
Write a cold-start handoff: current state, goal, files touched, decisions, commands run, pass/fail, remaining risks, next smallest step, and rollback notes.
```

```
cleanup
The feature/fix works. Now clean only the touched area. Extract repeated mechanics into small service-layer helpers. Keep domain policy in callers. Do not change user-facing behavior.
```
---
handoff
Write a concise cold-start handoff document so a fresh agent can continue the current work without rereading the full conversation. Save it as Markdown in the temporary directory of the user’s OS, not the current workspace/repo, and do not modify project files. If arguments are provided, treat them as the next-session focus. Redact secrets and unnecessary personal data. Do not duplicate content already captured in PRDs, plans, ADRs, issues, commits, diffs, branches, uploads, or prior handoffs; reference them by path, URL, branch, commit, issue, PR, or filename. Use only known facts; write Unknown instead of guessing. Include: current state, goal, constraints/do-not-change, relevant artifacts, files touched, decisions made, commands run, validation pass/fail/unknown, remaining risks, suggested skills to invoke, next smallest step, and rollback notes. End by printing the absolute handoff file path and a 3-bullet summary.

----

look for my text replacement s in the keyboard and add suggests a few new ones

