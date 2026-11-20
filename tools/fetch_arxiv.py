#!/usr/bin/env python3
"""Fetch arXiv records that mention JEPA and store them as JSON."""
import json, re, sys, time, urllib.parse, urllib.request
import xml.etree.ElementTree as ET

API = "https://export.arxiv.org/api/query"
NS = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom",
      "o": "http://a9.com/-/spec/opensearch/1.1/"}
QUERIES = [
    'ti:JEPA',
    'abs:JEPA',
    'all:"joint embedding predictive"',
    'all:"joint-embedding predictive architecture"',
]
PAGE = 200

def get(url, tries=5):
    for k in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "paper-list-builder/1.0"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except Exception as e:  # noqa
            print("  retry", k, e, file=sys.stderr)
            time.sleep(5 + 5 * k)
    raise SystemExit("fetch failed: " + url)

def norm(s):
    return re.sub(r"\s+", " ", s or "").strip()

def run(out):
    recs = {}
    for q in QUERIES:
        start, total = 0, None
        while total is None or start < total:
            url = API + "?" + urllib.parse.urlencode({
                "search_query": q, "start": start, "max_results": PAGE,
                "sortBy": "submittedDate", "sortOrder": "descending"})
            root = ET.fromstring(get(url))
            total = int(root.find("o:totalResults", NS).text)
            entries = root.findall("a:entry", NS)
            if not entries:
                # arXiv sometimes returns an empty page; retry once then move on
                time.sleep(6)
                root = ET.fromstring(get(url))
                entries = root.findall("a:entry", NS)
                if not entries:
                    print("  empty page at", start, "for", q, file=sys.stderr)
                    start += PAGE
                    continue
            for e in entries:
                raw = e.find("a:id", NS).text
                aid = re.sub(r"v\d+$", "", raw.rsplit("/abs/", 1)[-1])
                recs[aid] = {
                    "id": aid,
                    "title": norm(e.find("a:title", NS).text),
                    "abstract": norm(e.find("a:summary", NS).text),
                    "published": e.find("a:published", NS).text[:10],
                    "updated": e.find("a:updated", NS).text[:10],
                    "authors": [norm(a.find("a:name", NS).text) for a in e.findall("a:author", NS)],
                    "comment": norm(getattr(e.find("x:comment", NS), "text", "")),
                    "journal_ref": norm(getattr(e.find("x:journal_ref", NS), "text", "")),
                    "doi": norm(getattr(e.find("x:doi", NS), "text", "")),
                    "primary": (e.find("x:primary_category", NS).attrib.get("term")
                                if e.find("x:primary_category", NS) is not None else ""),
                    "cats": [c.attrib.get("term") for c in e.findall("a:category", NS)],
                }
            print(f"{q!r}: {min(start + PAGE, total)}/{total}  (unique so far {len(recs)})", file=sys.stderr)
            start += PAGE
            time.sleep(3.2)
    json.dump(sorted(recs.values(), key=lambda r: r["id"]), open(out, "w"), ensure_ascii=False, indent=1)
    print("saved", len(recs), "records to", out)

if __name__ == "__main__":
    run(sys.argv[1])
