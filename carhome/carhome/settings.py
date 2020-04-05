# -*- coding: utf-8 -*-
import os
# Scrapy settings for carhome project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'carhome'

SPIDER_MODULES = ['carhome.spiders']
NEWSPIDER_MODULE = 'carhome.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'carhome (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'User-Agent':  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'Host': 'car.autohome.com.cn',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
  'cookie': 'fvlid=158566178748823mAftgkef; sessionid=4BAEA1F7-CF49-4895-9519-127B1C5F28D5%7C%7C2020-03-31+21%3A36%3A28.603%7C%7Cwww.baidu.com; autoid=33c2a4eb3f087f9b6c7288209f987f3e; area=330110; ahpau=1; sessionuid=4BAEA1F7-CF49-4895-9519-127B1C5F28D5%7C%7C2020-03-31+21%3A36%3A28.603%7C%7Cwww.baidu.com; __ah_uuid_ng=c_4BAEA1F7-CF49-4895-9519-127B1C5F28D5; sessionip=115.204.173.248; Hm_lvt_9924a05a5a75caf05dbbfb51af638b07=1585796147,1585902231,1585967745,1586052666; FromPicList=0; sessionvid=43AA78E0-5569-43BC-8EE9-039B7E927775; pvidchain=2042222,2042222; ahpvno=37; Hm_lpvt_9924a05a5a75caf05dbbfb51af638b07=1586095684; v_no=3; visit_info_ad=4BAEA1F7-CF49-4895-9519-127B1C5F28D5||43AA78E0-5569-43BC-8EE9-039B7E927775||-1||-1||3; ref=www.baidu.com%7C0%7C0%7C0%7C2020-04-05+22%3A08%3A05.769%7C2020-03-31+21%3A36%3A28.603; ahrlid=1586095684109DGO4fSVreo-1586095688867'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'carhome.middlewares.CarhomeSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'carhome.middlewares.CarhomeDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'carhome.pipelines.BMWImagesPipeline': 1,
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

IMAGES_STORE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')