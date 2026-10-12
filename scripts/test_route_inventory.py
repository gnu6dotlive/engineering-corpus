import unittest
from export_route_inventory import export_surfaces
class ExportTests(unittest.TestCase):
 def test_preserves_every_generated_page(self):
  b=export_surfaces()
  self.assertGreater(len(b['pages']),18)
  routes={p['route'] for p in b['pages']}
  for route in ['/fr/hub.html','/en/api.html','/fr/sdk.html','/fr/studies/cuda-05h.html']:
   self.assertIn(route,routes)
  for p in b['pages']:
   self.assertRegex(p['source_sha256'],r'^[0-9a-f]{64}$')
   self.assertTrue(p['nodes'])
if __name__=='__main__': unittest.main()
