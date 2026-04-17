# How to use the `ingest-wiki` skill

The `ingest-wiki` skill supports four commands:

- `ingest`
- `direct-update`
- `lint`
- `save-output`

## 1. `ingest`

Use `ingest` when you want to process new files staged in `rawinput/`.

### What it does

- reads files from `rawinput/`
- creates or reuses source pages
- updates durable wiki pages
- moves processed files into `raw/`

### Example

```text
ingest the files in rawinput