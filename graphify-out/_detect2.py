import json
from pathlib import Path
from graphify.detect import detect

results = [detect(Path(p)) for p in ('langchain', 'langgraph')]

merged = {
    'scan_root': str(Path('.').resolve()),
    'total_files': sum(r['total_files'] for r in results),
    'total_words': sum(r.get('total_words', 0) for r in results),
    'files': {},
    'skipped_sensitive': [s for r in results for s in (r.get('skipped_sensitive') or [])],
}
cats = ('code', 'document', 'paper', 'image', 'video')
for cat in cats:
    fl = []
    for r in results:
        fl += r.get('files', {}).get(cat, [])
    if fl:
        merged['files'][cat] = fl

Path('graphify-out/.graphify_detect.json').write_text(
    json.dumps(merged, ensure_ascii=False), encoding='utf-8')
print(f"Detected {merged['total_files']} files, ~{merged['total_words']:,} words")
for cat in cats:
    fl = merged['files'].get(cat, [])
    if fl:
        print(f'{cat}: {len(fl)}')
print('skipped_sensitive:', len(merged['skipped_sensitive']))
for s in merged['skipped_sensitive']:
    print(' ', s)
