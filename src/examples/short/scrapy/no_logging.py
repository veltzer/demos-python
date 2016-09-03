#!/usr/bin/python3

'''
This example tries to show how to get ridd of the scrapy logging.

Notes:
- in order to disable scrapy logging you need to pass 'LOG_ENABLED':False
as a config option to the scrapy object. This will cause scrapy
to be totaly silent.
- if you still want to see some logs you need to configure python logging
with the logger name 'scrapy'.
- you also need to configure the logging level of your own spider (in
this example 'jetsearch'.
'''

import logging # for getLogger
import scrapy # for Spider, Request
import scrapy.crawler # for CrawlerProcess
 
logger=logging.getLogger(__name__)

class SearchSpider(scrapy.Spider):
    name = __name__
    allowed_domains = [
        'jet.com'
    ]
    start_urls = (
        'https://jet.com/search/',
    )
    ''' constructor '''
    def __init__(self, *args, **kwargs):
        # important, call the parent
        super(scrapy.Spider, self).__init__(*args, **kwargs)
        self.logger.info('in __init__')
    '''
    This method is called whenever you get a response
    '''
    def parse(self, response):
        self.logger.info('in parse')
    '''
    This method is called automatically when the crawler finishes
    '''
    def closed(self, reason):
        self.logger.info('in closed')

if __name__=='__main__':
    logging.getLogger('scrapy').setLevel(logging.WARN)
    logging.getLogger(__name__).setLevel(logging.WARN)
    process=scrapy.crawler.CrawlerProcess({
        'LOG_ENABLED': False,
    })
    process.crawl(SearchSpider)
    process.start()
