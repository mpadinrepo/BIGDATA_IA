import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SuvscrawlerSpider(CrawlSpider):
    name = "suvscrawler"
    allowed_domains = ["www.clicars.com"]
    start_urls = ["https://www.clicars.com/coches-segunda-mano-ocasion/4x4-suv"]

    rules = (Rule(LinkExtractor(allow=r"Items/"), callback="parse_item", follow=True),)

    def parse_item(self, response):
        item = {}
        #item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        #item["name"] = response.xpath('//div[@id="name"]').get()
        #item["description"] = response.xpath('//div[@id="description"]').get()
        return item
