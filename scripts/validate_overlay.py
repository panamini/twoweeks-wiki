#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

REQUIRED = [
    'README.md',
    'WIKI_SCHEMA.md',
    'CLAUDE.md',
    'AGENTS.md',
    'IMPLEMENTATION_RULES.md',
    'EXAMPLES.md',
    'SKILL.md',
    'skills/ingest-wiki/SKILL.md',
    'skills/apply-hybrid-code-layer/SKILL.md',
    'scripts/audit_code_repo.py',
    'scripts/score_code_repo.py',
    'audit/code-benchmark-criteria.csv',
]
KEY_PHRASES = {
    'CLAUDE.md': ['Goal:', 'Assumptions:', 'Smallest safe change:', 'Verification:', 'Surgical changes'],
    'AGENTS.md': ['compatibility shim', 'CLAUDE.md'],
    'SKILL.md': ['Goal:', 'Assumptions:', 'Smallest safe change:', 'Verification:'],
    'IMPLEMENTATION_RULES.md': ['Bug fix', 'Feature', 'Refactor', 'Performance'],
    'skills/apply-hybrid-code-layer/SKILL.md': ['repo-audit', 'implement', 'benchmark', 'save-output'],
}


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    missing = [rel for rel in REQUIRED if not (root / rel).exists()]
    phrase_failures = []

    for rel, phrases in KEY_PHRASES.items():
        path = root / rel
        text = path.read_text(encoding='utf-8') if path.exists() else ''
        for phrase in phrases:
            if phrase not in text:
                phrase_failures.append(f'{rel}: missing phrase {phrase!r}')

    root_skill = root / 'SKILL.md'
    nested_skill = root / 'skills' / 'ingest-wiki' / 'SKILL.md'
    if root_skill.exists() and nested_skill.exists():
        if root_skill.read_text(encoding='utf-8') != nested_skill.read_text(encoding='utf-8'):
            phrase_failures.append('SKILL.md and skills/ingest-wiki/SKILL.md diverged')

    if missing or phrase_failures:
        print('VALIDATION FAILED')
        if missing:
            print('Missing files:')
            for item in missing:
                print(f'- {item}')
        if phrase_failures:
            print('Phrase failures:')
            for item in phrase_failures:
                print(f'- {item}')
        raise SystemExit(1)

    print('VALIDATION PASSED')


if __name__ == '__main__':
    main()
