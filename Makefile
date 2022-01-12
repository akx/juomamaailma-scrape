doc.tsv: items.jsonlines
	python convert_to_tsv.py <$< >$@
items.jsonlines: scrape.py
	scrapy runspider scrape.py -o items.jsonlines
clean:
	rm -f doc.tsv items.jsonlines
