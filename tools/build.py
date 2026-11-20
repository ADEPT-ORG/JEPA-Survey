#!/usr/bin/env python3
"""Merge sources, resolve venue / code / acronym / category, and write data/papers.json."""
import json, re, collections, html

def nt(t): return re.sub(r'[^a-z0-9]+', ' ', (t or '').lower()).strip()

ax = json.load(open('data/arxiv_raw.json'))
s2 = json.load(open('data/s2_venues.json'))
oa_all = json.load(open('data/openalex_raw.json'))
oa_extra = json.load(open('data/openalex_extra_candidates.json'))

# ---------- venue ----------
VENUES = [
 ('NeurIPS', r'\bNeurIPS\b|Neural Information Processing Systems|\bNIPS\b'),
 ('ICML', r'\bICML\b|International Conference on Machine Learning(?! and Appl)'),
 ('ICLR', r'\bICLR\b|International Conference on Learning Representations'),
 ('CVPR', r'\bCVPRW?F?\b|Computer Vision and Pattern Recognition'),
 ('ICCV', r'\bICCVW?\b|International Conference on Computer Vision'),
 ('ECCV', r'\bECCVW?\b|European Conference on Computer Vision'),
 ('WACV', r'\bWACV\b|Winter Conference on Applications of Computer Vision'),
 ('BMVC', r'\bBMVC\b'), ('ACCV', r'\bACCV\b'), ('3DV', r'\b3DV\b'), ('ICPR', r'\bICPR\b'),
 ('AAAI', r'\bAAAI\b'), ('IJCAI', r'\bIJCAI\b'), ('ECAI', r'\bECAI\b'),
 ('ACL', r'\bACL\b(?! anthology)|Association for Computational Linguistics'),
 ('EMNLP', r'\bEMNLP\b|Empirical Methods in Natural Language'), ('NAACL', r'\bNAACL\b'), ('COLING', r'\bCOLING\b'),
 ('CoRL', r'\bCoRL\b|Conference on Robot Learning'), ('ICRA', r'\bICRA\b'), ('IROS', r'\bIROS\b'),
 ('RSS', r'Robotics: Science and Systems|\bRSS 20\d\d'), ('RA-L', r'\bRA-?L\b|Robotics and Automation Letters'),
 ('MICCAI', r'\bMICCAI\b|Medical Image Computing and Computer'), ('MIDL', r'\bMIDL\b'), ('ISBI', r'\bISBI\b'),
 ('ICASSP', r'\bICASSPW?\b|Acoustics, Speech,? and Signal Processing'), ('Interspeech', r'\bInterspeech\b'),
 ('ISMIR', r'\bISMIR\b|Music Information Retrieval'), ('EUSIPCO', r'\bEUSIPCO\b'), ('ICIP', r'\bICIP\b'),
 ('KDD', r'\bKDD\b|Knowledge Discovery and Data Mining'), ('CIKM', r'\bCIKM\b'), ('SIGIR', r'\bSIGIR\b'), ('WWW', r'\bWWW\b|The Web Conference'),
 ('ACM MM', r'\bACM MM\b|ACM Multimedia|International Conference on Multimedia'),
 ('UAI', r'\bUAI\b'), ('AISTATS', r'\bAISTATS\b'), ('COLT', r'\bCOLT\b'), ('LoG', r'Learning on Graphs'),
 ('IJCNN', r'\bIJCNN\b|Joint Conference on Neural Network'), ('ESANN', r'\bESANN\b|European Symposium on Artificial Neural'),
 ('L4DC', r'\bL4DC\b'), ('CoLLAs', r'\bCoLLAs\b'), ('CHIL', r'\bCHIL\b'), ('MLHC', r'\bMLHC\b'),
 ('IV', r'Intelligent Vehicles Symposium'), ('ITSC', r'\bITSC\b'), ('ICC', r'\bICC 20\d\d|International Conference on Communications'),
 ('GLOBECOM', r'\bGLOBECOM\b'), ('PIMRC', r'\bPIMRC\b|Personal, Indoor and Mobile Radio'), ('VTC', r'Vehicular Technology Conference'),
 ('TMLR', r'\bTMLR\b|Trans(actions|\.) (on )?Mach(ine|\.) Learn(ing|\.) Res'),
 ('JMLR', r'\bJMLR\b|Journal of Machine Learning Research'),
 ('TPAMI', r'\bT-?PAMI\b|Pattern Analysis and Machine Intelligence'), ('IJCV', r'\bIJCV\b|International Journal of Computer Vision'),
 ('TIP', r'\bTIP\b|Transactions on Image Processing'), ('TNNLS', r'\bTNNLS\b|Neural Networks and Learning Systems'),
 ('TCSVT', r'\bTCSVT\b|circuits and systems for video technology'), ('TGRS', r'\bTGRS\b|Geoscience and Remote Sensing'),
 ('CVIU', r'Computer Vision and Image Understanding'), ('IEEE Access', r'IEEE Access'), ('IoT-J', r'Internet of Things Journal'),
 ('Neurocomputing', r'\bNeurocomputing\b'), ('Pattern Recognition Letters', r'Pattern Recognition Letters'),
 ('Nature Communications', r'Nature Communications'), ('Nature Machine Intelligence', r'Nature Machine Intelligence'),
 ('Scientific Reports', r'Scientific Reports'), ('eLife', r'\beLife\b'),
]
VENUES = [(a, re.compile(p, re.I if not p.startswith(r'\bACL') and a not in ('IV', 'TIP', 'ICC', 'RSS', 'WWW', 'UAI', 'COLT', 'ACL') else 0)) for a, p in VENUES]
POS = re.compile(r'accept|publish|to appear|appear(s|ed|ing)? (in|at)|camera[- ]ready|proceedings|\boral\b|spotlight|poster|presented at|presentation at|workshop|findings', re.I)
NEG = re.compile(r'submitted|under review|in submission|submission to|under consideration|in review', re.I)

