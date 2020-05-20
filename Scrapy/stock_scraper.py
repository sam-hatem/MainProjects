# -*- coding: utf-8 -*-
#can either extract html or css elements 

import scrapy 
import re 
from scrapy import Spider, Item, Field
from collections import defaultdict

# class ValuationItems(Item): 
#     #all the valuation measures 
#     cap = Field()
#     entr_value= Field()
#     trailing_pe = Field()
#     forward_pe = Field()
#     pe_growth = Field()
#     p/s= Field()
#     p/b = Field()
#     entr_value/rev = Field() 
#     entr_value/ebtida = Field()
    
    
# class price(Item):
#     beta = Field()
#     52_change = Field()
#     52_high = Field()
#     52_low = Field()
#     50_day_ma = Field() 
#     200_day_ma = Field()
    
# class share_stats(Item): 
#     avg_vol_3mo = Field()
#     avg_vol_10d = Field()
#     shares = Field() 
#     floa = Field() 
#     insider_pct = Field()
#     institution_pct = Field()
#     shares_short = Field() 
#     short_ratio = Field()
#     short_pct = Field() 
#     re.find

stock_list = ['GTX', 'XSPA', 'EBIX', 'DXLG', 'QMCO', 'OMF', 'GDOT', 'AGS',
        'FLDM', 'STIM', 'CSU', 'KEGXD', 'TUSK', 'MTDR', 'NBLX', 'RUTH',
        'PRTY', 'SITO', 'INAP', 'CHK', 'AXAS', 'KOS', 'ROSE', 'MMLP',
        'USCR', 'TTPH', 'ICD', 'NUS', 'NSP', 'CVNA', 'WHD', 'CORT',
        'HUD', 'TVTY']
class stockItem(Item): 
    
  
    stock_info = Field()
        
    
    
class spiderFinance(Spider): 
    #name of spider 
    name = "YahooStats"
    #settign allowed_domain
    allowed_domain = ["www.finance.yahoo.com"]
    start_urls = [
        "https://finance.yahoo.com/quote/{name}/key-statistics?p={name}"
        .format(name = name) for name in stock_list
    ]
    #parsing 
    def parse(self, response): 
        #parse and retuern objects
        #workign with the response object
        #stock title 
        
        item = stockItem()
        
        
        #item['stock_name'] = response.xpath("//title//text()").extract_first()
        #getting stock_info
        lst = response.xpath("//table//tbody//td[1]//text()").extract()
        lst1 = [x for x in lst if len(x) > 1]
        field_names = [x for x in lst1 if re.findall(r"^[^(]",x)]
        numbers = response.xpath("//table//tbody//td[2]//text()").extract()

        
        
        #dict of info 
        info = defaultdict(str)
        info['name'] = response.xpath("//title//text()").extract_first()
        for name,number in zip(field_names, numbers): 
            info[name] = number 
        
        item['stock_info'] = info
        #make sure to yield item 
        yield item
        
                
        
        
        
        
        
        
        
        
        