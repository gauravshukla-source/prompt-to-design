import json, os, re
from functools import lru_cache
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTRY_PATH=os.path.join(ROOT,'icon_registry.json')
def _norm(v): return re.sub(r'[^a-z0-9]+','-',str(v or '').lower()).strip('-')
@lru_cache(maxsize=1)
def load_registry():
    with open(REGISTRY_PATH,encoding='utf-8') as f: return json.load(f)
def reload_registry(): load_registry.cache_clear(); return load_registry()
def _exists(url): return os.path.exists(os.path.join(ROOT,url.lstrip('/').replace('static/','static/',1)))
def resolve_icon(name, provider=None, category=None):
    reg=load_registry(); q=_norm(name); p=_norm(provider)
    scored=[]
    for item in reg.get('items',[]):
        score=0; vals=[item['id'],item['slug'],item['label']]+item.get('aliases',[])
        vals=[_norm(x) for x in vals]
        if q in vals: score+=100
        elif any(q and (q in x or x in q) for x in vals): score+=55
        if p and _norm(item['provider'])==p: score+=30
        if category and _norm(item['category'])==_norm(category): score+=10
        if score: scored.append((score,item))
    if scored:
        item=max(scored,key=lambda x:x[0])[1].copy()
        item['assetStatus']='available' if _exists(item['path']) else 'missing'
        if item['assetStatus']=='missing': item['fallbackPath']=reg['fallback']['path']
        return item
    return {'id':'generic-service','provider':'generic','slug':'generic-service','label':'Generic Service','category':category or 'application','path':reg['fallback']['path'],'assetStatus':'fallback'}
def search_icons(query='',provider=None,category=None,available_only=False):
    reg=load_registry(); q=_norm(query); out=[]
    for item0 in reg.get('items',[]):
        item=item0.copy(); hay=' '.join([item['id'],item['label']]+item.get('aliases',[])).lower()
        if q and q.replace('-',' ') not in hay and q not in _norm(hay): continue
        if provider and _norm(item['provider'])!=_norm(provider): continue
        if category and _norm(item['category'])!=_norm(category): continue
        item['assetStatus']='available' if _exists(item['path']) else 'missing'
        if available_only and item['assetStatus']!='available': continue
        if item['assetStatus']=='missing': item['fallbackPath']=reg['fallback']['path']
        out.append(item)
    return out
