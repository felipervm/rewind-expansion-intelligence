import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from model import fixture,classify
class ModelTests(unittest.TestCase):
 def setUp(self):self.rows=fixture()
 def test_count(self):self.assertEqual(len(self.rows),54)
 def test_determinism(self):self.assertEqual(fixture(),fixture())
 def test_three_stories(self):self.assertEqual([r['id'] for r in self.rows[:3]],['RX-001','RX-002','RX-003'])
 def test_coverage(self):self.assertEqual(classify(dict(self.rows[0],protected_tools=self.rows[0]['observed_tools']))['level'],'Coverage mapped')
 def test_consent_first(self):self.assertEqual(self.rows[2]['assessment']['level'],'Verify context')
 def test_stale_data(self):self.assertEqual(self.rows[1]['assessment']['level'],'Verify context')
 def test_no_invented_revenue(self):self.assertTrue(all('revenue' not in r['assessment'] for r in self.rows))



class BoundaryTests(unittest.TestCase):
 def test_inventory_and_review_boundaries(self):
  row=dict(fixture()[0],inventory_age_days=90,renewal_days=75)
  self.assertEqual(classify(row)['level'],'Discuss coverage')
  self.assertEqual(classify(dict(row,inventory_age_days=91))['level'],'Verify context')
  self.assertEqual(classify(dict(row,renewal_days=76))['level'],'Discovery later')
 def test_permission_precedes_staleness_when_additional_tools_exist(self):
  row=dict(fixture()[0],consent_to_discuss=False,inventory_age_days=180)
  out=classify(row)
  self.assertEqual(out['owner'],'Account owner')
  self.assertEqual(out['why'],'Consent is not confirmed')
 def test_classification_preserves_input_and_generated_records(self):
  import copy,json,re
  rows=fixture();snapshot=copy.deepcopy(rows)
  for row in rows:classify(row)
  self.assertEqual(rows,snapshot)
  root=Path(__file__).resolve().parents[1]
  payload=json.loads((root/'data/accounts.json').read_text(encoding='utf-8'))
  self.assertEqual(payload,rows)

if __name__=='__main__':unittest.main()
