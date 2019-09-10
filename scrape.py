import scrapy
import itertools

categories = ["soft-drinks", "waters", "juices", "special-drinks"]


class Jider(scrapy.Spider):
    name = "blogspider"

    def start_requests(self):
        for category_name in categories:
            yield scrapy.Request(
                url=f"https://www.juomamaailma.fi/fi/tuotteet/{category_name}?p=1",
                cb_kwargs={"category_name": category_name},
                callback=self.parse_category_page,
            )

    def parse_category_page(self, response, category_name):

        for product in response.css(".products.wrapper .product-item-info"):
            yield {
                "sku": product.xpath("@data-sku").get(),
                "name": product.css(".product-item-link::text").get().strip(),
                "package-info": product.css(".product-package-info::text")
                .get()
                .strip(),
                "url": product.css(".product-item-link::attr(href)").get().strip(),
                "category_name": category_name,
            }

        for page_link in response.css("div.pages li.item a"):
            yield response.follow(
                page_link,
                self.parse_category_page,
                cb_kwargs={"category_name": category_name},
            )
