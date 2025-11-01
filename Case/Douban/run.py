from scrapy import cmdline

cmdline.execute('scrapy crawl douban -o doubantop250.json'.split())