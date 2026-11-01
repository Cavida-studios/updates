import json
import re
from pathlib import Path

for file in Path('resources').glob('*.json'):
    data = json.loads(file.read_text(encoding='utf-8'))
    assert data['resource'] == file.stem
    assert re.fullmatch(r'[\w-]+', data['resource'])
    assert re.fullmatch(r'\d+\.\d+\.\d+', data['version'])
    assert data['releases'] and data['releases'][0]['version'] == data['version']
    assert Path('changelogs', file.stem + '.md').is_file()
    assert data['url'].startswith('https://github.com/Cavida-studios/updates/')
    assert data['download'].startswith('https://')
    versions = []
    for release in data['releases']:
        assert re.fullmatch(r'\d+\.\d+\.\d+', release['version'])
        assert release['changes'] and all(isinstance(s, str) and s.strip() for s in release['changes'])
        versions.append(tuple(map(int, release['version'].split('.'))))
    assert versions == sorted(set(versions), reverse=True)
print('PASS: public resource metadata and changelogs')
