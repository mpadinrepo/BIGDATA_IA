from scrapy.crawler import CrawlerProcess
from myproject.spiders.stackoverflow_spider import StackOverflowSpider

process = CrawlerProcess()
process.crawl(StackOverflowSpider)
process.start()
