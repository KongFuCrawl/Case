# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# 管道1 - 存入mongodb数据库
import datetime
import pymongo
from .settings import *

class DoubanMongoPipeline:
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(host=MONGO_HOST, port=MONGO_PORT)
        self.db = self.client[MONGO_DB]
        self.myset = self.db[MONGO_SET]




    def process_item(self, item, spider):
        # 将 item 对象转换为字典
        item_dict = dict(item)
        # 可选：添加爬去时间
        item_dict['crawl_time'] = datetime.datetime.now()

        # 使用链接作为唯一标识去重
        self.myset.update_one(
            {'link': item['link']},  # 查询条件
            {'$set': item_dict},  # 更新数据
            upsert=True  # 如果不存在则插入
        )
        return item