def match_venue(text):
    for a, rx in VENUES:
        m = rx.search(text)
        if m: return a, m
    return None, None

def clean_name(s):
    s = re.sub(r'^\d{4}\s+', '', s or '').strip()
    s = re.sub(r'^\d+(st|nd|rd|th)\s+', '', s)
    s = re.sub(r'\s*\(.*?\)\s*$', '', s)
    s = re.sub(r'(?i)^lecture notes in computer science$', 'LNCS', s)
    s = re.sub(r'(?i)^communications in computer and information science$', 'CCIS', s)
    if len(s) > 56:
        s = s[:56].rsplit(' ', 1)[0] + '…'
    return re.sub(r'\s*\([^)]*$', '', s).strip(' ,.;')

oa_by_ax = {}
def oa_aid(w):
    m = re.search(r'10\.48550/arxiv\.(\d{4}\.\d{4,5})', (w.get('doi') or ''), re.I)
    if m: return m.group(1)
    for loc in (w.get('locations') or []):
        u = (loc.get('landing_page_url') or '') + ' ' + (loc.get('pdf_url') or '')
        m = re.search(r'arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})', u)
        if m: return m.group(1)
for w in oa_all:
    a = oa_aid(w)
    if a: oa_by_ax.setdefault(a, []).append(w)
REPO = re.compile(r'arxiv|zenodo|ssrn|research square|biorxiv|medrxiv|preprints|hal\b|figshare|osf|openreview|techrxiv|authorea|pubmed|doaj|europe pmc|philpapers|repository|deepblue|scholar', re.I)

def resolve_venue(r):
    year = int(r['published'][:4])
    jr, cm = r.get('journal_ref') or '', r.get('comment') or ''
    if jr:
        a, m = match_venue(jr)
        y = re.search(r'(20\d\d)', jr)
        name = a or clean_name(re.split(r',|\bvol\b|\bpp\b|\d{4}', jr)[0])
        if name:
            ws = ' Workshop' if re.search(r'workshop', jr, re.I) and 'Workshop' not in name else ''
            return name + ws, int(y.group(1)) if y else year
    if cm and POS.search(cm) and not NEG.search(cm):
        a, m = match_venue(cm)
        if a:
            tail = cm[m.start(): m.end() + 30]
            y = re.search(r"(20\d\d)|'(\d\d)\b", tail)
            yy = int(y.group(1)) if y and y.group(1) else (2000 + int(y.group(2)) if y else year)
            ws = ' Workshop' if re.search(r'workshop', cm, re.I) else ''
            return a + ws, yy
    p = s2.get(r['id']) or {}
    v = (p.get('venue') or '').strip()
    if v and not REPO.search(v):
        a, _ = match_venue(v)
        ws = ' Workshop' if re.search(r'workshop|\bCVPRW\b|\bICCVW\b|\bICASSPW\b', v, re.I) else ''
        return (a + ws) if a else clean_name(v), p.get('year') or year
    for w in oa_by_ax.get(r['id'], []):
        s = ((w.get('primary_location') or {}).get('source') or {})
        n, t = s.get('display_name') or '', s.get('type') or ''
        if n and t in ('journal', 'conference') and not REPO.search(n):
            a, _ = match_venue(n)
            return a or clean_name(n), w.get('publication_year') or year
    return 'arXiv', year

