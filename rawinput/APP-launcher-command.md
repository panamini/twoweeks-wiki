Yes — use a **small, repo-local briefing file**.

Best filename:

```text
docs/llm/run-parser-export-brief.md
```

Here is a compact version designed to be cheap for an LLM to read.

````md
# Run / Parser / Export Brief

## Purpose
Small briefing file for humans and LLMs.
Explains the current dev commands, parser runtime modes, and when Docker rebuild is required.

---

## Recommended daily command

```bash
./run.sh tunnel
````

Use this for the normal end-to-end app workflow.

Why:

- stable validated image runtime
    
- import/upload path works
    
- export path works
    
- closest to real deployed behavior
    

---

## Command map

### `./run.sh tunnel`

Stable full workflow.

- parser uses **image runtime**
    
- starts Vite
    
- starts cloudflared
    
- frontend uses `PARSER_ORIGIN` / tunnel path
    
- recommended default command
    

### `./run.sh local`

Local parser mode.

- parser uses **image runtime**
    
- starts Vite
    
- frontend uses `http://127.0.0.1:8001`
    
- uses normal online/default Convex
    
- useful for local parser-backed app work
    

### `./run.sh local-convex`

Advanced local backend mode.

- parser uses **image runtime**
    
- starts Vite
    
- starts local Convex
    
- not the main recommended workflow
    

### `./run.sh parser-dev`

Fast Python parser hacking mode.

- parser uses **workspace-mounted runtime**
    
- `uvicorn --reload`
    
- for parser Python iteration only
    
- not the stable validation/runtime mode
    
- do not use this as the final truth for app behavior
    

### `./run.sh rebuild-docker`

Explicit rebuild command.  
Use this when parser/runtime Python changes must be reflected in stable image mode.

- rebuilds parser/export Docker runtime
    
- restarts parser cleanly
    
- may restore prior mode
    
- verifies readiness
    

### `./run.sh down`

Normal stop.

### `./run.sh reset`

Stronger non-destructive cleanup.

- stops stack
    
- removes stale containers/processes/temp state
    

### `./run.sh status`

Quick stack status.

### `./run.sh logs`

Parser logs.

---

## Core runtime rule

There are 2 parser runtime modes:

### 1. Image runtime

Used by:

- `tunnel`
    
- `local`
    
- `local-convex`
    

Characteristics:

- stable
    
- deployment-like
    
- does **not** pick up Python file edits automatically
    
- requires rebuild after Python/parser changes
    

### 2. Workspace runtime

Used by:

- `parser-dev`
    

Characteristics:

- fast Python iteration
    
- live code reload
    
- good for prompt/schema/parser hacking
    
- not the final stable validation runtime
    

---

## Rebuild rule

If you change parser Python files, including:

- prompt files
    
- schema files
    
- parser logic
    
- export worker/runtime-related Python code
    

then:

### If testing with `parser-dev`

No Docker rebuild needed.

### If testing with `tunnel` / stable image mode

Docker rebuild **is required**.

Use:

```bash
./run.sh rebuild-docker
./run.sh tunnel
```

---

## Best workflows

### A. I just want the app to work

```bash
./run.sh tunnel
```

### B. I am editing parser Python and want fast feedback

```bash
./run.sh parser-dev
```

### C. I changed parser Python and now want real app validation

```bash
./run.sh rebuild-docker
./run.sh tunnel
```

### D. The stack is weird

```bash
./run.sh reset
```

### E. I want to stop everything

```bash
./run.sh down
```

---

## Import vs export note

Import/upload and export can use different backend paths.

Important:

- one path working does not prove all paths are local
    
- `tunnel` is the safest mode for end-to-end validation
    
- `parser-dev` is mainly for direct parser development
    

---

## Export system summary

Exports supported:

- Resume ATS PDF
    
- Resume Styled PDF
    
- Proposal ATS PDF
    
- Proposal Styled PDF
    
- Proposal DOCX
    

Properties:

- direct-download
    
- source-of-truth driven
    
- export does not use preview DOM as content source
    
- Robial governs export geometry
    
- `stylePreset` affects typography/palette/ornament, not page geometry
    

Best validation mode for exports:

```bash
./run.sh tunnel
```

---

## Robial rule

For export layout:

- Robial governs margins, columns, gutters, and page rhythm
    
- `stylePreset` governs typography, palette, emphasis, ornament
    
- `stylePreset` must not change export page geometry
    

---

## Short LLM summary

```text
Recommended command: ./run.sh tunnel

Modes:
- tunnel = stable full workflow
- local = local parser + stable image runtime
- local-convex = advanced local backend mode
- parser-dev = fast Python parser dev with reload
- rebuild-docker = rebuild stable parser/export runtime
- down = stop
- reset = stronger cleanup

Main rule:
- parser-dev sees Python changes immediately
- tunnel/local stable image modes need rebuild after Python changes

Validation rule:
- use tunnel for real end-to-end validation
- use parser-dev for fast parser hacking
```

```

If you want, I can make an even **smaller 30-line version** optimized purely for LLM context windows.
```