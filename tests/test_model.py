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
if __name__=='__main__':unittest.main()