# ---------- code ----------
URL = re.compile(r'https?://[^\s<>"\')\]]+')
def find_code(r):
    text = (r.get('comment') or '') + ' ' + (r.get('abstract') or '')
    urls = [re.split(r'[{}\\]', u)[0].rstrip('.,;:)') for u in URL.findall(text)]
    urls = [u for u in urls if len(u) > 12]
    for u in urls:
        if re.search(r'github\.com/[\w.-]+/[\w.-]+', u): return 'Code', u
    for u in urls:
        if re.search(r'gitlab\.com|bitbucket\.org|huggingface\.co|codeberg\.org', u): return 'Code', u
    for u in urls:
        if re.search(r'github\.io|sites\.google\.com|/research/|project', u, re.I) and not re.search(r'drive\.google|youtu|4open\.science', u): return 'Project', u
    return None, None

# ---------- acronym ----------
ACR_TOKEN = re.compile(r'[A-Z]{2,}|\d|[a-z][A-Z]')
ACR_FIXED = {'2301.08243': 'I-JEPA', '2404.08471': 'V-JEPA', '2603.19312': 'LeWM', '2606.26217': 'Fast-LeWM'}
BASE = {'JEPA', 'JEPAs', 'I-JEPA', 'IJEPA', 'V-JEPA', 'VJEPA', 'V-JEPA 2', 'V-JEPA2', 'VJEPA-2', 'VJEPA2', 'V-JEPA 2.1', 'LeJEPA',
        'H-JEPA', 'JEPA-WMs', 'Video-JEPA', 'Graph-JEPA'}
SUFFIX = re.compile(r'-(based|style|inspired|guided|driven|like|conditioned|regulari[sz]ed|enhanced|derived|to|aware|free)\b', re.I)
def acronym(title):
    if ':' in title:
        pre = title.split(':', 1)[0].strip()
        toks = pre.split()
        if len(pre) <= 26 and (len(toks) == 1 or (len(toks) <= 3 and any(ACR_TOKEN.search(t) for t in toks))) and not SUFFIX.search(pre):
            return pre
    m = re.search(r'([\w.]+-)*\w*JEPA\w*(-[\w.]+)*(\s?\d(\.\d)?(-AC)?)?', title)
    if m and m.group(0).strip() not in BASE and not SUFFIX.search(m.group(0)):
        return m.group(0).strip()
    return '-'

