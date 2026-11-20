#!/usr/bin/env python3
"""Render README.md from data/papers.json in the style of survey companion lists."""
import json, datetime, collections

P = json.load(open('data/papers.json'))
TODAY = datetime.date.today().isoformat()

FAMILIES = [
 ('survey', 'Surveys and Tutorials'),
 ('theory', 'Theory and Analysis'),
 ('F', 'JEPA-F: Image and Static Representation Learning'),
 ('T', 'JEPA-T: Video and Temporal Prediction'),
 ('A', 'JEPA-A: Action-Conditioned World Models, Planning and Control'),
 ('M', 'JEPA-M: Multimodal'),
 ('SC', 'JEPA-SC: 3D, Structured and Object-Centric'),
]
APPS = [
 ('driving', 'Autonomous Driving'),
 ('medical', 'Medical and Healthcare'),
 ('science', 'Scientific Domains'),
 ('remote', 'Remote Sensing'),
 ('audio', 'Audio, Speech and Music'),
 ('language', 'Language and Reasoning'),
 ('tseries', 'Time Series, Tabular and Trajectories'),
 ('graph', 'Graphs and Recommendation'),
 ('wireless', 'Wireless, Networks and Security'),
 ('other', 'Other'),
]
LABEL = dict(FAMILIES + APPS)

def anchor(t):
    return ''.join(c for c in t.lower().replace(' ', '-') if c.isalnum() or c == '-')

def esc(s):
    return (s or '').replace('|', '\\|').replace('\n', ' ').strip()

def row(p):
    title = esc(p['title'])
    title = f"[{title}]({p['link']})" if p.get('link') else title
    code = f"[{p['code_kind']}]({p['code']})" if p.get('code') else '-'
    return f"| {p['year']} | {esc(p['venue'])} | {esc(p['acr'])} | {title} | {code} |"

def table(rows):
    rows = sorted(rows, key=lambda p: (-(p['year'] or 0), p['title'].lower()))
    out = ['| Year | Venue | Acronym | Paper Title | Code/Project |', '|:----:|:-----:|:-------:|:------------|:------------:|']
    return '\n'.join(out + [row(p) for p in rows])

core = [p for p in P if p['core']]
rel = [p for p in P if not p['core'] and p['src'] != 'survey-bib']
bg = [p for p in P if p['src'] == 'survey-bib']

L = []
L.append('# JEPA-Survey: A Paper List on Joint-Embedding Predictive Architectures\n')
L.append('A curated list of papers on **Joint-Embedding Predictive Architectures (JEPA)** and JEPA-based world models, '
         'organized by the taxonomy of our survey: static/foundational (JEPA-F), temporal (JEPA-T), action-conditioned (JEPA-A), '
         'multimodal (JEPA-M), and structured/scene-centric (JEPA-SC) methods, followed by application domains.\n')
L.append('This repository accompanies our survey on JEPA and world models. The paper link will be added here once it is public.\n')
L.append(f'**{len(P)} papers** in total: {len(core)} JEPA papers, {len(rel)} related works that use, evaluate or discuss JEPA, '
         f'and {len(bg)} background references cited in the survey. Last updated: {TODAY}.\n')
L.append('If a paper is missing or an entry is wrong, pull requests and issues are welcome.\n')
L.append('## How this list is built\n')
L.append('- **Sources.** arXiv records whose title or abstract mentions JEPA (or a JEPA-derived name such as LeJEPA or LeWorldModel), '
         'non-arXiv papers with JEPA in the title indexed by OpenAlex, and the reference list of the survey.\n'
         '- **Venue.** Taken from the arXiv journal reference or comment field and from Semantic Scholar. Papers without a confirmed venue are listed as `arXiv`.\n'
         '- **Code/Project.** The link the authors give in the arXiv abstract or comments. `-` means no link was found automatically, not that no code exists.\n'
         '- **Categories.** Assigned by keyword rules with a manual pass over part of the list. The JEPA-F/T/A/M/SC labels of the methods analyzed in the survey follow the paper.\n\n'
         'The venue, code and category fields are extracted automatically and will contain errors. Corrections are welcome. '
         'The scripts are in [`tools/`](tools) and the data in [`data/papers.json`](data/papers.json).\n')
L.append('## Contents\n')
toc = ['- [JEPA Methods](#jepa-methods)']
for k, name in FAMILIES:
    n = sum(1 for p in core if p['cat'] == k)
    if n: toc.append(f'  - [{name}](#{anchor(name)}) ({n})')
toc.append('- [Applications](#applications)')
for k, name in APPS:
    n = sum(1 for p in core if p['cat'] == k)
    if n: toc.append(f'  - [{name}](#{anchor(name)}) ({n})')
toc.append(f'- [Related Work That Uses, Evaluates or Discusses JEPA](#related-work-that-uses-evaluates-or-discusses-jepa) ({len(rel)})')
toc.append(f'- [Background Cited in the Survey](#background-cited-in-the-survey) ({len(bg)})')
L.append('\n'.join(toc) + '\n')

L.append('## JEPA Methods\n')
for k, name in FAMILIES:
    rows = [p for p in core if p['cat'] == k]
    if rows: L.append(f'### {name}\n\n' + table(rows) + '\n')
L.append('## Applications\n')
for k, name in APPS:
    rows = [p for p in core if p['cat'] == k]
    if rows: L.append(f'### {name}\n\n' + table(rows) + '\n')
L.append('## Related Work That Uses, Evaluates or Discusses JEPA\n')
L.append('Papers that are not primarily about a JEPA method but build on, benchmark against, or analyze JEPA models.\n')
for k, name in FAMILIES + APPS:
    rows = [p for p in rel if p['cat'] == k]
    if rows:
        short = name.split(': ', 1)[-1]
        L.append(f'#### Related: {short}\n\n' + table(rows) + '\n')
L.append('## Background Cited in the Survey\n')
L.append('Foundational work on self-supervised learning, world models, benchmarks and baselines that the survey builds on.\n')
L.append(table(bg) + '\n')
open('README.md', 'w').write('\n'.join(L))
print('README.md written:', len(P), 'papers;', len(core), 'core;', len(rel), 'related;', len(bg), 'background')
print(collections.Counter(p['cat'] for p in core).most_common())
