# -*- coding: utf-8 -*-

# Scrapy settings for weibo_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'weibo_spider'

SPIDER_MODULES = ['weibo_spider.spiders']
NEWSPIDER_MODULE = 'weibo_spider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'weibo_spider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

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
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'SINAGLOBAL=6361754581466.097.1538377265625; login_sid_t=751085a093893d41a4b9a08a1805801e; cross_origin_proto=SSL; _s_tentry=passport.weibo.com; Apache=4515391446731.273.1587185145869; ULV=1587185145876:9:1:1:4515391446731.273.1587185145869:1582020435566; WBStorage=42212210b087ca50|undefined; WBtopGlobal_register_version=fd6b3a12bb72ffed; ALF=1618721553; SSOLoginState=1587185554; SCF=AnqfGqBzx4It_kuOuM9ExXHyhYXSsbhvH67t6tvWtBEyLHwniFsmg7lnGR12NOHwE7UDc0qp5hkkZnDddrVa6Eg.; SUB=_2A25znvfCDeRhGeNL71EQ-SrKyzuIHXVQ6m4KrDV8PUNbmtANLU3hkW9NSRNTT5x5oVcvQR5tvSkAZVdY_orFL3Eu; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W53gydd22N8kBInCITyGTBS5JpX5KzhUgL.Fo-fShep1KBcehM2dJLoIpqN1K2pi--Xi-zRi-zcKgH0McLj9PS0; SUHB=0ftpkTUTCYiouf; UOR=www.anjian.com,widget.weibo.com,login.sina.com.cn',
    'Host': 's.weibo.com',
    'Referer': 'https://s.weibo.com/weibo/4AM?topnav=1&sudaref=login.sina.com.cn&page=2',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'weibo_spider.middlewares.WeiboSpiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'weibo_spider.middlewares.WeiboSpiderDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'weibo_spider.pipelines.WeiboSpiderPipeline': 300,
#}

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
