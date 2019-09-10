import scrapy
import itertools

categories = ["soft-drinks", "waters", "juices", "special-drinks"]


class Jider(scrapy.Spider):
    name = "blogspider"
    start_urls = [
        f"https://www.juomamaailma.fi/fi/tuotteet/{cat}?p=1" for cat in categories
    ]

    def parse(self, response):

        for product in response.css(".products.wrapper .product-item-info"):
            yield {
                "sku": product.xpath("@data-sku").get(),
                "name": product.css(".product-item-link::text").get().strip(),
                "package-info": product.css(".product-package-info::text")
                .get()
                .strip(),
                "url": product.css(".product-item-link::attr(href)").get().strip(),
            }

        for page_link in response.css("div.pages li.item a"):
            yield response.follow(page_link, self.parse)
