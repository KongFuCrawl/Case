# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from sre_constants import CHARSET
from venv import create

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# 管道1 ： 终端打印输出
class BooksPipeline:
    def process_item(self, item, spider):
        print(item['name'], item['price'])
        return item

# 管道2 ： 存入MYSQL数据库
# 提前建库建表
# create database booksdb charset utf8;
# use booksdb;
# create table bookstab(
# name varchar(200),
# price varchar(100),
# link varchar(300)
# )charset=utf8;


import pymysql
from .settings import *

class BooksMYSQLPipeline:
    def open_spider(self, spider):
        """爬虫程序开始时，只执行一次，一般用于数据库的连接"""
        self.db = pymysql.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PWD,
            database=MYSQL_DB,

        )
        self.cur = self.db.cursor()

    def process_item(self, item, spider):
        ins = 'INSERT INTO bookstab (name, price, link) VALUES (%s,%s,%s)'
        li = [
            item.get('name', '').strip() if item.get('name') else "",
            item.get('price', '').strip() if item.get('price') else '',
            item.get('link', '').strip() if item.get('link') else '',
        ]
        try:
            self.cur.execute(ins, li)
            # 提交到数据库执行
            self.db.commit()
        except Exception as e:

            self.db.rollback()

        return item

    def close_spider(self, spider):
        """爬虫程序结束时，只执行一次，一般用于数据的断开"""
        self.cur.close()
        self.db.close()


# 管道3 - 存入MongoDB数据库管道
import pymongo
class BooksMongoDBPipeline:
    def open_spider(self, spider):
        """连接mongodb"""
        self.client = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
        self.db = self.client[MONGO_DB]
        self.myset = self.db[MONGO_SET]

    def process_item(self, item, spider):
        d = dict(item)
        self.myset.insert_one(d)

        return item











