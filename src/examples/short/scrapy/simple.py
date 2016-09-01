#!/usr/bin/python3

'''
This is a simple example of how to use Scrapy
'''

import logging # for getLogger
import scrapy # for Spider, Request
import scrapy.crawler # for CrawlerProcess
 
logger=logging.getLogger(__name__)

class SearchSpider(scrapy.Spider):
    name = 'jetsearch'
    allowed_domains = [
        'jet.com'
    ]
    start_urls = (
        'https://jet.com/search/',
    )
    ''' constructor '''
    def __init__(self, *args, **kwargs):
        super(scrapy.Spider, self).__init__(*args, **kwargs)
    '''
    This method is called automatically when the crawler finishes
    '''
    def closed(self, reason):
        pass
    def parse(self, response):
        self.logger.info(response)


if __name__=='__main__':
    process=scrapy.crawler.CrawlerProcess()
    process.crawl(SearchSpider)
    process.start()
