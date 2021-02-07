# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
import json
#输出到文件管道
class QiubaiPipeline:
    #只在开始的时候调用一次
    def open_spider(self,spider):
        fp=None
        self.fp=open('./qiubai.txt','w',encoding='utf-8')
    #每爬取一次会调用一次
    def process_item(self, item, spider):
        author=item['author']
        text=item['text']
        self.fp.write(author+"："+text+'\rn')
        return item
    #只在结束的时候调用一次
    def close_spider(self,prider):
        self.fp.close()
#输出到mysql 管道
class insertmysql():
    #只在开始的时候调用一次
    conn=None
    curcor=None
    database = 'stock'
    configfile = 'D:/mysqlconfig.json'
    # 读取json格式的配置文件
    def file2dict(self,path):
        with open(path, encoding="utf-8") as f:
            jsoncontent = json.load(f)
            # if jsoncontent.startswith(u'\ufeff'):
            #     jsoncontent = jsoncontent.encode('utf8')[3:].decode('utf8')
            return jsoncontent

    def dbconnect(self):  # 建立连接
        dict = []
        dict = self.file2dict(self.configfile)  # 获取连接数据库需要的相关信息
        # 创建数据库连接
        self.conn = pymysql.connect(dict['host'], dict['user'], dict['password']
                               , dict['database'], charset='utf8')
        return self.conn

    def open_spider(self,spider):
        self.conn=self.dbconnect()
        self.cursor=self.conn.cursor()
    #每爬取一次会调用一次
    def process_item(self, item, spider):
        try:
            sql='insert into qiubai values(%s,%s)'
            values=(item["author"],item["text"])
            self.cursor.execute(sql,values)
            self.conn.commit()
        except BaseException as e:
            print(e)
            self.conn.rollback()
        return item
    #只在结束的时候调用一次
    def close_spider(self,prider):
        self.cursor.close()
        self.conn.close()

'''
create table qiubai(
author varchar(100),
text varchar(5000)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
