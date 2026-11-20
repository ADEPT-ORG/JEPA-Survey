#!/usr/bin/env python3
"""Fetch OpenAlex works whose title/abstract mention JEPA (venue info + non-arXiv papers)."""
import json, sys, time, urllib.parse, urllib.request

API = "https://api.openalex.org/works"
SEARCHES = ['JEPA', '"joint embedding predictive"', '"joint-embedding predictive architecture"']
SELECT = "id,doi,title,publication_year,publication_date,type,primary_location,locations,ids,cited_by_count"

def get(url, tries=4):
    for k in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "paper-list-builder/1.0"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read())
        except Exception as e:  # noqa
            print("  retry", k, e, file=sys.stderr)
            time.sleep(4 + 4 * k)
    raise SystemExit("fetch failed: " + url)

def run(out):
    works = {}
    for s in SEARCHES:
        page, n, total = 1, 0, None
        while total is None or n < total:
            url = API + "?" + urllib.parse.urlencode({
                "filter": f"title_and_abstract.search:{s}", "per-page": 200,
                "page": page, "select": SELECT})
            try:
                data = get(url)
            except SystemExit as e:
                print("  stopped early:", e, file=sys.stderr)
                break
            res = data.get("results", [])
            if not res:
                break
            for w in res:
                works[w["id"]] = w
            n += len(res)
            total = data.get("meta", {}).get("count")
            print(f"{s}: {n}/{total} (unique {len(works)})", file=sys.stderr)
            page += 1
            time.sleep(1.0)
    json.dump(list(works.values()), open(out, "w"), ensure_ascii=False)
    print("saved", len(works), "works to", out)

if __name__ == "__main__":
    run(sys.argv[1])
