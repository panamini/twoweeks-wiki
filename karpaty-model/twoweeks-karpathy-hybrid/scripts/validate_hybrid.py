#!/usr/bin/env python3
from pathlib import Path
import json
import csv
import sys

ROOT = Path(__file__).resolve().parent.parent

required_paths = [
    ROOT / "README.md",
    ROOT / "WIKI_SCHEMA.md",
    ROOT / "CLAUDE.md",
    ROOT / "EXAMPLES.md",
    ROOT / "skills" / "ingest-wiki" / "SKILL.md",
    ROOT / ".claude-plugin" / "plugin.json",
    ROOT / ".claude-plugin" / "marketplace.json",
    ROOT / "audit" / "benchmark-matrix.csv",
    ROOT / "audit" / "benchmark-summary.json",
    ROOT / "audit" / "hybrid-audit-report.md",
]

missing = [str(p.relative_to(ROOT)) for p in required_paths if not p.exists()]

summary_path = ROOT / "audit" / "benchmark-summary.json"
benchmark_path = ROOT / "audit" / "benchmark-matrix.csv"

errors = []

if summary_path.exists():
    summary = json.loads(summary_path.read_text())
    if summary.get("weights_total") != 100:
        errors.append(f"weights_total expected 100, got {summary.get('weights_total')}")
else:
    errors.append("benchmark-summary.json missing")

if benchmark_path.exists():
    with benchmark_path.open() as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    if len(rows) < 5:
        errors.append("benchmark-matrix.csv unexpectedly short")
else:
    errors.append("benchmark-matrix.csv missing")

if missing:
    print("MISSING FILES:")
    for item in missing:
        print(f"- {item}")

if errors:
    print("VALIDATION ERRORS:")
    for item in errors:
        print(f"- {item}")

if not missing and not errors:
    print("VALIDATION OK")
    print(f"Checked {len(required_paths)} required paths.")
    sys.exit(0)

sys.exit(1)