# ---------- category ----------
CATS = collections.OrderedDict([
 ('survey',   r'\bsurvey\b|\btutorial\b|\breview\b|position paper|\bperspective\b|\broadmap\b|\bprimer\b'),
 ('driving',  r'autonomous driving|self-driving|\bdriving\b|\bdrive\b|vehicle|traffic|\bV2X\b|\bBEV\b|motion forecasting|trajectory prediction|pedestrian'),
 ('medical',  r'medical|clinical|patient|sepsis|glucose|arrhythm|fetal|\bskin\b|lesion|nodule|triage|emergency department|hemodynamic|vascular|photoplethysmograph|breathing|\bECG\b|\bEEG\b|\bEMG\b|\bPPG\b|fMRI|\bMRI\b|\bCT\b|radiolog|patholog|histolog|ultrasound|echocardi|x-ray|chest|tumor|cancer|surgical|surgery|endoscop|health|brain|neuroimag|sleep|\bICU\b|biomedical|cardiac|retina|disease|physiolog'),
 ('remote',   r'remote sensing|satellite|geospatial|earth observation|hyperspectral|\bSAR\b|aerial|multispectral'),
 ('wireless', r'wireless|WiFi|network fingerprint|phishing|zero trust|\b6G\b|\b5G\b|channel state|\bCSI\b|radio|beamform|spectrum|\bMIMO\b|network traffic|\bRF\b|communications?\b|\bGNSS\b|radar|malware|intrusion|cyber'),
 ('science',  r'physic|\bPDE|fluid|cryo-EM|antibody|atomistic|aerodynam|precipitation|coastal|neural circuit|neural recording|climate|weather|molecul|protein|genom|\bDNA\b|\bRNA\b|chemi|material|crystal|polymer|particle|collider|\bjet\b|astronom|galax|seismic|plasma|\bcell\b|transcriptom|single-cell|quantum|turbulen|neutrino|lattice|biolog'),
 ('audio',    r'\baudio\b|speech|music|\bsound\b|acoustic|spoken|\bMIDI\b'),
 ('graph',    r'\bgraphs?\b|recommend|knowledge graph|\bnode\b'),
 ('tseries',  r'time[- ]series|tabular|financ|stock|forecasting|\bIoT\b|sensor data|sensor-based|wearable|multivariate|trajectory (similarity|embedding)|anomaly detection|log data|trading|insurance'),
 ('language', r'language models?|\bLLMs?\b|\bNLP\b|sentence|natural language|\bBERT\b|linguistic|theorem proving|first-order logic'),
 ('theory',   r'theor|provabl|identifiab|collapse|implicit bias|generalization|spectral|information bottleneck|regulari[sz]|isotrop|gaussian|\bSIGReg\b|\bVICReg\b|understanding|analysis|why |when does|eigen|geometry of|dynamics of learning'),
 ('A',        r'action[- ]conditioned|planning|planner|world models?|robot|manipulat|\bcontrol\b|reinforcement|\bRL\b|policy|navigation|embodied|\bVLA\b|\bMPC\b|goal-conditioned|latent dynamics|imitation|agent'),
 ('M',        r'multimodal|multi-modal|vision[- ]language|video[- ]language|text[- ]conditional|text[- ]image|image-text|audio-visual|audiovisual|cross-modal|\bVLMs?\b|caption|\bVQA\b|retrieval'),
 ('SC',       r'point clouds?|\b3D\b|\b4D\b|object-centric|\bslot|scene graph|\bmesh|geometr|gaussian splat|depth|skeleton|\bpose\b|lidar'),
 ('T',        r'\bvideos?\b|temporal|spatiotemporal|spatio-temporal|motion|action recognition|\bframes?\b|optical flow|anticipation'),
 ('F',        r'\bimages?\b|masked|representation learning|\bViT\b|ImageNet|self-supervised'),
])
CRX = {k: re.compile(v, re.I if k not in () else 0) for k, v in CATS.items()}
ORDER = [k for k in CATS.keys() if k != 'language']
ORDER.insert(ORDER.index('M') + 1, 'language')
# family assignments fixed by the survey (Table 2)
FIXED = [
 (r'^Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture', 'F'), (r'^Discrete JEPA', 'F'), (r'^DMT-JEPA', 'F'),
 (r'^SparseJEPA', 'F'), (r'^T-JEPA: Augmentation-Free', 'F'),
 (r'^Revisiting Feature Prediction for Learning Visual Representations from Video', 'T'), (r'^V-JEPA 2: Self-Supervised Video Models', 'T'),
 (r'^MC-JEPA', 'T'), (r'^CF-JEPA', 'T'), (r'^Branch-JEPA', 'T'), (r'^UWM-JEPA', 'T'),
 (r'^ACT-JEPA', 'A'), (r'^LeWorldModel', 'A'), (r'^Fast LeWorldModel', 'A'), (r'^Sub-JEPA', 'A'),
 (r'^VL-JEPA', 'M'), (r'^M3-JEPA', 'M'), (r'^Le MuMo JEPA', 'M'), (r'^MJEPA', 'M'), (r'^AV-JEPA', 'M'), (r'^AquaJEPA', 'M'),
 (r'^Point-JEPA', 'SC'), (r'^Causal-JEPA', 'SC'), (r'^3D-JEPA', 'SC'), (r'^Cross4D-JEPA', 'SC'),
]
def categorize(title, abstract):
    for rx, c in FIXED:
        if re.search(rx, title, re.I): return c
    if CRX['survey'].search(title): return 'survey'
    score = {}
    for k in ORDER[1:]:
        t = len(set(m.group(0).lower() for m in CRX[k].finditer(title)))
        a = len(set(m.group(0).lower() for m in CRX[k].finditer(abstract or '')))
        score[k] = 4 * t + min(a, 3)
    # theory only when the title signals it
    if not CRX['theory'].search(title): score['theory'] = 0
    best = max(ORDER[1:], key=lambda k: (score[k], -ORDER.index(k)))
    return best if score[best] > 0 else 'F'

OVERRIDE = {}
for line in open('data/category_overrides.tsv'):
    line = line.split('#')[0].strip()
    if line:
        k, v = line.split()
        OVERRIDE[k] = v
