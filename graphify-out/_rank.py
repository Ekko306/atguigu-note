import json
from pathlib import Path
from collections import Counter

d = json.loads(Path('graphify-out/.graphify_detect.json').read_text(encoding='utf-8'))
root = d['scan_root'].replace('\\', '/').rstrip('/')
skipped = d.get('skipped_sensitive') or []
print('SKIPPED_SENSITIVE:')
for s in skipped:
    print(' ', s)

allf = []
for cat in ('code', 'document', 'paper', 'image', 'video'):
    allf += d['files'].get(cat, [])

c = Counter()
for f in allf:
    norm = f.replace('\\', '/')
    if norm.startswith(root + '/graphify-out/'):
        continue
    if norm.startswith(root):
        rel = norm[len(root) + 1:]
    else:
        rel = norm
    parts = rel.split('/')
    c[parts[0] if len(parts) > 1 else '(root)'] += 1

print('TOP_SUBDIRS:')
for k, v in c.most_common(8):
    print(f'  {v:4d}  {k}')
