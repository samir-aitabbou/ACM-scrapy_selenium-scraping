BOT_NAME = 'Acm'
SPIDER_MODULES = ['Acm.spiders']
NEWSPIDER_MODULE = 'Acm.spiders'
ROBOTSTXT_OBEY = False
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
DUPEFILTER_CLASS = 'scrapy.dupefilters.BaseDupeFilter'


# MongoDb Configuration

# ITEM_PIPELINES = ['Acm.pipelines.MongoDBPipeline', ]

# MONGODB_SERVER = "localhost"
# MONGODB_PORT = 27017
# MONGODB_DB = "stackoverflow"
# MONGODB_COLLECTION = "questions"
