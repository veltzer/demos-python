#!/usr/bin/python3

'''
This is a simple example of how to use Scrapy

Note that this is an 'in code' running of scrapy which *does not*
use the scrapy(1) command line tool. This is an integrated way
of running scrapy from within your code. There is another way
of running scrapy when all you are doing is scraping with a full
project structure and all. This is not that way.
'''

import scrapy # for Spider, Request
import scrapy.crawler # for CrawlerProcess
 
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
    process=scrapy.crawler.CrawlerProcess()
    process.crawl(SearchSpider)
    process.start()
