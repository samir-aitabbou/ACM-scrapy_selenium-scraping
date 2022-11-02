from itemadapter import ItemAdapter
import pymongo
from scrapy.conf import settings
from scrapy import log


class AcmPipeline:
    def process_item(self, item, spider):
        return item


class MongoDBPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]
    
    def process_item(self, item, spider):
       
        self.collection.insert(dict(item))
        log.msg("enregistrement added to MongoDB database!",level=log.DEBUG, spider=spider)
        return item