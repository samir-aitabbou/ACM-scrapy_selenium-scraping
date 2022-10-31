import scrapy
import time
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By


#webdriver with selenium 4
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


class ArticlesInfosSpider(scrapy.Spider):
    name = 'articles_infos'

    df = pd.read_csv('spiders/cleaned_links.csv')
    start_urls = df['links'] 

   
    def start_requests(self):
        headers= {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
        # for url in self.start_urls:
        #     yield scrapy.Request(url, headers=headers, callback=self.parse)
        yield scrapy.Request(start_urls[0], headers=headers, callback=self.parse)



            
    def parse(self, response):
        #print("****************************",response.request.url)
        #each url is gathered from response.request object
        driver.get(response.request.url)
        time.sleep(3)
            
        title = driver.find_element(By.XPATH,'//h1[@class="citation__title"]').text
        print("*****************",title)
        #  #Author name is taken here. Since there are multiple authors in some articles, these are lists of elements
        # author_name = driver.find_elements_by_xpath('//*[@class="author-data"]//*[@class="loa__author-name"]')
        # pub_date = driver.find_element_by_xpath('//span[@class="CitationCoverDate"]').text
        # citation = driver.find_element_by_xpath('//span[@class="citation"]//span').text
        # downloads = driver.find_element_by_xpath('//span[@class="metric"]//span').text
        # #Abstract of the article we have try except here since some of the articles does not have abstract and we set its initial value to none
        # abstract = "None"
        # try:
        #     abstract = driver.find_element_by_xpath('//div[@class="abstractSection abstractInFull"]//p').text
        # except:
        #     pass
        # dio = driver.find_element_by_xpath('//a[@class="issue-item__doi"]').text






        # #In order to reach the location info a button on the page must be triggered to fire embedded JavaScript code in order to 
        # #make the page generate a div element that contains location info
        # driver.execute_script("document.getElementsByClassName('show-hide-details u-font-sans')[0].click()")
        # time.sleep(1)
        # #Location is here. Since there are multiple contributing institutions in some articles, this is a list of elements
        # location = driver.find_elements_by_xpath('//*[contains(@class,"affiliation")]//dd')
        # #Empty arrays to be filled with texts stored in each element in the lists gathered above.
        # authors_firstname = []
        # authors_lastname = []
        # authors = []
        # # Necessary loops to extract texts from previously gathered lists and to be stored as array of texts.
        # for au in author_firstname:
        #     authors_firstname.append(au.text)
            
        # for au in author_lastname:
        #     authors_lastname.append(au.text)
            
        # for au in range(len(authors_firstname)):
        #     authors.append(authors_firstname[au]+" "+authors_lastname[au])
        
        # # Yielding takes place in each location element since we need our data to reflect number of contributions from countries among the world
        # for lo in location:
        #     country = lo.text.split(",")[-1].lstrip()
        #     yield {
        #         'title':title,
        #         'authors':authors,
        #         'abstract':abstract,
        #         'location':country
        #     }

