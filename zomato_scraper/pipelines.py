# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem


class DuplicatePipeline(object):

    def __init__(self):
        self.ids_seen = {}

    def process_item(self, item, spider):
        if item['id'] in self.ids_seen:
            raise DropItem('Duplicate item found: %s' % item['id'])
        else:
            self.ids_seen[item['id']] = None
            return item
