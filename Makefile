doc.tsv: items.jsonl
	python convert_to_tsv.py <$< >$@
items.jsonl: scrape.py
	scrapy runspider scrape.py -o items.jsonl -t jsonlines