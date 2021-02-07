# Scrapy settings for bosspro project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'bosspro'

SPIDER_MODULES = ['bosspro.spiders']
NEWSPIDER_MODULE = 'bosspro.spiders'
LOG_LEVEL='ERROR'

# Crawl responsibly by identifying yourself (and your website) on the user-agent

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 3
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'USER_AGENT' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
'cookie': 'Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1612664435; __g=sem; lastCity=101250100; __fid=049f8d26082dd2210aede5f9bc9b344e; wt2=5Guaw1NWjhfwzLRs; _bl_uid=ULkjzkn2uvzkqb9y3a0m0mdnzO55; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1612678522; __c=1612664433; __l=r=https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.Ks00000EAMrnlPLIy9zH6toAE8CbUbJrSqg9Nm_xZBSJ6K1eN0gUthImV9Zth5c8NLiNyLOmGRgjZ6H4c7Jj-ebe8oD_RPeRNDN8n6FJ1nrGGA-dNV2Ug8FWaDMjYYScsts-8BDMrgIVsP8_knG_cq6AFdMJPIH6J5EqIZqyQqzb5OdHAOKIbDZRT4E4vYdsbonXhUK0gHTbLrd5UUOMMh_v8qRi.DR_NR2Ar5Od663rj6t8AGSPticrZA1AlaqM766WHGek3hcYlXE_sgn8mE8kstVerQKMks4OgSWS534Oqo4yunOogEOtZV_zyUr1oWC_knmx5I9LtTrzEj4SrZuEse59sSX1jexo9vxQ5jWl3cMYAn5M8seSrZug9tOZj_L3IMs4t5MEseQnrOv3x5kseS1jeIMgVHC3ZHgng8WWlsk8sHfGmEIjfEl1F8xnhA6kNfCm3t5Zv3TMds45osTZK4TPHtU3bmTMdWHGs45ogu1RojPakvTXMkv20.U1Yk0ZDqmhq1TsKspynqn0KY5yFETLn0pyYqnWcd0ATqUvwlnfKdpHdBmy-bIfKspyfqnHT0mv-b5Hndn6KVIjYknjD4g1DsnHIxn1DzP7tknjfYg1DsnWPxn1msnfKopHYs0ZFY5Hb1n6KBpHYkPH9xnW0Yg1ckPdtdnjn0UynqnH0snNtkrjTYnj0kP1f1g1Dsn-tknjFxnNts0Z7spyfqn0Kkmv-b5H00ThIYmyTqn0K9mWYsg100ugFM5H00TZ0qn0K8IM0qna3snj0snj0sn0KVIZ0qn0KbuAqs5H00ThCqn0KbugmqTAn0uMfqn0KspjYs0Aq15H00mMTqnH00UMfqn0K1XWY0mgPxpywW5gK1QyIlpZ940A-bm1dcHbc0IA7zuvNY5Hm1g1KxnHRs0ZwdT1YkPWTvPjb3nWfsrj04njmYPHTznsKzug7Y5HDvnHcvPWfYn10znWn0Tv-b5yf4uWfzPHKbnj01n1bsmWm0mLPV5Hf4rRcznDm3nbwDwHuKnHb0mynqnfKsUWYs0Z7VIjYs0Z7VT1Ys0Aw-I7qWTADqn0KlIjYs0AdWgvuzUvYqn7tsg1KxnH0YP-tsg100uA78IyF-gLK_my4GuZnqn7tsg1f1nH04rHNxPjnknjb4PNtsg100TA7Ygvu_myTqn0Kbmv-b5H00ugwGujYVnfK9TLKWm1Ys0ZNspy4Wm1Ys0Z7VuWYs0AuWIgfqn0KGTvP_5H00XMK_Ignqn0K9uAu_myTqnfK_uhnqn0KbmvPb5fKYTh7buHYLPW0znjc0mhwGujY3wbN7fYmsnjTLPjnvnRFDfbc4PYu7wWIDrDnvrjRdP6KEm1Yk0AFY5H00Uv7YI1Ys0AqY5HD0ULFsIjYzc10WnH0WnBn1PjmkrHnkn10WnH0snj0WnH0snj08nj0snj0sc1DWnBnsczYWna3snjbsnW0Wna33nW0snj00TNqv5H08rHKxna3sn7tsQW0sg108PWKxna3vP7tsQWnk0AF1gLKzUvwGujYs0A-1gvPsmHYs0APs5H00mLFW5HcvPH03%26word%3D%26ck%3D7344.3.127.242.177.672.205.302%26shh%3Dwww.baidu.com%26sht%3Dbaidu%26us%3D1.0.1.0.1.367.0%26wd%3D%26bc%3D110101&l=%2Fwww.zhipin.com%2Fc101250100%2Fy_5%2F%3Fquery%3D%25E6%25B5%258B%25E8%25AF%2595%26ka%3Dsel-salary-5&g=%2Fwww.zhipin.com%2Fsem%2F10.html%3Fsid%3Dsem%26qudao%3Dbdpc_baidu-pc-BOSS-JD02-B19KA02084%26plan%3D%25E5%2593%2581%25E7%2589%258C%25E8%25AF%258D-cp%26unit%3D%25E5%2593%2581%25E7%2589%258C-%25E9%2580%259A%25E7%2594%25A8%26keyword%3Dboss%26bd_vid%3D11601827306815731128%26csource%3Dboctb&s=3&friend_source=0&s=3&friend_source=0; __a=69565552.1612664433..1612664433.58.1.58.58; __zp_stoken__=e95abAEYtPks9LhR2NwYwfWIVKQwtXCMVWzh8BGMuPzhdLUgQdD1KVh88aHV2ZhpkLSY2R0hKXRxBXWYkc3N0elUqYl0ydRA3Ry0nMi8JVC1jMyUgC2wud14vYjMRGwoBK3c8fnVDR2c0WFpHdA%3D%3D'

}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'bosspro.middlewares.BossproSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    #'bosspro.middlewares.BossproDownloaderMiddleware': 543,
#    'bosspro.middlewares.CookiesMiddlewares': 544
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'bosspro.pipelines.BossproPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'