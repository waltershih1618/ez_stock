import scrapy
import json


class StockSpider(scrapy.Spider):
    name = "stocks"

    def start_requests(self):
        urls = [
            'https://www.tpex.org.tw/web/stock/3insti/daily_trade/3itrade_hedge_result.php?l=zh-tw&o=json&se=EW&t=D&d=110/03/04&s=0,asc'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # stock[0] means stock code
    # stock[1] means stock name
    # stock[2] means foreign investors total buy
    # stock[3] means foreign investors total sell
    # stock[4] means foreign investors difference
    # stock[11] means securities investment trust companies total buy
    # stock[12] means securities investment trust companies total sell
    # stock[13] means securities investment trust companies difference
    # stock[20] means dealer total buy
    # stock[21] means dealer total sell
    # stock[22] means dealer total difference
    # stock[23] total difference

    def parse(self, response):
        with open('stock_list.json', 'r') as j:
            stock_list = json.loads(j.read())
            json_response = json.loads(response.body)            

            # print title
            print('{0:4} {1:4} {2:8} {3:8} {4:9} {5:8} {6:8} {7:9} {8:9} {9:9} {10:10} {11:8} '.format('股票','代號','外資買入','外資賣出','外資買賣超','投信買入','投信賣出','投信買賣超','自營商買入','自營商賣出','自營商買賣超','三大法人買賣超'))

            #print content
            for stock in (json_response['aaData']):
                if (stock[0] in stock_list):
                    print('{0:4} {1:6} {2:12} {3:12} {4:14} {5:12} {6:12} {7:14} {8:14} {9:14} {10:16} {11:16}'.format(stock[1], stock[0], stock[2], stock[3], stock[4], stock[11], stock[12], stock[13], stock[20], stock[21], stock[22], stock[23]))
                
    
                
            
        
    