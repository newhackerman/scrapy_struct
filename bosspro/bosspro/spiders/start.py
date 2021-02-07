import os
from scrapy import cmdline


if __name__ == '__main__':
    # os.system('cd d:/pythonTtest/bosspro')
    # cmd='scrapy crawl boss' #执行爬虫命令
    # os.popen(cmd)
    #print(result.read())
    cmdline.execute('scrapy crawl' 'boss')