"""DOCS-SPLIT-01: canonical routes, integrity and fail-closed document semantics."""
import hashlib
import json
from export_docs_bundle import OUT, ROOT, make_bundle, serialize
from export_shell_documents import UnsafeDocument, parse_semantic

def main():
    raw=serialize(make_bundle())
    assert raw==serialize(make_bundle()), 'non-deterministic export'
    bundle=json.loads(raw)
    assert bundle['schema']=='gnu6.docs.content.v1'
    assert bundle['canonical_origin']=='https://docs.gnu6.live'
    assert len(bundle['documents'])==18
    assert {d['locale'] for d in bundle['documents']}=={'fr','en'}
    for d in bundle['documents']:
        assert d['route'].startswith('/'+d['locale']+'/') or d['route']=='/'+d['locale']
        assert not d['route'].startswith('/docs/')
        assert d['legacy_routes'][0].startswith('/docs/')
        assert hashlib.sha256((ROOT/d['source']).read_bytes()).hexdigest()==d['source_sha256']
    assert len({d['route'] for d in bundle['documents']})==18
    for bad in ['<script>x</script>','<a href="javascript:alert(1)">bad</a>']:
        try: parse_semantic(bad)
        except UnsafeDocument: pass
        else: raise AssertionError('unsafe content accepted')
    print('DOCS_CONTENT_BUNDLE_TEST_PASS',len(bundle['documents']),hashlib.sha256(raw).hexdigest())

if __name__=='__main__':main()
