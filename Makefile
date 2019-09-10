doc.tsv: items.jsonl
	jq -r -s 'sort_by(.name, .sku) | .[] | [.sku,.name,.["package-info"],.url] | @tsv' items.jsonl | uniq > doc.tsv

items.jsonl: scrape.py
	scrapy runspider scrape.py -o items.jsonl -t jsonlines