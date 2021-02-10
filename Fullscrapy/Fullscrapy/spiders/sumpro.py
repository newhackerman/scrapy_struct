import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SumproSpider(CrawlSpider):
    name = 'sumpro'
    allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.xxx.com/']
    link=LinkExtractor(allow=r'Items/')

    rules = (
        Rule(link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
