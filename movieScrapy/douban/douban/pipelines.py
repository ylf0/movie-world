# -*- coding: utf-8 -*-
from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanPipeline(object):

    def __init__(self):
        dbargs = dict(
            host = '127.0.0.1',
            db = 'douban',
            user = 'root',
            passwd = '',
            cursorclass = MySQLdb.cursors.DictCursor,
            use_unicode = True,
        )
        self.dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)

    def process_item(self, item, spider):
        res = self.dbpool.runInteraction(self.insert_into_douban, item)
        return item

    def insert_into_douban(self, conn, item):
        conn.execute('insert into `movie`(`order`, `title`, `info`, `star`, `votes`, `quote`) values (%s,%s,%s,%s,%s,%s)',
        (item['order'],item['title'],item['info'],item['star'],item['votes'],item['quote']))

class MtimePipeline(object):

    def __init__(self):
        dbargs = dict(
            host = '127.0.0.1',
            db = 'douban',
            user = 'root',
            passwd = '',
            cursorclass = MySQLdb.cursors.DictCursor,
            use_unicode = True,
        )
        self.dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)

    def process_item(self, item, spider):
        res = self.dbpool.runInteraction(self.insert_into_poster, item)
        return item

    def insert_into_poster(self, conn, item):
        conn.execute('insert into `poster`(`title`, `poster_url`) values (%s, %s)', (item['title'], item['poster_url']))
