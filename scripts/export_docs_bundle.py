#!/usr/bin/env python3
"""DOCS-SPLIT-01 S1: deterministic offline canonical-docs content bundle."""
import hashlib
import json
from pathlib import Path
from export_shell_documents import ROOT, export_documents

OUT = ROOT / 'exports' / 'gnu6-docs-content.v1.json'

def make_bundle():
    semantic = export_documents()
    entries = []
    for doc in semantic['documents']:
        route = doc['route']
        assert route.startswith('/docs/')
        new = dict(doc)
        new['route'] = route.removeprefix('/docs')
        new['legacy_routes'] = [route, doc['legacy_route']]
        new.pop('legacy_route')
        entries.append(new)
    assert len(entries) == 18 and len({d['route'] for d in entries}) == 18
    return {
        'schema': 'gnu6.docs.content.v1',
        'canonical_origin': 'https://docs.gnu6.live',
        'source_commit': semantic['source_commit'],
        'source_edition': semantic['edition'],
        'locales': ['fr', 'en'],
        'license_policy': 'MIT where first-party rights permit; preserve third-party notices',
        'documents': entries,
    }

def serialize(bundle):
    return (json.dumps(bundle, sort_keys=True, ensure_ascii=False, separators=(',', ':'))+'\n').encode()

def main():
    data=serialize(make_bundle())
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_bytes(data)
    print('DOCS_CONTENT_BUNDLE_PASS',len(json.loads(data)['documents']),hashlib.sha256(data).hexdigest())

if __name__=='__main__':main()
