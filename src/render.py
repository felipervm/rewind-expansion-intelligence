from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
data=json.loads((root/'data/accounts.json').read_text())
source=(root/'src/template.html').read_text(encoding='utf-8')
(root/'index.html').write_text(source.replace('/*ACCOUNT_DATA*/',json.dumps(data,separators=(',',':')).replace('</','<\\/')),encoding='utf-8')
print('Rendered site with',len(data),'fictional accounts')
