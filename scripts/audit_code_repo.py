#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

IGNORE_DIRS = {
    '.git',
    '.hg',
    '.svn',
    'node_modules',
    '.next',
    '.turbo',
    'dist',
    'build',
    'coverage',
    '.venv',
    'venv',
    '__pycache__',
    '.mypy_cache',
    '.pytest_cache',
    '.idea',
    '.vscode',
    '.obsidian',
    '.makemd',
    '.space',
    '.claude-plugin',
    'raw',
    'rawinput',
    'wiki',
    'Tags',
}
NON_APP_PREFIXES = ('scripts/', 'references/', 'audit/')
SOURCE_ROOTS = ['src', 'app', 'lib', 'packages', 'services', 'server', 'client']
TEST_ROOTS = ['tests', '__tests__', 'spec', 'specs']
MANIFESTS = ['package.json', 'pyproject.toml', 'Cargo.toml', 'go.mod', 'pom.xml', 'build.gradle', 'requirements.txt']
LINT_FILES = ['.eslintrc', '.eslintrc.json', '.eslintrc.js', 'ruff.toml', 'pyproject.toml', '.prettierrc', 'mypy.ini']
DOCS_FILES = ['README.md', 'AGENTS.md', 'CLAUDE.md', 'WIKI_SCHEMA.md', 'EXAMPLES.md', 'IMPLEMENTATION_RULES.md']
CODE_EXTS = {'.py', '.pyi', '.js', '.jsx', '.ts', '.tsx', '.go', '.rs', '.java', '.kt', '.rb', '.php', '.c', '.cc', '.cpp', '.h', '.hpp', '.cs'}
TEST_PATTERNS = ['test_', '_test', '.spec.', '.test.']


def should_skip(path: Path) -> bool:
    return any(part in IGNORE_DIRS for part in path.parts)


