import scrapy
from imgspro.items import ImgsproItem

class ImgsSpider(scrapy.Spider):
    name = 'imgs'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.xiao688.com/cms/list/typeid-185_page-1.html']

    def parse(self, response):
        li_list=response.xpath('//div[@class="row mt0 cfix"]//div[@class="piclist2"]/ul//li')
        for li in li_list:
            img_url=li.xpath('./a/img/@data').extract_first()
            if img_url=='':
                continue
            item=ImgsproItem()
            item['img_url']=img_url
            yield  item
            next_page='http://www.xiao688.com/cms/list/typeid-185_page-%s.html'
            for i in range(1,10):
                try:
                    url=next_page %i
                    #print(url)
                    yield scrapy.Request(url)
                except BaseException as E:
                    print(E)
                    continue
