import scrapy
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# webdriver with selenium 4
# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager
# #driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


class AcmSpider(scrapy.Spider):
    name = 'acm'
    
    start_urls = ['https://dl.acm.org/action/doSearch?AllField=blockchain&startPage=0&pageSize=50']

    
    
    def parse(self, response):
        for t in response.css('div.issue-item__detail'):
            text= t.css('a::text').get()
            print("********************************  ",text)
            yield{
                'link':text
            }
           
            
        next_page = response.xpath("//a[@class='pagination__btn--next']/@href").extract_first()
        if next_page is not None:
            yield scrapy.Request(next_page, callback=self.parse)