#!/usr/bin/env python3
"""Look up publication venues for arXiv ids via the Semantic Scholar batch endpoint."""
import json, sys, time, urllib.request
ax = json.load(open('data/arxiv_raw.json'))
import os
out = json.load(open('data/s2_venues.json')) if os.path.exists('data/s2_venues.json') else {}
ids = [r['id'] for r in ax if r['id'] not in out]
URL = "https://api.semanticscholar.org/graph/v1/paper/batch?fields=venue,year,publicationVenue,journal,externalIds,publicationTypes"
for i in range(0, len(ids), 400):
    chunk = ids[i:i+400]
    body = json.dumps({"ids": ["ARXIV:" + x for x in chunk]}).encode()
    for k in range(6):
        try:
            req = urllib.request.Request(URL, data=body, headers={"Content-Type": "application/json", "User-Agent": "paper-list-builder/1.0"})
            with urllib.request.urlopen(req, timeout=90) as r:
                res = json.loads(r.read())
            break
        except Exception as e:
            print("retry", k, e, file=sys.stderr); time.sleep(8 + 8 * k)
    else:
        print("giving up on chunk", i, file=sys.stderr); res = [None] * len(chunk)
    for x, p in zip(chunk, res):
        if p: out[x] = p
    print("chunk", i, "found", sum(1 for p in res if p), "/", len(chunk), file=sys.stderr)
    time.sleep(4)
json.dump(out, open('data/s2_venues.json', 'w'), ensure_ascii=False)
print("saved", len(out))
