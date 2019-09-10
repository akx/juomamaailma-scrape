import sys
import json
import csv

sort_keys = ["category_name", "name", "sku"]
output_keys = ["category_name", "name", "sku", "package-info", "url"]
uniq_key = "sku"

docs = [json.loads(doc) for doc in sys.stdin]
cw = csv.writer(sys.stdout, dialect=csv.excel_tab)
seen = set()
for doc in sorted(docs, key=lambda doc: [doc[k] for k in sort_keys]):
    id = doc[uniq_key]
    if id in seen:
        continue
    cw.writerow([str(doc.get(key) or "") for key in output_keys])
    seen.add(id)
