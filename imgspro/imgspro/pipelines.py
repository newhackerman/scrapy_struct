# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# class ImgsproPipeline:
#     def process_item(self, item, spider):
#         return item
#基于图片爬取功能，重写 get_media_requests，file_path，item_completed 方法
class imgspipeline(ImagesPipeline):

   def get_media_requests(self, item, info):
       #访问图片地址，下载图片
       yield scrapy.Request(item['img_url'])

   def file_path(self, request, response=None, info=None, *, item=None):
        #取得图片的文件名称
        imgName=request.url.split('/')[-1]
        return imgName

   def item_completed(self, results, item, info):
    # 返回执行结果
       return item
