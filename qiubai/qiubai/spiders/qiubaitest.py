import scrapy
from qiubai.items import QiubaiItem

class QiubaitestSpider(scrapy.Spider):
    name = 'qiubaitest'
    #allowed_domains = ['wwww.xxx.com']
    url='https://www.qiushibaike.com/text/page/{}'
    urls=[]
    for i in range(1,11,1):

        #print(url)
        urls.append(url.format(str(i)))
    print(urls)
    start_urls=urls
    #命令方式输出(在控制台 scrapy  crawl qiubaitest -o 文件名)
    # def parse(self, response):
    #     div_lists=response.xpath('//*[@id="content"]/div[@class="content-block clearfix"]/div[2]/div')
    #     all_contents=[]
    #     for div in div_lists:
    #
    #         author=div.xpath('./div[@class="author clearfix"]/a[2]/h2/text()').extract_first()
    #         text=div.xpath('./a[@class="contentHerf"]/div[@class="content"]/span//text()').extract()[0]
    #         #text=''.join(text)
    #         print(author,text)
    #         content={'author':author,'text':text}
    #         all_contents.append(content)
    #     return all_contents
    #以管道方式输出
    def parse(self, response):
        div_lists=response.xpath('//*[@id="content"]/div[@class="content-block clearfix"]/div[2]/div')
        all_contents=[]
        for div in div_lists:
            author=div.xpath('./div[@class="author clearfix"]/a[2]/h2/text()').extract_first()
            text=div.xpath('./a[@class="contentHerf"]/div[@class="content"]/span//text()').extract()[0]
            #########使用管道解释
            item=QiubaiItem()
            item['author']=author
            item['text'] = text
            yield item  #将item 提交给管道