def walk_files(root: Path):
    for path in root.rglob('*'):
        if should_skip(path):
            continue
        if path.is_file():
            yield path


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding='utf-8')
    except Exception:
        return ''


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('root', nargs='?', default='.')
    parser.add_argument('--json', dest='json_path')
    parser.add_argument('--markdown', dest='md_path')
    args = parser.parse_args()

    root = Path(args.root).resolve()
    files = list(walk_files(root))

    manifests = [str(path.relative_to(root)) for path in files if path.name in MANIFESTS]
    source_roots = [name for name in SOURCE_ROOTS if (root / name).exists()]
    test_roots = [name for name in TEST_ROOTS if (root / name).exists()]
    workflows = [str(path.relative_to(root)) for path in files if '.github/workflows' in str(path.relative_to(root)).replace('\\', '/')]
    lint_files = [str(path.relative_to(root)) for path in files if path.name in LINT_FILES]
    docs = [str(path.relative_to(root)) for path in files if path.name in DOCS_FILES]
    skill_files = [str(path.relative_to(root)) for path in files if 'skills' in path.parts and path.name == 'SKILL.md']

    code_files = []
    test_files = []
    ext_counter = Counter()
    for path in files:
        rel = str(path.relative_to(root))
        ext = path.suffix.lower()
        ext_counter[ext] += 1
        if ext in CODE_EXTS:
            code_files.append(rel)
            low = rel.lower()
            if any(token in low for token in TEST_PATTERNS):
                test_files.append(rel)

    combined_rules = '\n'.join(
        [
            read_text(root / 'AGENTS.md'),
            read_text(root / 'CLAUDE.md'),
            read_text(root / 'EXAMPLES.md'),
            read_text(root / 'IMPLEMENTATION_RULES.md'),
            '\n'.join(read_text(root / rel) for rel in skill_files),
        ]
    ).lower()

    non_overlay_code_files = [
        rel
        for rel in code_files
        if not any(rel.startswith(prefix) for prefix in NON_APP_PREFIXES)
    ]
    actual_code_repo_present = bool(manifests or source_roots or test_roots or workflows or len(non_overlay_code_files) >= 5)
    has_preflight = all(key in combined_rules for key in ['goal:', 'assumptions:', 'smallest safe change:', 'verification:'])
    has_simplicity = 'simplicity' in combined_rules or 'minimum change' in combined_rules or 'minimum code' in combined_rules
    has_surgical = 'surgical' in combined_rules or 'touch only what the request requires' in combined_rules or 'every changed line' in combined_rules
    has_verification = 'verification matrix' in combined_rules or 'verify' in combined_rules
    has_repo_discovery_order = (
        ('manifest' in combined_rules or 'package.json' in combined_rules or 'pyproject.toml' in combined_rules)
        and 'test' in combined_rules
        and ('ci' in combined_rules or 'lint' in combined_rules or 'build' in combined_rules)
        and (
            'owning module' in combined_rules
            or 'owner module' in combined_rules
            or 'entrypoint' in combined_rules
            or 'smallest source module' in combined_rules
        )
    )

    language_counts = {ext: count for ext, count in ext_counter.most_common() if ext and count >= 1}
    primary_languages = [ext for ext, _count in ext_counter.most_common(6) if ext in CODE_EXTS][:5]

    result = {
        'root': str(root),
        'actual_code_repo_present': actual_code_repo_present,
        'manifests': manifests,
        'source_roots': source_roots,
        'test_roots': test_roots,
        'workflow_files': workflows,
        'lint_files': lint_files,
        'docs_files': docs,
        'skill_files': skill_files,
        'code_file_count': len(code_files),
        'non_overlay_code_file_count': len(non_overlay_code_files),
        'test_file_count': len(test_files),
        'primary_languages': primary_languages,
        'language_extension_counts': language_counts,
        'rules': {
            'has_preflight': has_preflight,
            'has_simplicity_guardrail': has_simplicity,
            'has_surgical_rule': has_surgical,
            'has_verification_contract': has_verification,
            'has_repo_discovery_order': has_repo_discovery_order,
        },
        'gaps': [],
        'strengths': [],
    }

    if has_preflight:
        result['strengths'].append('Non-trivial work is gated by an explicit preflight template.')
    else:
        result['gaps'].append('Missing explicit Goal/Assumptions/Smallest safe change/Verification preflight.')

    if has_simplicity:
        result['strengths'].append('Rules explicitly pressure the model toward minimum viable changes.')
    else:
        result['gaps'].append('Missing explicit anti-bloat / simplicity guidance.')

    if has_surgical:
        result['strengths'].append('Rules explicitly constrain diff scope.')
    else:
        result['gaps'].append('Missing surgical-diff guidance.')

    if has_verification:
        result['strengths'].append('Verification is part of the contract, not an afterthought.')
    else:
        result['gaps'].append('Missing explicit verification contract.')

    if has_repo_discovery_order:
        result['strengths'].append('Read order identifies manifests, tests, CI, and the owning module before broader exploration.')
    else:
        result['gaps'].append('Missing explicit code-plane discovery order in the write-time contract.')

    if not manifests:
        result['gaps'].append('No build/dependency manifest detected.')
    if not source_roots and len(non_overlay_code_files) < 5:
        result['gaps'].append('No substantial application source tree detected in common source roots.')
    if not test_roots and len(test_files) == 0:
        result['gaps'].append('No test roots or obvious test files detected.')
    if not workflows:
        result['gaps'].append('No CI workflow files detected.')
    if not skill_files:
        result['gaps'].append('No reusable skill files detected.')

    markdown_lines = []
    markdown_lines.append('# Code Repo Audit')
    markdown_lines.append('')
    markdown_lines.append(f'- Root: `{root}`')
    markdown_lines.append(f'- Actual code repo present: `{actual_code_repo_present}`')
    markdown_lines.append(f'- Manifests: `{len(manifests)}`')
    markdown_lines.append(f'- Source roots: `{", ".join(source_roots) if source_roots else "none"}`')
    markdown_lines.append(f'- Test roots: `{", ".join(test_roots) if test_roots else "none"}`')
    markdown_lines.append(f'- CI workflows: `{len(workflows)}`')
    markdown_lines.append(f'- Code files: `{len(code_files)}`')
    markdown_lines.append(f'- Non-overlay code files: `{len(non_overlay_code_files)}`')
    markdown_lines.append(f'- Test-like files: `{len(test_files)}`')
    markdown_lines.append('')
    markdown_lines.append('## Strengths')
    if result['strengths']:
        for item in result['strengths']:
            markdown_lines.append(f'- {item}')
    else:
        markdown_lines.append('- None detected')
    markdown_lines.append('')
    markdown_lines.append('## Gaps')
    if result['gaps']:
        for item in result['gaps']:
            markdown_lines.append(f'- {item}')
    else:
        markdown_lines.append('- None detected')
    markdown_lines.append('')
    markdown_lines.append('## Inventory')
    markdown_lines.append(f'- Manifests: {manifests or ["none"]}')
    markdown_lines.append(f'- Workflows: {workflows or ["none"]}')
    markdown_lines.append(f'- Lint files: {lint_files or ["none"]}')
    markdown_lines.append(f'- Docs files: {docs or ["none"]}')
    markdown_lines.append(f'- Skill files: {skill_files or ["none"]}')

    if args.json_path:
        Path(args.json_path).write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    if args.md_path:
        Path(args.md_path).write_text('\n'.join(markdown_lines) + '\n', encoding='utf-8')
    if not args.json_path and not args.md_path:
        print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
