import scrapy

from bosspro.items import BossproItem



class BossSpider(scrapy.Spider):
    name = 'boss'
    #allowed_domains = ['www.xxx.com']
    query='测试'

    salary_level='sel-salary-5'
    url='https://www.zhipin.com/c101250100/?query=%s&page=%s'

    start_urls = ['https://www.zhipin.com/c101250100/y_5/?query=%E6%B5%8B%E8%AF%95&ka=sel-salary-5']
    print('开始')
    def parse_detail(self,response):
        item=response.meta['item']
        job_desc=response.xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[1]/div[@class="text"]//text()').extract()
        job_desc=''.join(job_desc)
        item['job_desc']=job_desc
        yield  item
    def parse(self, response):
        #print(response)
        li_list=response.xpath('//div[@class="job-list"]/ul/li')
        print(li_list)
        for li in li_list:
            item=BossproItem()
            print(li)
            job_name=li.xpath('./div[@class="job-primary"]//div[@class="job-title"]/span[@class="job-name"]/text()').extract_first()
            job_area=li.xpath('./div[@class="job-primary"]//div[@class="job-title"]/span[@class="job-area-wrapper"]/span[@class="job-area"]/text()').extract_first()
            job_time=li.xpath('./div[@class="job-primary"]//div[@class="job-title"]/span[@class="job-pub-time"]/text()').extract_first()
            salary=li.xpath('./div[@class="job-primary"]//div[@class="job-limit clearfix"]/span[@class="red"]/text()').extract_first()
            company=li.xpath('./div[@class="job-primary"]//div[@"class="info-company""]//h3[@class="name"]/a/text()').extract_first()
            item['job_name']=job_name
            item['job_area']=job_area
            item['job_time'] = job_time
            item['salary'] = salary
            item['company'] = company
            detail_url=li.xpath('./div[@class="job-primary"]//div[@"class="info-company""]/div[@class="primary-wrapper"]/div[@class="primary-box"]/@href').extract_first()
            #print(detail_url)
            #将item 以参数传给parse_detail  meta={}
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})