DROP_IDS = {'W7134971968', 'W7139575559'}
CORE_T = re.compile(r'jepa|joint[- ]embedding predictive', re.I)
CORE_A = re.compile(r'(we|this (paper|work|study|article))\s+(\w+\s+){0,3}(propose|introduce|present|develop|design|build|extend|adapt)[^.]{0,200}(JEPA|joint[- ]embedding predictive)', re.I)
def is_core(title, abstract):
    if CORE_T.search(title): return True
    if CORE_A.search(abstract or ''): return True
    return len(re.findall(r'JEPA', abstract or '')) >= 3

papers, seen = [], set()
for r in ax:
    k = nt(r['title'])
    if k in seen: continue
    seen.add(k)
    venue, year = resolve_venue(r)
    kind, url = find_code(r)
    papers.append({'src': 'arxiv', 'id': r['id'], 'title': r['title'], 'year': year, 'venue': venue,
                   'acr': ACR_FIXED.get(r['id']) or acronym(r['title']), 'link': 'https://arxiv.org/abs/' + r['id'],
                   'code_kind': kind, 'code': url, 'cat': OVERRIDE.get(r['id']) or categorize(r['title'], r['abstract']),
                   'core': is_core(r['title'], r['abstract'])})

DROP = re.compile(r'JEPA MANDAR|MAKANAN JEPA|Kepala Sekolah|Tradisional Jepa|TEKSTUR JEPA|Japan Economic Partnership|Recreating the V-JEPA 2-AC|TS-L-JEPA|Quantum-Grounded|pico-JEPA', re.I)
PREP = [('bioRxiv', r'biorxiv'), ('medRxiv', r'medrxiv'), ('SSRN', r'ssrn'), ('Research Square', r'research square'),
        ('Preprints.org', r'preprints\.org'), ('HAL', r'^hal$'), ('engrXiv', r'engrxiv'), ('PubMed', r'pubmed'), ('PhilSci-Archive', r'philsci')]
for w in oa_extra:
    t = html.unescape(w.get('title') or '').strip()
    if DROP.search(t) or nt(t) in seen or w['id'].rsplit('/', 1)[-1] in DROP_IDS: continue
    seen.add(nt(t))
    s = ((w.get('primary_location') or {}).get('source') or {})
    n = s.get('display_name') or ''
    a, _ = match_venue(n)
    venue = a or next((p for p, rx in PREP if re.search(rx, n, re.I)), None) or clean_name(n)
    link = w.get('doi') or ((w.get('primary_location') or {}).get('landing_page_url')) or w.get('id')
    papers.append({'src': 'openalex', 'id': w['id'].rsplit('/', 1)[-1], 'title': t, 'year': w.get('publication_year'), 'venue': venue,
                   'acr': acronym(t), 'link': link, 'code_kind': None, 'code': None,
                   'cat': OVERRIDE.get(w['id'].rsplit('/', 1)[-1]) or categorize(t, ''), 'core': True})

for line in open('data/manual_additions.psv'):
    line = line.rstrip('\n')
    if not line: continue
    y, v, t, ref, cat = line.split('|')
    if nt(t) in seen: continue
    seen.add(nt(t))
    papers.append({'src': 'manual', 'id': '', 'title': t, 'year': int(y), 'venue': v, 'acr': acronym(t), 'link': ref,
                   'code_kind': None, 'code': None, 'cat': cat, 'core': True})

bg = 0
for line in open('data/survey_background.psv'):
    line = line.rstrip('\n')
    if not line: continue
    y, v, t, ref = line.split('|')
    if nt(t) in seen: continue
    aid = ref if re.fullmatch(r'\d{4}\.\d{4,5}', ref) else None
    if aid and any(p['id'] == aid for p in papers): continue
    seen.add(nt(t)); bg += 1
    papers.append({'src': 'survey-bib', 'id': aid or '', 'title': t, 'year': int(y), 'venue': v or '-',
                   'acr': acronym(t) if ':' in t else '-', 'link': ('https://arxiv.org/abs/' + aid) if aid else (ref or None),
                   'code_kind': None, 'code': None, 'cat': 'background', 'core': False})

json.dump(papers, open('data/papers.json', 'w'), ensure_ascii=False, indent=1)
c = collections.Counter(p['src'] for p in papers)
print('total', len(papers), dict(c), '| background added', bg)
print('core', sum(p['core'] for p in papers), '| with code/project link', sum(1 for p in papers if p['code']))
print('venue != arXiv among arxiv-sourced:', sum(1 for p in papers if p['src'] == 'arxiv' and p['venue'] != 'arXiv'))
print(collections.Counter((p['cat'], p['core']) for p in papers if p['src'] != 'survey-bib').most_common())
print(collections.Counter(p['venue'] for p in papers if p['src'] == 'arxiv').most_common(40))
