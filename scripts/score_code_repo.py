#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def load_audit(path: Path) -> dict:
    return json.loads(path.read_text(encoding='utf-8'))


def score_from_audit(audit: dict, root: Path) -> dict:
    rules = audit.get('rules', {})
    manifests = audit.get('manifests', [])
    source_roots = audit.get('source_roots', [])
    test_roots = audit.get('test_roots', [])
    workflow_files = audit.get('workflow_files', [])
    skill_files = audit.get('skill_files', [])
    docs_files = audit.get('docs_files', [])
    code_count = audit.get('non_overlay_code_file_count', audit.get('code_file_count', 0))
    test_count = audit.get('test_file_count', 0)

    scores = {}
    scores['ambiguity_preflight'] = 5 if rules.get('has_preflight') else 1
    scores['simplicity_guardrail'] = 5 if rules.get('has_simplicity_guardrail') else 1
    scores['surgical_diff_discipline'] = 5 if rules.get('has_surgical_rule') else 1
    scores['verification_contract'] = 5 if rules.get('has_verification_contract') else 1
    scores['repo_discovery_order'] = 5 if rules.get('has_repo_discovery_order') else 1
    scores['examples_and_onboarding'] = 5 if 'EXAMPLES.md' in docs_files else 2
    scores['portability_and_skills'] = 2 if skill_files else 1

    if code_count >= 20 and source_roots:
        scores['actual_source_structure'] = 5
    elif code_count >= 5 or source_roots:
        scores['actual_source_structure'] = 3
    else:
        scores['actual_source_structure'] = 0

    if test_count >= 5 or test_roots:
        scores['tests_near_behavior'] = 5
    elif test_count >= 1:
        scores['tests_near_behavior'] = 3
    else:
        scores['tests_near_behavior'] = 0

    if workflow_files:
        scores['ci_lint_build'] = 5
    else:
        scores['ci_lint_build'] = 1 if manifests else 0

    has_audit_script = (root / 'scripts' / 'audit_code_repo.py').exists()
    has_score_script = (root / 'scripts' / 'score_code_repo.py').exists()
    if has_audit_script and has_score_script:
        scores['benchmark_repeatability'] = 5
    elif has_audit_script or has_score_script:
        scores['benchmark_repeatability'] = 2
    else:
        scores['benchmark_repeatability'] = 0

    if (root / 'audit').exists() and 'IMPLEMENTATION_RULES.md' in docs_files:
        scores['artifact_reporting'] = 5
    elif (root / 'audit').exists():
        scores['artifact_reporting'] = 3
    else:
        scores['artifact_reporting'] = 1

    return scores


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('root', nargs='?', default='.')
    parser.add_argument('--audit-json', dest='audit_json')
    parser.add_argument('--criteria', default='audit/code-benchmark-criteria.csv')
    parser.add_argument('--output', default='audit/live-score-summary.json')
    args = parser.parse_args()

    root = Path(args.root).resolve()
    audit_path = Path(args.audit_json) if args.audit_json else root / 'audit' / 'live-code-audit.json'
    criteria_path = root / args.criteria if not Path(args.criteria).is_absolute() else Path(args.criteria)
    output_path = root / args.output if not Path(args.output).is_absolute() else Path(args.output)

    audit = load_audit(audit_path)
    raw_scores = score_from_audit(audit, root)

    weighted_total = 0.0
    weight_sum = 0.0
    instruction_total = 0.0
    instruction_weights = 0.0
    repo_total = 0.0
    repo_weights = 0.0
    criteria_rows = []

    with criteria_path.open(encoding='utf-8') as handle:
        for row in csv.DictReader(handle):
            criterion = row['criterion']
            weight = float(row['weight'])
            dimension = row['dimension']
            score = float(raw_scores.get(criterion, 0))
            weighted_points = (score / 5.0) * weight
            criteria_rows.append(
                {
                    'criterion': criterion,
                    'dimension': dimension,
                    'weight': weight,
                    'score_0_to_5': score,
                    'weighted_points': round(weighted_points, 2),
                }
            )
            weighted_total += weighted_points
            weight_sum += weight
            if dimension == 'instruction':
                instruction_total += weighted_points
                instruction_weights += weight
            else:
                repo_total += weighted_points
                repo_weights += weight

    summary = {
        'root': str(root),
        'full_score_pct': round((weighted_total / weight_sum) * 100 if weight_sum else 0, 2),
        'instruction_layer_score_pct': round((instruction_total / instruction_weights) * 100 if instruction_weights else 0, 2),
        'repo_evidence_score_pct': round((repo_total / repo_weights) * 100 if repo_weights else 0, 2),
        'criteria': criteria_rows,
        'notes': [
            'Instruction-layer score reflects the quality of the repo rules, skills, and reporting contract.',
            'Repo-evidence score reflects the actual presence of manifests, source roots, tests, and CI in the target tree.',
        ],
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(summary, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
