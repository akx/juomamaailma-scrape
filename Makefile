doc.tsv: items.jsonl
	jq -r -s 'sort_by(.category_name, .name, .sku) | .[] | [.category_name,.sku,.name,.["package-info"],.url] | @tsv' items.jsonl | uniq > doc.tsv

items.jsonl: scrape.py
	scrapy runspider scrape.py -o items.jsonl -t jsonlines