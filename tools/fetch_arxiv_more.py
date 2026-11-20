#!/usr/bin/env python3
"""Second pass: names where JEPA is concatenated (LeJEPA, VJEPA, ...) plus explicit ids."""
import json, sys, time, urllib.parse
sys.path.insert(0, 'tools')
import fetch_arxiv as F
import xml.etree.ElementTree as ET, re

EXTRA_Q = ['all:LeJEPA', 'all:VJEPA', 'all:IJEPA', 'all:JEPAs', 'all:LeWorldModel', 'all:LeWM', 'all:VJEPA2', 'all:"V-JEPA2"', 'all:SIGReg']
IDS = ['2605.26379', '2602.02603']
recs = {r['id']: r for r in json.load(open('data/arxiv_raw.json'))}
before = len(recs)

def ingest(root):
    n = 0
    for e in root.findall('a:entry', F.NS):
        raw = e.find('a:id', F.NS).text
        aid = re.sub(r'v\d+$', '', raw.rsplit('/abs/', 1)[-1])
        if aid in recs: continue
        g = lambda tag: F.norm(getattr(e.find(tag, F.NS), 'text', ''))
        pc = e.find('x:primary_category', F.NS)
        recs[aid] = {'id': aid, 'title': g('a:title'), 'abstract': g('a:summary'), 'published': e.find('a:published', F.NS).text[:10],
                     'updated': e.find('a:updated', F.NS).text[:10], 'authors': [F.norm(a.find('a:name', F.NS).text) for a in e.findall('a:author', F.NS)],
                     'comment': g('x:comment'), 'journal_ref': g('x:journal_ref'), 'doi': g('x:doi'),
                     'primary': pc.attrib.get('term') if pc is not None else '', 'cats': [c.attrib.get('term') for c in e.findall('a:category', F.NS)],
                     'via': 'second-pass'}
        n += 1
    return n

for q in EXTRA_Q:
    start, total = 0, None
    while total is None or start < total:
        url = F.API + '?' + urllib.parse.urlencode({'search_query': q, 'start': start, 'max_results': 200, 'sortBy': 'submittedDate', 'sortOrder': 'descending'})
        root = ET.fromstring(F.get(url))
        total = int(root.find('o:totalResults', F.NS).text)
        new = ingest(root)
        print(f'{q}: {min(start + 200, total)}/{total}, new {new}, unique {len(recs)}', file=sys.stderr)
        start += 200
        time.sleep(3.2)
root = ET.fromstring(F.get(F.API + '?' + urllib.parse.urlencode({'id_list': ','.join(IDS), 'max_results': 10})))
print('ids: new', ingest(root), file=sys.stderr)
json.dump(sorted(recs.values(), key=lambda r: r['id']), open('data/arxiv_raw.json', 'w'), ensure_ascii=False, indent=1)
print('arxiv records:', before, '->', len(recs))
new = [r for r in recs.values() if r.get('via') == 'second-pass']
for r in sorted(new, key=lambda r: r['id'])[:400]:
    print(r['id'], '|', r['title'][:90])
