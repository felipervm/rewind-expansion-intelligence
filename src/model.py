"""Deterministic fictional account exploration — not Rewind customer data."""
from pathlib import Path
import csv,json,random
ROOT=Path(__file__).resolve().parents[1]
SEED=20261020
PLATFORMS=('Shopify','GitHub','Jira','Confluence','Azure DevOps','BigCommerce')
SEGMENTS=('Commerce','Software','Professional services','Consumer brands')
def classify(row):
 unknown=[p for p in row['observed_tools'] if p not in row['protected_tools']]
 if not unknown:return dict(level='Coverage mapped',candidate=None,owner='Customer Success',next_step='Confirm coverage still meets recovery needs',why='No additional tool observed in synthetic inventory')
 candidate=next((p for p in ('GitHub','Jira','Shopify','Confluence','Azure DevOps','BigCommerce') if p in unknown),unknown[0])
 if not row['consent_to_discuss']:return dict(level='Verify context',candidate=candidate,owner='Account owner',next_step='Confirm account engagement preferences before outreach',why='Consent is not confirmed')
 if row['inventory_age_days']>90:return dict(level='Verify context',candidate=candidate,owner='Customer Success',next_step='Revalidate application inventory and coverage status',why='Information may be outdated')
 if row['renewal_days']<=75 and row['recovery_priority'] in ('High','Critical'):return dict(level='Discuss coverage',candidate=candidate,owner='Customer Success + Account Manager',next_step=f'Ask whether {candidate} requires independent recovery coverage',why='Relevant recovery priority and near-term review')
 return dict(level='Discovery later',candidate=candidate,owner='Account owner',next_step=f'Validate whether {candidate} is business critical at a future check-in',why='Observed use is not a qualified sales opportunity')
def fixture():
 rng=random.Random(SEED);rows=[]
 for i in range(1,55):
  tools=rng.sample(list(PLATFORMS),rng.randint(2,4));protected=rng.sample(tools,rng.randint(1,len(tools)))
  rows.append(dict(id=f'RX-{i:03d}',name=f'Fictional Account {i:03d}',segment=rng.choice(SEGMENTS),observed_tools=tools,protected_tools=protected,inventory_age_days=rng.choice([14,30,45,70,110,180]),renewal_days=rng.choice([30,60,90,150,220]),recovery_priority=rng.choice(['Standard','High','Critical']),consent_to_discuss=rng.choice([True,True,True,False])))
 rows[:3]=[
 dict(id='RX-001',name='Northstar Commerce (fictional)',segment='Commerce',observed_tools=['Shopify','GitHub','Jira'],protected_tools=['Shopify'],inventory_age_days=30,renewal_days=60,recovery_priority='Critical',consent_to_discuss=True),
 dict(id='RX-002',name='Meridian Systems (fictional)',segment='Software',observed_tools=['GitHub','Jira','Confluence'],protected_tools=['GitHub'],inventory_age_days=180,renewal_days=30,recovery_priority='High',consent_to_discuss=True),
 dict(id='RX-003',name='Atlas Retail Group (fictional)',segment='Commerce',observed_tools=['Shopify','BigCommerce','GitHub'],protected_tools=['Shopify'],inventory_age_days=45,renewal_days=120,recovery_priority='High',consent_to_discuss=False)]
 return [dict(r,assessment=classify(r)) for r in rows]
def main():
 rows=fixture();(ROOT/'data').mkdir(exist_ok=True)
 (ROOT/'data/accounts.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
 with (ROOT/'data/decisions.csv').open('w',newline='',encoding='utf-8') as f:
  w=csv.writer(f);w.writerow(['id','fictional_name','assessment','candidate_platform','proposed_owner','next_step','rationale'])
  for r in rows:
   a=r['assessment'];w.writerow([r['id'],r['name'],a['level'],a['candidate'],a['owner'],a['next_step'],a['why']])
 print('Generated',len(rows),'synthetic accounts')
if __name__=='__main__':main()
