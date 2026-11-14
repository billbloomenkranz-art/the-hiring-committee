from pathlib import Path
root=Path(__file__).resolve().parents[1]
required=['README.md','CLAUDE.md','identity.md','rules.md','examples.md','reference/company.md','reference/case.md','reference/interaction.md','tests/judge_protocol.md','tests/check_package.py']
missing=[p for p in required if not (root/p).is_file() or not (root/p).read_text().strip()]
assert not missing, f'Missing/empty files: {missing}'
readme=(root/'README.md').read_text()
for name in ['identity.md','rules.md','examples.md','reference/company.md','reference/case.md','reference/interaction.md']:
    assert '`'+name+'`' in readme
assert 'Do not upload' in readme and 'END SESSION' in readme
assert not any((root/p).exists() for p in ['persona','engine','scenarios','PRD.md'])
print('STATIC PASS: clean required layout, no legacy files. Live Claude tests NOT RUN.')