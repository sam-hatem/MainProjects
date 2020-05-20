#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 17:10:21 2020

@author: sam
"""

import scrapy


#creating a spider 


class spiderOne(scrapy.Spider): 
    #1) name of spider
    name = "FirstSpider" 
    
    #2) request method
    def start_requests(self): 
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        #returning an interable of requests 
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    #3) parsign the requessts method 
    #response: instance of Textresponse holding the page content 
    def parse(self, response): 
        #scrapes the data as dicts and finds new urls to follow 
        #to create new request 
        #scraped data 
        page = response.url.split('/')[-2]
        filename = "quotes-%s.html" % page
        with open(filename, 'wb') as f: 
            f.write(response.body)
        self.log('Saved file %s' % filename)

#runing a spider 
        #go into project, go to spiders, on terminal run scrapy crawl <spidername> the name attribute of the spider !
        
        
# can just make a start_urls class attribute which will be used by the default implemtenation of stat_requests; parse is the default 
#callback method 