#!/usr/bin/env python3
from pathlib import Path
import csv
import json

ROOT = Path(__file__).resolve().parent.parent
benchmark_path = ROOT / "audit" / "benchmark-matrix.csv"
rows = list(csv.DictReader(benchmark_path.open()))

def total_for(column):
    score = 0.0
    total_weight = 0
    for row in rows:
        weight = int(row["weight"])
        total_weight += weight
        score += weight * (int(row[column]) / 5)
    return round(score, 2), total_weight

tw, w1 = total_for("twoweeks_score")
kar, w2 = total_for("karpathy_score")
hyb, w3 = total_for("hybrid_score")

summary = {
    "weights_total": w1,
    "totals": {
        "twoweeks_baseline": tw,
        "karpathy_baseline": kar,
        "hybrid_target": hyb,
    },
    "scale": "0-100 weighted score, each criterion scored 1-5 and normalized by weight",
}

out_path = ROOT / "audit" / "benchmark-summary.json"
out_path.write_text(json.dumps(summary, indent=2) + "\n")
print(json.dumps(summary, indent=2))
